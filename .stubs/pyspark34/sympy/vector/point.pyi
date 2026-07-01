from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.cache import cacheit as cacheit
from sympy.core.symbol import Str as Str
from sympy.vector.coordsysrect import CoordSys3D as CoordSys3D
from sympy.vector.vector import Vector as Vector

class Point(Basic):
    """
    Represents a point in 3-D space.
    """
    def __new__(cls, name, position=..., parent_point: Incomplete | None = None): ...
    def position_wrt(self, other):
        """
        Returns the position vector of this Point with respect to
        another Point/CoordSys3D.

        Parameters
        ==========

        other : Point/CoordSys3D
            If other is a Point, the position of this Point wrt it is
            returned. If its an instance of CoordSyRect, the position
            wrt its origin is returned.

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> p1 = N.origin.locate_new('p1', 10 * N.i)
        >>> N.origin.position_wrt(p1)
        (-10)*N.i

        """
    def locate_new(self, name, position):
        """
        Returns a new Point located at the given position wrt this
        Point.
        Thus, the position vector of the new Point wrt this one will
        be equal to the given 'position' parameter.

        Parameters
        ==========

        name : str
            Name of the new point

        position : Vector
            The position vector of the new Point wrt this one

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> p1 = N.origin.locate_new('p1', 10 * N.i)
        >>> p1.position_wrt(N.origin)
        10*N.i

        """
    def express_coordinates(self, coordinate_system):
        """
        Returns the Cartesian/rectangular coordinates of this point
        wrt the origin of the given CoordSys3D instance.

        Parameters
        ==========

        coordinate_system : CoordSys3D
            The coordinate system to express the coordinates of this
            Point in.

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> p1 = N.origin.locate_new('p1', 10 * N.i)
        >>> p2 = p1.locate_new('p2', 5 * N.j)
        >>> p2.express_coordinates(N)
        (10, 5, 0)

        """
