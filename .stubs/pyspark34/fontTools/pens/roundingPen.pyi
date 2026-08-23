from _typeshed import Incomplete
from fontTools.pens.filterPen import FilterPen, FilterPointPen

__all__ = ['RoundingPen', 'RoundingPointPen']

class RoundingPen(FilterPen):
    '''
    Filter pen that rounds point coordinates and component XY offsets to integer. For
    rounding the component transform values, a separate round function can be passed to
    the pen.

    >>> from fontTools.pens.recordingPen import RecordingPen
    >>> recpen = RecordingPen()
    >>> roundpen = RoundingPen(recpen)
    >>> roundpen.moveTo((0.4, 0.6))
    >>> roundpen.lineTo((1.6, 2.5))
    >>> roundpen.qCurveTo((2.4, 4.6), (3.3, 5.7), (4.9, 6.1))
    >>> roundpen.curveTo((6.4, 8.6), (7.3, 9.7), (8.9, 10.1))
    >>> roundpen.addComponent("a", (1.5, 0, 0, 1.5, 10.5, -10.5))
    >>> recpen.value == [
    ...     (\'moveTo\', ((0, 1),)),
    ...     (\'lineTo\', ((2, 3),)),
    ...     (\'qCurveTo\', ((2, 5), (3, 6), (5, 6))),
    ...     (\'curveTo\', ((6, 9), (7, 10), (9, 10))),
    ...     (\'addComponent\', (\'a\', (1.5, 0, 0, 1.5, 11, -10))),
    ... ]
    True
    '''
    roundFunc: Incomplete
    transformRoundFunc: Incomplete
    def __init__(self, outPen, roundFunc=..., transformRoundFunc=...) -> None: ...
    def moveTo(self, pt) -> None: ...
    def lineTo(self, pt) -> None: ...
    def curveTo(self, *points) -> None: ...
    def qCurveTo(self, *points) -> None: ...
    def addComponent(self, glyphName, transformation) -> None: ...

class RoundingPointPen(FilterPointPen):
    '''
    Filter point pen that rounds point coordinates and component XY offsets to integer.
    For rounding the component scale values, a separate round function can be passed to
    the pen.

    >>> from fontTools.pens.recordingPen import RecordingPointPen
    >>> recpen = RecordingPointPen()
    >>> roundpen = RoundingPointPen(recpen)
    >>> roundpen.beginPath()
    >>> roundpen.addPoint((0.4, 0.6), \'line\')
    >>> roundpen.addPoint((1.6, 2.5), \'line\')
    >>> roundpen.addPoint((2.4, 4.6))
    >>> roundpen.addPoint((3.3, 5.7))
    >>> roundpen.addPoint((4.9, 6.1), \'qcurve\')
    >>> roundpen.endPath()
    >>> roundpen.addComponent("a", (1.5, 0, 0, 1.5, 10.5, -10.5))
    >>> recpen.value == [
    ...     (\'beginPath\', (), {}),
    ...     (\'addPoint\', ((0, 1), \'line\', False, None), {}),
    ...     (\'addPoint\', ((2, 3), \'line\', False, None), {}),
    ...     (\'addPoint\', ((2, 5), None, False, None), {}),
    ...     (\'addPoint\', ((3, 6), None, False, None), {}),
    ...     (\'addPoint\', ((5, 6), \'qcurve\', False, None), {}),
    ...     (\'endPath\', (), {}),
    ...     (\'addComponent\', (\'a\', (1.5, 0, 0, 1.5, 11, -10)), {}),
    ... ]
    True
    '''
    roundFunc: Incomplete
    transformRoundFunc: Incomplete
    def __init__(self, outPen, roundFunc=..., transformRoundFunc=...) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addComponent(self, baseGlyphName, transformation, identifier: Incomplete | None = None, **kwargs) -> None: ...
