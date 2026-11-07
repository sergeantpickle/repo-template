#!/usr/bin/env python3
import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def parse_semver(value):
  if not isinstance(value, str) or not SEMVER.fullmatch(value):
    raise ValueError(f"not a MAJOR.MINOR.PATCH version: {value}")
  return tuple(int(part) for part in value.split("."))


def read_adoption(project):
  path = project / ".repo-standard.json"
  data = json.loads(path.read_text(encoding="utf-8"))
  version = data.get("version")
  source = data.get("source")
  parse_semver(version)
  if not isinstance(source, str) or not source.strip():
    raise ValueError("adoption manifest source must be a non-empty string")
  return {"version": version, "source": source.strip()}


def latest_url_from_source(source):
  parsed = urllib.parse.urlparse(source)
  if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
    raise ValueError("cannot derive VERSION URL from non-GitHub source; pass --latest-url")
  parts = [part for part in parsed.path.split("/") if part]
  if len(parts) != 2:
    raise ValueError("GitHub source must be https://github.com/<owner>/<repo>")
  owner, repository = parts
  if repository.endswith(".git"):
    repository = repository[:-4]
  if not owner or not repository:
    raise ValueError("GitHub source must include owner and repository")
  return f"https://raw.githubusercontent.com/{owner}/{repository}/main/VERSION"


def fetch_latest(url, timeout):
  request = urllib.request.Request(url, headers={"User-Agent": "repo-growth-standard"})
  with urllib.request.urlopen(request, timeout=timeout) as response:
    value = response.read(128).decode("utf-8").strip()
  parse_semver(value)
  return value


def compare(adopted, latest):
  current = parse_semver(adopted)
  available = parse_semver(latest)
  if current < available:
    return "behind"
  if current > available:
    return "ahead"
  return "current"


def main():
  parser = argparse.ArgumentParser(description="Check whether a project has adopted the latest upstream Repository Growth Standard version.")
  parser.add_argument("project", nargs="?", default=".", help="project directory")
  parser.add_argument("--latest-url", help="override the VERSION URL derived from the manifest source")
  parser.add_argument("--latest-version", help="use an explicit latest version instead of network access")
  parser.add_argument("--fail-if-behind", action="store_true", help="exit 1 when a newer upstream version exists")
  parser.add_argument("--fail-on-network", action="store_true", help="exit 2 when the upstream version cannot be retrieved")
  parser.add_argument("--format", choices=["text", "json"], default="text")
  args = parser.parse_args()

  project = Path(args.project).resolve()
  try:
    adoption = read_adoption(project)
  except (OSError, json.JSONDecodeError, ValueError, TypeError) as exc:
    print(f"error: cannot read adopted standard: {exc}", file=sys.stderr)
    return 2

  try:
    latest_url = args.latest_url or latest_url_from_source(adoption["source"])
    latest = args.latest_version or fetch_latest(latest_url, timeout=10)
    parse_semver(latest)
  except (urllib.error.URLError, OSError, ValueError) as exc:
    if args.format == "json":
      print(json.dumps({
        "status": "unavailable",
        "adopted": adoption["version"],
        "source": adoption["source"],
        "error": str(exc),
      }, indent=2, sort_keys=True))
    else:
      print(f"WARN: upstream standard version unavailable: {exc}")
    return 2 if args.fail_on_network else 0

  status = compare(adoption["version"], latest)
  result = {
    "status": status,
    "adopted": adoption["version"],
    "latest": latest,
    "source": adoption["source"],
  }
  if args.format == "json":
    print(json.dumps(result, indent=2, sort_keys=True))
  else:
    if status == "behind":
      print(f"UPDATE AVAILABLE: project adopts {adoption['version']}; upstream standard is {latest}")
    elif status == "ahead":
      print(f"INFO: project adopts {adoption['version']}, which is newer than upstream {latest}")
    else:
      print(f"Standard is current: {adoption['version']}")
  return 1 if status == "behind" and args.fail_if_behind else 0


if __name__ == "__main__":
  sys.exit(main())
