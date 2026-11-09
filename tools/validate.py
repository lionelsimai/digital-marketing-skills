#!/usr/bin/env python3
"""Validate the Digital Marketing Skills collection. Stdlib only.

    python3 tools/validate.py

Checks (exit 1 on any failure):
- exactly 120 skill folders, 12 categories x 10 skills
- unique slugs; folder name == frontmatter name
- every SKILL.md has valid frontmatter: name, description (with a
  TRIGGERS line), category, version
- every SKILL.md has the required body sections and real substance
  (workflow with >=4 steps, deliverable, metrics, guardrails)
- catalog.json count/categories/skills match the folders on disk
- CATALOG.md lists every slug
- root files present: README.md, LICENSE, CHANGELOG.md, CONTRIBUTING.md,
  .claude-plugin/plugin.json + marketplace.json (valid JSON, marketplace
  name lionel-sim-skills, plugin source ./ exists)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_TOTAL = 120
EXPECTED_PER_CATEGORY = 10
REQUIRED_SECTIONS = ["## What this skill does", "## Inputs to collect",
                     "## Workflow", "## Deliverable", "## Success metrics",
                     "## Quality checklist", "## Guardrails"]
ROOT_FILES = ["README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
              "CATALOG.md", "catalog.json", ".gitignore"]


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = {}
    current = None
    for line in text[4:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            current = m.group(1)
            fm[current] = m.group(2).strip()
        elif current and line.startswith("  "):
            fm[current] = (fm.get(current, "") + " " + line.strip()).strip()
    return fm


def main():
    errors, warnings = [], []

    for rel in ROOT_FILES + [".claude-plugin/plugin.json",
                             ".claude-plugin/marketplace.json"]:
        if not os.path.isfile(os.path.join(ROOT, rel)):
            errors.append(f"missing root file: {rel}")

    folders = sorted(d for d in os.listdir(ROOT)
                     if os.path.isdir(os.path.join(ROOT, d))
                     and not d.startswith(".") and d != "tools")
    if len(folders) != EXPECTED_TOTAL:
        errors.append(f"skill folders: {len(folders)} != {EXPECTED_TOTAL}")

    slugs, by_category = [], {}
    for slug in folders:
        path = os.path.join(ROOT, slug, "SKILL.md")
        if not os.path.isfile(path):
            errors.append(f"{slug}: missing SKILL.md")
            continue
        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{slug}: no valid frontmatter")
            continue
        for key in ("name", "description", "category", "version"):
            if not fm.get(key):
                errors.append(f"{slug}: frontmatter missing '{key}'")
        if fm.get("name") != slug:
            errors.append(f"{slug}: frontmatter name '{fm.get('name')}' != folder")
        if "TRIGGERS" not in fm.get("description", ""):
            errors.append(f"{slug}: description lacks TRIGGERS line")
        if len(fm.get("description", "")) < 60:
            errors.append(f"{slug}: description too short to be a real skill")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{slug}: missing section '{section}'")
        steps = re.findall(r"^\d+\. \*\*", text, flags=re.M)
        if len(steps) < 4:
            errors.append(f"{slug}: workflow has {len(steps)} steps (<4)")
        if len(text) < 1800:
            errors.append(f"{slug}: SKILL.md only {len(text)} chars (<1800) - stub?")
        slugs.append(slug)
        by_category.setdefault(fm.get("category", "?"), []).append(slug)

    if len(slugs) != len(set(slugs)):
        errors.append("duplicate slugs detected")
    if len(by_category) != 12:
        errors.append(f"categories: {len(by_category)} != 12 ({sorted(by_category)})")
    for cat, members in sorted(by_category.items()):
        if len(members) != EXPECTED_PER_CATEGORY:
            errors.append(f"category '{cat}': {len(members)} skills != 10")

    catalog_path = os.path.join(ROOT, "catalog.json")
    if os.path.isfile(catalog_path):
        catalog = json.load(open(catalog_path))
        cat_slugs = sorted(s["slug"] for s in catalog.get("skills", []))
        if catalog.get("count") != len(folders):
            errors.append(f"catalog count {catalog.get('count')} != folders {len(folders)}")
        if cat_slugs != sorted(folders):
            errors.append("catalog skill slugs do not match folders on disk")
        for centry in catalog.get("categories", []):
            if centry["count"] != len(by_category.get(centry["name"], [])):
                errors.append(f"catalog category '{centry['name']}' count mismatch")

    catalog_md = os.path.join(ROOT, "CATALOG.md")
    if os.path.isfile(catalog_md):
        md = open(catalog_md, encoding="utf-8").read()
        for slug in folders:
            if f"{slug}/SKILL.md" not in md:
                errors.append(f"CATALOG.md does not list {slug}")

    mp_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    if os.path.isfile(mp_path):
        mp = json.load(open(mp_path))
        if mp.get("name") != "lionel-sim-skills":
            errors.append("marketplace name is not 'lionel-sim-skills'")
        for plugin in mp.get("plugins", []):
            src = plugin.get("source", "")
            if not os.path.isdir(os.path.join(ROOT, src)):
                errors.append(f"marketplace plugin source '{src}' does not exist")
    pj_path = os.path.join(ROOT, ".claude-plugin", "plugin.json")
    if os.path.isfile(pj_path):
        json.load(open(pj_path))

    print(f"Folders: {len(folders)} | Slugs parsed: {len(slugs)} | "
          f"Categories: {len(by_category)}")
    for cat, members in sorted(by_category.items()):
        print(f"  {cat}: {len(members)}")
    if warnings:
        print("WARNINGS:")
        [print(f"  - {w}") for w in warnings]
    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        [print(f"  - {e}") for e in errors]
        return 1
    print("\nALL CHECKS PASSED: 120 skills, 12 categories x 10, "
          "100% frontmatter compliance, catalog matches folders.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
