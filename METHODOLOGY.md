# Methodology

## Scope

This report analyzes dated snapshots of ESMA's MiCAR register. The 2026 Q3 edition covers Title II, Title III, and Title IV white-paper entries, authorised CASPs, and entities identified by national competent authorities as non-compliant.

## Legal framing

MiCAR Articles 6(10), 19(9), and 51(9) require white papers to be made available in a machine-readable format. Commission Implementing Regulation (EU) 2024/2984 specifies XHTML with Inline XBRL and applies from 23 December 2025.

Article 109 establishes ESMA's register and requires it to contain the relevant white papers and classification data. The current report does not equate presence in the register with regulatory approval. ESMA states that registered white papers have not been reviewed or approved by a competent authority.

## Current data source

The report consumes a versioned snapshot from the [MiCAR Register Observatory](https://github.com/sebastianfoerste/micar-register-observatory). The observatory normalizes ESMA's public CSV exports and records a `format_class` inferred from the register link.

## Link-shape classification

The current `format_class` is based on URL shape. It supports these descriptive categories:

| Category | Meaning |
| --- | --- |
| `xhtml/html` | The register link is shaped like an XHTML or HTML resource. |
| `json` | The register link is shaped like a JSON resource. |
| `docx` | The register link is shaped like a DOCX resource. |
| `pdf` | The register link is shaped like a PDF resource. |
| `unspecified` | The link is a landing page, redirect-like path, or bare domain whose document type is not evident from the URL. |
| `none` | The register row contains no usable link. |

These categories are candidates. They do not establish:

- the final URL after redirects;
- the HTTP response status;
- the response `Content-Type`;
- the file signature or actual byte format;
- successful parsing;
- Inline XBRL markup;
- conformance with Implementing Regulation (EU) 2024/2984.

The code therefore names the metric `structured_link_candidates`, not `machine_readable`.

## Current metrics

The report publishes:

- register entry counts;
- register-link candidate counts and shares;
- home Member State counts;
- content-verified document count;
- verified Inline XBRL document count.

The latter two remain zero until the upstream snapshot includes content-verification results.

## Content-verification design

A content-level audit should record, for every public white-paper link:

1. original register URL;
2. final URL after redirects;
3. retrieval timestamp;
4. HTTP status;
5. response `Content-Type`;
6. response byte length;
7. SHA-256 of the retrieved bytes;
8. file signature;
9. detected format;
10. parse success or failure;
11. presence of Inline XBRL markup and taxonomy references;
12. error category where retrieval or parsing fails.

Rate limiting, retry policy, maximum response size, and a transparent user agent must be documented. Results should distinguish inaccessible content from non-conforming content.

## Publication rules

Until content verification is performed, the report may describe register-link shapes only. It must not state that:

- only 12% of registered white papers are machine-readable;
- a PDF-shaped or landing-page link proves non-compliance;
- a link-shape candidate is a verified document format;
- the register measures legal sufficiency.

Once content verification exists, the report should publish both link-shape and content-verified figures so that the effect of redirects and misleading suffixes remains visible.
