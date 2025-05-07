from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from requirement_agent.ai.agents.requirement_generator.tools import ask_followup_question, attempt_completion
from requirement_agent.ai.llms.model import llm
from requirement_agent.ai.prompts.system import SYSTEM_PROMPT
from requirement_agent.ai.state.requirement_agent_state import RequirementAgentState


def requirement_generate(state: RequirementAgentState):
    llm_with_tools = llm.bind_tools([ask_followup_question, attempt_completion])
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    chain = prompt | llm_with_tools
    messages = chain.invoke(state["messages"])
    return {"messages": [messages]}
