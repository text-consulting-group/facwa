#!/usr/bin/env python3
import argparse
import os
import re
from pathlib import Path


def is_yaml_problem_line(line: str) -> bool:
    # Detect shotlist or description_status as quoted strings containing unescaped quotes
    m = re.match(r'^(?P<indent>\s*)(?P<key>shotlist|description_status):\s*"(?P<value>.*)"\s*$', line)
    if not m:
        return False

    value = m.group('value')
    # If the quoted value contains unescaped double quotes, it's invalid YAML
    if '"' in value:
        return True
    return False


def scan_file(path: Path):
    problems = []
    lines = path.read_text(encoding='utf-8').splitlines()
    for i, line in enumerate(lines, start=1):
        if is_yaml_problem_line(line):
            problems.append((i, line))
    return problems


def scan_dir(root: Path, ext: str):
    problems = {}
    for path in sorted(root.rglob(f'*{ext}')):
        if path.is_file():
            file_problems = scan_file(path)
            if file_problems:
                problems[path] = file_problems
    return problems


def main():
    parser = argparse.ArgumentParser(description='Scan markdown files for YAML quote issues in shotlist/description_status fields.')
    parser.add_argument('path', nargs='?', default='content', help='Root path to scan')
    parser.add_argument('--ext', default='.md', help='File extension to scan')
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists():
        raise SystemExit(f'Path not found: {root}')

    problems = scan_dir(root, args.ext)
    if not problems:
        print('No YAML problems found.')
        return

    for path, file_problems in problems.items():
        print(path)
        for line_no, line in file_problems:
            print(f'  {line_no}: {line}')
        print()
    print(f'Found {sum(len(v) for v in problems.values())} YAML issue lines in {len(problems)} files.')


if __name__ == '__main__':
    main()
