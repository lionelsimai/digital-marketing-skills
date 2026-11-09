---
name: incrementality-and-geo-testing
description: |
  Design incrementality tests - geo splits, holdouts, on/off - that answer whether a channel causes results or just claims them.
  TRIGGERS - Use when user needs help with incrementality and geo split testing tasks.
category: Paid Media Planning & Buying
version: 1.0
---
# Incrementality and Geo Testing

## What this skill does

Produces a defensible test design for the hardest question in media: what would have happened without this spend.

## Inputs to collect

- Channel or campaign in question and its claimed results
- Geo or audience units that can be split cleanly
- Baseline period data and the outcome metric that matters (revenue, qualified leads)

## Workflow

1. **Frame the decision** - Write the decision this test informs (scale, cut, keep) and the effect size that would change it. Tests without decisions are academic.
2. **Build matched groups** - Split geos/audiences into test and control matched on historical outcomes, size and seasonality. Randomise where possible; document matching quality.
3. **Set duration and power** - Run long enough to capture the sales cycle and enough volume to detect the decision-relevant effect. Underpowered tests conclude 'no effect' by design - avoid them.
4. **Freeze confounders** - No simultaneous launches, promos or pricing changes in either group. Log anything that breaches the freeze.
5. **Read results plainly** - Compare outcome rates test vs control with uncertainty ranges. Report 'we can't tell' when that's the truth - it's a valid, money-saving answer.

## Deliverable

- Test design document: groups, duration, decision rule
- Confounder freeze log
- Results memo with uncertainty and the decision taken

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Incremental outcome per dollar | Test minus control, per spend |
| Detection power achieved | Whether the test could have seen the effect it hunted |
| Decision follow-through | Whether the result actually changed the budget |

## Quality checklist

- [ ] Groups matched and documented before launch
- [ ] Outcome is a business metric, not a platform metric
- [ ] Negative or null results reported with the same prominence as positive ones

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Buy media the business can measure. If a placement cannot be tracked or brand-lift measured, size it as an experiment, not a pillar.
