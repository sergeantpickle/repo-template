#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "starter"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
LATEST = (ROOT / "LATEST").read_text(encoding="utf-8").strip()
ALIGN_VERSION = VERSION if LATEST in {"none", "null", ""} else LATEST
DEFAULT_SOURCE = "https://github.com/sergeantpickle/repo-template"
STARTER_FILES = ["README.md", "AGENTS.md", ".repo-standard.json"]


def render_manifest(source):
  return json.dumps(
    {
      "source": source,
      "version": ALIGN_VERSION,
      "last_checked": None,
      "exceptions": {},
    },
    indent=2,
    sort_keys=False,
  ) + "\n"


def initialize(target, source):
  if target.exists():
    existing = sorted(
      path.name
      for path in target.iterdir()
      if path.name != ".git"
    )
    if existing:
      raise FileExistsError(
        "target is not empty; use pre-adoption review for an existing project: "
        + ", ".join(existing)
      )

  target.mkdir(parents=True, exist_ok=True)
  for name in STARTER_FILES:
    destination = target / name
    if name == ".repo-standard.json":
      content = render_manifest(source)
    else:
      content = (STARTER / name).read_text(encoding="utf-8")
    destination.write_text(content, encoding="utf-8")


def main():
  parser = argparse.ArgumentParser(
    description="Export the minimal downstream starter without copying the upstream guide."
  )
  parser.add_argument("target", help="new or existing directory that does not already contain starter paths")
  parser.add_argument(
    "--source",
    default=DEFAULT_SOURCE,
    help="upstream standard repository recorded in .repo-standard.json",
  )
  args = parser.parse_args()

  target = Path(args.target).resolve()
  try:
    initialize(target, args.source)
  except (OSError, ValueError) as exc:
    print(f"error: {exc}", file=sys.stderr)
    return 1

  print(f"Initialized Repository Growth Standard starter at {target}")
  print(f"Alignment version: {ALIGN_VERSION}")
  if LATEST in {"none", "null", ""}:
    print("NOTE: no stable release exists yet; this is a Draft trial and should pin a reviewed upstream commit SHA.")
  print("Created: " + ", ".join(STARTER_FILES))
  return 0


if __name__ == "__main__":
  sys.exit(main())
