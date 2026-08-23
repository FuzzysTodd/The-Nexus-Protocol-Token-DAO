from _typeshed import Incomplete
from fontTools.pens.filterPen import ContourFilterPen as ContourFilterPen
from fontTools.pens.reverseContourPen import ReverseContourPen as ReverseContourPen
from fontTools.qu2cu import quadratic_to_curves as quadratic_to_curves

class Qu2CuPen(ContourFilterPen):
    """A filter pen to convert quadratic bezier splines to cubic curves
    using the FontTools SegmentPen protocol.

    Args:

        other_pen: another SegmentPen used to draw the transformed outline.
        max_err: maximum approximation error in font units. For optimal results,
            if you know the UPEM of the font, we recommend setting this to a
            value equal, or close to UPEM / 1000.
        reverse_direction: flip the contours' direction but keep starting point.
        stats: a dictionary counting the point numbers of cubic segments.
    """
    all_cubic: Incomplete
    max_err: Incomplete
    stats: Incomplete
    def __init__(self, other_pen, max_err, all_cubic: bool = False, reverse_direction: bool = False, stats: Incomplete | None = None) -> None: ...
    def filterContour(self, contour): ...
