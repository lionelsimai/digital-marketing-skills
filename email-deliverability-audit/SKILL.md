---
name: email-deliverability-audit
description: |
  Audit deliverability end to end: authentication, list quality, engagement signals, content triggers and infrastructure.
  TRIGGERS - Use when user needs help with email deliverability audit tasks.
category: Email & Lifecycle Marketing
version: 1.0
---
# Email Deliverability Audit

## What this skill does

Diagnoses why emails land in spam or promotions - separating technical faults from the harder truth that engagement and list quality usually cause it.

## Inputs to collect

- Sending domains and ESP setup
- Authentication records (SPF, DKIM, DMARC) status
- Last 90 days: bounces, complaints, unsubscribes, engagement by segment

## Workflow

1. **Verify authentication** - SPF, DKIM aligned and passing; DMARC present with a real policy; dedicated subdomain for marketing sends to protect the root domain.
2. **Grade list quality** - Hard bounce rate, role/garbage addresses, age of the list, source quality per signup path. Purchased or ancient lists get quarantined, not mailed.
3. **Read engagement honestly** - Segment by recency: engaged 90d, cooling, dead. Mailbox providers watch this; mailing the dead drags the living into spam with them.
4. **Check content and cadence** - Image/text balance, link domains, URL shorteners, and send-volume spikes. Content rarely causes spam placement alone, but it compounds list problems.
5. **Write the remediation plan** - Sequence: fix auth, quarantine bad data, sunset policy for the unengaged, warm-up schedule if domains/IPs change. With dates and expected recovery signals.

## Deliverable

- Deliverability report: auth, list, engagement, content findings
- Sunset and quarantine policy
- Remediation plan with recovery checkpoints

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Inbox placement (seed/panel data where available) | The metric of record; opens are a proxy |
| Hard bounce and complaint rates | Complaints above ~0.1% need action; above 0.3% is an emergency |
| Engaged-segment share of sends | Should rise as sunsets bite |

## Quality checklist

- [ ] SPF/DKIM/DMARC verified with live lookups, not assumed
- [ ] Sunset policy has an owner and a schedule
- [ ] No recommendation to buy, rent or scrape addresses - ever

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Permission-based sending only: no purchased or scraped lists, ever. Clear consent, honest sender identity, one-click unsubscribe in every email.
- Deliverability is trust: no deceptive subject lines, no hidden downsides, no dark patterns in preference or unsubscribe flows.
- Never suggest list purchasing, scraping or 'cleaning' a bought list into legitimacy. The fix for a bad list is to stop mailing it.
