---
name: funnel-drop-off-diagnosis
description: |
  Diagnose where and why a funnel loses people: step analytics, session evidence and targeted fixes per leak.
  TRIGGERS - Use when user needs help with funnel drop-off analysis and diagnosis tasks.
category: CRO & Landing Pages
version: 1.0
---
# Funnel Drop-Off Diagnosis

## What this skill does

Moves beyond 'conversion is low' to a per-step diagnosis with evidence - so fixes target the actual leak instead of redesigning everything.

## Inputs to collect

- Step-level funnel data (sessions, progression, conversion)
- Device and source breakdowns per step
- Session recordings/heatmaps and any exit feedback

## Workflow

1. **Quantify each step's leak** - Compute progression rates step by step, segmented by device and source. The biggest absolute leak and the biggest relative leak are both named - they may differ.
2. **Watch real sessions at the leak** - Review 20-30 recordings at the worst step. Classify what you see: confusion, distrust, technical failure, price shock, distraction.
3. **Cross-check the technical layer** - Speed, errors, and browser/device-specific breakage at that step. A broken step masquerades as a copy problem with depressing regularity.
4. **Form the fix hypothesis** - One hypothesis per leak, in the standard format, with the fix sketched and the expected effect sized from the step's traffic.
5. **Fix or test by confidence** - Obvious breakage gets fixed immediately; judgement calls become A/B tests. Track the step rate after each change with dates annotated.

## Deliverable

- Step leak table with device/source segments
- Diagnosis per leak with session evidence
- Fix/test queue ordered by recovered-value estimate

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Step progression rates | Trended weekly with change annotations |
| Recovered conversions per fix | Leak size x improvement - the diagnosis dividend |
| Mobile vs desktop gap per step | A persistent gap is a standing bug report |

## Quality checklist

- [ ] Diagnosis cites observed behaviour, not just aggregate rates
- [ ] Technical breakage ruled in or out explicitly
- [ ] Every leak ends as fix-now or test - never 'monitor' without a metric and date

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- No dark patterns: no fake countdowns, confirm-shaming, hidden costs or pre-ticked add-ons. Conversion bought with deception is refunded with interest in trust.
- Social proof must be real: genuine testimonials with permission, accurate numbers, no fabricated reviews or logos.
