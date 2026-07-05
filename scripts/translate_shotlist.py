#!/usr/bin/env python3
"""Translate Korean shotlist to English in .en.md files."""

import os
import re
import sys

# Translation dictionary for shotlist patterns
SHOTLIST_TRANSLATIONS = {
    # Common prefixes
    "숏 리스트 #": "Shot List #",
    "슬레이트": "Slate",
    "슬레이트 없음": "No slate",
    
    # Time markers
    "초": "sec",
    "분": "min",
    
    # Shot descriptions
    "보인다": "is visible",
    "보인다.": "is visible.",
    "이동한다": "is moving",
    "이동하고 있다": "is moving",
    "촬영되고 있다": "is being filmed",
    "나타나고 있다": "appears",
    "등장한다": "appears",
    "들어간다": "enters",
    "걸어간다": "walks",
    "뛰어간다": "runs",
    "운반하고 있다": "is transporting",
    "건설하고 있다": "is constructing",
    "시찰하고 있다": "is inspecting",
    "훈련하고 있다": "is training",
    "근무하고 있다": "is on duty",
    "순찰하고 있다": "is patrolling",
    "교체하고 있다": "is exchanging",
    "이송되고 있다": "is being transported",
    "수송되고 있다": "is being shipped",
    "포획되고 있다": "is being captured",
    "석방되고 있다": "is being released",
    "교환되고 있다": "is being exchanged",
    
    # Military terms
    "미군": "U.S. forces",
    "미 육군": "U.S. Army",
    "미 해병": "U.S. Marines",
    "미 공군": "U.S. Air Force",
    "미 해군": "U.S. Navy",
    "한국군": "ROK forces",
    "북한군": "North Korean forces",
    "유엔군": "United Nations Command",
    "영연방군": "Commonwealth forces",
    
    # Locations
    "비무장지대": "Demilitarized Zone (DMZ)",
    "군사분계선": "Military Demarcation Line",
    "판문점": "Panmunjom",
    "임진강": "Imjin River",
    "문산": "Munsan",
    "파주": "Paju",
    "개성": "Kaesong",
    "인천": "Incheon",
    "서울": "Seoul",
    "부산": "Busan",
    
    # Actions
    "촬영": "filming",
    "촬영한": "filmed",
    "촬영되었다": "was filmed",
    "제작되었다": "was produced",
    "기록되었다": "was recorded",
    "방문했다": "visited",
    "시찰했다": "inspected",
    "훈련": "training",
    "근무": "duty",
    "순찰": "patrol",
    "전투": "combat",
    "교환": "exchange",
    "이송": "transport",
    "석방": "release",
    "포로": "prisoner of war",
    "수용소": "camp",
    
    # Common endings
    "것이다": ".",
    " 것이다": ".",
    "입니다": ".",
    "습니다": ".",
    "한다": ".",
    "한다.": ".",
    "있다": ".",
    "있다.": ".",
}

def translate_shotlist(text):
    """Simple translation using dictionary patterns."""
    if not text:
        return text
    
    # Check if text contains Korean
    if not re.search('[가-힣]', text):
        return text
    
    # Apply translations
    result = text
    for korean, english in sorted(SHOTLIST_TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        result = result.replace(korean, english)
    
    # If still has Korean, mark for manual review
    if re.search('[가-힣]', result):
        result = result + " [NEEDS REVIEW]"
    
    return result

def process_file(filepath):
    """Process a single .en.md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find shotlist line
    match = re.search(r'^shotlist:\s*"(.*?)"', content, re.MULTILINE | re.DOTALL)
    if not match:
        return False
    
    original = match.group(1)
    
    # Check if it contains Korean
    if not re.search('[가-힣]', original):
        return False
    
    # Skip if just "해당없음"
    if original.strip() == "해당없음":
        new_content = content.replace(
            f'shotlist: "{original}"',
            'shotlist: "N/A"'
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    # Translate
    translated = translate_shotlist(original)
    
    # Replace in content
    new_content = content.replace(
        f'shotlist: "{original}"',
        f'shotlist: "{translated}"'
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    base_dir = "/Users/woonjjang/ai/archivej/facwa/content/items"
    
    count = 0
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.en.md'):
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    count += 1
                    if count % 50 == 0:
                        print(f"Progress: {count} files translated...")
    
    print(f"\nTotal shotlist files translated: {count}")

if __name__ == "__main__":
    main()
