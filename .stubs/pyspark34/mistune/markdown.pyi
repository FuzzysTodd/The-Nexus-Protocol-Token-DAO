from .block_parser import BlockParser as BlockParser
from .core import BlockState as BlockState
from .inline_parser import InlineParser as InlineParser
from _typeshed import Incomplete

class Markdown:
    """Markdown instance to convert markdown text into HTML or other formats.
    Here is an example with the HTMLRenderer::

        from mistune import HTMLRenderer

        md = Markdown(renderer=HTMLRenderer(escape=False))
        md('hello **world**')

    :param renderer: a renderer to convert parsed tokens
    :param block: block level syntax parser
    :param inline: inline level syntax parser
    :param plugins: mistune plugins to use
    """
    renderer: Incomplete
    block: Incomplete
    inline: Incomplete
    before_parse_hooks: Incomplete
    before_render_hooks: Incomplete
    after_render_hooks: Incomplete
    def __init__(self, renderer: Incomplete | None = None, block: BlockParser | None = None, inline: InlineParser | None = None, plugins: Incomplete | None = None) -> None: ...
    def use(self, plugin) -> None: ...
    def render_state(self, state: BlockState): ...
    def parse(self, s: str, state: BlockState | None = None):
        """Parse and convert the given markdown string. If renderer is None,
        the returned **result** will be parsed markdown tokens.

        :param s: markdown string
        :param state: instance of BlockState
        :returns: result, state
        """
    def read(self, filepath, encoding: str = 'utf-8', state: Incomplete | None = None): ...
    def __call__(self, s: str): ...
