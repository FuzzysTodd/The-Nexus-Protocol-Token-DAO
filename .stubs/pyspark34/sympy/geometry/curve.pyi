from _typeshed import Incomplete
from sympy.core import diff as diff
from sympy.core.containers import Tuple as Tuple
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.geometry.entity import GeometryEntity as GeometryEntity, GeometrySet as GeometrySet
from sympy.geometry.point import Point as Point
from sympy.integrals import integrate as integrate
from sympy.matrices import Matrix as Matrix, rot_axis3 as rot_axis3
from sympy.utilities.iterables import is_sequence as is_sequence

class Curve(GeometrySet):
    """A curve in space.

    A curve is defined by parametric functions for the coordinates, a
    parameter and the lower and upper bounds for the parameter value.

    Parameters
    ==========

    function : list of functions
    limits : 3-tuple
        Function parameter and lower and upper bounds.

    Attributes
    ==========

    functions
    parameter
    limits

    Raises
    ======

    ValueError
        When `functions` are specified incorrectly.
        When `limits` are specified incorrectly.

    Examples
    ========

    >>> from sympy import Curve, sin, cos, interpolate
    >>> from sympy.abc import t, a
    >>> C = Curve((sin(t), cos(t)), (t, 0, 2))
    >>> C.functions
    (sin(t), cos(t))
    >>> C.limits
    (t, 0, 2)
    >>> C.parameter
    t
    >>> C = Curve((t, interpolate([1, 4, 9, 16], t)), (t, 0, 1)); C
    Curve((t, t**2), (t, 0, 1))
    >>> C.subs(t, 4)
    Point2D(4, 16)
    >>> C.arbitrary_point(a)
    Point2D(a, a**2)

    See Also
    ========

    sympy.core.function.Function
    sympy.polys.polyfuncs.interpolate

    """
    def __new__(cls, function, limits): ...
    def __call__(self, f): ...
    def arbitrary_point(self, parameter: str = 't'):
        """A parameterized point on the curve.

        Parameters
        ==========

        parameter : str or Symbol, optional
            Default value is 't'.
            The Curve's parameter is selected with None or self.parameter
            otherwise the provided symbol is used.

        Returns
        =======

        Point :
            Returns a point in parametric form.

        Raises
        ======

        ValueError
            When `parameter` already appears in the functions.

        Examples
        ========

        >>> from sympy import Curve, Symbol
        >>> from sympy.abc import s
        >>> C = Curve([2*s, s**2], (s, 0, 2))
        >>> C.arbitrary_point()
        Point2D(2*t, t**2)
        >>> C.arbitrary_point(C.parameter)
        Point2D(2*s, s**2)
        >>> C.arbitrary_point(None)
        Point2D(2*s, s**2)
        >>> C.arbitrary_point(Symbol('a'))
        Point2D(2*a, a**2)

        See Also
        ========

        sympy.geometry.point.Point

        """
    @property
    def free_symbols(self):
        """Return a set of symbols other than the bound symbols used to
        parametrically define the Curve.

        Returns
        =======

        set :
            Set of all non-parameterized symbols.

        Examples
        ========

        >>> from sympy.abc import t, a
        >>> from sympy import Curve
        >>> Curve((t, t**2), (t, 0, 2)).free_symbols
        set()
        >>> Curve((t, t**2), (t, a, 2)).free_symbols
        {a}

        """
    @property
    def ambient_dimension(self):
        """The dimension of the curve.

        Returns
        =======

        int :
            the dimension of curve.

        Examples
        ========

        >>> from sympy.abc import t
        >>> from sympy import Curve
        >>> C = Curve((t, t**2), (t, 0, 2))
        >>> C.ambient_dimension
        2

        """
    @property
    def functions(self):
        """The functions specifying the curve.

        Returns
        =======

        functions :
            list of parameterized coordinate functions.

        Examples
        ========

        >>> from sympy.abc import t
        >>> from sympy import Curve
        >>> C = Curve((t, t**2), (t, 0, 2))
        >>> C.functions
        (t, t**2)

        See Also
        ========

        parameter

        """
    @property
    def limits(self):
        """The limits for the curve.

        Returns
        =======

        limits : tuple
            Contains parameter and lower and upper limits.

        Examples
        ========

        >>> from sympy.abc import t
        >>> from sympy import Curve
        >>> C = Curve([t, t**3], (t, -2, 2))
        >>> C.limits
        (t, -2, 2)

        See Also
        ========

        plot_interval

        """
    @property
    def parameter(self):
        """The curve function variable.

        Returns
        =======

        Symbol :
            returns a bound symbol.

        Examples
        ========

        >>> from sympy.abc import t
        >>> from sympy import Curve
        >>> C = Curve([t, t**2], (t, 0, 2))
        >>> C.parameter
        t

        See Also
        ========

        functions

        """
    @property
    def length(self):
        """The curve length.

        Examples
        ========

        >>> from sympy import Curve
        >>> from sympy.abc import t
        >>> Curve((t, t), (t, 0, 1)).length
        sqrt(2)

        """
    def plot_interval(self, parameter: str = 't'):
        """The plot interval for the default geometric plot of the curve.

        Parameters
        ==========

        parameter : str or Symbol, optional
            Default value is 't';
            otherwise the provided symbol is used.

        Returns
        =======

        List :
            the plot interval as below:
                [parameter, lower_bound, upper_bound]

        Examples
        ========

        >>> from sympy import Curve, sin
        >>> from sympy.abc import x, s
        >>> Curve((x, sin(x)), (x, 1, 2)).plot_interval()
        [t, 1, 2]
        >>> Curve((x, sin(x)), (x, 1, 2)).plot_interval(s)
        [s, 1, 2]

        See Also
        ========

        limits : Returns limits of the parameter interval

        """
    def rotate(self, angle: int = 0, pt: Incomplete | None = None):
        """This function is used to rotate a curve along given point ``pt`` at given angle(in radian).

        Parameters
        ==========

        angle :
            the angle at which the curve will be rotated(in radian) in counterclockwise direction.
            default value of angle is 0.

        pt : Point
            the point along which the curve will be rotated.
            If no point given, the curve will be rotated around origin.

        Returns
        =======

        Curve :
            returns a curve rotated at given angle along given point.

        Examples
        ========

        >>> from sympy import Curve, pi
        >>> from sympy.abc import x
        >>> Curve((x, x), (x, 0, 1)).rotate(pi/2)
        Curve((-x, x), (x, 0, 1))

        """
    def scale(self, x: int = 1, y: int = 1, pt: Incomplete | None = None):
        """Override GeometryEntity.scale since Curve is not made up of Points.

        Returns
        =======

        Curve :
            returns scaled curve.

        Examples
        ========

        >>> from sympy import Curve
        >>> from sympy.abc import x
        >>> Curve((x, x), (x, 0, 1)).scale(2)
        Curve((2*x, x), (x, 0, 1))

        """
    def translate(self, x: int = 0, y: int = 0):
        """Translate the Curve by (x, y).

        Returns
        =======

        Curve :
            returns a translated curve.

        Examples
        ========

        >>> from sympy import Curve
        >>> from sympy.abc import x
        >>> Curve((x, x), (x, 0, 1)).translate(1, 2)
        Curve((x + 1, x + 2), (x, 0, 1))

        """
