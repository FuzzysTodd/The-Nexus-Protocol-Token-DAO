from . import util as util
from .blockparser import BlockParser as BlockParser
from _typeshed import Incomplete

logger: Incomplete

def build_block_parser(md, **kwargs):
    """ Build the default block parser used by Markdown. """

class BlockProcessor:
    """ Base class for block processors.

    Each subclass will provide the methods below to work with the source and
    tree. Each processor will need to define it's own `test` and `run`
    methods. The `test` method should return True or False, to indicate
    whether the current block should be processed by this processor. If the
    test passes, the parser will call the processors `run` method.

    """
    parser: Incomplete
    tab_length: Incomplete
    def __init__(self, parser) -> None: ...
    def lastChild(self, parent):
        """ Return the last child of an `etree` element. """
    def detab(self, text, length: Incomplete | None = None):
        """ Remove a tab from the front of each line of the given text. """
    def looseDetab(self, text, level: int = 1):
        """ Remove a tab from front of lines but allowing dedented lines. """
    def test(self, parent, block) -> None:
        """ Test for block type. Must be overridden by subclasses.

        As the parser loops through processors, it will call the `test`
        method on each to determine if the given block of text is of that
        type. This method must return a boolean `True` or `False`. The
        actual method of testing is left to the needs of that particular
        block type. It could be as simple as `block.startswith(some_string)`
        or a complex regular expression. As the block type may be different
        depending on the parent of the block (i.e. inside a list), the parent
        `etree` element is also provided and may be used as part of the test.

        Keywords:

        * ``parent``: An `etree` element which will be the parent of the block.
        * ``block``: A block of text from the source which has been split at
            blank lines.
        """
    def run(self, parent, blocks) -> None:
        """ Run processor. Must be overridden by subclasses.

        When the parser determines the appropriate type of a block, the parser
        will call the corresponding processor's ``run`` method. This method
        should parse the individual lines of the block and append them to
        the `etree`.

        Note that both the ``parent`` and ``etree`` keywords are pointers
        to instances of the objects which should be edited in place. Each
        processor must make changes to the existing objects as there is no
        mechanism to return new/different objects to replace them.

        This means that this method should be adding `SubElements` or adding text
        to the parent, and should remove (``pop``) or add (``insert``) items to
        the list of blocks.

        Keywords:

        * ``parent``: An `etree` element which is the parent of the current block.
        * ``blocks``: A list of all remaining blocks of the document.
        """

class ListIndentProcessor(BlockProcessor):
    """ Process children of list items.

    Example:
        * a list item
            process this part

            or this part

    """
    ITEM_TYPES: Incomplete
    LIST_TYPES: Incomplete
    INDENT_RE: Incomplete
    def __init__(self, *args) -> None: ...
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...
    def create_item(self, parent, block) -> None:
        """ Create a new `li` and parse the block with it as the parent. """
    def get_level(self, parent, block):
        """ Get level of indent based on list level. """

class CodeBlockProcessor(BlockProcessor):
    """ Process code blocks. """
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...

class BlockQuoteProcessor(BlockProcessor):
    RE: Incomplete
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...
    def clean(self, line):
        """ Remove ``>`` from beginning of a line. """

class OListProcessor(BlockProcessor):
    """ Process ordered list blocks. """
    TAG: str
    STARTSWITH: str
    LAZY_OL: bool
    SIBLING_TAGS: Incomplete
    RE: Incomplete
    CHILD_RE: Incomplete
    INDENT_RE: Incomplete
    def __init__(self, parser) -> None: ...
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...
    def get_items(self, block):
        """ Break a block into list items. """

class UListProcessor(OListProcessor):
    """ Process unordered list blocks. """
    TAG: str
    RE: Incomplete
    def __init__(self, parser) -> None: ...

class HashHeaderProcessor(BlockProcessor):
    """ Process Hash Headers. """
    RE: Incomplete
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...

class SetextHeaderProcessor(BlockProcessor):
    """ Process Setext-style Headers. """
    RE: Incomplete
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...

class HRProcessor(BlockProcessor):
    """ Process Horizontal Rules. """
    RE: str
    SEARCH_RE: Incomplete
    match: Incomplete
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...

class EmptyBlockProcessor(BlockProcessor):
    """ Process blocks that are empty or start with an empty line. """
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...

class ReferenceProcessor(BlockProcessor):
    """ Process link references. """
    RE: Incomplete
    def test(self, parent, block): ...
    def run(self, parent, blocks): ...

class ParagraphProcessor(BlockProcessor):
    """ Process Paragraph blocks. """
    def test(self, parent, block): ...
    def run(self, parent, blocks) -> None: ...
