from .entity import GeometryEntity as GeometryEntity
from .line import Line as Line, Line3D as Line3D, LinearEntity as LinearEntity, LinearEntity3D as LinearEntity3D, Ray as Ray, Ray3D as Ray3D, Segment as Segment, Segment3D as Segment3D
from .point import Point as Point, Point3D as Point3D
from _typeshed import Incomplete
from sympy.core import Dummy as Dummy, Rational as Rational, S as S, Symbol as Symbol
from sympy.functions.elementary.trigonometric import acos as acos, asin as asin, cos as cos, sin as sin, sqrt as sqrt
from sympy.matrices import Matrix as Matrix
from sympy.polys.polytools import cancel as cancel
from sympy.solvers import linsolve as linsolve, solve as solve
from sympy.utilities.iterables import is_sequence as is_sequence, uniq as uniq
from sympy.utilities.misc import Undecidable as Undecidable, filldedent as filldedent, func_name as func_name

x: Incomplete
y: Incomplete
z: Incomplete
t: Incomplete

class Plane(GeometryEntity):
    """
    A plane is a flat, two-dimensional surface. A plane is the two-dimensional
    analogue of a point (zero-dimensions), a line (one-dimension) and a solid
    (three-dimensions). A plane can generally be constructed by two types of
    inputs. They are three non-collinear points and a point and the plane's
    normal vector.

    Attributes
    ==========

    p1
    normal_vector

    Examples
    ========

    >>> from sympy import Plane, Point3D
    >>> Plane(Point3D(1, 1, 1), Point3D(2, 3, 4), Point3D(2, 2, 2))
    Plane(Point3D(1, 1, 1), (-1, 2, -1))
    >>> Plane((1, 1, 1), (2, 3, 4), (2, 2, 2))
    Plane(Point3D(1, 1, 1), (-1, 2, -1))
    >>> Plane(Point3D(1, 1, 1), normal_vector=(1,4,7))
    Plane(Point3D(1, 1, 1), (1, 4, 7))

    """
    def __new__(cls, p1, a: Incomplete | None = None, b: Incomplete | None = None, **kwargs): ...
    def __contains__(self, o) -> bool: ...
    def angle_between(self, o):
        """Angle between the plane and other geometric entity.

        Parameters
        ==========

        LinearEntity3D, Plane.

        Returns
        =======

        angle : angle in radians

        Notes
        =====

        This method accepts only 3D entities as it's parameter, but if you want
        to calculate the angle between a 2D entity and a plane you should
        first convert to a 3D entity by projecting onto a desired plane and
        then proceed to calculate the angle.

        Examples
        ========

        >>> from sympy import Point3D, Line3D, Plane
        >>> a = Plane(Point3D(1, 2, 2), normal_vector=(1, 2, 3))
        >>> b = Line3D(Point3D(1, 3, 4), Point3D(2, 2, 2))
        >>> a.angle_between(b)
        -asin(sqrt(21)/6)

        """
    def arbitrary_point(self, u: Incomplete | None = None, v: Incomplete | None = None):
        """ Returns an arbitrary point on the Plane. If given two
        parameters, the point ranges over the entire plane. If given 1
        or no parameters, returns a point with one parameter which,
        when varying from 0 to 2*pi, moves the point in a circle of
        radius 1 about p1 of the Plane.

        Examples
        ========

        >>> from sympy import Plane, Ray
        >>> from sympy.abc import u, v, t, r
        >>> p = Plane((1, 1, 1), normal_vector=(1, 0, 0))
        >>> p.arbitrary_point(u, v)
        Point3D(1, u + 1, v + 1)
        >>> p.arbitrary_point(t)
        Point3D(1, cos(t) + 1, sin(t) + 1)

        While arbitrary values of u and v can move the point anywhere in
        the plane, the single-parameter point can be used to construct a
        ray whose arbitrary point can be located at angle t and radius
        r from p.p1:

        >>> Ray(p.p1, _).arbitrary_point(r)
        Point3D(1, r*cos(t) + 1, r*sin(t) + 1)

        Returns
        =======

        Point3D

        """
    @staticmethod
    def are_concurrent(*planes):
        """Is a sequence of Planes concurrent?

        Two or more Planes are concurrent if their intersections
        are a common line.

        Parameters
        ==========

        planes: list

        Returns
        =======

        Boolean

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a = Plane(Point3D(5, 0, 0), normal_vector=(1, -1, 1))
        >>> b = Plane(Point3D(0, -2, 0), normal_vector=(3, 1, 1))
        >>> c = Plane(Point3D(0, -1, 0), normal_vector=(5, -1, 9))
        >>> Plane.are_concurrent(a, b)
        True
        >>> Plane.are_concurrent(a, b, c)
        False

        """
    def distance(self, o):
        """Distance between the plane and another geometric entity.

        Parameters
        ==========

        Point3D, LinearEntity3D, Plane.

        Returns
        =======

        distance

        Notes
        =====

        This method accepts only 3D entities as it's parameter, but if you want
        to calculate the distance between a 2D entity and a plane you should
        first convert to a 3D entity by projecting onto a desired plane and
        then proceed to calculate the distance.

        Examples
        ========

        >>> from sympy import Point3D, Line3D, Plane
        >>> a = Plane(Point3D(1, 1, 1), normal_vector=(1, 1, 1))
        >>> b = Point3D(1, 2, 3)
        >>> a.distance(b)
        sqrt(3)
        >>> c = Line3D(Point3D(2, 3, 1), Point3D(1, 2, 2))
        >>> a.distance(c)
        0

        """
    def equals(self, o):
        """
        Returns True if self and o are the same mathematical entities.

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a = Plane(Point3D(1, 2, 3), normal_vector=(1, 1, 1))
        >>> b = Plane(Point3D(1, 2, 3), normal_vector=(2, 2, 2))
        >>> c = Plane(Point3D(1, 2, 3), normal_vector=(-1, 4, 6))
        >>> a.equals(a)
        True
        >>> a.equals(b)
        True
        >>> a.equals(c)
        False
        """
    def equation(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None):
        """The equation of the Plane.

        Examples
        ========

        >>> from sympy import Point3D, Plane
        >>> a = Plane(Point3D(1, 1, 2), Point3D(2, 4, 7), Point3D(3, 5, 1))
        >>> a.equation()
        -23*x + 11*y - 2*z + 16
        >>> a = Plane(Point3D(1, 4, 2), normal_vector=(6, 6, 6))
        >>> a.equation()
        6*x + 6*y + 6*z - 42

        """
    def intersection(self, o):
        """ The intersection with other geometrical entity.

        Parameters
        ==========

        Point, Point3D, LinearEntity, LinearEntity3D, Plane

        Returns
        =======

        List

        Examples
        ========

        >>> from sympy import Point3D, Line3D, Plane
        >>> a = Plane(Point3D(1, 2, 3), normal_vector=(1, 1, 1))
        >>> b = Point3D(1, 2, 3)
        >>> a.intersection(b)
        [Point3D(1, 2, 3)]
        >>> c = Line3D(Point3D(1, 4, 7), Point3D(2, 2, 2))
        >>> a.intersection(c)
        [Point3D(2, 2, 2)]
        >>> d = Plane(Point3D(6, 0, 0), normal_vector=(2, -5, 3))
        >>> e = Plane(Point3D(2, 0, 0), normal_vector=(3, 4, -3))
        >>> d.intersection(e)
        [Line3D(Point3D(78/23, -24/23, 0), Point3D(147/23, 321/23, 23))]

        """
    def is_coplanar(self, o):
        """ Returns True if `o` is coplanar with self, else False.

        Examples
        ========

        >>> from sympy import Plane
        >>> o = (0, 0, 0)
        >>> p = Plane(o, (1, 1, 1))
        >>> p2 = Plane(o, (2, 2, 2))
        >>> p == p2
        False
        >>> p.is_coplanar(p2)
        True
        """
    def is_parallel(self, l):
        """Is the given geometric entity parallel to the plane?

        Parameters
        ==========

        LinearEntity3D or Plane

        Returns
        =======

        Boolean

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a = Plane(Point3D(1,4,6), normal_vector=(2, 4, 6))
        >>> b = Plane(Point3D(3,1,3), normal_vector=(4, 8, 12))
        >>> a.is_parallel(b)
        True

        """
    def is_perpendicular(self, l):
        """Is the given geometric entity perpendicualar to the given plane?

        Parameters
        ==========

        LinearEntity3D or Plane

        Returns
        =======

        Boolean

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a = Plane(Point3D(1,4,6), normal_vector=(2, 4, 6))
        >>> b = Plane(Point3D(2, 2, 2), normal_vector=(-1, 2, -1))
        >>> a.is_perpendicular(b)
        True

        """
    @property
    def normal_vector(self):
        """Normal vector of the given plane.

        Examples
        ========

        >>> from sympy import Point3D, Plane
        >>> a = Plane(Point3D(1, 1, 1), Point3D(2, 3, 4), Point3D(2, 2, 2))
        >>> a.normal_vector
        (-1, 2, -1)
        >>> a = Plane(Point3D(1, 1, 1), normal_vector=(1, 4, 7))
        >>> a.normal_vector
        (1, 4, 7)

        """
    @property
    def p1(self):
        """The only defining point of the plane. Others can be obtained from the
        arbitrary_point method.

        See Also
        ========

        sympy.geometry.point.Point3D

        Examples
        ========

        >>> from sympy import Point3D, Plane
        >>> a = Plane(Point3D(1, 1, 1), Point3D(2, 3, 4), Point3D(2, 2, 2))
        >>> a.p1
        Point3D(1, 1, 1)

        """
    def parallel_plane(self, pt):
        """
        Plane parallel to the given plane and passing through the point pt.

        Parameters
        ==========

        pt: Point3D

        Returns
        =======

        Plane

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a = Plane(Point3D(1, 4, 6), normal_vector=(2, 4, 6))
        >>> a.parallel_plane(Point3D(2, 3, 5))
        Plane(Point3D(2, 3, 5), (2, 4, 6))

        """
    def perpendicular_line(self, pt):
        """A line perpendicular to the given plane.

        Parameters
        ==========

        pt: Point3D

        Returns
        =======

        Line3D

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a = Plane(Point3D(1,4,6), normal_vector=(2, 4, 6))
        >>> a.perpendicular_line(Point3D(9, 8, 7))
        Line3D(Point3D(9, 8, 7), Point3D(11, 12, 13))

        """
    def perpendicular_plane(self, *pts):
        """
        Return a perpendicular passing through the given points. If the
        direction ratio between the points is the same as the Plane's normal
        vector then, to select from the infinite number of possible planes,
        a third point will be chosen on the z-axis (or the y-axis
        if the normal vector is already parallel to the z-axis). If less than
        two points are given they will be supplied as follows: if no point is
        given then pt1 will be self.p1; if a second point is not given it will
        be a point through pt1 on a line parallel to the z-axis (if the normal
        is not already the z-axis, otherwise on the line parallel to the
        y-axis).

        Parameters
        ==========

        pts: 0, 1 or 2 Point3D

        Returns
        =======

        Plane

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a, b = Point3D(0, 0, 0), Point3D(0, 1, 0)
        >>> Z = (0, 0, 1)
        >>> p = Plane(a, normal_vector=Z)
        >>> p.perpendicular_plane(a, b)
        Plane(Point3D(0, 0, 0), (1, 0, 0))
        """
    def projection_line(self, line):
        """Project the given line onto the plane through the normal plane
        containing the line.

        Parameters
        ==========

        LinearEntity or LinearEntity3D

        Returns
        =======

        Point3D, Line3D, Ray3D or Segment3D

        Notes
        =====

        For the interaction between 2D and 3D lines(segments, rays), you should
        convert the line to 3D by using this method. For example for finding the
        intersection between a 2D and a 3D line, convert the 2D line to a 3D line
        by projecting it on a required plane and then proceed to find the
        intersection between those lines.

        Examples
        ========

        >>> from sympy import Plane, Line, Line3D, Point3D
        >>> a = Plane(Point3D(1, 1, 1), normal_vector=(1, 1, 1))
        >>> b = Line(Point3D(1, 1), Point3D(2, 2))
        >>> a.projection_line(b)
        Line3D(Point3D(4/3, 4/3, 1/3), Point3D(5/3, 5/3, -1/3))
        >>> c = Line3D(Point3D(1, 1, 1), Point3D(2, 2, 2))
        >>> a.projection_line(c)
        Point3D(1, 1, 1)

        """
    def projection(self, pt):
        """Project the given point onto the plane along the plane normal.

        Parameters
        ==========

        Point or Point3D

        Returns
        =======

        Point3D

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> A = Plane(Point3D(1, 1, 2), normal_vector=(1, 1, 1))

        The projection is along the normal vector direction, not the z
        axis, so (1, 1) does not project to (1, 1, 2) on the plane A:

        >>> b = Point3D(1, 1)
        >>> A.projection(b)
        Point3D(5/3, 5/3, 2/3)
        >>> _ in A
        True

        But the point (1, 1, 2) projects to (1, 1) on the XY-plane:

        >>> XY = Plane((0, 0, 0), (0, 0, 1))
        >>> XY.projection((1, 1, 2))
        Point3D(1, 1, 0)
        """
    def random_point(self, seed: Incomplete | None = None):
        """ Returns a random point on the Plane.

        Returns
        =======

        Point3D

        Examples
        ========

        >>> from sympy import Plane
        >>> p = Plane((1, 0, 0), normal_vector=(0, 1, 0))
        >>> r = p.random_point(seed=42)  # seed value is optional
        >>> r.n(3)
        Point3D(2.29, 0, -1.35)

        The random point can be moved to lie on the circle of radius
        1 centered on p1:

        >>> c = p.p1 + (r - p.p1).unit
        >>> c.distance(p.p1).equals(1)
        True
        """
    def parameter_value(self, other, u, v: Incomplete | None = None):
        """Return the parameter(s) corresponding to the given point.

        Examples
        ========

        >>> from sympy import pi, Plane
        >>> from sympy.abc import t, u, v
        >>> p = Plane((2, 0, 0), (0, 0, 1), (0, 1, 0))

        By default, the parameter value returned defines a point
        that is a distance of 1 from the Plane's p1 value and
        in line with the given point:

        >>> on_circle = p.arbitrary_point(t).subs(t, pi/4)
        >>> on_circle.distance(p.p1)
        1
        >>> p.parameter_value(on_circle, t)
        {t: pi/4}

        Moving the point twice as far from p1 does not change
        the parameter value:

        >>> off_circle = p.p1 + (on_circle - p.p1)*2
        >>> off_circle.distance(p.p1)
        2
        >>> p.parameter_value(off_circle, t)
        {t: pi/4}

        If the 2-value parameter is desired, supply the two
        parameter symbols and a replacement dictionary will
        be returned:

        >>> p.parameter_value(on_circle, u, v)
        {u: sqrt(10)/10, v: sqrt(10)/30}
        >>> p.parameter_value(off_circle, u, v)
        {u: sqrt(10)/5, v: sqrt(10)/15}
        """
    @property
    def ambient_dimension(self): ...
