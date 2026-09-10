from . import Extension as Extension
from ..blockprocessors import BlockProcessor as BlockProcessor
from _typeshed import Incomplete

class AdmonitionExtension(Extension):
    """ Admonition extension for Python-Markdown. """
    def extendMarkdown(self, md) -> None:
        """ Add Admonition to Markdown instance. """

class AdmonitionProcessor(BlockProcessor):
    CLASSNAME: str
    CLASSNAME_TITLE: str
    RE: Incomplete
    RE_SPACES: Incomplete
    current_sibling: Incomplete
    content_indention: int
    def __init__(self, parser) -> None:
        """Initialization."""
    content_indent: int
    def parse_content(self, parent, block):
        """Get sibling admonition.

        Retrieve the appropriate sibling element. This can get tricky when
        dealing with lists.

        """
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...
    def get_class_and_title(self, match): ...

def makeExtension(**kwargs): ...
