import os

from langchain_openai import ChatOpenAI


class LLM:
    def __init__(self):
        self.api_key = os.getenv("SILICONCLOUD_API_KEY")
        self.base_url = "https://api.siliconflow.cn/v1"

    def get(self):
        return ChatOpenAI(
            model="Qwen/Qwen3-235B-A22B",
            api_key=self.api_key,
            base_url=self.base_url,
            streaming=True,
            stream_usage=True,
            temperature=0,
            max_tokens=8000,
            extra_body={
                "enable_thinking": True,
                "thinking_budget": 4096
            },
        )


llm = LLM().get()
