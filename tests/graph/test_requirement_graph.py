import pytest

from requirement_agent.ai.graph.requirement_graph import RequirementGraph
from requirement_agent.shared.log import LOG


@pytest.fixture
def graph():
    return RequirementGraph()


def test_stream(graph):
    events = graph.stream("招乎文档智能表格目前不能按单元格授予权限，需要支持按单元格授权才能满足用户需求。请按痛点、目标、改进思路、用户价值四个方面描述此需求，结果以表格形式呈现。", "test")
    latest_answer = events[-1]["messages"][-1]["content"]
    LOG.info(latest_answer)
    assert latest_answer is not None
