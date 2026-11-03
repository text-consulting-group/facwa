#!/usr/bin/env python3
"""facwa #1 후속 배치 — en frontmatter 한글 잔재 + description_status 문형 uniform.

scripts/fix_en_consistency.py (PR #2)의 후속. 기계적 변환만 수행하고
편집 판단이 필요한 항목은 리포트로 남긴다.

대상: content/items/**/*.en.md  (_index 제외)
변환(자동):
  1) 표기/고정 용어: 해당없음→none, 유성/무성→sound/silent, 년월일 날짜→점 표기,
     N분N초→Nm Ns, N롤→N roll(s), 총→total, 등→et al., 한글+(로마자)→로마자
  2) description_status/typo: 백틱 아포스트로피(`→'), Shows→This footage shows,
     This footage contains→This footage shows
리포트(수동 잔여): F3 지명, F4 부대명, F5/creators 인명, 잔여 문형, sentinel/shotlist 이상

사용:
  python3 scripts/fix_en_followup_batch.py           # dry-run 분석
  python3 scripts/fix_en_followup_batch.py --apply   # 기록 + YAML 검증
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML 필요: repo .venv (`.venv/bin/python scripts/fix_en_followup_batch.py`)로 실행")

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "content/items"
HANGUL = re.compile(r"[가-힣]")

# ── exact-value maps (프로젝트 확정 표기) ──────────────────────────────
EXACT_MAP = {
    "해당없음": "none",
    "유성/무성": "sound/silent",
    "1953년 4월 20일": "1953.4.20",
    "1953년 7월 29-30일": "1953.7.29-30",
    "1954년 1월 19일~20일": "1954.1.19-20",
    "1953년 4월 21일~22일": "1953.4.21-22",
    "1944.9.8 이후(추정)": "after 1944.9.8 (presumed)",
    "M. W. Barens 등": "M. W. Barens et al.",
    "M. W. Barnes 등": "M. W. Barnes et al.",
    "브라이트(Bright)": "Bright",
}

SENTINELS = {"N/A", "Unknown", "none", "None", "-", "해당없음", "not applicable", "Not applicable"}


def fm_span(text: str) -> tuple[int, int] | None:
    """frontmatter 블록의 (start, end) 오프셋 — end는 닫는 --- 직전 개행."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return 3, end + 1


def dur_units(s: str) -> str:
    """'21분 37초' → '21m 37s' (초/분 leading zero 제거, gold 스타일 7m 2s)."""
    s = re.sub(r"(\d+)븐\s*(\d+)초", lambda m: f"{int(m.group(1))}m {int(m.group(2))}s", s)
    s = re.sub(r"(\d+)분\s*(\d+)초", lambda m: f"{int(m.group(1))}m {int(m.group(2))}s", s)
    s = re.sub(r"(\d+)분(?![가-힣\d])", lambda m: f"{int(m.group(1))}m", s)
    s = re.sub(r"(\d+)초(?![가-힣\d])", lambda m: f"{int(m.group(1))}s", s)
    s = re.sub(r"(\d+)롤(?![가-힣\d])", lambda m: f"{int(m.group(1))} {'roll' if int(m.group(1)) == 1 else 'rolls'}", s)
    s = re.sub(r"총\s*(?=\d)", "total ", s)
    return s


def has_duration_typo(s: str) -> bool:
    """N분N분 등 — 의미 불명 확신 불가, 수정하지 않고 보고만."""
    return bool(re.search(r"\d+분\s*\d+분", s) or re.search(r"\d+초\s*\d+초", s))


def transform_hangul_line(line: str, stats: Counter) -> str:
    """frontmatter 한 줄에서 기계적 한글 변환."""
    if has_duration_typo(line):
        stats["anomaly_duration_typo_lines"] += 1
        return line
    orig = line
    for ko, en in EXACT_MAP.items():
        if ko in line:
            n = line.count(ko)
            line = line.replace(ko, en)
            stats[f"exact:{ko}"] += n
    if HANGUL.search(line):
        new = re.sub(r"(?<![가-힣])유성(?![가-힣])", "sound", line)
        if new != line:
            stats["audio_sound"] += len(re.findall(r"(?<![가-힣])유성(?![가-힣])", line))
            line = new
        new = re.sub(r"(?<![가-힣])무성(?![가-힣])", "silent", line)
        if new != line:
            stats["audio_silent"] += len(re.findall(r"(?<![가-힣])무성(?![가-힣])", line))
            line = new
    if HANGUL.search(line) and re.search(r"\d+(분|초|븐|롤)|총", line):
        before = line
        line = dur_units(line)
        if line != before:
            stats["duration_lines"] += 1
    return line


def fix_status_and_title(block: str, stats: Counter) -> str:
    """description_status/title: 백틱·문형 uniform 변환."""
    out = []
    for line in block.split("\n"):
        m = re.match(r"^(description_status|title):\s*(.*)$", line)
        if not m:
            out.append(line)
            continue
        key, rest = m.group(1), m.group(2)
        quote = ""
        val = rest
        if rest.startswith('"') and rest.endswith('"') and len(rest) >= 2:
            quote = '"'
            val = rest[1:-1]
        elif rest.startswith("'") and rest.endswith("'") and len(rest) >= 2:
            quote = "'"
            val = rest[1:-1]
        orig_val = val
        if "`" in val:
            stats["backtick_files"] += 1
            stats["backtick_chars"] += val.count("`")
            val = val.replace("`", "'")
        if key == "description_status":
            if re.match(r"Shows\s", val):
                val = "This footage shows " + val[len("Shows "):]
                stats["opener_bare_shows"] += 1
            else:
                new_val, n = re.subn(
                    r"^This footage (?:contains|captures|depicts|records) ",
                    "This footage shows ", val, count=1)
                if n:
                    stats["opener_verb_unified"] += n
                    val = new_val
        if val != orig_val:
            out.append(f"{key}: {quote}{val}{quote}")
        else:
            out.append(line)
    return "\n".join(out)


def analyze(apply: bool = False, only: str = "all") -> dict:
    stats: Counter = Counter()
    hangul_class: dict[str, Counter] = defaultdict(Counter)
    hangul_samples: dict[str, list] = defaultdict(list)
    leftover: dict[str, Counter] = defaultdict(Counter)
    leftover_samples: dict[str, list] = defaultdict(list)
    status_openers: Counter = Counter()
    status_remaining_samples: list = []
    sentinel_vals: Counter = Counter()
    shot_anoms: list = []
    needs_review = 0
    body_hangul = 0
    edited = 0

    for path in sorted(ITEMS.rglob("*.en.md")):
        if "_index" in path.name:
            continue
        text = path.read_text(encoding="utf-8")
        span = fm_span(text)
        if not span:
            stats["no_frontmatter"] += 1
            continue
        s, e = span
        block, body = text[s:e], text[e:]
        rel = str(path.relative_to(ROOT))

        # YAML 원본 파싱 가능 여부 (적용 시 실패 유입 방지용 기준선)
        try:
            yaml.safe_load(block)
            yaml_before = True
        except Exception:
            yaml_before = False
            stats["yaml_fail_before"] += 1

        if HANGUL.search(body):
            body_hangul += 1

        new_block = block
        # 1) 한글 잔재 분류 + 변환
        for line in block.split("\n"):
            if not HANGUL.search(line):
                continue
            fm = re.match(r"^\s*-?\s*\"?(F[1-7])\b", line) or re.match(r"^(F[1-7])\b", line.strip())
            key = fm.group(1) if fm else (re.match(r"^(\w[\w_]*):", line).group(1) if re.match(r"^(\w[\w_]*):", line) else "other")
            val_for_class = line.strip()
            if "해당없음" in line:
                cls = "sentinel_haetae"
            elif re.search(r"\d+분|\d+초|\d+븐|\d+롤|총\d|총 \d", line):
                cls = "duration_notation"
            elif re.search(r"\d{4}년|\d{4}\.\s?\d|일~|이후\(추정\)", line):
                cls = "date_notation"
            elif re.search(r"(?<![가-힣])(유성|무성)(?![가-힣])", line):
                cls = "audio_term"
            elif re.search(r"\s등\b|\s등$", line) or "등\"" in line:
                cls = "suffix_et_al"
            elif re.search(r"[가-힣]+\(\w+\)", line):
                cls = "korean_with_romanization"
            elif re.match(r"^\s*-?\s*\"?F3\b", line) or line.startswith("F3"):
                cls = "place_name_F3"
            elif re.match(r"^\s*-?\s*\"?F4\b", line) or line.startswith("F4"):
                cls = "org_name_F4"
            elif re.match(r"^\s*-?\s*\"?F5\b", line) or line.startswith("F5"):
                cls = "person_name_F5"
            elif line.strip().startswith("- "):
                cls = "list_item_creators"
            else:
                cls = f"other:{key}"
            hangul_class[cls][val_for_class[:70]] += 1
            if len(hangul_samples[cls]) < 5:
                hangul_samples[cls].append(f"{rel}: {val_for_class[:80]}")

        fixed_lines = []
        for line in new_block.split("\n"):
            if only in ("all", "hangul") and (HANGUL.search(line) or any(k in line for k in EXACT_MAP)):
                line = transform_hangul_line(line, stats)
            fixed_lines.append(line)
        new_block = "\n".join(fixed_lines)

        # 2) description_status / title uniform
        if only in ("all", "status"):
            new_block = fix_status_and_title(new_block, stats)

        if new_block != block:
            edited += 1
            if apply:
                new_text = text[:s] + new_block + text[e:]
                try:
                    yaml.safe_load(new_block)
                    yaml_after = True
                except Exception:
                    yaml_after = False
                    stats["yaml_fail_after"] += 1
                    if yaml_before:
                        stats["yaml_fail_introduced"] += 1
                path.write_text(new_text, encoding="utf-8")

        # 3) 잔여 한글 (변환 후 블록 기준)
        for line in new_block.split("\n"):
            if not HANGUL.search(line):
                continue
            fm2 = re.match(r"^\s*-?\s*\"?(F[1-7])\b", line) or re.match(r"^(F[1-7])\b", line.strip())
            if fm2:
                k = {"F3": "F3_places", "F4": "F4_orgs", "F5": "F5_persons"}.get(fm2.group(1), fm2.group(1) + "_other")
            elif line.strip().startswith("- "):
                k = "creators"
            elif re.match(r"^(time_courts|date_range|date|title|description|description_status|shotlist|level__file):", line):
                k = re.match(r"^(\w[\w_]*):", line).group(1)
            else:
                k = "other"
            leftover[k][line.strip()[:70]] += 1
            if len(leftover_samples[k]) < 5:
                leftover_samples[k].append(f"{rel}: {line.strip()[:80]}")

        # 4) description_status 문형 집계
        m = re.search(r"^description_status:\s*\"?(.*?)\"?\s*$", new_block, re.M)
        ds = m.group(1) if m else ""
        if not ds or ds.strip() in SENTINELS:
            status_openers["<sentinel/empty>"] += 1
        elif ds.startswith("This footage shows"):
            status_openers["This footage shows (standard)"] += 1
        elif re.match(r"(This footage|Footage|This video|This film|A video|This is one)", ds):
            status_openers["near-standard other"] += 1
        else:
            w = " ".join(ds.split()[:3])
            status_openers[f"remaining:{w}"] += 1
            if len(status_remaining_samples) < 8:
                status_remaining_samples.append(f"{rel}: {ds[:90]}")

        # 5) sentinel / shotlist 이상 스캔 (보고 전용)
        for line in new_block.split("\n"):
            mm = re.match(r"^(\w[\w_]*):\s*\"?(.*?)\"?\s*$", line)
            if mm and mm.group(2).strip() in SENTINELS:
                sentinel_vals[f"{mm.group(1)}={mm.group(2).strip()}"] += 1
            if "[NEEDS REVIEW]" in line:
                needs_review += 1
        sm = re.search(r"^shotlist:\s*\"?(.*?)\"?\s*$", new_block, re.M)
        sl = sm.group(1) if sm else ""
        if not sl:
            shot_anoms.append(f"{rel}: shotlist empty/missing")
        elif sl.strip() not in SENTINELS and not sl.startswith("1. Shot list") and not sl.startswith("Shot list"):
            shot_anoms.append(f"{rel}: shotlist 비표준 헤더 ({sl[:40]!r}...)")

    return {
        "stats": stats,
        "hangul_class": hangul_class,
        "hangul_samples": hangul_samples,
        "leftover": leftover,
        "leftover_samples": leftover_samples,
        "status_openers": status_openers,
        "status_remaining_samples": status_remaining_samples,
        "sentinel_vals": sentinel_vals,
        "shot_anoms": shot_anoms,
        "needs_review": needs_review,
        "body_hangul": body_hangul,
        "edited": edited,
    }


def main() -> None:
    apply = "--apply" in sys.argv
    only = "all"
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1]
        elif a.startswith("--only="):
            only = a.split("=", 1)[1]
    if only not in ("all", "hangul", "status"):
        sys.exit("--only 은 all|hangul|status")
    r = analyze(apply=apply, only=only)
    mode = f"APPLIED[{only}]" if apply else f"DRY-RUN[{only}]"
    print(f"=== facwa #1 follow-up batch [{mode}] ===")
    print(f"files edited: {r['edited']}")
    print("\n-- mechanical fix counts --")
    for k, c in sorted(r["stats"].items()):
        print(f"  {k}: {c}")
    print("\n-- 한글 잔재 분류 (사전 변환 패턴별 distinct value / occurrences) --")
    for cls, vals in sorted(r["hangul_class"].items(), key=lambda x: -sum(x[1].values())):
        print(f"  [{cls}] occurrences={sum(vals.values())}, distinct={len(vals)}")
        for s in r["hangul_samples"][cls]:
            print(f"     e.g. {s}")
    print("\n-- 변환 후 잔여 한글 (수동 편집 필요) --")
    for k, vals in sorted(r["leftover"].items(), key=lambda x: -sum(x[1].values())):
        print(f"  [{k}] occurrences={sum(vals.values())}, distinct={len(vals)}")
        for s in r["leftover_samples"][k]:
            print(f"     e.g. {s}")
    print("\n-- description_status 문형 분포 --")
    for k, c in r["status_openers"].most_common(30):
        print(f"  [{c:4d}] {k}")
    print("  samples of remaining:")
    for s in r["status_remaining_samples"]:
        print(f"     {s}")
    print("\n-- sentinel values (report-only) --")
    for k, c in r["sentinel_vals"].most_common():
        print(f"  [{c:4d}] {k}")
    print(f"\n-- shotlist anomalies: {len(r['shot_anoms'])} --")
    for s in r["shot_anoms"][:12]:
        print(f"  {s}")
    print(f"\n[NEEDS REVIEW] markers: {r['needs_review']}")
    print(f"body-with-Hangul files (out of scope): {r['body_hangul']}")


if __name__ == "__main__":
    main()
