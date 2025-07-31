#!/usr/bin/env python3
"""Helper script to automatically resolve merge conflicts."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import Iterable


def get_conflicted_files() -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=U"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(f) for f in result.stdout.strip().split("\n") if f]


def apply_strategy(files: Iterable[Path], strategy: str) -> None:
    for f in files:
        choice = "--theirs" if strategy == "theirs" else "--ours"
        subprocess.run(["git", "checkout", choice, str(f)], check=True)
        subprocess.run(["git", "add", str(f)], check=True)


def fix_conflicts(strategy: str = "theirs", commit: bool = True) -> None:
    files = get_conflicted_files()
    if not files:
        print("No merge conflicts detected.")
        return
    apply_strategy(files, strategy)
    if commit:
        subprocess.run(
            ["git", "commit", "-m", "Auto-resolved merge conflicts"],
            check=True,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strategy", choices=["ours", "theirs"], default="theirs")
    parser.add_argument("--no-commit", action="store_true", help="Do not commit")
    args = parser.parse_args()
    fix_conflicts(strategy=args.strategy, commit=not args.no_commit)
