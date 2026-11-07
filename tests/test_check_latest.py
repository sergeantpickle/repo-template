import base64
import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_latest


class CheckLatestTests(unittest.TestCase):
  def test_compare_versions(self):
    self.assertEqual("behind", check_latest.compare("0.1.0", "0.2.0"))
    self.assertEqual("current", check_latest.compare("1.2.3", "1.2.3"))
    self.assertEqual("ahead", check_latest.compare("2.0.0", "1.9.9"))
    self.assertEqual("unreleased", check_latest.compare("0.1.0", None))

  def test_semver_rejects_non_release_value(self):
    with self.assertRaises(ValueError):
      check_latest.parse_semver("0.2")
    with self.assertRaises(ValueError):
      check_latest.parse_semver("v1.0.0")

  def test_parse_latest_accepts_none_sentinel(self):
    self.assertIsNone(check_latest.parse_latest("none\n"))
    self.assertIsNone(check_latest.parse_latest("null"))
    self.assertEqual("1.2.3", check_latest.parse_latest("1.2.3\n"))

  def test_read_alignment(self):
    with tempfile.TemporaryDirectory() as temp:
      project = Path(temp)
      (project / ".repo-standard.json").write_text(
        json.dumps({
          "schema_version": 1,
          "source": "https://github.com/example/standard",
          "version": "0.1.0",
        }),
        encoding="utf-8",
      )
      self.assertEqual(
        {
          "source": "https://github.com/example/standard",
          "version": "0.1.0",
        },
        check_latest.read_alignment(project),
      )

  def test_read_alignment_rejects_unsupported_schema(self):
    with tempfile.TemporaryDirectory() as temp:
      project = Path(temp)
      (project / ".repo-standard.json").write_text(
        json.dumps({
          "schema_version": 2,
          "source": "https://github.com/example/standard",
          "version": "0.1.0",
        }),
        encoding="utf-8",
      )
      with self.assertRaises(ValueError):
        check_latest.read_alignment(project)

  def test_latest_url_is_derived_from_manifest_source(self):
    self.assertEqual(
      "https://api.github.com/repos/example/standard/contents/LATEST",
      check_latest.latest_url_from_source("https://github.com/example/standard"),
    )
    self.assertEqual(
      "https://api.github.com/repos/example/standard/contents/LATEST",
      check_latest.latest_url_from_source("https://github.com/example/standard.git"),
    )

  def test_parse_latest_payload_accepts_plain_text(self):
    self.assertEqual("1.2.3", check_latest.parse_latest_payload(b"1.2.3\n"))
    self.assertIsNone(check_latest.parse_latest_payload(b"none\n"))

  def test_parse_latest_payload_accepts_github_contents_response(self):
    encoded = base64.b64encode(b"1.2.3\n").decode("ascii")
    payload = json.dumps({"encoding": "base64", "content": encoded}).encode("utf-8")
    self.assertEqual("1.2.3", check_latest.parse_latest_payload(payload))

  def test_parse_latest_payload_rejects_unexpected_json(self):
    with self.assertRaises(ValueError):
      check_latest.parse_latest_payload(b'{"message":"not a contents response"}')

  def test_non_github_source_requires_explicit_latest_url(self):
    with self.assertRaises(ValueError):
      check_latest.latest_url_from_source("https://example.com/standard")


if __name__ == "__main__":
  unittest.main()
