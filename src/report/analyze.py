"""Compute report metrics from an observatory snapshot. Pure functions."""

from __future__ import annotations

from collections import Counter

# These values are candidates inferred from the shape of the register link.
# They are not verified document formats and do not establish Inline XBRL
# conformance under Implementing Regulation (EU) 2024/2984.
STRUCTURED_LINK_CANDIDATES = {"xhtml/html", "json", "docx"}


def whitepaper_entries(snapshot: dict) -> list[dict]:
    return [
        entry
        for register in snapshot.get("registers", [])
        if register.get("kind") == "whitepaper" and register.get("fetched")
        for entry in register.get("entries", [])
    ]


def analyze(snapshot: dict) -> dict:
    whitepapers = whitepaper_entries(snapshot)
    total = len(whitepapers)

    def pct(n: int) -> float:
        return round(100 * n / total, 1) if total else 0.0

    formats = Counter(entry.get("format_class", "none") for entry in whitepapers)
    structured_link_candidates = sum(
        formats.get(fmt, 0) for fmt in STRUCTURED_LINK_CANDIDATES
    )
    landing = formats.get("unspecified", 0)

    verified = [
        entry
        for entry in whitepapers
        if entry.get("content_verification_status") == "verified"
    ]
    verified_ixbrl = sum(
        1 for entry in verified if entry.get("verified_format") == "inline-xbrl-xhtml"
    )

    member_states = Counter(
        (entry.get("member_state") or "?") for entry in whitepapers
    )

    register_totals = {
        register["slug"]: len(register.get("entries", []))
        for register in snapshot.get("registers", [])
        if register.get("fetched")
    }

    return {
        "snapshot_date": snapshot.get("snapshot_date"),
        "total_whitepapers": total,
        "format_classification_basis": "register_link_shape",
        "format_counts": dict(formats.most_common()),
        "structured_link_candidates": structured_link_candidates,
        "structured_link_candidate_pct": pct(structured_link_candidates),
        "pdf_link_candidates": formats.get("pdf", 0),
        "pdf_link_candidate_pct": pct(formats.get("pdf", 0)),
        "landing_or_unspecified_links": landing,
        "landing_or_unspecified_link_pct": pct(landing),
        "content_verified_documents": len(verified),
        "verified_inline_xbrl_documents": verified_ixbrl,
        "member_states": member_states.most_common(),
        "register_totals": register_totals,
    }
