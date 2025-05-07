from langgraph.graph import END

from requirement_agent.ai.state.requirement_agent_state import RequirementAgentState


def should_refection(state: RequirementAgentState):
    message = state["messages"][-1]
    if hasattr(message, "tool_calls") and len(message.tool_calls) > 0:
        tool_call = message.tool_calls[-1]
        if tool_call.get("name") == "attempt_completion":
            return "requirement_reflector"
    return END
