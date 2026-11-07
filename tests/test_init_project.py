import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import init_project


class InitProjectTests(unittest.TestCase):
  def test_initializes_only_minimal_starter(self):
    with tempfile.TemporaryDirectory() as temp:
      target = Path(temp) / "project"
      init_project.initialize(target, "https://github.com/example/standard")
      self.assertEqual(
        {".repo-standard.json", "AGENTS.md", "README.md"},
        {path.name for path in target.iterdir()},
      )
      manifest = json.loads((target / ".repo-standard.json").read_text(encoding="utf-8"))
      self.assertEqual("https://github.com/example/standard", manifest["source"])
      self.assertEqual(init_project.VERSION, manifest["version"])
      self.assertIsNone(manifest["last_checked"])

  def test_refuses_to_overwrite_existing_starter_path(self):
    with tempfile.TemporaryDirectory() as temp:
      target = Path(temp)
      (target / "README.md").write_text("# Existing\n", encoding="utf-8")
      with self.assertRaises(FileExistsError):
        init_project.initialize(target, "https://github.com/example/standard")
      self.assertFalse((target / "AGENTS.md").exists())
      self.assertFalse((target / ".repo-standard.json").exists())

  def test_empty_existing_directory_is_allowed(self):
    with tempfile.TemporaryDirectory() as temp:
      target = Path(temp)
      init_project.initialize(target, "https://github.com/example/standard")
      self.assertTrue((target / "AGENTS.md").is_file())


if __name__ == "__main__":
  unittest.main()
