from __future__ import annotations

import json

from models import GlobalPlanOutput, PlanTask, RobotPlan


def strip_code_fence(raw_text: str) -> str:
    raw = raw_text.strip()

    if raw.startswith("```"):
        parts = raw.split("```")
        if len(parts) >= 2:
            raw = parts[1]
        if raw.startswith("json"):
            raw = raw[4:]

    return raw.strip()


def parse_global_plan_raw_text(raw_text: str) -> GlobalPlanOutput:
    cleaned = strip_code_fence(raw_text)
    data = json.loads(cleaned)

    robot_plans_data = data.get("robot_plans", [])
    reasoning = data.get("reasoning", "")

    robot_plans: list[RobotPlan] = []

    for robot_plan_data in robot_plans_data:
        robot_id = robot_plan_data["robot_id"]
        tasks_data = robot_plan_data.get("tasks", [])

        tasks: list[PlanTask] = []
        for task_data in tasks_data:
            task = PlanTask(
                cube_id=task_data["cube_id"],
                from_zone=task_data["from_zone"],
                to_zone=task_data["to_zone"],
            )
            tasks.append(task)

        robot_plan = RobotPlan(
            robot_id=robot_id,
            tasks=tasks,
        )
        robot_plans.append(robot_plan)

    return GlobalPlanOutput(
        robot_plans=robot_plans,
        reasoning=reasoning,
    )
