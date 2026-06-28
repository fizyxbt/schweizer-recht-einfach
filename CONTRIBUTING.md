# Contributing

## Scope

Add plugins only when they have a clear Swiss-law workflow, official source anchors and at least one usable skill.

## Rules

1. Keep skill frontmatter to `name` and `description`.
2. Keep skill names lowercase hyphen-case and under 64 characters.
3. Use Fedlex for federal legal sources.
4. Use official cantonal collections for cantonal law.
5. Use Bundesgericht sources for BGE and judgments.
6. Run `python3 scripts/validate.py` before opening a pull request.

## Adding a plugin

1. Add `<plugin>/.claude-plugin/plugin.json`.
2. Add `<plugin>/README.md`.
3. Add at least one `<plugin>/skills/<skill>/SKILL.md`.
4. Add the plugin to `.claude-plugin/marketplace.json`.
5. Update the counts in `README.md`.
