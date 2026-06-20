from _typeshed import Incomplete
from fontTools.misc.loggingTools import LogMixin
from fontTools.misc.transform import DecomposedTransform
from typing import Dict, Tuple

__all__ = ['AbstractPen', 'NullPen', 'BasePen', 'PenError', 'decomposeSuperBezierSegment', 'decomposeQuadraticSegment']

class PenError(Exception):
    """Represents an error during penning."""
class OpenContourError(PenError): ...

class AbstractPen:
    def moveTo(self, pt: Tuple[float, float]) -> None:
        """Begin a new sub path, set the current point to 'pt'. You must
        end each sub path with a call to pen.closePath() or pen.endPath().
        """
    def lineTo(self, pt: Tuple[float, float]) -> None:
        """Draw a straight line from the current point to 'pt'."""
    def curveTo(self, *points: Tuple[float, float]) -> None:
        '''Draw a cubic bezier with an arbitrary number of control points.

        The last point specified is on-curve, all others are off-curve
        (control) points. If the number of control points is > 2, the
        segment is split into multiple bezier segments. This works
        like this:

        Let n be the number of control points (which is the number of
        arguments to this call minus 1). If n==2, a plain vanilla cubic
        bezier is drawn. If n==1, we fall back to a quadratic segment and
        if n==0 we draw a straight line. It gets interesting when n>2:
        n-1 PostScript-style cubic segments will be drawn as if it were
        one curve. See decomposeSuperBezierSegment().

        The conversion algorithm used for n>2 is inspired by NURB
        splines, and is conceptually equivalent to the TrueType "implied
        points" principle. See also decomposeQuadraticSegment().
        '''
    def qCurveTo(self, *points: Tuple[float, float]) -> None:
        """Draw a whole string of quadratic curve segments.

        The last point specified is on-curve, all others are off-curve
        points.

        This method implements TrueType-style curves, breaking up curves
        using 'implied points': between each two consequtive off-curve points,
        there is one implied point exactly in the middle between them. See
        also decomposeQuadraticSegment().

        The last argument (normally the on-curve point) may be None.
        This is to support contours that have NO on-curve points (a rarely
        seen feature of TrueType outlines).
        """
    def closePath(self) -> None:
        """Close the current sub path. You must call either pen.closePath()
        or pen.endPath() after each sub path.
        """
    def endPath(self) -> None:
        """End the current sub path, but don't close it. You must call
        either pen.closePath() or pen.endPath() after each sub path.
        """
    def addComponent(self, glyphName: str, transformation: Tuple[float, float, float, float, float, float]) -> None:
        """Add a sub glyph. The 'transformation' argument must be a 6-tuple
        containing an affine transformation, or a Transform object from the
        fontTools.misc.transform module. More precisely: it should be a
        sequence containing 6 numbers.
        """
    def addVarComponent(self, glyphName: str, transformation: DecomposedTransform, location: Dict[str, float]) -> None:
        """Add a VarComponent sub glyph. The 'transformation' argument
        must be a DecomposedTransform from the fontTools.misc.transform module,
        and the 'location' argument must be a dictionary mapping axis tags
        to their locations.
        """

class NullPen(AbstractPen):
    """A pen that does nothing."""
    def moveTo(self, pt) -> None: ...
    def lineTo(self, pt) -> None: ...
    def curveTo(self, *points) -> None: ...
    def qCurveTo(self, *points) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def addComponent(self, glyphName, transformation) -> None: ...
    def addVarComponent(self, glyphName, transformation, location) -> None: ...

class LoggingPen(LogMixin, AbstractPen):
    """A pen with a ``log`` property (see fontTools.misc.loggingTools.LogMixin)"""
class MissingComponentError(KeyError):
    """Indicates a component pointing to a non-existent glyph in the glyphset."""

class DecomposingPen(LoggingPen):
    """Implements a 'addComponent' method that decomposes components
    (i.e. draws them onto self as simple contours).
    It can also be used as a mixin class (e.g. see ContourRecordingPen).

    You must override moveTo, lineTo, curveTo and qCurveTo. You may
    additionally override closePath, endPath and addComponent.

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
    def addComponent(self, glyphName, transformation) -> None:
        """Transform the points of the base glyph and draw it onto self."""
    def addVarComponent(self, glyphName, transformation, location) -> None: ...

class BasePen(DecomposingPen):
    """Base class for drawing pens. You must override _moveTo, _lineTo and
    _curveToOne. You may additionally override _closePath, _endPath,
    addComponent, addVarComponent, and/or _qCurveToOne. You should not
    override any other methods.
    """
    def __init__(self, glyphSet: Incomplete | None = None) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def moveTo(self, pt) -> None: ...
    def lineTo(self, pt) -> None: ...
    def curveTo(self, *points) -> None: ...
    def qCurveTo(self, *points) -> None: ...

def decomposeSuperBezierSegment(points):
    """Split the SuperBezier described by 'points' into a list of regular
    bezier segments. The 'points' argument must be a sequence with length
    3 or greater, containing (x, y) coordinates. The last point is the
    destination on-curve point, the rest of the points are off-curve points.
    The start point should not be supplied.

    This function returns a list of (pt1, pt2, pt3) tuples, which each
    specify a regular curveto-style bezier segment.
    """
def decomposeQuadraticSegment(points):
    '''Split the quadratic curve segment described by \'points\' into a list
    of "atomic" quadratic segments. The \'points\' argument must be a sequence
    with length 2 or greater, containing (x, y) coordinates. The last point
    is the destination on-curve point, the rest of the points are off-curve
    points. The start point should not be supplied.

    This function returns a list of (pt1, pt2) tuples, which each specify a
    plain quadratic bezier segment.
    '''

class _TestPen(BasePen):
    """Test class that prints PostScript to stdout."""
