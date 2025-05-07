from typing_extensions import Annotated, TypedDict

class review(TypedDict):
    """
    向用户提供产品需求文档内容评审建议。当你遇到产品需求文档内容需要被优化时应使用此工具。
    """

    options: Annotated[list, ..., "（必需）一个包含 2-5 个评审建议选项的数组供用户选择。每个选项都应该是一个描述可能答案的字符串。评审建议尽可能的客观真实具体。"]