---
name: viral-loop-analysis
description: |
  Analyse viral and network loops: cycle time, conversion per step and the realistic ceiling on loop-driven growth.
  TRIGGERS - Use when user needs help with viral loop and network effects analysis tasks.
category: Growth Experiments & PLG
version: 1.0
---
# Viral Loop Analysis

## What this skill does

Applies honest maths to virality claims: models the loop's steps, measures each conversion, and states plainly whether the loop can carry growth or only assist it.

## Inputs to collect

- Loop description: how a user creates exposure for the next user
- Step data: exposure, click, signup, activation rates
- Cycle time from signup to generating new exposure

## Workflow

1. **Draw the loop precisely** - Each step a user takes and each conversion between steps, including the unglamorous ones (the invite email landing in spam is a step).
2. **Measure every step** - Instrument or estimate with labels: invites sent per user, invite open/click rate, signup rate, activation rate, time per cycle. Estimated steps are flagged, not blended in.
3. **Compute the loop factor** - K = invites per user x conversion to activated user. Report K with its inputs; K under 1 means the loop amplifies other channels - valuable, but not self-sustaining, and the plan must say so.
4. **Find the cheapest step to improve** - Sensitivity: which step's improvement moves K most per unit effort? Usually cycle time and invite rate, not the landing page.
5. **State the ceiling** - Model saturation: audience size, overlap and fatigue. Loops decay; the analysis names when, so plans don't bank on permanent exponential growth.

## Deliverable

- Loop diagram with measured step rates
- K-factor calculation with flagged estimates
- Improvement priorities and ceiling model

## Success metrics

| Metric | How to read it |
|--------|---------------|
| K-factor trend | By cohort and month |
| Cycle time | Shorter cycles compound faster at equal K |
| Loop-attributed activated users | Share of growth honestly credited to the loop |

## Quality checklist

- [ ] Every step rate measured or explicitly flagged as estimated
- [ ] K reported with inputs visible
- [ ] Ceiling/saturation addressed in the conclusions

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Growth never overrides consent or honesty: no spam invites, no contact scraping for referral mechanics, no dark-pattern virality.
- Experiments on pricing and billing must be transparent to affected users - no silent price tests on existing customers' renewals.
