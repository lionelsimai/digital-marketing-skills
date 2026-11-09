---
name: ga4-measurement-plan
description: |
  Write a GA4 measurement plan: business questions, events, parameters, conversions and the governance to keep it clean.
  TRIGGERS - Use when user needs help with GA4 measurement plan and event taxonomy tasks.
category: Web & Marketing Analytics
version: 1.0
---
# GA4 Measurement Plan

## What this skill does

Connects tracking to decisions before anyone touches GTM: every event exists because a business question needs it.

## Inputs to collect

- Business questions analytics must answer (funnel, revenue, retention)
- Site/app journeys and key actions
- Current GA4/GTM state and known issues

## Workflow

1. **List the decisions first** - Per journey: what will we decide with this data (fix a step, fund a channel, kill a feature). Decisions that nobody will take don't get events.
2. **Design the event taxonomy** - Consistent naming (object_action), required parameters per event, and which events mark conversions. A written taxonomy, versioned like code.
3. **Specify implementation precisely** - Per event: trigger conditions, parameters with example values, where it fires (data layer spec for developers), and QA steps.
4. **Plan the QA and debug routine** - DebugView checks, test transactions, cross-device sanity checks and a release checklist so redesigns don't silently kill tracking.
5. **Set governance** - Who can add events, the naming approval step, and a quarterly taxonomy prune. Unmanaged tags become unmanaged truth.

## Deliverable

- Measurement plan: questions, events, parameters, conversions
- Developer implementation spec (data layer)
- Governance and QA routine

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Event data quality (missing/duplicate parameter rate) | Sampled monthly from raw reports |
| Decision coverage | Share of planned business questions the data can actually answer |
| Tracking breakage incidents per release | Should fall once the release checklist exists |

## Quality checklist

- [ ] Every event maps to a stated decision
- [ ] Naming taxonomy documented and versioned
- [ ] Conversions defined by business value, not by ease of firing

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Track only with consent where required: respect consent mode, PDPA/GDPR obligations and platform policies. No fingerprinting workarounds, no tracking people who said no.
- Report uncertainty honestly: modelled and sampled data labelled as such; never present platform attribution as ground truth.
