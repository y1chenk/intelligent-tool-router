#!/usr/bin/env python3
"""Check manifest consistency or build a deterministic, self-contained ZIP."""

import argparse
import copy
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SHARED_FIELDS = (
    "name", "version", "description", "author", "homepage", "repository",
    "license", "keywords",
)
OMIT_PARTS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
ROOT_FILES = {"plugin.json", "README.md", "README_EN.md", "CHANGELOG.md", "LICENSE"}
ROOT_DIRS = {"skills", "scripts", "assets", ".codex-plugin"}


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"Duplicate JSON key: {key}")
        value[key] = item
    return value


def read_json(path):
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def manifests():
    source = read_json(ROOT / "plugin.json")
    name = source.get("name", "")
    if not isinstance(name, str) or not re.fullmatch(
        r"(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?", name
    ) or len(name) > 64 or name != ROOT.name:
        raise ValueError("Manifest name must match the containing directory.")
    if source.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("Unexpected portable manifest schema.")
    version = source.get("version", "")
    if not isinstance(version, str) or not re.fullmatch(
        r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", version
    ):
        raise ValueError("Use a release version such as 0.2.0.")
    interface = source["extensions"]["com.openai"]["interface"]
    if not isinstance(interface, dict):
        raise ValueError("interface must be a JSON object.")
    for key in ("displayName", "shortDescription", "longDescription"):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            raise ValueError(f"Missing interface text: {key}")
    if len(interface["shortDescription"]) > 30:
        raise ValueError("Listing shortDescription exceeds 30 characters.")
    prompts = interface.get("defaultPrompt")
    values = [prompts] if isinstance(prompts, str) else prompts
    if not isinstance(values, list) or not 1 <= len(values) <= 3 or any(
        not isinstance(p, str) or not p.strip() for p in values
    ):
        raise ValueError("defaultPrompt must be a string or 1–3 nonempty strings.")
    keywords = source.get("keywords", [])
    if not isinstance(keywords, list) or any(not isinstance(k, str) for k in keywords):
        raise ValueError("keywords must be an array of strings.")
    path = ROOT / ".codex-plugin/plugin.json"
    current = read_json(path) if path.exists() else {"skills": "./skills"}
    expected = copy.deepcopy(current)
    for key in SHARED_FIELDS:
        if key in source:
            expected[key] = copy.deepcopy(source[key])
        else:
            expected.pop(key, None)
    expected["interface"] = copy.deepcopy(interface)
    return path, current, expected


def package_files():
    files = []
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if any(part in OMIT_PARTS for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlinks cannot be packaged: {relative}")
        if not path.is_file() or path.suffix == ".pyc" or path.name == ".DS_Store":
            continue
        if (len(relative.parts) == 1 and path.name not in ROOT_FILES) or (
            len(relative.parts) > 1 and relative.parts[0] not in ROOT_DIRS
        ):
            raise ValueError(f"Unexpected package file: {relative}")
        if any(part.startswith(".") and part != ".codex-plugin" for part in relative.parts):
            raise ValueError(f"Unexpected hidden package file: {relative}")
        files.append(path)
    if not list((ROOT / "skills").glob("*/SKILL.md")):
        raise ValueError("No skills found.")
    return files


def build(output, overlay_path, overlay):
    output = output.resolve()
    if output == ROOT or ROOT in output.parents or output.suffix != ".zip":
        raise ValueError("Write the .zip archive outside the plugin directory.")
    package_files()
    output.parent.mkdir(parents=True, exist_ok=True)
    overlay_path.parent.mkdir(parents=True, exist_ok=True)
    overlay_path.write_text(json.dumps(overlay, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=output.parent, suffix=".zip", delete=False) as handle:
            temporary = Path(handle.name)
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in package_files():
                entry = zipfile.ZipInfo(f"{ROOT.name}/{path.relative_to(ROOT).as_posix()}")
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                entry.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(entry, path.read_bytes(), compresslevel=9)
        os.replace(temporary, output)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    print(f"Built {output} ({output.stat().st_size} bytes)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true", help="Read-only drift and package checks")
    action.add_argument("--output", type=Path, help="Sync the compatibility manifest and build a ZIP")
    args = parser.parse_args()
    try:
        path, current, expected = manifests()
        if args.check:
            if current != expected or not path.is_file():
                raise ValueError("Manifest drift detected; rebuild from root plugin.json.")
            package_files()
            print("Manifest consistency and basic package checks passed.")
        else:
            build(args.output, path, expected)
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
