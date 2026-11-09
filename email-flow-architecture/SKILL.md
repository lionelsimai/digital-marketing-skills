---
name: email-flow-architecture
description: |
  Design the complete automated flow architecture: triggers, journeys, exclusions and the priority order to build them in.
  TRIGGERS - Use when user needs help with email automation flow architecture tasks.
category: Email & Lifecycle Marketing
version: 1.0
---
# Email Flow Architecture

## What this skill does

Maps every automated journey a list needs - welcome, nurture, abandon, post-purchase/onboarding, reactivation - as one architecture without overlaps or dead ends.

## Inputs to collect

- Business model: how leads and customers are created
- Current flows and their performance (if any)
- ESP capabilities and data available for triggers

## Workflow

1. **Inventory the moments** - List every lifecycle moment that deserves an automated response: signup, first purchase, onboarding milestone, inactivity, renewal window, referral moment.
2. **Design each journey** - Per flow: trigger, goal, emails (count and spacing), exit conditions, and what it must never collide with (campaigns, other flows).
3. **Set global rules** - Frequency caps across all flows, suppression logic (don't pitch buyers what they just bought), and quiet rules for transactional vs marketing.
4. **Prioritise the build order** - Rank by revenue proximity and list coverage: welcome and abandon flows usually first, winback later. One flow live beats five drafted.
5. **Instrument everything** - Per flow: the primary metric, a holdout where feasible, and a review date. Architecture includes measurement or it's decoration.

## Deliverable

- Flow architecture map: triggers, emails, exits, rules
- Build priority order with rationale
- Global frequency and suppression rule set

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Revenue per recipient per flow | The architecture's unit economics |
| Flow coverage of lifecycle moments | Share of key moments with a live journey |
| Unsubscribe/complaint rate across flows | Architecture health guardrail |

## Quality checklist

- [ ] Exit and suppression rules defined per flow
- [ ] No two flows can email the same person the same day by accident
- [ ] Every flow has a named primary metric

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Permission-based sending only: no purchased or scraped lists, ever. Clear consent, honest sender identity, one-click unsubscribe in every email.
- Deliverability is trust: no deceptive subject lines, no hidden downsides, no dark patterns in preference or unsubscribe flows.
