---
name: experiment-results-writeup
description: |
  Write up experiment results so the organisation learns: context, data, decision and the next hypothesis - for wins and losses alike.
  TRIGGERS - Use when user needs help with experiment results documentation and writeup tasks.
category: CRO & Landing Pages
version: 1.0
---
# Experiment Results Writeup

## What this skill does

Converts finished tests into institutional knowledge, preventing the two classic wastes: re-running settled tests and ignoring what a loss taught.

## Inputs to collect

- Test design document and decision rule
- Raw results: primary, guardrails, segments
- Implementation notes (what actually shipped, when)

## Workflow

1. **Restate the bet** - Hypothesis, audience, primary metric and the pre-registered decision rule - quoted, not paraphrased after the fact.
2. **Report the numbers plainly** - Effect size with confidence interval, absolute numbers beside percentages, guardrail outcomes, and runtime/sample achieved vs planned.
3. **Interrogate surprises** - Segment effects, novelty/primacy suspicions, and any implementation deviations. Label speculation as speculation.
4. **State the decision and its owner** - Ship, iterate or kill - with who decided and the follow-on action. A writeup without a decision is a diary entry.
5. **Extract the reusable learning** - One or two principles for the backlog ('proof beside price beats proof in footer for this audience'). File it where future test designers will actually search.

## Deliverable

- One-page result writeup in the standard format
- Updated experiment log entry
- Follow-on hypothesis (if any) added to the backlog

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Writeup completion rate | Share of finished tests with a filed writeup - target 100% |
| Repeat-test rate | Tests re-run because results weren't findable - target zero |
| Decision implementation rate | Ship decisions actually shipped within 2 cycles |

## Quality checklist

- [ ] Decision rule quoted from the pre-registration
- [ ] Negative results filed with equal prominence
- [ ] Absolute numbers shown beside percentages

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- No dark patterns: no fake countdowns, confirm-shaming, hidden costs or pre-ticked add-ons. Conversion bought with deception is refunded with interest in trust.
- Social proof must be real: genuine testimonials with permission, accurate numbers, no fabricated reviews or logos.
