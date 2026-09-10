from . import util as util
from _typeshed import Incomplete

class State(list):
    """ Track the current and nested state of the parser.

    This utility class is used to track the state of the `BlockParser` and
    support multiple levels if nesting. It's just a simple API wrapped around
    a list. Each time a state is set, that state is appended to the end of the
    list. Each time a state is reset, that state is removed from the end of
    the list.

    Therefore, each time a state is set for a nested block, that state must be
    reset when we back out of that level of nesting or the state could be
    corrupted.

    While all the methods of a list object are available, only the three
    defined below need be used.

    """
    def set(self, state) -> None:
        """ Set a new state. """
    def reset(self) -> None:
        """ Step back one step in nested state. """
    def isstate(self, state):
        """ Test that top (current) level is of given state. """

class BlockParser:
    """ Parse Markdown blocks into an `ElementTree` object.

    A wrapper class that stitches the various `BlockProcessors` together,
    looping through them and creating an `ElementTree` object.
    """
    blockprocessors: Incomplete
    state: Incomplete
    md: Incomplete
    def __init__(self, md) -> None: ...
    root: Incomplete
    def parseDocument(self, lines):
        """ Parse a markdown document into an ElementTree.

        Given a list of lines, an ElementTree object (not just a parent
        Element) is created and the root element is passed to the parser
        as the parent. The ElementTree object is returned.

        This should only be called on an entire document, not pieces.

        """
    def parseChunk(self, parent, text) -> None:
        """ Parse a chunk of markdown text and attach to given `etree` node.

        While the `text` argument is generally assumed to contain multiple
        blocks which will be split on blank lines, it could contain only one
        block. Generally, this method would be called by extensions when
        block parsing is required.

        The `parent` `etree` Element passed in is altered in place.
        Nothing is returned.

        """
    def parseBlocks(self, parent, blocks) -> None:
        """ Process blocks of markdown text and attach to given `etree` node.

        Given a list of `blocks`, each `blockprocessor` is stepped through
        until there are no blocks left. While an extension could potentially
        call this method directly, it's generally expected to be used
        internally.

        This is a public method as an extension may need to add/alter
        additional `BlockProcessors` which call this method to recursively
        parse a nested block.

        """
