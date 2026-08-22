#!/usr/bin/env python3
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_json(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def resolve(selector):
    reg = load_json('04_PERSONA_SELECTOR_REGISTRY.json')
    key = selector.strip().upper()
    matches = [x for x in reg['selectors'] if x['selector'].upper() == key]
    if len(matches) != 1:
        raise ValueError('REVIEW_REQUIRED: selector unresolved or ambiguous')
    return matches[0]

def runtime_loadout(selector):
    resolved = resolve(selector)
    idx = load_json('05_PERSONA_MEMORY_INDEX.json')
    ent = next((x for x in idx['entries'] if x['code'] == resolved['selector']), None)
    if ent is None:
        raise ValueError('REVIEW_REQUIRED: memory route missing')
    tasks = load_json('08_CURRENT_TASK_BLOCKER_REGISTRY.json')
    common = (ROOT / idx['common_runtime_view']).read_text(encoding='utf-8')
    memory = (ROOT / ent['memory']).read_text(encoding='utf-8')
    return {
        'CURRENT_PERSONA_LOCK': resolved['selector'],
        'persona_id': resolved['persona_id'],
        'common_runtime_view': common,
        'persona_runtime_view': memory,
        'memory_path': ent['memory'],
        'worklog_path': ent['worklog'],
        'program_state': tasks['state'],
        'blockers': tasks['blockers'],
        'cutover': tasks['cutover']
    }

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: byul_persona_bootstrap.py <selector>')
    print(json.dumps(runtime_loadout(sys.argv[1]), ensure_ascii=False, indent=2))
