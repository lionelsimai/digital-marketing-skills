---
name: onboarding-activation-audit
description: |
  Audit onboarding against the activation behaviours that predict retention, and redesign the path to the first value moment.
  TRIGGERS - Use when user needs help with onboarding and activation audit for PLG tasks.
category: Growth Experiments & PLG
version: 1.0
---
# Onboarding Activation Audit

## What this skill does

Finds the gap between signing up and getting value: measures the activation funnel, identifies the aha behaviours from cohort data, and rebuilds onboarding to drive exactly those.

## Inputs to collect

- Cohort data: retained vs churned users' early behaviours
- Current onboarding flow (every step, email, prompt)
- Activation funnel analytics by step and day

## Workflow

1. **Define activation from data** - From the cohort analysis: the 1-3 behaviours in the first days that separate retained users. Activation = completing those, not 'finished the tour'.
2. **Map the current path's friction** - Walk the flow as a new user on a cold start: count steps, decisions, dead ends and time-to-first-value. Screenshot everything.
3. **Segment the drop-offs** - Where users stall: before starting, mid-setup, at the value moment, or after (no second session). Each stall has a different cure.
4. **Redesign around the aha** - Remove or defer every step that doesn't serve the activation behaviours; add guidance (templates, defaults, examples) that makes the value moment hard to miss.
5. **Instrument and iterate** - Per-step activation funnel reviewed weekly; each change shipped as an experiment with the activation rate as the primary metric.

## Deliverable

- Activation definition with evidence
- Onboarding friction map with screenshots
- Redesign spec and experiment queue

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Activation rate (new users completing the aha behaviours) | The programme's headline metric |
| Median time to activation | Faster usually compounds into retention |
| Day-30 retention of activated vs non-activated | Validates the activation definition each quarter |

## Quality checklist

- [ ] Activation behaviours derived from retention data, not intuition
- [ ] Every onboarding step justifies itself against the aha
- [ ] Cold-start walkthrough done on a real new account

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Growth never overrides consent or honesty: no spam invites, no contact scraping for referral mechanics, no dark-pattern virality.
- Experiments on pricing and billing must be transparent to affected users - no silent price tests on existing customers' renewals.
