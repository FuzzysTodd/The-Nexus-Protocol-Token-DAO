from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['BoundsPen', 'ControlBoundsPen']

class ControlBoundsPen(BasePen):
    '''Pen to calculate the "control bounds" of a shape. This is the
    bounding box of all control points, so may be larger than the
    actual bounding box if there are curves that don\'t have points
    on their extremes.

    When the shape has been drawn, the bounds are available as the
    ``bounds`` attribute of the pen object. It\'s a 4-tuple::

            (xMin, yMin, xMax, yMax).

    If ``ignoreSinglePoints`` is True, single points are ignored.
    '''
    ignoreSinglePoints: Incomplete
    def __init__(self, glyphSet, ignoreSinglePoints: bool = False) -> None: ...
    bounds: Incomplete
    def init(self) -> None: ...

class BoundsPen(ControlBoundsPen):
    '''Pen to calculate the bounds of a shape. It calculates the
    correct bounds even when the shape contains curves that don\'t
    have points on their extremes. This is somewhat slower to compute
    than the "control bounds".

    When the shape has been drawn, the bounds are available as the
    ``bounds`` attribute of the pen object. It\'s a 4-tuple::

            (xMin, yMin, xMax, yMax)
    '''
