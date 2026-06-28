#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
README_RE = re.compile(r"\| (Plugins|Skills) \| ([0-9]+) \|")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{rel(path)}: invalid JSON: {exc}")
        return {}


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(?P<body>.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{rel(path)}: missing YAML frontmatter")
        return {}
    data: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{rel(path)}: malformed frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key not in {"name", "description"}:
            errors.append(f"{rel(path)}: unsupported frontmatter field {key}")
        data[key] = value
    if "name" not in data:
        errors.append(f"{rel(path)}: missing name")
    if "description" not in data:
        errors.append(f"{rel(path)}: missing description")
    if data.get("name") and not NAME_RE.fullmatch(data["name"]):
        errors.append(f"{rel(path)}: invalid skill name {data['name']}")
    if len(data.get("description", "")) > 1024:
        errors.append(f"{rel(path)}: description exceeds 1024 chars")
    return data


def validate_links(errors: list[str]) -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if re.match(r"^(https?://|mailto:|#)", target):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).exists():
                errors.append(f"{rel(path)}: missing local link {target}")


def validate_readme_counts(plugin_count: int, skill_count: int, errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    found = dict(README_RE.findall(readme))
    if found.get("Plugins") != str(plugin_count):
        errors.append(f"README.md: Plugins count is {found.get('Plugins')} but actual is {plugin_count}")
    if found.get("Skills") != str(skill_count):
        errors.append(f"README.md: Skills count is {found.get('Skills')} but actual is {skill_count}")


def validate_coverage_files(errors: list[str]) -> None:
    required = [
        ROOT / "references" / "abdeckung.md",
        ROOT / "references" / "einfache-beispiele.md",
        ROOT / "references" / "rechtsgebiete-index.md",
        ROOT / "references" / "grundrechte-katalog.md",
        ROOT / "references" / "kantonale-abdeckung.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"{rel(path)}: required coverage file missing")


def main() -> int:
    errors: list[str] = []
    marketplace = load_json(MARKETPLACE, errors)
    plugins = marketplace.get("plugins", [])
    if not isinstance(plugins, list) or not plugins:
        errors.append(".claude-plugin/marketplace.json: plugins must be a non-empty array")
        plugins = []

    names: set[str] = set()
    skill_count = 0
    for plugin in plugins:
        name = plugin.get("name", "")
        source = plugin.get("source", "")
        if not NAME_RE.fullmatch(name):
            errors.append(f"marketplace: invalid plugin name {name}")
        if name in names:
            errors.append(f"marketplace: duplicate plugin name {name}")
        names.add(name)
        if not isinstance(source, str) or not source.startswith("./"):
            errors.append(f"{name}: source must start with ./")
            continue
        root = ROOT / source.removeprefix("./")
        manifest = root / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            errors.append(f"{name}: missing .claude-plugin/plugin.json")
            continue
        data = load_json(manifest, errors)
        if data.get("name") != name:
            errors.append(f"{rel(manifest)}: name does not match marketplace")
        if not VERSION_RE.fullmatch(str(data.get("version", ""))):
            errors.append(f"{rel(manifest)}: version must be x.y.z")
        for skill in sorted((root / "skills").glob("*/SKILL.md")):
            skill_count += 1
            fm = parse_frontmatter(skill, errors)
            if fm.get("name") != skill.parent.name:
                errors.append(f"{rel(skill)}: name must match skill folder")
        example = root / "examples" / "beispiel-einfach.md"
        if not example.exists():
            errors.append(f"{plugin['name']}: missing examples/beispiel-einfach.md")

    validate_links(errors)
    validate_readme_counts(len(plugins), skill_count, errors)
    validate_coverage_files(errors)

    if errors:
        print(f"validate failed with {len(errors)} issue(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"validate OK ({len(plugins)} plugins, {skill_count} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
