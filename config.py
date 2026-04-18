"""
Base configuration for the shared OMX global plan generator workspace.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "global_plan_generator"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
LLM_MODEL = os.getenv("GLOBAL_PLAN_LLM_MODEL", "gpt-4o")

TOTAL_ROBOTS = 9
TOTAL_ZONES = 16

ADJACENT_ZONES = {
    1: [1, 2, 5, 6],
    2: [2, 3, 6, 7],
    3: [3, 4, 7, 8],
    4: [5, 6, 9, 10],
    5: [6, 7, 10, 11],
    6: [7, 8, 11, 12],
    7: [9, 10, 13, 14],
    8: [10, 11, 14, 15],
    9: [11, 12, 15, 16],
}
