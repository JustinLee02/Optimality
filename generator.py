from __future__ import annotations

from openai import OpenAI

from config import LLM_MODEL, OPENAI_API_KEY


class GlobalPlanGenerator:
    def __init__(self, api_key: str | None = None, model: str = LLM_MODEL):
        '''
        .env 파일 생성 후 OPENAI_API_KEY=your_api_key 형식으로 키를 입력해주세요.
        '''
        self.api_key = api_key or OPENAI_API_KEY
        self.model = model

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set.")

        self.client = OpenAI(api_key=self.api_key)

    def generate_raw(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.0,
        )

        content = response.choices[0].message.content
        if content is None:
            raise ValueError("LLM returned empty content.")

        return content.strip()
