#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STANDARD_VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
RULES_PATH = ROOT / "rules.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_rules():
  data = json.loads(RULES_PATH.read_text(encoding="utf-8"))
  return {rule["id"]: rule for rule in data["rules"]}


def normalize_source(source):
  if not isinstance(source, str) or not source.strip():
    raise ValueError("source must be a non-empty string")
  value = source.strip()
  parsed = urllib.parse.urlparse(value)
  if parsed.scheme == "https" and parsed.netloc.lower() == "github.com":
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) == 2:
      owner, repository = parts
      if repository.endswith(".git"):
        repository = repository[:-4]
      if owner and repository:
        return f"https://github.com/{owner.lower()}/{repository.lower()}"
  return value.rstrip("/")


def load_manifest(project, pre_adoption=False):
  path = project / ".repo-standard.json"
  if not path.is_file():
    if pre_adoption:
      return None, []
    return None, [{"code": "manifest-missing", "message": f"missing alignment manifest: {path.name}"}]
  try:
    return json.loads(path.read_text(encoding="utf-8")), []
  except (OSError, json.JSONDecodeError) as exc:
    return None, [{"code": "manifest-invalid", "message": f"invalid alignment manifest: {exc}"}]


def validate_exceptions(manifest, rules):
  errors = []
  warnings = []
  exceptions = {}
  raw = manifest.get("exceptions", {})
  if not isinstance(raw, dict):
    return {}, [{"code": "exceptions-invalid", "message": "manifest exceptions must be an object keyed by rule ID"}], []

  today = dt.date.today()
  for rule_id, value in raw.items():
    rule = rules.get(rule_id)
    if rule is None:
      errors.append({"code": "exception-unknown-rule", "message": f"exception references unknown rule ID: {rule_id}"})
      continue
    if not rule.get("exception_allowed", False):
      errors.append({"code": "exception-not-allowed", "message": f"rule does not allow exceptions: {rule_id}"})
      continue
    if not isinstance(value, dict):
      errors.append({"code": "exception-invalid", "message": f"exception {rule_id} must be an object"})
      continue
    reason = value.get("reason")
    if not isinstance(reason, str) or not reason.strip():
      errors.append({"code": "exception-reason-missing", "message": f"exception {rule_id} requires a non-empty reason"})
      continue
    review_after = value.get("review_after")
    if review_after is not None:
      if not isinstance(review_after, str) or not DATE.fullmatch(review_after):
        errors.append({"code": "exception-review-date-invalid", "message": f"exception {rule_id} review_after must be YYYY-MM-DD"})
        continue
      try:
        review_date = dt.date.fromisoformat(review_after)
      except ValueError:
        errors.append({"code": "exception-review-date-invalid", "message": f"exception {rule_id} has an invalid review_after date"})
        continue
      if review_date < today:
        rule_meta = rules["RGS-EXCEPT-001"]
        warnings.append({
          "id": "RGS-EXCEPT-001",
          "level": "warning",
          "rule_level": rule_meta["level"],
          "detection": rule_meta["detection"],
          "status": "active",
          "message": f"exception {rule_id} passed its review_after date {review_after}",
          "paths": [".repo-standard.json"],
        })
    exceptions[rule_id] = value
  return exceptions, errors, warnings


def heading_hits(path, terms):
  if not path.is_file():
    return []
  hits = []
  for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
    stripped = line.lstrip()
    if not stripped.startswith("#"):
      continue
    heading = stripped.lstrip("# ").strip().lower()
    if any(term in heading for term in terms):
      hits.append(line.strip())
  return hits


def normalized_digest(path):
  text = path.read_text(encoding="utf-8", errors="replace")
  lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
  normalized = "\n".join(lines).strip() + "\n"
  return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def add_finding(findings, exceptions, rules, rule_id, level, message, paths=None):
  exception = exceptions.get(rule_id)
  status = "excepted" if exception else "active"
  rule = rules[rule_id]
  finding = {
    "id": rule_id,
    "level": level,
    "rule_level": rule["level"],
    "detection": rule["detection"],
    "status": status,
    "message": message,
    "paths": paths or [],
  }
  if exception:
    finding["exception"] = exception
  findings.append(finding)


SKIP_INSTRUCTION_DIRS = {
  ".git",
  ".hg",
  ".svn",
  ".venv",
  "venv",
  "node_modules",
  "vendor",
  "dist",
  "build",
  "target",
  "__pycache__",
}


def discover_instruction_files(project):
  found = []
  for root, dirs, files in os.walk(project):
    dirs[:] = [name for name in dirs if name not in SKIP_INSTRUCTION_DIRS]
    root_path = Path(root)
    for name in files:
      path = root_path / name
      if path.is_symlink():
        continue
      relative = path.relative_to(project)
      if name in {"AGENTS.md", "CLAUDE.md", "GEMINI.md"}:
        found.append(path)
      elif relative.as_posix() == ".github/copilot-instructions.md":
        found.append(path)
  return sorted(found)


def duplicate_instruction_groups(paths):
  groups = {}
  for path in paths:
    groups.setdefault(normalized_digest(path), []).append(path)
  return [group for group in groups.values() if len(group) > 1]


def is_pointer_adapter(path, canonical):
  if path == canonical or not canonical.is_file():
    return False
  text = path.read_text(encoding="utf-8", errors="replace").strip()
  if not text or len(text) > 512:
    return False
  nonblank = [line.strip() for line in text.splitlines() if line.strip()]
  if len(nonblank) > 5:
    return False
  lowered = text.lower()
  return "agents.md" in lowered and (
    text == "@AGENTS.md"
    or text == "@agents.md"
    or "read agents.md" in lowered
    or "follow agents.md" in lowered
    or "see agents.md" in lowered
  )


def is_generated_adapter(path, canonical):
  if path == canonical or not canonical.is_file():
    return False
  adapter_text = path.read_text(encoding="utf-8", errors="replace")
  header = "\n".join(adapter_text.splitlines()[:40]).lower()
  generated_marker = (
    "generated file" in header
    or "do not edit by hand" in header
    or "generated from agents.md" in header
  )
  if not generated_marker:
    return False
  canonical_text = canonical.read_text(encoding="utf-8", errors="replace").strip()
  return bool(canonical_text) and canonical_text in adapter_text


def audit(
  project,
  pre_adoption=False,
  require_version_match=False,
  require_source=None,
):
  rules = load_rules()
  errors = []
  findings = []
  manifest, manifest_errors = load_manifest(project, pre_adoption=pre_adoption)
  errors.extend(manifest_errors)
  exceptions = {}

  if manifest is not None:
    schema_version = manifest.get("schema_version")
    if schema_version != 1:
      errors.append({
        "code": "manifest-schema-unsupported",
        "message": "alignment manifest schema_version must be 1",
      })
    source = manifest.get("source")
    adopted = manifest.get("version")
    last_checked = manifest.get("last_checked")
    try:
      normalized_source = normalize_source(source)
    except ValueError:
      normalized_source = None
      errors.append({"code": "manifest-source-invalid", "message": "manifest source must be a non-empty string"})
    if require_source is not None and normalized_source is not None:
      try:
        normalized_required_source = normalize_source(require_source)
      except ValueError:
        errors.append({"code": "auditor-source-invalid", "message": "required auditor source is invalid"})
      else:
        if normalized_source != normalized_required_source:
          errors.append({
            "code": "auditor-source-mismatch",
            "message": (
              f"project records source {source!r} but the pinned auditor source is "
              f"{require_source!r}"
            ),
          })
    if not isinstance(adopted, str) or not SEMVER.fullmatch(adopted):
      errors.append({"code": "manifest-version-invalid", "message": "manifest version must use MAJOR.MINOR.PATCH"})
    elif adopted != STANDARD_VERSION:
      findings.append({
        "id": "standard-version-drift",
        "level": "info",
        "status": "active",
        "message": f"project last aligned to {adopted}; this auditor checkout is {STANDARD_VERSION}",
        "paths": [".repo-standard.json"],
      })
      if require_version_match:
        errors.append({
          "code": "auditor-version-mismatch",
          "message": f"project last aligned to {adopted} but the pinned auditor is {STANDARD_VERSION}",
        })
    if last_checked is not None:
      if not isinstance(last_checked, str) or not DATE.fullmatch(last_checked):
        errors.append({"code": "manifest-last-checked-invalid", "message": "last_checked must be null or YYYY-MM-DD"})
      else:
        try:
          dt.date.fromisoformat(last_checked)
        except ValueError:
          errors.append({"code": "manifest-last-checked-invalid", "message": "last_checked is not a valid calendar date"})
    exceptions, exception_errors, exception_warnings = validate_exceptions(manifest, rules)
    errors.extend(exception_errors)
    findings.extend(exception_warnings)

  readme_hits = heading_hits(
    project / "README.md",
    ["handoff", "current state", "next steps", "progress", "work log", "development log", "implementation status", "blockers"],
  )
  if readme_hits:
    add_finding(
      findings,
      exceptions,
      rules,
      "RGS-ROUTE-README-001",
      "warning",
      "README contains headings commonly associated with active work or handoff state: " + ", ".join(readme_hits),
      ["README.md"],
    )

  changelog_hits = heading_hits(
    project / "CHANGELOG.md",
    ["handoff", "current state", "next steps", "progress", "blockers", "work log", "development log", "todo"],
  )
  if changelog_hits:
    add_finding(
      findings,
      exceptions,
      rules,
      "RGS-ROUTE-CHANGELOG-001",
      "warning",
      "CHANGELOG contains headings commonly associated with active work: " + ", ".join(changelog_hits),
      ["CHANGELOG.md"],
    )

  if (project / "HANDOFF.md").is_file():
    add_finding(
      findings,
      exceptions,
      rules,
      "RGS-ROUTE-HANDOFF-001",
      "warning",
      "root HANDOFF.md is a broad singleton; verify that its scope and retirement boundary are explicit",
      ["HANDOFF.md"],
    )

  buckets = [name for name in ["NOTES.md", "LOG.md"] if (project / name).is_file()]
  if buckets:
    add_finding(
      findings,
      exceptions,
      rules,
      "RGS-ROUTE-BUCKET-001",
      "warning",
      "generic root buckets need bounded ownership: " + ", ".join(buckets),
      buckets,
    )

  root_instruction_paths = [
    project / "AGENTS.md",
    project / "CLAUDE.md",
    project / "GEMINI.md",
    project / ".github/copilot-instructions.md",
  ]
  root_instruction_files = [path for path in root_instruction_paths if path.is_file() and not path.is_symlink()]
  canonical_agents = project / "AGENTS.md"
  managed_adapters = {
    path
    for path in root_instruction_files
    if (
      is_generated_adapter(path, canonical_agents)
      or is_pointer_adapter(path, canonical_agents)
    )
  }
  unmanaged_root_files = [
    path
    for path in root_instruction_files
    if path not in managed_adapters
  ]
  if len(unmanaged_root_files) > 1:
    digests = {normalized_digest(path) for path in unmanaged_root_files}
    if len(digests) == 1:
      message = "multiple independent root instruction files contain the same content; copies can drift unless generated, linked, or checked"
    else:
      message = "multiple independent root instruction files differ; verify that differences are intentionally tool-specific rather than unmanaged drift"
    add_finding(
      findings,
      exceptions,
      rules,
      "RGS-INSTR-002",
      "warning",
      message,
      [str(path.relative_to(project)) for path in unmanaged_root_files],
    )

  all_instruction_files = discover_instruction_files(project)
  root_set = set(root_instruction_files)
  for group in duplicate_instruction_groups(all_instruction_files):
    if set(group).issubset(root_set):
      continue
    add_finding(
      findings,
      exceptions,
      rules,
      "RGS-INSTR-002",
      "warning",
      "identical instruction content is independently copied across repository scopes; verify intentional inheritance or generate/link/check the copies",
      [str(path.relative_to(project)) for path in group],
    )

  agent_hits = heading_hits(
    project / "AGENTS.md",
    ["current state", "next steps", "progress", "blockers", "handoff", "implementation status"],
  )
  if agent_hits:
    add_finding(
      findings,
      exceptions,
      rules,
      "RGS-INSTR-001",
      "warning",
      "AGENTS.md contains headings commonly associated with active task state: " + ", ".join(agent_hits),
      ["AGENTS.md"],
    )

  return {
    "schema_version": 1,
    "project": str(project),
    "standard_version": STANDARD_VERSION,
    "alignment_status": "aligned" if manifest is not None else "pre-alignment",
    "errors": errors,
    "findings": findings,
    "exceptions": exceptions,
  }


def text_report(result):
  lines = [
    f"Repository Growth Standard audit: {result['project']}",
    f"Standard checkout: {result['standard_version']}",
    f"Alignment status: {result['alignment_status']}",
  ]
  for error in result["errors"]:
    lines.append(f"ERROR [{error['code']}]: {error['message']}")
  for finding in result["findings"]:
    prefix = "EXCEPT" if finding["status"] == "excepted" else finding["level"].upper()
    line = f"{prefix} [{finding['id']}]: {finding['message']}"
    if finding["status"] == "excepted":
      line += f" | reason: {finding['exception']['reason']}"
    lines.append(line)
  if not result["errors"] and not result["findings"]:
    lines.append("No findings.")
  return "\n".join(lines)


def exit_code(result, strict):
  if result["errors"]:
    return 1
  if strict and any(finding["status"] == "active" and finding["level"] == "warning" for finding in result["findings"]):
    return 1
  return 0


def main():
  parser = argparse.ArgumentParser(description="Audit a project against this checkout of the Repository Growth Standard.")
  parser.add_argument("project", nargs="?", default=".", help="project directory to audit")
  parser.add_argument("--strict", action="store_true", help="treat active warnings as failures")
  parser.add_argument("--pre-adoption", action="store_true", help="allow auditing a repository that has not adopted the standard yet")
  parser.add_argument("--require-version-match", action="store_true", help="fail when the project version differs from this auditor checkout")
  parser.add_argument("--require-source", help="fail when the manifest source does not match this auditor source")
  parser.add_argument("--format", choices=["text", "json"], default="text", help="report format")
  args = parser.parse_args()

  project = Path(args.project).resolve()
  if not project.is_dir():
    print(f"error: not a directory: {project}", file=sys.stderr)
    return 2

  result = audit(
    project,
    pre_adoption=args.pre_adoption,
    require_version_match=args.require_version_match,
    require_source=args.require_source,
  )
  if args.format == "json":
    print(json.dumps(result, indent=2, sort_keys=True))
  else:
    print(text_report(result))
  return exit_code(result, args.strict)


if __name__ == "__main__":
  sys.exit(main())
