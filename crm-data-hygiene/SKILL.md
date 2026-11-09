---
name: crm-data-hygiene
description: |
  Clean and keep clean CRM data: dedupe rules, field standards, enrichment boundaries and a hygiene cadence.
  TRIGGERS - Use when user needs help with CRM data hygiene and deduplication tasks.
category: Marketing Automation & CRM
version: 1.0
---
# CRM Data Hygiene

## What this skill does

Fixes the root cause of broken automation and reporting - dirty data - with standards at the point of entry, not annual panic cleans.

## Inputs to collect

- CRM field inventory and current completion rates
- Duplicate rate estimate and merge history
- List of data sources feeding the CRM (forms, imports, integrations)

## Workflow

1. **Set the field standards** - For each critical field: format, allowed values, source of truth, required-at-which-stage. Publish the standard where people enter data, not in a wiki nobody opens.
2. **Dedupe with a survivor logic** - Match on strong keys (email, then phone+company), merge by rules (most recent engagement, most complete record), and log merges. Never auto-delete without a review queue for high-value records.
3. **Fix the sources** - Forms get validation and picklists; imports get a template with required fields and a rejection report; integrations get field-mapping reviews. Cleaning without source fixes is mopping with the tap on.
4. **Enrich carefully** - Enrichment fills gaps from reputable providers, marked as enriched with a date. Never overwrite human-verified data with provider guesses.
5. **Run the cadence** - Weekly duplicate queue, monthly field-completion report, quarterly source audit. Small and constant beats annual and traumatic.

## Deliverable

- Field standards document
- Dedupe rules and merge log process
- Source-fix list and hygiene cadence calendar

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Duplicate rate | Trended monthly; target a sustained low single-digit percentage |
| Critical field completion | By source - the worst source gets fixed first |
| Automation error rate from bad data | Bounced emails, failed syncs, misroutes attributable to data |

## Quality checklist

- [ ] Merge rules reviewed by a human for high-value records
- [ ] Enriched data flagged and dated, never silently overwriting verified data
- [ ] Every import path has validation or a rejection report

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
- Personal data hygiene includes deletion duties: honour erasure requests across the CRM and connected tools, and don't retain data 'just in case' beyond its purpose.
