"""Offline deterministic validation for the public frontier snapshot monitor."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

path=Path(__file__).with_name("skills_watch.py")
spec=importlib.util.spec_from_file_location("skill_watch_under_test",path)
assert spec and spec.loader
watch=importlib.util.module_from_spec(spec)
spec.loader.exec_module(watch)

class SourceWatchTests(unittest.TestCase):
    def fake(self, repo, token=None):
        return {"full_name":repo,"stargazers_count":12,"forks_count":2,"open_issues_count":0,
                "license":{"spdx_id":"MIT"},"pushed_at":"2026-11-25T01:02:03Z","archived":False}

    def test_whole_fixed_universe(self):
        out=watch.snapshot(self.fake)
        self.assertEqual(out["status"],"COMPLETE")
        self.assertEqual(out["success_count"],10)
        self.assertEqual(len(out["repositories"]),len(watch.PROJECTS))
        self.assertEqual(len(set(x["repo"].lower() for x in out["repositories"])),10)
        self.assertIn("Stars",watch.markdown(out))

    def test_incomplete_fails_honestly(self):
        def failing(repo,token=None):
            if repo=="NVIDIA/SkillEvaluator":raise ValueError("corrupt")
            return self.fake(repo,token)
        o=watch.snapshot(failing)
        self.assertEqual(o["status"],"INCOMPLETE")
        self.assertEqual(o["success_count"],9)
        self.assertEqual(o["errors"][0]["reason"],"ValueError")

    def test_unverified_license_is_not_mit(self):
        data=self.fake("agentskills/agentskills")
        data["license"]=None
        a=watch.record("agentskills/agentskills","Specification",data)
        self.assertEqual(a["license_spdx"],"UNVERIFIED")

    def test_reject_identity_spoof(self):
        with self.assertRaises(ValueError):
            watch.record("agentskills/agentskills","Specification",self.fake("attacker/repo"))

    def test_reject_malformed_source_path(self):
        with self.assertRaises(ValueError):
            watch.fetch("../secrets")

    def test_reject_github_injection_metadata(self):
        data=self.fake("agentskills/agentskills")
        data["stargazers_count"]="-1 stars!"
        data["pushed_at"]="2026-11-25T01:02:03Z | BAD"
        data["license"]={"spdx_id":"MIT | injected"}
        result=watch.record("agentskills/agentskills","Specification",data)
        self.assertIsNone(result["stars"])
        self.assertIsNone(result["pushed_at_utc"])
        self.assertEqual(result["license_spdx"],"UNVERIFIED")

    def test_snapshot_metadata_only(self):
        r=watch.snapshot(self.fake)
        s=str(r)
        self.assertNotIn("skill_instructions",s)
        self.assertNotIn("COMPATIBLE",s)

if __name__=="__main__":
    unittest.main()
