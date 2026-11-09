"""Utilities for locating the repository root regardless of the current working directory."""

from pathlib import Path


def find_project_root(start: str | Path | None = None) -> Path:
    """Return the repo root by walking upward from the supplied path or the current working directory.

    The project expects to be located at the directory that contains ``generate_data.py`` and the
    ``src`` package. This keeps notebooks and scripts working even when VS Code launches them from a
    nested directory such as ``notebooks/``.
    """
    base = Path(start).resolve() if start is not None else Path.cwd().resolve()
    for candidate in (base, *base.parents):
        if (candidate / "generate_data.py").exists() and (candidate / "src").is_dir():
            return candidate
    raise FileNotFoundError(f"Could not locate the project root from: {base}")
