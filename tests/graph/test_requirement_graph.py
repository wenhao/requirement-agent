import json

import pytest

from requirement_agent.ai.graph.requirement_graph import RequirementGraph
from requirement_agent.shared.utils.logger import LOG


@pytest.fixture
def graph():
    return RequirementGraph()


def test_stream(graph):
    events = graph.stream(
        "招乎文档智能表格目前不能按单元格授予权限，需要支持按单元格授权才能满足用户需求。请按痛点、目标、改进思路、用户价值四个方面描述此需求，结果以表格形式呈现。",
        "test",
        "values"
    )
    for event in events:
        LOG.info(event)
        # for value in event.values():
        #     for message in value["messages"]:
        #         for tool_call in message.tool_calls:
        #             if tool_call["name"] == "attempt_completion":
        #                 args = tool_call["args"]
        #                 LOG.info(f"result: {args['result']}")
        #             if tool_call["name"] == "ask_followup_question":
        #                 args = tool_call["args"]
        #                 LOG.info(f"question: {args['question']}")
        #                 LOG.info(f"options: {args['options']}")