#!/usr/bin/env python3
"""Replace user-facing Firecrawl with CrawlHub in markdown, skipping technical identifiers."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKIP_PATTERNS = (
    "firecrawl.dev",
    "github.com/firecrawl",
    "firecrawl-local",
    "firecrawl-cli",
    "FIRECRAWL_",
    "CRAWLHUB_",
    "api.firecrawl",
    "@mendable",
    "docs.firecrawl",
    "alexandria.firecrawl",
    "ghcr.io/firecrawl",
    "notifications.firecrawl",
    "help@firecrawl",
    "/firecrawl",
    "firecrawl-mcp",
    "firecrawl_theme",
    "pepy.tech/project/firecrawl",
)


def should_skip_line(line: str) -> bool:
    lower = line.lower()
    return any(p.lower() in lower for p in SKIP_PATTERNS)


def transform_line(line: str) -> str:
    if should_skip_line(line):
        return line
    return line.replace("Firecrawl", "CrawlHub")


def transform_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out = "".join(transform_line(line) for line in lines)
    if out != text:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def main(argv: list[str]) -> int:
    roots = [Path(p) for p in argv[1:]] or [Path("README.md"), Path("SELF_HOST.md")]
    changed = 0
    for root in roots:
        files = [root] if root.is_file() else root.rglob("*.md")
        for path in files:
            if path.suffix != ".md":
                continue
            if transform_file(path):
                changed += 1
                print(path)
    print(f"Updated {changed} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))