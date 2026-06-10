#!/usr/bin/env python3
"""Validate workshop slides structure and local asset references."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def validate_slide_file(slide_path: Path) -> None:
    if not slide_path.exists():
        raise FileNotFoundError(f"Slide file not found: {slide_path}")

    content = slide_path.read_text(encoding="utf-8")

    required_tokens = [
        '<div class="reveal">',
        '<div class="slides">',
        "new Reveal(",
        "const agenda = [",
        "const invitedSpeakers = [",
    ]
    missing = [token for token in required_tokens if token not in content]
    if missing:
        raise RuntimeError(f"Missing required slide tokens: {missing}")

    # Verify all local image refs declared via data-image-path exist.
    refs = re.findall(r'data-image-path="([^"]+)"', content)
    missing_files: list[str] = []
    for rel in refs:
        if rel.startswith("${"):
            # Runtime template interpolation inside JS strings.
            continue
        if rel.startswith(("http://", "https://", "data:")):
            continue
        target = (slide_path.parent / rel).resolve()
        if not target.exists():
            missing_files.append(rel)

    if missing_files:
        details = "\n".join(f" - {ref}" for ref in missing_files)
        raise RuntimeError(f"Missing local assets referenced by data-image-path:\n{details}")

    # Verify local href/src targets in static HTML tags exist.
    local_refs = re.findall(r'(?:href|src)="([^"]+)"', content)
    missing_static_refs: list[str] = []
    ignored_prefixes = ("http://", "https://", "data:", "mailto:", "javascript:", "#")
    for ref in local_refs:
        if ref.startswith("${") or ref.startswith(ignored_prefixes):
            continue
        target = (slide_path.parent / ref).resolve()
        if not target.exists():
            missing_static_refs.append(ref)

    if missing_static_refs:
        details = "\n".join(f" - {ref}" for ref in missing_static_refs)
        raise RuntimeError(f"Missing local static href/src targets:\n{details}")


def main() -> int:
    slide_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("slides/workshop-slides.html")

    try:
        validate_slide_file(slide_path)
    except Exception as exc:  # noqa: BLE001
        print(str(exc))
        return 1

    print("Slides CI checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
