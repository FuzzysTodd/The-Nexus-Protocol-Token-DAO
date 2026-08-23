from _typeshed import Incomplete
from openpyxl.cell.text import InlineFont as InlineFont, Text as Text
from openpyxl.descriptors import Strict as Strict, String as String, Typed as Typed

class TextBlock(Strict):
    """ Represents text string in a specific format

    This class is used as part of constructing a rich text strings.
    """
    font: Incomplete
    text: Incomplete
    def __init__(self, font, text) -> None: ...
    def __eq__(self, other): ...

class CellRichText(list):
    """Represents a rich text string.

    Initialize with a list made of pure strings or :class:`TextBlock` elements
    Can index object to access or modify individual rich text elements
    it also supports the + and += operators between rich text strings
    There are no user methods for this class

    operations which modify the string will generally call an optimization pass afterwards,
    that merges text blocks with identical formats, consecutive pure text strings,
    and remove empty strings and empty text blocks
    """
    def __init__(self, *args) -> None: ...
    @classmethod
    def from_tree(cls, node): ...
    def __iadd__(self, arg): ...
    def __add__(self, arg): ...
    def __setitem__(self, indx, val) -> None: ...
    def append(self, arg) -> None: ...
    def extend(self, arg) -> None: ...
    def as_list(self):
        """
        Returns a list of the strings contained.
        The main reason for this is to make editing easier.
        """
