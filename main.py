"""
Entry point placeholder for the shared global plan generator project.
"""

from __future__ import annotations
from models import GlobalPlanRequest
from prompt_template import build_global_plan_prompt

from config import LLM_MODEL, PROJECT_NAME, TOTAL_ROBOTS, TOTAL_ZONES


def main() -> None:
    print(f"project: {PROJECT_NAME}")
    print(f"model: {LLM_MODEL}")
    print(f"robots: {TOTAL_ROBOTS}")
    print(f"zones: {TOTAL_ZONES}")

    request = GlobalPlanRequest(
        user_command="배치된 큐브들을 goal 위치로 옮겨줘",
        robot_positions={
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: 6,
            6: 7,
            7: 9,
            8: 10,
            9: 11,
        },
        cube_positions={
            "C1": 1,
            "C2": 3,
        },
        goal_positions={
            "C1": 2,
            "C2": 4,
        },
    )

    prompt = build_global_plan_prompt(request)
    print(prompt)


if __name__ == "__main__":
    main()
