---
name: lead-scoring-model-design
description: |
  Design a lead scoring model combining fit and behaviour, validated against real closed-won/lost outcomes.
  TRIGGERS - Use when user needs help with lead scoring model design tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Lead Scoring Model Design

## What this skill does

Builds scoring that predicts sales outcomes instead of rewarding activity theatre - points from evidence, thresholds from capacity.

## Inputs to collect

- Closed-won and closed-lost records with firmographic and activity data (6-12 months)
- Sales team's definition of a good lead, in their words
- Current routing capacity (how many leads sales can work well)

## Workflow

1. **Analyse what actually closed** - Compare won vs lost on attributes (size, industry, role) and behaviours (pages, events, replies). Score what differs, not what feels right.
2. **Split fit and intent** - Two scores, kept separate: Fit (who they are) and Intent (what they're doing now). A high-intent bad-fit lead and a perfect-fit cold lead need different handling.
3. **Set decay and negatives** - Intent points decay (30-60 days is typical); negative signals subtract (competitor, student, unsubscribed, wrong region). Scores that only rise are fiction.
4. **Calibrate thresholds to capacity** - Set the MQL threshold so the volume matches what sales can work within SLA. Backtest: what share of last quarter's wins would have crossed it, and how early?
5. **Review monthly, rebuild quarterly** - Track score-band conversion rates monthly. If a band stops predicting, the model gets rebuilt - not defended.

## Deliverable

- Scoring model: fit + intent points tables with decay and negatives
- Threshold calibration with backtest results
- Monthly band-performance review template

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Conversion rate by score band | Bands must separate outcomes; if they don't, the model is decoration |
| Win capture rate | Share of eventual wins that crossed MQL in time to matter |
| Sales acceptance rate of MQLs | The trust metric - low acceptance means model or handoff is broken |

## Quality checklist

- [ ] Model derived from closed data, not opinion
- [ ] Negative scoring and decay implemented
- [ ] Threshold backtested against last quarter's wins

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
