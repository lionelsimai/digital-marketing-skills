---
name: checkout-flow-review
description: |
  Review a checkout flow through a CRO lens: cost transparency, account walls, payment options and error recovery.
  TRIGGERS - Use when user needs help with checkout flow conversion review tasks.
category: CRO & Landing Pages
version: 1.0
---
# Checkout Flow Review

## What this skill does

Audits the last mile where intent is highest and patience is lowest, focusing on the conversion killers: surprise costs, forced accounts and fragile payment steps. (Operational fulfilment stays with the ecommerce team's remit; this is the persuasion layer.)

## Inputs to collect

- Checkout analytics: step completion, payment failure rates
- Full cost structure: shipping, taxes, fees and when they're revealed
- Payment methods offered vs market expectations

## Workflow

1. **Walk it as a stranger** - Complete a purchase on mobile with a real card path (test mode), timing each step and screenshotting every moment of doubt or confusion.
2. **Surface total cost early** - Shipping and fees visible before the final step - ideally on product/cart pages. Surprise at checkout is the single biggest self-inflicted abandon cause.
3. **Remove the account wall** - Guest checkout as the default; account creation offered after purchase with a benefit, not demanded before it.
4. **Fix payment resilience** - Offer the payment methods the market actually uses (cards plus local favourites like PayNow/GrabPay in SG where relevant), clear error messages that preserve entered data, and a retry path that doesn't restart the order.
5. **Add the reassurance layer** - Delivery estimate, returns summary and support contact visible at the payment step - answering the last three questions buyers ask before paying.

## Deliverable

- Checkout review with step-by-step findings and screenshots
- Cost-transparency fix list
- Payment resilience and error-handling fixes

## Success metrics

| Metric | How to read it |
|--------|---------------|
| Checkout completion rate | By device, trended weekly |
| Payment failure rate and recovery rate | Failures happen; recovery is the skill |
| Cart-to-checkout progression | Where the cost surprise bites |

## Quality checklist

- [ ] Total cost knowable before the final step
- [ ] Guest checkout available and tested
- [ ] Failed payment keeps the order and the entered data

## Guardrails

- Claims discipline: use only proof the user supplies or verifies. Never invent clients, results, rankings, or testimonials.
- Privacy and consent: collect and use personal data only with a lawful basis and consent where required. Respect PDPA (Singapore) and GDPR; honour unsubscribes and opt-outs immediately.
- Platform policy: follow each ad and search platform's current policies. When a rule changes often, flag it for a human to re-check before launch.
- No dark patterns: no fake countdowns, confirm-shaming, hidden costs or pre-ticked add-ons. Conversion bought with deception is refunded with interest in trust.
- Social proof must be real: genuine testimonials with permission, accurate numbers, no fabricated reviews or logos.
