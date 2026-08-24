from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

__all__ = ['approximateCubicArcLength', 'approximateCubicArcLengthC', 'approximateQuadraticArcLength', 'approximateQuadraticArcLengthC', 'calcCubicArcLength', 'calcCubicArcLengthC', 'calcQuadraticArcLength', 'calcQuadraticArcLengthC', 'calcCubicBounds', 'calcQuadraticBounds', 'splitLine', 'splitQuadratic', 'splitCubic', 'splitQuadraticAtT', 'splitCubicAtT', 'splitCubicAtTC', 'splitCubicIntoTwoAtTC', 'solveQuadratic', 'solveCubic', 'quadraticPointAtT', 'cubicPointAtT', 'cubicPointAtTC', 'linePointAtT', 'segmentPointAtT', 'lineLineIntersections', 'curveLineIntersections', 'curveCurveIntersections', 'segmentSegmentIntersections']

class Intersection(NamedTuple):
    pt: Incomplete
    t1: Incomplete
    t2: Incomplete

def calcCubicArcLength(pt1, pt2, pt3, pt4, tolerance: float = 0.005):
    '''Calculates the arc length for a cubic Bezier segment.

    Whereas :func:`approximateCubicArcLength` approximates the length, this
    function calculates it by "measuring", recursively dividing the curve
    until the divided segments are shorter than ``tolerance``.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
        tolerance: Controls the precision of the calcuation.

    Returns:
        Arc length value.
    '''
def calcCubicArcLengthC(pt1, pt2, pt3, pt4, tolerance: float = 0.005):
    """Calculates the arc length for a cubic Bezier segment.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers.
        tolerance: Controls the precision of the calcuation.

    Returns:
        Arc length value.
    """
def calcQuadraticArcLength(pt1, pt2, pt3):
    """Calculates the arc length for a quadratic Bezier segment.

    Args:
        pt1: Start point of the Bezier as 2D tuple.
        pt2: Handle point of the Bezier as 2D tuple.
        pt3: End point of the Bezier as 2D tuple.

    Returns:
        Arc length value.

    Example::

        >>> calcQuadraticArcLength((0, 0), (0, 0), (0, 0)) # empty segment
        0.0
        >>> calcQuadraticArcLength((0, 0), (50, 0), (80, 0)) # collinear points
        80.0
        >>> calcQuadraticArcLength((0, 0), (0, 50), (0, 80)) # collinear points vertical
        80.0
        >>> calcQuadraticArcLength((0, 0), (50, 20), (100, 40)) # collinear points
        107.70329614269008
        >>> calcQuadraticArcLength((0, 0), (0, 100), (100, 0))
        154.02976155645263
        >>> calcQuadraticArcLength((0, 0), (0, 50), (100, 0))
        120.21581243984076
        >>> calcQuadraticArcLength((0, 0), (50, -10), (80, 50))
        102.53273816445825
        >>> calcQuadraticArcLength((0, 0), (40, 0), (-40, 0)) # collinear points, control point outside
        66.66666666666667
        >>> calcQuadraticArcLength((0, 0), (40, 0), (0, 0)) # collinear points, looping back
        40.0
    """
def calcQuadraticArcLengthC(pt1, pt2, pt3):
    """Calculates the arc length for a quadratic Bezier segment.

    Args:
        pt1: Start point of the Bezier as a complex number.
        pt2: Handle point of the Bezier as a complex number.
        pt3: End point of the Bezier as a complex number.

    Returns:
        Arc length value.
    """
def approximateQuadraticArcLength(pt1, pt2, pt3):
    """Calculates the arc length for a quadratic Bezier segment.

    Uses Gauss-Legendre quadrature for a branch-free approximation.
    See :func:`calcQuadraticArcLength` for a slower but more accurate result.

    Args:
        pt1: Start point of the Bezier as 2D tuple.
        pt2: Handle point of the Bezier as 2D tuple.
        pt3: End point of the Bezier as 2D tuple.

    Returns:
        Approximate arc length value.
    """
def approximateQuadraticArcLengthC(pt1, pt2, pt3):
    """Calculates the arc length for a quadratic Bezier segment.

    Uses Gauss-Legendre quadrature for a branch-free approximation.
    See :func:`calcQuadraticArcLength` for a slower but more accurate result.

    Args:
        pt1: Start point of the Bezier as a complex number.
        pt2: Handle point of the Bezier as a complex number.
        pt3: End point of the Bezier as a complex number.

    Returns:
        Approximate arc length value.
    """
def calcQuadraticBounds(pt1, pt2, pt3):
    """Calculates the bounding rectangle for a quadratic Bezier segment.

    Args:
        pt1: Start point of the Bezier as a 2D tuple.
        pt2: Handle point of the Bezier as a 2D tuple.
        pt3: End point of the Bezier as a 2D tuple.

    Returns:
        A four-item tuple representing the bounding rectangle ``(xMin, yMin, xMax, yMax)``.

    Example::

        >>> calcQuadraticBounds((0, 0), (50, 100), (100, 0))
        (0, 0, 100, 50.0)
        >>> calcQuadraticBounds((0, 0), (100, 0), (100, 100))
        (0.0, 0.0, 100, 100)
    """
def approximateCubicArcLength(pt1, pt2, pt3, pt4):
    """Approximates the arc length for a cubic Bezier segment.

    Uses Gauss-Lobatto quadrature with n=5 points to approximate arc length.
    See :func:`calcCubicArcLength` for a slower but more accurate result.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.

    Returns:
        Arc length value.

    Example::

        >>> approximateCubicArcLength((0, 0), (25, 100), (75, 100), (100, 0))
        190.04332968932817
        >>> approximateCubicArcLength((0, 0), (50, 0), (100, 50), (100, 100))
        154.8852074945903
        >>> approximateCubicArcLength((0, 0), (50, 0), (100, 0), (150, 0)) # line; exact result should be 150.
        149.99999999999991
        >>> approximateCubicArcLength((0, 0), (50, 0), (100, 0), (-50, 0)) # cusp; exact result should be 150.
        136.9267662156362
        >>> approximateCubicArcLength((0, 0), (50, 0), (100, -50), (-50, 0)) # cusp
        154.80848416537057
    """
def approximateCubicArcLengthC(pt1, pt2, pt3, pt4):
    """Approximates the arc length for a cubic Bezier segment.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers.

    Returns:
        Arc length value.
    """
def calcCubicBounds(pt1, pt2, pt3, pt4):
    '''Calculates the bounding rectangle for a quadratic Bezier segment.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.

    Returns:
        A four-item tuple representing the bounding rectangle ``(xMin, yMin, xMax, yMax)``.

    Example::

        >>> calcCubicBounds((0, 0), (25, 100), (75, 100), (100, 0))
        (0, 0, 100, 75.0)
        >>> calcCubicBounds((0, 0), (50, 0), (100, 50), (100, 100))
        (0.0, 0.0, 100, 100)
        >>> print("%f %f %f %f" % calcCubicBounds((50, 0), (0, 100), (100, 100), (50, 0)))
        35.566243 0.000000 64.433757 75.000000
    '''
def splitLine(pt1, pt2, where, isHorizontal):
    """Split a line at a given coordinate.

    Args:
        pt1: Start point of line as 2D tuple.
        pt2: End point of line as 2D tuple.
        where: Position at which to split the line.
        isHorizontal: Direction of the ray splitting the line. If true,
            ``where`` is interpreted as a Y coordinate; if false, then
            ``where`` is interpreted as an X coordinate.

    Returns:
        A list of two line segments (each line segment being two 2D tuples)
        if the line was successfully split, or a list containing the original
        line.

    Example::

        >>> printSegments(splitLine((0, 0), (100, 100), 50, True))
        ((0, 0), (50, 50))
        ((50, 50), (100, 100))
        >>> printSegments(splitLine((0, 0), (100, 100), 100, True))
        ((0, 0), (100, 100))
        >>> printSegments(splitLine((0, 0), (100, 100), 0, True))
        ((0, 0), (0, 0))
        ((0, 0), (100, 100))
        >>> printSegments(splitLine((0, 0), (100, 100), 0, False))
        ((0, 0), (0, 0))
        ((0, 0), (100, 100))
        >>> printSegments(splitLine((100, 0), (0, 0), 50, False))
        ((100, 0), (50, 0))
        ((50, 0), (0, 0))
        >>> printSegments(splitLine((0, 100), (0, 0), 50, True))
        ((0, 100), (0, 50))
        ((0, 50), (0, 0))
    """
def splitQuadratic(pt1, pt2, pt3, where, isHorizontal):
    """Split a quadratic Bezier curve at a given coordinate.

    Args:
        pt1,pt2,pt3: Control points of the Bezier as 2D tuples.
        where: Position at which to split the curve.
        isHorizontal: Direction of the ray splitting the curve. If true,
            ``where`` is interpreted as a Y coordinate; if false, then
            ``where`` is interpreted as an X coordinate.

    Returns:
        A list of two curve segments (each curve segment being three 2D tuples)
        if the curve was successfully split, or a list containing the original
        curve.

    Example::

        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 150, False))
        ((0, 0), (50, 100), (100, 0))
        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 50, False))
        ((0, 0), (25, 50), (50, 50))
        ((50, 50), (75, 50), (100, 0))
        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 25, False))
        ((0, 0), (12.5, 25), (25, 37.5))
        ((25, 37.5), (62.5, 75), (100, 0))
        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 25, True))
        ((0, 0), (7.32233, 14.6447), (14.6447, 25))
        ((14.6447, 25), (50, 75), (85.3553, 25))
        ((85.3553, 25), (92.6777, 14.6447), (100, -7.10543e-15))
        >>> # XXX I'm not at all sure if the following behavior is desirable:
        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 50, True))
        ((0, 0), (25, 50), (50, 50))
        ((50, 50), (50, 50), (50, 50))
        ((50, 50), (75, 50), (100, 0))
    """
def splitCubic(pt1, pt2, pt3, pt4, where, isHorizontal):
    """Split a cubic Bezier curve at a given coordinate.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
        where: Position at which to split the curve.
        isHorizontal: Direction of the ray splitting the curve. If true,
            ``where`` is interpreted as a Y coordinate; if false, then
            ``where`` is interpreted as an X coordinate.

    Returns:
        A list of two curve segments (each curve segment being four 2D tuples)
        if the curve was successfully split, or a list containing the original
        curve.

    Example::

        >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 150, False))
        ((0, 0), (25, 100), (75, 100), (100, 0))
        >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 50, False))
        ((0, 0), (12.5, 50), (31.25, 75), (50, 75))
        ((50, 75), (68.75, 75), (87.5, 50), (100, 0))
        >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 25, True))
        ((0, 0), (2.29379, 9.17517), (4.79804, 17.5085), (7.47414, 25))
        ((7.47414, 25), (31.2886, 91.6667), (68.7114, 91.6667), (92.5259, 25))
        ((92.5259, 25), (95.202, 17.5085), (97.7062, 9.17517), (100, 1.77636e-15))
    """
def splitQuadraticAtT(pt1, pt2, pt3, *ts):
    """Split a quadratic Bezier curve at one or more values of t.

    Args:
        pt1,pt2,pt3: Control points of the Bezier as 2D tuples.
        *ts: Positions at which to split the curve.

    Returns:
        A list of curve segments (each curve segment being three 2D tuples).

    Examples::

        >>> printSegments(splitQuadraticAtT((0, 0), (50, 100), (100, 0), 0.5))
        ((0, 0), (25, 50), (50, 50))
        ((50, 50), (75, 50), (100, 0))
        >>> printSegments(splitQuadraticAtT((0, 0), (50, 100), (100, 0), 0.5, 0.75))
        ((0, 0), (25, 50), (50, 50))
        ((50, 50), (62.5, 50), (75, 37.5))
        ((75, 37.5), (87.5, 25), (100, 0))
    """
def splitCubicAtT(pt1, pt2, pt3, pt4, *ts):
    """Split a cubic Bezier curve at one or more values of t.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
        *ts: Positions at which to split the curve.

    Returns:
        A list of curve segments (each curve segment being four 2D tuples).

    Examples::

        >>> printSegments(splitCubicAtT((0, 0), (25, 100), (75, 100), (100, 0), 0.5))
        ((0, 0), (12.5, 50), (31.25, 75), (50, 75))
        ((50, 75), (68.75, 75), (87.5, 50), (100, 0))
        >>> printSegments(splitCubicAtT((0, 0), (25, 100), (75, 100), (100, 0), 0.5, 0.75))
        ((0, 0), (12.5, 50), (31.25, 75), (50, 75))
        ((50, 75), (59.375, 75), (68.75, 68.75), (77.3438, 56.25))
        ((77.3438, 56.25), (85.9375, 43.75), (93.75, 25), (100, 0))
    """
def splitCubicAtTC(pt1, pt2, pt3, pt4, *ts) -> Generator[Incomplete, Incomplete, None]:
    """Split a cubic Bezier curve at one or more values of t.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers..
        *ts: Positions at which to split the curve.

    Yields:
        Curve segments (each curve segment being four complex numbers).
    """
def splitCubicIntoTwoAtTC(pt1, pt2, pt3, pt4, t):
    """Split a cubic Bezier curve at t.

    Args:
        pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers.
        t: Position at which to split the curve.

    Returns:
        A tuple of two curve segments (each curve segment being four complex numbers).
    """
def solveQuadratic(a, b, c, sqrt=...):
    """Solve a quadratic equation.

    Solves *a*x*x + b*x + c = 0* where a, b and c are real.

    Args:
        a: coefficient of *x²*
        b: coefficient of *x*
        c: constant term

    Returns:
        A list of roots. Note that the returned list is neither guaranteed to
        be sorted nor to contain unique values!
    """
def solveCubic(a, b, c, d):
    """Solve a cubic equation.

    Solves *a*x*x*x + b*x*x + c*x + d = 0* where a, b, c and d are real.

    Args:
        a: coefficient of *x³*
        b: coefficient of *x²*
        c: coefficient of *x*
        d: constant term

    Returns:
        A list of roots. Note that the returned list is neither guaranteed to
        be sorted nor to contain unique values!

    Examples::

        >>> solveCubic(1, 1, -6, 0)
        [-3.0, -0.0, 2.0]
        >>> solveCubic(-10.0, -9.0, 48.0, -29.0)
        [-2.9, 1.0, 1.0]
        >>> solveCubic(-9.875, -9.0, 47.625, -28.75)
        [-2.911392, 1.0, 1.0]
        >>> solveCubic(1.0, -4.5, 6.75, -3.375)
        [1.5, 1.5, 1.5]
        >>> solveCubic(-12.0, 18.0, -9.0, 1.50023651123)
        [0.5, 0.5, 0.5]
        >>> solveCubic(
        ...     9.0, 0.0, 0.0, -7.62939453125e-05
        ... ) == [-0.0, -0.0, -0.0]
        True
    """
def linePointAtT(pt1, pt2, t):
    """Finds the point at time `t` on a line.

    Args:
        pt1, pt2: Coordinates of the line as 2D tuples.
        t: The time along the line.

    Returns:
        A 2D tuple with the coordinates of the point.
    """
def quadraticPointAtT(pt1, pt2, pt3, t):
    """Finds the point at time `t` on a quadratic curve.

    Args:
        pt1, pt2, pt3: Coordinates of the curve as 2D tuples.
        t: The time along the curve.

    Returns:
        A 2D tuple with the coordinates of the point.
    """
def cubicPointAtT(pt1, pt2, pt3, pt4, t):
    """Finds the point at time `t` on a cubic curve.

    Args:
        pt1, pt2, pt3, pt4: Coordinates of the curve as 2D tuples.
        t: The time along the curve.

    Returns:
        A 2D tuple with the coordinates of the point.
    """
def cubicPointAtTC(pt1, pt2, pt3, pt4, t):
    """Finds the point at time `t` on a cubic curve.

    Args:
        pt1, pt2, pt3, pt4: Coordinates of the curve as complex numbers.
        t: The time along the curve.

    Returns:
        A complex number with the coordinates of the point.
    """
def segmentPointAtT(seg, t): ...
def lineLineIntersections(s1, e1, s2, e2):
    """Finds intersections between two line segments.

    Args:
        s1, e1: Coordinates of the first line as 2D tuples.
        s2, e2: Coordinates of the second line as 2D tuples.

    Returns:
        A list of ``Intersection`` objects, each object having ``pt``, ``t1``
        and ``t2`` attributes containing the intersection point, time on first
        segment and time on second segment respectively.

    Examples::

        >>> a = lineLineIntersections( (310,389), (453, 222), (289, 251), (447, 367))
        >>> len(a)
        1
        >>> intersection = a[0]
        >>> intersection.pt
        (374.44882952482897, 313.73458370177315)
        >>> (intersection.t1, intersection.t2)
        (0.45069111555824465, 0.5408153767394238)
    """
def curveLineIntersections(curve, line):
    """Finds intersections between a curve and a line.

    Args:
        curve: List of coordinates of the curve segment as 2D tuples.
        line: List of coordinates of the line segment as 2D tuples.

    Returns:
        A list of ``Intersection`` objects, each object having ``pt``, ``t1``
        and ``t2`` attributes containing the intersection point, time on first
        segment and time on second segment respectively.

    Examples::
        >>> curve = [ (100, 240), (30, 60), (210, 230), (160, 30) ]
        >>> line  = [ (25, 260), (230, 20) ]
        >>> intersections = curveLineIntersections(curve, line)
        >>> len(intersections)
        3
        >>> intersections[0].pt
        (84.9000930760723, 189.87306176459828)
    """
def curveCurveIntersections(curve1, curve2):
    """Finds intersections between a curve and a curve.

    Args:
        curve1: List of coordinates of the first curve segment as 2D tuples.
        curve2: List of coordinates of the second curve segment as 2D tuples.

    Returns:
        A list of ``Intersection`` objects, each object having ``pt``, ``t1``
        and ``t2`` attributes containing the intersection point, time on first
        segment and time on second segment respectively.

    Examples::
        >>> curve1 = [ (10,100), (90,30), (40,140), (220,220) ]
        >>> curve2 = [ (5,150), (180,20), (80,250), (210,190) ]
        >>> intersections = curveCurveIntersections(curve1, curve2)
        >>> len(intersections)
        3
        >>> intersections[0].pt
        (81.7831487395506, 109.88904552375288)
    """
def segmentSegmentIntersections(seg1, seg2):
    """Finds intersections between two segments.

    Args:
        seg1: List of coordinates of the first segment as 2D tuples.
        seg2: List of coordinates of the second segment as 2D tuples.

    Returns:
        A list of ``Intersection`` objects, each object having ``pt``, ``t1``
        and ``t2`` attributes containing the intersection point, time on first
        segment and time on second segment respectively.

    Examples::
        >>> curve1 = [ (10,100), (90,30), (40,140), (220,220) ]
        >>> curve2 = [ (5,150), (180,20), (80,250), (210,190) ]
        >>> intersections = segmentSegmentIntersections(curve1, curve2)
        >>> len(intersections)
        3
        >>> intersections[0].pt
        (81.7831487395506, 109.88904552375288)
        >>> curve3 = [ (100, 240), (30, 60), (210, 230), (160, 30) ]
        >>> line  = [ (25, 260), (230, 20) ]
        >>> intersections = segmentSegmentIntersections(curve3, line)
        >>> len(intersections)
        3
        >>> intersections[0].pt
        (84.9000930760723, 189.87306176459828)

    """
