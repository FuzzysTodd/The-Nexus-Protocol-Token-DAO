from _typeshed import Incomplete
from fontTools.pens.basePen import BasePen

__all__ = ['PointInsidePen']

class PointInsidePen(BasePen):
    '''This pen implements "point inside" testing: to test whether
    a given point lies inside the shape (black) or outside (white).
    Instances of this class can be recycled, as long as the
    setTestPoint() method is used to set the new point to test.

    Typical usage:

            pen = PointInsidePen(glyphSet, (100, 200))
            outline.draw(pen)
            isInside = pen.getResult()

    Both the even-odd algorithm and the non-zero-winding-rule
    algorithm are implemented. The latter is the default, specify
    True for the evenOdd argument of __init__ or setTestPoint
    to use the even-odd algorithm.
    '''
    def __init__(self, glyphSet, testPoint, evenOdd: bool = False) -> None: ...
    testPoint: Incomplete
    evenOdd: Incomplete
    firstPoint: Incomplete
    intersectionCount: int
    def setTestPoint(self, testPoint, evenOdd: bool = False) -> None:
        """Set the point to test. Call this _before_ the outline gets drawn."""
    def getWinding(self): ...
    def getResult(self):
        """After the shape has been drawn, getResult() returns True if the test
        point lies within the (black) shape, and False if it doesn't.
        """
