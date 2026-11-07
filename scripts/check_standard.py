#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

REQUIRED = [
  "README.md",
  "AGENTS.md",
  "STANDARD.md",
  "VERSION",
  "CHANGELOG.md",
  "docs/README.md",
  "docs/adoption.md",
  "docs/routing.md",
  "docs/growth.md",
  "docs/examples.md",
  "docs/evidence.md",
  "starter/README.md",
  "starter/AGENTS.md",
  "starter/.repo-standard.json",
  "scripts/audit_project.py",
]


def main():
  errors = []

  for relative in REQUIRED:
    if not (ROOT / relative).is_file():
      errors.append(f"missing required standard file: {relative}")

  version_path = ROOT / "VERSION"
  version = version_path.read_text(encoding="utf-8").strip() if version_path.is_file() else ""
  if not SEMVER.fullmatch(version):
    errors.append("VERSION must contain MAJOR.MINOR.PATCH")

  if version:
    standard = (ROOT / "STANDARD.md").read_text(encoding="utf-8") if (ROOT / "STANDARD.md").is_file() else ""
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").is_file() else ""
    if f"Version: **{version}**" not in standard:
      errors.append("STANDARD.md version does not match VERSION")
    if f"## {version} " not in changelog:
      errors.append("CHANGELOG.md has no entry for VERSION")

    manifest_path = ROOT / "starter/.repo-standard.json"
    if manifest_path.is_file():
      try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
      except json.JSONDecodeError as exc:
        errors.append(f"starter manifest is invalid JSON: {exc}")
      else:
        if manifest.get("version") != version:
          errors.append("starter manifest version does not match VERSION")

  docs_index = ROOT / "docs/README.md"
  if docs_index.is_file():
    text = docs_index.read_text(encoding="utf-8")
    for link in ["adoption.md", "routing.md", "growth.md", "examples.md", "evidence.md"]:
      if f"({link})" not in text:
        errors.append(f"docs/README.md does not link {link}")

  if not errors:
    result = subprocess.run(
      [sys.executable, str(ROOT / "scripts/audit_project.py"), str(ROOT / "starter")],
      cwd=ROOT,
      capture_output=True,
      text=True,
      check=False,
    )
    if result.returncode != 0:
      errors.append("starter audit failed:\n" + result.stdout + result.stderr)

  if errors:
    print("Standard check failed:")
    for error in errors:
      print(f"- {error}")
    return 1

  print(f"Standard check passed (version {version}).")
  return 0


if __name__ == "__main__":
  sys.exit(main())
