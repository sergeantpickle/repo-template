#!/usr/bin/env python3
import argparse
import base64
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
NO_RELEASE = {"none", "null", ""}


def parse_semver(value):
  if not isinstance(value, str) or not SEMVER.fullmatch(value):
    raise ValueError(f"not a MAJOR.MINOR.PATCH version: {value}")
  return tuple(int(part) for part in value.split("."))


def parse_latest(value):
  if not isinstance(value, str):
    raise ValueError("latest release value must be text")
  normalized = value.strip().lower()
  if normalized in NO_RELEASE:
    return None
  parse_semver(value.strip())
  return value.strip()


def read_alignment(project):
  path = project / ".repo-standard.json"
  data = json.loads(path.read_text(encoding="utf-8"))
  if data.get("schema_version") != 1:
    raise ValueError("alignment manifest schema_version must be 1")
  version = data.get("version")
  source = data.get("source")
  parse_semver(version)
  if not isinstance(source, str) or not source.strip():
    raise ValueError("alignment manifest source must be a non-empty string")
  return {"version": version, "source": source.strip()}


def latest_url_from_source(source):
  parsed = urllib.parse.urlparse(source)
  if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
    raise ValueError("cannot derive LATEST URL from non-GitHub source; pass --latest-url")
  parts = [part for part in parsed.path.split("/") if part]
  if len(parts) != 2:
    raise ValueError("GitHub source must be https://github.com/<owner>/<repo>")
  owner, repository = parts
  if repository.endswith(".git"):
    repository = repository[:-4]
  if not owner or not repository:
    raise ValueError("GitHub source must include owner and repository")
  return f"https://api.github.com/repos/{owner}/{repository}/contents/LATEST"


def parse_latest_payload(payload):
  text = payload.decode("utf-8")
  try:
    data = json.loads(text)
  except json.JSONDecodeError:
    return parse_latest(text)

  if isinstance(data, dict) and data.get("encoding") == "base64":
    encoded = data.get("content")
    if not isinstance(encoded, str):
      raise ValueError("GitHub contents response is missing base64 content")
    try:
      decoded = base64.b64decode(encoded, validate=False).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as exc:
      raise ValueError(f"invalid base64 LATEST content: {exc}") from exc
    return parse_latest(decoded)

  raise ValueError("LATEST endpoint did not return plain text or a GitHub contents response")


def fetch_latest(url, timeout):
  request = urllib.request.Request(
    url,
    headers={
      "User-Agent": "repo-growth-standard",
      "Accept": "application/vnd.github+json",
    },
  )
  with urllib.request.urlopen(request, timeout=timeout) as response:
    payload = response.read(16384)
  return parse_latest_payload(payload)


def compare(aligned, latest):
  if latest is None:
    return "unreleased"
  current = parse_semver(aligned)
  target = parse_semver(latest)
  if current < target:
    return "behind"
  if current > target:
    return "ahead"
  return "current"


def main():
  parser = argparse.ArgumentParser(
    description="Check a project's last-aligned Repository Growth Standard version against the latest released upstream target."
  )
  parser.add_argument("project", nargs="?", default=".", help="project directory")
  parser.add_argument("--latest-url", help="override the LATEST URL derived from the manifest source")
  parser.add_argument("--latest-version", help="use an explicit latest released version (or 'none') instead of network access")
  parser.add_argument("--fail-if-behind", action="store_true", help="exit 1 when a newer released upstream target exists")
  parser.add_argument("--fail-on-network", action="store_true", help="exit 2 when the upstream target cannot be retrieved")
  parser.add_argument("--format", choices=["text", "json"], default="text")
  args = parser.parse_args()

  project = Path(args.project).resolve()
  try:
    alignment = read_alignment(project)
  except (OSError, json.JSONDecodeError, ValueError, TypeError) as exc:
    print(f"error: cannot read alignment state: {exc}", file=sys.stderr)
    return 2

  try:
    latest_url = args.latest_url or latest_url_from_source(alignment["source"])
    latest = parse_latest(args.latest_version) if args.latest_version is not None else fetch_latest(latest_url, timeout=10)
  except (urllib.error.URLError, OSError, ValueError) as exc:
    if args.format == "json":
      print(json.dumps({
        "status": "unavailable",
        "aligned": alignment["version"],
        "source": alignment["source"],
        "error": str(exc),
      }, indent=2, sort_keys=True))
    else:
      print(f"WARN: latest released standard target unavailable: {exc}")
    return 2 if args.fail_on_network else 0

  status = compare(alignment["version"], latest)
  result = {
    "status": status,
    "aligned": alignment["version"],
    "latest": latest,
    "source": alignment["source"],
  }
  if args.format == "json":
    print(json.dumps(result, indent=2, sort_keys=True))
  else:
    if status == "behind":
      print(
        f"ALIGNMENT AVAILABLE: project last aligned to {alignment['version']}; "
        f"latest released standard is {latest}"
      )
    elif status == "ahead":
      print(
        f"INFO: project last aligned to {alignment['version']}, which is newer than "
        f"the latest released target {latest}; this is likely a draft/trial alignment"
      )
    elif status == "unreleased":
      print(
        f"INFO: upstream has no stable released target yet; project alignment is "
        f"{alignment['version']}"
      )
    else:
      print(f"Project is aligned with the latest released standard: {alignment['version']}")
  return 1 if status == "behind" and args.fail_if_behind else 0


if __name__ == "__main__":
  sys.exit(main())
