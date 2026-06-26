from _typeshed import Incomplete
from collections.abc import Generator
from fontTools.pens.filterPen import ContourFilterPen

__all__ = ['reversedContour', 'ReverseContourPen']

class ReverseContourPen(ContourFilterPen):
    """Filter pen that passes outline data to another pen, but reversing
    the winding direction of all contours. Components are simply passed
    through unchanged.

    Closed contours are reversed in such a way that the first point remains
    the first point.
    """
    outputImpliedClosingLine: Incomplete
    def __init__(self, outPen, outputImpliedClosingLine: bool = False) -> None: ...
    def filterContour(self, contour): ...

def reversedContour(contour, outputImpliedClosingLine: bool = False) -> Generator[Incomplete, None, None]:
    """Generator that takes a list of pen's (operator, operands) tuples,
    and yields them with the winding direction reversed.
    """
