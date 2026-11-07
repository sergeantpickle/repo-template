#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STANDARD_VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def load_manifest(project: Path):
  path = project / ".repo-standard.json"
  if not path.is_file():
    return None, [f"missing adoption manifest: {path.name}"]
  try:
    data = json.loads(path.read_text(encoding="utf-8"))
  except (OSError, json.JSONDecodeError) as exc:
    return None, [f"invalid adoption manifest: {exc}"]
  return data, []


def exception_set(manifest):
  raw = manifest.get("exceptions", {}) if manifest else {}
  if isinstance(raw, dict):
    return set(raw)
  return set()


def add_warning(warnings, exceptions, rule_id, message):
  if rule_id not in exceptions:
    warnings.append((rule_id, message))


def heading_smells(path: Path, terms):
  if not path.is_file():
    return []
  hits = []
  for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
    if not line.lstrip().startswith("#"):
      continue
    heading = line.lstrip("# ").strip().lower()
    for term in terms:
      if term in heading:
        hits.append(line.strip())
        break
  return hits


def audit(project: Path):
  errors = []
  warnings = []
  manifest, manifest_errors = load_manifest(project)
  errors.extend(manifest_errors)
  exceptions = exception_set(manifest)

  if manifest:
    source = manifest.get("source")
    adopted = manifest.get("version")
    exceptions_raw = manifest.get("exceptions")
    if not isinstance(source, str) or not source.strip():
      errors.append("manifest source must be a non-empty string")
    if not isinstance(adopted, str) or not SEMVER.fullmatch(adopted):
      errors.append("manifest version must use MAJOR.MINOR.PATCH")
    elif adopted != STANDARD_VERSION:
      add_warning(
        warnings,
        exceptions,
        "standard-version-drift",
        f"project adopts {adopted}; this checkout of the standard is {STANDARD_VERSION}",
      )
    if not isinstance(exceptions_raw, dict):
      errors.append("manifest exceptions must be an object mapping rule ids to reasons")
    elif any(not isinstance(v, str) or not v.strip() for v in exceptions_raw.values()):
      errors.append("every manifest exception must have a non-empty string reason")

  readme_hits = heading_smells(
    project / "README.md",
    ["handoff", "current state", "next steps", "progress", "work log", "development log", "implementation status"],
  )
  if readme_hits:
    add_warning(
      warnings,
      exceptions,
      "readme-routing-smell",
      "README contains headings commonly associated with active work/history: " + ", ".join(readme_hits),
    )

  changelog_hits = heading_smells(
    project / "CHANGELOG.md",
    ["handoff", "current state", "next steps", "progress", "blockers", "work log", "development log"],
  )
  if changelog_hits:
    add_warning(
      warnings,
      exceptions,
      "changelog-routing-smell",
      "CHANGELOG contains headings commonly associated with active work: " + ", ".join(changelog_hits),
    )

  for filename, rule_id in [
    ("HANDOFF.md", "singleton-handoff"),
    ("NOTES.md", "generic-notes"),
    ("LOG.md", "generic-log"),
  ]:
    if (project / filename).is_file():
      add_warning(
        warnings,
        exceptions,
        rule_id,
        f"{filename} is a broad singleton bucket; verify that its responsibility is bounded and unambiguous",
      )

  instruction_paths = [
    project / "AGENTS.md",
    project / "CLAUDE.md",
    project / "GEMINI.md",
    project / ".github/copilot-instructions.md",
  ]
  instruction_files = [p for p in instruction_paths if p.is_file() and not p.is_symlink()]
  if len(instruction_files) > 1:
    add_warning(
      warnings,
      exceptions,
      "instruction-copy-drift",
      "multiple independent root instruction surfaces can drift: "
      + ", ".join(str(p.relative_to(project)) for p in instruction_files),
    )

  agents = project / "AGENTS.md"
  if agents.is_file():
    line_count = len(agents.read_text(encoding="utf-8", errors="replace").splitlines())
    if line_count > 200:
      add_warning(
        warnings,
        exceptions,
        "large-agents-file",
        f"AGENTS.md is {line_count} lines; review whether narrower rules/procedures can load on demand",
      )

  return errors, warnings


def main():
  parser = argparse.ArgumentParser(description="Audit a project against this checkout of the Repository Growth Standard.")
  parser.add_argument("project", nargs="?", default=".", help="project directory to audit")
  parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
  args = parser.parse_args()

  project = Path(args.project).resolve()
  if not project.is_dir():
    print(f"error: not a directory: {project}")
    return 2

  errors, warnings = audit(project)
  print(f"Repository Growth Standard audit: {project}")
  print(f"Upstream version: {STANDARD_VERSION}")

  for message in errors:
    print(f"ERROR: {message}")
  for rule_id, message in warnings:
    print(f"WARN [{rule_id}]: {message}")

  if not errors and not warnings:
    print("No findings.")

  if errors:
    return 1
  if warnings and args.strict:
    return 1
  return 0


if __name__ == "__main__":
  sys.exit(main())
