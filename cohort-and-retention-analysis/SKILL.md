---
name: cohort-and-retention-analysis
description: |
  Run cohort analysis on customers or subscribers: acquisition cohorts, retention curves and where lifecycle value is created or lost.
  TRIGGERS - Use when user needs help with cohort and retention analysis for marketing tasks.
category: Web & Marketing Analytics
version: 1.0
---
# Cohort and Retention Analysis

## What this skill does

Reveals what averages conceal: whether newer customers are better or worse than older ones, and which early behaviours predict staying.

## Inputs to collect

- Customer/subscriber records with start dates and activity/revenue over time
- Acquisition source per cohort member
- Product/engagement events that might predict retention

## Workflow

1. **Build the cohort table** - Rows: acquisition month (or campaign). Columns: period since start. Cells: retained share and revenue per member. Use one clear retention definition (active, paying, or engaged) and state it.
2. **Read the curves** - Find where curves flatten (your retained core) and where the steepest drop lives. The drop point is the onboarding problem; the flattening level is product-market fit's signature.
3. **Compare cohorts fairly** - Same-age comparisons only (month-3 of this cohort vs month-3 of last). Check whether acquisition source or campaign explains quality differences.
4. **Hunt the predictor behaviours** - Compare retained vs churned members' first-14-days behaviour. The 1-3 actions that separate them become the activation targets.
5. **Translate into actions** - Acquisition: favour sources with good same-age retention. Lifecycle: build onboarding around the predictor behaviours. Product: fix the drop point's known friction.

## Deliverable

- Cohort table and retention curves
- Source-quality ranking by same-age retention
- Predictor behaviour list for activation work

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Month-3/6/12 retention by cohort | Trended - improving cohorts mean the system is learning |
| Revenue per cohort member at same age | Quality of growth, not just quantity |
| Predictor behaviour adoption rate | New users completing the retention-linked actions |

## Quality checklist

- [ ] Retention definition stated and consistent
- [ ] Cohorts compared at equal ages only
- [ ] Small cohorts flagged before conclusions drawn

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Track only with consent where required: respect consent mode, PDPA/GDPR obligations and platform policies. No fingerprinting workarounds, no tracking people who said no.
- Report uncertainty honestly: modelled and sampled data labelled as such; never present platform attribution as ground truth.
