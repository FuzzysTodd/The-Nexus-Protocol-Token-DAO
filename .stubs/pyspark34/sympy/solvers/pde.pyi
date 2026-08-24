from _typeshed import Incomplete
from sympy.core import Add as Add, S as S
from sympy.core.function import AppliedUndef as AppliedUndef, Function as Function, Subs as Subs, expand as expand
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.symbol import Symbol as Symbol, Wild as Wild, symbols as symbols
from sympy.functions import exp as exp
from sympy.integrals.integrals import Integral as Integral, integrate as integrate
from sympy.simplify import simplify as simplify
from sympy.simplify.radsimp import collect as collect
from sympy.solvers.deutils import ode_order as ode_order
from sympy.solvers.solvers import solve as solve
from sympy.utilities.iterables import has_dups as has_dups, is_sequence as is_sequence
from sympy.utilities.misc import filldedent as filldedent

allhints: Incomplete

def pdsolve(eq, func: Incomplete | None = None, hint: str = 'default', dict: bool = False, solvefun: Incomplete | None = None, **kwargs):
    '''
    Solves any (supported) kind of partial differential equation.

    **Usage**

        pdsolve(eq, f(x,y), hint) -> Solve partial differential equation
        eq for function f(x,y), using method hint.

    **Details**

        ``eq`` can be any supported partial differential equation (see
            the pde docstring for supported methods).  This can either
            be an Equality, or an expression, which is assumed to be
            equal to 0.

        ``f(x,y)`` is a function of two variables whose derivatives in that
            variable make up the partial differential equation. In many
            cases it is not necessary to provide this; it will be autodetected
            (and an error raised if it could not be detected).

        ``hint`` is the solving method that you want pdsolve to use.  Use
            classify_pde(eq, f(x,y)) to get all of the possible hints for
            a PDE.  The default hint, \'default\', will use whatever hint
            is returned first by classify_pde().  See Hints below for
            more options that you can use for hint.

        ``solvefun`` is the convention used for arbitrary functions returned
            by the PDE solver. If not set by the user, it is set by default
            to be F.

    **Hints**

        Aside from the various solving methods, there are also some
        meta-hints that you can pass to pdsolve():

        "default":
                This uses whatever hint is returned first by
                classify_pde(). This is the default argument to
                pdsolve().

        "all":
                To make pdsolve apply all relevant classification hints,
                use pdsolve(PDE, func, hint="all").  This will return a
                dictionary of hint:solution terms.  If a hint causes
                pdsolve to raise the NotImplementedError, value of that
                hint\'s key will be the exception object raised.  The
                dictionary will also include some special keys:

                - order: The order of the PDE.  See also ode_order() in
                  deutils.py
                - default: The solution that would be returned by
                  default.  This is the one produced by the hint that
                  appears first in the tuple returned by classify_pde().

        "all_Integral":
                This is the same as "all", except if a hint also has a
                corresponding "_Integral" hint, it only returns the
                "_Integral" hint.  This is useful if "all" causes
                pdsolve() to hang because of a difficult or impossible
                integral.  This meta-hint will also be much faster than
                "all", because integrate() is an expensive routine.

        See also the classify_pde() docstring for more info on hints,
        and the pde docstring for a list of all supported hints.

    **Tips**
        - You can declare the derivative of an unknown function this way:

            >>> from sympy import Function, Derivative
            >>> from sympy.abc import x, y # x and y are the independent variables
            >>> f = Function("f")(x, y) # f is a function of x and y
            >>> # fx will be the partial derivative of f with respect to x
            >>> fx = Derivative(f, x)
            >>> # fy will be the partial derivative of f with respect to y
            >>> fy = Derivative(f, y)

        - See test_pde.py for many tests, which serves also as a set of
          examples for how to use pdsolve().
        - pdsolve always returns an Equality class (except for the case
          when the hint is "all" or "all_Integral"). Note that it is not possible
          to get an explicit solution for f(x, y) as in the case of ODE\'s
        - Do help(pde.pde_hintname) to get help more information on a
          specific hint


    Examples
    ========

    >>> from sympy.solvers.pde import pdsolve
    >>> from sympy import Function, Eq
    >>> from sympy.abc import x, y
    >>> f = Function(\'f\')
    >>> u = f(x, y)
    >>> ux = u.diff(x)
    >>> uy = u.diff(y)
    >>> eq = Eq(1 + (2*(ux/u)) + (3*(uy/u)), 0)
    >>> pdsolve(eq)
    Eq(f(x, y), F(3*x - 2*y)*exp(-2*x/13 - 3*y/13))

    '''
def classify_pde(eq, func: Incomplete | None = None, dict: bool = False, *, prep: bool = True, **kwargs):
    '''
    Returns a tuple of possible pdsolve() classifications for a PDE.

    The tuple is ordered so that first item is the classification that
    pdsolve() uses to solve the PDE by default.  In general,
    classifications near the beginning of the list will produce
    better solutions faster than those near the end, though there are
    always exceptions.  To make pdsolve use a different classification,
    use pdsolve(PDE, func, hint=<classification>).  See also the pdsolve()
    docstring for different meta-hints you can use.

    If ``dict`` is true, classify_pde() will return a dictionary of
    hint:match expression terms. This is intended for internal use by
    pdsolve().  Note that because dictionaries are ordered arbitrarily,
    this will most likely not be in the same order as the tuple.

    You can get help on different hints by doing help(pde.pde_hintname),
    where hintname is the name of the hint without "_Integral".

    See sympy.pde.allhints or the sympy.pde docstring for a list of all
    supported hints that can be returned from classify_pde.


    Examples
    ========

    >>> from sympy.solvers.pde import classify_pde
    >>> from sympy import Function, Eq
    >>> from sympy.abc import x, y
    >>> f = Function(\'f\')
    >>> u = f(x, y)
    >>> ux = u.diff(x)
    >>> uy = u.diff(y)
    >>> eq = Eq(1 + (2*(ux/u)) + (3*(uy/u)), 0)
    >>> classify_pde(eq)
    (\'1st_linear_constant_coeff_homogeneous\',)
    '''
def checkpdesol(pde, sol, func: Incomplete | None = None, solve_for_func: bool = True):
    """
    Checks if the given solution satisfies the partial differential
    equation.

    pde is the partial differential equation which can be given in the
    form of an equation or an expression. sol is the solution for which
    the pde is to be checked. This can also be given in an equation or
    an expression form. If the function is not provided, the helper
    function _preprocess from deutils is used to identify the function.

    If a sequence of solutions is passed, the same sort of container will be
    used to return the result for each solution.

    The following methods are currently being implemented to check if the
    solution satisfies the PDE:

        1. Directly substitute the solution in the PDE and check. If the
           solution has not been solved for f, then it will solve for f
           provided solve_for_func has not been set to False.

    If the solution satisfies the PDE, then a tuple (True, 0) is returned.
    Otherwise a tuple (False, expr) where expr is the value obtained
    after substituting the solution in the PDE. However if a known solution
    returns False, it may be due to the inability of doit() to simplify it to zero.

    Examples
    ========

    >>> from sympy import Function, symbols
    >>> from sympy.solvers.pde import checkpdesol, pdsolve
    >>> x, y = symbols('x y')
    >>> f = Function('f')
    >>> eq = 2*f(x,y) + 3*f(x,y).diff(x) + 4*f(x,y).diff(y)
    >>> sol = pdsolve(eq)
    >>> assert checkpdesol(eq, sol)[0]
    >>> eq = x*f(x,y) + f(x,y).diff(x)
    >>> checkpdesol(eq, sol)
    (False, (x*F(4*x - 3*y) - 6*F(4*x - 3*y)/25 + 4*Subs(Derivative(F(_xi_1), _xi_1), _xi_1, 4*x - 3*y))*exp(-6*x/25 - 8*y/25))
    """
def pde_1st_linear_constant_coeff_homogeneous(eq, func, order, match, solvefun):
    '''
    Solves a first order linear homogeneous
    partial differential equation with constant coefficients.

    The general form of this partial differential equation is

    .. math:: a \\frac{\\partial f(x,y)}{\\partial x}
              + b \\frac{\\partial f(x,y)}{\\partial y} + c f(x,y) = 0

    where `a`, `b` and `c` are constants.

    The general solution is of the form:

    .. math::
        f(x, y) = F(- a y + b x ) e^{- \\frac{c (a x + b y)}{a^2 + b^2}}

    and can be found in SymPy with ``pdsolve``::

        >>> from sympy.solvers import pdsolve
        >>> from sympy.abc import x, y, a, b, c
        >>> from sympy import Function, pprint
        >>> f = Function(\'f\')
        >>> u = f(x,y)
        >>> ux = u.diff(x)
        >>> uy = u.diff(y)
        >>> genform = a*ux + b*uy + c*u
        >>> pprint(genform)
          d               d
        a*--(f(x, y)) + b*--(f(x, y)) + c*f(x, y)
          dx              dy

        >>> pprint(pdsolve(genform))
                                 -c*(a*x + b*y)
                                 ---------------
                                      2    2
                                     a  + b
        f(x, y) = F(-a*y + b*x)*e

    Examples
    ========

    >>> from sympy import pdsolve
    >>> from sympy import Function, pprint
    >>> from sympy.abc import x,y
    >>> f = Function(\'f\')
    >>> pdsolve(f(x,y) + f(x,y).diff(x) + f(x,y).diff(y))
    Eq(f(x, y), F(x - y)*exp(-x/2 - y/2))
    >>> pprint(pdsolve(f(x,y) + f(x,y).diff(x) + f(x,y).diff(y)))
                          x   y
                        - - - -
                          2   2
    f(x, y) = F(x - y)*e

    References
    ==========

    - Viktor Grigoryan, "Partial Differential Equations"
      Math 124A - Fall 2010, pp.7

    '''
def pde_1st_linear_constant_coeff(eq, func, order, match, solvefun):
    '''
    Solves a first order linear partial differential equation
    with constant coefficients.

    The general form of this partial differential equation is

    .. math:: a \\frac{\\partial f(x,y)}{\\partial x}
              + b \\frac{\\partial f(x,y)}{\\partial y}
              + c f(x,y) = G(x,y)

    where `a`, `b` and `c` are constants and `G(x, y)` can be an arbitrary
    function in `x` and `y`.

    The general solution of the PDE is:

    .. math::
        f(x, y) = \\left. \\left[F(\\eta) + \\frac{1}{a^2 + b^2}
        \\int\\limits^{a x + b y} G\\left(\\frac{a \\xi + b \\eta}{a^2 + b^2},
        \\frac{- a \\eta + b \\xi}{a^2 + b^2} \\right)
        e^{\\frac{c \\xi}{a^2 + b^2}}\\, d\\xi\\right]
        e^{- \\frac{c \\xi}{a^2 + b^2}}
        \\right|_{\\substack{\\eta=- a y + b x\\\\ \\xi=a x + b y }}\\, ,

    where `F(\\eta)` is an arbitrary single-valued function. The solution
    can be found in SymPy with ``pdsolve``::

        >>> from sympy.solvers import pdsolve
        >>> from sympy.abc import x, y, a, b, c
        >>> from sympy import Function, pprint
        >>> f = Function(\'f\')
        >>> G = Function(\'G\')
        >>> u = f(x,y)
        >>> ux = u.diff(x)
        >>> uy = u.diff(y)
        >>> genform = a*ux + b*uy + c*u - G(x,y)
        >>> pprint(genform)
          d               d
        a*--(f(x, y)) + b*--(f(x, y)) + c*f(x, y) - G(x, y)
          dx              dy
        >>> pprint(pdsolve(genform, hint=\'1st_linear_constant_coeff_Integral\'))
                  //          a*x + b*y                                             \\\n                  ||              /                                                 |
                  ||             |                                                  |
                  ||             |                                       c*xi       |
                  ||             |                                     -------      |
                  ||             |                                      2    2      |
                  ||             |      /a*xi + b*eta  -a*eta + b*xi\\  a  + b       |
                  ||             |     G|------------, -------------|*e        d(xi)|
                  ||             |      |   2    2         2    2   |               |
                  ||             |      \\  a  + b         a  + b    /               |
                  ||             |                                                  |
                  ||            /                                                   |
                  ||                                                                |
        f(x, y) = ||F(eta) + -------------------------------------------------------|*
                  ||                                  2    2                        |
                  \\\\                                 a  + b                         /
        <BLANKLINE>
                \\|
                ||
                ||
                ||
                ||
                ||
                ||
                ||
                ||
          -c*xi ||
         -------||
          2    2||
         a  + b ||
        e       ||
                ||
                /|eta=-a*y + b*x, xi=a*x + b*y


    Examples
    ========

    >>> from sympy.solvers.pde import pdsolve
    >>> from sympy import Function, pprint, exp
    >>> from sympy.abc import x,y
    >>> f = Function(\'f\')
    >>> eq = -2*f(x,y).diff(x) + 4*f(x,y).diff(y) + 5*f(x,y) - exp(x + 3*y)
    >>> pdsolve(eq)
    Eq(f(x, y), (F(4*x + 2*y)*exp(x/2) + exp(x + 4*y)/15)*exp(-y))

    References
    ==========

    - Viktor Grigoryan, "Partial Differential Equations"
      Math 124A - Fall 2010, pp.7

    '''
def pde_1st_linear_variable_coeff(eq, func, order, match, solvefun):
    '''
    Solves a first order linear partial differential equation
    with variable coefficients. The general form of this partial
    differential equation is

    .. math:: a(x, y) \\frac{\\partial f(x, y)}{\\partial x}
                + b(x, y) \\frac{\\partial f(x, y)}{\\partial y}
                + c(x, y) f(x, y) = G(x, y)

    where `a(x, y)`, `b(x, y)`, `c(x, y)` and `G(x, y)` are arbitrary
    functions in `x` and `y`. This PDE is converted into an ODE by
    making the following transformation:

    1. `\\xi` as `x`

    2. `\\eta` as the constant in the solution to the differential
       equation `\\frac{dy}{dx} = -\\frac{b}{a}`

    Making the previous substitutions reduces it to the linear ODE

    .. math:: a(\\xi, \\eta)\\frac{du}{d\\xi} + c(\\xi, \\eta)u - G(\\xi, \\eta) = 0

    which can be solved using ``dsolve``.

    >>> from sympy.abc import x, y
    >>> from sympy import Function, pprint
    >>> a, b, c, G, f= [Function(i) for i in [\'a\', \'b\', \'c\', \'G\', \'f\']]
    >>> u = f(x,y)
    >>> ux = u.diff(x)
    >>> uy = u.diff(y)
    >>> genform = a(x, y)*u + b(x, y)*ux + c(x, y)*uy - G(x,y)
    >>> pprint(genform)
                                         d                     d
    -G(x, y) + a(x, y)*f(x, y) + b(x, y)*--(f(x, y)) + c(x, y)*--(f(x, y))
                                         dx                    dy


    Examples
    ========

    >>> from sympy.solvers.pde import pdsolve
    >>> from sympy import Function, pprint
    >>> from sympy.abc import x,y
    >>> f = Function(\'f\')
    >>> eq =  x*(u.diff(x)) - y*(u.diff(y)) + y**2*u - y**2
    >>> pdsolve(eq)
    Eq(f(x, y), F(x*y)*exp(y**2/2) + 1)

    References
    ==========

    - Viktor Grigoryan, "Partial Differential Equations"
      Math 124A - Fall 2010, pp.7

    '''
def pde_separate(eq, fun, sep, strategy: str = 'mul'):
    """Separate variables in partial differential equation either by additive
    or multiplicative separation approach. It tries to rewrite an equation so
    that one of the specified variables occurs on a different side of the
    equation than the others.

    :param eq: Partial differential equation

    :param fun: Original function F(x, y, z)

    :param sep: List of separated functions [X(x), u(y, z)]

    :param strategy: Separation strategy. You can choose between additive
        separation ('add') and multiplicative separation ('mul') which is
        default.

    Examples
    ========

    >>> from sympy import E, Eq, Function, pde_separate, Derivative as D
    >>> from sympy.abc import x, t
    >>> u, X, T = map(Function, 'uXT')

    >>> eq = Eq(D(u(x, t), x), E**(u(x, t))*D(u(x, t), t))
    >>> pde_separate(eq, u(x, t), [X(x), T(t)], strategy='add')
    [exp(-X(x))*Derivative(X(x), x), exp(T(t))*Derivative(T(t), t)]

    >>> eq = Eq(D(u(x, t), x, 2), D(u(x, t), t, 2))
    >>> pde_separate(eq, u(x, t), [X(x), T(t)], strategy='mul')
    [Derivative(X(x), (x, 2))/X(x), Derivative(T(t), (t, 2))/T(t)]

    See Also
    ========
    pde_separate_add, pde_separate_mul
    """
def pde_separate_add(eq, fun, sep):
    """
    Helper function for searching additive separable solutions.

    Consider an equation of two independent variables x, y and a dependent
    variable w, we look for the product of two functions depending on different
    arguments:

    `w(x, y, z) = X(x) + y(y, z)`

    Examples
    ========

    >>> from sympy import E, Eq, Function, pde_separate_add, Derivative as D
    >>> from sympy.abc import x, t
    >>> u, X, T = map(Function, 'uXT')

    >>> eq = Eq(D(u(x, t), x), E**(u(x, t))*D(u(x, t), t))
    >>> pde_separate_add(eq, u(x, t), [X(x), T(t)])
    [exp(-X(x))*Derivative(X(x), x), exp(T(t))*Derivative(T(t), t)]

    """
def pde_separate_mul(eq, fun, sep):
    """
    Helper function for searching multiplicative separable solutions.

    Consider an equation of two independent variables x, y and a dependent
    variable w, we look for the product of two functions depending on different
    arguments:

    `w(x, y, z) = X(x)*u(y, z)`

    Examples
    ========

    >>> from sympy import Function, Eq, pde_separate_mul, Derivative as D
    >>> from sympy.abc import x, y
    >>> u, X, Y = map(Function, 'uXY')

    >>> eq = Eq(D(u(x, y), x, 2), D(u(x, y), y, 2))
    >>> pde_separate_mul(eq, u(x, y), [X(x), Y(y)])
    [Derivative(X(x), (x, 2))/X(x), Derivative(Y(y), (y, 2))/Y(y)]

    """
