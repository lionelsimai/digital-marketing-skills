---
name: utm-governance
description: |
  Govern UTM tagging: a naming standard, a builder, and cleanup rules so campaign data stays comparable forever.
  TRIGGERS - Use when user needs help with UTM naming convention and governance tasks.
category: Web & Marketing Analytics
version: 1.0
---
# UTM Governance

## What this skill does

Fixes the silent killer of campaign reporting - inconsistent UTMs - with a standard simple enough that everyone actually follows it.

## Inputs to collect

- Current UTM values in analytics (the mess, documented)
- Channel and campaign taxonomy (from media/content plans)
- Tools in use (builder sheet, link tools, ESP defaults)

## Workflow

1. **Define the standard** - Fixed value lists: source (platform), medium (channel type), campaign (initiative_date or initiative_theme), content (creative variant), term (paid keywords only). Lowercase, hyphens, no spaces - written as rules with examples.
2. **Build the builder** - A locked-formula sheet or internal tool that generates tagged URLs from dropdowns. If tagging requires memory, it will drift; make the right way the easy way.
3. **Tag the defaults** - Set UTM templates in the ESP, ad platforms and social tools so routine sends are tagged correctly by default.
4. **Clean the history carefully** - Map legacy variants to standard values in reporting views/filters where possible; never pretend history was clean - annotate the cutover date.
5. **Audit monthly** - Pull the month's new source/medium values; anything off-standard gets a named owner and a fix date. Drift caught monthly stays small.

## Deliverable

- UTM standard document with examples and banned patterns
- URL builder (sheet/tool) with dropdowns
- Monthly drift audit routine

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Off-standard session share | Should fall to low single digits after cutover |
| (not set) / unassigned traffic share | The untagged leak, trended |
| Campaign comparability | Share of campaigns reportable without manual cleanup |

## Quality checklist

- [ ] Standard covers every active channel including email and QR/offline
- [ ] Builder uses controlled vocabularies, not free text
- [ ] Internal traffic never tagged as campaigns

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- Track only with consent where required: respect consent mode, PDPA/GDPR obligations and platform policies. No fingerprinting workarounds, no tracking people who said no.
- Report uncertainty honestly: modelled and sampled data labelled as such; never present platform attribution as ground truth.
- Never put personal data (emails, names, IDs) in UTM parameters - it lands in analytics and logs and violates privacy policy and platform terms.
