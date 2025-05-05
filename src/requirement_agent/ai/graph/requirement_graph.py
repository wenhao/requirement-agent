from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END

from requirement_agent.ai.agents.requirement_agent import RequirementGenerateAgent
from requirement_agent.ai.memory.memory import memory
from requirement_agent.ai.state.requirement_agent_state import RequirementAgentState


class RequirementGraph:

    def __init__(self):
        graph_builder = StateGraph(RequirementAgentState)
        graph_builder.add_node("requirement_generator", RequirementGenerateAgent().create())
        graph_builder.add_edge(START, "requirement_generator")
        graph_builder.add_edge("requirement_generator", END)
        self.graph = graph_builder.compile(checkpointer=memory)

    def stream(self, question, conversation_id: str):
        return self.graph.stream(
            {"messages": HumanMessage(content=question)},
            {"configurable": {"thread_id": conversation_id}},
            stream_mode="values",
        )
