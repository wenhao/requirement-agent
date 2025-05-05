from langgraph.prebuilt import create_react_agent

from requirement_agent.ai.llms.model import LLM
from requirement_agent.ai.prompts.system import SYSTEM_PROMPT

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class RequirementGenerateAgent:
    def __init__(self):
        self.agent = create_react_agent(
            model=LLM().get(),
            tools=[],
            prompt=SYSTEM_PROMPT,
            name="requirement_generate_agent",
        )

    def requirement_generate(state: State):
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=SYSTEM_PROMPT),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        chain = prompt | llm
        messages = chain.invoke(state["messages"])
        return {"messages": [messages]}

    def create(self):
        return self.agent
