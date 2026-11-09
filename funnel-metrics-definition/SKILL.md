---
name: funnel-metrics-definition
description: |
  Define funnel metrics once, in writing: every stage metric's formula, source and owner - the house dictionary.
  TRIGGERS - Use when user needs help with funnel metrics definitions and KPI dictionary tasks.
category: Web & Marketing Analytics
version: 1.0
---
# Funnel Metrics Definition

## What this skill does

Ends metric arguments permanently by publishing the formulas: when two reports disagree after this, one of them is simply wrong.

## Inputs to collect

- Funnel stages (from lifecycle definitions)
- Systems of record per stage (GA4, CRM, billing)
- Current conflicting definitions in the wild

## Workflow

1. **Inventory the confusion** - Collect every metric currently reported by two or more teams with different formulas (CPA, MQL rate, activation are usual suspects). The conflicts list is the work plan.
2. **Write each definition completely** - Formula, inclusions/exclusions, attribution window, data source, refresh cadence, owner. If a definition fits on one line, it's not finished.
3. **Reconcile with finance** - Revenue-adjacent metrics (CAC, payback, LTV) get agreed with whoever owns the P&L, using billing data as truth for money numbers.
4. **Publish where people work** - The dictionary lives one click from the dashboards and report templates, versioned, with a change log. Changes apply prospectively and are announced.
5. **Enforce in reviews** - Reports using off-dictionary metrics get returned for correction - kindly, every time. Standards live or die in the second month.

## Deliverable

- Funnel metrics dictionary (versioned)
- Conflict resolution log
- Change process for definitions

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Conflicting-definition count | To zero, verified by sampling reports |
| Report correction rate | Should fall as the dictionary beds in |
| Time to produce standard reports | Falls when nobody re-derives formulas |

## Quality checklist

- [ ] Money metrics reconciled to billing/finance data
- [ ] Every definition has an owner and a source system
- [ ] Dictionary versioned with a visible change log

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Track only with consent where required: respect consent mode, PDPA/GDPR obligations and platform policies. No fingerprinting workarounds, no tracking people who said no.
- Report uncertainty honestly: modelled and sampled data labelled as such; never present platform attribution as ground truth.
