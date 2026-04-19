from __future__ import annotations

from models import GlobalPlanRequest
from config import ADJACENT_ZONES, TOTAL_ROBOTS


def _format_robot_state(request: GlobalPlanRequest) -> str:
    '''
    로봇 상태를 프롬프트용 문자열로 포맷팅하는 함수입니다.
    '''
    lines = []
    for robot_id in range(1, TOTAL_ROBOTS + 1):
        reachable_zones = ADJACENT_ZONES.get(robot_id, [])
        lines.append(
            f"R{robot_id}: reachable_zones={reachable_zones}"
        )
    return "\n".join(lines)


def _format_cube_state(request: GlobalPlanRequest) -> str:
    '''
    큐브 상태를 프롬프트용 문자열로 포맷팅하는 함수입니다.
    '''
    lines = []
    for cube_id, current_zone in sorted(request.cube_positions.items()):
        goal_zone = request.goal_positions.get(cube_id, "unknown")
        lines.append(f"{cube_id}: current_zone={current_zone}, goal_zone={goal_zone}")
    return "\n".join(lines)


def _output_schema_text() -> str:
    '''
    LLM이 따라야 할 출력 JSON 스키마를 문자열로 반환하는 함수입니다.
    '''
    return """{
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
    }
  ],
  "reasoning": "brief explanation"
}"""


def build_global_plan_prompt(request: GlobalPlanRequest) -> str:
    '''
    robot 상태, 큐브 상태, 출력 스키마를 전부 합쳐 최종 프롬프트를 생성하는 함수입니다.
        - LLM의 역할 : global planner 
        - 환경 설명 : 9개 로봇, reachable zone 제약
        - 규칙 : cube 중복 할당 금지, reachability 위반 금지
        - 출력 형식 : JSON only
    '''
    cube_state = _format_cube_state(request)
    output_schema = _output_schema_text()

    return f"""You are a global planner for a 9-robot OMX cube manipulation system.

## Goal
Generate a robot-wise global plan for moving all cubes to their goal zones.

## Environment
- There are 9 robots: R1 ~ R9.
- Each robot can only manipulate cubes in its reachable zones.
- The output will later be mapped into a predefined identical BT.
- Do not generate low-level trajectories or joint commands.

## Collision-Free Planning Rules
1. The same cube must not be assigned to multiple robots.
2. A robot must only be assigned tasks in zones it can reach.
3. The plan should avoid conflicting assignments across robots.

## Cube State
{cube_state}

## User Command
{request.user_command}

## Output Rules
- Output JSON only.
- Do not include markdown fences.
- Do not include any explanation outside JSON.
- Every cube in the environment should be included in the plan.
- Use this exact schema:

{output_schema}

## Task Format
Each task must contain:
- cube_id
- from_zone
- to_zone
"""