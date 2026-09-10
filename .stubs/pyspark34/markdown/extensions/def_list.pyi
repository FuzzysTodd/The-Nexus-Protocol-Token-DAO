from . import Extension as Extension
from ..blockprocessors import BlockProcessor as BlockProcessor, ListIndentProcessor as ListIndentProcessor
from _typeshed import Incomplete

class DefListProcessor(BlockProcessor):
    """ Process Definition Lists. """
    RE: Incomplete
    NO_INDENT_RE: Incomplete
    def test(self, parent, block): ...
    def run(self, parent, blocks): ...

class DefListIndentProcessor(ListIndentProcessor):
    """ Process indented children of definition list items. """
    ITEM_TYPES: Incomplete
    LIST_TYPES: Incomplete
    def create_item(self, parent, block) -> None:
        """ Create a new `dd` or `li` (depending on parent) and parse the block with it as the parent. """

class DefListExtension(Extension):
    """ Add definition lists to Markdown. """
    def extendMarkdown(self, md) -> None:
        """ Add an instance of `DefListProcessor` to `BlockParser`. """

def makeExtension(**kwargs): ...
