#!/usr/bin/env python3
"""Build all 120 SKILL.md files + CATALOG.md + catalog.json for the
Digital Marketing Skills collection. Data is hand-authored in
skills_data.py; this script only renders it. Stdlib only."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skills_data import CATEGORIES, GLOBAL_GUARDRAILS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def render_skill(cat, skill):
    lines = []
    lines.append("---")
    lines.append(f"name: {skill['slug']}")
    lines.append("description: |")
    lines.append(f"  {skill['desc']}")
    lines.append(f"  TRIGGERS - Use when user needs help with {skill['triggers']} tasks.")
    lines.append(f"category: {cat['name']}")
    lines.append("version: 1.0")
    lines.append("---")
    lines.append(f"# {skill['title']}")
    lines.append("")
    lines.append(f"## What this skill does")
    lines.append("")
    lines.append(skill["does"])
    lines.append("")
    lines.append("## Inputs to collect")
    lines.append("")
    for item in skill["inputs"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Workflow")
    lines.append("")
    for i, step in enumerate(skill["steps"], 1):
        lines.append(f"{i}. **{step['h']}** - {step['d']}")
    lines.append("")
    lines.append("## Deliverable")
    lines.append("")
    for item in skill["outputs"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Success metrics")
    lines.append("")
    lines.append("| Metric | How to read it |")
    lines.append("|--------|---------------|")
    for m, how in skill["metrics"]:
        lines.append(f"| {m} | {how} |")
    lines.append("")
    lines.append("## Quality checklist")
    lines.append("")
    for item in skill["checks"]:
        lines.append(f"- [ ] {item}")
    lines.append("")
    lines.append("## Guardrails")
    lines.append("")
    for g in GLOBAL_GUARDRAILS:
        lines.append(f"- {g}")
    for g in cat["guardrails"]:
        lines.append(f"- {g}")
    for g in skill.get("guardrails", []):
        lines.append(f"- {g}")
    lines.append("")
    return "\n".join(lines)


def main():
    catalog = []
    total = 0
    for cat in CATEGORIES:
        for skill in cat["skills"]:
            folder = os.path.join(ROOT, skill["slug"])
            os.makedirs(folder, exist_ok=True)
            with open(os.path.join(folder, "SKILL.md"), "w") as fh:
                fh.write(render_skill(cat, skill))
            catalog.append({
                "slug": skill["slug"],
                "name": skill["title"],
                "category": cat["name"],
                "description": skill["desc"],
                "version": "1.0",
            })
            total += 1
    with open(os.path.join(ROOT, "catalog.json"), "w") as fh:
        json.dump({
            "name": "digital-marketing-skills",
            "version": "1.0.0",
            "author": "Lionel Sim",
            "license": "MIT",
            "count": total,
            "categories": [
                {"name": c["name"], "count": len(c["skills"]),
                 "slugs": [s["slug"] for s in c["skills"]]}
                for c in CATEGORIES
            ],
            "skills": catalog,
        }, fh, indent=2)
        fh.write("\n")
    md = ["# Catalogue - Digital Marketing Skills", "",
          f"{total} skills across {len(CATEGORIES)} categories. "
          "Every skill is a folder with a SKILL.md an agent can load.", ""]
    for cat in CATEGORIES:
        md.append(f"## {cat['name']}")
        md.append("")
        md.append(cat["blurb"])
        md.append("")
        md.append("| Skill | What it does |")
        md.append("|-------|-------------|")
        for s in cat["skills"]:
            md.append(f"| [{s['slug']}]({s['slug']}/SKILL.md) | {s['desc']} |")
        md.append("")
    with open(os.path.join(ROOT, "CATALOG.md"), "w") as fh:
        fh.write("\n".join(md))
    print(f"Built {total} skills in {len(CATEGORIES)} categories.")


if __name__ == "__main__":
    main()
