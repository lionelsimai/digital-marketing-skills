---
name: retention-curve-analysis
description: |
  Analyse retention curves to find the retained core, the drop points and the product/marketing fixes each implies.
  TRIGGERS - Use when user needs help with retention curve analysis tasks.
category: Growth Experiments & PLG
version: 1.0
---
# Retention Curve Analysis

## What this skill does

Reads the retention curve as the business's biography: where users decide to stay, where they quietly leave, and what the flat part of the curve is worth.

## Inputs to collect

- Cohort retention data (from the cohort analysis)
- Product usage events across the lifecycle
- Pricing/plan and channel dimensions for segmentation

## Workflow

1. **Plot and segment the curves** - By cohort, channel, plan and activation status. The aggregate curve is the least useful version - segments are where the stories are.
2. **Locate the cliffs and the plateau** - Mark the steepest drop intervals and the point where the curve flattens. The flattening level = your retained core share; the cliffs = your fix list, in order.
3. **Interrogate the first cliff** - Session data, exit surveys and support themes for users who left at the first cliff. Classify: never activated, activated but no habit, value stopped growing.
4. **Value the plateau** - Revenue and expansion behaviour of the retained core: what they use, what they buy next, what they say. The plateau defines your best-customer profile better than any persona workshop.
5. **Assign the fixes** - Each cliff gets an owner and a fix class: onboarding (cliff 1), habit/engagement (mid), value expansion (late). Re-measure the same cohorts' successors next cycle.

## Deliverable

- Segmented retention curves with cliffs and plateau marked
- First-cliff diagnosis with evidence
- Fix assignments per cliff with owners

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Plateau level (retained core share) | The product-market-fit gauge, trended by cohort |
| First-cliff survival rate | The onboarding programme's report card |
| Retained-core revenue share | How much of the business the plateau carries |

## Quality checklist

- [ ] Curves segmented, not just aggregate
- [ ] First cliff diagnosed with user evidence
- [ ] Fixes assigned per cliff with owners

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Growth never overrides consent or honesty: no spam invites, no contact scraping for referral mechanics, no dark-pattern virality.
- Experiments on pricing and billing must be transparent to affected users - no silent price tests on existing customers' renewals.
