#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
RISK = {
 'Feb 2026 Status':'stale platform status',
 'API global release was delayed':'stale API status',
 'real-person face uploads paused':'stale likeness status',
 'in the style of Studio Trigger':'studio-name style request',
 'Studio Ghibli':'studio-name style request',
 'Ghibli-style':'studio-name style request',
 'Ghibli style':'studio-name style request',
 'Spider-Man':'named franchise character',
 'always refused':'over-absolute policy claim',
 '37% block rate':'unsourced statistic',
 '37% block-rate':'unsourced statistic',
 'rhythm clone':'copyright-sensitive clone wording',
 'performance clone':'copyright-sensitive clone wording',
 'dance performance clone':'copyright-sensitive clone wording',
}
IGNORE_FILES={'CHANGELOG.md'}
IGNORE_PREFIXES=['.git/','references/migrated/']
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('repo', nargs='?', default='.'); ap.add_argument('--strict', action='store_true'); args=ap.parse_args()
    root=Path(args.repo).resolve(); findings=[]
    for path in root.rglob('*.md'):
        rel=str(path.relative_to(root)).replace('\\','/')
        if path.name in IGNORE_FILES or any(rel.startswith(p) for p in IGNORE_PREFIXES): continue
        text=path.read_text(encoding='utf-8', errors='ignore')
        for phrase, reason in RISK.items():
            if phrase in text: findings.append((rel, phrase, reason))
    if findings:
        print('Content audit findings:')
        for rel, phrase, reason in findings: print(f'- {rel}: `{phrase}` ({reason})')
        return 1 if args.strict else 0
    print('Content audit passed: no active risky/stale phrases found.')
    return 0
if __name__ == '__main__': raise SystemExit(main())
