---
name: ab-test-design
description: |
  Design A/B tests that produce decisions: hypothesis, primary metric, sample size, guardrails and a pre-registered decision rule.
  TRIGGERS - Use when user needs help with A/B test design and experimentation setup tasks.
category: CRO & Landing Pages
version: 1.0
---
# A/B Test Design

## What this skill does

Stops random split-testing: each test is built from an insight, powered to detect a meaningful effect, and judged by a rule written before it launches.

## Inputs to collect

- Insight or problem the test addresses (with evidence)
- Baseline conversion rate and traffic volume for the page/flow
- Minimum effect worth acting on (business decision)

## Workflow

1. **Write the hypothesis properly** - Because [insight], changing [element] for [audience] will [expected effect on primary metric]. If you can't fill the brackets, you're not ready to test.
2. **Pick one primary metric** - The metric that decides. Guardrail metrics (revenue per visitor, unsubscribes, support load) get veto power, not decision power.
3. **Size and schedule it** - Compute required sample from baseline, minimum detectable effect and standard power/significance. State the expected runtime; if it exceeds 4-6 weeks, choose a higher-traffic surface or a bigger change.
4. **Pre-register the decision rule** - Ship if primary metric lifts by at least X with guardrails intact at the planned end date. No peeking to significance and stopping early - that's how false wins happen.
5. **Document and share the result** - Win, lose or flat: the result, the learning and the decision go into the experiment log where the whole team can find them.

## Deliverable

- Test design document: hypothesis, metrics, sizing, decision rule
- QA record (targeting, splits, tracking verified)
- Result entry in the experiment log

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Decision rate | Share of tests ending in a clear ship/kill decision |
| Realised vs predicted lift | Calibrates future hypotheses |
| False-win incidents (shipped tests that regressed) | Should fall as pre-registration discipline bites |

## Quality checklist

- [ ] Sample size computed before launch
- [ ] Decision rule written and dated before launch
- [ ] Tracking verified in both variants before full traffic

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- No dark patterns: no fake countdowns, confirm-shaming, hidden costs or pre-ticked add-ons. Conversion bought with deception is refunded with interest in trust.
- Social proof must be real: genuine testimonials with permission, accurate numbers, no fabricated reviews or logos.
- Never stop a test early because it 'hit significance', and never extend a loser hoping it turns. Both convert statistics into astrology.
