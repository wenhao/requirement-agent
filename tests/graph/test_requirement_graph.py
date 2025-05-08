import json

import pytest

from requirement_agent.ai.graph.requirement_graph import RequirementGraph
from requirement_agent.shared.utils.logger import LOG


@pytest.fixture
def graph():
    return RequirementGraph()


def test_stream(graph):
    events = graph.stream(
        "招乎文档智能表格目前不能按单元格授予权限，要支持基于角色/用户组的单元格权限，需要设置不同单元格的编辑/查看权限。请按痛点、目标、改进思路、用户价值四个方面描述此需求，结果以表格形式呈现。",
        "test34",
        "values"
    )
    for event in events:
        LOG.info(event)