---
name: consent-and-preference-centre
description: |
  Design consent capture and a preference centre that is honest, granular and easy - reducing unsubscribes while respecting choice.
  TRIGGERS - Use when user needs help with consent management and email preference centre design tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Consent and Preference Centre

## What this skill does

Turns consent from a legal footer into a product: clear choices at signup, a preference page people can actually use, and records that prove what was agreed.

## Inputs to collect

- Markets served and their consent regimes (PDPA, GDPR, CAN-SPAM as applicable)
- Current signup points and consent language
- Email programme types (newsletter, product, offers, events)

## Workflow

1. **Map every capture point** - List each place personal data is collected, what is promised there, and what consent is recorded. Gaps between promise and practice are the risk.
2. **Write consent in plain language** - At each point: what they'll receive, how often, from whom - in one or two human sentences, with unticked boxes where express consent is required.
3. **Design the preference centre** - Granular choices by content type and frequency, plus the global unsubscribe. Saving preferences must be easier than unsubscribing, but unsubscribe must never be hidden or obstructed.
4. **Record consent as data** - Store timestamp, source, wording version and IP/form evidence per contact. If you can't show it, you don't have it.
5. **Wire consent into every send** - Suppression logic reads consent and preferences at send time - for campaigns, flows and sales sends alike. Test with opted-down seed contacts.

## Deliverable

- Capture-point consent map with plain-language copy
- Preference centre spec and copy
- Consent record schema and send-time suppression rules

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Preference-centre saves vs unsubscribes | People choosing down instead of out is the design working |
| Consent record completeness | Share of contacts with full provenance |
| Complaint rate trend | Honest consent shows up here first |

## Quality checklist

- [ ] Unsubscribe is one click and honoured immediately
- [ ] No pre-ticked consent boxes anywhere
- [ ] Seed tests prove preference choices change what gets sent

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
- Never make unsubscribing harder than subscribing, never hide it, and never email someone who has opted out - for any reason, including 'just this once' campaigns.
