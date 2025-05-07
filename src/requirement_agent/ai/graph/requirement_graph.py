from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END

from requirement_agent.ai.agents.requirement_generator.agent import requirement_generate
from requirement_agent.ai.agents.requirement_reflector.agent import requirement_reflect
from requirement_agent.ai.graph.condition import should_refection
from requirement_agent.ai.memory.memory import checkpointer
from requirement_agent.ai.state.requirement_agent_state import RequirementAgentState


class RequirementGraph:

    def __init__(self):
        graph_builder = StateGraph(RequirementAgentState)

        graph_builder.add_node("requirement_generator", requirement_generate)
        graph_builder.add_node("requirement_reflector", requirement_reflect)

        graph_builder.add_edge(START, "requirement_generator")
        graph_builder.add_conditional_edges(
            "requirement_generator",
            should_refection,
            {
                "requirement_reflector": "requirement_reflector",
                END: END
            }
        )
        self.graph = graph_builder.compile(checkpointer=checkpointer)

    def stream(self, question, conversation_id: str, stream_mode="values"):
        return self.graph.stream(
            {"messages": HumanMessage(content=question)},
            {"configurable": {"thread_id": conversation_id}},
            stream_mode=stream_mode,
        )
