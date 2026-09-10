from _typeshed import Incomplete
from sympy.core import Add as Add, Dummy as Dummy, Expr as Expr, Mul as Mul, S as S, Symbol as Symbol
from sympy.core.assumptions import check_assumptions as check_assumptions
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function, UndefinedFunction as UndefinedFunction, expand as expand, expand_func as expand_func, expand_log as expand_log, expand_mul as expand_mul, expand_power_exp as expand_power_exp, nfloat as nfloat
from sympy.core.logic import fuzzy_not as fuzzy_not
from sympy.core.numbers import Float as Float, Rational as Rational, ilcm as ilcm
from sympy.core.power import Pow as Pow, integer_log as integer_log
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.sympify import sympify as sympify
from sympy.core.traversal import preorder_traversal as preorder_traversal
from sympy.functions import Abs as Abs, LambertW as LambertW, acos as acos, arg as arg, asin as asin, atan as atan, atan2 as atan2, cos as cos, exp as exp, im as im, log as log, re as re, sin as sin, sqrt as sqrt, tan as tan
from sympy.functions.combinatorial.factorials import binomial as binomial
from sympy.functions.elementary.hyperbolic import HyperbolicFunction as HyperbolicFunction
from sympy.functions.elementary.piecewise import Piecewise as Piecewise, piecewise_fold as piecewise_fold
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction
from sympy.integrals.integrals import Integral as Integral
from sympy.logic.boolalg import And as And, BooleanAtom as BooleanAtom
from sympy.matrices import Matrix as Matrix, zeros as zeros
from sympy.matrices.common import NonInvertibleMatrixError as NonInvertibleMatrixError
from sympy.ntheory.factor_ import divisors as divisors
from sympy.polys import Poly as Poly, cancel as cancel, factor as factor, roots as roots
from sympy.polys.polyerrors import GeneratorsNeeded as GeneratorsNeeded, PolynomialError as PolynomialError
from sympy.polys.solvers import solve_lin_sys as solve_lin_sys, sympy_eqs_to_ring as sympy_eqs_to_ring
from sympy.simplify import collect as collect, denom as denom, fraction as fraction, logcombine as logcombine, nsimplify as nsimplify, posify as posify, powdenest as powdenest, powsimp as powsimp, separatevars as separatevars, simplify as simplify, sqrtdenest as sqrtdenest
from sympy.simplify.fu import TR1 as TR1, TR2i as TR2i
from sympy.simplify.sqrtdenest import sqrt_depth as sqrt_depth
from sympy.solvers.bivariate import bivariate_type as bivariate_type
from sympy.solvers.polysys import solve_poly_system as solve_poly_system
from sympy.utilities.decorator import conserve_mpmath_dps as conserve_mpmath_dps
from sympy.utilities.iterables import connected_components as connected_components, flatten as flatten, generate_bell as generate_bell, is_sequence as is_sequence, iterable as iterable, subsets as subsets, uniq as uniq
from sympy.utilities.lambdify import lambdify as lambdify
from sympy.utilities.misc import debugf as debugf, filldedent as filldedent

def recast_to_symbols(eqs, symbols):
    """
    Return (e, s, d) where e and s are versions of *eqs* and
    *symbols* in which any non-Symbol objects in *symbols* have
    been replaced with generic Dummy symbols and d is a dictionary
    that can be used to restore the original expressions.

    Examples
    ========

    >>> from sympy.solvers.solvers import recast_to_symbols
    >>> from sympy import symbols, Function
    >>> x, y = symbols('x y')
    >>> fx = Function('f')(x)
    >>> eqs, syms = [fx + 1, x, y], [fx, y]
    >>> e, s, d = recast_to_symbols(eqs, syms); (e, s, d)
    ([_X0 + 1, x, y], [_X0, y], {_X0: f(x)})

    The original equations and symbols can be restored using d:

    >>> assert [i.xreplace(d) for i in eqs] == eqs
    >>> assert [d.get(i, i) for i in s] == syms

    """
def denoms(eq, *symbols):
    """
    Return (recursively) set of all denominators that appear in *eq*
    that contain any symbol in *symbols*; if *symbols* are not
    provided then all denominators will be returned.

    Examples
    ========

    >>> from sympy.solvers.solvers import denoms
    >>> from sympy.abc import x, y, z

    >>> denoms(x/y)
    {y}

    >>> denoms(x/(y*z))
    {y, z}

    >>> denoms(3/x + y/z)
    {x, z}

    >>> denoms(x/2 + y/z)
    {2, z}

    If *symbols* are provided then only denominators containing
    those symbols will be returned:

    >>> denoms(1/x + 1/y + 1/z, y, z)
    {y, z}

    """
def checksol(f, symbol, sol: Incomplete | None = None, **flags):
    """
    Checks whether sol is a solution of equation f == 0.

    Explanation
    ===========

    Input can be either a single symbol and corresponding value
    or a dictionary of symbols and values. When given as a dictionary
    and flag ``simplify=True``, the values in the dictionary will be
    simplified. *f* can be a single equation or an iterable of equations.
    A solution must satisfy all equations in *f* to be considered valid;
    if a solution does not satisfy any equation, False is returned; if one or
    more checks are inconclusive (and none are False) then None is returned.

    Examples
    ========

    >>> from sympy import checksol, symbols
    >>> x, y = symbols('x,y')
    >>> checksol(x**4 - 1, x, 1)
    True
    >>> checksol(x**4 - 1, x, 0)
    False
    >>> checksol(x**2 + y**2 - 5**2, {x: 3, y: 4})
    True

    To check if an expression is zero using ``checksol()``, pass it
    as *f* and send an empty dictionary for *symbol*:

    >>> checksol(x**2 + x - x*(x + 1), {})
    True

    None is returned if ``checksol()`` could not conclude.

    flags:
        'numerical=True (default)'
           do a fast numerical check if ``f`` has only one symbol.
        'minimal=True (default is False)'
           a very fast, minimal testing.
        'warn=True (default is False)'
           show a warning if checksol() could not conclude.
        'simplify=True (default)'
           simplify solution before substituting into function and
           simplify the function before trying specific simplifications
        'force=True (default is False)'
           make positive all symbols without assumptions regarding sign.

    """
def solve(f, *symbols, **flags):
    '''
    Algebraically solves equations and systems of equations.

    Explanation
    ===========

    Currently supported:
        - polynomial
        - transcendental
        - piecewise combinations of the above
        - systems of linear and polynomial equations
        - systems containing relational expressions
        - systems implied by undetermined coefficients

    Examples
    ========

    The default output varies according to the input and might
    be a list (possibly empty), a dictionary, a list of
    dictionaries or tuples, or an expression involving relationals.
    For specifics regarding different forms of output that may appear, see :ref:`solve_output`.
    Let it suffice here to say that to obtain a uniform output from
    `solve` use ``dict=True`` or ``set=True`` (see below).

        >>> from sympy import solve, Poly, Eq, Matrix, Symbol
        >>> from sympy.abc import x, y, z, a, b

    The expressions that are passed can be Expr, Equality, or Poly
    classes (or lists of the same); a Matrix is considered to be a
    list of all the elements of the matrix:

        >>> solve(x - 3, x)
        [3]
        >>> solve(Eq(x, 3), x)
        [3]
        >>> solve(Poly(x - 3), x)
        [3]
        >>> solve(Matrix([[x, x + y]]), x, y) == solve([x, x + y], x, y)
        True

    If no symbols are indicated to be of interest and the equation is
    univariate, a list of values is returned; otherwise, the keys in
    a dictionary will indicate which (of all the variables used in
    the expression(s)) variables and solutions were found:

        >>> solve(x**2 - 4)
        [-2, 2]
        >>> solve((x - a)*(y - b))
        [{a: x}, {b: y}]
        >>> solve([x - 3, y - 1])
        {x: 3, y: 1}
        >>> solve([x - 3, y**2 - 1])
        [{x: 3, y: -1}, {x: 3, y: 1}]

    If you pass symbols for which solutions are sought, the output will vary
    depending on the number of symbols you passed, whether you are passing
    a list of expressions or not, and whether a linear system was solved.
    Uniform output is attained by using ``dict=True`` or ``set=True``.

        >>> #### *** feel free to skip to the stars below *** ####
        >>> from sympy import TableForm
        >>> h = [None, \';|;\'.join([\'e\', \'s\', \'solve(e, s)\', \'solve(e, s, dict=True)\',
        ... \'solve(e, s, set=True)\']).split(\';\')]
        >>> t = []
        >>> for e, s in [
        ...         (x - y, y),
        ...         (x - y, [x, y]),
        ...         (x**2 - y, [x, y]),
        ...         ([x - 3, y -1], [x, y]),
        ...         ]:
        ...     how = [{}, dict(dict=True), dict(set=True)]
        ...     res = [solve(e, s, **f) for f in how]
        ...     t.append([e, \'|\', s, \'|\'] + [res[0], \'|\', res[1], \'|\', res[2]])
        ...
        >>> # ******************************************************* #
        >>> TableForm(t, headings=h, alignments="<")
        e              | s      | solve(e, s)  | solve(e, s, dict=True) | solve(e, s, set=True)
        ---------------------------------------------------------------------------------------
        x - y          | y      | [x]          | [{y: x}]               | ([y], {(x,)})
        x - y          | [x, y] | [(y, y)]     | [{x: y}]               | ([x, y], {(y, y)})
        x**2 - y       | [x, y] | [(x, x**2)]  | [{y: x**2}]            | ([x, y], {(x, x**2)})
        [x - 3, y - 1] | [x, y] | {x: 3, y: 1} | [{x: 3, y: 1}]         | ([x, y], {(3, 1)})

        * If any equation does not depend on the symbol(s) given, it will be
          eliminated from the equation set and an answer may be given
          implicitly in terms of variables that were not of interest:

            >>> solve([x - y, y - 3], x)
            {x: y}

    When you pass all but one of the free symbols, an attempt
    is made to find a single solution based on the method of
    undetermined coefficients. If it succeeds, a dictionary of values
    is returned. If you want an algebraic solutions for one
    or more of the symbols, pass the expression to be solved in a list:

        >>> e = a*x + b - 2*x - 3
        >>> solve(e, [a, b])
        {a: 2, b: 3}
        >>> solve([e], [a, b])
        {a: -b/x + (2*x + 3)/x}

    When there is no solution for any given symbol which will make all
    expressions zero, the empty list is returned (or an empty set in
    the tuple when ``set=True``):

        >>> from sympy import sqrt
        >>> solve(3, x)
        []
        >>> solve(x - 3, y)
        []
        >>> solve(sqrt(x) + 1, x, set=True)
        ([x], set())

    When an object other than a Symbol is given as a symbol, it is
    isolated algebraically and an implicit solution may be obtained.
    This is mostly provided as a convenience to save you from replacing
    the object with a Symbol and solving for that Symbol. It will only
    work if the specified object can be replaced with a Symbol using the
    subs method:

        >>> from sympy import exp, Function
        >>> f = Function(\'f\')

        >>> solve(f(x) - x, f(x))
        [x]
        >>> solve(f(x).diff(x) - f(x) - x, f(x).diff(x))
        [x + f(x)]
        >>> solve(f(x).diff(x) - f(x) - x, f(x))
        [-x + Derivative(f(x), x)]
        >>> solve(x + exp(x)**2, exp(x), set=True)
        ([exp(x)], {(-sqrt(-x),), (sqrt(-x),)})

        >>> from sympy import Indexed, IndexedBase, Tuple
        >>> A = IndexedBase(\'A\')
        >>> eqs = Tuple(A[1] + A[2] - 3, A[1] - A[2] + 1)
        >>> solve(eqs, eqs.atoms(Indexed))
        {A[1]: 1, A[2]: 2}

        * To solve for a function within a derivative, use :func:`~.dsolve`.

    To solve for a symbol implicitly, use implicit=True:

        >>> solve(x + exp(x), x)
        [-LambertW(1)]
        >>> solve(x + exp(x), x, implicit=True)
        [-exp(x)]

    It is possible to solve for anything in an expression that can be
    replaced with a symbol using :obj:`~sympy.core.basic.Basic.subs`:

        >>> solve(x + 2 + sqrt(3), x + 2)
        [-sqrt(3)]
        >>> solve((x + 2 + sqrt(3), x + 4 + y), y, x + 2)
        {y: -2 + sqrt(3), x + 2: -sqrt(3)}

        * Nothing heroic is done in this implicit solving so you may end up
          with a symbol still in the solution:

            >>> eqs = (x*y + 3*y + sqrt(3), x + 4 + y)
            >>> solve(eqs, y, x + 2)
            {y: -sqrt(3)/(x + 3), x + 2: -2*x/(x + 3) - 6/(x + 3) + sqrt(3)/(x + 3)}
            >>> solve(eqs, y*x, x)
            {x: -y - 4, x*y: -3*y - sqrt(3)}

        * If you attempt to solve for a number, remember that the number
          you have obtained does not necessarily mean that the value is
          equivalent to the expression obtained:

            >>> solve(sqrt(2) - 1, 1)
            [sqrt(2)]
            >>> solve(x - y + 1, 1)  # /!\\ -1 is targeted, too
            [x/(y - 1)]
            >>> [_.subs(z, -1) for _ in solve((x - y + 1).subs(-1, z), 1)]
            [-x + y]

    **Additional Examples**

    ``solve()`` with check=True (default) will run through the symbol tags to
    eliminate unwanted solutions. If no assumptions are included, all possible
    solutions will be returned:

        >>> x = Symbol("x")
        >>> solve(x**2 - 1)
        [-1, 1]

    By setting the ``positive`` flag, only one solution will be returned:

        >>> pos = Symbol("pos", positive=True)
        >>> solve(pos**2 - 1)
        [1]

    When the solutions are checked, those that make any denominator zero
    are automatically excluded. If you do not want to exclude such solutions,
    then use the check=False option:

        >>> from sympy import sin, limit
        >>> solve(sin(x)/x)  # 0 is excluded
        [pi]

    If ``check=False``, then a solution to the numerator being zero is found
    but the value of $x = 0$ is a spurious solution since $\\sin(x)/x$ has the well
    known limit (without discontinuity) of 1 at $x = 0$:

        >>> solve(sin(x)/x, check=False)
        [0, pi]

    In the following case, however, the limit exists and is equal to the
    value of $x = 0$ that is excluded when check=True:

        >>> eq = x**2*(1/x - z**2/x)
        >>> solve(eq, x)
        []
        >>> solve(eq, x, check=False)
        [0]
        >>> limit(eq, x, 0, \'-\')
        0
        >>> limit(eq, x, 0, \'+\')
        0

    **Solving Relationships**

    When one or more expressions passed to ``solve`` is a relational,
    a relational result is returned (and the ``dict`` and ``set`` flags
    are ignored):

        >>> solve(x < 3)
        (-oo < x) & (x < 3)
        >>> solve([x < 3, x**2 > 4], x)
        ((-oo < x) & (x < -2)) | ((2 < x) & (x < 3))
        >>> solve([x + y - 3, x > 3], x)
        (3 < x) & (x < oo) & Eq(x, 3 - y)

    Although checking of assumptions on symbols in relationals
    is not done, setting assumptions will affect how certain
    relationals might automatically simplify:

        >>> solve(x**2 > 4)
        ((-oo < x) & (x < -2)) | ((2 < x) & (x < oo))

        >>> r = Symbol(\'r\', real=True)
        >>> solve(r**2 > 4)
        (2 < r) | (r < -2)

    There is currently no algorithm in SymPy that allows you to use
    relationships to resolve more than one variable. So the following
    does not determine that ``q < 0`` (and trying to solve for ``r``
    and ``q`` will raise an error):

        >>> from sympy import symbols
        >>> r, q = symbols(\'r, q\', real=True)
        >>> solve([r + q - 3, r > 3], r)
        (3 < r) & Eq(r, 3 - q)

    You can directly call the routine that ``solve`` calls
    when it encounters a relational: :func:`~.reduce_inequalities`.
    It treats Expr like Equality.

        >>> from sympy import reduce_inequalities
        >>> reduce_inequalities([x**2 - 4])
        Eq(x, -2) | Eq(x, 2)

    If each relationship contains only one symbol of interest,
    the expressions can be processed for multiple symbols:

        >>> reduce_inequalities([0 <= x  - 1, y < 3], [x, y])
        (-oo < y) & (1 <= x) & (x < oo) & (y < 3)

    But an error is raised if any relationship has more than one
    symbol of interest:

        >>> reduce_inequalities([0 <= x*y  - 1, y < 3], [x, y])
        Traceback (most recent call last):
        ...
        NotImplementedError:
        inequality has more than one symbol of interest.

    **Disabling High-Order Explicit Solutions**

    When solving polynomial expressions, you might not want explicit solutions
    (which can be quite long). If the expression is univariate, ``CRootOf``
    instances will be returned instead:

        >>> solve(x**3 - x + 1)
        [-1/((-1/2 - sqrt(3)*I/2)*(3*sqrt(69)/2 + 27/2)**(1/3)) -
        (-1/2 - sqrt(3)*I/2)*(3*sqrt(69)/2 + 27/2)**(1/3)/3,
        -(-1/2 + sqrt(3)*I/2)*(3*sqrt(69)/2 + 27/2)**(1/3)/3 -
        1/((-1/2 + sqrt(3)*I/2)*(3*sqrt(69)/2 + 27/2)**(1/3)),
        -(3*sqrt(69)/2 + 27/2)**(1/3)/3 -
        1/(3*sqrt(69)/2 + 27/2)**(1/3)]
        >>> solve(x**3 - x + 1, cubics=False)
        [CRootOf(x**3 - x + 1, 0),
         CRootOf(x**3 - x + 1, 1),
         CRootOf(x**3 - x + 1, 2)]

    If the expression is multivariate, no solution might be returned:

        >>> solve(x**3 - x + a, x, cubics=False)
        []

    Sometimes solutions will be obtained even when a flag is False because the
    expression could be factored. In the following example, the equation can
    be factored as the product of a linear and a quadratic factor so explicit
    solutions (which did not require solving a cubic expression) are obtained:

        >>> eq = x**3 + 3*x**2 + x - 1
        >>> solve(eq, cubics=False)
        [-1, -1 + sqrt(2), -sqrt(2) - 1]

    **Solving Equations Involving Radicals**

    Because of SymPy\'s use of the principle root, some solutions
    to radical equations will be missed unless check=False:

        >>> from sympy import root
        >>> eq = root(x**3 - 3*x**2, 3) + 1 - x
        >>> solve(eq)
        []
        >>> solve(eq, check=False)
        [1/3]

    In the above example, there is only a single solution to the
    equation. Other expressions will yield spurious roots which
    must be checked manually; roots which give a negative argument
    to odd-powered radicals will also need special checking:

        >>> from sympy import real_root, S
        >>> eq = root(x, 3) - root(x, 5) + S(1)/7
        >>> solve(eq)  # this gives 2 solutions but misses a 3rd
        [CRootOf(7*x**5 - 7*x**3 + 1, 1)**15,
        CRootOf(7*x**5 - 7*x**3 + 1, 2)**15]
        >>> sol = solve(eq, check=False)
        >>> [abs(eq.subs(x,i).n(2)) for i in sol]
        [0.48, 0.e-110, 0.e-110, 0.052, 0.052]

    The first solution is negative so ``real_root`` must be used to see that it
    satisfies the expression:

        >>> abs(real_root(eq.subs(x, sol[0])).n(2))
        0.e-110

    If the roots of the equation are not real then more care will be
    necessary to find the roots, especially for higher order equations.
    Consider the following expression:

        >>> expr = root(x, 3) - root(x, 5)

    We will construct a known value for this expression at x = 3 by selecting
    the 1-th root for each radical:

        >>> expr1 = root(x, 3, 1) - root(x, 5, 1)
        >>> v = expr1.subs(x, -3)

    The ``solve`` function is unable to find any exact roots to this equation:

        >>> eq = Eq(expr, v); eq1 = Eq(expr1, v)
        >>> solve(eq, check=False), solve(eq1, check=False)
        ([], [])

    The function ``unrad``, however, can be used to get a form of the equation
    for which numerical roots can be found:

        >>> from sympy.solvers.solvers import unrad
        >>> from sympy import nroots
        >>> e, (p, cov) = unrad(eq)
        >>> pvals = nroots(e)
        >>> inversion = solve(cov, x)[0]
        >>> xvals = [inversion.subs(p, i) for i in pvals]

    Although ``eq`` or ``eq1`` could have been used to find ``xvals``, the
    solution can only be verified with ``expr1``:

        >>> z = expr - v
        >>> [xi.n(chop=1e-9) for xi in xvals if abs(z.subs(x, xi).n()) < 1e-9]
        []
        >>> z1 = expr1 - v
        >>> [xi.n(chop=1e-9) for xi in xvals if abs(z1.subs(x, xi).n()) < 1e-9]
        [-3.0]

    Parameters
    ==========

    f :
        - a single Expr or Poly that must be zero
        - an Equality
        - a Relational expression
        - a Boolean
        - iterable of one or more of the above

    symbols : (object(s) to solve for) specified as
        - none given (other non-numeric objects will be used)
        - single symbol
        - denested list of symbols
          (e.g., ``solve(f, x, y)``)
        - ordered iterable of symbols
          (e.g., ``solve(f, [x, y])``)

    flags :
        dict=True (default is False)
            Return list (perhaps empty) of solution mappings.
        set=True (default is False)
            Return list of symbols and set of tuple(s) of solution(s).
        exclude=[] (default)
            Do not try to solve for any of the free symbols in exclude;
            if expressions are given, the free symbols in them will
            be extracted automatically.
        check=True (default)
            If False, do not do any testing of solutions. This can be
            useful if you want to include solutions that make any
            denominator zero.
        numerical=True (default)
            Do a fast numerical check if *f* has only one symbol.
        minimal=True (default is False)
            A very fast, minimal testing.
        warn=True (default is False)
            Show a warning if ``checksol()`` could not conclude.
        simplify=True (default)
            Simplify all but polynomials of order 3 or greater before
            returning them and (if check is not False) use the
            general simplify function on the solutions and the
            expression obtained when they are substituted into the
            function which should be zero.
        force=True (default is False)
            Make positive all symbols without assumptions regarding sign.
        rational=True (default)
            Recast Floats as Rational; if this option is not used, the
            system containing Floats may fail to solve because of issues
            with polys. If rational=None, Floats will be recast as
            rationals but the answer will be recast as Floats. If the
            flag is False then nothing will be done to the Floats.
        manual=True (default is False)
            Do not use the polys/matrix method to solve a system of
            equations, solve them one at a time as you might "manually."
        implicit=True (default is False)
            Allows ``solve`` to return a solution for a pattern in terms of
            other functions that contain that pattern; this is only
            needed if the pattern is inside of some invertible function
            like cos, exp, ect.
        particular=True (default is False)
            Instructs ``solve`` to try to find a particular solution to
            a linear system with as many zeros as possible; this is very
            expensive.
        quick=True (default is False; ``particular`` must be True)
            Selects a fast heuristic to find a solution with many zeros
            whereas a value of False uses the very slow method guaranteed
            to find the largest number of zeros possible.
        cubics=True (default)
            Return explicit solutions when cubic expressions are encountered.
            When False, quartics and quintics are disabled, too.
        quartics=True (default)
            Return explicit solutions when quartic expressions are encountered.
            When False, quintics are disabled, too.
        quintics=True (default)
            Return explicit solutions (if possible) when quintic expressions
            are encountered.

    See Also
    ========

    rsolve: For solving recurrence relationships
    dsolve: For solving differential equations

    '''
def solve_linear(lhs, rhs: int = 0, symbols=[], exclude=[]):
    """
    Return a tuple derived from ``f = lhs - rhs`` that is one of
    the following: ``(0, 1)``, ``(0, 0)``, ``(symbol, solution)``, ``(n, d)``.

    Explanation
    ===========

    ``(0, 1)`` meaning that ``f`` is independent of the symbols in *symbols*
    that are not in *exclude*.

    ``(0, 0)`` meaning that there is no solution to the equation amongst the
    symbols given. If the first element of the tuple is not zero, then the
    function is guaranteed to be dependent on a symbol in *symbols*.

    ``(symbol, solution)`` where symbol appears linearly in the numerator of
    ``f``, is in *symbols* (if given), and is not in *exclude* (if given). No
    simplification is done to ``f`` other than a ``mul=True`` expansion, so the
    solution will correspond strictly to a unique solution.

    ``(n, d)`` where ``n`` and ``d`` are the numerator and denominator of ``f``
    when the numerator was not linear in any symbol of interest; ``n`` will
    never be a symbol unless a solution for that symbol was found (in which case
    the second element is the solution, not the denominator).

    Examples
    ========

    >>> from sympy import cancel, Pow

    ``f`` is independent of the symbols in *symbols* that are not in
    *exclude*:

    >>> from sympy import cos, sin, solve_linear
    >>> from sympy.abc import x, y, z
    >>> eq = y*cos(x)**2 + y*sin(x)**2 - y  # = y*(1 - 1) = 0
    >>> solve_linear(eq)
    (0, 1)
    >>> eq = cos(x)**2 + sin(x)**2  # = 1
    >>> solve_linear(eq)
    (0, 1)
    >>> solve_linear(x, exclude=[x])
    (0, 1)

    The variable ``x`` appears as a linear variable in each of the
    following:

    >>> solve_linear(x + y**2)
    (x, -y**2)
    >>> solve_linear(1/x - y**2)
    (x, y**(-2))

    When not linear in ``x`` or ``y`` then the numerator and denominator are
    returned:

    >>> solve_linear(x**2/y**2 - 3)
    (x**2 - 3*y**2, y**2)

    If the numerator of the expression is a symbol, then ``(0, 0)`` is
    returned if the solution for that symbol would have set any
    denominator to 0:

    >>> eq = 1/(1/x - 2)
    >>> eq.as_numer_denom()
    (x, 1 - 2*x)
    >>> solve_linear(eq)
    (0, 0)

    But automatic rewriting may cause a symbol in the denominator to
    appear in the numerator so a solution will be returned:

    >>> (1/x)**-1
    x
    >>> solve_linear((1/x)**-1)
    (x, 0)

    Use an unevaluated expression to avoid this:

    >>> solve_linear(Pow(1/x, -1, evaluate=False))
    (0, 0)

    If ``x`` is allowed to cancel in the following expression, then it
    appears to be linear in ``x``, but this sort of cancellation is not
    done by ``solve_linear`` so the solution will always satisfy the
    original expression without causing a division by zero error.

    >>> eq = x**2*(1/x - z**2/x)
    >>> solve_linear(cancel(eq))
    (x, 0)
    >>> solve_linear(eq)
    (x**2*(1 - z**2), x)

    A list of symbols for which a solution is desired may be given:

    >>> solve_linear(x + y + z, symbols=[y])
    (y, -x - z)

    A list of symbols to ignore may also be given:

    >>> solve_linear(x + y + z, exclude=[x])
    (y, -x - z)

    (A solution for ``y`` is obtained because it is the first variable
    from the canonically sorted list of symbols that had a linear
    solution.)

    """
def minsolve_linear_system(system, *symbols, **flags):
    """
    Find a particular solution to a linear system.

    Explanation
    ===========

    In particular, try to find a solution with the minimal possible number
    of non-zero variables using a naive algorithm with exponential complexity.
    If ``quick=True``, a heuristic is used.

    """
def solve_linear_system(system, *symbols, **flags):
    """
    Solve system of $N$ linear equations with $M$ variables, which means
    both under- and overdetermined systems are supported.

    Explanation
    ===========

    The possible number of solutions is zero, one, or infinite. Respectively,
    this procedure will return None or a dictionary with solutions. In the
    case of underdetermined systems, all arbitrary parameters are skipped.
    This may cause a situation in which an empty dictionary is returned.
    In that case, all symbols can be assigned arbitrary values.

    Input to this function is a $N\\times M + 1$ matrix, which means it has
    to be in augmented form. If you prefer to enter $N$ equations and $M$
    unknowns then use ``solve(Neqs, *Msymbols)`` instead. Note: a local
    copy of the matrix is made by this routine so the matrix that is
    passed will not be modified.

    The algorithm used here is fraction-free Gaussian elimination,
    which results, after elimination, in an upper-triangular matrix.
    Then solutions are found using back-substitution. This approach
    is more efficient and compact than the Gauss-Jordan method.

    Examples
    ========

    >>> from sympy import Matrix, solve_linear_system
    >>> from sympy.abc import x, y

    Solve the following system::

           x + 4 y ==  2
        -2 x +   y == 14

    >>> system = Matrix(( (1, 4, 2), (-2, 1, 14)))
    >>> solve_linear_system(system, x, y)
    {x: -6, y: 2}

    A degenerate system returns an empty dictionary:

    >>> system = Matrix(( (0,0,0), (0,0,0) ))
    >>> solve_linear_system(system, x, y)
    {}

    """
def solve_undetermined_coeffs(equ, coeffs, *syms, **flags):
    """
    Solve a system of equations in $k$ parameters that is formed by
    matching coefficients in variables ``coeffs`` that are on
    factors dependent on the remaining variables (or those given
    explicitly by ``syms``.

    Explanation
    ===========

    The result of this function is a dictionary with symbolic values of those
    parameters with respect to coefficients in $q$ -- empty if there
    is no solution or coefficients do not appear in the equation -- else
    None (if the system was not recognized). If there is more than one
    solution, the solutions are passed as a list. The output can be modified using
    the same semantics as for `solve` since the flags that are passed are sent
    directly to `solve` so, for example the flag ``dict=True`` will always return a list
    of solutions as dictionaries.

    This function accepts both Equality and Expr class instances.
    The solving process is most efficient when symbols are specified
    in addition to parameters to be determined,  but an attempt to
    determine them (if absent) will be made. If an expected solution is not
    obtained (and symbols were not specified) try specifying them.

    Examples
    ========

    >>> from sympy import Eq, solve_undetermined_coeffs
    >>> from sympy.abc import a, b, c, h, p, k, x, y

    >>> solve_undetermined_coeffs(Eq(a*x + a + b, x/2), [a, b], x)
    {a: 1/2, b: -1/2}
    >>> solve_undetermined_coeffs(a - 2, [a])
    {a: 2}

    The equation can be nonlinear in the symbols:

    >>> X, Y, Z = y, x**y, y*x**y
    >>> eq = a*X + b*Y + c*Z - X - 2*Y - 3*Z
    >>> coeffs = a, b, c
    >>> syms = x, y
    >>> solve_undetermined_coeffs(eq, coeffs, syms)
    {a: 1, b: 2, c: 3}

    And the system can be nonlinear in coefficients, too, but if
    there is only a single solution, it will be returned as a
    dictionary:

    >>> eq = a*x**2 + b*x + c - ((x - h)**2 + 4*p*k)/4/p
    >>> solve_undetermined_coeffs(eq, (h, p, k), x)
    {h: -b/(2*a), k: (4*a*c - b**2)/(4*a), p: 1/(4*a)}

    Multiple solutions are always returned in a list:

    >>> solve_undetermined_coeffs(a**2*x + b - x, [a, b], x)
    [{a: -1, b: 0}, {a: 1, b: 0}]

    Using flag ``dict=True`` (in keeping with semantics in :func:`~.solve`)
    will force the result to always be a list with any solutions
    as elements in that list.

    >>> solve_undetermined_coeffs(a*x - 2*x, [a], dict=True)
    [{a: 2}]
    """
def solve_linear_system_LU(matrix, syms):
    """
    Solves the augmented matrix system using ``LUsolve`` and returns a
    dictionary in which solutions are keyed to the symbols of *syms* as ordered.

    Explanation
    ===========

    The matrix must be invertible.

    Examples
    ========

    >>> from sympy import Matrix, solve_linear_system_LU
    >>> from sympy.abc import x, y, z

    >>> solve_linear_system_LU(Matrix([
    ... [1, 2, 0, 1],
    ... [3, 2, 2, 1],
    ... [2, 0, 0, 1]]), [x, y, z])
    {x: 1/2, y: 1/4, z: -1/2}

    See Also
    ========

    LUsolve

    """
def det_perm(M):
    """
    Return the determinant of *M* by using permutations to select factors.

    Explanation
    ===========

    For sizes larger than 8 the number of permutations becomes prohibitively
    large, or if there are no symbols in the matrix, it is better to use the
    standard determinant routines (e.g., ``M.det()``.)

    See Also
    ========

    det_minor
    det_quick

    """
def det_minor(M):
    """
    Return the ``det(M)`` computed from minors without
    introducing new nesting in products.

    See Also
    ========

    det_perm
    det_quick

    """
def det_quick(M, method: Incomplete | None = None):
    """
    Return ``det(M)`` assuming that either
    there are lots of zeros or the size of the matrix
    is small. If this assumption is not met, then the normal
    Matrix.det function will be used with method = ``method``.

    See Also
    ========

    det_minor
    det_perm

    """
def inv_quick(M):
    """Return the inverse of ``M``, assuming that either
    there are lots of zeros or the size of the matrix
    is small.
    """

multi_inverses: Incomplete

def nsolve(*args, dict: bool = False, **kwargs):
    """
    Solve a nonlinear equation system numerically: ``nsolve(f, [args,] x0,
    modules=['mpmath'], **kwargs)``.

    Explanation
    ===========

    ``f`` is a vector function of symbolic expressions representing the system.
    *args* are the variables. If there is only one variable, this argument can
    be omitted. ``x0`` is a starting vector close to a solution.

    Use the modules keyword to specify which modules should be used to
    evaluate the function and the Jacobian matrix. Make sure to use a module
    that supports matrices. For more information on the syntax, please see the
    docstring of ``lambdify``.

    If the keyword arguments contain ``dict=True`` (default is False) ``nsolve``
    will return a list (perhaps empty) of solution mappings. This might be
    especially useful if you want to use ``nsolve`` as a fallback to solve since
    using the dict argument for both methods produces return values of
    consistent type structure. Please note: to keep this consistent with
    ``solve``, the solution will be returned in a list even though ``nsolve``
    (currently at least) only finds one solution at a time.

    Overdetermined systems are supported.

    Examples
    ========

    >>> from sympy import Symbol, nsolve
    >>> import mpmath
    >>> mpmath.mp.dps = 15
    >>> x1 = Symbol('x1')
    >>> x2 = Symbol('x2')
    >>> f1 = 3 * x1**2 - 2 * x2**2 - 1
    >>> f2 = x1**2 - 2 * x1 + x2**2 + 2 * x2 - 8
    >>> print(nsolve((f1, f2), (x1, x2), (-1, 1)))
    Matrix([[-1.19287309935246], [1.27844411169911]])

    For one-dimensional functions the syntax is simplified:

    >>> from sympy import sin, nsolve
    >>> from sympy.abc import x
    >>> nsolve(sin(x), x, 2)
    3.14159265358979
    >>> nsolve(sin(x), 2)
    3.14159265358979

    To solve with higher precision than the default, use the prec argument:

    >>> from sympy import cos
    >>> nsolve(cos(x) - x, 1)
    0.739085133215161
    >>> nsolve(cos(x) - x, 1, prec=50)
    0.73908513321516064165531208767387340401341175890076
    >>> cos(_)
    0.73908513321516064165531208767387340401341175890076

    To solve for complex roots of real functions, a nonreal initial point
    must be specified:

    >>> from sympy import I
    >>> nsolve(x**2 + 2, I)
    1.4142135623731*I

    ``mpmath.findroot`` is used and you can find their more extensive
    documentation, especially concerning keyword parameters and
    available solvers. Note, however, that functions which are very
    steep near the root, the verification of the solution may fail. In
    this case you should use the flag ``verify=False`` and
    independently verify the solution.

    >>> from sympy import cos, cosh
    >>> f = cos(x)*cosh(x) - 1
    >>> nsolve(f, 3.14*100)
    Traceback (most recent call last):
    ...
    ValueError: Could not find root within given tolerance. (1.39267e+230 > 2.1684e-19)
    >>> ans = nsolve(f, 3.14*100, verify=False); ans
    312.588469032184
    >>> f.subs(x, ans).n(2)
    2.1e+121
    >>> (f/f.diff(x)).subs(x, ans).n(2)
    7.4e-15

    One might safely skip the verification if bounds of the root are known
    and a bisection method is used:

    >>> bounds = lambda i: (3.14*i, 3.14*(i + 1))
    >>> nsolve(f, bounds(100), solver='bisect', verify=False)
    315.730061685774

    Alternatively, a function may be better behaved when the
    denominator is ignored. Since this is not always the case, however,
    the decision of what function to use is left to the discretion of
    the user.

    >>> eq = x**2/(1 - x)/(1 - 2*x)**2 - 100
    >>> nsolve(eq, 0.46)
    Traceback (most recent call last):
    ...
    ValueError: Could not find root within given tolerance. (10000 > 2.1684e-19)
    Try another starting point or tweak arguments.
    >>> nsolve(eq.as_numer_denom()[0], 0.46)
    0.46792545969349058

    """
def unrad(eq, *syms, **flags):
    """
    Remove radicals with symbolic arguments and return (eq, cov),
    None, or raise an error.

    Explanation
    ===========

    None is returned if there are no radicals to remove.

    NotImplementedError is raised if there are radicals and they cannot be
    removed or if the relationship between the original symbols and the
    change of variable needed to rewrite the system as a polynomial cannot
    be solved.

    Otherwise the tuple, ``(eq, cov)``, is returned where:

    *eq*, ``cov``
        *eq* is an equation without radicals (in the symbol(s) of
        interest) whose solutions are a superset of the solutions to the
        original expression. *eq* might be rewritten in terms of a new
        variable; the relationship to the original variables is given by
        ``cov`` which is a list containing ``v`` and ``v**p - b`` where
        ``p`` is the power needed to clear the radical and ``b`` is the
        radical now expressed as a polynomial in the symbols of interest.
        For example, for sqrt(2 - x) the tuple would be
        ``(c, c**2 - 2 + x)``. The solutions of *eq* will contain
        solutions to the original equation (if there are any).

    *syms*
        An iterable of symbols which, if provided, will limit the focus of
        radical removal: only radicals with one or more of the symbols of
        interest will be cleared. All free symbols are used if *syms* is not
        set.

    *flags* are used internally for communication during recursive calls.
    Two options are also recognized:

        ``take``, when defined, is interpreted as a single-argument function
        that returns True if a given Pow should be handled.

    Radicals can be removed from an expression if:

        *   All bases of the radicals are the same; a change of variables is
            done in this case.
        *   If all radicals appear in one term of the expression.
        *   There are only four terms with sqrt() factors or there are less than
            four terms having sqrt() factors.
        *   There are only two terms with radicals.

    Examples
    ========

    >>> from sympy.solvers.solvers import unrad
    >>> from sympy.abc import x
    >>> from sympy import sqrt, Rational, root

    >>> unrad(sqrt(x)*x**Rational(1, 3) + 2)
    (x**5 - 64, [])
    >>> unrad(sqrt(x) + root(x + 1, 3))
    (-x**3 + x**2 + 2*x + 1, [])
    >>> eq = sqrt(x) + root(x, 3) - 2
    >>> unrad(eq)
    (_p**3 + _p**2 - 2, [_p, _p**6 - x])

    """
