from __future__ import annotations

import sys
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


def find_disallowed_markdown(paths: list[str]) -> list[str]:
    return [path for path in paths if not is_allowed_doc(path)]


def main(argv: list[str]) -> int:
    disallowed = find_disallowed_markdown(argv)
    if not disallowed:
        print("docs-scope: OK")
        return 0

    print("docs-scope: disallowed markdown paths detected:")
    for path in disallowed:
        print(f"- {path}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
