#!/usr/bin/env python3
"""Checks the organization profile for the two things that can be wrong in it.

The profile is prose and links. Dashes the project does not use creep in
from editors, and a link to a repository the organization does not have is
the reader's first impression of a project that cannot keep its own index
current.
"""

import re
import sys
from pathlib import Path

REPOSITORIES = {"circuits", "prover", "docs", "contracts", ".github"}

REPOSITORY_LINK = re.compile(r"https://github\.com/zkICAO/([A-Za-z0-9_.-]+)")

DASHES = {"—": "em dash", "–": "en dash"}


def main():
    failures = []

    for document in sorted(Path(".").rglob("*.md")):
        for number, line in enumerate(document.read_text().splitlines(), start=1):
            for character, name in DASHES.items():
                if character in line:
                    failures.append(f"{document}:{number}: {name}")

            for match in REPOSITORY_LINK.finditer(line):
                named = match.group(1).split("/")[0]

                if named not in REPOSITORIES:
                    failures.append(
                        f"{document}:{number}: links to zkICAO/{named}, which is not a repository"
                    )

    for failure in failures:
        print(failure)

    print(f"{len(failures)} problems")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
