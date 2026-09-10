from . import Extension as Extension
from ..blockprocessors import BlockProcessor as BlockProcessor
from _typeshed import Incomplete

PIPE_NONE: int
PIPE_LEFT: int
PIPE_RIGHT: int

class TableProcessor(BlockProcessor):
    """ Process Tables. """
    RE_CODE_PIPES: Incomplete
    RE_END_BORDER: Incomplete
    border: bool
    separator: str
    config: Incomplete
    def __init__(self, parser, config) -> None: ...
    def test(self, parent, block):
        """
        Ensure first two rows (column header and separator row) are valid table rows.

        Keep border check and separator row do avoid repeating the work.
        """
    def run(self, parent, blocks) -> None:
        """ Parse a table block and build table. """

class TableExtension(Extension):
    """ Add tables to Markdown. """
    config: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def extendMarkdown(self, md) -> None:
        """ Add an instance of `TableProcessor` to `BlockParser`. """

def makeExtension(**kwargs): ...
