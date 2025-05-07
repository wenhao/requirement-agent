from typing_extensions import Annotated, TypedDict

class ask_followup_question(TypedDict):
    """
    向用户提问以收集完成任务所需的其他信息。当你遇到歧义、需要澄清或需要更多细节才能有效进行时，应使用此工具。它通过启用与用户的直接通信来实现交互式问题解决。明智地使用此工具，以在收集必要信息和避免过多来回沟通之间保持平衡。
    """

    question: Annotated[str, ..., "（必需）要问用户的问题。这应该是一个清晰、具体的问题，旨在解决你需要的信息。"]
    options: Annotated[list, ..., "（可选）一个包含 2-5 个选项的数组供用户选择。每个选项都应该是一个描述可能答案的字符串。你可能不总是需要提供选项，但在许多情况下，它可以帮助用户避免手动输入响应。"]


class attempt_completion(TypedDict):
    """
    向用户呈现任务的结果。当你认为任务已完成，应使用此工具。
    """

    result: Annotated[str, ..., "（必需）任务的结果。以最终且不需要用户进一步输入的方式制定此结果。不要以问题或提供进一步帮助的提议结束你的结果。"]