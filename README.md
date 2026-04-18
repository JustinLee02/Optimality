# Global Plan Generator Shared

구성:
- `config.py`: 공통 환경 설정과 OMX reachability 정의
- `models.py`: request / output 데이터 구조 초안
- `main.py`: 추후 엔트리포인트 자리
- `requirements.txt`: 기본 의존성


시작:

```bash
cd global_plan_generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
