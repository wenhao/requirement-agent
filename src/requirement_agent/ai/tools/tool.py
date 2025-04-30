from typing import Annotated, List

from langchain_core.tools import tool


@tool
def ask_followup_question(
        question: Annotated[str, "（必填）要问用户的问题。这应该是一个清晰、具体的问题，针对你所需的信息。"],
        options: Annotated[List[str], "（可选）供用户选择的2到5个选项数组。每个选项应是描述可能答案的字符串。并非总是需要提供选项，但在许多情况下可能会有所帮助，因为它可以节省用户手动输入回答的时间。重要提示：切勿包括切换到Act模式的选项，因为这是你需要指导用户手动操作的内容（如果需要）。"]
):
    """向用户提问以收集完成任务所需的更多信息。当遇到歧义、需要澄清或需要更多细节以有效进行时，应使用此工具。它通过与用户的直接沟通实现互动式问题解决。明智地使用此工具，以在获取必要信息和避免过多来回之间保持平衡。"""
    print(question)
    print(options)
    return ""
