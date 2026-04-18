# Global Plan Generator Shared

구성:
- `config.py`: 공통 환경 설정과 OMX reachability 정의
- `models.py`: request / output 데이터 구조 정의
- `main.py`: 추후 엔트리포인트 자리
- `requirements.txt`: 기본 의존성

입력:
```python
GlobalPlanRequest(
    user_command="큐브들을 goal 위치로 옮겨줘",
    robot_positions={1: 1, 2: 2, 3: 3},
    cube_positions={"C1": 1, "C2": 3},
    goal_positions={"C1": 2, "C2": 4},
)
```

출력:
```json
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
  "unassigned_cubes": [],
  "reasoning": "brief explanation"
}
```

필드 의미:
- `PlanTask`: identical BT에 매핑될 최소 작업 단위
- `RobotPlan`: 한 로봇이 맡은 작업 목록
- `GlobalPlanOutput`: 전체 robot-wise global plan


시작:

```bash
cd global_plan_generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
