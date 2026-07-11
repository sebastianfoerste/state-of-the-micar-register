# The State of the MiCAR Register

A quarterly, reproducible report on ESMA's public MiCAR register.

The current edition measures register composition, Member State concentration, and the shape of the links recorded for crypto-asset white papers. It does not yet verify the content served by every link or test Inline XBRL conformance.

Latest edition: **[editions/2026-Q3.md](editions/2026-Q3.md)** | shareable page: **<https://sebastianfoerste.github.io/state-of-the-micar-register/>**

## Current observation

In the 7 July 2026 snapshot:

- the register contained 953 crypto-asset white papers;
- 114 links, or 12.0%, were shaped like XHTML/HTML, JSON, or DOCX candidates;
- 584 links, or 61.3%, were landing pages, redirects, or bare domains whose document format could not be inferred reliably;
- 254 links, or 26.7%, were PDF-shaped candidates;
- no document had content-level format verification in the snapshot.

These are register-link observations. They are not measurements of actual document MIME type, parseability, or compliance with Commission Implementing Regulation (EU) 2024/2984.

## Why it exists

MiCAR Articles 6(10), 19(9), and 51(9) require crypto-asset white papers to be made available in a machine-readable format. Commission Implementing Regulation (EU) 2024/2984 specifies XHTML with Inline XBRL and applies from 23 December 2025. Article 109 establishes ESMA's public register.

That makes the register a useful object of empirical research. Reliable conclusions require separating three questions:

1. What does the register row say?
2. What content does the link actually serve?
3. Does the fetched document conform to the applicable technical requirements?

The current edition answers the first question only.

## How it works

Figures are generated from the [MiCAR Register Observatory](https://github.com/sebastianfoerste/micar-register-observatory), which snapshots ESMA's public register exports and commits changes. Each edition is built from one dated snapshot.

The analyzer treats the existing `format_class` as a URL-shape candidate. The report now exposes `format_classification_basis: register_link_shape`, the number of content-verified documents, and the number verified as Inline XBRL XHTML.

See [METHODOLOGY.md](METHODOLOGY.md) for definitions, limitations, and the content-verification design.

```bash
git clone https://github.com/sebastianfoerste/state-of-the-micar-register
cd state-of-the-micar-register
make install && make test
make build
```

## What this is and is not

The report states reproducible facts about a dated public-register snapshot. It does not:

- infer an issuer's compliance from a URL suffix;
- claim that a landing-page link points to no machine-readable document;
- treat a PDF-shaped URL as proof of the response format;
- assess any named issuer;
- provide legal advice.

## Editions

| Edition | Snapshot | Headline |
| --- | --- | --- |
| [2026-Q3](editions/2026-Q3.md) | 2026-07-07 | 12.0% structured-link candidates; 61.3% ambiguous landing or bare-domain links |

Author: Sebastian Förste, German-qualified lawyer in EU financial regulation and former NLP data scientist. Code is MIT; report text may be cited with attribution.
