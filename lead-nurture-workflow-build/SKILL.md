---
name: lead-nurture-workflow-build
description: |
  Build a nurture workflow that moves leads by stage: educational sequence, branching by engagement, and clear graduation rules.
  TRIGGERS - Use when user needs help with lead nurture workflow build tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Lead Nurture Workflow Build

## What this skill does

Designs nurture as a guided path - each email earns the next - rather than a drip of random content sprayed at everyone who ever downloaded something.

## Inputs to collect

- Entry source and what the lead originally wanted
- Content assets mapped to journey stages
- Graduation definition: what behaviour earns a sales conversation

## Workflow

1. **Define the journey in 3 acts** - Problem education, solution education, proof and offer. Each act has one job and content that does it; leads can skip acts by behaviour, never by time alone.
2. **Write to the entry intent** - The first emails continue the conversation the lead started (the topic they downloaded/attended), then broaden. Changing the subject abruptly is why nurture gets ignored.
3. **Branch on real signals** - High-intent actions (pricing page, repeat visits, replying) fast-track to a human. Low engagement slows cadence instead of shouting louder.
4. **Build the graduation and exit rules** - Graduate on intent threshold; exit on conversion, unsubscribe, or sales ownership. No lead lives in nurture forever - long-stay leads move to a low-cadence long-tail track.
5. **Test the whole path** - Seed records through every branch, including the boring ones. Verify tags, scoring and CRM fields update as designed.

## Deliverable

- Nurture workflow: emails, branches, timing, rules
- Content-to-stage map with gaps flagged
- Graduation/exit rule documentation

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Nurture-to-MQL conversion rate | Against entry-source baseline |
| Time to graduation | Faster is not always better - watch win rate of fast vs slow graduates |
| Engagement decay curve | Where attention dies tells you which email to fix |

## Quality checklist

- [ ] Branches tested end to end with seed records
- [ ] Fast-track to human exists for hot behaviour
- [ ] Long-tail track prevents infinite nurturing

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
