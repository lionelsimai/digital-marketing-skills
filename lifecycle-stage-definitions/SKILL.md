---
name: lifecycle-stage-definitions
description: |
  Define lifecycle stages with entry/exit criteria both marketing and sales sign: subscriber, MQL, SQL, opportunity, customer, evangelist.
  TRIGGERS - Use when user needs help with lifecycle stage definitions and funnel governance tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Lifecycle Stage Definitions

## What this skill does

Ends the oldest marketing-sales argument - what counts as a lead - with written, data-checkable definitions and movement rules.

## Inputs to collect

- Current stage usage and where records get stuck
- Sales process stages and qualification criteria
- Reporting needs: what the business reviews weekly

## Workflow

1. **Define each stage by evidence** - Entry criteria must be observable in the CRM (actions taken, data present), never 'seems interested'. Include the disqualifiers too.
2. **Set movement rules** - Forward movement, backward movement (recycling), and who can move a record. SQL rejection requires a reason code - that data is gold for marketing.
3. **Assign stage owners and SLAs** - Marketing owns nurture-stage quality; sales owns SQL response time and disposition completeness. Write the numbers down.
4. **Instrument the funnel** - Stage timestamps on every record so conversion and velocity are computable. Definitions without timestamps are unmeasurable.
5. **Run the monthly stage review** - Conversion by stage, stuck-record report, rejection reason Pareto. Adjust definitions only in the review, with changes logged.

## Deliverable

- Stage definition sheet: criteria, disqualifiers, owners, SLAs
- Movement and recycling rules
- Stage health dashboard spec

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Stage conversion rates | The funnel's truth, by cohort |
| Median days in stage | Velocity reveals friction definitions can't |
| SQL rejection rate + reason mix | Rising 'bad fit' means targeting; rising 'no response' means speed or persistence |

## Quality checklist

- [ ] Criteria are checkable in the CRM, not judgement calls
- [ ] Rejection reason codes are mandatory and used
- [ ] Both marketing and sales leads have signed the definitions

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
