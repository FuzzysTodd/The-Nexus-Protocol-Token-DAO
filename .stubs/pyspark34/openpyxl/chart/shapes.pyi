from openpyxl.drawing.fill import *
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Typed as Typed
from openpyxl.descriptors.nested import EmptyTag as EmptyTag
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.drawing.colors import ColorChoiceDescriptor as ColorChoiceDescriptor
from openpyxl.drawing.geometry import CustomGeometry2D as CustomGeometry2D, PresetGeometry2D as PresetGeometry2D, Scene3D as Scene3D, Shape3D as Shape3D, Transform2D as Transform2D
from openpyxl.drawing.line import LineProperties as LineProperties

class GraphicalProperties(Serialisable):
    """
    Somewhat vaguely 21.2.2.197 says this:

    This element specifies the formatting for the parent chart element. The
    custGeom, prstGeom, scene3d, and xfrm elements are not supported. The
    bwMode attribute is not supported.

    This doesn't leave much. And the element is used in different places.
    """
    tagname: str
    bwMode: Incomplete
    xfrm: Incomplete
    transform: Incomplete
    custGeom: Incomplete
    prstGeom: Incomplete
    noFill: Incomplete
    solidFill: Incomplete
    gradFill: Incomplete
    pattFill: Incomplete
    ln: Incomplete
    line: Incomplete
    scene3d: Incomplete
    sp3d: Incomplete
    shape3D: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, bwMode: Incomplete | None = None, xfrm: Incomplete | None = None, noFill: Incomplete | None = None, solidFill: Incomplete | None = None, gradFill: Incomplete | None = None, pattFill: Incomplete | None = None, ln: Incomplete | None = None, scene3d: Incomplete | None = None, custGeom: Incomplete | None = None, prstGeom: Incomplete | None = None, sp3d: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
