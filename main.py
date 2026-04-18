"""
Entry point placeholder for the shared global plan generator project.
"""

from __future__ import annotations

from config import LLM_MODEL, PROJECT_NAME, TOTAL_ROBOTS, TOTAL_ZONES


def main() -> None:
    print(f"project: {PROJECT_NAME}")
    print(f"model: {LLM_MODEL}")
    print(f"robots: {TOTAL_ROBOTS}")
    print(f"zones: {TOTAL_ZONES}")


if __name__ == "__main__":
    main()
