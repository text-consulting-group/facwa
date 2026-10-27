#!/usr/bin/env python3
"""Translate Korean description_status to English in .en.md files."""

import os
import re
import sys

# Translation dictionary for common patterns
TRANSLATIONS = {
    # Common phrases
    "이 영상은": "This footage shows",
    "이 장면은": "This scene shows",
    "이 사진은": "This photo shows",
    "이 문서는": "This document shows",
    "촬영한 부대는": "The filming unit was",
    "촬영자는": "The photographer was",
    "촬영 카메라는": "The camera used was",
    "전체적으로 영상은": "Overall, the footage is",
    "영상은": "The footage",
    "영상에 나오는": "Featured in the footage",
    "장면이": "scenes are",
    "장면을": "scenes",
    "구성되어 있다": "is composed of",
    "보여주고 있다": "shows",
    "담고 있다": "contains",
    "나타나고 있다": "appears",
    "기록되어 있다": "is recorded",
    
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
    "도라산": "Dorasan",
    
    # Time periods
    "한국전쟁": "Korean War",
    "정전협정": "Armistice Agreement",
    "휴전": "ceasefire",
    
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
}

def translate_korean_to_english(text):
    """Simple translation using dictionary patterns."""
    if not text:
        return text
    
    # Check if text contains Korean
    if not re.search('[가-힣]', text):
        return text
    
    # Apply translations
    result = text
    for korean, english in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        result = result.replace(korean, english)
    
    # If still has Korean, mark for manual review
    if re.search('[가-힣]', result):
        result = result + " [NEEDS REVIEW]"
    
    return result

def process_file(filepath):
    """Process a single .en.md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find description_status line
    match = re.search(r'^description_status:\s*"(.*?)"', content, re.MULTILINE | re.DOTALL)
    if not match:
        return False
    
    original = match.group(1)
    
    # Check if it contains Korean
    if not re.search('[가-힣]', original):
        return False
    
    # Translate
    translated = translate_korean_to_english(original)
    
    # Replace in content
    new_content = content.replace(
        f'description_status: "{original}"',
        f'description_status: "{translated}"'
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
                    print(f"Translated: {filepath}")
    
    print(f"\nTotal files translated: {count}")

if __name__ == "__main__":
    main()
