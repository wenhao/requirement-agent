from typing import Annotated

from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class RequirementAgentState(TypedDict):
    messages: Annotated[list, add_messages]