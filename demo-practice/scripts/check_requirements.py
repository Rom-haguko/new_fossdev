from __future__ import annotations

import ast
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"

STDLIB_MODULES = {
    "abc", "argparse", "ast", "asyncio", "collections", "dataclasses", "datetime",
    "functools", "itertools", "json", "logging", "math", "os", "pathlib", "re",
    "sys", "time", "typing", "unittest"
}

IMPORT_TO_PACKAGE = {
    "fastapi": "fastapi",
    "numpy": "numpy",
    "requests": "requests",
    "pytest": "pytest",
}


def extract_imports_from_file(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])

    return imports


def extract_project_imports(src_dir: Path) -> set[str]:
    result: set[str] = set()
    for py_file in src_dir.rglob("*.py"):
        result |= extract_imports_from_file(py_file)
    return result


def load_declared_requirements(path: Path) -> set[str]:
    declared: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        pkg = line.split("==")[0].split(">=")[0].split("[")[0].strip().lower()
        declared.add(pkg)
    return declared


def main() -> int:
    imports = extract_project_imports(SRC_DIR)
    external_imports = {
        IMPORT_TO_PACKAGE.get(name, name).lower()
        for name in imports
        if name not in STDLIB_MODULES
    }

    declared = load_declared_requirements(REQUIREMENTS_FILE)

    missing = sorted(external_imports - declared)
    unused = sorted(declared - external_imports - {"mypy", "ruff"})

    if missing:
        print("Missing dependencies in requirements.txt:")
        for dep in missing:
            print(f"  - {dep}")

    if unused:
        print("Possibly unused dependencies in requirements.txt:")
        for dep in unused:
            print(f"  - {dep}")

    if missing:
        return 1

    print("Dependency declaration check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
