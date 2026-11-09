---
name: schema-markup-implementation
description: |
  Plan and validate structured data: Organization, LocalBusiness, Article, FAQ, Product and Breadcrumb schema that matches visible content.
  TRIGGERS - Use when user needs help with schema markup and structured data implementation tasks.
category: SEO
version: 1.0
---
# Schema Markup Implementation

## What this skill does

Adds the structured data a site qualifies for - accurately, validly, and only where it describes content a visitor can actually see.

## Inputs to collect

- Page templates and content types list
- Business details: legal name, logo, contact, locations
- Current schema state from a validator crawl

## Workflow

1. **Map types to templates** - Assign schema per template: Organization/LocalBusiness site-wide, Article for editorial, Product where price/offer data is real, BreadcrumbList everywhere.
2. **Write the JSON-LD** - Generate clean JSON-LD per template with required and recommended properties, pulling values from the same data that renders the page.
3. **Keep it truthful** - FAQ schema only for questions visibly answered on the page; review markup only for genuine, displayed reviews with real counts.
4. **Validate and test** - Run every template through schema validators and the Rich Results Test; fix errors, triage warnings by eligibility impact.
5. **Monitor after launch** - Watch Search Console enhancement reports for new errors after releases; add schema checks to the release checklist.

## Deliverable

- Template-to-schema map
- Validated JSON-LD snippets per template
- Enhancement-report monitoring routine

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Templates passing validation | 100% of in-scope templates |
| Rich result impressions | From Search Console performance by search appearance |
| Enhancement errors after releases | Target zero unaddressed for 14+ days |

## Quality checklist

- [ ] Schema describes only visible, real content
- [ ] No fabricated ratings, prices or FAQ content
- [ ] Values come from page data, not hard-coded copies that drift

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- White-hat only: no purchased links, link schemes, PBNs, keyword stuffing, cloaking or scraped/spun content. Earn coverage and links with assets worth citing.
- Never mark up reviews, ratings, prices or offers that do not exist on the page - that is a manual-action risk.
