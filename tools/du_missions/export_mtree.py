# -*- coding: utf-8 -*-
"""Export Denmark Universalis missions to EU5 Mission Tree Editor .mtree (format 2).

Run from any directory:
    python tools/du_missions/export_mtree.py
Optional output folder:
    python tools/du_missions/export_mtree.py output/editor_missions

This reads the existing mission generators; it does not rewrite or discard their
gameplay conditions, effects, AI branches, or prerequisite relationships.
"""
import json
import re
import sys
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import framework as F
import age1_a
import age1_b
import age2


def block(src, name):
    """Return the contents of one top-level Paradox script block.

    The rendered task and tree use one tab for direct fields. Counting braces
    (rather than regex matching to the first closing brace) preserves nested
    AI conditions, scripted effects, and complex rewards.
    """
    match = re.search(r"(?m)^\t" + re.escape(name) + r"\s*=\s*\{", src)
    if not match:
        return ""
    start = match.end()
    depth = 1
    quote = False
    escape = False
    for i in range(start, len(src)):
        c = src[i]
        if quote:
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                quote = False
            continue
        if c == '"':
            quote = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return textwrap.dedent(src[start:i].strip("\n")).strip()
    raise ValueError("Unbalanced block: " + name)


def convert(m):
    group_id = "group_1"
    missions = []
    ids = {task.tid for task in m.tasks}
    for task in m.tasks:
        for req in task.req:
            if req not in ids:
                raise ValueError("%s: missing dependency %s" % (m.key, req))
        rendered_task = F.render_task(m, task)
        missions.append({
            "id": "%s_%s" % (m.key, task.tid),
            "name": task.name,
            "desc": task.desc,
            "icon": task.icon or "",
            "group": group_id,
            "requires": ["%s_%s" % (m.key, req) for req in task.req],
            "duration_days": task.duration or 0,
            "final": bool(task.final),
            "notes": "Imported from Denmark Universalis mission generator.",
            "manual_index": None,
            "blocks": {
                field: block(rendered_task, field)
                for field in ("visible", "enabled", "bypass", "highlight",
                              "select_trigger", "modifier_while_progressing",
                              "on_start", "on_completion",
                              "on_persistent_completion", "on_persistent_start",
                              "on_monthly")
            },
        })
    doc = {
        "format": "eu5-mission-tree/2",
        "icon_folder": "",
        "tree": {
            "id": m.key,
            "name": m.name,
            "icon": m.icon or "",
            "repeatable": False,
            "player_playstyle": m.playstyle or "",
            "chance": m.chance,
            "notes": m.desc,
            "blocks": {
                name: value
                for name, value in {
                    "visible": m.visible,
                    "enabled": m.enabled,
                    "select_trigger": "",
                    "on_start": "hidden_effect = { if = { limit = { is_ai = yes } du_mission_ai_ventetid_effect = yes } }",
                    "on_completion": "",
                    "on_abort": "",
                }.items()
            },
        },
        "groups": [{
            "id": group_id,
            "name": m.name,
            "color": "#4f81bd",
            "visible": "",
            "notes": "Original Denmark Universalis mission tree.",
        }],
        "missions": missions,
        "exclusive_sets": [],
        "hidden_groups": [],
    }
    return doc


def main():
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent.parent / "editor_missions"
    output.mkdir(parents=True, exist_ok=True)
    trees = [f() for f in age1_a.TREES_A + age1_b.TREES_B]
    trees.extend(age2.missions())
    filenames = set()
    count = 0
    for m in trees:
        if m.key in filenames:
            raise ValueError("Duplicate tree id: " + m.key)
        filenames.add(m.key)
        doc = convert(m)
        path = output / (m.key + ".mtree")
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += len(doc["missions"])
        # Verify every generated document is valid JSON and every prereq resolves.
        reread = json.loads(path.read_text(encoding="utf-8"))
        valid = {task["id"] for task in reread["missions"]}
        for task in reread["missions"]:
            if not set(task["requires"]).issubset(valid):
                raise ValueError("Bad requires in " + path.name)
    print("Exported %s trees and %s tasks to %s" % (len(trees), count, output))


if __name__ == "__main__":
    main()
