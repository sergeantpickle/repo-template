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

  def test_semver_rejects_non_release_value(self):
    with self.assertRaises(ValueError):
      check_latest.parse_semver("0.2")
    with self.assertRaises(ValueError):
      check_latest.parse_semver("v1.0.0")

  def test_read_adoption(self):
    with tempfile.TemporaryDirectory() as temp:
      project = Path(temp)
      (project / ".repo-standard.json").write_text(
        json.dumps({
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
        check_latest.read_adoption(project),
      )

  def test_latest_url_is_derived_from_manifest_source(self):
    self.assertEqual(
      "https://raw.githubusercontent.com/example/standard/main/VERSION",
      check_latest.latest_url_from_source("https://github.com/example/standard"),
    )
    self.assertEqual(
      "https://raw.githubusercontent.com/example/standard/main/VERSION",
      check_latest.latest_url_from_source("https://github.com/example/standard.git"),
    )

  def test_non_github_source_requires_explicit_latest_url(self):
    with self.assertRaises(ValueError):
      check_latest.latest_url_from_source("https://example.com/standard")


if __name__ == "__main__":
  unittest.main()
