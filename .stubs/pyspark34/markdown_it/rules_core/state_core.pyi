from ..ruler import StateBase as StateBase
from ..token import Token as Token
from ..utils import EnvType as EnvType
from _typeshed import Incomplete
from markdown_it import MarkdownIt as MarkdownIt

class StateCore(StateBase):
    src: Incomplete
    md: Incomplete
    env: Incomplete
    tokens: Incomplete
    inlineMode: bool
    def __init__(self, src: str, md: MarkdownIt, env: EnvType, tokens: list[Token] | None = None) -> None: ...
