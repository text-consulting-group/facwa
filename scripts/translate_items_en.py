#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "content" / "items"


EXACT_TITLE_MAP = {
    "부상포로 교환 (LITTLE SWAP)": "Exchange of Sick and Wounded Prisoners (LITTLE SWAP)",
    "폐허가 된 오키나와 나하": "Ruined Naha, Okinawa",
    "정전협정 조인식(선유리 유엔군임시사령부, 판문점) 2": "Armistice Agreement Signing Ceremony (Seonyuri UNC Advance HQ, Panmunjom) 2",
}

EXACT_DESCRIPTION_STATUS_MAP = {
    "이 영상은 아시아태평양전쟁 말기 오키나와 전투에서 폐허가 된 나하의 모습을 찍은 영상이다.": "This footage shows ruined Naha during the Battle of Okinawa near the end of the Asia-Pacific War.",
}

EXACT_VALUE_MAP = {
    "수집": "Collected",
    "해당없음": "Unknown",
    "오픈컬렉션": "Open Collection",
    "숏리스트": "Shot list",
    "자료 전체": "Entire archive",
    "Record Group(레코드그룹)": "Record Group",
    "Seires(시리즈)": "Series",
    "R1 한국전쟁": "R1 Korean War",
    "R2 DMZ&판문점": "R2 DMZ&Panmunjom",
    "R3 일본군 '위안부'": 'R3 Japanese Military "Comfort Women"',
    "R3 일본군’위안부’": 'R3 Japanese Military "Comfort Women"',
    "R4 빅 픽쳐": "R4 The Big Picture",
    "S1 포로&수용소": "S1 Prisoners and Camps",
    "S2 피난민": "S2 Refugees",
    "S3 학살": "S3 Massacres",
    "S4 일상": "S4 Everyday Life",
    "S1 판문점": "S1 Panmunjom",
    "S2 DMZ&판문점": "S2 DMZ and MDR",
    "S2 DMZ&MDR": "S2 DMZ and MDR",
    "S1 일본군’위안부’": 'S1 "Comfort Women"',
    "S1 일본군 '위안부'": 'S1 "Comfort Women"',
    "S2 오키나와": "S2 Okinawa",
    "S3 아시아태평양전쟁": "S3 Asia-Pacific War",
    "S1 The Big Picture": "S1 The Big Picture",
}

PHRASE_MAP = [
    ("정전협정 조인식", "Armistice Agreement Signing Ceremony"),
    ("정전회담", "Armistice Talks"),
    ("군사정전위원회 회의", "Military Armistice Commission Meeting"),
    ("포로교환", "prisoner exchange"),
    ("포로 송환", "repatriation of prisoners"),
    ("귀환포로", "returned prisoners of war"),
    ("부상포로", "wounded prisoners of war"),
    ("포로수용소", "prisoner-of-war camp"),
    ("포로", "prisoners of war"),
    ("수용소", "camp"),
    ("한국전쟁", "Korean War"),
    ("판문점", "Panmunjom"),
    ("비무장지대", "Demilitarized Zone"),
    ("DMZ", "DMZ"),
    ("정찰헌병", "reconnaissance military police"),
    ("철조망", "barbed-wire fence"),
    ("초소", "guard post"),
    ("공동경비구역", "Joint Security Area"),
    ("유엔군임시사령부", "United Nations Command Advance Headquarters"),
    ("북한인민군", "North Korean People's Army"),
    ("중국인민지원군", "Chinese People's Volunteers"),
    ("유엔군", "United Nations Command"),
    ("미군", "U.S. forces"),
    ("한국군", "ROK forces"),
    ("영국군", "British forces"),
    ("캐나다군", "Canadian forces"),
    ("호주", "Australia"),
    ("캐나다", "Canada"),
    ("영국", "Britain"),
    ("파주", "Paju"),
    ("문산", "Munsan"),
    ("대구", "Daegu"),
    ("부산", "Busan"),
    ("서울", "Seoul"),
    ("인천", "Incheon"),
    ("개성", "Kaesong"),
    ("오키나와", "Okinawa"),
    ("나하", "Naha"),
    ("일본군'위안부'", 'Japanese military "comfort women"'),
    ("일본군’위안부’", 'Japanese military "comfort women"'),
    ("아시아태평양전쟁", "Asia-Pacific War"),
    ("빅 픽쳐", "The Big Picture"),
    ("생산기관(부대명)", "Sources"),
    ("생산장소", "Venues"),
    ("촬영자", "Creators"),
    ("주제", "Subjects"),
    ("탐색", "Browse"),
    ("검색", "Search"),
    ("전경", "overall view"),
    ("훈련", "training"),
    ("근무", "duty"),
    ("일상", "everyday life"),
    ("학살", "massacre"),
    ("피난민", "refugees"),
    ("자유의 마을", "Freedom Village"),
    ("자유의 다리", "Freedom Bridge"),
]

LIST_VALUE_MAP = {
    "판문점": "Panmunjom",
    "문산": "Munsan",
    "대구": "Daegu",
    "부산": "Busan",
    "나하": "Naha",
    "포로": "Prisoners of War",
    "수용소": "Camp",
    "오픈컬렉션": "Open Collection",
    "해당없음": "Unknown",
    "일본군'위안부'": 'Japanese Military "Comfort Women"',
    "일본군’위안부’": 'Japanese Military "Comfort Women"',
}


def normalise_spacing(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace(" ,", ",")
    text = text.replace("( ", "(").replace(" )", ")")
    return text


def translate_text(text: str) -> str:
    text = text.strip()
    if not text:
      return text
    if text in EXACT_VALUE_MAP:
        return EXACT_VALUE_MAP[text]
    if text in EXACT_TITLE_MAP:
        return EXACT_TITLE_MAP[text]

    translated = text
    for src, dst in PHRASE_MAP:
        translated = translated.replace(src, dst)

    translated = translated.replace("  ", " ")
    translated = normalise_spacing(translated)
    translated = translate_unit_name(translated)
    return translated


def convert_time(value: str) -> str:
    value = value.strip()
    match = re.fullmatch(r"(?:(\d+)\s*분)?\s*(\d+)\s*초", value)
    if not match:
        return value
    minutes = int(match.group(1) or 0)
    seconds = int(match.group(2))
    if minutes and seconds:
        return f"{minutes}m {seconds}s"
    if minutes:
        return f"{minutes}m"
    return f"{seconds}s"


def ordinal(number: str) -> str:
    n = int(number)
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def translate_unit_name(text: str) -> str:
    patterns = [
        (r"미(\d+)해병사단", lambda m: f"U.S. {ordinal(m.group(1))} Marine Division"),
        (r"미(\d+)사단", lambda m: f"U.S. {ordinal(m.group(1))} Division"),
        (r"(\d+)통신운영대대", lambda m: f"{ordinal(m.group(1))} Signal Operations Battalion"),
        (r"(\d+)통신서비스중대", lambda m: f"{ordinal(m.group(1))} Signal Service Company"),
        (r"(\d+)통신중대", lambda m: f"{ordinal(m.group(1))} Signal Company"),
        (r"(\d+)보병사단", lambda m: f"{ordinal(m.group(1))} Infantry Division"),
    ]
    translated = text
    for pattern, repl in patterns:
        translated = re.sub(pattern, repl, translated)
    return translated


def read_source_scalar(path: Path, key: str) -> str | None:
    source_path = Path(str(path).replace(".en.md", ".md"))
    if not source_path.exists():
        return None
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.*)$")
    for line in source_path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        value = match.group(1).strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        return value
    return None


def read_source_list_map(path: Path) -> dict[str, list[str]]:
    source_path = Path(str(path).replace(".en.md", ".md"))
    if not source_path.exists():
        return {}
    content = source_path.read_text(encoding="utf-8").splitlines()
    result: dict[str, list[str]] = {}
    current_key: str | None = None
    for line in content:
        key_match = re.match(r"^([A-Za-z0-9_]+):\s*$", line)
        if key_match:
            current_key = key_match.group(1)
            result.setdefault(current_key, [])
            continue
        if re.match(r"^\S.*:\s*", line):
            current_key = None
            continue
        if current_key and re.match(r"^\s*-\s*", line):
            value = re.sub(r"^\s*-\s*", "", line).strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            result.setdefault(current_key, []).append(value)
    return result


def translate_description_status(value: str, path: Path) -> str:
    source_value = read_source_scalar(path, "description_status") or value
    source_value = source_value.strip()
    if source_value in EXACT_DESCRIPTION_STATUS_MAP:
        return EXACT_DESCRIPTION_STATUS_MAP[source_value]
    return source_value


def translate_from_source_scalar(path: Path, key: str, fallback: str) -> str:
    source_value = read_source_scalar(path, key)
    return translate_text(source_value if source_value is not None else fallback)


def replace_scalar(line: str, key: str, transform) -> str:
    pattern = rf'^({re.escape(key)}:\s*)(.*)$'
    match = re.match(pattern, line)
    if not match:
        return line
    prefix, raw_value = match.groups()
    value = raw_value.strip()
    quote = ""
    if value.startswith('"') and value.endswith('"'):
        quote = '"'
        value = value[1:-1]
    elif value.startswith("'") and value.endswith("'"):
        quote = "'"
        value = value[1:-1]
    new_value = transform(value)
    if '"' in new_value and quote == '"':
        quote = "'"
    if quote:
        return f"{prefix}{quote}{new_value}{quote}"
    return f"{prefix}{new_value}"


def translate_list_item(line: str) -> str:
    match = re.match(r'^(\s*-\s*)(.*)$', line)
    if not match:
        return line
    prefix, raw_value = match.groups()
    value = raw_value.strip()
    quote = ""
    if value.startswith('"') and value.endswith('"'):
        quote = '"'
        value = value[1:-1]
    translated = LIST_VALUE_MAP.get(value, translate_text(value))
    if '"' in translated and quote == '"':
        quote = "'"
    if quote:
        return f"{prefix}{quote}{translated}{quote}"
    return f"{prefix}{translated}"


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    if not original.startswith("---\n"):
        return False

    try:
        _, frontmatter, body = original.split("---\n", 2)
    except ValueError:
        return False

    lines = frontmatter.splitlines()
    source_lists = read_source_list_map(path)
    current_list = None
    list_index: dict[str, int] = {}
    updated_lines = []

    for line in lines:
        if re.match(r"^[A-Za-z0-9_]+:\s*$", line):
            current_list = line.split(":", 1)[0]
            updated_lines.append(line)
            continue

        if re.match(r"^\S.*:\s*", line):
            current_list = None

        new_line = line
        if current_list in {"venues", "sources", "creators", "subjects", "tags"} and re.match(r"^\s*-\s*", line):
            values = source_lists.get(current_list, [])
            index = list_index.get(current_list, 0)
            list_index[current_list] = index + 1
            if index < len(values):
                raw_value = values[index]
                translated = LIST_VALUE_MAP.get(raw_value, translate_text(raw_value))
                prefix = re.match(r"^(\s*-\s*)", line).group(1)
                quote = "'" if '"' in translated else '"'
                new_line = f"{prefix}{quote}{translated}{quote}"
            else:
                new_line = translate_list_item(line)
        else:
            new_line = replace_scalar(new_line, "title", translate_text)
            new_line = replace_scalar(new_line, "description_status", lambda value: translate_description_status(value, path))
            new_line = replace_scalar(new_line, "description", translate_text)
            new_line = replace_scalar(new_line, "acquisition_transfer", translate_text)
            new_line = replace_scalar(new_line, "level__rg", lambda value: translate_from_source_scalar(path, "level__rg", value))
            new_line = replace_scalar(new_line, "level__series", lambda value: translate_from_source_scalar(path, "level__series", value))
            new_line = replace_scalar(new_line, "time_courts", convert_time)
        updated_lines.append(new_line)

    updated = "---\n" + "\n".join(updated_lines) + "\n---\n" + body
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.en.md")):
        if process_file(path):
            changed += 1
    print(changed)


if __name__ == "__main__":
    main()
