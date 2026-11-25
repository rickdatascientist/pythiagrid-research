#!/usr/bin/env python3
"""Public-source Agent Skills ecosystem monitor (not a skill scanner or model).

Read-only GitHub repository metadata, in a bounded allowlist. The output is a
timestamped snapshot; GitHub stars are interest signals, NOT evidence that a
technology is secure, useful, novel, or destined to trend.
No third-party skill code, repository trees, secrets, or user data are fetched.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
import re
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

PROJECTS = (
    ("agentskills/agentskills", "Specification"),
    ("vercel-labs/skills", "Distribution"),
    ("anthropics/skills", "Official skill examples"),
    ("NVIDIA/SkillEvaluator", "Evaluation and risk"),
    ("ControllableModel/SWE-Skills-Bench", "Real task outcomes"),
    ("ynulihao/AgentSkillOS", "Large-scale selection"),
    ("agent-contracts/skill-preflight", "Pre-install checks"),
    ("southwind-ai/soup", "Routing"),
    ("obra/superpowers", "Developer workflow"),
    ("HKUDS/CLI-Anything", "Agent-native tools"),
)
REPO_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,99}/[A-Za-z0-9][A-Za-z0-9_.-]{0,99}$")
SCHEMA = "pythiagrid.open-science.skill-frontier.v1"

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def safe_int(value):
    return value if type(value) is int and value >= 0 else None

def record(name: str, category: str, data: dict) -> dict:
    """Validate and limit the external input's displayed fields."""
    if not REPO_PATTERN.fullmatch(name) or data.get("full_name", "").lower() != name.lower():
        raise ValueError("repository identity mismatch")
    license_data = data.get("license")
    license_spdx = license_data.get("spdx_id") if isinstance(license_data, dict) else None
    if not isinstance(license_spdx, str) or not re.fullmatch(r"[a-zA-Z0-9.+-]{1,40}", license_spdx):
        license_spdx = "UNVERIFIED"
    pushed = data.get("pushed_at")
    if not isinstance(pushed, str) or not re.fullmatch(r"20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9:]{8}Z", pushed):
        pushed = None
    return {
        "repo":name, "category":category,
        "stars":safe_int(data.get("stargazers_count")),
        "forks":safe_int(data.get("forks_count")),
        "open_issues":safe_int(data.get("open_issues_count")),
        "pushed_at_utc":pushed,
        "license_spdx":license_spdx,
        "archived":data.get("archived") is True,
        "source":"https://github.com/"+name,
    }

def fetch(name: str, *, token: str | None = None) -> dict:
    if not REPO_PATTERN.fullmatch(name):
        raise ValueError("unsafe repository slug")
    headers = {"Accept":"application/vnd.github+json",
               "User-Agent":"PythiaGrid-Research-Frontier/1.0",
               "X-GitHub-Api-Version":"2022-11-28"}
    if token:
        headers["Authorization"] = "Bearer "+token
    req = Request("https://api.github.com/repos/"+name,headers=headers)
    with urlopen(req,timeout=15) as response:
        if response.status != 200:
            raise RuntimeError("unexpected HTTP status")
        body = response.read(120_001)
        if len(body)>120_000:
            raise RuntimeError("oversized API response")
        return json.loads(body.decode("utf-8"))

def snapshot(fetcher=fetch, *, token: str | None = None) -> dict:
    records=[]
    errors=[]
    for name,category in PROJECTS:
        try:
            data = fetcher(name,token=token)
            records.append(record(name,category,data))
        except (HTTPError,URLError,RuntimeError,ValueError,KeyError,TypeError,UnicodeError) as e:
            errors.append({"repo":name,"reason":type(e).__name__})
    return {
        "schema":SCHEMA,
        "observed_at_utc":utc_now(),
        "population":"fixed ten-public-repository sample; NOT all GitHub skills",
        "success_count":len(records),
        "expected_count":len(PROJECTS),
        "status":"COMPLETE" if not errors else "INCOMPLETE",
        "repositories":records,
        "errors":errors,
        "interpretation":"Metadata watch only: popularity is not validity, evidence of utility, or a market-share metric.",
        "release_effect":"NONE; no skill installed, benchmark promoted, or paper released",
    }

def markdown(result:dict) -> str:
    lines=[
        "## PythiaGrid Research — Agent Skills frontier snapshot",
        "Observed UTC: "+result["observed_at_utc"],
        "**"+result["status"]+"** — "+str(result["success_count"])+"/"+str(result["expected_count"])+" sources",
        "",
        "| Public project | Research angle | Stars* | Licence metadata | Last source update (UTC) |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for item in result["repositories"]:
        # All labels and URLs derive from the fixed, internally authored allowlist.
        lines.append("| ["+item["repo"]+"]("+item["source"]+") | "+
                     item["category"]+" | "+
                     (str(item["stars"]) if item["stars"] is not None else "UNKNOWN")+
                     " | "+item["license_spdx"]+" | "+(item["pushed_at_utc"] or "UNKNOWN")+" |")
    if result["errors"]:
        lines.extend(["", "**Source errors:** "+", ".join(x["repo"]+" ("+x["reason"]+")" for x in result["errors"])])
    lines.extend([
        "",
        "*Stars are unaudited platform engagement counts, not scientific scores or forecasts.*",
        "",
        "No skill instructions executed; no production mutation, public release, or security verdict.",
    ])
    return "\n".join(lines)+"\n"

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json",action="store_true",help="Print machine-readable report")
    p.add_argument("--strict",action="store_true",help="Exit nonzero when any source is missing")
    args=p.parse_args(argv)
    result=snapshot(token=os.environ.get("GITHUB_TOKEN"))
    print(json.dumps(result,sort_keys=True,indent=2) if args.json else markdown(result))
    # Github Actions run Summary shows the table; no write access to GitHub needed.
    summary_path=os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path,"a",encoding="utf-8") as f:
            f.write(markdown(result))
    return 1 if args.strict and result["status"]!="COMPLETE" else 0

if __name__ == "__main__":
    sys.exit(main())
