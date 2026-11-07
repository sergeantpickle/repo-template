#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STANDARD_VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
RULES_PATH = ROOT / "rules.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_rules():
  data = json.loads(RULES_PATH.read_text(encoding="utf-8"))
  return {rule["id"]: rule for rule in data["rules"]}


def load_manifest(project):
  path = project / ".repo-standard.json"
  if not path.is_file():
    return None, [{"code": "manifest-missing", "message": f"missing adoption manifest: {path.name}"}]
  try:
    return json.loads(path.read_text(encoding="utf-8")), []
  except (OSError, json.JSONDecodeError) as exc:
    return None, [{"code": "manifest-invalid", "message": f"invalid adoption manifest: {exc}"}]


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
        warnings.append({
          "id": "RGS-EXCEPT-001",
          "level": "warning",
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


def add_finding(findings, exceptions, rule_id, level, message, paths=None):
  exception = exceptions.get(rule_id)
  status = "excepted" if exception else "active"
  finding = {
    "id": rule_id,
    "level": level,
    "status": status,
    "message": message,
    "paths": paths or [],
  }
  if exception:
    finding["exception"] = exception
  findings.append(finding)


def audit(project):
  rules = load_rules()
  errors = []
  findings = []
  manifest, manifest_errors = load_manifest(project)
  errors.extend(manifest_errors)
  exceptions = {}

  if manifest is not None:
    source = manifest.get("source")
    adopted = manifest.get("version")
    last_checked = manifest.get("last_checked")
    if not isinstance(source, str) or not source.strip():
      errors.append({"code": "manifest-source-invalid", "message": "manifest source must be a non-empty string"})
    if not isinstance(adopted, str) or not SEMVER.fullmatch(adopted):
      errors.append({"code": "manifest-version-invalid", "message": "manifest version must use MAJOR.MINOR.PATCH"})
    elif adopted != STANDARD_VERSION:
      findings.append({
        "id": "standard-version-drift",
        "level": "info",
        "status": "active",
        "message": f"project adopts {adopted}; this checkout of the standard is {STANDARD_VERSION}",
        "paths": [".repo-standard.json"],
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
      "RGS-ROUTE-CHANGELOG-001",
      "warning",
      "CHANGELOG contains headings commonly associated with active work: " + ", ".join(changelog_hits),
      ["CHANGELOG.md"],
    )

  if (project / "HANDOFF.md").is_file():
    add_finding(
      findings,
      exceptions,
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
      "RGS-ROUTE-BUCKET-001",
      "warning",
      "generic root buckets need bounded ownership: " + ", ".join(buckets),
      buckets,
    )

  instruction_paths = [
    project / "AGENTS.md",
    project / "CLAUDE.md",
    project / "GEMINI.md",
    project / ".github/copilot-instructions.md",
  ]
  instruction_files = [path for path in instruction_paths if path.is_file() and not path.is_symlink()]
  if len(instruction_files) > 1:
    digests = {normalized_digest(path) for path in instruction_files}
    if len(digests) == 1:
      message = "multiple independent root instruction files contain the same content; copies can drift unless generated, linked, or checked"
    else:
      message = "multiple independent root instruction files differ; verify that differences are intentionally tool-specific rather than unmanaged drift"
    add_finding(
      findings,
      exceptions,
      "RGS-INSTR-002",
      "warning",
      message,
      [str(path.relative_to(project)) for path in instruction_files],
    )

  agent_hits = heading_hits(
    project / "AGENTS.md",
    ["current state", "next steps", "progress", "blockers", "handoff", "implementation status"],
  )
  if agent_hits:
    add_finding(
      findings,
      exceptions,
      "RGS-INSTR-001",
      "warning",
      "AGENTS.md contains headings commonly associated with active task state: " + ", ".join(agent_hits),
      ["AGENTS.md"],
    )

  return {
    "project": str(project),
    "standard_version": STANDARD_VERSION,
    "errors": errors,
    "findings": findings,
    "exceptions": exceptions,
  }


def text_report(result):
  lines = [
    f"Repository Growth Standard audit: {result['project']}",
    f"Standard checkout: {result['standard_version']}",
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
  parser.add_argument("--format", choices=["text", "json"], default="text", help="report format")
  args = parser.parse_args()

  project = Path(args.project).resolve()
  if not project.is_dir():
    print(f"error: not a directory: {project}", file=sys.stderr)
    return 2

  result = audit(project)
  if args.format == "json":
    print(json.dumps(result, indent=2, sort_keys=True))
  else:
    print(text_report(result))
  return exit_code(result, args.strict)


if __name__ == "__main__":
  sys.exit(main())
