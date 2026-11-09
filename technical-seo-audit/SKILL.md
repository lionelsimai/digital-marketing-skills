---
name: technical-seo-audit
description: |
  Run a technical SEO audit: crawlability, indexation, site structure, Core Web Vitals, duplicates and canonicals - with a prioritised fix list.
  TRIGGERS - Use when user needs help with technical SEO audit tasks.
category: SEO
version: 1.0
---
# Technical SEO Audit

## What this skill does

Finds the technical issues that quietly cap a site's organic performance and ranks fixes by impact and effort so developers work on what matters.

## Inputs to collect

- Site URL and CMS/platform details
- Search Console and analytics access (or exports)
- List of priority pages and known past migrations or redesigns

## Workflow

1. **Crawl and inventory** - Crawl the full site; export URL inventory with status codes, depth, word count and indexability. Compare against the sitemap and Search Console coverage.
2. **Check indexation control** - Review robots.txt, meta robots, canonicals, sitemap hygiene and parameter handling. Flag valuable pages excluded and junk pages indexed.
3. **Assess performance and mobile** - Pull Core Web Vitals field data for top templates. Separate template-wide problems from one-off heavy pages.
4. **Review structure and duplicates** - Check internal linking depth for money pages, duplicate titles/content, redirect chains and broken internal links.
5. **Prioritise the fix list** - Score each issue by traffic at risk x fix effort. Deliver as a developer-ready list: issue, evidence URLs, fix, acceptance test.

## Deliverable

- Audit report with evidence URLs per issue
- Prioritised fix backlog (impact x effort) with acceptance tests
- Indexation summary: indexed, excluded, and should-be-excluded

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Valid indexed pages vs intended | In Search Console coverage, trended monthly |
| Core Web Vitals pass rate | Share of URL groups passing all three thresholds |
| Crawl errors and redirect chains | Should trend to near zero for internal links |

## Quality checklist

- [ ] Findings evidenced with live URLs, not generic advice
- [ ] Fix list separates site-wide template issues from page issues
- [ ] No recommendation that risks deindexing revenue pages without a test

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- White-hat only: no purchased links, link schemes, PBNs, keyword stuffing, cloaking or scraped/spun content. Earn coverage and links with assets worth citing.
