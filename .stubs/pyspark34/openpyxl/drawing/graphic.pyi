from .effect import EffectContainer as EffectContainer, EffectList as EffectList
from .fill import Blip as Blip, BlipFillProperties as BlipFillProperties, GradientFillProperties as GradientFillProperties
from .picture import PictureFrame as PictureFrame
from .properties import GroupShapeProperties as GroupShapeProperties, NonVisualDrawingProps as NonVisualDrawingProps, NonVisualGroupShape as NonVisualGroupShape
from .relation import ChartRelation as ChartRelation
from .xdr import XDRTransform2D as XDRTransform2D
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, String as String, Typed as Typed
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import CHART_NS as CHART_NS, DRAWING_NS as DRAWING_NS

class GraphicFrameLocking(Serialisable):
    noGrp: Incomplete
    noDrilldown: Incomplete
    noSelect: Incomplete
    noChangeAspect: Incomplete
    noMove: Incomplete
    noResize: Incomplete
    extLst: Incomplete
    def __init__(self, noGrp: Incomplete | None = None, noDrilldown: Incomplete | None = None, noSelect: Incomplete | None = None, noChangeAspect: Incomplete | None = None, noMove: Incomplete | None = None, noResize: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class NonVisualGraphicFrameProperties(Serialisable):
    tagname: str
    graphicFrameLocks: Incomplete
    extLst: Incomplete
    def __init__(self, graphicFrameLocks: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class NonVisualGraphicFrame(Serialisable):
    tagname: str
    cNvPr: Incomplete
    cNvGraphicFramePr: Incomplete
    __elements__: Incomplete
    def __init__(self, cNvPr: Incomplete | None = None, cNvGraphicFramePr: Incomplete | None = None) -> None: ...

class GraphicData(Serialisable):
    tagname: str
    namespace = DRAWING_NS
    uri: Incomplete
    chart: Incomplete
    def __init__(self, uri=..., chart: Incomplete | None = None) -> None: ...

class GraphicObject(Serialisable):
    tagname: str
    namespace = DRAWING_NS
    graphicData: Incomplete
    def __init__(self, graphicData: Incomplete | None = None) -> None: ...

class GraphicFrame(Serialisable):
    tagname: str
    nvGraphicFramePr: Incomplete
    xfrm: Incomplete
    graphic: Incomplete
    macro: Incomplete
    fPublished: Incomplete
    __elements__: Incomplete
    def __init__(self, nvGraphicFramePr: Incomplete | None = None, xfrm: Incomplete | None = None, graphic: Incomplete | None = None, macro: Incomplete | None = None, fPublished: Incomplete | None = None) -> None: ...

class GroupShape(Serialisable):
    nvGrpSpPr: Incomplete
    nonVisualProperties: Incomplete
    grpSpPr: Incomplete
    visualProperties: Incomplete
    pic: Incomplete
    __elements__: Incomplete
    def __init__(self, nvGrpSpPr: Incomplete | None = None, grpSpPr: Incomplete | None = None, pic: Incomplete | None = None) -> None: ...
