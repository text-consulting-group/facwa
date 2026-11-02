#!/usr/bin/env python3
"""facwa #1 — 영문 설명 필드 정합 점검·자동 수정.

검사 대상: content/items/**/*.en.md
수정 항목(자동): level__file 줄바꿈 복원, sentinel 값 통일, Shot list 표기 통일
보고 항목(수동): description_status 문형, shotlist 구조 — 리포트로 출력
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "content/items"

SENTINELS = {"Unknown", "N/A", "none", "None", "not applicable", "Not applicable", "해당없음"}
SENTINEL_CANON = "Unknown"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Extract simple frontmatter key: value pairs (multiline values included)."""
    if not text.startswith("---"):
        return {}, text
    end = text.index("---", 3)
    block = text[3:end]
    body = text[end + 3:]
    fields: dict[str, str] = {}
    current_key = None
    for line in block.split("\n"):
        m = re.match(r'^(\w[\w_]*):\s*(.*)', line)
        if m:
            current_key = m.group(1)
            fields[current_key] = m.group(2).strip().strip('"')
        elif current_key:
            fields[current_key] += "\n" + line
    return fields, body


def fix_level_file(value: str) -> str:
    """Restore F1~F7 multi-line structure from compressed single-line format."""
    # Already multi-line
    if "\n" in value:
        return value
    # Pattern: "F1 ... F2 ... F3 ..." → split before each F\d
    parts = re.split(r'(?=\bF[1-7]\b)', value)
    parts = [p.strip() for p in parts if p.strip()]
    return "\n".join(parts) if len(parts) > 1 else value


def fix_shotlist_marker(value: str) -> str:
    """Unify 'Shot List' → 'Shot list'."""
    return re.sub(r'\bShot List\b', 'Shot list', value)


def fix_sentinel(value: str) -> str:
    """Unify sentinel values to canonical form."""
    stripped = value.strip()
    if stripped in SENTINELS:
        return SENTINEL_CANON
    return value


def scan_and_fix(dry_run: bool = True) -> dict:
    report = {
        "total_en": 0,
        "level_file_fixed": 0,
        "shotlist_marker_fixed": 0,
        "sentinel_fixed": 0,
        "description_status_needs_review": 0,
        "korean_remnants": 0,
        "files": [],
    }
    korean_pattern = re.compile(r'[가-힣]')

    for en_path in sorted(ITEMS.rglob("*.en.md")):
        if "_index" in en_path.name:
            continue
        report["total_en"] += 1
        text = en_path.read_text(encoding="utf-8")
        fields, body = parse_frontmatter(text)
        changed = False
        fixes = []

        # 1. level__file multi-line restore
        lf = fields.get("level__file", "")
        if lf and "\n" not in lf and re.search(r'\bF[1-7]\b.*\bF[1-7]\b', lf):
            new_lf = fix_level_file(lf)
            if new_lf != lf:
                # Replace in original text (keep quotes style)
                old_quoted = f'level__file: "{lf}"'
                new_quoted = f'level__file: "{new_lf}"'
                if old_quoted in text:
                    text = text.replace(old_quoted, new_quoted)
                    report["level_file_fixed"] += 1
                    fixes.append("level__file multiline")
                    changed = True

        # 2. Shot List → Shot list
        for field in ("shotlist", "description"):
            val = fields.get(field, "")
            if val and re.search(r'\bShot List\b', val):
                text = text.replace(f'"{val}"', f'"{fix_shotlist_marker(val)}"')
                report["shotlist_marker_fixed"] += 1
                fixes.append(f"{field} marker")
                changed = True

        # 3. Sentinel unification in list-like fields
        for field in ("sources", "venues"):
            val = fields.get(field, "")
            if val and val.strip() in SENTINELS:
                old_line = f'"{val}"'
                new_line = f'"{SENTINEL_CANON}"'
                # Only replace within this field's context
                text = text.replace(old_line, new_line, 1)
                report["sentinel_fixed"] += 1
                fixes.append(f"{field} sentinel")
                changed = True

        # 4. Report: description_status review needed (non-standard opening)
        ds = fields.get("description_status", "")
        if ds and not re.match(r'(Footage|This footage|This video|This film|A video)', ds):
            report["description_status_needs_review"] += 1

        # 5. Report: Korean remnants in English fields
        for field in ("level__file", "description_status", "description", "shotlist"):
            val = fields.get(field, "")
            if val and korean_pattern.search(val):
                report["korean_remnants"] += 1
                fixes.append(f"{field} korean-remnant")
                break

        if changed and not dry_run:
            en_path.write_text(text, encoding="utf-8")
        if fixes:
            report["files"].append({"file": str(en_path.relative_to(ROOT)), "fixes": fixes})

    return report


if __name__ == "__main__":
    dry = "--apply" not in sys.argv
    r = scan_and_fix(dry_run=dry)
    mode = "DRY-RUN (use --apply to write)" if dry else "APPLIED"
    print(f"=== facwa en-consistency scan [{mode}] ===")
    print(f"English items scanned: {r['total_en']}")
    print(f"level__file multiline fixes: {r['level_file_fixed']}")
    print(f"Shot list marker fixes: {r['shotlist_marker_fixed']}")
    print(f"Sentinel unification fixes: {r['sentinel_fixed']}")
    print(f"description_status needs review: {r['description_status_needs_review']}")
    print(f"Korean remnants detected: {r['korean_remnants']}")
    print(f"Files with changes: {len(r['files'])}")
    if r["files"][:5]:
        print("\nSample changes:")
        for f in r["files"][:5]:
            print(f"  {f['file']}: {', '.join(f['fixes'])}")
