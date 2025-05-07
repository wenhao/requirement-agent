from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from requirement_agent.ai.agents.requirement_reflector.tools import review
from requirement_agent.ai.llms.model import llm
from requirement_agent.ai.prompts.reflect_system import REFLECT_SYSTEM_PROMPT
from requirement_agent.ai.state.requirement_agent_state import RequirementAgentState


def requirement_reflect(state: RequirementAgentState):
    llm_with_tools = llm.bind_tools([review])
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=REFLECT_SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    reflect_chain = prompt | llm_with_tools
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    translated = [state["messages"][0]] + [
        cls_map[msg.type](content=msg.content) for msg in state["messages"][1:]
    ]
    message = reflect_chain.invoke(translated)
    return {"messages": [message]}
