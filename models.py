"""
Shared data models for future global plan generator work.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class GlobalPlanRequest:
    user_command: str = ""
    robot_positions: dict[int, int] = field(default_factory=dict)
    cube_positions: dict[str, int] = field(default_factory=dict)
    goal_positions: dict[str, int] = field(default_factory=dict)


@dataclass
class GlobalPlanOutput:
    robot_plans: list[dict[str, Any]] = field(default_factory=list)
    unassigned_cubes: list[str] = field(default_factory=list)
    reasoning: str = ""
