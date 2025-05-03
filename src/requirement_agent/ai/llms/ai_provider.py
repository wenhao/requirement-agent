import os

from langchain_core.prompts import SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI


class AIProvider:
    def __init__(self):
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    def get_model_name(self) -> str:
        pass

    def create_messages(self):
        model = ChatOpenAI(
            model=self.get_model_name(),
            api_key=self.api_key,
            base_url=self.base_url,
            temperature=0,
            streaming=True,
        )
        system_template = SystemMessagePromptTemplate.from_template("")
        pass
