"""
Entry point placeholder for the shared global plan generator project.
"""

from __future__ import annotations
from models import GlobalPlanRequest
from prompt_template import build_global_plan_prompt
from generator import GlobalPlanGenerator
from parser import parse_global_plan_raw_text

from config import LLM_MODEL, PROJECT_NAME, TOTAL_ROBOTS, TOTAL_ZONES


def main() -> None:
    print(f"project: {PROJECT_NAME}")
    print(f"model: {LLM_MODEL}")
    print(f"robots: {TOTAL_ROBOTS}")
    print(f"zones: {TOTAL_ZONES}")

    raw_text = """
    {
      "robot_plans": [
        {
          "robot_id": 1,
          "tasks": [
            {
              "cube_id": "C1",
              "from_zone": 1,
              "to_zone": 2
            }
          ]
        },
        {
          "robot_id": 3,
          "tasks": [
            {
              "cube_id": "C2",
              "from_zone": 3,
              "to_zone": 4
            }
          ]
        }
      ],
      "reasoning": "test output"
    }
    """

    parsed = parse_global_plan_raw_text(raw_text)

    print(parsed)
    print(parsed.to_dict())



if __name__ == "__main__":
    main()
