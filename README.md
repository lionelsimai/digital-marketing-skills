# Digital Marketing Skills

**120 skills for the performance and growth side of digital marketing** —
strategy, SEO, paid search and media, content, email and lifecycle,
automation and CRM, CRO, analytics, brand and creative, growth
experiments, and agency delivery. Built and maintained by
[Lionel Sim](https://www.linkedin.com/in/lionelshen) (The AI Capitol),
founder of OpenBuilder. MIT licensed — free to use, fork and build on.

Each skill is a `SKILL.md` playbook an AI agent can load to do one real
marketing job properly: inputs to collect, a specific workflow, a defined
deliverable, the metrics that judge it, and the guardrails that keep it
honest.

## How this repo differs from its sister repos

Lionel publishes a family of skill collections. They are deliberately
scoped so they don't duplicate each other:

| Repo | Scope |
|------|-------|
| **digital-marketing-skills** (this one) | The performance/growth discipline: SEO, SEM/PPC, paid media, content marketing, email & lifecycle, automation & CRM, CRO, analytics, brand & creative, growth experiments & PLG, agency delivery |
| social-media-marketing-skills | Organic social: platform content, community, creators |
| ecommerce-skills-collection | Running a store: catalogue, fulfilment, store operations |
| aeo-geo-skills | Answer Engine / Generative Engine Optimization as a full discipline (this repo keeps search AI-visibility to light coverage inside SEO) |
| gtm-skills-collection | Founder-led go-to-market: ICP, outbound, partnerships |

If a topic lives in a sister repo, this repo stays out of its way.

## The 12 categories

| Category | Skills | What it covers |
|----------|-------:|---------------|
| Digital Strategy & Funnels | 10 | Strategy plans, funnel architecture, personas, journey mapping, budgets, channel mix, campaign calendars, competitor audits, offers, growth models |
| SEO | 10 | Technical audits, keyword mapping, on-page, briefs, internal linking, local SEO, link earning & digital PR, content refresh, schema, reporting |
| SEM & PPC | 10 | Account structure, campaign builds, match types, ad copy, bidding, Quality Score, negatives, message match, RLSA, audits |
| Paid Media Planning & Buying | 10 | Media plans, budget scenarios, paid social structure, programmatic, YouTube ads, negotiation, fatigue, reallocation, incrementality, reporting cadence |
| Content Marketing | 10 | Strategy, editorial ops, pillars & clusters, long-form production, lead magnets, case studies, webinars, newsletters, distribution, performance reviews |
| Email & Lifecycle Marketing | 10 | Flow architecture, welcome, abandon recovery, campaigns, deliverability, list hygiene, lifecycle mapping, winback, transactional email, programme reporting |
| Marketing Automation & CRM | 10 | Lead scoring, nurture workflows, CRM hygiene, lifecycle stages, sales handoff & SLA, workflow audits, event automation, personalisation, consent, martech review |
| CRO & Landing Pages | 10 | Heuristic audits, A/B test design, landing copy, forms, headline/CTA testing, drop-off diagnosis, social proof, pricing pages, checkout review, results writeups |
| Web & Marketing Analytics | 10 | GA4 measurement plans, UTM governance, attribution comparison, dashboards, metric definitions, campaign analysis, cohorts, server-side tracking, consent mode, weekly scorecard |
| Brand & Creative | 10 | Positioning, messaging frameworks, creative briefs, ad concepting, voice, visual identity briefs, message houses, creative testing, proof libraries, rebrands |
| Growth Experiments & PLG | 10 | Experiment backlogs, ICE/RICE, activation audits, referral design, viral loops, trial conversion, pricing experiments, growth loops, retention curves, programme ops |
| Agency & Client Delivery | 10 | Discovery & onboarding, audit delivery, proposals & scope, retainer reporting, communication cadence, sprint planning, launch QA, account growth, freelancer briefing, monthly reviews |

Full index with a description of every skill: [CATALOG.md](CATALOG.md) ·
machine-readable: [catalog.json](catalog.json)

## The guardrails baked into every skill

- **No black-hat anything.** No purchased links or link schemes, no
  keyword stuffing, no fake reviews, no fabricated testimonials, logos
  or results, no dark patterns (fake countdowns, hidden costs,
  confirm-shaming).
- **Claims discipline.** Only proof the user supplies or verifies.
  Every skill that produces copy carries a claims/proof step.
- **Ad-platform policy compliance.** Ads promise only what the landing
  page delivers; restricted categories are checked against current
  platform rules before launch.
- **Privacy and consent.** PDPA (Singapore) and GDPR awareness in every
  email, tracking and automation skill: permission-based sending only,
  consent-gated tracking, easy unsubscribe, no personal data in UTMs.

## Install

This collection uses the open Agent Skills format (`SKILL.md`), so the
same folders run in Claude Code, Codex, Gemini CLI and any agent runtime
that reads skill folders.

### Claude Code — plugin install

```text
/plugin marketplace add lionelsimai/digital-marketing-skills
/plugin install digital-marketing-skills@lionel-sim-skills
```

### Manual — any agent

```bash
git clone https://github.com/lionelsimai/digital-marketing-skills.git
cp -r digital-marketing-skills/<skill-slug> ~/.claude/skills/   # or your agent's skills directory
```

Then describe the task ("run a technical SEO audit on my site", "design
our lead scoring model") and the agent picks up the matching skill, or
invoke it by name where your runtime supports that.

## Validate the collection

```bash
python3 tools/validate.py
```

Checks all 120 skills for frontmatter compliance (name, description
with TRIGGERS, category, version), required sections, real substance,
unique slugs, and that `catalog.json` / `CATALOG.md` match the folders.
Regenerate skills and catalogues from the authored data with
`python3 tools/build_skills.py`.

## Contributing

Issues and pull requests welcome. The bar: keep the guardrails intact,
keep every skill substantive and specific (no template stubs), and run
the validator. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Lionel Sim, The AI Capitol.
