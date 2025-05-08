from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

examples = [
    HumanMessage(
        content="用户的任务"
    ),
    AIMessage(
        content='',
        tool_calls=[
            {'name': 'review', 'args': {'options': ['选项 1', '选项 2', '选项 3']}, 'id': 'call_c49',
             'type': 'tool_call'}
        ],
    ),
    ToolMessage('5334742b5b73c49', tool_call_id='call_c49'),
]
