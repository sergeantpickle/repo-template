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

  def test_read_adopted(self):
    with tempfile.TemporaryDirectory() as temp:
      project = Path(temp)
      (project / ".repo-standard.json").write_text(
        json.dumps({"version": "0.1.0"}),
        encoding="utf-8",
      )
      self.assertEqual("0.1.0", check_latest.read_adopted(project))


if __name__ == "__main__":
  unittest.main()
