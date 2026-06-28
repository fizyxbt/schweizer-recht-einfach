#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"


def main() -> int:
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugins = marketplace["plugins"]
    skill_files = []
    for plugin in plugins:
        source = plugin["source"].removeprefix("./")
        skill_files.extend(sorted((ROOT / source / "skills").glob("*/SKILL.md")))
    print(json.dumps({"plugins": len(plugins), "skills": len(skill_files)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
