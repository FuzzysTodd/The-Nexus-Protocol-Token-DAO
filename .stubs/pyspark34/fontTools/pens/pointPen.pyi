from _typeshed import Incomplete
from fontTools.misc.loggingTools import LogMixin
from fontTools.misc.transform import DecomposedTransform
from fontTools.pens.basePen import AbstractPen, MissingComponentError
from typing import Any, Dict, Tuple

__all__ = ['AbstractPointPen', 'BasePointToSegmentPen', 'PointToSegmentPen', 'SegmentToPointPen', 'GuessSmoothPointPen', 'ReverseContourPointPen']

class AbstractPointPen:
    """Baseclass for all PointPens."""
    def beginPath(self, identifier: str | None = None, **kwargs: Any) -> None:
        """Start a new sub path."""
    def endPath(self) -> None:
        """End the current sub path."""
    def addPoint(self, pt: Tuple[float, float], segmentType: str | None = None, smooth: bool = False, name: str | None = None, identifier: str | None = None, **kwargs: Any) -> None:
        """Add a point to the current sub path."""
    def addComponent(self, baseGlyphName: str, transformation: Tuple[float, float, float, float, float, float], identifier: str | None = None, **kwargs: Any) -> None:
        """Add a sub glyph."""
    def addVarComponent(self, glyphName: str, transformation: DecomposedTransform, location: Dict[str, float], identifier: str | None = None, **kwargs: Any) -> None:
        """Add a VarComponent sub glyph. The 'transformation' argument
        must be a DecomposedTransform from the fontTools.misc.transform module,
        and the 'location' argument must be a dictionary mapping axis tags
        to their locations.
        """

class BasePointToSegmentPen(AbstractPointPen):
    """
    Base class for retrieving the outline in a segment-oriented
    way. The PointPen protocol is simple yet also a little tricky,
    so when you need an outline presented as segments but you have
    as points, do use this base implementation as it properly takes
    care of all the edge cases.
    """
    currentPath: Incomplete
    def __init__(self) -> None: ...
    def beginPath(self, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def endPath(self) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, identifier: Incomplete | None = None, **kwargs) -> None: ...

class PointToSegmentPen(BasePointToSegmentPen):
    """
    Adapter class that converts the PointPen protocol to the
    (Segment)Pen protocol.

    NOTE: The segment pen does not support and will drop point names, identifiers
    and kwargs.
    """
    pen: Incomplete
    outputImpliedClosingLine: Incomplete
    def __init__(self, segmentPen, outputImpliedClosingLine: bool = False) -> None: ...
    def addComponent(self, glyphName, transform, identifier: Incomplete | None = None, **kwargs) -> None: ...

class SegmentToPointPen(AbstractPen):
    """
    Adapter class that converts the (Segment)Pen protocol to the
    PointPen protocol.
    """
    pen: Incomplete
    contour: Incomplete
    def __init__(self, pointPen, guessSmooth: bool = True) -> None: ...
    def moveTo(self, pt) -> None: ...
    def lineTo(self, pt) -> None: ...
    def curveTo(self, *pts) -> None: ...
    def qCurveTo(self, *pts) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def addComponent(self, glyphName, transform) -> None: ...

class GuessSmoothPointPen(AbstractPointPen):
    '''
    Filtering PointPen that tries to determine whether an on-curve point
    should be "smooth", ie. that it\'s a "tangent" point or a "curve" point.
    '''
    def __init__(self, outPen, error: float = 0.05) -> None: ...
    def beginPath(self, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def endPath(self) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addComponent(self, glyphName, transformation, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addVarComponent(self, glyphName, transformation, location, identifier: Incomplete | None = None, **kwargs) -> None: ...

class ReverseContourPointPen(AbstractPointPen):
    """
    This is a PointPen that passes outline data to another PointPen, but
    reversing the winding direction of all contours. Components are simply
    passed through unchanged.

    Closed contours are reversed in such a way that the first point remains
    the first point.
    """
    pen: Incomplete
    currentContour: Incomplete
    def __init__(self, outputPointPen) -> None: ...
    currentContourIdentifier: Incomplete
    onCurve: Incomplete
    def beginPath(self, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def endPath(self) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: bool = False, name: Incomplete | None = None, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addComponent(self, glyphName, transform, identifier: Incomplete | None = None, **kwargs) -> None: ...

class DecomposingPointPen(LogMixin, AbstractPointPen):
    """Implements a 'addComponent' method that decomposes components
    (i.e. draws them onto self as simple contours).
    It can also be used as a mixin class (e.g. see DecomposingRecordingPointPen).

    You must override beginPath, addPoint, endPath. You may
    additionally override addVarComponent and addComponent.

    By default a warning message is logged when a base glyph is missing;
    set the class variable ``skipMissingComponents`` to False if you want
    all instances of a sub-class to raise a :class:`MissingComponentError`
    exception by default.
    """
    skipMissingComponents: bool
    MissingComponentError = MissingComponentError
    glyphSet: Incomplete
    reverseFlipped: Incomplete
    def __init__(self, glyphSet, *args, skipMissingComponents: Incomplete | None = None, reverseFlipped: bool = False, **kwargs) -> None:
        """Takes a 'glyphSet' argument (dict), in which the glyphs that are referenced
        as components are looked up by their name.

        If the optional 'reverseFlipped' argument is True, components whose transformation
        matrix has a negative determinant will be decomposed with a reversed path direction
        to compensate for the flip.

        The optional 'skipMissingComponents' argument can be set to True/False to
        override the homonymous class attribute for a given pen instance.
        """
    def addComponent(self, baseGlyphName, transformation, identifier: Incomplete | None = None, **kwargs) -> None:
        """Transform the points of the base glyph and draw it onto self.

        The `identifier` parameter and any extra kwargs are ignored.
        """
