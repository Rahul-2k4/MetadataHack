from __future__ import annotations

from pathlib import Path

ALLOWED_MD_PREFIXES = (
    Path("docs"),
    Path("projects/main-submission"),
    Path("projects/experiments"),
    Path("assets"),
)


def is_allowed_doc(path: str) -> bool:
    p = Path(path)
    if p.suffix.lower() != ".md":
        return True

    normalized = Path(*p.parts)
    return any(normalized == prefix or prefix in normalized.parents for prefix in ALLOWED_MD_PREFIXES)
