from .base import StyleAndTextTuples
from _typeshed import Incomplete
from pygments.token import Token

__all__ = ['PygmentsTokens']

class PygmentsTokens:
    """
    Turn a pygments token list into a list of prompt_toolkit text fragments
    (``(style_str, text)`` tuples).
    """
    token_list: Incomplete
    def __init__(self, token_list: list[tuple[Token, str]]) -> None: ...
    def __pt_formatted_text__(self) -> StyleAndTextTuples: ...
