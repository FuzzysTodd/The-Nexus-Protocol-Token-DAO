from .author import AuthorList as AuthorList
from .comments import Comment as Comment
from .shape_writer import ShapeWriter as ShapeWriter
from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.cell.text import Text as Text
from openpyxl.descriptors import Bool as Bool, Integer as Integer, Set as Set, String as String, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList, Guid as Guid
from openpyxl.descriptors.sequence import NestedSequence as NestedSequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils.indexed_list import IndexedList as IndexedList
from openpyxl.xml.constants import SHEET_MAIN_NS as SHEET_MAIN_NS

class Properties(Serialisable):
    locked: Incomplete
    defaultSize: Incomplete
    disabled: Incomplete
    uiObject: Incomplete
    autoFill: Incomplete
    autoLine: Incomplete
    altText: Incomplete
    textHAlign: Incomplete
    textVAlign: Incomplete
    lockText: Incomplete
    justLastX: Incomplete
    autoScale: Incomplete
    rowHidden: Incomplete
    colHidden: Incomplete
    __elements__: Incomplete
    anchor: Incomplete
    def __init__(self, locked: Incomplete | None = None, defaultSize: Incomplete | None = None, _print: Incomplete | None = None, disabled: Incomplete | None = None, uiObject: Incomplete | None = None, autoFill: Incomplete | None = None, autoLine: Incomplete | None = None, altText: Incomplete | None = None, textHAlign: Incomplete | None = None, textVAlign: Incomplete | None = None, lockText: Incomplete | None = None, justLastX: Incomplete | None = None, autoScale: Incomplete | None = None, rowHidden: Incomplete | None = None, colHidden: Incomplete | None = None, anchor: Incomplete | None = None) -> None: ...

class CommentRecord(Serialisable):
    tagname: str
    ref: Incomplete
    authorId: Incomplete
    guid: Incomplete
    shapeId: Incomplete
    text: Incomplete
    commentPr: Incomplete
    author: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    height: Incomplete
    width: Incomplete
    def __init__(self, ref: str = '', authorId: int = 0, guid: Incomplete | None = None, shapeId: int = 0, text: Incomplete | None = None, commentPr: Incomplete | None = None, author: Incomplete | None = None, height: int = 79, width: int = 144) -> None: ...
    @classmethod
    def from_cell(cls, cell):
        """
        Class method to convert cell comment
        """
    @property
    def content(self):
        """
        Remove all inline formatting and stuff
        """

class CommentSheet(Serialisable):
    tagname: str
    authors: Incomplete
    commentList: Incomplete
    extLst: Incomplete
    mime_type: str
    __elements__: Incomplete
    def __init__(self, authors: Incomplete | None = None, commentList: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
    def to_tree(self): ...
    @property
    def comments(self) -> Generator[Incomplete, None, None]:
        """
        Return a dictionary of comments keyed by coord
        """
    @classmethod
    def from_comments(cls, comments):
        """
        Create a comment sheet from a list of comments for a particular worksheet
        """
    def write_shapes(self, vml: Incomplete | None = None):
        """
        Create the VML for comments
        """
    @property
    def path(self):
        """
        Return path within the archive
        """
