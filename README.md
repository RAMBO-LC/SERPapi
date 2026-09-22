# 🇮🇳 Grounds India

**An AI Overview Claim Auditor** — fact-checking Google's AI answers against independent evidence, built for the Indian information ecosystem.

![Status](https://img.shields.io/badge/status-in%20development-orange)
![License](https://img.shields.io/badge/license-TBD-lightgrey)

---

## Problem

Google's AI Overview increasingly sits at the top of search results, delivering a single confident-sounding answer before a user ever sees a link. In India's fast-moving, multilingual information environment — health remedies, political claims, financial advice, viral WhatsApp forwards making their way into search queries — that confidence can be misleading. AI Overviews sometimes:

- Cite thin, outdated, or low-authority sources
- Flatten a contested or nuanced topic into a single stated "fact"
- Miss recent developments that contradict or update the claim
- Surface region-specific misinformation that hasn't been fact-checked locally

There's currently no easy way for a curious user, journalist, or researcher to ask: **"Is this AI-generated answer actually well-supported?"**

## Solution

**Grounds India** takes any claim and the entity it's about, retrieves Google's AI-generated answer, and independently audits it — surfacing what genuinely supports the claim, what contradicts it, and where the picture is more nuanced than a single-sentence summary suggests. It's a transparency layer for AI-generated answers, not a replacement for them.

## How It Works

1. **Input** — User enters a claim and the relevant entity (person, company, policy, event, etc.)
2. **Fetch** — Grounds India retrieves Google's AI Overview / AI Mode answer for that claim
3. **Extract** — It parses out the sources Google's AI cited as support
4. **Cross-check** — It runs independent Google Search and Google News queries, decoupled from the AI Overview's own citations
5. **Synthesize** — It presents a three-way breakdown: **Supporting evidence**, **Contradicting evidence**, and **Nuanced / contextual evidence**

```
Claim + Entity → AI Overview → Cited Sources
                                     ↓
                         Independent Search + News
                                     ↓
                    Supporting | Contradicting | Nuanced
```

## SerpApi Engines Used

| Engine | Purpose |
|---|---|
| `google_ai_overview` / `google_ai_mode` | Retrieve the AI-generated answer + its citations |
| `google` (Search) | Independent web evidence, decoupled from AI citations |
| `google_news` | Recent, time-sensitive evidence and corrections |

## Status

🚧 **In development** — core pipeline and evidence-classification logic are being built out. Contributions and feedback welcome once the repo opens up.