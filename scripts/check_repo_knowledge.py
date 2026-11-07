#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_MARKER = ROOT / ".repo-template"

REQUIRED = [
  "README.md",
  "AGENTS.md",
  "INDEX.md",
  "docs/README.md",
  "docs/GOVERNANCE.md",
  "docs/PLANS.md",
  "docs/templates/exec-plan.md",
  "docs/templates/decision.md",
  "docs/templates/research.md",
  "docs/templates/handoff.md",
]

PLACEHOLDER_PATTERNS = [
  re.compile(r"<Task title>"),
  re.compile(r"<Decision title>"),
  re.compile(r"<Research topic>"),
  re.compile(r"<Handoff topic>"),
  re.compile(r"Template state:"),
]

errors = []

for relative in REQUIRED:
  if not (ROOT / relative).is_file():
    errors.append(f"missing required repository-knowledge file: {relative}")

index = ROOT / "INDEX.md"
if index.is_file():
  text = index.read_text(encoding="utf-8")
  for section in [
    "Repository map",
    "Validation",
    "Active work",
    "Maintenance rule",
  ]:
    if section not in text:
      errors.append(f"INDEX.md is missing required section: {section}")

docs_index = ROOT / "docs/README.md"
if docs_index.is_file() and "../INDEX.md" not in docs_index.read_text(encoding="utf-8"):
  errors.append("docs/README.md does not link to ../INDEX.md")

agents = ROOT / "AGENTS.md"
if agents.is_file():
  lines = agents.read_text(encoding="utf-8").splitlines()
  if len(lines) > 220:
    errors.append(
      f"AGENTS.md is {len(lines)} lines; keep it a compact routing/instruction surface"
    )

if not TEMPLATE_MARKER.exists():
  checked = [
    ROOT / "README.md",
    ROOT / "INDEX.md",
  ]
  for path in checked:
    if not path.is_file():
      continue
    text = path.read_text(encoding="utf-8")
    for pattern in PLACEHOLDER_PATTERNS:
      if pattern.search(text):
        errors.append(
          f"{path.relative_to(ROOT)} still contains template marker matching "
          f"{pattern.pattern!r}"
        )

if errors:
  print("Repository knowledge check failed:")
  for error in errors:
    print(f"- {error}")
  sys.exit(1)

state = "template" if TEMPLATE_MARKER.exists() else "initialized project"
print(f"Repository knowledge check passed ({state} state).")
