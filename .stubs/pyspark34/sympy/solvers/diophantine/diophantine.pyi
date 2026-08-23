from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['diophantine', 'classify_diop']

class DiophantineSolutionSet(set):
    """
    Container for a set of solutions to a particular diophantine equation.

    The base representation is a set of tuples representing each of the solutions.

    Parameters
    ==========

    symbols : list
        List of free symbols in the original equation.
    parameters: list
        List of parameters to be used in the solution.

    Examples
    ========

    Adding solutions:

        >>> from sympy.solvers.diophantine.diophantine import DiophantineSolutionSet
        >>> from sympy.abc import x, y, t, u
        >>> s1 = DiophantineSolutionSet([x, y], [t, u])
        >>> s1
        set()
        >>> s1.add((2, 3))
        >>> s1.add((-1, u))
        >>> s1
        {(-1, u), (2, 3)}
        >>> s2 = DiophantineSolutionSet([x, y], [t, u])
        >>> s2.add((3, 4))
        >>> s1.update(*s2)
        >>> s1
        {(-1, u), (2, 3), (3, 4)}

    Conversion of solutions into dicts:

        >>> list(s1.dict_iterator())
        [{x: -1, y: u}, {x: 2, y: 3}, {x: 3, y: 4}]

    Substituting values:

        >>> s3 = DiophantineSolutionSet([x, y], [t, u])
        >>> s3.add((t**2, t + u))
        >>> s3
        {(t**2, t + u)}
        >>> s3.subs({t: 2, u: 3})
        {(4, 5)}
        >>> s3.subs(t, -1)
        {(1, u - 1)}
        >>> s3.subs(t, 3)
        {(9, u + 3)}

    Evaluation at specific values. Positional arguments are given in the same order as the parameters:

        >>> s3(-2, 3)
        {(4, 1)}
        >>> s3(5)
        {(25, u + 5)}
        >>> s3(None, 2)
        {(t**2, t + 2)}
    """
    symbols: Incomplete
    parameters: Incomplete
    def __init__(self, symbols_seq, parameters) -> None: ...
    def add(self, solution) -> None: ...
    def update(self, *solutions) -> None: ...
    def dict_iterator(self) -> Generator[Incomplete, None, None]: ...
    def subs(self, *args, **kwargs): ...
    def __call__(self, *args): ...

class DiophantineEquationType:
    """
    Internal representation of a particular diophantine equation type.

    Parameters
    ==========

    equation :
        The diophantine equation that is being solved.
    free_symbols : list (optional)
        The symbols being solved for.

    Attributes
    ==========

    total_degree :
        The maximum of the degrees of all terms in the equation
    homogeneous :
        Does the equation contain a term of degree 0
    homogeneous_order :
        Does the equation contain any coefficient that is in the symbols being solved for
    dimension :
        The number of symbols being solved for
    """
    name: str
    equation: Incomplete
    free_symbols: Incomplete
    coeff: Incomplete
    total_degree: Incomplete
    homogeneous: Incomplete
    homogeneous_order: Incomplete
    dimension: Incomplete
    def __init__(self, equation, free_symbols: Incomplete | None = None) -> None: ...
    def matches(self):
        """
        Determine whether the given equation can be matched to the particular equation type.
        """
    @property
    def n_parameters(self): ...
    @property
    def parameters(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: Incomplete | None = None) -> DiophantineSolutionSet: ...
    def pre_solve(self, parameters: Incomplete | None = None) -> None: ...

class Univariate(DiophantineEquationType):
    """
    Representation of a univariate diophantine equation.

    A univariate diophantine equation is an equation of the form
    `a_{0} + a_{1}x + a_{2}x^2 + .. + a_{n}x^n = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x` is an integer variable.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import Univariate
    >>> from sympy.abc import x
    >>> Univariate((x - 2)*(x - 3)**2).solve() # solves equation (x - 2)*(x - 3)**2 == 0
    {(2,), (3,)}

    """
    name: str
    def matches(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: Incomplete | None = None): ...

class Linear(DiophantineEquationType):
    """
    Representation of a linear diophantine equation.

    A linear diophantine equation is an equation of the form `a_{1}x_{1} +
    a_{2}x_{2} + .. + a_{n}x_{n} = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x_{1}, x_{2}, ..x_{n}` are integer variables.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import Linear
    >>> from sympy.abc import x, y, z
    >>> l1 = Linear(2*x - 3*y - 5)
    >>> l1.matches() # is this equation linear
    True
    >>> l1.solve() # solves equation 2*x - 3*y - 5 == 0
    {(3*t_0 - 5, 2*t_0 - 5)}

    Here x = -3*t_0 - 5 and y = -2*t_0 - 5

    >>> Linear(2*x - 3*y - 4*z -3).solve()
    {(t_0, 2*t_0 + 4*t_1 + 3, -t_0 - 3*t_1 - 3)}

    """
    name: str
    def matches(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: Incomplete | None = None): ...

class BinaryQuadratic(DiophantineEquationType):
    """
    Representation of a binary quadratic diophantine equation.

    A binary quadratic diophantine equation is an equation of the
    form `Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0`, where `A, B, C, D, E,
    F` are integer constants and `x` and `y` are integer variables.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.solvers.diophantine.diophantine import BinaryQuadratic
    >>> b1 = BinaryQuadratic(x**3 + y**2 + 1)
    >>> b1.matches()
    False
    >>> b2 = BinaryQuadratic(x**2 + y**2 + 2*x + 2*y + 2)
    >>> b2.matches()
    True
    >>> b2.solve()
    {(-1, -1)}

    References
    ==========

    .. [1] Methods to solve Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, [online],
          Available: https://www.alpertron.com.ar/METHODS.HTM
    .. [2] Solving the equation ax^2+ bxy + cy^2 + dx + ey + f= 0, [online],
          Available: https://web.archive.org/web/20160323033111/http://www.jpr2718.org/ax2p.pdf

    """
    name: str
    def matches(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: Incomplete | None = None) -> DiophantineSolutionSet: ...

class InhomogeneousTernaryQuadratic(DiophantineEquationType):
    """

    Representation of an inhomogeneous ternary quadratic.

    No solver is currently implemented for this equation type.

    """
    name: str
    def matches(self): ...

class HomogeneousTernaryQuadraticNormal(DiophantineEquationType):
    """
    Representation of a homogeneous ternary quadratic normal diophantine equation.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.solvers.diophantine.diophantine import HomogeneousTernaryQuadraticNormal
    >>> HomogeneousTernaryQuadraticNormal(4*x**2 - 5*y**2 + z**2).solve()
    {(1, 2, 4)}

    """
    name: str
    def matches(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: Incomplete | None = None) -> DiophantineSolutionSet: ...

class HomogeneousTernaryQuadratic(DiophantineEquationType):
    """
    Representation of a homogeneous ternary quadratic diophantine equation.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.solvers.diophantine.diophantine import HomogeneousTernaryQuadratic
    >>> HomogeneousTernaryQuadratic(x**2 + y**2 - 3*z**2 + x*y).solve()
    {(-1, 2, 1)}
    >>> HomogeneousTernaryQuadratic(3*x**2 + y**2 - 3*z**2 + 5*x*y + y*z).solve()
    {(3, 12, 13)}

    """
    name: str
    def matches(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: Incomplete | None = None): ...

class InhomogeneousGeneralQuadratic(DiophantineEquationType):
    """

    Representation of an inhomogeneous general quadratic.

    No solver is currently implemented for this equation type.

    """
    name: str
    def matches(self): ...

class HomogeneousGeneralQuadratic(DiophantineEquationType):
    """

    Representation of a homogeneous general quadratic.

    No solver is currently implemented for this equation type.

    """
    name: str
    def matches(self): ...

class GeneralSumOfSquares(DiophantineEquationType):
    """
    Representation of the diophantine equation

    `x_{1}^2 + x_{2}^2 + . . . + x_{n}^2 - k = 0`.

    Details
    =======

    When `n = 3` if `k = 4^a(8m + 7)` for some `a, m \\in Z` then there will be
    no solutions. Refer [1]_ for more details.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import GeneralSumOfSquares
    >>> from sympy.abc import a, b, c, d, e
    >>> GeneralSumOfSquares(a**2 + b**2 + c**2 + d**2 + e**2 - 2345).solve()
    {(15, 22, 22, 24, 24)}

    By default only 1 solution is returned. Use the `limit` keyword for more:

    >>> sorted(GeneralSumOfSquares(a**2 + b**2 + c**2 + d**2 + e**2 - 2345).solve(limit=3))
    [(15, 22, 22, 24, 24), (16, 19, 24, 24, 24), (16, 20, 22, 23, 26)]

    References
    ==========

    .. [1] Representing an integer as a sum of three squares, [online],
        Available:
        https://www.proofwiki.org/wiki/Integer_as_Sum_of_Three_Squares
    """
    name: str
    def matches(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: int = 1): ...

class GeneralPythagorean(DiophantineEquationType):
    """
    Representation of the general pythagorean equation,
    `a_{1}^2x_{1}^2 + a_{2}^2x_{2}^2 + . . . + a_{n}^2x_{n}^2 - a_{n + 1}^2x_{n + 1}^2 = 0`.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import GeneralPythagorean
    >>> from sympy.abc import a, b, c, d, e, x, y, z, t
    >>> GeneralPythagorean(a**2 + b**2 + c**2 - d**2).solve()
    {(t_0**2 + t_1**2 - t_2**2, 2*t_0*t_2, 2*t_1*t_2, t_0**2 + t_1**2 + t_2**2)}
    >>> GeneralPythagorean(9*a**2 - 4*b**2 + 16*c**2 + 25*d**2 + e**2).solve(parameters=[x, y, z, t])
    {(-10*t**2 + 10*x**2 + 10*y**2 + 10*z**2, 15*t**2 + 15*x**2 + 15*y**2 + 15*z**2, 15*t*x, 12*t*y, 60*t*z)}
    """
    name: str
    def matches(self): ...
    @property
    def n_parameters(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: int = 1): ...

class CubicThue(DiophantineEquationType):
    """
    Representation of a cubic Thue diophantine equation.

    A cubic Thue diophantine equation is a polynomial of the form
    `f(x, y) = r` of degree 3, where `x` and `y` are integers
    and `r` is a rational number.

    No solver is currently implemented for this equation type.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.solvers.diophantine.diophantine import CubicThue
    >>> c1 = CubicThue(x**3 + y**2 + 1)
    >>> c1.matches()
    True

    """
    name: str
    def matches(self): ...

class GeneralSumOfEvenPowers(DiophantineEquationType):
    """
    Representation of the diophantine equation

    `x_{1}^e + x_{2}^e + . . . + x_{n}^e - k = 0`

    where `e` is an even, integer power.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import GeneralSumOfEvenPowers
    >>> from sympy.abc import a, b
    >>> GeneralSumOfEvenPowers(a**4 + b**4 - (2**4 + 3**4)).solve()
    {(2, 3)}

    """
    name: str
    def matches(self): ...
    def solve(self, parameters: Incomplete | None = None, limit: int = 1): ...

def diophantine(eq, param=..., syms: Incomplete | None = None, permute: bool = False):
    """
    Simplify the solution procedure of diophantine equation ``eq`` by
    converting it into a product of terms which should equal zero.

    Explanation
    ===========

    For example, when solving, `x^2 - y^2 = 0` this is treated as
    `(x + y)(x - y) = 0` and `x + y = 0` and `x - y = 0` are solved
    independently and combined. Each term is solved by calling
    ``diop_solve()``. (Although it is possible to call ``diop_solve()``
    directly, one must be careful to pass an equation in the correct
    form and to interpret the output correctly; ``diophantine()`` is
    the public-facing function to use in general.)

    Output of ``diophantine()`` is a set of tuples. The elements of the
    tuple are the solutions for each variable in the equation and
    are arranged according to the alphabetic ordering of the variables.
    e.g. For an equation with two variables, `a` and `b`, the first
    element of the tuple is the solution for `a` and the second for `b`.

    Usage
    =====

    ``diophantine(eq, t, syms)``: Solve the diophantine
    equation ``eq``.
    ``t`` is the optional parameter to be used by ``diop_solve()``.
    ``syms`` is an optional list of symbols which determines the
    order of the elements in the returned tuple.

    By default, only the base solution is returned. If ``permute`` is set to
    True then permutations of the base solution and/or permutations of the
    signs of the values will be returned when applicable.

    Details
    =======

    ``eq`` should be an expression which is assumed to be zero.
    ``t`` is the parameter to be used in the solution.

    Examples
    ========

    >>> from sympy import diophantine
    >>> from sympy.abc import a, b
    >>> eq = a**4 + b**4 - (2**4 + 3**4)
    >>> diophantine(eq)
    {(2, 3)}
    >>> diophantine(eq, permute=True)
    {(-3, -2), (-3, 2), (-2, -3), (-2, 3), (2, -3), (2, 3), (3, -2), (3, 2)}

    >>> from sympy.abc import x, y, z
    >>> diophantine(x**2 - y**2)
    {(t_0, -t_0), (t_0, t_0)}

    >>> diophantine(x*(2*x + 3*y - z))
    {(0, n1, n2), (t_0, t_1, 2*t_0 + 3*t_1)}
    >>> diophantine(x**2 + 3*x*y + 4*x)
    {(0, n1), (3*t_0 - 4, -t_0)}

    See Also
    ========

    diop_solve
    sympy.utilities.iterables.permute_signs
    sympy.utilities.iterables.signed_permutations
    """
def classify_diop(eq, _dict: bool = True): ...
sum_of_powers = power_representation
