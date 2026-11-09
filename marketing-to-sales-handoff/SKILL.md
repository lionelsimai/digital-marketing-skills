---
name: marketing-to-sales-handoff
description: |
  Design the MQL-to-SQL handoff: routing rules, speed-to-lead SLA, context pack and the feedback loop that keeps quality honest.
  TRIGGERS - Use when user needs help with marketing to sales handoff and SLA design tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Marketing-to-Sales Handoff (MQL/SQL SLA)

## What this skill does

Makes the handoff a designed system - right lead, right rep, full context, fast - with a feedback loop that improves lead quality over time.

## Inputs to collect

- MQL definition and scoring thresholds
- Sales team structure and routing logic (territory, size, product)
- Current speed-to-lead and follow-up data

## Workflow

1. **Define the handoff packet** - Every MQL arrives with: fit data, intent signals with dates, source campaign, and the content they consumed. Reps should never start from zero.
2. **Set routing and ownership** - Rules for assignment (round-robin within segment, account ownership for named accounts), plus a named backup when the owner is away. Unowned leads are dead leads.
3. **Agree the SLA in numbers** - First touch within X minutes/hours by lead temperature, minimum attempt pattern (channels and cadence), and disposition deadline. Both sides sign; the CRM enforces with alerts.
4. **Build the feedback loop** - Dispositions flow back weekly: accepted, rejected (reason), converted. Marketing reviews rejection Pareto and adjusts targeting/scoring visibly.
5. **Run the joint review** - Monthly 30 minutes, one agenda: SLA compliance, rejection reasons, win stories. No blame items without data attached.

## Deliverable

- Handoff spec: packet, routing, SLA numbers
- CRM alert and reporting setup
- Feedback loop and joint review cadence

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Speed to first touch (median + % within SLA) | The strongest controllable predictor of conversion |
| MQL-to-SQL acceptance rate | The handoff's quality score |
| SQL-to-opportunity rate by source | Closes the loop on which marketing actually works |

## Quality checklist

- [ ] SLA signed by both function leads
- [ ] Rejection without a reason code is impossible in the CRM
- [ ] Context packet tested with a real rep on a real lead

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
