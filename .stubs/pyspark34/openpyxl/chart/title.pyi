from .layout import Layout as Layout
from .shapes import GraphicalProperties as GraphicalProperties
from .text import RichText as RichText, Text as Text
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.drawing.text import CharacterProperties as CharacterProperties, LineBreak as LineBreak, Paragraph as Paragraph, ParagraphProperties as ParagraphProperties, RegularTextRun as RegularTextRun

class Title(Serialisable):
    tagname: str
    tx: Incomplete
    text: Incomplete
    layout: Incomplete
    overlay: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    body: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, tx: Incomplete | None = None, layout: Incomplete | None = None, overlay: Incomplete | None = None, spPr: Incomplete | None = None, txPr: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

def title_maker(text): ...

class TitleDescriptor(Typed):
    expected_type = Title
    allow_none: bool
    def __set__(self, instance, value) -> None: ...
