---
name: list-hygiene-and-segmentation
description: |
  Keep the list clean and segmented by behaviour: hygiene rules, engagement tiers and segment maps that campaigns actually use.
  TRIGGERS - Use when user needs help with email list hygiene and segmentation tasks.
category: Email & Lifecycle Marketing
version: 1.0
---
# List Hygiene and Segmentation

## What this skill does

Builds the unglamorous system that makes every other email skill work: clean data in, behaviour-based segments out.

## Inputs to collect

- List export with source, dates and engagement history
- Available behavioural data: purchases, clicks, site visits
- ESP tagging/segment capabilities

## Workflow

1. **Define hygiene rules** - Automatic handling: hard bounces out immediately, soft-bounce limits, complaint suppression permanent, duplicate resolution by most recent engagement.
2. **Build engagement tiers** - Tier by recency of any real signal (click, purchase, site visit - opens alone are unreliable post-MPP): hot 0-90d, warm 91-180d, cold 181d+. Each tier gets a mailing policy.
3. **Create behavioural segments** - Segments from actions, not demographics: bought category X, viewed but never bought, flow graduates, event attendees. Each segment names its marketing use.
4. **Fix collection at the source** - Audit signup forms: confirmation/double opt-in where list quality is poor, bot protection, and source tagging so future quality is measurable per source.
5. **Schedule the rhythm** - Monthly automated hygiene, quarterly segment review, and a re-permission campaign before any cold tier is mailed again.

## Deliverable

- Hygiene rule set implemented in the ESP
- Engagement tier + behavioural segment map with mailing policies
- Signup source quality report

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Deliverability trend after hygiene | Bounce/complaint direction over 60 days |
| Revenue per email by tier | Proves tiering reflects reality |
| List decay rate | Natural churn (~20-30%/yr) made visible, not feared |

## Quality checklist

- [ ] Suppressions are permanent and honoured across systems
- [ ] Segments defined by behaviour with a stated use each
- [ ] Re-permission required before mailing cold tiers

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Permission-based sending only: no purchased or scraped lists, ever. Clear consent, honest sender identity, one-click unsubscribe in every email.
- Deliverability is trust: no deceptive subject lines, no hidden downsides, no dark patterns in preference or unsubscribe flows.
