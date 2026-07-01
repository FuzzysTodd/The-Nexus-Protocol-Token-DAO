from .data_source import StrRef as StrRef
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.drawing.text import ListStyle as ListStyle, Paragraph as Paragraph, RichTextProperties as RichTextProperties

class RichText(Serialisable):
    """
    From the specification: 21.2.2.216

    This element specifies text formatting. The lstStyle element is not supported.
    """
    tagname: str
    bodyPr: Incomplete
    properties: Incomplete
    lstStyle: Incomplete
    p: Incomplete
    paragraphs: Incomplete
    __elements__: Incomplete
    def __init__(self, bodyPr: Incomplete | None = None, lstStyle: Incomplete | None = None, p: Incomplete | None = None) -> None: ...

class Text(Serialisable):
    """
    The value can be either a cell reference or a text element
    If both are present then the reference will be used.
    """
    tagname: str
    strRef: Incomplete
    rich: Incomplete
    __elements__: Incomplete
    def __init__(self, strRef: Incomplete | None = None, rich: Incomplete | None = None) -> None: ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...
