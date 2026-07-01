from .holonomicerrors import NotHolonomicError as NotHolonomicError, NotHyperSeriesError as NotHyperSeriesError, NotPowerSeriesError as NotPowerSeriesError, SingularityError as SingularityError
from .recurrence import HolonomicSequence as HolonomicSequence, RecurrenceOperator as RecurrenceOperator, RecurrenceOperators as RecurrenceOperators
from _typeshed import Incomplete
from sympy.core import Add as Add, Mul as Mul, Pow as Pow
from sympy.core.numbers import Float as Float, I as I, Infinity as Infinity, NaN as NaN, NegativeInfinity as NegativeInfinity, equal_valued as equal_valued, pi as pi
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import binomial as binomial, factorial as factorial, rf as rf
from sympy.functions.elementary.exponential import exp as exp, exp_polar as exp_polar, log as log
from sympy.functions.elementary.hyperbolic import cosh as cosh, sinh as sinh
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin, sinc as sinc
from sympy.functions.special.error_functions import Ci as Ci, Shi as Shi, Si as Si, erf as erf, erfc as erfc, erfi as erfi
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.functions.special.hyper import hyper as hyper, meijerg as meijerg
from sympy.integrals import meijerint as meijerint
from sympy.matrices import Matrix as Matrix
from sympy.polys.domains import QQ as QQ, RR as RR
from sympy.polys.fields import FracElement as FracElement
from sympy.polys.matrices import DomainMatrix as DomainMatrix
from sympy.polys.polyclasses import DMF as DMF
from sympy.polys.polyroots import roots as roots
from sympy.polys.polytools import Poly as Poly
from sympy.polys.rings import PolyElement as PolyElement
from sympy.printing import sstr as sstr
from sympy.series.limits import limit as limit
from sympy.series.order import Order as Order
from sympy.simplify.hyperexpand import hyperexpand as hyperexpand
from sympy.simplify.simplify import nsimplify as nsimplify
from sympy.solvers.solvers import solve as solve

def DifferentialOperators(base, generator):
    '''
    This function is used to create annihilators using ``Dx``.

    Explanation
    ===========

    Returns an Algebra of Differential Operators also called Weyl Algebra
    and the operator for differentiation i.e. the ``Dx`` operator.

    Parameters
    ==========

    base:
        Base polynomial ring for the algebra.
        The base polynomial ring is the ring of polynomials in :math:`x` that
        will appear as coefficients in the operators.
    generator:
        Generator of the algebra which can
        be either a noncommutative ``Symbol`` or a string. e.g. "Dx" or "D".

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy.abc import x
    >>> from sympy.holonomic.holonomic import DifferentialOperators
    >>> R, Dx = DifferentialOperators(ZZ.old_poly_ring(x), \'Dx\')
    >>> R
    Univariate Differential Operator Algebra in intermediate Dx over the base ring ZZ[x]
    >>> Dx*x
    (1) + (x)*Dx
    '''

class DifferentialOperatorAlgebra:
    """
    An Ore Algebra is a set of noncommutative polynomials in the
    intermediate ``Dx`` and coefficients in a base polynomial ring :math:`A`.
    It follows the commutation rule:

    .. math ::
       Dxa = \\sigma(a)Dx + \\delta(a)

    for :math:`a \\subset A`.

    Where :math:`\\sigma: A \\Rightarrow A` is an endomorphism and :math:`\\delta: A \\rightarrow A`
    is a skew-derivation i.e. :math:`\\delta(ab) = \\delta(a) b + \\sigma(a) \\delta(b)`.

    If one takes the sigma as identity map and delta as the standard derivation
    then it becomes the algebra of Differential Operators also called
    a Weyl Algebra i.e. an algebra whose elements are Differential Operators.

    This class represents a Weyl Algebra and serves as the parent ring for
    Differential Operators.

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy import symbols
    >>> from sympy.holonomic.holonomic import DifferentialOperators
    >>> x = symbols('x')
    >>> R, Dx = DifferentialOperators(ZZ.old_poly_ring(x), 'Dx')
    >>> R
    Univariate Differential Operator Algebra in intermediate Dx over the base ring
    ZZ[x]

    See Also
    ========

    DifferentialOperator
    """
    base: Incomplete
    derivative_operator: Incomplete
    gen_symbol: Incomplete
    def __init__(self, base, generator) -> None: ...
    def __eq__(self, other): ...

class DifferentialOperator:
    """
    Differential Operators are elements of Weyl Algebra. The Operators
    are defined by a list of polynomials in the base ring and the
    parent ring of the Operator i.e. the algebra it belongs to.

    Explanation
    ===========

    Takes a list of polynomials for each power of ``Dx`` and the
    parent ring which must be an instance of DifferentialOperatorAlgebra.

    A Differential Operator can be created easily using
    the operator ``Dx``. See examples below.

    Examples
    ========

    >>> from sympy.holonomic.holonomic import DifferentialOperator, DifferentialOperators
    >>> from sympy import ZZ
    >>> from sympy import symbols
    >>> x = symbols('x')
    >>> R, Dx = DifferentialOperators(ZZ.old_poly_ring(x),'Dx')

    >>> DifferentialOperator([0, 1, x**2], R)
    (1)*Dx + (x**2)*Dx**2

    >>> (x*Dx*x + 1 - Dx**2)**2
    (2*x**2 + 2*x + 1) + (4*x**3 + 2*x**2 - 4)*Dx + (x**4 - 6*x - 2)*Dx**2 + (-2*x**2)*Dx**3 + (1)*Dx**4

    See Also
    ========

    DifferentialOperatorAlgebra
    """
    parent: Incomplete
    x: Incomplete
    listofpoly: Incomplete
    order: Incomplete
    def __init__(self, list_of_poly, parent) -> None:
        """
        Parameters
        ==========

        list_of_poly:
            List of polynomials belonging to the base ring of the algebra.
        parent:
            Parent algebra of the operator.
        """
    def __mul__(self, other):
        """
        Multiplies two DifferentialOperator and returns another
        DifferentialOperator instance using the commutation rule
        Dx*a = a*Dx + a'
        """
    def __rmul__(self, other): ...
    def __add__(self, other): ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __neg__(self): ...
    def __truediv__(self, other): ...
    def __pow__(self, n): ...
    def __eq__(self, other): ...
    def is_singular(self, x0):
        """
        Checks if the differential equation is singular at x0.
        """

class HolonomicFunction:
    '''
    A Holonomic Function is a solution to a linear homogeneous ordinary
    differential equation with polynomial coefficients. This differential
    equation can also be represented by an annihilator i.e. a Differential
    Operator ``L`` such that :math:`L.f = 0`. For uniqueness of these functions,
    initial conditions can also be provided along with the annihilator.

    Explanation
    ===========

    Holonomic functions have closure properties and thus forms a ring.
    Given two Holonomic Functions f and g, their sum, product,
    integral and derivative is also a Holonomic Function.

    For ordinary points initial condition should be a vector of values of
    the derivatives i.e. :math:`[y(x_0), y\'(x_0), y\'\'(x_0) ... ]`.

    For regular singular points initial conditions can also be provided in this
    format:
    :math:`{s0: [C_0, C_1, ...], s1: [C^1_0, C^1_1, ...], ...}`
    where s0, s1, ... are the roots of indicial equation and vectors
    :math:`[C_0, C_1, ...], [C^0_0, C^0_1, ...], ...` are the corresponding initial
    terms of the associated power series. See Examples below.

    Examples
    ========

    >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
    >>> from sympy import QQ
    >>> from sympy import symbols, S
    >>> x = symbols(\'x\')
    >>> R, Dx = DifferentialOperators(QQ.old_poly_ring(x),\'Dx\')

    >>> p = HolonomicFunction(Dx - 1, x, 0, [1])  # e^x
    >>> q = HolonomicFunction(Dx**2 + 1, x, 0, [0, 1])  # sin(x)

    >>> p + q  # annihilator of e^x + sin(x)
    HolonomicFunction((-1) + (1)*Dx + (-1)*Dx**2 + (1)*Dx**3, x, 0, [1, 2, 1])

    >>> p * q  # annihilator of e^x * sin(x)
    HolonomicFunction((2) + (-2)*Dx + (1)*Dx**2, x, 0, [0, 1])

    An example of initial conditions for regular singular points,
    the indicial equation has only one root `1/2`.

    >>> HolonomicFunction(-S(1)/2 + x*Dx, x, 0, {S(1)/2: [1]})
    HolonomicFunction((-1/2) + (x)*Dx, x, 0, {1/2: [1]})

    >>> HolonomicFunction(-S(1)/2 + x*Dx, x, 0, {S(1)/2: [1]}).to_expr()
    sqrt(x)

    To plot a Holonomic Function, one can use `.evalf()` for numerical
    computation. Here\'s an example on `sin(x)**2/x` using numpy and matplotlib.

    >>> import sympy.holonomic # doctest: +SKIP
    >>> from sympy import var, sin # doctest: +SKIP
    >>> import matplotlib.pyplot as plt # doctest: +SKIP
    >>> import numpy as np # doctest: +SKIP
    >>> var("x") # doctest: +SKIP
    >>> r = np.linspace(1, 5, 100) # doctest: +SKIP
    >>> y = sympy.holonomic.expr_to_holonomic(sin(x)**2/x, x0=1).evalf(r) # doctest: +SKIP
    >>> plt.plot(r, y, label="holonomic function") # doctest: +SKIP
    >>> plt.show() # doctest: +SKIP

    '''
    y0: Incomplete
    x0: Incomplete
    annihilator: Incomplete
    x: Incomplete
    def __init__(self, annihilator, x, x0: int = 0, y0: Incomplete | None = None) -> None:
        """

        Parameters
        ==========

        annihilator:
            Annihilator of the Holonomic Function, represented by a
            `DifferentialOperator` object.
        x:
            Variable of the function.
        x0:
            The point at which initial conditions are stored.
            Generally an integer.
        y0:
            The initial condition. The proper format for the initial condition
            is described in class docstring. To make the function unique,
            length of the vector `y0` should be equal to or greater than the
            order of differential equation.
        """
    def unify(self, other):
        """
        Unifies the base polynomial ring of a given two Holonomic
        Functions.
        """
    def is_singularics(self):
        """
        Returns True if the function have singular initial condition
        in the dictionary format.

        Returns False if the function have ordinary initial condition
        in the list format.

        Returns None for all other cases.
        """
    def __add__(self, other): ...
    def integrate(self, limits, initcond: bool = False):
        """
        Integrates the given holonomic function.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import QQ
        >>> from sympy import symbols
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(QQ.old_poly_ring(x),'Dx')
        >>> HolonomicFunction(Dx - 1, x, 0, [1]).integrate((x, 0, x))  # e^x - 1
        HolonomicFunction((-1)*Dx + (1)*Dx**2, x, 0, [0, 1])
        >>> HolonomicFunction(Dx**2 + 1, x, 0, [1, 0]).integrate((x, 0, x))
        HolonomicFunction((1)*Dx + (1)*Dx**3, x, 0, [0, 1, 0])
        """
    def diff(self, *args, **kwargs):
        """
        Differentiation of the given Holonomic function.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import ZZ
        >>> from sympy import symbols
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(ZZ.old_poly_ring(x),'Dx')
        >>> HolonomicFunction(Dx**2 + 1, x, 0, [0, 1]).diff().to_expr()
        cos(x)
        >>> HolonomicFunction(Dx - 2, x, 0, [1]).diff().to_expr()
        2*exp(2*x)

        See Also
        ========

        integrate
        """
    def __eq__(self, other): ...
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __neg__(self): ...
    def __truediv__(self, other): ...
    def __pow__(self, n): ...
    def degree(self):
        """
        Returns the highest power of `x` in the annihilator.
        """
    def composition(self, expr, *args, **kwargs):
        """
        Returns function after composition of a holonomic
        function with an algebraic function. The method cannot compute
        initial conditions for the result by itself, so they can be also be
        provided.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import QQ
        >>> from sympy import symbols
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(QQ.old_poly_ring(x),'Dx')
        >>> HolonomicFunction(Dx - 1, x).composition(x**2, 0, [1])  # e^(x**2)
        HolonomicFunction((-2*x) + (1)*Dx, x, 0, [1])
        >>> HolonomicFunction(Dx**2 + 1, x).composition(x**2 - 1, 1, [1, 0])
        HolonomicFunction((4*x**3) + (-1)*Dx + (x)*Dx**2, x, 1, [1, 0])

        See Also
        ========

        from_hyper
        """
    def to_sequence(self, lb: bool = True):
        """
        Finds recurrence relation for the coefficients in the series expansion
        of the function about :math:`x_0`, where :math:`x_0` is the point at
        which the initial condition is stored.

        Explanation
        ===========

        If the point :math:`x_0` is ordinary, solution of the form :math:`[(R, n_0)]`
        is returned. Where :math:`R` is the recurrence relation and :math:`n_0` is the
        smallest ``n`` for which the recurrence holds true.

        If the point :math:`x_0` is regular singular, a list of solutions in
        the format :math:`(R, p, n_0)` is returned, i.e. `[(R, p, n_0), ... ]`.
        Each tuple in this vector represents a recurrence relation :math:`R`
        associated with a root of the indicial equation ``p``. Conditions of
        a different format can also be provided in this case, see the
        docstring of HolonomicFunction class.

        If it's not possible to numerically compute a initial condition,
        it is returned as a symbol :math:`C_j`, denoting the coefficient of
        :math:`(x - x_0)^j` in the power series about :math:`x_0`.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import QQ
        >>> from sympy import symbols, S
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(QQ.old_poly_ring(x),'Dx')
        >>> HolonomicFunction(Dx - 1, x, 0, [1]).to_sequence()
        [(HolonomicSequence((-1) + (n + 1)Sn, n), u(0) = 1, 0)]
        >>> HolonomicFunction((1 + x)*Dx**2 + Dx, x, 0, [0, 1]).to_sequence()
        [(HolonomicSequence((n**2) + (n**2 + n)Sn, n), u(0) = 0, u(1) = 1, u(2) = -1/2, 2)]
        >>> HolonomicFunction(-S(1)/2 + x*Dx, x, 0, {S(1)/2: [1]}).to_sequence()
        [(HolonomicSequence((n), n), u(0) = 1, 1/2, 1)]

        See Also
        ========

        HolonomicFunction.series

        References
        ==========

        .. [1] https://hal.inria.fr/inria-00070025/document
        .. [2] https://www3.risc.jku.at/publications/download/risc_2244/DIPLFORM.pdf

        """
    def series(self, n: int = 6, coefficient: bool = False, order: bool = True, _recur: Incomplete | None = None):
        """
        Finds the power series expansion of given holonomic function about :math:`x_0`.

        Explanation
        ===========

        A list of series might be returned if :math:`x_0` is a regular point with
        multiple roots of the indicial equation.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import QQ
        >>> from sympy import symbols
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(QQ.old_poly_ring(x),'Dx')
        >>> HolonomicFunction(Dx - 1, x, 0, [1]).series()  # e^x
        1 + x + x**2/2 + x**3/6 + x**4/24 + x**5/120 + O(x**6)
        >>> HolonomicFunction(Dx**2 + 1, x, 0, [0, 1]).series(n=8)  # sin(x)
        x - x**3/6 + x**5/120 - x**7/5040 + O(x**8)

        See Also
        ========

        HolonomicFunction.to_sequence
        """
    def evalf(self, points, method: str = 'RK4', h: float = 0.05, derivatives: bool = False):
        """
        Finds numerical value of a holonomic function using numerical methods.
        (RK4 by default). A set of points (real or complex) must be provided
        which will be the path for the numerical integration.

        Explanation
        ===========

        The path should be given as a list :math:`[x_1, x_2, \\dots x_n]`. The numerical
        values will be computed at each point in this order
        :math:`x_1 \\rightarrow x_2 \\rightarrow x_3 \\dots \\rightarrow x_n`.

        Returns values of the function at :math:`x_1, x_2, \\dots x_n` in a list.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import QQ
        >>> from sympy import symbols
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(QQ.old_poly_ring(x),'Dx')

        A straight line on the real axis from (0 to 1)

        >>> r = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

        Runge-Kutta 4th order on e^x from 0.1 to 1.
        Exact solution at 1 is 2.71828182845905

        >>> HolonomicFunction(Dx - 1, x, 0, [1]).evalf(r)
        [1.10517083333333, 1.22140257085069, 1.34985849706254, 1.49182424008069,
        1.64872063859684, 1.82211796209193, 2.01375162659678, 2.22553956329232,
        2.45960141378007, 2.71827974413517]

        Euler's method for the same

        >>> HolonomicFunction(Dx - 1, x, 0, [1]).evalf(r, method='Euler')
        [1.1, 1.21, 1.331, 1.4641, 1.61051, 1.771561, 1.9487171, 2.14358881,
        2.357947691, 2.5937424601]

        One can also observe that the value obtained using Runge-Kutta 4th order
        is much more accurate than Euler's method.
        """
    def change_x(self, z):
        """
        Changes only the variable of Holonomic Function, for internal
        purposes. For composition use HolonomicFunction.composition()
        """
    def shift_x(self, a):
        """
        Substitute `x + a` for `x`.
        """
    def to_hyper(self, as_list: bool = False, _recur: Incomplete | None = None):
        """
        Returns a hypergeometric function (or linear combination of them)
        representing the given holonomic function.

        Explanation
        ===========

        Returns an answer of the form:
        `a_1 \\cdot x^{b_1} \\cdot{hyper()} + a_2 \\cdot x^{b_2} \\cdot{hyper()} \\dots`

        This is very useful as one can now use ``hyperexpand`` to find the
        symbolic expressions/functions.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import ZZ
        >>> from sympy import symbols
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(ZZ.old_poly_ring(x),'Dx')
        >>> # sin(x)
        >>> HolonomicFunction(Dx**2 + 1, x, 0, [0, 1]).to_hyper()
        x*hyper((), (3/2,), -x**2/4)
        >>> # exp(x)
        >>> HolonomicFunction(Dx - 1, x, 0, [1]).to_hyper()
        hyper((), (), x)

        See Also
        ========

        from_hyper, from_meijerg
        """
    def to_expr(self):
        """
        Converts a Holonomic Function back to elementary functions.

        Examples
        ========

        >>> from sympy.holonomic.holonomic import HolonomicFunction, DifferentialOperators
        >>> from sympy import ZZ
        >>> from sympy import symbols, S
        >>> x = symbols('x')
        >>> R, Dx = DifferentialOperators(ZZ.old_poly_ring(x),'Dx')
        >>> HolonomicFunction(x**2*Dx**2 + x*Dx + (x**2 - 1), x, 0, [0, S(1)/2]).to_expr()
        besselj(1, x)
        >>> HolonomicFunction((1 + x)*Dx**3 + Dx**2, x, 0, [1, 1, 1]).to_expr()
        x*log(x + 1) + log(x + 1) + 1

        """
    def change_ics(self, b, lenics: Incomplete | None = None):
        """
        Changes the point `x0` to ``b`` for initial conditions.

        Examples
        ========

        >>> from sympy.holonomic import expr_to_holonomic
        >>> from sympy import symbols, sin, exp
        >>> x = symbols('x')

        >>> expr_to_holonomic(sin(x)).change_ics(1)
        HolonomicFunction((1) + (1)*Dx**2, x, 1, [sin(1), cos(1)])

        >>> expr_to_holonomic(exp(x)).change_ics(2)
        HolonomicFunction((-1) + (1)*Dx, x, 2, [exp(2)])
        """
    def to_meijerg(self):
        """
        Returns a linear combination of Meijer G-functions.

        Examples
        ========

        >>> from sympy.holonomic import expr_to_holonomic
        >>> from sympy import sin, cos, hyperexpand, log, symbols
        >>> x = symbols('x')
        >>> hyperexpand(expr_to_holonomic(cos(x) + sin(x)).to_meijerg())
        sin(x) + cos(x)
        >>> hyperexpand(expr_to_holonomic(log(x)).to_meijerg()).simplify()
        log(x)

        See Also
        ========

        to_hyper
        """

def from_hyper(func, x0: int = 0, evalf: bool = False):
    """
    Converts a hypergeometric function to holonomic.
    ``func`` is the Hypergeometric Function and ``x0`` is the point at
    which initial conditions are required.

    Examples
    ========

    >>> from sympy.holonomic.holonomic import from_hyper
    >>> from sympy import symbols, hyper, S
    >>> x = symbols('x')
    >>> from_hyper(hyper([], [S(3)/2], x**2/4))
    HolonomicFunction((-x) + (2)*Dx + (x)*Dx**2, x, 1, [sinh(1), -sinh(1) + cosh(1)])
    """
def from_meijerg(func, x0: int = 0, evalf: bool = False, initcond: bool = True, domain=...):
    """
    Converts a Meijer G-function to Holonomic.
    ``func`` is the G-Function and ``x0`` is the point at
    which initial conditions are required.

    Examples
    ========

    >>> from sympy.holonomic.holonomic import from_meijerg
    >>> from sympy import symbols, meijerg, S
    >>> x = symbols('x')
    >>> from_meijerg(meijerg(([], []), ([S(1)/2], [0]), x**2/4))
    HolonomicFunction((1) + (1)*Dx**2, x, 0, [0, 1/sqrt(pi)])
    """

x_1: Incomplete
domain_for_table: Incomplete

def expr_to_holonomic(func, x: Incomplete | None = None, x0: int = 0, y0: Incomplete | None = None, lenics: Incomplete | None = None, domain: Incomplete | None = None, initcond: bool = True):
    """
    Converts a function or an expression to a holonomic function.

    Parameters
    ==========

    func:
        The expression to be converted.
    x:
        variable for the function.
    x0:
        point at which initial condition must be computed.
    y0:
        One can optionally provide initial condition if the method
        is not able to do it automatically.
    lenics:
        Number of terms in the initial condition. By default it is
        equal to the order of the annihilator.
    domain:
        Ground domain for the polynomials in ``x`` appearing as coefficients
        in the annihilator.
    initcond:
        Set it false if you do not want the initial conditions to be computed.

    Examples
    ========

    >>> from sympy.holonomic.holonomic import expr_to_holonomic
    >>> from sympy import sin, exp, symbols
    >>> x = symbols('x')
    >>> expr_to_holonomic(sin(x))
    HolonomicFunction((1) + (1)*Dx**2, x, 0, [0, 1])
    >>> expr_to_holonomic(exp(x))
    HolonomicFunction((-1) + (1)*Dx, x, 0, [1])

    See Also
    ========

    sympy.integrals.meijerint._rewrite1, _convert_poly_rat_alg, _create_table
    """
def DMFdiff(frac): ...
def DMFsubs(frac, x0, mpm: bool = False): ...
