from .connector import Shape as Shape
from .fill import Blip as Blip
from .geometry import PresetGeometry2D as PresetGeometry2D
from .graphic import GraphicFrame as GraphicFrame, GroupShape as GroupShape
from .picture import PictureFrame as PictureFrame
from .relation import ChartRelation as ChartRelation
from .xdr import XDRPoint2D as XDRPoint2D, XDRPositiveSize2D as XDRPositiveSize2D
from _typeshed import Incomplete
from openpyxl.chart._chart import ChartBase as ChartBase
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, NoneSet as NoneSet, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import Relation as Relation
from openpyxl.descriptors.nested import NestedNoneSet as NestedNoneSet, NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.drawing.image import Image as Image
from openpyxl.packaging.relationship import Relationship as Relationship, RelationshipList as RelationshipList
from openpyxl.utils import coordinate_to_tuple as coordinate_to_tuple
from openpyxl.utils.units import cm_to_EMU as cm_to_EMU, pixels_to_EMU as pixels_to_EMU
from openpyxl.xml.constants import SHEET_DRAWING_NS as SHEET_DRAWING_NS

class AnchorClientData(Serialisable):
    fLocksWithSheet: Incomplete
    fPrintsWithSheet: Incomplete
    def __init__(self, fLocksWithSheet: Incomplete | None = None, fPrintsWithSheet: Incomplete | None = None) -> None: ...

class AnchorMarker(Serialisable):
    tagname: str
    col: Incomplete
    colOff: Incomplete
    row: Incomplete
    rowOff: Incomplete
    def __init__(self, col: int = 0, colOff: int = 0, row: int = 0, rowOff: int = 0) -> None: ...

class _AnchorBase(Serialisable):
    sp: Incomplete
    shape: Incomplete
    grpSp: Incomplete
    groupShape: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    connectionShape: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, clientData: Incomplete | None = None, sp: Incomplete | None = None, grpSp: Incomplete | None = None, graphicFrame: Incomplete | None = None, cxnSp: Incomplete | None = None, pic: Incomplete | None = None, contentPart: Incomplete | None = None) -> None: ...

class AbsoluteAnchor(_AnchorBase):
    tagname: str
    pos: Incomplete
    ext: Incomplete
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, pos: Incomplete | None = None, ext: Incomplete | None = None, **kw) -> None: ...

class OneCellAnchor(_AnchorBase):
    tagname: str
    ext: Incomplete
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, _from: Incomplete | None = None, ext: Incomplete | None = None, **kw) -> None: ...

class TwoCellAnchor(_AnchorBase):
    tagname: str
    editAs: Incomplete
    to: Incomplete
    sp: Incomplete
    grpSp: Incomplete
    graphicFrame: Incomplete
    cxnSp: Incomplete
    pic: Incomplete
    contentPart: Incomplete
    clientData: Incomplete
    __elements__: Incomplete
    def __init__(self, editAs: Incomplete | None = None, _from: Incomplete | None = None, to: Incomplete | None = None, **kw) -> None: ...

class SpreadsheetDrawing(Serialisable):
    tagname: str
    mime_type: str
    PartName: str
    twoCellAnchor: Incomplete
    oneCellAnchor: Incomplete
    absoluteAnchor: Incomplete
    __elements__: Incomplete
    charts: Incomplete
    images: Incomplete
    def __init__(self, twoCellAnchor=(), oneCellAnchor=(), absoluteAnchor=()) -> None: ...
    def __hash__(self):
        """
        Just need to check for identity
        """
    def __bool__(self) -> bool: ...
    @property
    def path(self): ...
