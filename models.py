"""
Shared data models for global plan generation.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class GlobalPlanRequest:
    """
    Input schema for global plan generation.

    - user_command: natural language instruction from the user
    - cube_positions: current zone for each cube
    - goal_positions: desired goal zone for each cube
    이 부분은 좀 수정이 필요할 수도 있음. 아예 명령 안에 목적지 및 큐브 정보가 포함될 수도 있기 때문. 일단은 명확하게 구분해서 넣어보는 식으로 접근해봄.
    """

    user_command: str = ""
    cube_positions: dict[str, int] = field(default_factory=dict)
    goal_positions: dict[str, int] = field(default_factory=dict)


@dataclass
class PlanTask:
    """
    One task assignment unit that can later be mapped into identical BT arguments.

    For now, the minimum required fields are:
    - cube_id
    - from_zone
    - to_zone
    """

    cube_id: str = ""
    from_zone: int = 0
    to_zone: int = 0


@dataclass
class RobotPlan:
    """
    Ordered task list for one robot.

    tasks[0] means the first task for that robot.
    Later we can interpret task index as stage index if needed.
    """

    robot_id: int = 0
    tasks: list[PlanTask] = field(default_factory=list)


@dataclass
class GlobalPlanOutput:
    """
    Output schema for global plan generation.

    - robot_plans: robot-wise task assignments
    - reasoning: short free-text explanation for debugging or discussion
    """

    robot_plans: list[RobotPlan] = field(default_factory=list)
    reasoning: str = ""

    def to_dict(self) -> dict:
        """Convert nested dataclasses into a plain JSON-serializable dict."""
        return asdict(self)
