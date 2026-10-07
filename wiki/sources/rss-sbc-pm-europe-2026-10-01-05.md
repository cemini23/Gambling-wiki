---
title: "SBC Europe batch — Czech blocks Kalshi, Dutch Polymarket appeal, lotteries, Betsson (2026-10-01–05)"
type: source
tags: [source, rss, pm-retail, regulatory, europe, kalshi, polymarket, k181]
keywords: [czech-block, kalshi-czech, netherlands-ksa, polymarket-appeal, european-lotteries, sbc-summit, betsson-belgium]
related:
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/prediction-markets-crossover.md
  - sources/rss-lsr-pm-industry-2026-09-29-30.md
  - sources/daily-digest-batch-k181-2026-10-06.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/
phase_0_verdict: REFERENCE — European regulatory awareness; no operator action
wire_status: policy_wired
---

## Relations

- @entities/platforms/kalshi.md — Czech listing as an unauthorised operator
- @entities/platforms/polymarket.md — Dutch court appeal
- @concepts/prediction-markets-crossover.md — the US-vs-Europe classification split
- @sources/daily-digest-batch-k181-2026-10-06.md — K181 batch hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Feed** | SBC News (`sbc-news`) |
| **Published** | 2026-10-01 → 2026-10-05 |
| **Articles** | 5 |
| **Body access** | SBC 403s direct fetch; bodies via Brave LLM Context + Lottery Daily, iGamingToday, gambling.com, European Gaming, Gaming Intelligence |

**Location** (`cemini-egress-fi:/opt/cemini-bulk/research/gambling/`): the 5 archived `rss-sbc-news-2026-10-0{1,2,5}-*.md` files.

**Article URLs** (required for batch pages — `preingest_check.py` matches on these):
https://sbcnews.co.uk/europe/2026/10/01/european-lotteries-predictions/
https://sbcnews.co.uk/events/2026/10/01/sbc-summmit-lisbon-portugal/
https://sbcnews.co.uk/europe/2026/10/02/kalshi-czech-republic/
https://sbcnews.co.uk/sportsbook/2026/10/05/betsson-belgium-launch/
https://sbcnews.co.uk/europe/2026/10/05/polymarket-netherlands/

## Narrative

### Czech Republic blocks Kalshi — effective 2026-10-15

The **Czech Ministry of Finance** added **Kalshi** to its register of unauthorised gambling operators on **2026-09-30**. Under Czech law, ISPs have **15 days** from publication to block the sites, so conventional access ends **Thursday 2026-10-15**. VPN workarounds remain possible.

This follows the **July 2026** order against **Polymarket**. Two blocks in one year indicates a settled Czech position: **prediction markets are gambling by substance**, whatever the product is called. The listing reportedly came after the **Czech Institute for Gambling Regulation (IPRH)** — representing **>90%** of the regulated domestic sector — brought Kalshi to the authorities.

> "When Polymarket was added to the list, we said that it was an important precedent, not the end of the matter. The inclusion of Kalshi shows that this approach is now being reflected in practice." — **Jan Řehola**, IPRH Director

**Context:** Kalshi is reportedly raising at ~**$40B** valuation and saw ~**$60B** in September trading activity. Czech authorities treat market self-description as irrelevant; Belgian, French, Romanian, Spanish, and German regulators take the same line. Spain launched legal action against both platforms in May 2026.

**Gibraltar's counter-position** (Andrew Lyman, Gambling Commissioner): "If you are in denial and you want to ban or block, then you are fighting against the tide of consumers who really want this product. Therefore it's much better to regulate…"

### Polymarket appeals a €420,000 Dutch penalty

**Polymarket** has gone to **The Hague** to appeal a **€420,000** penalty from the Dutch regulator **Kansspelautoriteit (KSA)**.

Timeline: the KSA blacklisted Polymarket in January 2026 for offering unlicensed gambling to Dutch consumers, warning parent **Adventure One QSS** unless access was blocked by **2026-02-17**. Polymarket complied on **2026-02-18** — one day late — which the KSA ruled sufficient to trigger the full penalty. The penalty is expressed as **€420,000 per week, capped at €840,000**. Polymarket's earlier appeal was rejected in June; the KSA held that **blockchain and crypto payments do not change the legal nature of the activity**. Users still stake value on uncertain events, and chance plays a key role.

**Polymarket's argument:** its contracts function as **financial derivatives**, which would put it under the **Dutch Authority for Financial Markets** rather than the KSA.

**The critique worth recording:** if Polymarket wants financial-instrument classification, the closest European analogue is **binary options — already banned for retail sale in most of Europe**. The wiki records the same point in the CFTC Letter 26-27 comparison table (`@sources/rss-lsr-cftc-mention-market-advisory-2026-09-23.md`).

**Political movement:** Dutch MP **Iem Al Biyati** submitted a motion to create a separate prediction-market framework; State Secretary **Claudia Van Bruggen** rejected it, citing the KSA's position. Dutch users reportedly bet **>$30M** on Polymarket around the November 2025 parliamentary election.

### European Lotteries: judge the product, not the label

**European Lotteries (EL)** — the umbrella body for state lotteries — issued a statement (published 2026-09-30) urging policymakers to judge prediction markets on **legal characteristics, economic substance, and risk**, "rather than on the terminology used to market or describe them, or the technology through which they are offered."

EL stopped short of calling prediction markets gambling. Its structural point is the important one:

> "Qualification as a financial instrument does not, in itself, create an exemption from otherwise applicable national gambling legislation."

That aligns with **ESMA**, which recognised earlier in 2026 that event contracts may also constitute betting under national gambling law. Under **MiFID II**, a product failing the financial-instrument test falls to the relevant national gambling framework.

> "Prediction markets are developing rapidly, and regulation should keep pace. EL's position is simple: activities that present similar risks should be subject to similar safeguards." — **Piet Van Baeveghem**, EL Secretary General

EL calls for a **jurisdiction-by-jurisdiction** approach first, given that gambling regulation is a national competence and frameworks diverge across member states.

### SBC Summit Day 3: the Global Prediction Markets Forum

The **Global Prediction Markets Forum** ran on the final day of SBC Summit Lisbon, with Kalshi, Betr, WagerWire, and the Gibraltar and Malta governments present. The framing was "extraordinary opportunity in innovation," with doubts remaining.

> "They are applying. There is a lot of interest. Over the last months, we've seen huge interest from operators. We've had a lot of discussions with them." — **Charles Mizzi**, CEO, Malta Gaming Authority

> "We would love to. We are talking to regulators across the pond like ESMA and others." — **Udesh Jha**, Chief Risk Officer, Kalshi, on European expansion

SBC signed a long-term agreement to remain in Lisbon through **2030**; the 2026 edition drew attendees from **178 countries**.

### Betsson rebrands betFIRST in Belgium (context)

**Betsson Group** moved its Belgian operator **betFIRST** onto the flagship Betsson brand on **2026-10-05**, three years after a **€120M** acquisition (€117M upfront + up to €3M earnout). It keeps its **Belgian Gaming Commission** licences — an F1+ sports-betting licence (betFIRST was the first to obtain one, 2011) and an A+ casino licence (2024, via Groupe Partouche's Middelkerke Casino).

The dual-brand structure is the notable part: **Betsson.sport** operates as a sports **infotainment** platform with **no gambling licence**, and holds the Club Brugge main-partner role — because **front-of-shirt gambling sponsorships are banned in Belgian sport**. betFIRST was the 9th-largest brand in Belgium; Blask data ranks Belgium the 28th-biggest gambling market globally.

## Snippets

> "Qualification as a financial instrument does not, in itself, create an exemption from otherwise applicable national gambling legislation." — European Lotteries [Source: EL statement, 2026-09-30]

> "The KSA added that blockchain technology and crypto payments do not change the legal nature of the activity." [Source: Dutch regulator via gambling.com, 2026-10-05]

## Dead Ends

- **No operator action.** European regulatory awareness. No pm scp, no geofence change.
- **The Czech block is not yet in force.** It takes effect **2026-10-15**; the operator has no Czech exposure in any case.
- **Kalshi's $40B valuation and $60B September volume are secondary reporting.** Cite the source, not a bare number. [TENTATIVE]
- Betsson/Belgium is **industry context only** — it is not a wagering-product change.
