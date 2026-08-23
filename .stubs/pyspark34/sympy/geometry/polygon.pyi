from .ellipse import Circle as Circle
from .entity import GeometryEntity as GeometryEntity, GeometrySet as GeometrySet
from .exceptions import GeometryError as GeometryError
from .line import Line as Line, Ray as Ray, Segment as Segment
from .point import Point as Point
from _typeshed import Incomplete
from sympy.core import Expr as Expr, S as S, oo as oo, pi as pi, sympify as sympify
from sympy.core.evalf import N as N
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions.elementary.complexes import sign as sign
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin, tan as tan
from sympy.logic import And as And
from sympy.matrices import Matrix as Matrix
from sympy.simplify.simplify import simplify as simplify
from sympy.solvers.solvers import solve as solve
from sympy.utilities.iterables import has_dups as has_dups, has_variety as has_variety, least_rotation as least_rotation, rotate_left as rotate_left, uniq as uniq
from sympy.utilities.misc import as_int as as_int, func_name as func_name

x: Incomplete
y: Incomplete
T: Incomplete

class Polygon(GeometrySet):
    """A two-dimensional polygon.

    A simple polygon in space. Can be constructed from a sequence of points
    or from a center, radius, number of sides and rotation angle.

    Parameters
    ==========

    vertices
        A sequence of points.

    n : int, optional
        If $> 0$, an n-sided RegularPolygon is created.
        Default value is $0$.

    Attributes
    ==========

    area
    angles
    perimeter
    vertices
    centroid
    sides

    Raises
    ======

    GeometryError
        If all parameters are not Points.

    See Also
    ========

    sympy.geometry.point.Point, sympy.geometry.line.Segment, Triangle

    Notes
    =====

    Polygons are treated as closed paths rather than 2D areas so
    some calculations can be be negative or positive (e.g., area)
    based on the orientation of the points.

    Any consecutive identical points are reduced to a single point
    and any points collinear and between two points will be removed
    unless they are needed to define an explicit intersection (see examples).

    A Triangle, Segment or Point will be returned when there are 3 or
    fewer points provided.

    Examples
    ========

    >>> from sympy import Polygon, pi
    >>> p1, p2, p3, p4, p5 = [(0, 0), (1, 0), (5, 1), (0, 1), (3, 0)]
    >>> Polygon(p1, p2, p3, p4)
    Polygon(Point2D(0, 0), Point2D(1, 0), Point2D(5, 1), Point2D(0, 1))
    >>> Polygon(p1, p2)
    Segment2D(Point2D(0, 0), Point2D(1, 0))
    >>> Polygon(p1, p2, p5)
    Segment2D(Point2D(0, 0), Point2D(3, 0))

    The area of a polygon is calculated as positive when vertices are
    traversed in a ccw direction. When the sides of a polygon cross the
    area will have positive and negative contributions. The following
    defines a Z shape where the bottom right connects back to the top
    left.

    >>> Polygon((0, 2), (2, 2), (0, 0), (2, 0)).area
    0

    When the keyword `n` is used to define the number of sides of the
    Polygon then a RegularPolygon is created and the other arguments are
    interpreted as center, radius and rotation. The unrotated RegularPolygon
    will always have a vertex at Point(r, 0) where `r` is the radius of the
    circle that circumscribes the RegularPolygon. Its method `spin` can be
    used to increment that angle.

    >>> p = Polygon((0,0), 1, n=3)
    >>> p
    RegularPolygon(Point2D(0, 0), 1, 3, 0)
    >>> p.vertices[0]
    Point2D(1, 0)
    >>> p.args[0]
    Point2D(0, 0)
    >>> p.spin(pi/2)
    >>> p.vertices[0]
    Point2D(0, 1)

    """
    def __new__(cls, *args, n: int = 0, **kwargs): ...
    @property
    def area(self):
        """
        The area of the polygon.

        Notes
        =====

        The area calculation can be positive or negative based on the
        orientation of the points. If any side of the polygon crosses
        any other side, there will be areas having opposite signs.

        See Also
        ========

        sympy.geometry.ellipse.Ellipse.area

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly = Polygon(p1, p2, p3, p4)
        >>> poly.area
        3

        In the Z shaped polygon (with the lower right connecting back
        to the upper left) the areas cancel out:

        >>> Z = Polygon((0, 1), (1, 1), (0, 0), (1, 0))
        >>> Z.area
        0

        In the M shaped polygon, areas do not cancel because no side
        crosses any other (though there is a point of contact).

        >>> M = Polygon((0, 0), (0, 1), (2, 0), (3, 1), (3, 0))
        >>> M.area
        -3/2

        """
    @property
    def angles(self):
        """The internal angle at each vertex.

        Returns
        =======

        angles : dict
            A dictionary where each key is a vertex and each value is the
            internal angle at that vertex. The vertices are represented as
            Points.

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.line.LinearEntity.angle_between

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly = Polygon(p1, p2, p3, p4)
        >>> poly.angles[p1]
        pi/2
        >>> poly.angles[p2]
        acos(-4*sqrt(17)/17)

        """
    @property
    def ambient_dimension(self): ...
    @property
    def perimeter(self):
        """The perimeter of the polygon.

        Returns
        =======

        perimeter : number or Basic instance

        See Also
        ========

        sympy.geometry.line.Segment.length

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly = Polygon(p1, p2, p3, p4)
        >>> poly.perimeter
        sqrt(17) + 7
        """
    @property
    def vertices(self):
        """The vertices of the polygon.

        Returns
        =======

        vertices : list of Points

        Notes
        =====

        When iterating over the vertices, it is more efficient to index self
        rather than to request the vertices and index them. Only use the
        vertices when you want to process all of them at once. This is even
        more important with RegularPolygons that calculate each vertex.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly = Polygon(p1, p2, p3, p4)
        >>> poly.vertices
        [Point2D(0, 0), Point2D(1, 0), Point2D(5, 1), Point2D(0, 1)]
        >>> poly.vertices[0]
        Point2D(0, 0)

        """
    @property
    def centroid(self):
        """The centroid of the polygon.

        Returns
        =======

        centroid : Point

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.util.centroid

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly = Polygon(p1, p2, p3, p4)
        >>> poly.centroid
        Point2D(31/18, 11/18)

        """
    def second_moment_of_area(self, point: Incomplete | None = None):
        '''Returns the second moment and product moment of area of a two dimensional polygon.

        Parameters
        ==========

        point : Point, two-tuple of sympifyable objects, or None(default=None)
            point is the point about which second moment of area is to be found.
            If "point=None" it will be calculated about the axis passing through the
            centroid of the polygon.

        Returns
        =======

        I_xx, I_yy, I_xy : number or SymPy expression
                           I_xx, I_yy are second moment of area of a two dimensional polygon.
                           I_xy is product moment of area of a two dimensional polygon.

        Examples
        ========

        >>> from sympy import Polygon, symbols
        >>> a, b = symbols(\'a, b\')
        >>> p1, p2, p3, p4, p5 = [(0, 0), (a, 0), (a, b), (0, b), (a/3, b/3)]
        >>> rectangle = Polygon(p1, p2, p3, p4)
        >>> rectangle.second_moment_of_area()
        (a*b**3/12, a**3*b/12, 0)
        >>> rectangle.second_moment_of_area(p5)
        (a*b**3/9, a**3*b/9, a**2*b**2/36)

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Second_moment_of_area

        '''
    def first_moment_of_area(self, point: Incomplete | None = None):
        """
        Returns the first moment of area of a two-dimensional polygon with
        respect to a certain point of interest.

        First moment of area is a measure of the distribution of the area
        of a polygon in relation to an axis. The first moment of area of
        the entire polygon about its own centroid is always zero. Therefore,
        here it is calculated for an area, above or below a certain point
        of interest, that makes up a smaller portion of the polygon. This
        area is bounded by the point of interest and the extreme end
        (top or bottom) of the polygon. The first moment for this area is
        is then determined about the centroidal axis of the initial polygon.

        References
        ==========

        .. [1] https://skyciv.com/docs/tutorials/section-tutorials/calculating-the-statical-or-first-moment-of-area-of-beam-sections/?cc=BMD
        .. [2] https://mechanicalc.com/reference/cross-sections

        Parameters
        ==========

        point: Point, two-tuple of sympifyable objects, or None (default=None)
            point is the point above or below which the area of interest lies
            If ``point=None`` then the centroid acts as the point of interest.

        Returns
        =======

        Q_x, Q_y: number or SymPy expressions
            Q_x is the first moment of area about the x-axis
            Q_y is the first moment of area about the y-axis
            A negative sign indicates that the section modulus is
            determined for a section below (or left of) the centroidal axis

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> a, b = 50, 10
        >>> p1, p2, p3, p4 = [(0, b), (0, 0), (a, 0), (a, b)]
        >>> p = Polygon(p1, p2, p3, p4)
        >>> p.first_moment_of_area()
        (625, 3125)
        >>> p.first_moment_of_area(point=Point(30, 7))
        (525, 3000)
        """
    def polar_second_moment_of_area(self):
        """Returns the polar modulus of a two-dimensional polygon

        It is a constituent of the second moment of area, linked through
        the perpendicular axis theorem. While the planar second moment of
        area describes an object's resistance to deflection (bending) when
        subjected to a force applied to a plane parallel to the central
        axis, the polar second moment of area describes an object's
        resistance to deflection when subjected to a moment applied in a
        plane perpendicular to the object's central axis (i.e. parallel to
        the cross-section)

        Examples
        ========

        >>> from sympy import Polygon, symbols
        >>> a, b = symbols('a, b')
        >>> rectangle = Polygon((0, 0), (a, 0), (a, b), (0, b))
        >>> rectangle.polar_second_moment_of_area()
        a**3*b/12 + a*b**3/12

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Polar_moment_of_inertia

        """
    def section_modulus(self, point: Incomplete | None = None):
        '''Returns a tuple with the section modulus of a two-dimensional
        polygon.

        Section modulus is a geometric property of a polygon defined as the
        ratio of second moment of area to the distance of the extreme end of
        the polygon from the centroidal axis.

        Parameters
        ==========

        point : Point, two-tuple of sympifyable objects, or None(default=None)
            point is the point at which section modulus is to be found.
            If "point=None" it will be calculated for the point farthest from the
            centroidal axis of the polygon.

        Returns
        =======

        S_x, S_y: numbers or SymPy expressions
                  S_x is the section modulus with respect to the x-axis
                  S_y is the section modulus with respect to the y-axis
                  A negative sign indicates that the section modulus is
                  determined for a point below the centroidal axis

        Examples
        ========

        >>> from sympy import symbols, Polygon, Point
        >>> a, b = symbols(\'a, b\', positive=True)
        >>> rectangle = Polygon((0, 0), (a, 0), (a, b), (0, b))
        >>> rectangle.section_modulus()
        (a*b**2/6, a**2*b/6)
        >>> rectangle.section_modulus(Point(a/4, b/4))
        (-a*b**2/3, -a**2*b/3)

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Section_modulus

        '''
    @property
    def sides(self):
        """The directed line segments that form the sides of the polygon.

        Returns
        =======

        sides : list of sides
            Each side is a directed Segment.

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.line.Segment

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly = Polygon(p1, p2, p3, p4)
        >>> poly.sides
        [Segment2D(Point2D(0, 0), Point2D(1, 0)),
        Segment2D(Point2D(1, 0), Point2D(5, 1)),
        Segment2D(Point2D(5, 1), Point2D(0, 1)), Segment2D(Point2D(0, 1), Point2D(0, 0))]

        """
    @property
    def bounds(self):
        """Return a tuple (xmin, ymin, xmax, ymax) representing the bounding
        rectangle for the geometric figure.

        """
    def is_convex(self):
        """Is the polygon convex?

        A polygon is convex if all its interior angles are less than 180
        degrees and there are no intersections between sides.

        Returns
        =======

        is_convex : boolean
            True if this polygon is convex, False otherwise.

        See Also
        ========

        sympy.geometry.util.convex_hull

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly = Polygon(p1, p2, p3, p4)
        >>> poly.is_convex()
        True

        """
    def encloses_point(self, p):
        """
        Return True if p is enclosed by (is inside of) self.

        Notes
        =====

        Being on the border of self is considered False.

        Parameters
        ==========

        p : Point

        Returns
        =======

        encloses_point : True, False or None

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.ellipse.Ellipse.encloses_point

        Examples
        ========

        >>> from sympy import Polygon, Point
        >>> p = Polygon((0, 0), (4, 0), (4, 4))
        >>> p.encloses_point(Point(2, 1))
        True
        >>> p.encloses_point(Point(2, 2))
        False
        >>> p.encloses_point(Point(5, 5))
        False

        References
        ==========

        .. [1] http://paulbourke.net/geometry/polygonmesh/#insidepoly

        """
    def arbitrary_point(self, parameter: str = 't'):
        """A parameterized point on the polygon.

        The parameter, varying from 0 to 1, assigns points to the position on
        the perimeter that is that fraction of the total perimeter. So the
        point evaluated at t=1/2 would return the point from the first vertex
        that is 1/2 way around the polygon.

        Parameters
        ==========

        parameter : str, optional
            Default value is 't'.

        Returns
        =======

        arbitrary_point : Point

        Raises
        ======

        ValueError
            When `parameter` already appears in the Polygon's definition.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Polygon, Symbol
        >>> t = Symbol('t', real=True)
        >>> tri = Polygon((0, 0), (1, 0), (1, 1))
        >>> p = tri.arbitrary_point('t')
        >>> perimeter = tri.perimeter
        >>> s1, s2 = [s.length for s in tri.sides[:2]]
        >>> p.subs(t, (s1 + s2/2)/perimeter)
        Point2D(1, 1/2)

        """
    def parameter_value(self, other, t): ...
    def plot_interval(self, parameter: str = 't'):
        """The plot interval for the default geometric plot of the polygon.

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

        >>> from sympy import Polygon
        >>> p = Polygon((0, 0), (1, 0), (1, 1))
        >>> p.plot_interval()
        [t, 0, 1]

        """
    def intersection(self, o):
        """The intersection of polygon and geometry entity.

        The intersection may be empty and can contain individual Points and
        complete Line Segments.

        Parameters
        ==========

        other: GeometryEntity

        Returns
        =======

        intersection : list
            The list of Segments and Points

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.line.Segment

        Examples
        ========

        >>> from sympy import Point, Polygon, Line
        >>> p1, p2, p3, p4 = map(Point, [(0, 0), (1, 0), (5, 1), (0, 1)])
        >>> poly1 = Polygon(p1, p2, p3, p4)
        >>> p5, p6, p7 = map(Point, [(3, 2), (1, -1), (0, 2)])
        >>> poly2 = Polygon(p5, p6, p7)
        >>> poly1.intersection(poly2)
        [Point2D(1/3, 1), Point2D(2/3, 0), Point2D(9/5, 1/5), Point2D(7/3, 1)]
        >>> poly1.intersection(Line(p1, p2))
        [Segment2D(Point2D(0, 0), Point2D(1, 0))]
        >>> poly1.intersection(p1)
        [Point2D(0, 0)]
        """
    def cut_section(self, line):
        """
        Returns a tuple of two polygon segments that lie above and below
        the intersecting line respectively.

        Parameters
        ==========

        line: Line object of geometry module
            line which cuts the Polygon. The part of the Polygon that lies
            above and below this line is returned.

        Returns
        =======

        upper_polygon, lower_polygon: Polygon objects or None
            upper_polygon is the polygon that lies above the given line.
            lower_polygon is the polygon that lies below the given line.
            upper_polygon and lower polygon are ``None`` when no polygon
            exists above the line or below the line.

        Raises
        ======

        ValueError: When the line does not intersect the polygon

        Examples
        ========

        >>> from sympy import Polygon, Line
        >>> a, b = 20, 10
        >>> p1, p2, p3, p4 = [(0, b), (0, 0), (a, 0), (a, b)]
        >>> rectangle = Polygon(p1, p2, p3, p4)
        >>> t = rectangle.cut_section(Line((0, 5), slope=0))
        >>> t
        (Polygon(Point2D(0, 10), Point2D(0, 5), Point2D(20, 5), Point2D(20, 10)),
        Polygon(Point2D(0, 5), Point2D(0, 0), Point2D(20, 0), Point2D(20, 5)))
        >>> upper_segment, lower_segment = t
        >>> upper_segment.area
        100
        >>> upper_segment.centroid
        Point2D(10, 15/2)
        >>> lower_segment.centroid
        Point2D(10, 5/2)

        References
        ==========

        .. [1] https://github.com/sympy/sympy/wiki/A-method-to-return-a-cut-section-of-any-polygon-geometry

        """
    def distance(self, o):
        """
        Returns the shortest distance between self and o.

        If o is a point, then self does not need to be convex.
        If o is another polygon self and o must be convex.

        Examples
        ========

        >>> from sympy import Point, Polygon, RegularPolygon
        >>> p1, p2 = map(Point, [(0, 0), (7, 5)])
        >>> poly = Polygon(*RegularPolygon(p1, 1, 3).vertices)
        >>> poly.distance(p2)
        sqrt(61)
        """
    def __contains__(self, o) -> bool:
        """
        Return True if o is contained within the boundary lines of self.altitudes

        Parameters
        ==========

        other : GeometryEntity

        Returns
        =======

        contained in : bool
            The points (and sides, if applicable) are contained in self.

        See Also
        ========

        sympy.geometry.entity.GeometryEntity.encloses

        Examples
        ========

        >>> from sympy import Line, Segment, Point
        >>> p = Point(0, 0)
        >>> q = Point(1, 1)
        >>> s = Segment(p, q*2)
        >>> l = Line(p, q)
        >>> p in q
        False
        >>> p in s
        True
        >>> q*3 in s
        False
        >>> s in l
        True

        """
    def bisectors(p, prec: Incomplete | None = None):
        """Returns angle bisectors of a polygon. If prec is given
        then approximate the point defining the ray to that precision.

        The distance between the points defining the bisector ray is 1.

        Examples
        ========

        >>> from sympy import Polygon, Point
        >>> p = Polygon(Point(0, 0), Point(2, 0), Point(1, 1), Point(0, 3))
        >>> p.bisectors(2)
        {Point2D(0, 0): Ray2D(Point2D(0, 0), Point2D(0.71, 0.71)),
         Point2D(0, 3): Ray2D(Point2D(0, 3), Point2D(0.23, 2.0)),
         Point2D(1, 1): Ray2D(Point2D(1, 1), Point2D(0.19, 0.42)),
         Point2D(2, 0): Ray2D(Point2D(2, 0), Point2D(1.1, 0.38))}
        """

class RegularPolygon(Polygon):
    """
    A regular polygon.

    Such a polygon has all internal angles equal and all sides the same length.

    Parameters
    ==========

    center : Point
    radius : number or Basic instance
        The distance from the center to a vertex
    n : int
        The number of sides

    Attributes
    ==========

    vertices
    center
    radius
    rotation
    apothem
    interior_angle
    exterior_angle
    circumcircle
    incircle
    angles

    Raises
    ======

    GeometryError
        If the `center` is not a Point, or the `radius` is not a number or Basic
        instance, or the number of sides, `n`, is less than three.

    Notes
    =====

    A RegularPolygon can be instantiated with Polygon with the kwarg n.

    Regular polygons are instantiated with a center, radius, number of sides
    and a rotation angle. Whereas the arguments of a Polygon are vertices, the
    vertices of the RegularPolygon must be obtained with the vertices method.

    See Also
    ========

    sympy.geometry.point.Point, Polygon

    Examples
    ========

    >>> from sympy import RegularPolygon, Point
    >>> r = RegularPolygon(Point(0, 0), 5, 3)
    >>> r
    RegularPolygon(Point2D(0, 0), 5, 3, 0)
    >>> r.vertices[0]
    Point2D(5, 0)

    """
    def __new__(self, c, r, n, rot: int = 0, **kwargs): ...
    @property
    def args(self):
        """
        Returns the center point, the radius,
        the number of sides, and the orientation angle.

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> r = RegularPolygon(Point(0, 0), 5, 3)
        >>> r.args
        (Point2D(0, 0), 5, 3, 0)
        """
    @property
    def area(self):
        """Returns the area.

        Examples
        ========

        >>> from sympy import RegularPolygon
        >>> square = RegularPolygon((0, 0), 1, 4)
        >>> square.area
        2
        >>> _ == square.length**2
        True
        """
    @property
    def length(self):
        """Returns the length of the sides.

        The half-length of the side and the apothem form two legs
        of a right triangle whose hypotenuse is the radius of the
        regular polygon.

        Examples
        ========

        >>> from sympy import RegularPolygon
        >>> from sympy import sqrt
        >>> s = square_in_unit_circle = RegularPolygon((0, 0), 1, 4)
        >>> s.length
        sqrt(2)
        >>> sqrt((_/2)**2 + s.apothem**2) == s.radius
        True

        """
    @property
    def center(self):
        """The center of the RegularPolygon

        This is also the center of the circumscribing circle.

        Returns
        =======

        center : Point

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.ellipse.Ellipse.center

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> rp = RegularPolygon(Point(0, 0), 5, 4)
        >>> rp.center
        Point2D(0, 0)
        """
    centroid = center
    @property
    def circumcenter(self):
        """
        Alias for center.

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> rp = RegularPolygon(Point(0, 0), 5, 4)
        >>> rp.circumcenter
        Point2D(0, 0)
        """
    @property
    def radius(self):
        """Radius of the RegularPolygon

        This is also the radius of the circumscribing circle.

        Returns
        =======

        radius : number or instance of Basic

        See Also
        ========

        sympy.geometry.line.Segment.length, sympy.geometry.ellipse.Circle.radius

        Examples
        ========

        >>> from sympy import Symbol
        >>> from sympy import RegularPolygon, Point
        >>> radius = Symbol('r')
        >>> rp = RegularPolygon(Point(0, 0), radius, 4)
        >>> rp.radius
        r

        """
    @property
    def circumradius(self):
        """
        Alias for radius.

        Examples
        ========

        >>> from sympy import Symbol
        >>> from sympy import RegularPolygon, Point
        >>> radius = Symbol('r')
        >>> rp = RegularPolygon(Point(0, 0), radius, 4)
        >>> rp.circumradius
        r
        """
    @property
    def rotation(self):
        """CCW angle by which the RegularPolygon is rotated

        Returns
        =======

        rotation : number or instance of Basic

        Examples
        ========

        >>> from sympy import pi
        >>> from sympy.abc import a
        >>> from sympy import RegularPolygon, Point
        >>> RegularPolygon(Point(0, 0), 3, 4, pi/4).rotation
        pi/4

        Numerical rotation angles are made canonical:

        >>> RegularPolygon(Point(0, 0), 3, 4, a).rotation
        a
        >>> RegularPolygon(Point(0, 0), 3, 4, pi).rotation
        0

        """
    @property
    def apothem(self):
        """The inradius of the RegularPolygon.

        The apothem/inradius is the radius of the inscribed circle.

        Returns
        =======

        apothem : number or instance of Basic

        See Also
        ========

        sympy.geometry.line.Segment.length, sympy.geometry.ellipse.Circle.radius

        Examples
        ========

        >>> from sympy import Symbol
        >>> from sympy import RegularPolygon, Point
        >>> radius = Symbol('r')
        >>> rp = RegularPolygon(Point(0, 0), radius, 4)
        >>> rp.apothem
        sqrt(2)*r/2

        """
    @property
    def inradius(self):
        """
        Alias for apothem.

        Examples
        ========

        >>> from sympy import Symbol
        >>> from sympy import RegularPolygon, Point
        >>> radius = Symbol('r')
        >>> rp = RegularPolygon(Point(0, 0), radius, 4)
        >>> rp.inradius
        sqrt(2)*r/2
        """
    @property
    def interior_angle(self):
        """Measure of the interior angles.

        Returns
        =======

        interior_angle : number

        See Also
        ========

        sympy.geometry.line.LinearEntity.angle_between

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> rp = RegularPolygon(Point(0, 0), 4, 8)
        >>> rp.interior_angle
        3*pi/4

        """
    @property
    def exterior_angle(self):
        """Measure of the exterior angles.

        Returns
        =======

        exterior_angle : number

        See Also
        ========

        sympy.geometry.line.LinearEntity.angle_between

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> rp = RegularPolygon(Point(0, 0), 4, 8)
        >>> rp.exterior_angle
        pi/4

        """
    @property
    def circumcircle(self):
        """The circumcircle of the RegularPolygon.

        Returns
        =======

        circumcircle : Circle

        See Also
        ========

        circumcenter, sympy.geometry.ellipse.Circle

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> rp = RegularPolygon(Point(0, 0), 4, 8)
        >>> rp.circumcircle
        Circle(Point2D(0, 0), 4)

        """
    @property
    def incircle(self):
        """The incircle of the RegularPolygon.

        Returns
        =======

        incircle : Circle

        See Also
        ========

        inradius, sympy.geometry.ellipse.Circle

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> rp = RegularPolygon(Point(0, 0), 4, 7)
        >>> rp.incircle
        Circle(Point2D(0, 0), 4*cos(pi/7))

        """
    @property
    def angles(self):
        """
        Returns a dictionary with keys, the vertices of the Polygon,
        and values, the interior angle at each vertex.

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> r = RegularPolygon(Point(0, 0), 5, 3)
        >>> r.angles
        {Point2D(-5/2, -5*sqrt(3)/2): pi/3,
         Point2D(-5/2, 5*sqrt(3)/2): pi/3,
         Point2D(5, 0): pi/3}
        """
    def encloses_point(self, p):
        """
        Return True if p is enclosed by (is inside of) self.

        Notes
        =====

        Being on the border of self is considered False.

        The general Polygon.encloses_point method is called only if
        a point is not within or beyond the incircle or circumcircle,
        respectively.

        Parameters
        ==========

        p : Point

        Returns
        =======

        encloses_point : True, False or None

        See Also
        ========

        sympy.geometry.ellipse.Ellipse.encloses_point

        Examples
        ========

        >>> from sympy import RegularPolygon, S, Point, Symbol
        >>> p = RegularPolygon((0, 0), 3, 4)
        >>> p.encloses_point(Point(0, 0))
        True
        >>> r, R = p.inradius, p.circumradius
        >>> p.encloses_point(Point((r + R)/2, 0))
        True
        >>> p.encloses_point(Point(R/2, R/2 + (R - r)/10))
        False
        >>> t = Symbol('t', real=True)
        >>> p.encloses_point(p.arbitrary_point().subs(t, S.Half))
        False
        >>> p.encloses_point(Point(5, 5))
        False

        """
    def spin(self, angle) -> None:
        """Increment *in place* the virtual Polygon's rotation by ccw angle.

        See also: rotate method which moves the center.

        >>> from sympy import Polygon, Point, pi
        >>> r = Polygon(Point(0,0), 1, n=3)
        >>> r.vertices[0]
        Point2D(1, 0)
        >>> r.spin(pi/6)
        >>> r.vertices[0]
        Point2D(sqrt(3)/2, 1/2)

        See Also
        ========

        rotation
        rotate : Creates a copy of the RegularPolygon rotated about a Point

        """
    def rotate(self, angle, pt: Incomplete | None = None):
        """Override GeometryEntity.rotate to first rotate the RegularPolygon
        about its center.

        >>> from sympy import Point, RegularPolygon, pi
        >>> t = RegularPolygon(Point(1, 0), 1, 3)
        >>> t.vertices[0] # vertex on x-axis
        Point2D(2, 0)
        >>> t.rotate(pi/2).vertices[0] # vertex on y axis now
        Point2D(0, 2)

        See Also
        ========

        rotation
        spin : Rotates a RegularPolygon in place

        """
    def scale(self, x: int = 1, y: int = 1, pt: Incomplete | None = None):
        """Override GeometryEntity.scale since it is the radius that must be
        scaled (if x == y) or else a new Polygon must be returned.

        >>> from sympy import RegularPolygon

        Symmetric scaling returns a RegularPolygon:

        >>> RegularPolygon((0, 0), 1, 4).scale(2, 2)
        RegularPolygon(Point2D(0, 0), 2, 4, 0)

        Asymmetric scaling returns a kite as a Polygon:

        >>> RegularPolygon((0, 0), 1, 4).scale(2, 1)
        Polygon(Point2D(2, 0), Point2D(0, 1), Point2D(-2, 0), Point2D(0, -1))

        """
    def reflect(self, line):
        """Override GeometryEntity.reflect since this is not made of only
        points.

        Examples
        ========

        >>> from sympy import RegularPolygon, Line

        >>> RegularPolygon((0, 0), 1, 4).reflect(Line((0, 1), slope=-2))
        RegularPolygon(Point2D(4/5, 2/5), -1, 4, atan(4/3))

        """
    @property
    def vertices(self):
        """The vertices of the RegularPolygon.

        Returns
        =======

        vertices : list
            Each vertex is a Point.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import RegularPolygon, Point
        >>> rp = RegularPolygon(Point(0, 0), 5, 4)
        >>> rp.vertices
        [Point2D(5, 0), Point2D(0, 5), Point2D(-5, 0), Point2D(0, -5)]

        """
    def __eq__(self, o): ...
    def __hash__(self): ...

class Triangle(Polygon):
    """
    A polygon with three vertices and three sides.

    Parameters
    ==========

    points : sequence of Points
    keyword: asa, sas, or sss to specify sides/angles of the triangle

    Attributes
    ==========

    vertices
    altitudes
    orthocenter
    circumcenter
    circumradius
    circumcircle
    inradius
    incircle
    exradii
    medians
    medial
    nine_point_circle

    Raises
    ======

    GeometryError
        If the number of vertices is not equal to three, or one of the vertices
        is not a Point, or a valid keyword is not given.

    See Also
    ========

    sympy.geometry.point.Point, Polygon

    Examples
    ========

    >>> from sympy import Triangle, Point
    >>> Triangle(Point(0, 0), Point(4, 0), Point(4, 3))
    Triangle(Point2D(0, 0), Point2D(4, 0), Point2D(4, 3))

    Keywords sss, sas, or asa can be used to give the desired
    side lengths (in order) and interior angles (in degrees) that
    define the triangle:

    >>> Triangle(sss=(3, 4, 5))
    Triangle(Point2D(0, 0), Point2D(3, 0), Point2D(3, 4))
    >>> Triangle(asa=(30, 1, 30))
    Triangle(Point2D(0, 0), Point2D(1, 0), Point2D(1/2, sqrt(3)/6))
    >>> Triangle(sas=(1, 45, 2))
    Triangle(Point2D(0, 0), Point2D(2, 0), Point2D(sqrt(2)/2, sqrt(2)/2))

    """
    def __new__(cls, *args, **kwargs): ...
    @property
    def vertices(self):
        """The triangle's vertices

        Returns
        =======

        vertices : tuple
            Each element in the tuple is a Point

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Triangle, Point
        >>> t = Triangle(Point(0, 0), Point(4, 0), Point(4, 3))
        >>> t.vertices
        (Point2D(0, 0), Point2D(4, 0), Point2D(4, 3))

        """
    def is_similar(t1, t2):
        """Is another triangle similar to this one.

        Two triangles are similar if one can be uniformly scaled to the other.

        Parameters
        ==========

        other: Triangle

        Returns
        =======

        is_similar : boolean

        See Also
        ========

        sympy.geometry.entity.GeometryEntity.is_similar

        Examples
        ========

        >>> from sympy import Triangle, Point
        >>> t1 = Triangle(Point(0, 0), Point(4, 0), Point(4, 3))
        >>> t2 = Triangle(Point(0, 0), Point(-4, 0), Point(-4, -3))
        >>> t1.is_similar(t2)
        True

        >>> t2 = Triangle(Point(0, 0), Point(-4, 0), Point(-4, -4))
        >>> t1.is_similar(t2)
        False

        """
    def is_equilateral(self):
        """Are all the sides the same length?

        Returns
        =======

        is_equilateral : boolean

        See Also
        ========

        sympy.geometry.entity.GeometryEntity.is_similar, RegularPolygon
        is_isosceles, is_right, is_scalene

        Examples
        ========

        >>> from sympy import Triangle, Point
        >>> t1 = Triangle(Point(0, 0), Point(4, 0), Point(4, 3))
        >>> t1.is_equilateral()
        False

        >>> from sympy import sqrt
        >>> t2 = Triangle(Point(0, 0), Point(10, 0), Point(5, 5*sqrt(3)))
        >>> t2.is_equilateral()
        True

        """
    def is_isosceles(self):
        """Are two or more of the sides the same length?

        Returns
        =======

        is_isosceles : boolean

        See Also
        ========

        is_equilateral, is_right, is_scalene

        Examples
        ========

        >>> from sympy import Triangle, Point
        >>> t1 = Triangle(Point(0, 0), Point(4, 0), Point(2, 4))
        >>> t1.is_isosceles()
        True

        """
    def is_scalene(self):
        """Are all the sides of the triangle of different lengths?

        Returns
        =======

        is_scalene : boolean

        See Also
        ========

        is_equilateral, is_isosceles, is_right

        Examples
        ========

        >>> from sympy import Triangle, Point
        >>> t1 = Triangle(Point(0, 0), Point(4, 0), Point(1, 4))
        >>> t1.is_scalene()
        True

        """
    def is_right(self):
        """Is the triangle right-angled.

        Returns
        =======

        is_right : boolean

        See Also
        ========

        sympy.geometry.line.LinearEntity.is_perpendicular
        is_equilateral, is_isosceles, is_scalene

        Examples
        ========

        >>> from sympy import Triangle, Point
        >>> t1 = Triangle(Point(0, 0), Point(4, 0), Point(4, 3))
        >>> t1.is_right()
        True

        """
    @property
    def altitudes(self):
        """The altitudes of the triangle.

        An altitude of a triangle is a segment through a vertex,
        perpendicular to the opposite side, with length being the
        height of the vertex measured from the line containing the side.

        Returns
        =======

        altitudes : dict
            The dictionary consists of keys which are vertices and values
            which are Segments.

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.line.Segment.length

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.altitudes[p1]
        Segment2D(Point2D(0, 0), Point2D(1/2, 1/2))

        """
    @property
    def orthocenter(self):
        """The orthocenter of the triangle.

        The orthocenter is the intersection of the altitudes of a triangle.
        It may lie inside, outside or on the triangle.

        Returns
        =======

        orthocenter : Point

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.orthocenter
        Point2D(0, 0)

        """
    @property
    def circumcenter(self):
        """The circumcenter of the triangle

        The circumcenter is the center of the circumcircle.

        Returns
        =======

        circumcenter : Point

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.circumcenter
        Point2D(1/2, 1/2)
        """
    @property
    def circumradius(self):
        """The radius of the circumcircle of the triangle.

        Returns
        =======

        circumradius : number of Basic instance

        See Also
        ========

        sympy.geometry.ellipse.Circle.radius

        Examples
        ========

        >>> from sympy import Symbol
        >>> from sympy import Point, Triangle
        >>> a = Symbol('a')
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, a)
        >>> t = Triangle(p1, p2, p3)
        >>> t.circumradius
        sqrt(a**2/4 + 1/4)
        """
    @property
    def circumcircle(self):
        """The circle which passes through the three vertices of the triangle.

        Returns
        =======

        circumcircle : Circle

        See Also
        ========

        sympy.geometry.ellipse.Circle

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.circumcircle
        Circle(Point2D(1/2, 1/2), sqrt(2)/2)

        """
    def bisectors(self):
        """The angle bisectors of the triangle.

        An angle bisector of a triangle is a straight line through a vertex
        which cuts the corresponding angle in half.

        Returns
        =======

        bisectors : dict
            Each key is a vertex (Point) and each value is the corresponding
            bisector (Segment).

        See Also
        ========

        sympy.geometry.point.Point, sympy.geometry.line.Segment

        Examples
        ========

        >>> from sympy import Point, Triangle, Segment
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> from sympy import sqrt
        >>> t.bisectors()[p2] == Segment(Point(1, 0), Point(0, sqrt(2) - 1))
        True

        """
    @property
    def incenter(self):
        """The center of the incircle.

        The incircle is the circle which lies inside the triangle and touches
        all three sides.

        Returns
        =======

        incenter : Point

        See Also
        ========

        incircle, sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.incenter
        Point2D(1 - sqrt(2)/2, 1 - sqrt(2)/2)

        """
    @property
    def inradius(self):
        """The radius of the incircle.

        Returns
        =======

        inradius : number of Basic instance

        See Also
        ========

        incircle, sympy.geometry.ellipse.Circle.radius

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(4, 0), Point(0, 3)
        >>> t = Triangle(p1, p2, p3)
        >>> t.inradius
        1

        """
    @property
    def incircle(self):
        """The incircle of the triangle.

        The incircle is the circle which lies inside the triangle and touches
        all three sides.

        Returns
        =======

        incircle : Circle

        See Also
        ========

        sympy.geometry.ellipse.Circle

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(2, 0), Point(0, 2)
        >>> t = Triangle(p1, p2, p3)
        >>> t.incircle
        Circle(Point2D(2 - sqrt(2), 2 - sqrt(2)), 2 - sqrt(2))

        """
    @property
    def exradii(self):
        """The radius of excircles of a triangle.

        An excircle of the triangle is a circle lying outside the triangle,
        tangent to one of its sides and tangent to the extensions of the
        other two.

        Returns
        =======

        exradii : dict

        See Also
        ========

        sympy.geometry.polygon.Triangle.inradius

        Examples
        ========

        The exradius touches the side of the triangle to which it is keyed, e.g.
        the exradius touching side 2 is:

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(6, 0), Point(0, 2)
        >>> t = Triangle(p1, p2, p3)
        >>> t.exradii[t.sides[2]]
        -2 + sqrt(10)

        References
        ==========

        .. [1] https://mathworld.wolfram.com/Exradius.html
        .. [2] https://mathworld.wolfram.com/Excircles.html

        """
    @property
    def excenters(self):
        """Excenters of the triangle.

        An excenter is the center of a circle that is tangent to a side of the
        triangle and the extensions of the other two sides.

        Returns
        =======

        excenters : dict


        Examples
        ========

        The excenters are keyed to the side of the triangle to which their corresponding
        excircle is tangent: The center is keyed, e.g. the excenter of a circle touching
        side 0 is:

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(6, 0), Point(0, 2)
        >>> t = Triangle(p1, p2, p3)
        >>> t.excenters[t.sides[0]]
        Point2D(12*sqrt(10), 2/3 + sqrt(10)/3)

        See Also
        ========

        sympy.geometry.polygon.Triangle.exradii

        References
        ==========

        .. [1] https://mathworld.wolfram.com/Excircles.html

        """
    @property
    def medians(self):
        """The medians of the triangle.

        A median of a triangle is a straight line through a vertex and the
        midpoint of the opposite side, and divides the triangle into two
        equal areas.

        Returns
        =======

        medians : dict
            Each key is a vertex (Point) and each value is the median (Segment)
            at that point.

        See Also
        ========

        sympy.geometry.point.Point.midpoint, sympy.geometry.line.Segment.midpoint

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.medians[p1]
        Segment2D(Point2D(0, 0), Point2D(1/2, 1/2))

        """
    @property
    def medial(self):
        """The medial triangle of the triangle.

        The triangle which is formed from the midpoints of the three sides.

        Returns
        =======

        medial : Triangle

        See Also
        ========

        sympy.geometry.line.Segment.midpoint

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.medial
        Triangle(Point2D(1/2, 0), Point2D(1/2, 1/2), Point2D(0, 1/2))

        """
    @property
    def nine_point_circle(self):
        """The nine-point circle of the triangle.

        Nine-point circle is the circumcircle of the medial triangle, which
        passes through the feet of altitudes and the middle points of segments
        connecting the vertices and the orthocenter.

        Returns
        =======

        nine_point_circle : Circle

        See also
        ========

        sympy.geometry.line.Segment.midpoint
        sympy.geometry.polygon.Triangle.medial
        sympy.geometry.polygon.Triangle.orthocenter

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.nine_point_circle
        Circle(Point2D(1/4, 1/4), sqrt(2)/4)

        """
    @property
    def eulerline(self):
        """The Euler line of the triangle.

        The line which passes through circumcenter, centroid and orthocenter.

        Returns
        =======

        eulerline : Line (or Point for equilateral triangles in which case all
                    centers coincide)

        Examples
        ========

        >>> from sympy import Point, Triangle
        >>> p1, p2, p3 = Point(0, 0), Point(1, 0), Point(0, 1)
        >>> t = Triangle(p1, p2, p3)
        >>> t.eulerline
        Line2D(Point2D(0, 0), Point2D(1/2, 1/2))

        """

def rad(d):
    """Return the radian value for the given degrees (pi = 180 degrees)."""
def deg(r):
    """Return the degree value for the given radians (pi = 180 degrees)."""
