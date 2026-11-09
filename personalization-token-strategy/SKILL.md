---
name: personalization-token-strategy
description: |
  Use personalisation safely: which tokens, what fallbacks, and behaviour-based content blocks that never embarrass.
  TRIGGERS - Use when user needs help with email and web personalization token strategy tasks.
category: Marketing Automation & CRM
version: 1.0
---
# Personalization Token Strategy

## What this skill does

Sets the rules for personalisation so it adds relevance instead of risk: right fields, tested fallbacks, and behavioural content over creepy data displays.

## Inputs to collect

- Available contact/company fields and their fill rates
- ESP/web personalisation capabilities
- Past personalisation incidents or near-misses

## Workflow

1. **Audit field quality first** - Check fill rate and accuracy for every candidate field. A token is only usable above a quality bar (e.g. 95% filled, format-consistent) for the segment being mailed.
2. **Set fallbacks that read naturally** - Every token gets a fallback that keeps the sentence grammatical and sensible ('your team' beats a blank or 'there'). Test renders with missing data, not just complete records.
3. **Prefer behaviour over biography** - Personalise on what they did (viewed, bought, attended, downloaded) rather than displaying scraped personal details back at them. Relevance without surveillance vibes.
4. **Build content blocks per segment** - Modular blocks (proof, offer, content) swapped by segment rules, each block QA'd in every combination it can appear in.
5. **Add the pre-send token check** - Seed list includes records with empty, long, unicode and edge-case values for every token used. Sign-off requires eyeballing those renders.

## Deliverable

- Token usage standard: fields, quality bars, fallbacks
- Segment content-block map
- Pre-send token QA checklist

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Personalisation error incidents | Target zero - one bad merge can cost a list |
| Engagement lift of personalised vs control sends | Personalisation must earn its complexity |
| Field quality trend | Fill/accuracy of token fields quarter on quarter |

## Quality checklist

- [ ] Fallbacks tested with empty and edge-case data
- [ ] No token displays data the contact didn't knowingly provide or behaviour they didn't take
- [ ] Every combination of swapped blocks proofread

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Automation amplifies whatever it touches - verify data and logic on test records before any workflow touches the live list.
- Consent travels with the contact: a workflow must never re-subscribe, re-permit or message someone outside the consent they gave.
- Never fake familiarity: personalisation must come from data the person provided or behaviour on your own properties - not purchased dossiers.
