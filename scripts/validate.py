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


def markdown_table_rows(path: Path, header_marker: str) -> list[list[str]]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        if line.startswith("| ---") or header_marker in line:
            continue
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def validate_coverage_files(errors: list[str]) -> None:
    required = [
        ROOT / "references" / "abdeckung.md",
        ROOT / "references" / "einfache-beispiele.md",
        ROOT / "references" / "rechte-katalog.md",
        ROOT / "references" / "bundesrechte-detailmatrix-einfache-beispiele.md",
        ROOT / "references" / "fedlex-sr-index.md",
        ROOT / "references" / "fedlex-sr-einfache-beispiele.md",
        ROOT / "references" / "fedlex-sr-statistik.md",
        ROOT / "references" / "rechtsgebiete-index.md",
        ROOT / "references" / "sr-feinraster.md",
        ROOT / "references" / "grundrechte-katalog.md",
        ROOT / "references" / "kantonale-abdeckung.md",
        ROOT / "references" / "kantonale-rechte-einfache-beispiele.md",
        ROOT / "references" / "kantone.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"{rel(path)}: required coverage file missing")
    canton_files = sorted((ROOT / "references" / "kantone").glob("*.md"))
    if len(canton_files) != 26:
        errors.append(f"references/kantone: expected 26 canton files, found {len(canton_files)}")
    cantonal_examples = ROOT / "references" / "kantonale-rechte-einfache-beispiele.md"
    if cantonal_examples.exists():
        rows = markdown_table_rows(cantonal_examples, "Kanton | Kürzel")
        if len(rows) < 26 * 30:
            errors.append(
                "references/kantonale-rechte-einfache-beispiele.md: "
                f"expected at least 780 cantonal example rows, found {len(rows)}"
            )
        expected_codes = {
            "AG", "AI", "AR", "BE", "BL", "BS", "FR", "GE", "GL", "GR", "JU", "LU", "NE",
            "NW", "OW", "SG", "SH", "SO", "SZ", "TG", "TI", "UR", "VD", "VS", "ZG", "ZH",
        }
        counts = {code: 0 for code in expected_codes}
        for row in rows:
            if len(row) >= 2 and row[1] in counts:
                counts[row[1]] += 1
        missing = sorted(code for code, count in counts.items() if count < 30)
        if missing:
            errors.append(
                "references/kantonale-rechte-einfache-beispiele.md: "
                f"expected at least 30 examples per canton, missing {', '.join(missing)}"
            )
    rights_catalogue = ROOT / "references" / "rechte-katalog.md"
    if rights_catalogue.exists():
        rows = [
            line for line in rights_catalogue.read_text(encoding="utf-8").splitlines()
            if line.startswith("| ") and not line.startswith("| ---") and "Recht oder Anspruch" not in line
        ]
        if len(rows) < 100:
            errors.append(f"references/rechte-katalog.md: expected at least 100 rights rows, found {len(rows)}")
    federal_detail = ROOT / "references" / "bundesrechte-detailmatrix-einfache-beispiele.md"
    if federal_detail.exists():
        rows = markdown_table_rows(federal_detail, "Rechtsbereich | Recht oder Anspruch")
        if len(rows) < 200:
            errors.append(
                "references/bundesrechte-detailmatrix-einfache-beispiele.md: "
                f"expected at least 200 federal detail rows, found {len(rows)}"
            )
        areas = {row[0] for row in rows if row}
        if len(areas) < 20:
            errors.append(
                "references/bundesrechte-detailmatrix-einfache-beispiele.md: "
                f"expected at least 20 legal areas, found {len(areas)}"
            )
    fedlex_index = ROOT / "references" / "fedlex-sr-index.md"
    fedlex_rows: list[list[str]] = []
    if fedlex_index.exists():
        fedlex_rows = markdown_table_rows(fedlex_index, "SR | Kurztitel")
        if len(fedlex_rows) < 10000:
            errors.append(f"references/fedlex-sr-index.md: expected at least 10000 SR rows, found {len(fedlex_rows)}")
    fedlex_examples = ROOT / "references" / "fedlex-sr-einfache-beispiele.md"
    if fedlex_examples.exists():
        rows = markdown_table_rows(fedlex_examples, "SR | Titel")
        if len(rows) < 10000:
            errors.append(f"references/fedlex-sr-einfache-beispiele.md: expected at least 10000 example rows, found {len(rows)}")
        if fedlex_rows and len(rows) != len(fedlex_rows):
            errors.append(
                "references/fedlex-sr-einfache-beispiele.md: "
                f"example row count {len(rows)} does not match Fedlex index row count {len(fedlex_rows)}"
            )
        if fedlex_rows and len(rows) == len(fedlex_rows):
            for number, (index_row, example_row) in enumerate(zip(fedlex_rows, rows), start=1):
                if len(index_row) < 3 or len(example_row) < 2:
                    errors.append(f"references/fedlex-sr-einfache-beispiele.md: malformed table row {number}")
                    continue
                if index_row[0] != example_row[0] or index_row[2] != example_row[1]:
                    errors.append(
                        "references/fedlex-sr-einfache-beispiele.md: "
                        f"row {number} does not match index ({index_row[0]} {index_row[2]})"
                    )
                    break
    fedlex_stats = ROOT / "references" / "fedlex-sr-statistik.md"
    if fedlex_stats.exists():
        text = fedlex_stats.read_text(encoding="utf-8")
        for group in range(10):
            if f"| {group} " not in text:
                errors.append(f"references/fedlex-sr-statistik.md: missing SR main group {group}")


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
