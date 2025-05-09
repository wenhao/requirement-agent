from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

examples = [
    HumanMessage(
        content="用户的任务"
    ),
    AIMessage(
        content='',
        tool_calls=[
            {'name': 'ask_followup_question', 'args': {'question': '在此处输入你的问题', 'options': ['选项 1', '选项 2', '选项 3']}, 'id': 'call_c49',
             'type': 'tool_call'}
        ],
    ),
    ToolMessage('5334742b5b73c49', tool_call_id='call_c49'),
    AIMessage(
        content='',
        tool_calls=[
            {'name': 'attempt_completion', 'args': {'result': '任务的结果'}, 'id': 'call_f38', 'type': 'tool_call'}
        ],
    ),
    ToolMessage('16505054784', tool_call_id='call_f38'),
]
