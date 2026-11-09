# Contributing

Issues and pull requests welcome. This collection has a high bar —
it exists so agents do marketing work properly, not quickly-and-dirty.

## The rules

1. **Substance over stubs.** Every skill needs a real workflow (4+
   specific steps), a defined deliverable, success metrics and a
   quality checklist. Template clones with swapped nouns are rejected.
2. **Frontmatter compliance.** `name` (matching the folder), a
   `description` ending with a `TRIGGERS - Use when...` line,
   `category`, and `version`. Run `python3 tools/validate.py` — it
   must pass at 100%.
3. **Guardrails stay.** No black-hat SEO, purchased links, fake
   reviews or testimonials, invented results, dark patterns, or
   consent shortcuts. New skills in regulated areas (email, tracking,
   advertising claims) must carry the relevant policy/privacy
   guardrail.
4. **Examples are fictional.** Never include real client names, real
   campaign data or anyone's personal information.
5. **Stay in scope.** Organic social belongs in
   social-media-marketing-skills, store operations in
   ecommerce-skills-collection, and AEO/GEO depth in aeo-geo-skills.
   Cross-link instead of duplicating.

## Adding a skill

Skills are rendered from authored data in `tools/skills_data.py`:

1. Add the skill entry (slug, title, description, inputs, steps,
   outputs, metrics, checks, any skill-specific guardrails) to its
   category there.
2. Run `python3 tools/build_skills.py` to regenerate the SKILL.md
   files and the catalogues.
3. Run `python3 tools/validate.py` and fix anything it flags.
4. Update the category table in `README.md` and the `CHANGELOG.md`
   if counts change.
