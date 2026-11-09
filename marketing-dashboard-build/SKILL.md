---
name: marketing-dashboard-build
description: |
  Build a marketing dashboard that gets used: one page per audience, decision-linked metrics, and honest data plumbing.
  TRIGGERS - Use when user needs help with marketing dashboard design and build tasks.
category: Web & Marketing Analytics
version: 1.0
---
# Marketing Dashboard Build

## What this skill does

Designs dashboards around the decisions of their readers - executives, operators, channel owners - instead of a wall of every available metric.

## Inputs to collect

- Readers and the decisions each makes
- Data sources and their reliability/latency
- House metric definitions (from the funnel metrics standard)

## Workflow

1. **Start from decisions, again** - Interview each reader: what do you decide weekly/monthly, and what would you need to see? Every widget must cite its decision or be cut.
2. **Structure by question** - Top layer: are we winning (outcome KPIs vs target). Middle: why (funnel and channel drivers). Bottom: what we changed (activity and experiment log). One page per layer, not one endless scroll.
3. **Plumb the data honestly** - Automated connectors where reliable; labelled manual imports where not. Freshness timestamps on every source - stale data displayed as stale.
4. **Add targets and annotations** - Targets on the charts, and a shared annotation habit: launches, outages, campaigns marked on the timeline so movements get explained, not debated.
5. **Review usage quarterly** - Which pages get opened, which widgets get ignored? Prune ruthlessly. A dashboard nobody opens is a reporting tax.

## Deliverable

- Layered dashboard (outcome, drivers, activity)
- Metric definition sheet for every widget
- Annotation and freshness conventions

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Dashboard usage by intended readers | Opens per week from the actual audience |
| Time to answer standard questions | E.g. 'what did paid social deliver last month' in under 2 minutes |
| Data freshness compliance | Share of sources within their stated latency |

## Quality checklist

- [ ] Every widget names its decision
- [ ] Freshness visible on the dashboard itself
- [ ] Definitions match the house standard - no per-dashboard variants

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Track only with consent where required: respect consent mode, PDPA/GDPR obligations and platform policies. No fingerprinting workarounds, no tracking people who said no.
- Report uncertainty honestly: modelled and sampled data labelled as such; never present platform attribution as ground truth.
