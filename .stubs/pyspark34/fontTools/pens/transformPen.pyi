from _typeshed import Incomplete
from fontTools.pens.filterPen import FilterPen, FilterPointPen

__all__ = ['TransformPen', 'TransformPointPen']

class TransformPen(FilterPen):
    """Pen that transforms all coordinates using a Affine transformation,
    and passes them to another pen.
    """
    def __init__(self, outPen, transformation) -> None:
        """The 'outPen' argument is another pen object. It will receive the
        transformed coordinates. The 'transformation' argument can either
        be a six-tuple, or a fontTools.misc.transform.Transform object.
        """
    def moveTo(self, pt) -> None: ...
    def lineTo(self, pt) -> None: ...
    def curveTo(self, *points) -> None: ...
    def qCurveTo(self, *points) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def addComponent(self, glyphName, transformation) -> None: ...

class TransformPointPen(FilterPointPen):
    '''PointPen that transforms all coordinates using a Affine transformation,
    and passes them to another PointPen.

    >>> from fontTools.pens.recordingPen import RecordingPointPen
    >>> rec = RecordingPointPen()
    >>> pen = TransformPointPen(rec, (2, 0, 0, 2, -10, 5))
    >>> v = iter(rec.value)
    >>> pen.beginPath(identifier="contour-0")
    >>> next(v)
    (\'beginPath\', (), {\'identifier\': \'contour-0\'})
    >>> pen.addPoint((100, 100), "line")
    >>> next(v)
    (\'addPoint\', ((190, 205), \'line\', False, None), {})
    >>> pen.endPath()
    >>> next(v)
    (\'endPath\', (), {})
    >>> pen.addComponent("a", (1, 0, 0, 1, -10, 5), identifier="component-0")
    >>> next(v)
    (\'addComponent\', (\'a\', <Transform [2 0 0 2 -30 15]>), {\'identifier\': \'component-0\'})
    '''
    def __init__(self, outPointPen, transformation) -> None:
        """The 'outPointPen' argument is another point pen object.
        It will receive the transformed coordinates.
        The 'transformation' argument can either be a six-tuple, or a
        fontTools.misc.transform.Transform object.
        """
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, **kwargs) -> None: ...
    def addComponent(self, baseGlyphName, transformation, **kwargs) -> None: ...
