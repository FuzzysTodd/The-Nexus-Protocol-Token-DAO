from .geometry import Point2D as Point2D, PositiveSize2D as PositiveSize2D, Transform2D as Transform2D
from _typeshed import Incomplete

class XDRPoint2D(Point2D):
    namespace: Incomplete
    x: Incomplete
    y: Incomplete

class XDRPositiveSize2D(PositiveSize2D):
    namespace: Incomplete
    cx: Incomplete
    cy: Incomplete

class XDRTransform2D(Transform2D):
    namespace: Incomplete
    rot: Incomplete
    flipH: Incomplete
    flipV: Incomplete
    off: Incomplete
    ext: Incomplete
    chOff: Incomplete
    chExt: Incomplete
