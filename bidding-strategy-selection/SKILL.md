---
name: bidding-strategy-selection
description: |
  Choose and manage bid strategies - tCPA, tROAS, max conversions, manual - based on data volume, value quality and margin.
  TRIGGERS - Use when user needs help with Google Ads bidding strategy selection tasks.
category: SEM & PPC
version: 1.0
---
# Bidding Strategy Selection

## What this skill does

Matches the bidding strategy to the data the account actually has, with a migration path and guardrails instead of defaulting to whatever the platform suggests.

## Inputs to collect

- Conversion volume and value data by campaign (last 30-90 days)
- Margins and target CPA/ROAS by product or lead type
- Budget stability and seasonality patterns

## Workflow

1. **Audit the conversion signal** - Count conversions per campaign and check value integrity. Strategies are only as smart as the signal; fix tracking before touching bids.
2. **Pick by volume and value** - High volume + real values: tROAS. High volume, single action: tCPA or max conversions with a cap. Low volume: maximise clicks with CPC ceilings or manual for control.
3. **Set targets from reality** - Initial targets within 10-20% of recent actual CPA/ROAS. Fantasy targets starve campaigns; the learning period is not an excuse for a dead month.
4. **Manage the learning period** - Freeze structural changes during learning; judge after volume thresholds (e.g. 2-3x target conversions), not calendar impatience.
5. **Review and step targets** - Monthly: tighten or loosen targets in small steps tied to business margin changes, documenting each change and its effect.

## Deliverable

- Bid strategy assignment per campaign with rationale
- Target-setting sheet tied to margins
- Change log template for bid/target adjustments

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Actual CPA/ROAS vs target | By campaign, with volume context |
| Conversion value per dollar by tier | Guards against optimising to cheap junk |
| Volatility after changes | Large swings after target changes signal over-steering |

## Quality checklist

- [ ] Tracking verified before any smart bidding rollout
- [ ] Targets derived from margins, not copied from platform recommendations
- [ ] Learning-period rules agreed with stakeholders in advance

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Ad policy compliance: no misleading claims, no prohibited content, no trademark abuse. Ads must promise only what the landing page delivers.
- Never advertise results, prices or offers the business cannot honour today.
