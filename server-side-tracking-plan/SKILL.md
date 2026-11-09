---
name: server-side-tracking-plan
description: |
  Plan server-side tracking and conversion APIs: what to send, deduplication, consent gating and data quality controls.
  TRIGGERS - Use when user needs help with server-side tracking and conversions API planning tasks.
category: Web & Marketing Analytics
version: 1.0
---
# Server-Side Tracking Plan

## What this skill does

Improves measurement resilience the legitimate way: first-party, consent-respecting server events that deduplicate with browser events instead of double-counting.

## Inputs to collect

- Current browser tracking setup and its known losses
- Platform conversion APIs in scope (Meta CAPI, Google enhanced conversions, etc.)
- Consent management platform and how consent state is stored

## Workflow

1. **Justify each event** - Server-side is for value-bearing events (lead, purchase, key milestones) where browser loss distorts optimisation. Pageviews don't need a server pipeline.
2. **Design deduplication** - Shared event IDs between browser and server sends, documented per platform. Dedup failure is worse than browser-only: it invents conversions.
3. **Gate on consent** - Server events fire only with the same consent state a browser event would require. Consent is checked server-side too - 'the server can't see the banner' is not an excuse.
4. **Spec the data payload** - Per event: parameters, matching keys (hashed where required), value and currency rules, and what must never be sent (sensitive data, free-text PII).
5. **Monitor match and error rates** - Platform diagnostics reviewed weekly during rollout: match quality, dedup rate, rejected events. Set alerts for sudden drops.

## Deliverable

- Server-side tracking plan: events, payloads, dedup design
- Consent gating spec
- Rollout and monitoring checklist

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Deduplication rate | Matched browser/server pairs vs total - the design's proof |
| Event match quality scores | Per platform diagnostics |
| Conversion count reconciliation | Platform vs CRM/billing variance stays within its historical band |

## Quality checklist

- [ ] Consent checked server-side before any send
- [ ] Event IDs shared and dedup tested with real test conversions
- [ ] No sensitive or prohibited data in payloads

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Track only with consent where required: respect consent mode, PDPA/GDPR obligations and platform policies. No fingerprinting workarounds, no tracking people who said no.
- Report uncertainty honestly: modelled and sampled data labelled as such; never present platform attribution as ground truth.
- Server-side tracking must never be used to circumvent consent choices, platform privacy features or ad-blockers' user intent. If the user said no, the answer is no.
