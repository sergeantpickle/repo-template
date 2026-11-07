import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_project


class AuditProjectTests(unittest.TestCase):
  def make_project(self, files=None, manifest=None):
    temp = tempfile.TemporaryDirectory()
    project = Path(temp.name)
    data = manifest or {
      "source": "https://github.com/sergeantpickle/repo-template",
      "version": "0.1.0",
      "last_checked": None,
      "exceptions": {},
    }
    (project / ".repo-standard.json").write_text(json.dumps(data), encoding="utf-8")
    for relative, content in (files or {}).items():
      path = project / relative
      path.parent.mkdir(parents=True, exist_ok=True)
      path.write_text(content, encoding="utf-8")
    return temp, project

  def active_findings(self, result):
    return [finding for finding in result["findings"] if finding["status"] == "active"]

  def test_pre_adoption_mode_allows_missing_manifest(self):
    with tempfile.TemporaryDirectory() as temp:
      project = Path(temp)
      (project / "README.md").write_text("# Example\n\n## Current state\nWork in progress.\n", encoding="utf-8")
      result = audit_project.audit(project, pre_adoption=True)
      self.assertEqual([], result["errors"])
      self.assertEqual("pre-adoption", result["adoption_status"])
      self.assertTrue(any(f["id"] == "RGS-ROUTE-README-001" for f in result["findings"]))

  def test_missing_manifest_is_error_after_adoption(self):
    with tempfile.TemporaryDirectory() as temp:
      project = Path(temp)
      result = audit_project.audit(project)
      self.assertTrue(any(error["code"] == "manifest-missing" for error in result["errors"]))

  def test_minimal_project_has_no_findings(self):
    temp, project = self.make_project({
      "README.md": "# Example\n\nSetup and usage.\n",
      "AGENTS.md": "# Agent Instructions\n\nRun tests with `pytest`.\n",
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    self.assertEqual([], result["errors"])
    self.assertEqual([], result["findings"])

  def test_readme_active_work_heading_warns(self):
    temp, project = self.make_project({"README.md": "# Example\n\n## Current state\nWorking on auth.\n"})
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    ids = {finding["id"] for finding in self.active_findings(result)}
    self.assertIn("RGS-ROUTE-README-001", ids)

  def test_changelog_active_work_heading_warns(self):
    temp, project = self.make_project({"CHANGELOG.md": "# Changelog\n\n## Blockers\nWaiting on CI.\n"})
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    ids = {finding["id"] for finding in self.active_findings(result)}
    self.assertIn("RGS-ROUTE-CHANGELOG-001", ids)

  def test_singleton_buckets_warn(self):
    temp, project = self.make_project({
      "HANDOFF.md": "# Handoff\n",
      "NOTES.md": "# Notes\n",
      "LOG.md": "# Log\n",
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    ids = {finding["id"] for finding in self.active_findings(result)}
    self.assertIn("RGS-ROUTE-HANDOFF-001", ids)
    self.assertIn("RGS-ROUTE-BUCKET-001", ids)

  def test_instruction_copies_warn_even_when_identical(self):
    temp, project = self.make_project({
      "AGENTS.md": "# Rules\n\nRun tests.\n",
      "CLAUDE.md": "# Rules\n\nRun tests.\n",
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    finding = next(f for f in result["findings"] if f["id"] == "RGS-INSTR-002")
    self.assertIn("same content", finding["message"])

  def test_instruction_copies_warn_when_different(self):
    temp, project = self.make_project({
      "AGENTS.md": "# Rules\n\nRun tests.\n",
      "CLAUDE.md": "# Claude\n\nDo not run tests.\n",
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    finding = next(f for f in result["findings"] if f["id"] == "RGS-INSTR-002")
    self.assertIn("differ", finding["message"])

  def test_generated_root_adapter_does_not_warn_when_it_contains_canonical_agents(self):
    canonical = "# Shared rules\n\nRun tests.\n"
    generated = (
      "<!-- GENERATED FILE -- do not edit by hand.\n"
      "Generated from AGENTS.md. -->\n\n"
      + canonical
    )
    temp, project = self.make_project({
      "AGENTS.md": canonical,
      "CLAUDE.md": generated,
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    self.assertFalse(any(f["id"] == "RGS-INSTR-002" for f in result["findings"]))

  def test_generated_marker_does_not_hide_diverged_adapter(self):
    temp, project = self.make_project({
      "AGENTS.md": "# Shared rules\n\nRun tests.\n",
      "CLAUDE.md": "<!-- GENERATED FILE -- do not edit by hand. -->\n\n# Different rules\n",
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    self.assertTrue(any(f["id"] == "RGS-INSTR-002" for f in result["findings"]))

  def test_nested_identical_instruction_copies_warn(self):
    temp, project = self.make_project({
      "AGENTS.md": "# Root rules\n",
      "services/api/AGENTS.md": "# Same scoped rules\n\nRun API tests.\n",
      "services/worker/AGENTS.md": "# Same scoped rules\n\nRun API tests.\n",
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    matching = [
      finding
      for finding in result["findings"]
      if finding["id"] == "RGS-INSTR-002"
      and "services/api/AGENTS.md" in finding["paths"]
      and "services/worker/AGENTS.md" in finding["paths"]
    ]
    self.assertEqual(1, len(matching))
    self.assertEqual("recommended", matching[0]["rule_level"])
    self.assertEqual("heuristic", matching[0]["detection"])

  def test_different_nested_scoped_instructions_do_not_warn_by_themselves(self):
    temp, project = self.make_project({
      "services/api/AGENTS.md": "# API\n\nRun API tests.\n",
      "services/web/AGENTS.md": "# Web\n\nRun browser tests.\n",
    })
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    self.assertFalse(any(f["id"] == "RGS-INSTR-002" for f in result["findings"]))

  def test_exception_is_visible_not_hidden(self):
    manifest = {
      "source": "https://github.com/sergeantpickle/repo-template",
      "version": "0.1.0",
      "last_checked": None,
      "exceptions": {
        "RGS-ROUTE-HANDOFF-001": {
          "reason": "Release train coordination intentionally uses a bounded handoff file."
        }
      },
    }
    temp, project = self.make_project({"HANDOFF.md": "# Handoff\n"}, manifest)
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    finding = next(f for f in result["findings"] if f["id"] == "RGS-ROUTE-HANDOFF-001")
    self.assertEqual("excepted", finding["status"])
    self.assertIn("Release train", finding["exception"]["reason"])

  def test_unknown_exception_is_error(self):
    manifest = {
      "source": "https://github.com/sergeantpickle/repo-template",
      "version": "0.1.0",
      "last_checked": None,
      "exceptions": {
        "DOES-NOT-EXIST": {"reason": "test"}
      },
    }
    temp, project = self.make_project({}, manifest)
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    codes = {error["code"] for error in result["errors"]}
    self.assertIn("exception-unknown-rule", codes)

  def test_non_exception_rule_cannot_be_excepted(self):
    manifest = {
      "source": "https://github.com/sergeantpickle/repo-template",
      "version": "0.1.0",
      "last_checked": None,
      "exceptions": {
        "RGS-ADOPT-001": {"reason": "test"}
      },
    }
    temp, project = self.make_project({}, manifest)
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    codes = {error["code"] for error in result["errors"]}
    self.assertIn("exception-not-allowed", codes)

  def test_expired_exception_warns(self):
    yesterday = (dt.date.today() - dt.timedelta(days=1)).isoformat()
    manifest = {
      "source": "https://github.com/sergeantpickle/repo-template",
      "version": "0.1.0",
      "last_checked": None,
      "exceptions": {
        "RGS-ROUTE-HANDOFF-001": {
          "reason": "temporary",
          "review_after": yesterday,
        }
      },
    }
    temp, project = self.make_project({}, manifest)
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    self.assertTrue(any(f["id"] == "RGS-EXCEPT-001" for f in result["findings"]))

  def test_version_match_can_be_required_for_pinned_auditor(self):
    manifest = {
      "source": "https://github.com/sergeantpickle/repo-template",
      "version": "9.9.9",
      "last_checked": None,
      "exceptions": {},
    }
    temp, project = self.make_project({}, manifest)
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project, require_version_match=True)
    self.assertTrue(any(error["code"] == "auditor-version-mismatch" for error in result["errors"]))

  def test_version_drift_is_informational_and_not_exceptable(self):
    manifest = {
      "source": "https://github.com/sergeantpickle/repo-template",
      "version": "9.9.9",
      "last_checked": None,
      "exceptions": {},
    }
    temp, project = self.make_project({}, manifest)
    self.addCleanup(temp.cleanup)
    result = audit_project.audit(project)
    finding = next(f for f in result["findings"] if f["id"] == "standard-version-drift")
    self.assertEqual("info", finding["level"])


if __name__ == "__main__":
  unittest.main()
