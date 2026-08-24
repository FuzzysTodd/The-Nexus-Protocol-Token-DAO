from .block_parser import BlockParser as BlockParser
from .core import BaseRenderer as BaseRenderer, BlockState as BlockState, InlineState as InlineState
from .inline_parser import InlineParser as InlineParser
from .markdown import Markdown as Markdown
from .renderers.html import HTMLRenderer as HTMLRenderer
from .util import escape as escape, escape_url as escape_url, safe_entity as safe_entity, unikey as unikey
from _typeshed import Incomplete

__all__ = ['Markdown', 'HTMLRenderer', 'BlockParser', 'BlockState', 'BaseRenderer', 'InlineParser', 'InlineState', 'escape', 'escape_url', 'safe_entity', 'unikey', 'html', 'create_markdown', 'markdown']

def create_markdown(escape: bool = True, hard_wrap: bool = False, renderer: str = 'html', plugins: Incomplete | None = None) -> Markdown:
    """Create a Markdown instance based on the given condition.

    :param escape: Boolean. If using html renderer, escape html.
    :param hard_wrap: Boolean. Break every new line into ``<br>``.
    :param renderer: renderer instance, default is HTMLRenderer.
    :param plugins: List of plugins.

    This method is used when you want to re-use a Markdown instance::

        markdown = create_markdown(
            escape=False,
            hard_wrap=True,
        )
        # re-use markdown function
        markdown('.... your text ...')
    """

html: Markdown

def markdown(text, escape: bool = True, renderer: str = 'html', plugins: Incomplete | None = None) -> str: ...
