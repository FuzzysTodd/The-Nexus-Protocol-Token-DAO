from _typeshed import Incomplete
from sympy.core import Basic as Basic, Eq as Eq, Integer as Integer, Tuple as Tuple, diff as diff, expand as expand
from sympy.core.numbers import Rational as Rational
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import symbols as symbols
from sympy.functions.elementary.complexes import sign as sign
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.geometry import Point as Point
from sympy.ntheory.factor_ import core as core
from sympy.polys import total_degree as total_degree
from sympy.polys.polytools import gcd as gcd
from sympy.sets.sets import Complement as Complement
from sympy.solvers import diophantine as diophantine, nonlinsolve as nonlinsolve, solveset as solveset

class ImplicitRegion(Basic):
    """
    Represents an implicit region in space.

    Examples
    ========

    >>> from sympy import Eq
    >>> from sympy.abc import x, y, z, t
    >>> from sympy.vector import ImplicitRegion

    >>> ImplicitRegion((x, y), x**2 + y**2 - 4)
    ImplicitRegion((x, y), x**2 + y**2 - 4)
    >>> ImplicitRegion((x, y), Eq(y*x, 1))
    ImplicitRegion((x, y), x*y - 1)

    >>> parabola = ImplicitRegion((x, y), y**2 - 4*x)
    >>> parabola.degree
    2
    >>> parabola.equation
    -4*x + y**2
    >>> parabola.rational_parametrization(t)
    (4/t**2, 4/t)

    >>> r = ImplicitRegion((x, y, z), Eq(z, x**2 + y**2))
    >>> r.variables
    (x, y, z)
    >>> r.singular_points()
    EmptySet
    >>> r.regular_point()
    (-10, -10, 200)

    Parameters
    ==========

    variables : tuple to map variables in implicit equation to base scalars.

    equation : An expression or Eq denoting the implicit equation of the region.

    """
    def __new__(cls, variables, equation): ...
    @property
    def variables(self): ...
    @property
    def equation(self): ...
    @property
    def degree(self): ...
    def regular_point(self):
        '''
        Returns a point on the implicit region.

        Examples
        ========

        >>> from sympy.abc import x, y, z
        >>> from sympy.vector import ImplicitRegion
        >>> circle = ImplicitRegion((x, y), (x + 2)**2 + (y - 3)**2 - 16)
        >>> circle.regular_point()
        (-2, -1)
        >>> parabola = ImplicitRegion((x, y), x**2 - 4*y)
        >>> parabola.regular_point()
        (0, 0)
        >>> r = ImplicitRegion((x, y, z), (x + y + z)**4)
        >>> r.regular_point()
        (-10, -10, 20)

        References
        ==========

        - Erik Hillgarter, "Rational Points on Conics", Diploma Thesis, RISC-Linz,
          J. Kepler Universitat Linz, 1996. Available:
          https://www3.risc.jku.at/publications/download/risc_1355/Rational%20Points%20on%20Conics.pdf

        '''
    def singular_points(self):
        """
        Returns a set of singular points of the region.

        The singular points are those points on the region
        where all partial derivatives vanish.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy.vector import ImplicitRegion
        >>> I = ImplicitRegion((x, y), (y-1)**2 -x**3 + 2*x**2 -x)
        >>> I.singular_points()
        {(1, 1)}

        """
    def multiplicity(self, point):
        """
        Returns the multiplicity of a singular point on the region.

        A singular point (x,y) of region is said to be of multiplicity m
        if all the partial derivatives off to order m - 1 vanish there.

        Examples
        ========

        >>> from sympy.abc import x, y, z
        >>> from sympy.vector import ImplicitRegion
        >>> I = ImplicitRegion((x, y, z), x**2 + y**3 - z**4)
        >>> I.singular_points()
        {(0, 0, 0)}
        >>> I.multiplicity((0, 0, 0))
        2

        """
    def rational_parametrization(self, parameters=('t', 's'), reg_point: Incomplete | None = None):
        '''
        Returns the rational parametrization of implicit region.

        Examples
        ========

        >>> from sympy import Eq
        >>> from sympy.abc import x, y, z, s, t
        >>> from sympy.vector import ImplicitRegion

        >>> parabola = ImplicitRegion((x, y), y**2 - 4*x)
        >>> parabola.rational_parametrization()
        (4/t**2, 4/t)

        >>> circle = ImplicitRegion((x, y), Eq(x**2 + y**2, 4))
        >>> circle.rational_parametrization()
        (4*t/(t**2 + 1), 4*t**2/(t**2 + 1) - 2)

        >>> I = ImplicitRegion((x, y), x**3 + x**2 - y**2)
        >>> I.rational_parametrization()
        (t**2 - 1, t*(t**2 - 1))

        >>> cubic_curve = ImplicitRegion((x, y), x**3 + x**2 - y**2)
        >>> cubic_curve.rational_parametrization(parameters=(t))
        (t**2 - 1, t*(t**2 - 1))

        >>> sphere = ImplicitRegion((x, y, z), x**2 + y**2 + z**2 - 4)
        >>> sphere.rational_parametrization(parameters=(t, s))
        (-2 + 4/(s**2 + t**2 + 1), 4*s/(s**2 + t**2 + 1), 4*t/(s**2 + t**2 + 1))

        For some conics, regular_points() is unable to find a point on curve.
        To calulcate the parametric representation in such cases, user need
        to determine a point on the region and pass it using reg_point.

        >>> c = ImplicitRegion((x, y), (x  - 1/2)**2 + (y)**2 - (1/4)**2)
        >>> c.rational_parametrization(reg_point=(3/4, 0))
        (0.75 - 0.5/(t**2 + 1), -0.5*t/(t**2 + 1))

        References
        ==========

        - Christoph M. Hoffmann, "Conversion Methods between Parametric and
          Implicit Curves and Surfaces", Purdue e-Pubs, 1990. Available:
          https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1827&context=cstech

        '''

def conic_coeff(variables, equation): ...
