---
name: martech-stack-review
description: |
  Review the marketing technology stack: what each tool earns, overlaps, data flows and the consolidate/keep/replace decisions.
  TRIGGERS - Use when user needs help with martech stack audit and review tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Martech Stack Review

## What this skill does

Applies zero-based thinking to the stack: every tool must justify its cost with usage and outcomes, and the data flows between tools must be mapped and owned.

## Inputs to collect

- Tool inventory with costs, contracts and renewal dates
- Usage data and the workflows each tool supports
- Data flow map (or the integrations list to build one from)

## Workflow

1. **Inventory with owners** - Every tool: cost, owner, primary users, the jobs it does, renewal date. Tools without owners are renewal accidents waiting to happen.
2. **Score usage vs promise** - Active users vs licences bought, features used vs features paid for, and the outcome each tool claims to drive. Interview the actual users, not just the buyer.
3. **Map overlaps and gaps** - Where two tools do the same job, pick the survivor by workflow fit, not sunk cost. Where a needed job has no tool, name the gap explicitly.
4. **Trace the data flows** - Diagram how contact, consent and conversion data moves between systems, and where it breaks or duplicates. Integration debt is usually the real stack problem.
5. **Decide and sequence** - Keep / consolidate / replace / retire per tool, sequenced around renewal dates, with migration effort estimated honestly.

## Deliverable

- Stack inventory with owners, costs and verdicts
- Data flow diagram with break points
- 12-month stack roadmap tied to renewals

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Cost per active user per tool | Exposes shelfware in one number |
| Licence utilisation | Paid seats actually used monthly |
| Integration failure rate | Sync errors and silent data gaps per month |

## Quality checklist

- [ ] Every tool has a named owner and a verdict
- [ ] Consent and suppression flows traced across systems
- [ ] Decisions sequenced before renewal deadlines, not after auto-renewal

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
