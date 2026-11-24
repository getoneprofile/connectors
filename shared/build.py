#!/usr/bin/env python3
"""
Write every store's skills from shared/skills, so a change is made once.

  python3 shared/build.py          write claude/, chatgpt/ and cursor/ skills
  python3 shared/build.py --check  fail when one differs, or names a tool no app is listed

{{name}} in a source is a store's own words (STORES). microsoft/mcptools.json is the
server's own tools/list, the one list every app gets; a skill may name only its tools.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "shared" / "skills"
STORES = {
    "claude": {
        "server": "Oneprofile connector",
        "cannot_buy": "Claude can't",
        "attached": "If they attached a spreadsheet or CSV, read",
        "give_csv": "Give it to the user as a file, or as a short table when it's small.",
        "credits_note": " The free plan has 200 credits a month; what they reach is the number the answer gives.",
    },
    "chatgpt": {
        "server": "Oneprofile app",
        "cannot_buy": "This app can't",
        "attached": "If they attached a spreadsheet or CSV, read",
        "give_csv": "Give it to the user as a file, or as a short table when it's small.",
        "credits_note": " What the credits reach is the number the answer gives.",
    },
    "cursor": {
        "server": "Oneprofile MCP server",
        "cannot_buy": "You can't",
        "attached": "If they attached a spreadsheet or CSV, or point to one in the workspace, read",
        "give_csv": "Save it as a `.csv` file in the workspace where the user asks, or show it as a short table when it's small.",
        "credits_note": " The free plan has 200 credits a month; what they reach is the number the answer gives.",
    },
}
#: Backticked words in a skill that are arguments, values or columns, never tools.
NOT_TOOLS = re.compile(r"`([a-z]+(?:_[a-z]+)+)`")


def rendered(source: str, words: dict[str, str]) -> str:
    text = re.sub(r"\{\{(\w+)\}\}", lambda match: words[match.group(1)], source)
    if "{{" in text:
        raise SystemExit("a placeholder was left unfilled")
    return text


def listed() -> tuple[set[str], set[str]]:
    tools = json.loads((ROOT / "microsoft" / "mcptools.json").read_text())["tools"]
    text = json.dumps(tools)
    return {tool["name"] for tool in tools}, set(re.findall(r"[a-z]+(?:_[a-z]+)+", text))


def microsoft_tools() -> str:
    """The tool tables of microsoft/intro.md, from the list itself."""
    tools = json.loads((ROOT / "microsoft" / "mcptools.json").read_text())["tools"]
    groups: dict[str, list[str]] = {"Looks things up": [], "Changes the workspace": [], "Can send, remove or overwrite": []}
    for tool in tools:
        hints = tool["annotations"]
        if hints["readOnlyHint"]:
            group = "Looks things up"
        elif hints["destructiveHint"]:
            group = "Can send, remove or overwrite"
        else:
            group = "Changes the workspace"
        groups[group].append(f"| `{tool['name']}` | {hints['title']} |")
    return "\n\n".join(
        f"### {name}\n\n| Tool | What it does |\n| --- | --- |\n" + "\n".join(rows)
        for name, rows in groups.items()
    )


def microsoft_intro(text: str) -> str:
    start = text.index("## Supported operations")
    end = text.index("## Obtaining credentials")
    return (
        text[:start]
        + "## Supported operations\n\nThe server acts as you, in the one Oneprofile workspace you pick when you sign in, "
        "with the everyday tools of the AI Assistant inside Oneprofile. Each tool does one job and says whether it only "
        "looks things up, changes the workspace, or can send, remove or overwrite something.\n\n"
        + microsoft_tools()
        + "\n\n"
        + text[end:]
    )


def main() -> int:
    check = "--check" in sys.argv
    names, words_in_schemas = listed()
    problems: list[str] = []
    for source in sorted(SKILLS.glob("*.md")):
        text = source.read_text()
        for word in NOT_TOOLS.findall(text):
            if word not in names and word not in words_in_schemas:
                problems.append(f"{source.name} names {word}, which no app is listed")
        for word in re.findall(r"\b(?:run_(?:read|change|send_or_remove)_tool|describe_tool|list_\w+_tools)\b", text):
            problems.append(f"{source.name} names {word}")
        for store, words in STORES.items():
            target = ROOT / store / "skills" / source.stem / "SKILL.md"
            body = rendered(text, words)
            if check:
                if not target.exists() or target.read_text() != body:
                    problems.append(f"{target.relative_to(ROOT)} is not built from shared/skills")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(body)
    intro = ROOT / "microsoft" / "intro.md"
    built = microsoft_intro(intro.read_text())
    if check and intro.read_text() != built:
        problems.append("microsoft/intro.md's tool tables are not built from mcptools.json")
    elif not check:
        intro.write_text(built)
    print("\n".join(problems) or "ok")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
