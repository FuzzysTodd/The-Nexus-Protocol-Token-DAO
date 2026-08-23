from .single import SingleODEProblem as SingleODEProblem, SingleODESolver as SingleODESolver, solver_map as solver_map
from _typeshed import Incomplete
from sympy.core import Add as Add, Mul as Mul, Pow as Pow, S as S, oo as oo
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import AtomicExpr as AtomicExpr, Expr as Expr
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function, Subs as Subs, diff as diff, expand as expand, expand_mul as expand_mul
from sympy.core.multidimensional import vectorize as vectorize
from sympy.core.numbers import Number as Number, nan as nan, zoo as zoo
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, Wild as Wild, symbols as symbols
from sympy.core.sympify import sympify as sympify
from sympy.core.traversal import preorder_traversal as preorder_traversal
from sympy.functions import exp as exp, log as log, sqrt as sqrt
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.integrals.integrals import Integral as Integral
from sympy.logic.boolalg import BooleanAtom as BooleanAtom, BooleanFalse as BooleanFalse, BooleanTrue as BooleanTrue
from sympy.polys import Poly as Poly, PolynomialError as PolynomialError, lcm as lcm, terms_gcd as terms_gcd
from sympy.polys.polytools import cancel as cancel
from sympy.series import Order as Order
from sympy.series.series import series as series
from sympy.simplify import collect as collect, cse as cse, logcombine as logcombine, powsimp as powsimp, separatevars as separatevars, simplify as simplify
from sympy.simplify.radsimp import collect_const as collect_const
from sympy.solvers import checksol as checksol, solve as solve
from sympy.solvers.deutils import ode_order as ode_order
from sympy.utilities import numbered_symbols as numbered_symbols
from sympy.utilities.iterables import iterable as iterable, sift as sift, uniq as uniq

allhints: Incomplete

def get_numbered_constants(eq, num: int = 1, start: int = 1, prefix: str = 'C'):
    """
    Returns a list of constants that do not occur
    in eq already.
    """
def iter_numbered_constants(eq, start: int = 1, prefix: str = 'C'):
    """
    Returns an iterator of constants that do not occur
    in eq already.
    """
def dsolve(eq, func: Incomplete | None = None, hint: str = 'default', simplify: bool = True, ics: Incomplete | None = None, xi: Incomplete | None = None, eta: Incomplete | None = None, x0: int = 0, n: int = 6, **kwargs):
    '''
    Solves any (supported) kind of ordinary differential equation and
    system of ordinary differential equations.

    For single ordinary differential equation
    =========================================

    It is classified under this when number of equation in ``eq`` is one.
    **Usage**

        ``dsolve(eq, f(x), hint)`` -> Solve ordinary differential equation
        ``eq`` for function ``f(x)``, using method ``hint``.

    **Details**

        ``eq`` can be any supported ordinary differential equation (see the
            :py:mod:`~sympy.solvers.ode` docstring for supported methods).
            This can either be an :py:class:`~sympy.core.relational.Equality`,
            or an expression, which is assumed to be equal to ``0``.

        ``f(x)`` is a function of one variable whose derivatives in that
            variable make up the ordinary differential equation ``eq``.  In
            many cases it is not necessary to provide this; it will be
            autodetected (and an error raised if it could not be detected).

        ``hint`` is the solving method that you want dsolve to use.  Use
            ``classify_ode(eq, f(x))`` to get all of the possible hints for an
            ODE.  The default hint, ``default``, will use whatever hint is
            returned first by :py:meth:`~sympy.solvers.ode.classify_ode`.  See
            Hints below for more options that you can use for hint.

        ``simplify`` enables simplification by
            :py:meth:`~sympy.solvers.ode.ode.odesimp`.  See its docstring for more
            information.  Turn this off, for example, to disable solving of
            solutions for ``func`` or simplification of arbitrary constants.
            It will still integrate with this hint. Note that the solution may
            contain more arbitrary constants than the order of the ODE with
            this option enabled.

        ``xi`` and ``eta`` are the infinitesimal functions of an ordinary
            differential equation. They are the infinitesimals of the Lie group
            of point transformations for which the differential equation is
            invariant. The user can specify values for the infinitesimals. If
            nothing is specified, ``xi`` and ``eta`` are calculated using
            :py:meth:`~sympy.solvers.ode.infinitesimals` with the help of various
            heuristics.

        ``ics`` is the set of initial/boundary conditions for the differential equation.
          It should be given in the form of ``{f(x0): x1, f(x).diff(x).subs(x, x2):
          x3}`` and so on.  For power series solutions, if no initial
          conditions are specified ``f(0)`` is assumed to be ``C0`` and the power
          series solution is calculated about 0.

        ``x0`` is the point about which the power series solution of a differential
          equation is to be evaluated.

        ``n`` gives the exponent of the dependent variable up to which the power series
          solution of a differential equation is to be evaluated.

    **Hints**

        Aside from the various solving methods, there are also some meta-hints
        that you can pass to :py:meth:`~sympy.solvers.ode.dsolve`:

        ``default``:
                This uses whatever hint is returned first by
                :py:meth:`~sympy.solvers.ode.classify_ode`. This is the
                default argument to :py:meth:`~sympy.solvers.ode.dsolve`.

        ``all``:
                To make :py:meth:`~sympy.solvers.ode.dsolve` apply all
                relevant classification hints, use ``dsolve(ODE, func,
                hint="all")``.  This will return a dictionary of
                ``hint:solution`` terms.  If a hint causes dsolve to raise the
                ``NotImplementedError``, value of that hint\'s key will be the
                exception object raised.  The dictionary will also include
                some special keys:

                - ``order``: The order of the ODE.  See also
                  :py:meth:`~sympy.solvers.deutils.ode_order` in
                  ``deutils.py``.
                - ``best``: The simplest hint; what would be returned by
                  ``best`` below.
                - ``best_hint``: The hint that would produce the solution
                  given by ``best``.  If more than one hint produces the best
                  solution, the first one in the tuple returned by
                  :py:meth:`~sympy.solvers.ode.classify_ode` is chosen.
                - ``default``: The solution that would be returned by default.
                  This is the one produced by the hint that appears first in
                  the tuple returned by
                  :py:meth:`~sympy.solvers.ode.classify_ode`.

        ``all_Integral``:
                This is the same as ``all``, except if a hint also has a
                corresponding ``_Integral`` hint, it only returns the
                ``_Integral`` hint.  This is useful if ``all`` causes
                :py:meth:`~sympy.solvers.ode.dsolve` to hang because of a
                difficult or impossible integral.  This meta-hint will also be
                much faster than ``all``, because
                :py:meth:`~sympy.core.expr.Expr.integrate` is an expensive
                routine.

        ``best``:
                To have :py:meth:`~sympy.solvers.ode.dsolve` try all methods
                and return the simplest one.  This takes into account whether
                the solution is solvable in the function, whether it contains
                any Integral classes (i.e.  unevaluatable integrals), and
                which one is the shortest in size.

        See also the :py:meth:`~sympy.solvers.ode.classify_ode` docstring for
        more info on hints, and the :py:mod:`~sympy.solvers.ode` docstring for
        a list of all supported hints.

    **Tips**

        - You can declare the derivative of an unknown function this way:

            >>> from sympy import Function, Derivative
            >>> from sympy.abc import x # x is the independent variable
            >>> f = Function("f")(x) # f is a function of x
            >>> # f_ will be the derivative of f with respect to x
            >>> f_ = Derivative(f, x)

        - See ``test_ode.py`` for many tests, which serves also as a set of
          examples for how to use :py:meth:`~sympy.solvers.ode.dsolve`.
        - :py:meth:`~sympy.solvers.ode.dsolve` always returns an
          :py:class:`~sympy.core.relational.Equality` class (except for the
          case when the hint is ``all`` or ``all_Integral``).  If possible, it
          solves the solution explicitly for the function being solved for.
          Otherwise, it returns an implicit solution.
        - Arbitrary constants are symbols named ``C1``, ``C2``, and so on.
        - Because all solutions should be mathematically equivalent, some
          hints may return the exact same result for an ODE. Often, though,
          two different hints will return the same solution formatted
          differently.  The two should be equivalent. Also note that sometimes
          the values of the arbitrary constants in two different solutions may
          not be the same, because one constant may have "absorbed" other
          constants into it.
        - Do ``help(ode.ode_<hintname>)`` to get help more information on a
          specific hint, where ``<hintname>`` is the name of a hint without
          ``_Integral``.

    For system of ordinary differential equations
    =============================================

    **Usage**
        ``dsolve(eq, func)`` -> Solve a system of ordinary differential
        equations ``eq`` for ``func`` being list of functions including
        `x(t)`, `y(t)`, `z(t)` where number of functions in the list depends
        upon the number of equations provided in ``eq``.

    **Details**

        ``eq`` can be any supported system of ordinary differential equations
        This can either be an :py:class:`~sympy.core.relational.Equality`,
        or an expression, which is assumed to be equal to ``0``.

        ``func`` holds ``x(t)`` and ``y(t)`` being functions of one variable which
        together with some of their derivatives make up the system of ordinary
        differential equation ``eq``. It is not necessary to provide this; it
        will be autodetected (and an error raised if it could not be detected).

    **Hints**

        The hints are formed by parameters returned by classify_sysode, combining
        them give hints name used later for forming method name.

    Examples
    ========

    >>> from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> dsolve(Derivative(f(x), x, x) + 9*f(x), f(x))
    Eq(f(x), C1*sin(3*x) + C2*cos(3*x))

    >>> eq = sin(x)*cos(f(x)) + cos(x)*sin(f(x))*f(x).diff(x)
    >>> dsolve(eq, hint=\'1st_exact\')
    [Eq(f(x), -acos(C1/cos(x)) + 2*pi), Eq(f(x), acos(C1/cos(x)))]
    >>> dsolve(eq, hint=\'almost_linear\')
    [Eq(f(x), -acos(C1/cos(x)) + 2*pi), Eq(f(x), acos(C1/cos(x)))]
    >>> t = symbols(\'t\')
    >>> x, y = symbols(\'x, y\', cls=Function)
    >>> eq = (Eq(Derivative(x(t),t), 12*t*x(t) + 8*y(t)), Eq(Derivative(y(t),t), 21*x(t) + 7*t*y(t)))
    >>> dsolve(eq)
    [Eq(x(t), C1*x0(t) + C2*x0(t)*Integral(8*exp(Integral(7*t, t))*exp(Integral(12*t, t))/x0(t)**2, t)),
    Eq(y(t), C1*y0(t) + C2*(y0(t)*Integral(8*exp(Integral(7*t, t))*exp(Integral(12*t, t))/x0(t)**2, t) +
    exp(Integral(7*t, t))*exp(Integral(12*t, t))/x0(t)))]
    >>> eq = (Eq(Derivative(x(t),t),x(t)*y(t)*sin(t)), Eq(Derivative(y(t),t),y(t)**2*sin(t)))
    >>> dsolve(eq)
    {Eq(x(t), -exp(C1)/(C2*exp(C1) - cos(t))), Eq(y(t), -1/(C1 - cos(t)))}
    '''
def solve_ics(sols, funcs, constants, ics):
    """
    Solve for the constants given initial conditions

    ``sols`` is a list of solutions.

    ``funcs`` is a list of functions.

    ``constants`` is a list of constants.

    ``ics`` is the set of initial/boundary conditions for the differential
    equation. It should be given in the form of ``{f(x0): x1,
    f(x).diff(x).subs(x, x2):  x3}`` and so on.

    Returns a dictionary mapping constants to values.
    ``solution.subs(constants)`` will replace the constants in ``solution``.

    Example
    =======
    >>> # From dsolve(f(x).diff(x) - f(x), f(x))
    >>> from sympy import symbols, Eq, exp, Function
    >>> from sympy.solvers.ode.ode import solve_ics
    >>> f = Function('f')
    >>> x, C1 = symbols('x C1')
    >>> sols = [Eq(f(x), C1*exp(x))]
    >>> funcs = [f(x)]
    >>> constants = [C1]
    >>> ics = {f(0): 2}
    >>> solved_constants = solve_ics(sols, funcs, constants, ics)
    >>> solved_constants
    {C1: 2}
    >>> sols[0].subs(solved_constants)
    Eq(f(x), 2*exp(x))

    """
def classify_ode(eq, func: Incomplete | None = None, dict: bool = False, ics: Incomplete | None = None, *, prep: bool = True, xi: Incomplete | None = None, eta: Incomplete | None = None, n: Incomplete | None = None, **kwargs):
    """
    Returns a tuple of possible :py:meth:`~sympy.solvers.ode.dsolve`
    classifications for an ODE.

    The tuple is ordered so that first item is the classification that
    :py:meth:`~sympy.solvers.ode.dsolve` uses to solve the ODE by default.  In
    general, classifications at the near the beginning of the list will
    produce better solutions faster than those near the end, thought there are
    always exceptions.  To make :py:meth:`~sympy.solvers.ode.dsolve` use a
    different classification, use ``dsolve(ODE, func,
    hint=<classification>)``.  See also the
    :py:meth:`~sympy.solvers.ode.dsolve` docstring for different meta-hints
    you can use.

    If ``dict`` is true, :py:meth:`~sympy.solvers.ode.classify_ode` will
    return a dictionary of ``hint:match`` expression terms. This is intended
    for internal use by :py:meth:`~sympy.solvers.ode.dsolve`.  Note that
    because dictionaries are ordered arbitrarily, this will most likely not be
    in the same order as the tuple.

    You can get help on different hints by executing
    ``help(ode.ode_hintname)``, where ``hintname`` is the name of the hint
    without ``_Integral``.

    See :py:data:`~sympy.solvers.ode.allhints` or the
    :py:mod:`~sympy.solvers.ode` docstring for a list of all supported hints
    that can be returned from :py:meth:`~sympy.solvers.ode.classify_ode`.

    Notes
    =====

    These are remarks on hint names.

    ``_Integral``

        If a classification has ``_Integral`` at the end, it will return the
        expression with an unevaluated :py:class:`~.Integral`
        class in it.  Note that a hint may do this anyway if
        :py:meth:`~sympy.core.expr.Expr.integrate` cannot do the integral,
        though just using an ``_Integral`` will do so much faster.  Indeed, an
        ``_Integral`` hint will always be faster than its corresponding hint
        without ``_Integral`` because
        :py:meth:`~sympy.core.expr.Expr.integrate` is an expensive routine.
        If :py:meth:`~sympy.solvers.ode.dsolve` hangs, it is probably because
        :py:meth:`~sympy.core.expr.Expr.integrate` is hanging on a tough or
        impossible integral.  Try using an ``_Integral`` hint or
        ``all_Integral`` to get it return something.

        Note that some hints do not have ``_Integral`` counterparts. This is
        because :py:func:`~sympy.integrals.integrals.integrate` is not used in
        solving the ODE for those method. For example, `n`\\th order linear
        homogeneous ODEs with constant coefficients do not require integration
        to solve, so there is no
        ``nth_linear_homogeneous_constant_coeff_Integrate`` hint. You can
        easily evaluate any unevaluated
        :py:class:`~sympy.integrals.integrals.Integral`\\s in an expression by
        doing ``expr.doit()``.

    Ordinals

        Some hints contain an ordinal such as ``1st_linear``.  This is to help
        differentiate them from other hints, as well as from other methods
        that may not be implemented yet. If a hint has ``nth`` in it, such as
        the ``nth_linear`` hints, this means that the method used to applies
        to ODEs of any order.

    ``indep`` and ``dep``

        Some hints contain the words ``indep`` or ``dep``.  These reference
        the independent variable and the dependent function, respectively. For
        example, if an ODE is in terms of `f(x)`, then ``indep`` will refer to
        `x` and ``dep`` will refer to `f`.

    ``subs``

        If a hints has the word ``subs`` in it, it means that the ODE is solved
        by substituting the expression given after the word ``subs`` for a
        single dummy variable.  This is usually in terms of ``indep`` and
        ``dep`` as above.  The substituted expression will be written only in
        characters allowed for names of Python objects, meaning operators will
        be spelled out.  For example, ``indep``/``dep`` will be written as
        ``indep_div_dep``.

    ``coeff``

        The word ``coeff`` in a hint refers to the coefficients of something
        in the ODE, usually of the derivative terms.  See the docstring for
        the individual methods for more info (``help(ode)``).  This is
        contrast to ``coefficients``, as in ``undetermined_coefficients``,
        which refers to the common name of a method.

    ``_best``

        Methods that have more than one fundamental way to solve will have a
        hint for each sub-method and a ``_best`` meta-classification. This
        will evaluate all hints and return the best, using the same
        considerations as the normal ``best`` meta-hint.


    Examples
    ========

    >>> from sympy import Function, classify_ode, Eq
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> classify_ode(Eq(f(x).diff(x), 0), f(x))
    ('nth_algebraic',
    'separable',
    '1st_exact',
    '1st_linear',
    'Bernoulli',
    '1st_homogeneous_coeff_best',
    '1st_homogeneous_coeff_subs_indep_div_dep',
    '1st_homogeneous_coeff_subs_dep_div_indep',
    '1st_power_series', 'lie_group', 'nth_linear_constant_coeff_homogeneous',
    'nth_linear_euler_eq_homogeneous',
    'nth_algebraic_Integral', 'separable_Integral', '1st_exact_Integral',
    '1st_linear_Integral', 'Bernoulli_Integral',
    '1st_homogeneous_coeff_subs_indep_div_dep_Integral',
    '1st_homogeneous_coeff_subs_dep_div_indep_Integral')
    >>> classify_ode(f(x).diff(x, 2) + 3*f(x).diff(x) + 2*f(x) - 4)
    ('factorable', 'nth_linear_constant_coeff_undetermined_coefficients',
    'nth_linear_constant_coeff_variation_of_parameters',
    'nth_linear_constant_coeff_variation_of_parameters_Integral')

    """
def classify_sysode(eq, funcs: Incomplete | None = None, **kwargs):
    '''
    Returns a dictionary of parameter names and values that define the system
    of ordinary differential equations in ``eq``.
    The parameters are further used in
    :py:meth:`~sympy.solvers.ode.dsolve` for solving that system.

    Some parameter names and values are:

    \'is_linear\' (boolean), which tells whether the given system is linear.
    Note that "linear" here refers to the operator: terms such as ``x*diff(x,t)`` are
    nonlinear, whereas terms like ``sin(t)*diff(x,t)`` are still linear operators.

    \'func\' (list) contains the :py:class:`~sympy.core.function.Function`s that
    appear with a derivative in the ODE, i.e. those that we are trying to solve
    the ODE for.

    \'order\' (dict) with the maximum derivative for each element of the \'func\'
    parameter.

    \'func_coeff\' (dict or Matrix) with the coefficient for each triple ``(equation number,
    function, order)```. The coefficients are those subexpressions that do not
    appear in \'func\', and hence can be considered constant for purposes of ODE
    solving. The value of this parameter can also be a  Matrix if the system of ODEs are
    linear first order of the form X\' = AX where X is the vector of dependent variables.
    Here, this function returns the coefficient matrix A.

    \'eq\' (list) with the equations from ``eq``, sympified and transformed into
    expressions (we are solving for these expressions to be zero).

    \'no_of_equations\' (int) is the number of equations (same as ``len(eq)``).

    \'type_of_equation\' (string) is an internal classification of the type of
    ODE.

    \'is_constant\' (boolean), which tells if the system of ODEs is constant coefficient
    or not. This key is temporary addition for now and is in the match dict only when
    the system of ODEs is linear first order constant coefficient homogeneous. So, this
    key\'s value is True for now if it is available else it does not exist.

    \'is_homogeneous\' (boolean), which tells if the system of ODEs is homogeneous. Like the
    key \'is_constant\', this key is a temporary addition and it is True since this key value
    is available only when the system is linear first order constant coefficient homogeneous.

    References
    ==========
    -https://eqworld.ipmnet.ru/en/solutions/sysode/sode-toc1.htm
    -A. D. Polyanin and A. V. Manzhirov, Handbook of Mathematics for Engineers and Scientists

    Examples
    ========

    >>> from sympy import Function, Eq, symbols, diff
    >>> from sympy.solvers.ode.ode import classify_sysode
    >>> from sympy.abc import t
    >>> f, x, y = symbols(\'f, x, y\', cls=Function)
    >>> k, l, m, n = symbols(\'k, l, m, n\', Integer=True)
    >>> x1 = diff(x(t), t) ; y1 = diff(y(t), t)
    >>> x2 = diff(x(t), t, t) ; y2 = diff(y(t), t, t)
    >>> eq = (Eq(x1, 12*x(t) - 6*y(t)), Eq(y1, 11*x(t) + 3*y(t)))
    >>> classify_sysode(eq)
    {\'eq\': [-12*x(t) + 6*y(t) + Derivative(x(t), t), -11*x(t) - 3*y(t) + Derivative(y(t), t)], \'func\': [x(t), y(t)],
     \'func_coeff\': {(0, x(t), 0): -12, (0, x(t), 1): 1, (0, y(t), 0): 6, (0, y(t), 1): 0, (1, x(t), 0): -11, (1, x(t), 1): 0, (1, y(t), 0): -3, (1, y(t), 1): 1}, \'is_linear\': True, \'no_of_equation\': 2, \'order\': {x(t): 1, y(t): 1}, \'type_of_equation\': None}
    >>> eq = (Eq(diff(x(t),t), 5*t*x(t) + t**2*y(t) + 2), Eq(diff(y(t),t), -t**2*x(t) + 5*t*y(t)))
    >>> classify_sysode(eq)
    {\'eq\': [-t**2*y(t) - 5*t*x(t) + Derivative(x(t), t) - 2, t**2*x(t) - 5*t*y(t) + Derivative(y(t), t)],
     \'func\': [x(t), y(t)], \'func_coeff\': {(0, x(t), 0): -5*t, (0, x(t), 1): 1, (0, y(t), 0): -t**2, (0, y(t), 1): 0,
     (1, x(t), 0): t**2, (1, x(t), 1): 0, (1, y(t), 0): -5*t, (1, y(t), 1): 1}, \'is_linear\': True, \'no_of_equation\': 2,
      \'order\': {x(t): 1, y(t): 1}, \'type_of_equation\': None}

    '''
def check_linear_2eq_order1(eq, func, func_coef): ...
def check_nonlinear_2eq_order1(eq, func, func_coef): ...
def check_nonlinear_2eq_order2(eq, func, func_coef) -> None: ...
def check_nonlinear_3eq_order1(eq, func, func_coef): ...
def check_nonlinear_3eq_order2(eq, func, func_coef) -> None: ...
def odesimp(ode, eq, func, hint):
    """
    Simplifies solutions of ODEs, including trying to solve for ``func`` and
    running :py:meth:`~sympy.solvers.ode.constantsimp`.

    It may use knowledge of the type of solution that the hint returns to
    apply additional simplifications.

    It also attempts to integrate any :py:class:`~sympy.integrals.integrals.Integral`\\s
    in the expression, if the hint is not an ``_Integral`` hint.

    This function should have no effect on expressions returned by
    :py:meth:`~sympy.solvers.ode.dsolve`, as
    :py:meth:`~sympy.solvers.ode.dsolve` already calls
    :py:meth:`~sympy.solvers.ode.ode.odesimp`, but the individual hint functions
    do not call :py:meth:`~sympy.solvers.ode.ode.odesimp` (because the
    :py:meth:`~sympy.solvers.ode.dsolve` wrapper does).  Therefore, this
    function is designed for mainly internal use.

    Examples
    ========

    >>> from sympy import sin, symbols, dsolve, pprint, Function
    >>> from sympy.solvers.ode.ode import odesimp
    >>> x, u2, C1= symbols('x,u2,C1')
    >>> f = Function('f')

    >>> eq = dsolve(x*f(x).diff(x) - f(x) - x*sin(f(x)/x), f(x),
    ... hint='1st_homogeneous_coeff_subs_indep_div_dep_Integral',
    ... simplify=False)
    >>> pprint(eq, wrap_line=False)
                            x
                           ----
                           f(x)
                             /
                            |
                            |   /        1   \\\n                            |  -|u1 + -------|
                            |   |        /1 \\|
                            |   |     sin|--||
                            |   \\        \\u1//
    log(f(x)) = log(C1) +   |  ---------------- d(u1)
                            |          2
                            |        u1
                            |
                           /

    >>> pprint(odesimp(eq, f(x), 1, {C1},
    ... hint='1st_homogeneous_coeff_subs_indep_div_dep'
    ... )) #doctest: +SKIP
        x
    --------- = C1
       /f(x)\\\n    tan|----|
       \\2*x /

    """
def ode_sol_simplicity(sol, func, trysolving: bool = True):
    """
    Returns an extended integer representing how simple a solution to an ODE
    is.

    The following things are considered, in order from most simple to least:

    - ``sol`` is solved for ``func``.
    - ``sol`` is not solved for ``func``, but can be if passed to solve (e.g.,
      a solution returned by ``dsolve(ode, func, simplify=False``).
    - If ``sol`` is not solved for ``func``, then base the result on the
      length of ``sol``, as computed by ``len(str(sol))``.
    - If ``sol`` has any unevaluated :py:class:`~sympy.integrals.integrals.Integral`\\s,
      this will automatically be considered less simple than any of the above.

    This function returns an integer such that if solution A is simpler than
    solution B by above metric, then ``ode_sol_simplicity(sola, func) <
    ode_sol_simplicity(solb, func)``.

    Currently, the following are the numbers returned, but if the heuristic is
    ever improved, this may change.  Only the ordering is guaranteed.

    +----------------------------------------------+-------------------+
    | Simplicity                                   | Return            |
    +==============================================+===================+
    | ``sol`` solved for ``func``                  | ``-2``            |
    +----------------------------------------------+-------------------+
    | ``sol`` not solved for ``func`` but can be   | ``-1``            |
    +----------------------------------------------+-------------------+
    | ``sol`` is not solved nor solvable for       | ``len(str(sol))`` |
    | ``func``                                     |                   |
    +----------------------------------------------+-------------------+
    | ``sol`` contains an                          | ``oo``            |
    | :obj:`~sympy.integrals.integrals.Integral`   |                   |
    +----------------------------------------------+-------------------+

    ``oo`` here means the SymPy infinity, which should compare greater than
    any integer.

    If you already know :py:meth:`~sympy.solvers.solvers.solve` cannot solve
    ``sol``, you can use ``trysolving=False`` to skip that step, which is the
    only potentially slow step.  For example,
    :py:meth:`~sympy.solvers.ode.dsolve` with the ``simplify=False`` flag
    should do this.

    If ``sol`` is a list of solutions, if the worst solution in the list
    returns ``oo`` it returns that, otherwise it returns ``len(str(sol))``,
    that is, the length of the string representation of the whole list.

    Examples
    ========

    This function is designed to be passed to ``min`` as the key argument,
    such as ``min(listofsolutions, key=lambda i: ode_sol_simplicity(i,
    f(x)))``.

    >>> from sympy import symbols, Function, Eq, tan, Integral
    >>> from sympy.solvers.ode.ode import ode_sol_simplicity
    >>> x, C1, C2 = symbols('x, C1, C2')
    >>> f = Function('f')

    >>> ode_sol_simplicity(Eq(f(x), C1*x**2), f(x))
    -2
    >>> ode_sol_simplicity(Eq(x**2 + f(x), C1), f(x))
    -1
    >>> ode_sol_simplicity(Eq(f(x), C1*Integral(2*x, x)), f(x))
    oo
    >>> eq1 = Eq(f(x)/tan(f(x)/(2*x)), C1)
    >>> eq2 = Eq(f(x)/tan(f(x)/(2*x) + f(x)), C2)
    >>> [ode_sol_simplicity(eq, f(x)) for eq in [eq1, eq2]]
    [28, 35]
    >>> min([eq1, eq2], key=lambda i: ode_sol_simplicity(i, f(x)))
    Eq(f(x)/tan(f(x)/(2*x)), C1)

    """
def constantsimp(expr, constants):
    '''
    Simplifies an expression with arbitrary constants in it.

    This function is written specifically to work with
    :py:meth:`~sympy.solvers.ode.dsolve`, and is not intended for general use.

    Simplification is done by "absorbing" the arbitrary constants into other
    arbitrary constants, numbers, and symbols that they are not independent
    of.

    The symbols must all have the same name with numbers after it, for
    example, ``C1``, ``C2``, ``C3``.  The ``symbolname`` here would be
    \'``C``\', the ``startnumber`` would be 1, and the ``endnumber`` would be 3.
    If the arbitrary constants are independent of the variable ``x``, then the
    independent symbol would be ``x``.  There is no need to specify the
    dependent function, such as ``f(x)``, because it already has the
    independent symbol, ``x``, in it.

    Because terms are "absorbed" into arbitrary constants and because
    constants are renumbered after simplifying, the arbitrary constants in
    expr are not necessarily equal to the ones of the same name in the
    returned result.

    If two or more arbitrary constants are added, multiplied, or raised to the
    power of each other, they are first absorbed together into a single
    arbitrary constant.  Then the new constant is combined into other terms if
    necessary.

    Absorption of constants is done with limited assistance:

    1. terms of :py:class:`~sympy.core.add.Add`\\s are collected to try join
       constants so `e^x (C_1 \\cos(x) + C_2 \\cos(x))` will simplify to `e^x
       C_1 \\cos(x)`;

    2. powers with exponents that are :py:class:`~sympy.core.add.Add`\\s are
       expanded so `e^{C_1 + x}` will be simplified to `C_1 e^x`.

    Use :py:meth:`~sympy.solvers.ode.ode.constant_renumber` to renumber constants
    after simplification or else arbitrary numbers on constants may appear,
    e.g. `C_1 + C_3 x`.

    In rare cases, a single constant can be "simplified" into two constants.
    Every differential equation solution should have as many arbitrary
    constants as the order of the differential equation.  The result here will
    be technically correct, but it may, for example, have `C_1` and `C_2` in
    an expression, when `C_1` is actually equal to `C_2`.  Use your discretion
    in such situations, and also take advantage of the ability to use hints in
    :py:meth:`~sympy.solvers.ode.dsolve`.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.solvers.ode.ode import constantsimp
    >>> C1, C2, C3, x, y = symbols(\'C1, C2, C3, x, y\')
    >>> constantsimp(2*C1*x, {C1, C2, C3})
    C1*x
    >>> constantsimp(C1 + 2 + x, {C1, C2, C3})
    C1 + x
    >>> constantsimp(C1*C2 + 2 + C2 + C3*x, {C1, C2, C3})
    C1 + C3*x

    '''
def constant_renumber(expr, variables: Incomplete | None = None, newconstants: Incomplete | None = None):
    """
    Renumber arbitrary constants in ``expr`` to use the symbol names as given
    in ``newconstants``. In the process, this reorders expression terms in a
    standard way.

    If ``newconstants`` is not provided then the new constant names will be
    ``C1``, ``C2`` etc. Otherwise ``newconstants`` should be an iterable
    giving the new symbols to use for the constants in order.

    The ``variables`` argument is a list of non-constant symbols. All other
    free symbols found in ``expr`` are assumed to be constants and will be
    renumbered. If ``variables`` is not given then any numbered symbol
    beginning with ``C`` (e.g. ``C1``) is assumed to be a constant.

    Symbols are renumbered based on ``.sort_key()``, so they should be
    numbered roughly in the order that they appear in the final, printed
    expression.  Note that this ordering is based in part on hashes, so it can
    produce different results on different machines.

    The structure of this function is very similar to that of
    :py:meth:`~sympy.solvers.ode.constantsimp`.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.solvers.ode.ode import constant_renumber
    >>> x, C1, C2, C3 = symbols('x,C1:4')
    >>> expr = C3 + C2*x + C1*x**2
    >>> expr
    C1*x**2  + C2*x + C3
    >>> constant_renumber(expr)
    C1 + C2*x + C3*x**2

    The ``variables`` argument specifies which are constants so that the
    other symbols will not be renumbered:

    >>> constant_renumber(expr, [C1, x])
    C1*x**2  + C2 + C3*x

    The ``newconstants`` argument is used to specify what symbols to use when
    replacing the constants:

    >>> constant_renumber(expr, [x], newconstants=symbols('E1:4'))
    E1 + E2*x + E3*x**2

    """
def homogeneous_order(eq, *symbols):
    """
    Returns the order `n` if `g` is homogeneous and ``None`` if it is not
    homogeneous.

    Determines if a function is homogeneous and if so of what order.  A
    function `f(x, y, \\cdots)` is homogeneous of order `n` if `f(t x, t y,
    \\cdots) = t^n f(x, y, \\cdots)`.

    If the function is of two variables, `F(x, y)`, then `f` being homogeneous
    of any order is equivalent to being able to rewrite `F(x, y)` as `G(x/y)`
    or `H(y/x)`.  This fact is used to solve 1st order ordinary differential
    equations whose coefficients are homogeneous of the same order (see the
    docstrings of
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsDepDivIndep` and
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsIndepDivDep`).

    Symbols can be functions, but every argument of the function must be a
    symbol, and the arguments of the function that appear in the expression
    must match those given in the list of symbols.  If a declared function
    appears with different arguments than given in the list of symbols,
    ``None`` is returned.

    Examples
    ========

    >>> from sympy import Function, homogeneous_order, sqrt
    >>> from sympy.abc import x, y
    >>> f = Function('f')
    >>> homogeneous_order(f(x), f(x)) is None
    True
    >>> homogeneous_order(f(x,y), f(y, x), x, y) is None
    True
    >>> homogeneous_order(f(x), f(x), x)
    1
    >>> homogeneous_order(x**2*f(x)/sqrt(x**2+f(x)**2), x, f(x))
    2
    >>> homogeneous_order(x**2+f(x), x, f(x)) is None
    True

    """
def ode_2nd_power_series_ordinary(eq, func, order, match):
    '''
    Gives a power series solution to a second order homogeneous differential
    equation with polynomial coefficients at an ordinary point. A homogeneous
    differential equation is of the form

    .. math :: P(x)\\frac{d^2y}{dx^2} + Q(x)\\frac{dy}{dx} + R(x) y(x) = 0

    For simplicity it is assumed that `P(x)`, `Q(x)` and `R(x)` are polynomials,
    it is sufficient that `\\frac{Q(x)}{P(x)}` and `\\frac{R(x)}{P(x)}` exists at
    `x_{0}`. A recurrence relation is obtained by substituting `y` as `\\sum_{n=0}^\\infty a_{n}x^{n}`,
    in the differential equation, and equating the nth term. Using this relation
    various terms can be generated.


    Examples
    ========

    >>> from sympy import dsolve, Function, pprint
    >>> from sympy.abc import x
    >>> f = Function("f")
    >>> eq = f(x).diff(x, 2) + f(x)
    >>> pprint(dsolve(eq, hint=\'2nd_power_series_ordinary\'))
              / 4    2    \\        /     2\\\n              |x    x     |        |    x |    / 6\\\n    f(x) = C2*|-- - -- + 1| + C1*x*|1 - --| + O\\x /
              \\24   2     /        \\    6 /


    References
    ==========
    - https://tutorial.math.lamar.edu/Classes/DE/SeriesSolutions.aspx
    - George E. Simmons, "Differential Equations with Applications and
      Historical Notes", p.p 176 - 184

    '''
def ode_2nd_power_series_regular(eq, func, order, match):
    '''
    Gives a power series solution to a second order homogeneous differential
    equation with polynomial coefficients at a regular point. A second order
    homogeneous differential equation is of the form

    .. math :: P(x)\\frac{d^2y}{dx^2} + Q(x)\\frac{dy}{dx} + R(x) y(x) = 0

    A point is said to regular singular at `x0` if `x - x0\\frac{Q(x)}{P(x)}`
    and `(x - x0)^{2}\\frac{R(x)}{P(x)}` are analytic at `x0`. For simplicity
    `P(x)`, `Q(x)` and `R(x)` are assumed to be polynomials. The algorithm for
    finding the power series solutions is:

    1.  Try expressing `(x - x0)P(x)` and `((x - x0)^{2})Q(x)` as power series
        solutions about x0. Find `p0` and `q0` which are the constants of the
        power series expansions.
    2.  Solve the indicial equation `f(m) = m(m - 1) + m*p0 + q0`, to obtain the
        roots `m1` and `m2` of the indicial equation.
    3.  If `m1 - m2` is a non integer there exists two series solutions. If
        `m1 = m2`, there exists only one solution. If `m1 - m2` is an integer,
        then the existence of one solution is confirmed. The other solution may
        or may not exist.

    The power series solution is of the form `x^{m}\\sum_{n=0}^\\infty a_{n}x^{n}`. The
    coefficients are determined by the following recurrence relation.
    `a_{n} = -\\frac{\\sum_{k=0}^{n-1} q_{n-k} + (m + k)p_{n-k}}{f(m + n)}`. For the case
    in which `m1 - m2` is an integer, it can be seen from the recurrence relation
    that for the lower root `m`, when `n` equals the difference of both the
    roots, the denominator becomes zero. So if the numerator is not equal to zero,
    a second series solution exists.


    Examples
    ========

    >>> from sympy import dsolve, Function, pprint
    >>> from sympy.abc import x
    >>> f = Function("f")
    >>> eq = x*(f(x).diff(x, 2)) + 2*(f(x).diff(x)) + x*f(x)
    >>> pprint(dsolve(eq, hint=\'2nd_power_series_regular\'))
                                  /    6    4    2    \\\n                                  |   x    x    x     |
              /  4    2    \\   C1*|- --- + -- - -- + 1|
              | x    x     |      \\  720   24   2     /    / 6\\\n    f(x) = C2*|--- - -- + 1| + ------------------------ + O\\x /
              \\120   6     /              x


    References
    ==========
    - George E. Simmons, "Differential Equations with Applications and
      Historical Notes", p.p 176 - 184

    '''
def ode_1st_power_series(eq, func, order, match):
    """
    The power series solution is a method which gives the Taylor series expansion
    to the solution of a differential equation.

    For a first order differential equation `\\frac{dy}{dx} = h(x, y)`, a power
    series solution exists at a point `x = x_{0}` if `h(x, y)` is analytic at `x_{0}`.
    The solution is given by

    .. math:: y(x) = y(x_{0}) + \\sum_{n = 1}^{\\infty} \\frac{F_{n}(x_{0},b)(x - x_{0})^n}{n!},

    where `y(x_{0}) = b` is the value of y at the initial value of `x_{0}`.
    To compute the values of the `F_{n}(x_{0},b)` the following algorithm is
    followed, until the required number of terms are generated.

    1. `F_1 = h(x_{0}, b)`
    2. `F_{n+1} = \\frac{\\partial F_{n}}{\\partial x} + \\frac{\\partial F_{n}}{\\partial y}F_{1}`

    Examples
    ========

    >>> from sympy import Function, pprint, exp, dsolve
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = exp(x)*(f(x).diff(x)) - f(x)
    >>> pprint(dsolve(eq, hint='1st_power_series'))
                           3       4       5
                       C1*x    C1*x    C1*x     / 6\\\n    f(x) = C1 + C1*x - ----- + ----- + ----- + O\\x /
                         6       24      60


    References
    ==========

    - Travis W. Walker, Analytic power series technique for solving first-order
      differential equations, p.p 17, 18

    """
def checkinfsol(eq, infinitesimals, func: Incomplete | None = None, order: Incomplete | None = None):
    """
    This function is used to check if the given infinitesimals are the
    actual infinitesimals of the given first order differential equation.
    This method is specific to the Lie Group Solver of ODEs.

    As of now, it simply checks, by substituting the infinitesimals in the
    partial differential equation.


    .. math:: \\frac{\\partial \\eta}{\\partial x} + \\left(\\frac{\\partial \\eta}{\\partial y}
                - \\frac{\\partial \\xi}{\\partial x}\\right)*h
                - \\frac{\\partial \\xi}{\\partial y}*h^{2}
                - \\xi\\frac{\\partial h}{\\partial x} - \\eta\\frac{\\partial h}{\\partial y} = 0


    where `\\eta`, and `\\xi` are the infinitesimals and `h(x,y) = \\frac{dy}{dx}`

    The infinitesimals should be given in the form of a list of dicts
    ``[{xi(x, y): inf, eta(x, y): inf}]``, corresponding to the
    output of the function infinitesimals. It returns a list
    of values of the form ``[(True/False, sol)]`` where ``sol`` is the value
    obtained after substituting the infinitesimals in the PDE. If it
    is ``True``, then ``sol`` would be 0.

    """
def sysode_linear_2eq_order1(match_): ...
def sysode_nonlinear_2eq_order1(match_): ...
def sysode_nonlinear_3eq_order1(match_): ...
