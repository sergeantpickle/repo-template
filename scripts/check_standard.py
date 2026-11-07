#!/usr/bin/env python3
import json
import re
import subprocess
import urllib.parse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
RULE_ID = re.compile(r"^RGS-[A-Z]+(?:-[A-Z]+)*-\d{3}$")

REQUIRED = [
  "README.md",
  "AGENTS.md",
  "STANDARD.md",
  "VERSION",
  "CHANGELOG.md",
  "rules.json",
  "action.yml",
  "docs/README.md",
  "docs/adoption.md",
  "docs/audit.md",
  "docs/lifecycle.md",
  "docs/routing.md",
  "docs/growth.md",
  "docs/examples.md",
  "docs/evidence.md",
  "examples/README.md",
  "examples/seed-to-mature.md",
  "examples/starting-at-twenty.md",
  "examples/recovering-from-sprawl.md",
  "examples/project-map.md",
  "examples/organization-scale.md",
  "examples/github-actions/repo-standard.yml",
  "starter/README.md",
  "starter/AGENTS.md",
  "starter/.repo-standard.json",
  "scripts/audit_project.py",
  "scripts/check_latest.py",
  "scripts/init_project.py",
  "tests/test_audit_project.py",
  "tests/test_check_latest.py",
  "tests/test_init_project.py",
]


def load_json(path, errors, label):
  try:
    return json.loads(path.read_text(encoding="utf-8"))
  except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"{label} is invalid JSON: {exc}")
    return None


MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_internal_links(errors):
  for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
      continue
    text = path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(text):
      target = raw_target.strip().split()[0].strip("<>")
      if not target or target.startswith("#"):
        continue
      parsed = urllib.parse.urlparse(target)
      if parsed.scheme or parsed.netloc:
        continue
      relative_target = urllib.parse.unquote(parsed.path)
      if not relative_target:
        continue
      destination = (path.parent / relative_target).resolve()
      try:
        destination.relative_to(ROOT.resolve())
      except ValueError:
        errors.append(
          f"{path.relative_to(ROOT)} links outside the repository: {target}"
        )
        continue
      if not destination.exists():
        errors.append(
          f"{path.relative_to(ROOT)} has broken internal link: {target}"
        )


def main():
  errors = []

  for relative in REQUIRED:
    if not (ROOT / relative).is_file():
      errors.append(f"missing required standard file: {relative}")

  check_internal_links(errors)

  version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").is_file() else ""
  if not SEMVER.fullmatch(version):
    errors.append("VERSION must contain MAJOR.MINOR.PATCH")

  rules_data = load_json(ROOT / "rules.json", errors, "rules.json") if (ROOT / "rules.json").is_file() else None
  rule_ids = set()
  if rules_data:
    if rules_data.get("standard_version") != version:
      errors.append("rules.json standard_version does not match VERSION")
    for rule in rules_data.get("rules", []):
      rule_id = rule.get("id")
      if not isinstance(rule_id, str) or not RULE_ID.fullmatch(rule_id):
        errors.append(f"invalid rule ID: {rule_id!r}")
        continue
      if rule_id in rule_ids:
        errors.append(f"duplicate rule ID: {rule_id}")
      rule_ids.add(rule_id)
      if rule.get("level") not in {"required", "recommended", "advisory"}:
        errors.append(f"invalid level for {rule_id}")
      if rule.get("detection") not in {"mechanical", "heuristic", "manual"}:
        errors.append(f"invalid detection class for {rule_id}")
      document = rule.get("document")
      if not isinstance(document, str) or not (ROOT / document).is_file():
        errors.append(f"rule {rule_id} references missing document: {document!r}")
      else:
        document_text = (ROOT / document).read_text(encoding="utf-8")
        if rule_id not in document_text:
          errors.append(
            f"rule {rule_id} is not present in its declared canonical document: {document}"
          )

  if version:
    standard = (ROOT / "STANDARD.md").read_text(encoding="utf-8") if (ROOT / "STANDARD.md").is_file() else ""
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").is_file() else ""
    if f"Version: **{version}**" not in standard:
      errors.append("STANDARD.md version does not match VERSION")
    if f"## {version} " not in changelog:
      errors.append("CHANGELOG.md has no entry for VERSION")

  manifest_path = ROOT / "starter/.repo-standard.json"
  manifest = load_json(manifest_path, errors, "starter manifest") if manifest_path.is_file() else None
  if manifest and manifest.get("version") != version:
    errors.append("starter manifest version must match VERSION")

  action_path = ROOT / "action.yml"
  if action_path.is_file():
    action_text = action_path.read_text(encoding="utf-8")
    if "actions/setup-python@v7" not in action_text:
      errors.append("action.yml must set up Python explicitly")
    if "--require-version-match" not in action_text:
      errors.append("action.yml must require the pinned auditor to match the adopted standard version")

  docs_index = ROOT / "docs/README.md"
  if docs_index.is_file():
    text = docs_index.read_text(encoding="utf-8")
    for link in ["adoption.md", "audit.md", "lifecycle.md", "routing.md", "growth.md", "examples.md", "evidence.md"]:
      if f"({link})" not in text:
        errors.append(f"docs/README.md does not link {link}")

  if not errors:
    test_result = subprocess.run(
      [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
      cwd=ROOT,
      capture_output=True,
      text=True,
      check=False,
    )
    if test_result.returncode != 0:
      errors.append("unit tests failed:\n" + test_result.stdout + test_result.stderr)

  if not errors:
    audit_result = subprocess.run(
      [sys.executable, str(ROOT / "scripts/audit_project.py"), str(ROOT / "starter"), "--strict"],
      cwd=ROOT,
      capture_output=True,
      text=True,
      check=False,
    )
    if audit_result.returncode != 0:
      errors.append("starter audit failed:\n" + audit_result.stdout + audit_result.stderr)

  if errors:
    print("Standard check failed:")
    for error in errors:
      print(f"- {error}")
    return 1

  print(f"Standard check passed (version {version}).")
  return 0


if __name__ == "__main__":
  sys.exit(main())
