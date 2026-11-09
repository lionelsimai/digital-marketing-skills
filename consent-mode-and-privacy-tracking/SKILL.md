---
name: consent-mode-and-privacy-tracking
description: |
  Implement consent mode and privacy-respecting measurement: banner behaviour, tag gating, and modelled-data literacy for stakeholders.
  TRIGGERS - Use when user needs help with consent mode implementation and privacy-first analytics tasks.
category: Web & Marketing Analytics
version: 1.0
---
# Consent Mode and Privacy Tracking

## What this skill does

Aligns the measurement stack with the law and the brand's promise: tags behave according to consent, and everyone understands what modelled data is and isn't.

## Inputs to collect

- Markets served and applicable regimes (GDPR, PDPA, CCPA as relevant)
- Current banner/CMP setup and tag inventory
- Platforms in use (Google, Meta, others) and their consent features

## Workflow

1. **Inventory what fires when** - For every tag: does it wait for consent, fire on page load regardless, or drop cookies pre-consent? Test in a clean browser, don't trust the tag manager's intentions.
2. **Configure consent states properly** - Map banner choices to platform consent signals (e.g. Google consent mode storage types), defaulting to denied where the regime requires it.
3. **Make the banner honest and usable** - Accept and reject at equal prominence, plain language, granular options behind one clear click. Dark-pattern banners are legal risk and brand damage in one package.
4. **Explain modelled data** - Write the stakeholder one-pager: what platforms model when consent is denied, what that does to reported numbers, and why totals won't match the CRM.
5. **Audit quarterly** - Re-test firing behaviour after every site/CMP release, and review vendor sub-processor changes. Consent setups rot silently.

## Deliverable

- Tag firing audit with fixes
- Consent configuration spec per platform
- Stakeholder one-pager on modelled vs observed data

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Pre-consent firing incidents | Target zero, verified by crawl tests |
| Consent rate by market | Context for data completeness - never a target to game |
| Modelled share of reported conversions | Disclosed in reporting so decisions price it in |

## Quality checklist

- [ ] Reject as easy as accept on the banner
- [ ] Tags tested in a clean environment, evidence saved
- [ ] Modelled data labelled in every stakeholder report

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Track only with consent where required: respect consent mode, PDPA/GDPR obligations and platform policies. No fingerprinting workarounds, no tracking people who said no.
- Report uncertainty honestly: modelled and sampled data labelled as such; never present platform attribution as ground truth.
- Never design consent flows to trick, shame or exhaust users into accepting. Aside from the ethics, regulators in the EU and Singapore both act on dark patterns.
