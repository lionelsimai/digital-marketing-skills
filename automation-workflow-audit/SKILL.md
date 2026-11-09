---
name: automation-workflow-audit
description: |
  Audit live automations for logic errors, dead ends, conflicts and zombie workflows - before they embarrass or cost you.
  TRIGGERS - Use when user needs help with marketing automation workflow audit tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Automation Workflow Audit

## What this skill does

Finds the workflows that are silently broken, duplicated or fighting each other, and returns the system to a state one person can explain.

## Inputs to collect

- Workflow/automation inventory export
- Contact volume and error logs per workflow
- Business rules the workflows are meant to implement

## Workflow

1. **Inventory and classify** - List every active workflow: purpose, trigger, audience, owner, last-edited date. Anything without an owner is a finding already.
2. **Trace the logic** - For the top workflows by volume: follow branches, check exit conditions, look for loops, missing fallbacks and filters that can never match (or always match).
3. **Hunt conflicts** - Map which workflows can touch the same contact on the same day; check frequency caps and priority order. Conflict pairs get explicit precedence rules.
4. **Kill the zombies** - Workflows with zero enrolments in 90 days, obsolete offers, or departed owners: pause with a note, archive after one cycle. Deleting history is not required; stopping silent sends is.
5. **Document the system** - One page per workflow (purpose, trigger, rules, owner, review date) in a shared register. The register is the audit's lasting value.

## Deliverable

- Workflow register with owners and review dates
- Defect list: logic errors, conflicts, dead ends
- Zombie archive list with rationale

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Workflows without owners | To zero |
| Contacts hit by conflicting workflows per month | Should fall as precedence rules land |
| Error/failure rate per workflow run | Trended after the audit |

## Quality checklist

- [ ] High-volume workflows traced branch by branch
- [ ] Every paused workflow has a note and a review date
- [ ] Register stored where the whole team can find it

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
