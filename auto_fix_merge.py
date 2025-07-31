#!/usr/bin/env python3
import subprocess
from pathlib import Path


def get_conflicted_files():
    result = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=U'],
                            check=True, capture_output=True, text=True)
    return [Path(f) for f in result.stdout.strip().split('\n') if f]


def fix_conflicts(strategy='theirs'):
    files = get_conflicted_files()
    for f in files:
        if strategy == 'theirs':
            subprocess.run(['git', 'checkout', '--theirs', str(f)], check=True)
        else:
            subprocess.run(['git', 'checkout', '--ours', str(f)], check=True)
        subprocess.run(['git', 'add', str(f)], check=True)
    if files:
        subprocess.run(
            ['git', 'commit', '-m', 'Auto-resolved merge conflicts'],
            check=True,
        )


if __name__ == '__main__':
    fix_conflicts()
