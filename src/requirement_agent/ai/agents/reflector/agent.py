from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from requirement_agent.ai.agents.reflector.few_shot import examples
from requirement_agent.ai.agents.reflector.tools import review
from requirement_agent.ai.llms.model import llm
from requirement_agent.ai.prompts.reflect_system import REFLECT_SYSTEM_PROMPT
from requirement_agent.ai.state.requirement_agent_state import RequirementAgentState


def requirement_reflect(state: RequirementAgentState):
    llm_with_tools = llm.bind_tools([review])
    few_shot_prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=REFLECT_SYSTEM_PROMPT),
            *examples,
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    reflect_chain = few_shot_prompt | llm_with_tools
    messages = [
        HumanMessage(content=get_result(state))
    ]
    reflect_message = reflect_chain.invoke(messages)
    return {"messages": [reflect_message]}


def get_result(state: RequirementAgentState):
    ai_message = state["messages"][-1]
    tool_call = ai_message.tool_calls[-1]
    return tool_call["args"]["result"]
