from _typeshed import Incomplete
from dataclasses import dataclass
from typing import NamedTuple

__all__ = ['Transform', 'Identity', 'Offset', 'Scale', 'DecomposedTransform']

class Transform(NamedTuple):
    '''2x2 transformation matrix plus offset, a.k.a. Affine transform.
    Transform instances are immutable: all transforming methods, eg.
    rotate(), return a new Transform instance.

    :Example:

            >>> t = Transform()
            >>> t
            <Transform [1 0 0 1 0 0]>
            >>> t.scale(2)
            <Transform [2 0 0 2 0 0]>
            >>> t.scale(2.5, 5.5)
            <Transform [2.5 0 0 5.5 0 0]>
            >>>
            >>> t.scale(2, 3).transformPoint((100, 100))
            (200, 300)

    Transform\'s constructor takes six arguments, all of which are
    optional, and can be used as keyword arguments::

            >>> Transform(12)
            <Transform [12 0 0 1 0 0]>
            >>> Transform(dx=12)
            <Transform [1 0 0 1 12 0]>
            >>> Transform(yx=12)
            <Transform [1 0 12 1 0 0]>

    Transform instances also behave like sequences of length 6::

            >>> len(Identity)
            6
            >>> list(Identity)
            [1, 0, 0, 1, 0, 0]
            >>> tuple(Identity)
            (1, 0, 0, 1, 0, 0)

    Transform instances are comparable::

            >>> t1 = Identity.scale(2, 3).translate(4, 6)
            >>> t2 = Identity.translate(8, 18).scale(2, 3)
            >>> t1 == t2
            1

    But beware of floating point rounding errors::

            >>> t1 = Identity.scale(0.2, 0.3).translate(0.4, 0.6)
            >>> t2 = Identity.translate(0.08, 0.18).scale(0.2, 0.3)
            >>> t1
            <Transform [0.2 0 0 0.3 0.08 0.18]>
            >>> t2
            <Transform [0.2 0 0 0.3 0.08 0.18]>
            >>> t1 == t2
            0

    Transform instances are hashable, meaning you can use them as
    keys in dictionaries::

            >>> d = {Scale(12, 13): None}
            >>> d
            {<Transform [12 0 0 13 0 0]>: None}

    But again, beware of floating point rounding errors::

            >>> t1 = Identity.scale(0.2, 0.3).translate(0.4, 0.6)
            >>> t2 = Identity.translate(0.08, 0.18).scale(0.2, 0.3)
            >>> t1
            <Transform [0.2 0 0 0.3 0.08 0.18]>
            >>> t2
            <Transform [0.2 0 0 0.3 0.08 0.18]>
            >>> d = {t1: None}
            >>> d
            {<Transform [0.2 0 0 0.3 0.08 0.18]>: None}
            >>> d[t2]
            Traceback (most recent call last):
              File "<stdin>", line 1, in ?
            KeyError: <Transform [0.2 0 0 0.3 0.08 0.18]>
    '''
    xx: float = ...
    xy: float = ...
    yx: float = ...
    yy: float = ...
    dx: float = ...
    dy: float = ...
    def transformPoint(self, p):
        """Transform a point.

        :Example:

                >>> t = Transform()
                >>> t = t.scale(2.5, 5.5)
                >>> t.transformPoint((100, 100))
                (250.0, 550.0)
        """
    def transformPoints(self, points):
        """Transform a list of points.

        :Example:

                >>> t = Scale(2, 3)
                >>> t.transformPoints([(0, 0), (0, 100), (100, 100), (100, 0)])
                [(0, 0), (0, 300), (200, 300), (200, 0)]
                >>>
        """
    def transformVector(self, v):
        """Transform an (dx, dy) vector, treating translation as zero.

        :Example:

                >>> t = Transform(2, 0, 0, 2, 10, 20)
                >>> t.transformVector((3, -4))
                (6, -8)
                >>>
        """
    def transformVectors(self, vectors):
        """Transform a list of (dx, dy) vector, treating translation as zero.

        :Example:
                >>> t = Transform(2, 0, 0, 2, 10, 20)
                >>> t.transformVectors([(3, -4), (5, -6)])
                [(6, -8), (10, -12)]
                >>>
        """
    def translate(self, x: int = 0, y: int = 0):
        """Return a new transformation, translated (offset) by x, y.

        :Example:
                >>> t = Transform()
                >>> t.translate(20, 30)
                <Transform [1 0 0 1 20 30]>
                >>>
        """
    def scale(self, x: int = 1, y: Incomplete | None = None):
        """Return a new transformation, scaled by x, y. The 'y' argument
        may be None, which implies to use the x value for y as well.

        :Example:
                >>> t = Transform()
                >>> t.scale(5)
                <Transform [5 0 0 5 0 0]>
                >>> t.scale(5, 6)
                <Transform [5 0 0 6 0 0]>
                >>>
        """
    def rotate(self, angle):
        """Return a new transformation, rotated by 'angle' (radians).

        :Example:
                >>> import math
                >>> t = Transform()
                >>> t.rotate(math.pi / 2)
                <Transform [0 1 -1 0 0 0]>
                >>>
        """
    def skew(self, x: int = 0, y: int = 0):
        """Return a new transformation, skewed by x and y.

        :Example:
                >>> import math
                >>> t = Transform()
                >>> t.skew(math.pi / 4)
                <Transform [1 0 1 1 0 0]>
                >>>
        """
    def transform(self, other):
        """Return a new transformation, transformed by another
        transformation.

        :Example:
                >>> t = Transform(2, 0, 0, 3, 1, 6)
                >>> t.transform((4, 3, 2, 1, 5, 6))
                <Transform [8 9 4 3 11 24]>
                >>>
        """
    def reverseTransform(self, other):
        """Return a new transformation, which is the other transformation
        transformed by self. self.reverseTransform(other) is equivalent to
        other.transform(self).

        :Example:
                >>> t = Transform(2, 0, 0, 3, 1, 6)
                >>> t.reverseTransform((4, 3, 2, 1, 5, 6))
                <Transform [8 6 6 3 21 15]>
                >>> Transform(4, 3, 2, 1, 5, 6).transform((2, 0, 0, 3, 1, 6))
                <Transform [8 6 6 3 21 15]>
                >>>
        """
    def inverse(self):
        """Return the inverse transformation.

        :Example:
                >>> t = Identity.translate(2, 3).scale(4, 5)
                >>> t.transformPoint((10, 20))
                (42, 103)
                >>> it = t.inverse()
                >>> it.transformPoint((42, 103))
                (10.0, 20.0)
                >>>
        """
    def toPS(self):
        """Return a PostScript representation

        :Example:

                >>> t = Identity.scale(2, 3).translate(4, 5)
                >>> t.toPS()
                '[2 0 0 3 8 15]'
                >>>
        """
    def toDecomposed(self) -> DecomposedTransform:
        """Decompose into a DecomposedTransform."""
    def __bool__(self) -> bool:
        """Returns True if transform is not identity, False otherwise.

        :Example:

                >>> bool(Identity)
                False
                >>> bool(Transform())
                False
                >>> bool(Scale(1.))
                False
                >>> bool(Scale(2))
                True
                >>> bool(Offset())
                False
                >>> bool(Offset(0))
                False
                >>> bool(Offset(2))
                True
        """

Identity: Incomplete

def Offset(x: int = 0, y: int = 0):
    """Return the identity transformation offset by x, y.

    :Example:
            >>> Offset(2, 3)
            <Transform [1 0 0 1 2 3]>
            >>>
    """
def Scale(x, y: Incomplete | None = None):
    """Return the identity transformation scaled by x, y. The 'y' argument
    may be None, which implies to use the x value for y as well.

    :Example:
            >>> Scale(2, 3)
            <Transform [2 0 0 3 0 0]>
            >>>
    """

@dataclass
class DecomposedTransform:
    """The DecomposedTransform class implements a transformation with separate
    translate, rotation, scale, skew, and transformation-center components.
    """
    translateX: float = ...
    translateY: float = ...
    rotation: float = ...
    scaleX: float = ...
    scaleY: float = ...
    skewX: float = ...
    skewY: float = ...
    tCenterX: float = ...
    tCenterY: float = ...
    def __bool__(self) -> bool: ...
    @classmethod
    def fromTransform(self, transform): ...
    def toTransform(self):
        """Return the Transform() equivalent of this transformation.

        :Example:
                >>> DecomposedTransform(scaleX=2, scaleY=2).toTransform()
                <Transform [2 0 0 2 0 0]>
                >>>
        """
    def __init__(self, translateX, translateY, rotation, scaleX, scaleY, skewX, skewY, tCenterX, tCenterY) -> None: ...
