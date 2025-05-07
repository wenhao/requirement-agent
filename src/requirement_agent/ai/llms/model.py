import os

from langchain_openai import ChatOpenAI


class LLM:
    def __init__(self):
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    def get(self):
        return ChatOpenAI(
            model="qwen3-32b",
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