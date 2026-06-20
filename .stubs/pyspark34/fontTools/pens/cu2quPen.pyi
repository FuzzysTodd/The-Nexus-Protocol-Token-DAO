from _typeshed import Incomplete
from fontTools.cu2qu import curve_to_quadratic as curve_to_quadratic, curves_to_quadratic as curves_to_quadratic
from fontTools.pens.basePen import decomposeSuperBezierSegment as decomposeSuperBezierSegment
from fontTools.pens.filterPen import FilterPen as FilterPen
from fontTools.pens.pointPen import BasePointToSegmentPen as BasePointToSegmentPen, ReverseContourPointPen as ReverseContourPointPen
from fontTools.pens.reverseContourPen import ReverseContourPen as ReverseContourPen

class Cu2QuPen(FilterPen):
    """A filter pen to convert cubic bezier curves to quadratic b-splines
    using the FontTools SegmentPen protocol.

    Args:

        other_pen: another SegmentPen used to draw the transformed outline.
        max_err: maximum approximation error in font units. For optimal results,
            if you know the UPEM of the font, we recommend setting this to a
            value equal, or close to UPEM / 1000.
        reverse_direction: flip the contours' direction but keep starting point.
        stats: a dictionary counting the point numbers of quadratic segments.
        all_quadratic: if True (default), only quadratic b-splines are generated.
            if False, quadratic curves or cubic curves are generated depending
            on which one is more economical.
    """
    max_err: Incomplete
    stats: Incomplete
    all_quadratic: Incomplete
    def __init__(self, other_pen, max_err, reverse_direction: bool = False, stats: Incomplete | None = None, all_quadratic: bool = True) -> None: ...
    def curveTo(self, *points) -> None: ...

class Cu2QuPointPen(BasePointToSegmentPen):
    """A filter pen to convert cubic bezier curves to quadratic b-splines
    using the FontTools PointPen protocol.

    Args:
        other_point_pen: another PointPen used to draw the transformed outline.
        max_err: maximum approximation error in font units. For optimal results,
            if you know the UPEM of the font, we recommend setting this to a
            value equal, or close to UPEM / 1000.
        reverse_direction: reverse the winding direction of all contours.
        stats: a dictionary counting the point numbers of quadratic segments.
        all_quadratic: if True (default), only quadratic b-splines are generated.
            if False, quadratic curves or cubic curves are generated depending
            on which one is more economical.
    """
    pen: Incomplete
    max_err: Incomplete
    stats: Incomplete
    all_quadratic: Incomplete
    def __init__(self, other_point_pen, max_err, reverse_direction: bool = False, stats: Incomplete | None = None, all_quadratic: bool = True) -> None: ...
    def addComponent(self, baseGlyphName, transformation) -> None: ...

class Cu2QuMultiPen:
    """A filter multi-pen to convert cubic bezier curves to quadratic b-splines
    in a interpolation-compatible manner, using the FontTools SegmentPen protocol.

    Args:

        other_pens: list of SegmentPens used to draw the transformed outlines.
        max_err: maximum approximation error in font units. For optimal results,
            if you know the UPEM of the font, we recommend setting this to a
            value equal, or close to UPEM / 1000.
        reverse_direction: flip the contours' direction but keep starting point.

    This pen does not follow the normal SegmentPen protocol. Instead, its
    moveTo/lineTo/qCurveTo/curveTo methods take a list of tuples that are
    arguments that would normally be passed to a SegmentPen, one item for
    each of the pens in other_pens.
    """
    pens: Incomplete
    max_err: Incomplete
    start_pts: Incomplete
    current_pts: Incomplete
    def __init__(self, other_pens, max_err, reverse_direction: bool = False) -> None: ...
    def moveTo(self, pts) -> None: ...
    def lineTo(self, pts) -> None: ...
    def qCurveTo(self, pointsList) -> None: ...
    def curveTo(self, pointsList) -> None: ...
    def closePath(self) -> None: ...
    def endPath(self) -> None: ...
    def addComponent(self, glyphName, transformations) -> None: ...
