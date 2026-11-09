---
name: keyword-match-type-strategy
description: |
  Decide how to use broad, phrase and exact match with smart bidding: where each belongs and how to control them.
  TRIGGERS - Use when user needs help with keyword match type strategy tasks.
category: SEM & PPC
version: 1.0
---
# Keyword Match Type Strategy

## What this skill does

Sets a match-type policy per campaign tier so reach expands where it is safe and stays tight where money is made.

## Inputs to collect

- Current match-type performance and search term reports
- Conversion volume per campaign (smart bidding needs signal)
- Budget and risk tolerance by tier

## Workflow

1. **Assess signal readiness** - Broad match + smart bidding works when conversion volume and values are real. Below ~30 conversions/month per campaign, keep tighter control.
2. **Assign match policy by tier** - Exact for proven money terms, phrase for controlled expansion, broad only in test campaigns with capped budgets and strong negatives.
3. **Build the control kit** - Account-level negative lists, brand exclusions where needed, and weekly search-term review slots. Broad without controls is a donation.
4. **Migrate in stages** - Move one tier at a time, holding a control where possible. Judge on 2-4 weeks of data, not launch week noise.
5. **Document the policy** - Write the rule set so future builds follow it: which tier gets which match types and what evidence changes the policy.

## Deliverable

- Match-type policy by campaign tier
- Negative list and review cadence setup
- Migration plan with control groups

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Spend share on irrelevant terms | The cost of loose matching, tracked weekly |
| Incremental conversions from expansion tiers | Broad must prove it adds, not cannibalises |
| CPA stability during migration | Pre-set tolerance bands with rollback triggers |

## Quality checklist

- [ ] Conversion volume assessed before recommending broad
- [ ] Rollback criteria written before migration
- [ ] Policy documented, not held in one person's head

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Ad policy compliance: no misleading claims, no prohibited content, no trademark abuse. Ads must promise only what the landing page delivers.
- Never advertise results, prices or offers the business cannot honour today.
