from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import symbols as symbols
from sympy.functions import sign as sign
from sympy.geometry.ellipse import Ellipse as Ellipse
from sympy.geometry.entity import GeometryEntity as GeometryEntity, GeometrySet as GeometrySet
from sympy.geometry.line import Line as Line, Line2D as Line2D, LinearEntity3D as LinearEntity3D, Ray2D as Ray2D, Segment2D as Segment2D
from sympy.geometry.point import Point as Point, Point2D as Point2D
from sympy.simplify import simplify as simplify
from sympy.solvers.solvers import solve as solve

class Parabola(GeometrySet):
    """A parabolic GeometryEntity.

    A parabola is declared with a point, that is called 'focus', and
    a line, that is called 'directrix'.
    Only vertical or horizontal parabolas are currently supported.

    Parameters
    ==========

    focus : Point
        Default value is Point(0, 0)
    directrix : Line

    Attributes
    ==========

    focus
    directrix
    axis of symmetry
    focal length
    p parameter
    vertex
    eccentricity

    Raises
    ======
    ValueError
        When `focus` is not a two dimensional point.
        When `focus` is a point of directrix.
    NotImplementedError
        When `directrix` is neither horizontal nor vertical.

    Examples
    ========

    >>> from sympy import Parabola, Point, Line
    >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7,8)))
    >>> p1.focus
    Point2D(0, 0)
    >>> p1.directrix
    Line2D(Point2D(5, 8), Point2D(7, 8))

    """
    def __new__(cls, focus: Incomplete | None = None, directrix: Incomplete | None = None, **kwargs): ...
    @property
    def ambient_dimension(self):
        """Returns the ambient dimension of parabola.

        Returns
        =======

        ambient_dimension : integer

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> f1 = Point(0, 0)
        >>> p1 = Parabola(f1, Line(Point(5, 8), Point(7, 8)))
        >>> p1.ambient_dimension
        2

        """
    @property
    def axis_of_symmetry(self):
        """Return the axis of symmetry of the parabola: a line
        perpendicular to the directrix passing through the focus.

        Returns
        =======

        axis_of_symmetry : Line

        See Also
        ========

        sympy.geometry.line.Line

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7, 8)))
        >>> p1.axis_of_symmetry
        Line2D(Point2D(0, 0), Point2D(0, 1))

        """
    @property
    def directrix(self):
        """The directrix of the parabola.

        Returns
        =======

        directrix : Line

        See Also
        ========

        sympy.geometry.line.Line

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> l1 = Line(Point(5, 8), Point(7, 8))
        >>> p1 = Parabola(Point(0, 0), l1)
        >>> p1.directrix
        Line2D(Point2D(5, 8), Point2D(7, 8))

        """
    @property
    def eccentricity(self):
        """The eccentricity of the parabola.

        Returns
        =======

        eccentricity : number

        A parabola may also be characterized as a conic section with an
        eccentricity of 1. As a consequence of this, all parabolas are
        similar, meaning that while they can be different sizes,
        they are all the same shape.

        See Also
        ========

        https://en.wikipedia.org/wiki/Parabola


        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7, 8)))
        >>> p1.eccentricity
        1

        Notes
        -----
        The eccentricity for every Parabola is 1 by definition.

        """
    def equation(self, x: str = 'x', y: str = 'y'):
        """The equation of the parabola.

        Parameters
        ==========
        x : str, optional
            Label for the x-axis. Default value is 'x'.
        y : str, optional
            Label for the y-axis. Default value is 'y'.

        Returns
        =======
        equation : SymPy expression

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7, 8)))
        >>> p1.equation()
        -x**2 - 16*y + 64
        >>> p1.equation('f')
        -f**2 - 16*y + 64
        >>> p1.equation(y='z')
        -x**2 - 16*z + 64

        """
    @property
    def focal_length(self):
        '''The focal length of the parabola.

        Returns
        =======

        focal_lenght : number or symbolic expression

        Notes
        =====

        The distance between the vertex and the focus
        (or the vertex and directrix), measured along the axis
        of symmetry, is the "focal length".

        See Also
        ========

        https://en.wikipedia.org/wiki/Parabola

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7, 8)))
        >>> p1.focal_length
        4

        '''
    @property
    def focus(self):
        """The focus of the parabola.

        Returns
        =======

        focus : Point

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> f1 = Point(0, 0)
        >>> p1 = Parabola(f1, Line(Point(5, 8), Point(7, 8)))
        >>> p1.focus
        Point2D(0, 0)

        """
    def intersection(self, o):
        """The intersection of the parabola and another geometrical entity `o`.

        Parameters
        ==========

        o : GeometryEntity, LinearEntity

        Returns
        =======

        intersection : list of GeometryEntity objects

        Examples
        ========

        >>> from sympy import Parabola, Point, Ellipse, Line, Segment
        >>> p1 = Point(0,0)
        >>> l1 = Line(Point(1, -2), Point(-1,-2))
        >>> parabola1 = Parabola(p1, l1)
        >>> parabola1.intersection(Ellipse(Point(0, 0), 2, 5))
        [Point2D(-2, 0), Point2D(2, 0)]
        >>> parabola1.intersection(Line(Point(-7, 3), Point(12, 3)))
        [Point2D(-4, 3), Point2D(4, 3)]
        >>> parabola1.intersection(Segment((-12, -65), (14, -68)))
        []

        """
    @property
    def p_parameter(self):
        """P is a parameter of parabola.

        Returns
        =======

        p : number or symbolic expression

        Notes
        =====

        The absolute value of p is the focal length. The sign on p tells
        which way the parabola faces. Vertical parabolas that open up
        and horizontal that open right, give a positive value for p.
        Vertical parabolas that open down and horizontal that open left,
        give a negative value for p.


        See Also
        ========

        https://www.sparknotes.com/math/precalc/conicsections/section2/

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7, 8)))
        >>> p1.p_parameter
        -4

        """
    @property
    def vertex(self):
        """The vertex of the parabola.

        Returns
        =======

        vertex : Point

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7, 8)))
        >>> p1.vertex
        Point2D(0, 4)

        """
