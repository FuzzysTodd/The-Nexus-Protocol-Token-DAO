from .entity import GeometryEntity as GeometryEntity, GeometrySet as GeometrySet
from .exceptions import GeometryError as GeometryError
from .point import Point as Point, Point3D as Point3D
from .util import find as find, intersection as intersection
from _typeshed import Incomplete
from sympy.core.containers import Tuple as Tuple
from sympy.core.evalf import N as N
from sympy.core.expr import Expr as Expr
from sympy.core.numbers import Float as Float, Rational as Rational, oo as oo
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, uniquely_named_symbol as uniquely_named_symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import acos as acos, atan2 as atan2, tan as tan
from sympy.logic.boolalg import And as And
from sympy.matrices import Matrix as Matrix
from sympy.sets.sets import Intersection as Intersection
from sympy.simplify.simplify import simplify as simplify
from sympy.solvers.solvers import solve as solve
from sympy.solvers.solveset import linear_coeffs as linear_coeffs
from sympy.utilities.misc import Undecidable as Undecidable, filldedent as filldedent

t: Incomplete
u: Incomplete

class LinearEntity(GeometrySet):
    """A base class for all linear entities (Line, Ray and Segment)
    in n-dimensional Euclidean space.

    Attributes
    ==========

    ambient_dimension
    direction
    length
    p1
    p2
    points

    Notes
    =====

    This is an abstract class and is not meant to be instantiated.

    See Also
    ========

    sympy.geometry.entity.GeometryEntity

    """
    def __new__(cls, p1, p2: Incomplete | None = None, **kwargs): ...
    def __contains__(self, other) -> bool:
        """Return a definitive answer or else raise an error if it cannot
        be determined that other is on the boundaries of self."""
    @property
    def ambient_dimension(self):
        """A property method that returns the dimension of LinearEntity
        object.

        Parameters
        ==========

        p1 : LinearEntity

        Returns
        =======

        dimension : integer

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(1, 1)
        >>> l1 = Line(p1, p2)
        >>> l1.ambient_dimension
        2

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0, 0), Point(1, 1, 1)
        >>> l1 = Line(p1, p2)
        >>> l1.ambient_dimension
        3

        """
    def angle_between(l1, l2):
        """Return the non-reflex angle formed by rays emanating from
        the origin with directions the same as the direction vectors
        of the linear entities.

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        angle : angle in radians

        Notes
        =====

        From the dot product of vectors v1 and v2 it is known that:

            ``dot(v1, v2) = |v1|*|v2|*cos(A)``

        where A is the angle formed between the two vectors. We can
        get the directional vectors of the two lines and readily
        find the angle between the two using the above formula.

        See Also
        ========

        is_perpendicular, Ray2D.closing_angle

        Examples
        ========

        >>> from sympy import Line
        >>> e = Line((0, 0), (1, 0))
        >>> ne = Line((0, 0), (1, 1))
        >>> sw = Line((1, 1), (0, 0))
        >>> ne.angle_between(e)
        pi/4
        >>> sw.angle_between(e)
        3*pi/4

        To obtain the non-obtuse angle at the intersection of lines, use
        the ``smallest_angle_between`` method:

        >>> sw.smallest_angle_between(e)
        pi/4

        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(-1, 2, 0)
        >>> l1, l2 = Line3D(p1, p2), Line3D(p2, p3)
        >>> l1.angle_between(l2)
        acos(-sqrt(2)/3)
        >>> l1.smallest_angle_between(l2)
        acos(sqrt(2)/3)
        """
    def smallest_angle_between(l1, l2):
        """Return the smallest angle formed at the intersection of the
        lines containing the linear entities.

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        angle : angle in radians

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(0, 4), Point(2, -2)
        >>> l1, l2 = Line(p1, p2), Line(p1, p3)
        >>> l1.smallest_angle_between(l2)
        pi/4

        See Also
        ========

        angle_between, is_perpendicular, Ray2D.closing_angle
        """
    def arbitrary_point(self, parameter: str = 't'):
        """A parameterized point on the Line.

        Parameters
        ==========

        parameter : str, optional
            The name of the parameter which will be used for the parametric
            point. The default value is 't'. When this parameter is 0, the
            first point used to define the line will be returned, and when
            it is 1 the second point will be returned.

        Returns
        =======

        point : Point

        Raises
        ======

        ValueError
            When ``parameter`` already appears in the Line's definition.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(1, 0), Point(5, 3)
        >>> l1 = Line(p1, p2)
        >>> l1.arbitrary_point()
        Point2D(4*t + 1, 3*t)
        >>> from sympy import Point3D, Line3D
        >>> p1, p2 = Point3D(1, 0, 0), Point3D(5, 3, 1)
        >>> l1 = Line3D(p1, p2)
        >>> l1.arbitrary_point()
        Point3D(4*t + 1, 3*t, t)

        """
    @staticmethod
    def are_concurrent(*lines):
        """Is a sequence of linear entities concurrent?

        Two or more linear entities are concurrent if they all
        intersect at a single point.

        Parameters
        ==========

        lines
            A sequence of linear entities.

        Returns
        =======

        True : if the set of linear entities intersect in one point
        False : otherwise.

        See Also
        ========

        sympy.geometry.util.intersection

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(3, 5)
        >>> p3, p4 = Point(-2, -2), Point(0, 2)
        >>> l1, l2, l3 = Line(p1, p2), Line(p1, p3), Line(p1, p4)
        >>> Line.are_concurrent(l1, l2, l3)
        True
        >>> l4 = Line(p2, p3)
        >>> Line.are_concurrent(l2, l3, l4)
        False
        >>> from sympy import Point3D, Line3D
        >>> p1, p2 = Point3D(0, 0, 0), Point3D(3, 5, 2)
        >>> p3, p4 = Point3D(-2, -2, -2), Point3D(0, 2, 1)
        >>> l1, l2, l3 = Line3D(p1, p2), Line3D(p1, p3), Line3D(p1, p4)
        >>> Line3D.are_concurrent(l1, l2, l3)
        True
        >>> l4 = Line3D(p2, p3)
        >>> Line3D.are_concurrent(l2, l3, l4)
        False

        """
    def contains(self, other) -> None:
        """Subclasses should implement this method and should return
            True if other is on the boundaries of self;
            False if not on the boundaries of self;
            None if a determination cannot be made."""
    @property
    def direction(self):
        """The direction vector of the LinearEntity.

        Returns
        =======

        p : a Point; the ray from the origin to this point is the
            direction of `self`

        Examples
        ========

        >>> from sympy import Line
        >>> a, b = (1, 1), (1, 3)
        >>> Line(a, b).direction
        Point2D(0, 2)
        >>> Line(b, a).direction
        Point2D(0, -2)

        This can be reported so the distance from the origin is 1:

        >>> Line(b, a).direction.unit
        Point2D(0, -1)

        See Also
        ========

        sympy.geometry.point.Point.unit

        """
    def intersection(self, other):
        """The intersection with another geometrical entity.

        Parameters
        ==========

        o : Point or LinearEntity

        Returns
        =======

        intersection : list of geometrical entities

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line, Segment
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(7, 7)
        >>> l1 = Line(p1, p2)
        >>> l1.intersection(p3)
        [Point2D(7, 7)]
        >>> p4, p5 = Point(5, 0), Point(0, 3)
        >>> l2 = Line(p4, p5)
        >>> l1.intersection(l2)
        [Point2D(15/8, 15/8)]
        >>> p6, p7 = Point(0, 5), Point(2, 6)
        >>> s1 = Segment(p6, p7)
        >>> l1.intersection(s1)
        []
        >>> from sympy import Point3D, Line3D, Segment3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(7, 7, 7)
        >>> l1 = Line3D(p1, p2)
        >>> l1.intersection(p3)
        [Point3D(7, 7, 7)]
        >>> l1 = Line3D(Point3D(4,19,12), Point3D(5,25,17))
        >>> l2 = Line3D(Point3D(-3, -15, -19), direction_ratio=[2,8,8])
        >>> l1.intersection(l2)
        [Point3D(1, 1, -3)]
        >>> p6, p7 = Point3D(0, 5, 2), Point3D(2, 6, 3)
        >>> s1 = Segment3D(p6, p7)
        >>> l1.intersection(s1)
        []

        """
    def is_parallel(l1, l2):
        """Are two linear entities parallel?

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        True : if l1 and l2 are parallel,
        False : otherwise.

        See Also
        ========

        coefficients

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(1, 1)
        >>> p3, p4 = Point(3, 4), Point(6, 7)
        >>> l1, l2 = Line(p1, p2), Line(p3, p4)
        >>> Line.is_parallel(l1, l2)
        True
        >>> p5 = Point(6, 6)
        >>> l3 = Line(p3, p5)
        >>> Line.is_parallel(l1, l3)
        False
        >>> from sympy import Point3D, Line3D
        >>> p1, p2 = Point3D(0, 0, 0), Point3D(3, 4, 5)
        >>> p3, p4 = Point3D(2, 1, 1), Point3D(8, 9, 11)
        >>> l1, l2 = Line3D(p1, p2), Line3D(p3, p4)
        >>> Line3D.is_parallel(l1, l2)
        True
        >>> p5 = Point3D(6, 6, 6)
        >>> l3 = Line3D(p3, p5)
        >>> Line3D.is_parallel(l1, l3)
        False

        """
    def is_perpendicular(l1, l2):
        """Are two linear entities perpendicular?

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        True : if l1 and l2 are perpendicular,
        False : otherwise.

        See Also
        ========

        coefficients

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(-1, 1)
        >>> l1, l2 = Line(p1, p2), Line(p1, p3)
        >>> l1.is_perpendicular(l2)
        True
        >>> p4 = Point(5, 3)
        >>> l3 = Line(p1, p4)
        >>> l1.is_perpendicular(l3)
        False
        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(-1, 2, 0)
        >>> l1, l2 = Line3D(p1, p2), Line3D(p2, p3)
        >>> l1.is_perpendicular(l2)
        False
        >>> p4 = Point3D(5, 3, 7)
        >>> l3 = Line3D(p1, p4)
        >>> l1.is_perpendicular(l3)
        False

        """
    def is_similar(self, other):
        """
        Return True if self and other are contained in the same line.

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 1), Point(3, 4), Point(2, 3)
        >>> l1 = Line(p1, p2)
        >>> l2 = Line(p1, p3)
        >>> l1.is_similar(l2)
        True
        """
    @property
    def length(self):
        """
        The length of the line.

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(3, 5)
        >>> l1 = Line(p1, p2)
        >>> l1.length
        oo
        """
    @property
    def p1(self):
        """The first defining point of a linear entity.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> l = Line(p1, p2)
        >>> l.p1
        Point2D(0, 0)

        """
    @property
    def p2(self):
        """The second defining point of a linear entity.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> l = Line(p1, p2)
        >>> l.p2
        Point2D(5, 3)

        """
    def parallel_line(self, p):
        """Create a new Line parallel to this linear entity which passes
        through the point `p`.

        Parameters
        ==========

        p : Point

        Returns
        =======

        line : Line

        See Also
        ========

        is_parallel

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(2, 3), Point(-2, 2)
        >>> l1 = Line(p1, p2)
        >>> l2 = l1.parallel_line(p3)
        >>> p3 in l2
        True
        >>> l1.is_parallel(l2)
        True
        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(2, 3, 4), Point3D(-2, 2, 0)
        >>> l1 = Line3D(p1, p2)
        >>> l2 = l1.parallel_line(p3)
        >>> p3 in l2
        True
        >>> l1.is_parallel(l2)
        True

        """
    def perpendicular_line(self, p):
        """Create a new Line perpendicular to this linear entity which passes
        through the point `p`.

        Parameters
        ==========

        p : Point

        Returns
        =======

        line : Line

        See Also
        ========

        sympy.geometry.line.LinearEntity.is_perpendicular, perpendicular_segment

        Examples
        ========

        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(2, 3, 4), Point3D(-2, 2, 0)
        >>> L = Line3D(p1, p2)
        >>> P = L.perpendicular_line(p3); P
        Line3D(Point3D(-2, 2, 0), Point3D(4/29, 6/29, 8/29))
        >>> L.is_perpendicular(P)
        True

        In 3D the, the first point used to define the line is the point
        through which the perpendicular was required to pass; the
        second point is (arbitrarily) contained in the given line:

        >>> P.p2 in L
        True
        """
    def perpendicular_segment(self, p):
        """Create a perpendicular line segment from `p` to this line.

        The endpoints of the segment are ``p`` and the closest point in
        the line containing self. (If self is not a line, the point might
        not be in self.)

        Parameters
        ==========

        p : Point

        Returns
        =======

        segment : Segment

        Notes
        =====

        Returns `p` itself if `p` is on this linear entity.

        See Also
        ========

        perpendicular_line

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(0, 2)
        >>> l1 = Line(p1, p2)
        >>> s1 = l1.perpendicular_segment(p3)
        >>> l1.is_perpendicular(s1)
        True
        >>> p3 in s1
        True
        >>> l1.perpendicular_segment(Point(4, 0))
        Segment2D(Point2D(4, 0), Point2D(2, 2))
        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(0, 2, 0)
        >>> l1 = Line3D(p1, p2)
        >>> s1 = l1.perpendicular_segment(p3)
        >>> l1.is_perpendicular(s1)
        True
        >>> p3 in s1
        True
        >>> l1.perpendicular_segment(Point3D(4, 0, 0))
        Segment3D(Point3D(4, 0, 0), Point3D(4/3, 4/3, 4/3))

        """
    @property
    def points(self):
        """The two points used to define this linear entity.

        Returns
        =======

        points : tuple of Points

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(5, 11)
        >>> l1 = Line(p1, p2)
        >>> l1.points
        (Point2D(0, 0), Point2D(5, 11))

        """
    def projection(self, other):
        """Project a point, line, ray, or segment onto this linear entity.

        Parameters
        ==========

        other : Point or LinearEntity (Line, Ray, Segment)

        Returns
        =======

        projection : Point or LinearEntity (Line, Ray, Segment)
            The return type matches the type of the parameter ``other``.

        Raises
        ======

        GeometryError
            When method is unable to perform projection.

        Notes
        =====

        A projection involves taking the two points that define
        the linear entity and projecting those points onto a
        Line and then reforming the linear entity using these
        projections.
        A point P is projected onto a line L by finding the point
        on L that is closest to P. This point is the intersection
        of L and the line perpendicular to L that passes through P.

        See Also
        ========

        sympy.geometry.point.Point, perpendicular_line

        Examples
        ========

        >>> from sympy import Point, Line, Segment, Rational
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(Rational(1, 2), 0)
        >>> l1 = Line(p1, p2)
        >>> l1.projection(p3)
        Point2D(1/4, 1/4)
        >>> p4, p5 = Point(10, 0), Point(12, 1)
        >>> s1 = Segment(p4, p5)
        >>> l1.projection(s1)
        Segment2D(Point2D(5, 5), Point2D(13/2, 13/2))
        >>> p1, p2, p3 = Point(0, 0, 1), Point(1, 1, 2), Point(2, 0, 1)
        >>> l1 = Line(p1, p2)
        >>> l1.projection(p3)
        Point3D(2/3, 2/3, 5/3)
        >>> p4, p5 = Point(10, 0, 1), Point(12, 1, 3)
        >>> s1 = Segment(p4, p5)
        >>> l1.projection(s1)
        Segment3D(Point3D(10/3, 10/3, 13/3), Point3D(5, 5, 6))

        """
    def random_point(self, seed: Incomplete | None = None):
        """A random point on a LinearEntity.

        Returns
        =======

        point : Point

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line, Ray, Segment
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> line = Line(p1, p2)
        >>> r = line.random_point(seed=42)  # seed value is optional
        >>> r.n(3)
        Point2D(-0.72, -0.432)
        >>> r in line
        True
        >>> Ray(p1, p2).random_point(seed=42).n(3)
        Point2D(0.72, 0.432)
        >>> Segment(p1, p2).random_point(seed=42).n(3)
        Point2D(3.2, 1.92)

        """
    def bisectors(self, other):
        """Returns the perpendicular lines which pass through the intersections
        of self and other that are in the same plane.

        Parameters
        ==========

        line : Line3D

        Returns
        =======

        list: two Line instances

        Examples
        ========

        >>> from sympy import Point3D, Line3D
        >>> r1 = Line3D(Point3D(0, 0, 0), Point3D(1, 0, 0))
        >>> r2 = Line3D(Point3D(0, 0, 0), Point3D(0, 1, 0))
        >>> r1.bisectors(r2)
        [Line3D(Point3D(0, 0, 0), Point3D(1, 1, 0)), Line3D(Point3D(0, 0, 0), Point3D(1, -1, 0))]

        """

class Line(LinearEntity):
    """An infinite line in space.

    A 2D line is declared with two distinct points, point and slope, or
    an equation. A 3D line may be defined with a point and a direction ratio.

    Parameters
    ==========

    p1 : Point
    p2 : Point
    slope : SymPy expression
    direction_ratio : list
    equation : equation of a line

    Notes
    =====

    `Line` will automatically subclass to `Line2D` or `Line3D` based
    on the dimension of `p1`.  The `slope` argument is only relevant
    for `Line2D` and the `direction_ratio` argument is only relevant
    for `Line3D`.

    The order of the points will define the direction of the line
    which is used when calculating the angle between lines.

    See Also
    ========

    sympy.geometry.point.Point
    sympy.geometry.line.Line2D
    sympy.geometry.line.Line3D

    Examples
    ========

    >>> from sympy import Line, Segment, Point, Eq
    >>> from sympy.abc import x, y, a, b

    >>> L = Line(Point(2,3), Point(3,5))
    >>> L
    Line2D(Point2D(2, 3), Point2D(3, 5))
    >>> L.points
    (Point2D(2, 3), Point2D(3, 5))
    >>> L.equation()
    -2*x + y + 1
    >>> L.coefficients
    (-2, 1, 1)

    Instantiate with keyword ``slope``:

    >>> Line(Point(0, 0), slope=0)
    Line2D(Point2D(0, 0), Point2D(1, 0))

    Instantiate with another linear object

    >>> s = Segment((0, 0), (0, 1))
    >>> Line(s).equation()
    x

    The line corresponding to an equation in the for `ax + by + c = 0`,
    can be entered:

    >>> Line(3*x + y + 18)
    Line2D(Point2D(0, -18), Point2D(1, -21))

    If `x` or `y` has a different name, then they can be specified, too,
    as a string (to match the name) or symbol:

    >>> Line(Eq(3*a + b, -18), x='a', y=b)
    Line2D(Point2D(0, -18), Point2D(1, -21))
    """
    def __new__(cls, *args, **kwargs): ...
    def contains(self, other):
        """
        Return True if `other` is on this Line, or False otherwise.

        Examples
        ========

        >>> from sympy import Line,Point
        >>> p1, p2 = Point(0, 1), Point(3, 4)
        >>> l = Line(p1, p2)
        >>> l.contains(p1)
        True
        >>> l.contains((0, 1))
        True
        >>> l.contains((0, 0))
        False
        >>> a = (0, 0, 0)
        >>> b = (1, 1, 1)
        >>> c = (2, 2, 2)
        >>> l1 = Line(a, b)
        >>> l2 = Line(b, a)
        >>> l1 == l2
        False
        >>> l1 in l2
        True

        """
    def distance(self, other):
        """
        Finds the shortest distance between a line and a point.

        Raises
        ======

        NotImplementedError is raised if `other` is not a Point

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(1, 1)
        >>> s = Line(p1, p2)
        >>> s.distance(Point(-1, 1))
        sqrt(2)
        >>> s.distance((-1, 2))
        3*sqrt(2)/2
        >>> p1, p2 = Point(0, 0, 0), Point(1, 1, 1)
        >>> s = Line(p1, p2)
        >>> s.distance(Point(-1, 1, 1))
        2*sqrt(6)/3
        >>> s.distance((-1, 1, 1))
        2*sqrt(6)/3

        """
    def equals(self, other):
        """Returns True if self and other are the same mathematical entities"""
    def plot_interval(self, parameter: str = 't'):
        """The plot interval for the default geometric plot of line. Gives
        values that will produce a line that is +/- 5 units long (where a
        unit is the distance between the two points that define the line).

        Parameters
        ==========

        parameter : str, optional
            Default value is 't'.

        Returns
        =======

        plot_interval : list (plot interval)
            [parameter, lower_bound, upper_bound]

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> l1 = Line(p1, p2)
        >>> l1.plot_interval()
        [t, -5, 5]

        """

class Ray(LinearEntity):
    """A Ray is a semi-line in the space with a source point and a direction.

    Parameters
    ==========

    p1 : Point
        The source of the Ray
    p2 : Point or radian value
        This point determines the direction in which the Ray propagates.
        If given as an angle it is interpreted in radians with the positive
        direction being ccw.

    Attributes
    ==========

    source

    See Also
    ========

    sympy.geometry.line.Ray2D
    sympy.geometry.line.Ray3D
    sympy.geometry.point.Point
    sympy.geometry.line.Line

    Notes
    =====

    `Ray` will automatically subclass to `Ray2D` or `Ray3D` based on the
    dimension of `p1`.

    Examples
    ========

    >>> from sympy import Ray, Point, pi
    >>> r = Ray(Point(2, 3), Point(3, 5))
    >>> r
    Ray2D(Point2D(2, 3), Point2D(3, 5))
    >>> r.points
    (Point2D(2, 3), Point2D(3, 5))
    >>> r.source
    Point2D(2, 3)
    >>> r.xdirection
    oo
    >>> r.ydirection
    oo
    >>> r.slope
    2
    >>> Ray(Point(0, 0), angle=pi/4).slope
    1

    """
    def __new__(cls, p1, p2: Incomplete | None = None, **kwargs): ...
    def contains(self, other):
        """
        Is other GeometryEntity contained in this Ray?

        Examples
        ========

        >>> from sympy import Ray,Point,Segment
        >>> p1, p2 = Point(0, 0), Point(4, 4)
        >>> r = Ray(p1, p2)
        >>> r.contains(p1)
        True
        >>> r.contains((1, 1))
        True
        >>> r.contains((1, 3))
        False
        >>> s = Segment((1, 1), (2, 2))
        >>> r.contains(s)
        True
        >>> s = Segment((1, 2), (2, 5))
        >>> r.contains(s)
        False
        >>> r1 = Ray((2, 2), (3, 3))
        >>> r.contains(r1)
        True
        >>> r1 = Ray((2, 2), (3, 5))
        >>> r.contains(r1)
        False
        """
    def distance(self, other):
        """
        Finds the shortest distance between the ray and a point.

        Raises
        ======

        NotImplementedError is raised if `other` is not a Point

        Examples
        ========

        >>> from sympy import Point, Ray
        >>> p1, p2 = Point(0, 0), Point(1, 1)
        >>> s = Ray(p1, p2)
        >>> s.distance(Point(-1, -1))
        sqrt(2)
        >>> s.distance((-1, 2))
        3*sqrt(2)/2
        >>> p1, p2 = Point(0, 0, 0), Point(1, 1, 2)
        >>> s = Ray(p1, p2)
        >>> s
        Ray3D(Point3D(0, 0, 0), Point3D(1, 1, 2))
        >>> s.distance(Point(-1, -1, 2))
        4*sqrt(3)/3
        >>> s.distance((-1, -1, 2))
        4*sqrt(3)/3

        """
    def equals(self, other):
        """Returns True if self and other are the same mathematical entities"""
    def plot_interval(self, parameter: str = 't'):
        """The plot interval for the default geometric plot of the Ray. Gives
        values that will produce a ray that is 10 units long (where a unit is
        the distance between the two points that define the ray).

        Parameters
        ==========

        parameter : str, optional
            Default value is 't'.

        Returns
        =======

        plot_interval : list
            [parameter, lower_bound, upper_bound]

        Examples
        ========

        >>> from sympy import Ray, pi
        >>> r = Ray((0, 0), angle=pi/4)
        >>> r.plot_interval()
        [t, 0, 10]

        """
    @property
    def source(self):
        """The point from which the ray emanates.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Ray
        >>> p1, p2 = Point(0, 0), Point(4, 1)
        >>> r1 = Ray(p1, p2)
        >>> r1.source
        Point2D(0, 0)
        >>> p1, p2 = Point(0, 0, 0), Point(4, 1, 5)
        >>> r1 = Ray(p2, p1)
        >>> r1.source
        Point3D(4, 1, 5)

        """

class Segment(LinearEntity):
    """A line segment in space.

    Parameters
    ==========

    p1 : Point
    p2 : Point

    Attributes
    ==========

    length : number or SymPy expression
    midpoint : Point

    See Also
    ========

    sympy.geometry.line.Segment2D
    sympy.geometry.line.Segment3D
    sympy.geometry.point.Point
    sympy.geometry.line.Line

    Notes
    =====

    If 2D or 3D points are used to define `Segment`, it will
    be automatically subclassed to `Segment2D` or `Segment3D`.

    Examples
    ========

    >>> from sympy import Point, Segment
    >>> Segment((1, 0), (1, 1)) # tuples are interpreted as pts
    Segment2D(Point2D(1, 0), Point2D(1, 1))
    >>> s = Segment(Point(4, 3), Point(1, 1))
    >>> s.points
    (Point2D(4, 3), Point2D(1, 1))
    >>> s.slope
    2/3
    >>> s.length
    sqrt(13)
    >>> s.midpoint
    Point2D(5/2, 2)
    >>> Segment((1, 0, 0), (1, 1, 1)) # tuples are interpreted as pts
    Segment3D(Point3D(1, 0, 0), Point3D(1, 1, 1))
    >>> s = Segment(Point(4, 3, 9), Point(1, 1, 7)); s
    Segment3D(Point3D(4, 3, 9), Point3D(1, 1, 7))
    >>> s.points
    (Point3D(4, 3, 9), Point3D(1, 1, 7))
    >>> s.length
    sqrt(17)
    >>> s.midpoint
    Point3D(5/2, 2, 8)

    """
    def __new__(cls, p1, p2, **kwargs): ...
    def contains(self, other):
        """
        Is the other GeometryEntity contained within this Segment?

        Examples
        ========

        >>> from sympy import Point, Segment
        >>> p1, p2 = Point(0, 1), Point(3, 4)
        >>> s = Segment(p1, p2)
        >>> s2 = Segment(p2, p1)
        >>> s.contains(s2)
        True
        >>> from sympy import Point3D, Segment3D
        >>> p1, p2 = Point3D(0, 1, 1), Point3D(3, 4, 5)
        >>> s = Segment3D(p1, p2)
        >>> s2 = Segment3D(p2, p1)
        >>> s.contains(s2)
        True
        >>> s.contains((p1 + p2)/2)
        True
        """
    def equals(self, other):
        """Returns True if self and other are the same mathematical entities"""
    def distance(self, other):
        """
        Finds the shortest distance between a line segment and a point.

        Raises
        ======

        NotImplementedError is raised if `other` is not a Point

        Examples
        ========

        >>> from sympy import Point, Segment
        >>> p1, p2 = Point(0, 1), Point(3, 4)
        >>> s = Segment(p1, p2)
        >>> s.distance(Point(10, 15))
        sqrt(170)
        >>> s.distance((0, 12))
        sqrt(73)
        >>> from sympy import Point3D, Segment3D
        >>> p1, p2 = Point3D(0, 0, 3), Point3D(1, 1, 4)
        >>> s = Segment3D(p1, p2)
        >>> s.distance(Point3D(10, 15, 12))
        sqrt(341)
        >>> s.distance((10, 15, 12))
        sqrt(341)
        """
    @property
    def length(self):
        """The length of the line segment.

        See Also
        ========

        sympy.geometry.point.Point.distance

        Examples
        ========

        >>> from sympy import Point, Segment
        >>> p1, p2 = Point(0, 0), Point(4, 3)
        >>> s1 = Segment(p1, p2)
        >>> s1.length
        5
        >>> from sympy import Point3D, Segment3D
        >>> p1, p2 = Point3D(0, 0, 0), Point3D(4, 3, 3)
        >>> s1 = Segment3D(p1, p2)
        >>> s1.length
        sqrt(34)

        """
    @property
    def midpoint(self):
        """The midpoint of the line segment.

        See Also
        ========

        sympy.geometry.point.Point.midpoint

        Examples
        ========

        >>> from sympy import Point, Segment
        >>> p1, p2 = Point(0, 0), Point(4, 3)
        >>> s1 = Segment(p1, p2)
        >>> s1.midpoint
        Point2D(2, 3/2)
        >>> from sympy import Point3D, Segment3D
        >>> p1, p2 = Point3D(0, 0, 0), Point3D(4, 3, 3)
        >>> s1 = Segment3D(p1, p2)
        >>> s1.midpoint
        Point3D(2, 3/2, 3/2)

        """
    def perpendicular_bisector(self, p: Incomplete | None = None):
        """The perpendicular bisector of this segment.

        If no point is specified or the point specified is not on the
        bisector then the bisector is returned as a Line. Otherwise a
        Segment is returned that joins the point specified and the
        intersection of the bisector and the segment.

        Parameters
        ==========

        p : Point

        Returns
        =======

        bisector : Line or Segment

        See Also
        ========

        LinearEntity.perpendicular_segment

        Examples
        ========

        >>> from sympy import Point, Segment
        >>> p1, p2, p3 = Point(0, 0), Point(6, 6), Point(5, 1)
        >>> s1 = Segment(p1, p2)
        >>> s1.perpendicular_bisector()
        Line2D(Point2D(3, 3), Point2D(-3, 9))

        >>> s1.perpendicular_bisector(p3)
        Segment2D(Point2D(5, 1), Point2D(3, 3))

        """
    def plot_interval(self, parameter: str = 't'):
        """The plot interval for the default geometric plot of the Segment gives
        values that will produce the full segment in a plot.

        Parameters
        ==========

        parameter : str, optional
            Default value is 't'.

        Returns
        =======

        plot_interval : list
            [parameter, lower_bound, upper_bound]

        Examples
        ========

        >>> from sympy import Point, Segment
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> s1 = Segment(p1, p2)
        >>> s1.plot_interval()
        [t, 0, 1]

        """

class LinearEntity2D(LinearEntity):
    """A base class for all linear entities (line, ray and segment)
    in a 2-dimensional Euclidean space.

    Attributes
    ==========

    p1
    p2
    coefficients
    slope
    points

    Notes
    =====

    This is an abstract class and is not meant to be instantiated.

    See Also
    ========

    sympy.geometry.entity.GeometryEntity

    """
    @property
    def bounds(self):
        """Return a tuple (xmin, ymin, xmax, ymax) representing the bounding
        rectangle for the geometric figure.

        """
    def perpendicular_line(self, p):
        """Create a new Line perpendicular to this linear entity which passes
        through the point `p`.

        Parameters
        ==========

        p : Point

        Returns
        =======

        line : Line

        See Also
        ========

        sympy.geometry.line.LinearEntity.is_perpendicular, perpendicular_segment

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(2, 3), Point(-2, 2)
        >>> L = Line(p1, p2)
        >>> P = L.perpendicular_line(p3); P
        Line2D(Point2D(-2, 2), Point2D(-5, 4))
        >>> L.is_perpendicular(P)
        True

        In 2D, the first point of the perpendicular line is the
        point through which was required to pass; the second
        point is arbitrarily chosen. To get a line that explicitly
        uses a point in the line, create a line from the perpendicular
        segment from the line to the point:

        >>> Line(L.perpendicular_segment(p3))
        Line2D(Point2D(-2, 2), Point2D(4/13, 6/13))
        """
    @property
    def slope(self):
        """The slope of this linear entity, or infinity if vertical.

        Returns
        =======

        slope : number or SymPy expression

        See Also
        ========

        coefficients

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(3, 5)
        >>> l1 = Line(p1, p2)
        >>> l1.slope
        5/3

        >>> p3 = Point(0, 4)
        >>> l2 = Line(p1, p3)
        >>> l2.slope
        oo

        """

class Line2D(LinearEntity2D, Line):
    """An infinite line in space 2D.

    A line is declared with two distinct points or a point and slope
    as defined using keyword `slope`.

    Parameters
    ==========

    p1 : Point
    pt : Point
    slope : SymPy expression

    See Also
    ========

    sympy.geometry.point.Point

    Examples
    ========

    >>> from sympy import Line, Segment, Point
    >>> L = Line(Point(2,3), Point(3,5))
    >>> L
    Line2D(Point2D(2, 3), Point2D(3, 5))
    >>> L.points
    (Point2D(2, 3), Point2D(3, 5))
    >>> L.equation()
    -2*x + y + 1
    >>> L.coefficients
    (-2, 1, 1)

    Instantiate with keyword ``slope``:

    >>> Line(Point(0, 0), slope=0)
    Line2D(Point2D(0, 0), Point2D(1, 0))

    Instantiate with another linear object

    >>> s = Segment((0, 0), (0, 1))
    >>> Line(s).equation()
    x
    """
    def __new__(cls, p1, pt: Incomplete | None = None, slope: Incomplete | None = None, **kwargs): ...
    @property
    def coefficients(self):
        """The coefficients (`a`, `b`, `c`) for `ax + by + c = 0`.

        See Also
        ========

        sympy.geometry.line.Line2D.equation

        Examples
        ========

        >>> from sympy import Point, Line
        >>> from sympy.abc import x, y
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> l = Line(p1, p2)
        >>> l.coefficients
        (-3, 5, 0)

        >>> p3 = Point(x, y)
        >>> l2 = Line(p1, p3)
        >>> l2.coefficients
        (-y, x, 0)

        """
    def equation(self, x: str = 'x', y: str = 'y'):
        """The equation of the line: ax + by + c.

        Parameters
        ==========

        x : str, optional
            The name to use for the x-axis, default value is 'x'.
        y : str, optional
            The name to use for the y-axis, default value is 'y'.

        Returns
        =======

        equation : SymPy expression

        See Also
        ========

        sympy.geometry.line.Line2D.coefficients

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(1, 0), Point(5, 3)
        >>> l1 = Line(p1, p2)
        >>> l1.equation()
        -3*x + 4*y + 3

        """

class Ray2D(LinearEntity2D, Ray):
    """
    A Ray is a semi-line in the space with a source point and a direction.

    Parameters
    ==========

    p1 : Point
        The source of the Ray
    p2 : Point or radian value
        This point determines the direction in which the Ray propagates.
        If given as an angle it is interpreted in radians with the positive
        direction being ccw.

    Attributes
    ==========

    source
    xdirection
    ydirection

    See Also
    ========

    sympy.geometry.point.Point, Line

    Examples
    ========

    >>> from sympy import Point, pi, Ray
    >>> r = Ray(Point(2, 3), Point(3, 5))
    >>> r
    Ray2D(Point2D(2, 3), Point2D(3, 5))
    >>> r.points
    (Point2D(2, 3), Point2D(3, 5))
    >>> r.source
    Point2D(2, 3)
    >>> r.xdirection
    oo
    >>> r.ydirection
    oo
    >>> r.slope
    2
    >>> Ray(Point(0, 0), angle=pi/4).slope
    1

    """
    def __new__(cls, p1, pt: Incomplete | None = None, angle: Incomplete | None = None, **kwargs): ...
    @property
    def xdirection(self):
        """The x direction of the ray.

        Positive infinity if the ray points in the positive x direction,
        negative infinity if the ray points in the negative x direction,
        or 0 if the ray is vertical.

        See Also
        ========

        ydirection

        Examples
        ========

        >>> from sympy import Point, Ray
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(0, -1)
        >>> r1, r2 = Ray(p1, p2), Ray(p1, p3)
        >>> r1.xdirection
        oo
        >>> r2.xdirection
        0

        """
    @property
    def ydirection(self):
        """The y direction of the ray.

        Positive infinity if the ray points in the positive y direction,
        negative infinity if the ray points in the negative y direction,
        or 0 if the ray is horizontal.

        See Also
        ========

        xdirection

        Examples
        ========

        >>> from sympy import Point, Ray
        >>> p1, p2, p3 = Point(0, 0), Point(-1, -1), Point(-1, 0)
        >>> r1, r2 = Ray(p1, p2), Ray(p1, p3)
        >>> r1.ydirection
        -oo
        >>> r2.ydirection
        0

        """
    def closing_angle(r1, r2):
        """Return the angle by which r2 must be rotated so it faces the same
        direction as r1.

        Parameters
        ==========

        r1 : Ray2D
        r2 : Ray2D

        Returns
        =======

        angle : angle in radians (ccw angle is positive)

        See Also
        ========

        LinearEntity.angle_between

        Examples
        ========

        >>> from sympy import Ray, pi
        >>> r1 = Ray((0, 0), (1, 0))
        >>> r2 = r1.rotate(-pi/2)
        >>> angle = r1.closing_angle(r2); angle
        pi/2
        >>> r2.rotate(angle).direction.unit == r1.direction.unit
        True
        >>> r2.closing_angle(r1)
        -pi/2
        """

class Segment2D(LinearEntity2D, Segment):
    """A line segment in 2D space.

    Parameters
    ==========

    p1 : Point
    p2 : Point

    Attributes
    ==========

    length : number or SymPy expression
    midpoint : Point

    See Also
    ========

    sympy.geometry.point.Point, Line

    Examples
    ========

    >>> from sympy import Point, Segment
    >>> Segment((1, 0), (1, 1)) # tuples are interpreted as pts
    Segment2D(Point2D(1, 0), Point2D(1, 1))
    >>> s = Segment(Point(4, 3), Point(1, 1)); s
    Segment2D(Point2D(4, 3), Point2D(1, 1))
    >>> s.points
    (Point2D(4, 3), Point2D(1, 1))
    >>> s.slope
    2/3
    >>> s.length
    sqrt(13)
    >>> s.midpoint
    Point2D(5/2, 2)

    """
    def __new__(cls, p1, p2, **kwargs): ...

class LinearEntity3D(LinearEntity):
    """An base class for all linear entities (line, ray and segment)
    in a 3-dimensional Euclidean space.

    Attributes
    ==========

    p1
    p2
    direction_ratio
    direction_cosine
    points

    Notes
    =====

    This is a base class and is not meant to be instantiated.
    """
    def __new__(cls, p1, p2, **kwargs): ...
    ambient_dimension: int
    @property
    def direction_ratio(self):
        """The direction ratio of a given line in 3D.

        See Also
        ========

        sympy.geometry.line.Line3D.equation

        Examples
        ========

        >>> from sympy import Point3D, Line3D
        >>> p1, p2 = Point3D(0, 0, 0), Point3D(5, 3, 1)
        >>> l = Line3D(p1, p2)
        >>> l.direction_ratio
        [5, 3, 1]
        """
    @property
    def direction_cosine(self):
        """The normalized direction ratio of a given line in 3D.

        See Also
        ========

        sympy.geometry.line.Line3D.equation

        Examples
        ========

        >>> from sympy import Point3D, Line3D
        >>> p1, p2 = Point3D(0, 0, 0), Point3D(5, 3, 1)
        >>> l = Line3D(p1, p2)
        >>> l.direction_cosine
        [sqrt(35)/7, 3*sqrt(35)/35, sqrt(35)/35]
        >>> sum(i**2 for i in _)
        1
        """

class Line3D(LinearEntity3D, Line):
    """An infinite 3D line in space.

    A line is declared with two distinct points or a point and direction_ratio
    as defined using keyword `direction_ratio`.

    Parameters
    ==========

    p1 : Point3D
    pt : Point3D
    direction_ratio : list

    See Also
    ========

    sympy.geometry.point.Point3D
    sympy.geometry.line.Line
    sympy.geometry.line.Line2D

    Examples
    ========

    >>> from sympy import Line3D, Point3D
    >>> L = Line3D(Point3D(2, 3, 4), Point3D(3, 5, 1))
    >>> L
    Line3D(Point3D(2, 3, 4), Point3D(3, 5, 1))
    >>> L.points
    (Point3D(2, 3, 4), Point3D(3, 5, 1))
    """
    def __new__(cls, p1, pt: Incomplete | None = None, direction_ratio=(), **kwargs): ...
    def equation(self, x: str = 'x', y: str = 'y', z: str = 'z'):
        """Return the equations that define the line in 3D.

        Parameters
        ==========

        x : str, optional
            The name to use for the x-axis, default value is 'x'.
        y : str, optional
            The name to use for the y-axis, default value is 'y'.
        z : str, optional
            The name to use for the z-axis, default value is 'z'.

        Returns
        =======

        equation : Tuple of simultaneous equations

        Examples
        ========

        >>> from sympy import Point3D, Line3D, solve
        >>> from sympy.abc import x, y, z
        >>> p1, p2 = Point3D(1, 0, 0), Point3D(5, 3, 0)
        >>> l1 = Line3D(p1, p2)
        >>> eq = l1.equation(x, y, z); eq
        (-3*x + 4*y + 3, z)
        >>> solve(eq.subs(z, 0), (x, y, z))
        {x: 4*y/3 + 1}
        """

class Ray3D(LinearEntity3D, Ray):
    """
    A Ray is a semi-line in the space with a source point and a direction.

    Parameters
    ==========

    p1 : Point3D
        The source of the Ray
    p2 : Point or a direction vector
    direction_ratio: Determines the direction in which the Ray propagates.


    Attributes
    ==========

    source
    xdirection
    ydirection
    zdirection

    See Also
    ========

    sympy.geometry.point.Point3D, Line3D


    Examples
    ========

    >>> from sympy import Point3D, Ray3D
    >>> r = Ray3D(Point3D(2, 3, 4), Point3D(3, 5, 0))
    >>> r
    Ray3D(Point3D(2, 3, 4), Point3D(3, 5, 0))
    >>> r.points
    (Point3D(2, 3, 4), Point3D(3, 5, 0))
    >>> r.source
    Point3D(2, 3, 4)
    >>> r.xdirection
    oo
    >>> r.ydirection
    oo
    >>> r.direction_ratio
    [1, 2, -4]

    """
    def __new__(cls, p1, pt: Incomplete | None = None, direction_ratio=(), **kwargs): ...
    @property
    def xdirection(self):
        """The x direction of the ray.

        Positive infinity if the ray points in the positive x direction,
        negative infinity if the ray points in the negative x direction,
        or 0 if the ray is vertical.

        See Also
        ========

        ydirection

        Examples
        ========

        >>> from sympy import Point3D, Ray3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(0, -1, 0)
        >>> r1, r2 = Ray3D(p1, p2), Ray3D(p1, p3)
        >>> r1.xdirection
        oo
        >>> r2.xdirection
        0

        """
    @property
    def ydirection(self):
        """The y direction of the ray.

        Positive infinity if the ray points in the positive y direction,
        negative infinity if the ray points in the negative y direction,
        or 0 if the ray is horizontal.

        See Also
        ========

        xdirection

        Examples
        ========

        >>> from sympy import Point3D, Ray3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(-1, -1, -1), Point3D(-1, 0, 0)
        >>> r1, r2 = Ray3D(p1, p2), Ray3D(p1, p3)
        >>> r1.ydirection
        -oo
        >>> r2.ydirection
        0

        """
    @property
    def zdirection(self):
        """The z direction of the ray.

        Positive infinity if the ray points in the positive z direction,
        negative infinity if the ray points in the negative z direction,
        or 0 if the ray is horizontal.

        See Also
        ========

        xdirection

        Examples
        ========

        >>> from sympy import Point3D, Ray3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(-1, -1, -1), Point3D(-1, 0, 0)
        >>> r1, r2 = Ray3D(p1, p2), Ray3D(p1, p3)
        >>> r1.ydirection
        -oo
        >>> r2.ydirection
        0
        >>> r2.zdirection
        0

        """

class Segment3D(LinearEntity3D, Segment):
    """A line segment in a 3D space.

    Parameters
    ==========

    p1 : Point3D
    p2 : Point3D

    Attributes
    ==========

    length : number or SymPy expression
    midpoint : Point3D

    See Also
    ========

    sympy.geometry.point.Point3D, Line3D

    Examples
    ========

    >>> from sympy import Point3D, Segment3D
    >>> Segment3D((1, 0, 0), (1, 1, 1)) # tuples are interpreted as pts
    Segment3D(Point3D(1, 0, 0), Point3D(1, 1, 1))
    >>> s = Segment3D(Point3D(4, 3, 9), Point3D(1, 1, 7)); s
    Segment3D(Point3D(4, 3, 9), Point3D(1, 1, 7))
    >>> s.points
    (Point3D(4, 3, 9), Point3D(1, 1, 7))
    >>> s.length
    sqrt(17)
    >>> s.midpoint
    Point3D(5/2, 2, 8)

    """
    def __new__(cls, p1, p2, **kwargs): ...
