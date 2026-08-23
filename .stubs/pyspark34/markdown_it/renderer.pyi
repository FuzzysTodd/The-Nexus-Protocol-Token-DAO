from .common.utils import escapeHtml as escapeHtml, unescapeAll as unescapeAll
from .token import Token as Token
from .utils import EnvType as EnvType, OptionsDict as OptionsDict
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, ClassVar, Protocol

class RendererProtocol(Protocol):
    __output__: ClassVar[str]
    def render(self, tokens: Sequence[Token], options: OptionsDict, env: EnvType) -> Any: ...

class RendererHTML(RendererProtocol):
    """Contains render rules for tokens. Can be updated and extended.

    Example:

    Each rule is called as independent static function with fixed signature:

    ::

        class Renderer:
            def token_type_name(self, tokens, idx, options, env) {
                # ...
                return renderedHTML

    ::

        class CustomRenderer(RendererHTML):
            def strong_open(self, tokens, idx, options, env):
                return '<b>'
            def strong_close(self, tokens, idx, options, env):
                return '</b>'

        md = MarkdownIt(renderer_cls=CustomRenderer)

        result = md.render(...)

    See https://github.com/markdown-it/markdown-it/blob/master/lib/renderer.js
    for more details and examples.
    """
    __output__: str
    rules: Incomplete
    def __init__(self, parser: Any = None) -> None: ...
    def render(self, tokens: Sequence[Token], options: OptionsDict, env: EnvType) -> str:
        """Takes token stream and generates HTML.

        :param tokens: list on block tokens to render
        :param options: params of parser instance
        :param env: additional data from parsed input

        """
    def renderInline(self, tokens: Sequence[Token], options: OptionsDict, env: EnvType) -> str:
        """The same as ``render``, but for single token of `inline` type.

        :param tokens: list on block tokens to render
        :param options: params of parser instance
        :param env: additional data from parsed input (references, for example)
        """
    def renderToken(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str:
        """Default token renderer.

        Can be overridden by custom function

        :param idx: token index to render
        :param options: params of parser instance
        """
    @staticmethod
    def renderAttrs(token: Token) -> str:
        """Render token attributes to string."""
    def renderInlineAsText(self, tokens: Sequence[Token] | None, options: OptionsDict, env: EnvType) -> str:
        """Special kludge for image `alt` attributes to conform CommonMark spec.

        Don't try to use it! Spec requires to show `alt` content with stripped markup,
        instead of simple escaping.

        :param tokens: list on block tokens to render
        :param options: params of parser instance
        :param env: additional data from parsed input
        """
    def code_inline(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def code_block(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def fence(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def image(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def hardbreak(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def softbreak(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def text(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def html_block(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
    def html_inline(self, tokens: Sequence[Token], idx: int, options: OptionsDict, env: EnvType) -> str: ...
