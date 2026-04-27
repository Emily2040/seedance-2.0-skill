#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
EXPECTED = ['seedance-antislop','seedance-audio','seedance-camera','seedance-characters','seedance-copyright','seedance-examples-zh','seedance-filter','seedance-interview-short','seedance-interview','seedance-lighting','seedance-motion','seedance-pipeline','seedance-prompt-short','seedance-prompt','seedance-recipes','seedance-style','seedance-troubleshoot','seedance-vfx','seedance-vocab-es','seedance-vocab-ja','seedance-vocab-ko','seedance-vocab-ru','seedance-vocab-zh']
REQ_REFS = ['references/api-status.md','references/source-registry.md','references/platform-constraints.md','references/audio-guide.md','references/anti-slop-lexicon.md','references/filter-vocab.md']
REQ_FILES = ['scripts/validate_skills.py','scripts/content_audit.py','.github/workflows/validate-skills.yml','evals/evals.json']
STALE = ['Feb 2026 Status','API global release was delayed','real-person face uploads paused']
REQUIRED = ['name','description','license','user-invocable','user-invokable','tags','metadata']
def split_fm(text):
    text = text.lstrip('\ufeff')
    if not text.startswith('---'): raise ValueError('missing opening ---')
    rest = text[3:]; end = rest.find('---')
    if end < 0: raise ValueError('missing closing ---')
    return rest[:end].strip(), rest[end+3:].lstrip()
def top_keys(fm):
    keys=[]
    for line in fm.splitlines():
        if not line.strip() or line.lstrip().startswith('#'): continue
        if not line.startswith(' ') and ':' in line:
            keys.append(line.split(':',1)[0].strip())
    return keys
def value_for(fm, key):
    m=re.search(rf'^{re.escape(key)}:\s*(.*)$', fm, re.M)
    if not m: return None
    v=m.group(1).strip()
    if len(v)>=2 and v[0] in '"\'' and v[-1]==v[0]: v=v[1:-1]
    return v
def metadata_value(fm, key):
    in_meta=False
    for line in fm.splitlines():
        if line.startswith('metadata:'): in_meta=True; continue
        if in_meta:
            if line and not line.startswith(' '): break
            m=re.match(rf'^\s+{re.escape(key)}:\s*(.*)$', line)
            if m:
                v=m.group(1).strip()
                if len(v)>=2 and v[0] in '"\'' and v[-1]==v[0]: v=v[1:-1]
                return v
    return None
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('repo', nargs='?', default='.'); ap.add_argument('--strict', action='store_true'); args=ap.parse_args()
    root=Path(args.repo).resolve(); errors=[]; warnings=[]
    skill_files=[root/'SKILL.md']+[root/'skills'/n/'SKILL.md' for n in EXPECTED]
    for path in skill_files:
        if not path.exists(): errors.append(f'missing skill file: {path.relative_to(root)}'); continue
        try:
            fm, body = split_fm(path.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f'{path.relative_to(root)}: frontmatter parse error: {exc}'); continue
        rel=str(path.relative_to(root)); keys=top_keys(fm)
        for field in REQUIRED:
            if field not in keys: errors.append(f'{rel}: missing `{field}`')
        if 'parent' in keys: errors.append(f'{rel}: illegal top-level `parent`; must be inside metadata')
        if path != root/'SKILL.md' and metadata_value(fm,'parent') != 'seedance-20': errors.append(f'{rel}: missing metadata.parent=seedance-20')
        desc=value_for(fm,'description') or ''
        if 'This skill should be used when' not in desc: warnings.append(f'{rel}: description should use third-person trigger phrasing')
        if metadata_value(fm,'version') != '5.1.0': warnings.append(f'{rel}: metadata.version is not 5.1.0')
        name=value_for(fm,'name')
        if path != root/'SKILL.md' and path.parent.name.startswith('seedance-') and name != path.parent.name: errors.append(f'{rel}: name does not match folder')
    dirs=sorted(p.name for p in (root/'skills').glob('seedance-*') if p.is_dir()) if (root/'skills').exists() else []
    missing=sorted(set(EXPECTED)-set(dirs)); extra=sorted(set(dirs)-set(EXPECTED))
    if missing: errors.append('missing expected sub-skill dirs: '+', '.join(missing))
    if extra: warnings.append('extra sub-skill dirs: '+', '.join(extra))
    for rel in REQ_REFS+REQ_FILES:
        if not (root/rel).exists(): errors.append(f'missing required v5.1.0 file: {rel}')
    ev=root/'evals'/'evals.json'
    if ev.exists():
        try:
            cases=json.loads(ev.read_text(encoding='utf-8')).get('cases',[])
            if len(cases)<10: errors.append('evals/evals.json must contain at least 10 cases')
        except Exception as exc: errors.append(f'evals/evals.json parse error: {exc}')
    for rel in ['README.md','SKILL.md','references/platform-constraints.md','references/api-status.md']:
        path=root/rel
        if path.exists():
            text=path.read_text(encoding='utf-8', errors='ignore')
            for phrase in STALE:
                if phrase in text: errors.append(f'{rel} contains stale active-status phrase: {phrase}')
    if warnings:
        print('WARNINGS:'); [print('- '+w) for w in warnings]; print()
    if errors:
        print('ERRORS:'); [print('- '+e) for e in errors]; return 1
    print(f'Validated {len(skill_files)} skill files, {len(REQ_REFS)} required references, CI workflow, and evals.')
    return 0
if __name__ == '__main__': raise SystemExit(main())
