from _typeshed import Incomplete
from sympy.core import Add as Add, Mul as Mul, S as S
from sympy.core.containers import Tuple as Tuple
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, Function as Function, Subs as Subs, expand as expand, expand_mul as expand_mul
from sympy.core.numbers import I as I
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.sorting import default_sort_key as default_sort_key, ordered as ordered
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions import Piecewise as Piecewise, cos as cos, exp as exp, im as im, log as log, piecewise_fold as piecewise_fold, re as re, sin as sin, sqrt as sqrt
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.integrals.integrals import Integral as Integral, integrate as integrate
from sympy.matrices import Matrix as Matrix, MatrixBase as MatrixBase, NonSquareMatrixError as NonSquareMatrixError, eye as eye, zeros as zeros
from sympy.polys import Poly as Poly, together as together
from sympy.sets.sets import FiniteSet as FiniteSet
from sympy.simplify import collect as collect, radsimp as radsimp, signsimp as signsimp
from sympy.simplify.powsimp import powdenest as powdenest, powsimp as powsimp
from sympy.simplify.ratsimp import ratsimp as ratsimp
from sympy.simplify.simplify import simplify as simplify
from sympy.solvers.deutils import ode_order as ode_order
from sympy.solvers.solveset import NonlinearError as NonlinearError, solveset as solveset
from sympy.utilities.iterables import connected_components as connected_components, iterable as iterable, strongly_connected_components as strongly_connected_components
from sympy.utilities.misc import filldedent as filldedent

class ODEOrderError(ValueError):
    """Raised by linear_ode_to_matrix if the system has the wrong order"""
class ODENonlinearError(NonlinearError):
    """Raised by linear_ode_to_matrix if the system is nonlinear"""

def simpsol(sol, wrt1, wrt2, doit: bool = True):
    """Simplify solutions from dsolve_system."""
def linodesolve_type(A, t, b: Incomplete | None = None):
    '''
    Helper function that determines the type of the system of ODEs for solving with :obj:`sympy.solvers.ode.systems.linodesolve()`

    Explanation
    ===========

    This function takes in the coefficient matrix and/or the non-homogeneous term
    and returns the type of the equation that can be solved by :obj:`sympy.solvers.ode.systems.linodesolve()`.

    If the system is constant coefficient homogeneous, then "type1" is returned

    If the system is constant coefficient non-homogeneous, then "type2" is returned

    If the system is non-constant coefficient homogeneous, then "type3" is returned

    If the system is non-constant coefficient non-homogeneous, then "type4" is returned

    If the system has a non-constant coefficient matrix which can be factorized into constant
    coefficient matrix, then "type5" or "type6" is returned for when the system is homogeneous or
    non-homogeneous respectively.

    Note that, if the system of ODEs is of "type3" or "type4", then along with the type,
    the commutative antiderivative of the coefficient matrix is also returned.

    If the system cannot be solved by :obj:`sympy.solvers.ode.systems.linodesolve()`, then
    NotImplementedError is raised.

    Parameters
    ==========

    A : Matrix
        Coefficient matrix of the system of ODEs
    b : Matrix or None
        Non-homogeneous term of the system. The default value is None.
        If this argument is None, then the system is assumed to be homogeneous.

    Examples
    ========

    >>> from sympy import symbols, Matrix
    >>> from sympy.solvers.ode.systems import linodesolve_type
    >>> t = symbols("t")
    >>> A = Matrix([[1, 1], [2, 3]])
    >>> b = Matrix([t, 1])

    >>> linodesolve_type(A, t)
    {\'antiderivative\': None, \'type_of_equation\': \'type1\'}

    >>> linodesolve_type(A, t, b=b)
    {\'antiderivative\': None, \'type_of_equation\': \'type2\'}

    >>> A_t = Matrix([[1, t], [-t, 1]])

    >>> linodesolve_type(A_t, t)
    {\'antiderivative\': Matrix([
    [      t, t**2/2],
    [-t**2/2,      t]]), \'type_of_equation\': \'type3\'}

    >>> linodesolve_type(A_t, t, b=b)
    {\'antiderivative\': Matrix([
    [      t, t**2/2],
    [-t**2/2,      t]]), \'type_of_equation\': \'type4\'}

    >>> A_non_commutative = Matrix([[1, t], [t, -1]])
    >>> linodesolve_type(A_non_commutative, t)
    Traceback (most recent call last):
    ...
    NotImplementedError:
    The system does not have a commutative antiderivative, it cannot be
    solved by linodesolve.

    Returns
    =======

    Dict

    Raises
    ======

    NotImplementedError
        When the coefficient matrix does not have a commutative antiderivative

    See Also
    ========

    linodesolve: Function for which linodesolve_type gets the information

    '''
def linear_ode_to_matrix(eqs, funcs, t, order):
    """
    Convert a linear system of ODEs to matrix form

    Explanation
    ===========

    Express a system of linear ordinary differential equations as a single
    matrix differential equation [1]. For example the system $x' = x + y + 1$
    and $y' = x - y$ can be represented as

    .. math:: A_1 X' = A_0 X + b

    where $A_1$ and $A_0$ are $2 \\times 2$ matrices and $b$, $X$ and $X'$ are
    $2 \\times 1$ matrices with $X = [x, y]^T$.

    Higher-order systems are represented with additional matrices e.g. a
    second-order system would look like

    .. math:: A_2 X'' =  A_1 X' + A_0 X  + b

    Examples
    ========

    >>> from sympy import Function, Symbol, Matrix, Eq
    >>> from sympy.solvers.ode.systems import linear_ode_to_matrix
    >>> t = Symbol('t')
    >>> x = Function('x')
    >>> y = Function('y')

    We can create a system of linear ODEs like

    >>> eqs = [
    ...     Eq(x(t).diff(t), x(t) + y(t) + 1),
    ...     Eq(y(t).diff(t), x(t) - y(t)),
    ... ]
    >>> funcs = [x(t), y(t)]
    >>> order = 1 # 1st order system

    Now ``linear_ode_to_matrix`` can represent this as a matrix
    differential equation.

    >>> (A1, A0), b = linear_ode_to_matrix(eqs, funcs, t, order)
    >>> A1
    Matrix([
    [1, 0],
    [0, 1]])
    >>> A0
    Matrix([
    [1, 1],
    [1,  -1]])
    >>> b
    Matrix([
    [1],
    [0]])

    The original equations can be recovered from these matrices:

    >>> eqs_mat = Matrix([eq.lhs - eq.rhs for eq in eqs])
    >>> X = Matrix(funcs)
    >>> A1 * X.diff(t) - A0 * X - b == eqs_mat
    True

    If the system of equations has a maximum order greater than the
    order of the system specified, a ODEOrderError exception is raised.

    >>> eqs = [Eq(x(t).diff(t, 2), x(t).diff(t) + x(t)), Eq(y(t).diff(t), y(t) + x(t))]
    >>> linear_ode_to_matrix(eqs, funcs, t, 1)
    Traceback (most recent call last):
    ...
    ODEOrderError: Cannot represent system in 1-order form

    If the system of equations is nonlinear, then ODENonlinearError is
    raised.

    >>> eqs = [Eq(x(t).diff(t), x(t) + y(t)), Eq(y(t).diff(t), y(t)**2 + x(t))]
    >>> linear_ode_to_matrix(eqs, funcs, t, 1)
    Traceback (most recent call last):
    ...
    ODENonlinearError: The system of ODEs is nonlinear.

    Parameters
    ==========

    eqs : list of SymPy expressions or equalities
        The equations as expressions (assumed equal to zero).
    funcs : list of applied functions
        The dependent variables of the system of ODEs.
    t : symbol
        The independent variable.
    order : int
        The order of the system of ODEs.

    Returns
    =======

    The tuple ``(As, b)`` where ``As`` is a tuple of matrices and ``b`` is the
    the matrix representing the rhs of the matrix equation.

    Raises
    ======

    ODEOrderError
        When the system of ODEs have an order greater than what was specified
    ODENonlinearError
        When the system of ODEs is nonlinear

    See Also
    ========

    linear_eq_to_matrix: for systems of linear algebraic equations.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Matrix_differential_equation

    """
def matrix_exp(A, t):
    """
    Matrix exponential $\\exp(A*t)$ for the matrix ``A`` and scalar ``t``.

    Explanation
    ===========

    This functions returns the $\\exp(A*t)$ by doing a simple
    matrix multiplication:

    .. math:: \\exp(A*t) = P * expJ * P^{-1}

    where $expJ$ is $\\exp(J*t)$. $J$ is the Jordan normal
    form of $A$ and $P$ is matrix such that:

    .. math:: A = P * J * P^{-1}

    The matrix exponential $\\exp(A*t)$ appears in the solution of linear
    differential equations. For example if $x$ is a vector and $A$ is a matrix
    then the initial value problem

    .. math:: \\frac{dx(t)}{dt} = A \\times x(t),   x(0) = x0

    has the unique solution

    .. math:: x(t) = \\exp(A t) x0

    Examples
    ========

    >>> from sympy import Symbol, Matrix, pprint
    >>> from sympy.solvers.ode.systems import matrix_exp
    >>> t = Symbol('t')

    We will consider a 2x2 matrix for comupting the exponential

    >>> A = Matrix([[2, -5], [2, -4]])
    >>> pprint(A)
    [2  -5]
    [     ]
    [2  -4]

    Now, exp(A*t) is given as follows:

    >>> pprint(matrix_exp(A, t))
    [   -t           -t                    -t              ]
    [3*e  *sin(t) + e  *cos(t)         -5*e  *sin(t)       ]
    [                                                      ]
    [         -t                     -t           -t       ]
    [      2*e  *sin(t)         - 3*e  *sin(t) + e  *cos(t)]

    Parameters
    ==========

    A : Matrix
        The matrix $A$ in the expression $\\exp(A*t)$
    t : Symbol
        The independent variable

    See Also
    ========

    matrix_exp_jordan_form: For exponential of Jordan normal form

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Jordan_normal_form
    .. [2] https://en.wikipedia.org/wiki/Matrix_exponential

    """
def matrix_exp_jordan_form(A, t):
    """
    Matrix exponential $\\exp(A*t)$ for the matrix *A* and scalar *t*.

    Explanation
    ===========

    Returns the Jordan form of the $\\exp(A*t)$ along with the matrix $P$ such that:

    .. math::
        \\exp(A*t) = P * expJ * P^{-1}

    Examples
    ========

    >>> from sympy import Matrix, Symbol
    >>> from sympy.solvers.ode.systems import matrix_exp, matrix_exp_jordan_form
    >>> t = Symbol('t')

    We will consider a 2x2 defective matrix. This shows that our method
    works even for defective matrices.

    >>> A = Matrix([[1, 1], [0, 1]])

    It can be observed that this function gives us the Jordan normal form
    and the required invertible matrix P.

    >>> P, expJ = matrix_exp_jordan_form(A, t)

    Here, it is shown that P and expJ returned by this function is correct
    as they satisfy the formula: P * expJ * P_inverse = exp(A*t).

    >>> P * expJ * P.inv() == matrix_exp(A, t)
    True

    Parameters
    ==========

    A : Matrix
        The matrix $A$ in the expression $\\exp(A*t)$
    t : Symbol
        The independent variable

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Defective_matrix
    .. [2] https://en.wikipedia.org/wiki/Jordan_matrix
    .. [3] https://en.wikipedia.org/wiki/Jordan_normal_form

    """
def linodesolve(A, t, b: Incomplete | None = None, B: Incomplete | None = None, type: str = 'auto', doit: bool = False, tau: Incomplete | None = None):
    '''
    System of n equations linear first-order differential equations

    Explanation
    ===========

    This solver solves the system of ODEs of the following form:

    .. math::
        X\'(t) = A(t) X(t) +  b(t)

    Here, $A(t)$ is the coefficient matrix, $X(t)$ is the vector of n independent variables,
    $b(t)$ is the non-homogeneous term and $X\'(t)$ is the derivative of $X(t)$

    Depending on the properties of $A(t)$ and $b(t)$, this solver evaluates the solution
    differently.

    When $A(t)$ is constant coefficient matrix and $b(t)$ is zero vector i.e. system is homogeneous,
    the system is "type1". The solution is:

    .. math::
        X(t) = \\exp(A t) C

    Here, $C$ is a vector of constants and $A$ is the constant coefficient matrix.

    When $A(t)$ is constant coefficient matrix and $b(t)$ is non-zero i.e. system is non-homogeneous,
    the system is "type2". The solution is:

    .. math::
        X(t) = e^{A t} ( \\int e^{- A t} b \\,dt + C)

    When $A(t)$ is coefficient matrix such that its commutative with its antiderivative $B(t)$ and
    $b(t)$ is a zero vector i.e. system is homogeneous, the system is "type3". The solution is:

    .. math::
        X(t) = \\exp(B(t)) C

    When $A(t)$ is commutative with its antiderivative $B(t)$ and $b(t)$ is non-zero i.e. system is
    non-homogeneous, the system is "type4". The solution is:

    .. math::
        X(t) =  e^{B(t)} ( \\int e^{-B(t)} b(t) \\,dt + C)

    When $A(t)$ is a coefficient matrix such that it can be factorized into a scalar and a constant
    coefficient matrix:

    .. math::
        A(t) = f(t) * A

    Where $f(t)$ is a scalar expression in the independent variable $t$ and $A$ is a constant matrix,
    then we can do the following substitutions:

    .. math::
        tau = \\int f(t) dt, X(t) = Y(tau), b(t) = b(f^{-1}(tau))

    Here, the substitution for the non-homogeneous term is done only when its non-zero.
    Using these substitutions, our original system becomes:

    .. math::
        Y\'(tau) = A * Y(tau) + b(tau)/f(tau)

    The above system can be easily solved using the solution for "type1" or "type2" depending
    on the homogeneity of the system. After we get the solution for $Y(tau)$, we substitute the
    solution for $tau$ as $t$ to get back $X(t)$

    .. math::
        X(t) = Y(tau)

    Systems of "type5" and "type6" have a commutative antiderivative but we use this solution
    because its faster to compute.

    The final solution is the general solution for all the four equations since a constant coefficient
    matrix is always commutative with its antidervative.

    An additional feature of this function is, if someone wants to substitute for value of the independent
    variable, they can pass the substitution `tau` and the solution will have the independent variable
    substituted with the passed expression(`tau`).

    Parameters
    ==========

    A : Matrix
        Coefficient matrix of the system of linear first order ODEs.
    t : Symbol
        Independent variable in the system of ODEs.
    b : Matrix or None
        Non-homogeneous term in the system of ODEs. If None is passed,
        a homogeneous system of ODEs is assumed.
    B : Matrix or None
        Antiderivative of the coefficient matrix. If the antiderivative
        is not passed and the solution requires the term, then the solver
        would compute it internally.
    type : String
        Type of the system of ODEs passed. Depending on the type, the
        solution is evaluated. The type values allowed and the corresponding
        system it solves are: "type1" for constant coefficient homogeneous
        "type2" for constant coefficient non-homogeneous, "type3" for non-constant
        coefficient homogeneous, "type4" for non-constant coefficient non-homogeneous,
        "type5" and "type6" for non-constant coefficient homogeneous and non-homogeneous
        systems respectively where the coefficient matrix can be factorized to a constant
        coefficient matrix.
        The default value is "auto" which will let the solver decide the correct type of
        the system passed.
    doit : Boolean
        Evaluate the solution if True, default value is False
    tau: Expression
        Used to substitute for the value of `t` after we get the solution of the system.

    Examples
    ========

    To solve the system of ODEs using this function directly, several things must be
    done in the right order. Wrong inputs to the function will lead to incorrect results.

    >>> from sympy import symbols, Function, Eq
    >>> from sympy.solvers.ode.systems import canonical_odes, linear_ode_to_matrix, linodesolve, linodesolve_type
    >>> from sympy.solvers.ode.subscheck import checkodesol
    >>> f, g = symbols("f, g", cls=Function)
    >>> x, a = symbols("x, a")
    >>> funcs = [f(x), g(x)]
    >>> eqs = [Eq(f(x).diff(x) - f(x), a*g(x) + 1), Eq(g(x).diff(x) + g(x), a*f(x))]

    Here, it is important to note that before we derive the coefficient matrix, it is
    important to get the system of ODEs into the desired form. For that we will use
    :obj:`sympy.solvers.ode.systems.canonical_odes()`.

    >>> eqs = canonical_odes(eqs, funcs, x)
    >>> eqs
    [[Eq(Derivative(f(x), x), a*g(x) + f(x) + 1), Eq(Derivative(g(x), x), a*f(x) - g(x))]]

    Now, we will use :obj:`sympy.solvers.ode.systems.linear_ode_to_matrix()` to get the coefficient matrix and the
    non-homogeneous term if it is there.

    >>> eqs = eqs[0]
    >>> (A1, A0), b = linear_ode_to_matrix(eqs, funcs, x, 1)
    >>> A = A0

    We have the coefficient matrices and the non-homogeneous term ready. Now, we can use
    :obj:`sympy.solvers.ode.systems.linodesolve_type()` to get the information for the system of ODEs
    to finally pass it to the solver.

    >>> system_info = linodesolve_type(A, x, b=b)
    >>> sol_vector = linodesolve(A, x, b=b, B=system_info[\'antiderivative\'], type=system_info[\'type_of_equation\'])

    Now, we can prove if the solution is correct or not by using :obj:`sympy.solvers.ode.checkodesol()`

    >>> sol = [Eq(f, s) for f, s in zip(funcs, sol_vector)]
    >>> checkodesol(eqs, sol)
    (True, [0, 0])

    We can also use the doit method to evaluate the solutions passed by the function.

    >>> sol_vector_evaluated = linodesolve(A, x, b=b, type="type2", doit=True)

    Now, we will look at a system of ODEs which is non-constant.

    >>> eqs = [Eq(f(x).diff(x), f(x) + x*g(x)), Eq(g(x).diff(x), -x*f(x) + g(x))]

    The system defined above is already in the desired form, so we do not have to convert it.

    >>> (A1, A0), b = linear_ode_to_matrix(eqs, funcs, x, 1)
    >>> A = A0

    A user can also pass the commutative antiderivative required for type3 and type4 system of ODEs.
    Passing an incorrect one will lead to incorrect results. If the coefficient matrix is not commutative
    with its antiderivative, then :obj:`sympy.solvers.ode.systems.linodesolve_type()` raises a NotImplementedError.
    If it does have a commutative antiderivative, then the function just returns the information about the system.

    >>> system_info = linodesolve_type(A, x, b=b)

    Now, we can pass the antiderivative as an argument to get the solution. If the system information is not
    passed, then the solver will compute the required arguments internally.

    >>> sol_vector = linodesolve(A, x, b=b)

    Once again, we can verify the solution obtained.

    >>> sol = [Eq(f, s) for f, s in zip(funcs, sol_vector)]
    >>> checkodesol(eqs, sol)
    (True, [0, 0])

    Returns
    =======

    List

    Raises
    ======

    ValueError
        This error is raised when the coefficient matrix, non-homogeneous term
        or the antiderivative, if passed, are not a matrix or
        do not have correct dimensions
    NonSquareMatrixError
        When the coefficient matrix or its antiderivative, if passed is not a
        square matrix
    NotImplementedError
        If the coefficient matrix does not have a commutative antiderivative

    See Also
    ========

    linear_ode_to_matrix: Coefficient matrix computation function
    canonical_odes: System of ODEs representation change
    linodesolve_type: Getting information about systems of ODEs to pass in this solver

    '''
def canonical_odes(eqs, funcs, t):
    '''
    Function that solves for highest order derivatives in a system

    Explanation
    ===========

    This function inputs a system of ODEs and based on the system,
    the dependent variables and their highest order, returns the system
    in the following form:

    .. math::
        X\'(t) = A(t) X(t) + b(t)

    Here, $X(t)$ is the vector of dependent variables of lower order, $A(t)$ is
    the coefficient matrix, $b(t)$ is the non-homogeneous term and $X\'(t)$ is the
    vector of dependent variables in their respective highest order. We use the term
    canonical form to imply the system of ODEs which is of the above form.

    If the system passed has a non-linear term with multiple solutions, then a list of
    systems is returned in its canonical form.

    Parameters
    ==========

    eqs : List
        List of the ODEs
    funcs : List
        List of dependent variables
    t : Symbol
        Independent variable

    Examples
    ========

    >>> from sympy import symbols, Function, Eq, Derivative
    >>> from sympy.solvers.ode.systems import canonical_odes
    >>> f, g = symbols("f g", cls=Function)
    >>> x, y = symbols("x y")
    >>> funcs = [f(x), g(x)]
    >>> eqs = [Eq(f(x).diff(x) - 7*f(x), 12*g(x)), Eq(g(x).diff(x) + g(x), 20*f(x))]

    >>> canonical_eqs = canonical_odes(eqs, funcs, x)
    >>> canonical_eqs
    [[Eq(Derivative(f(x), x), 7*f(x) + 12*g(x)), Eq(Derivative(g(x), x), 20*f(x) - g(x))]]

    >>> system = [Eq(Derivative(f(x), x)**2 - 2*Derivative(f(x), x) + 1, 4), Eq(-y*f(x) + Derivative(g(x), x), 0)]

    >>> canonical_system = canonical_odes(system, funcs, x)
    >>> canonical_system
    [[Eq(Derivative(f(x), x), -1), Eq(Derivative(g(x), x), y*f(x))], [Eq(Derivative(f(x), x), 3), Eq(Derivative(g(x), x), y*f(x))]]

    Returns
    =======

    List

    '''
def dsolve_system(eqs, funcs: Incomplete | None = None, t: Incomplete | None = None, ics: Incomplete | None = None, doit: bool = False, simplify: bool = True):
    '''
    Solves any(supported) system of Ordinary Differential Equations

    Explanation
    ===========

    This function takes a system of ODEs as an input, determines if the
    it is solvable by this function, and returns the solution if found any.

    This function can handle:
    1. Linear, First Order, Constant coefficient homogeneous system of ODEs
    2. Linear, First Order, Constant coefficient non-homogeneous system of ODEs
    3. Linear, First Order, non-constant coefficient homogeneous system of ODEs
    4. Linear, First Order, non-constant coefficient non-homogeneous system of ODEs
    5. Any implicit system which can be divided into system of ODEs which is of the above 4 forms
    6. Any higher order linear system of ODEs that can be reduced to one of the 5 forms of systems described above.

    The types of systems described above are not limited by the number of equations, i.e. this
    function can solve the above types irrespective of the number of equations in the system passed.
    But, the bigger the system, the more time it will take to solve the system.

    This function returns a list of solutions. Each solution is a list of equations where LHS is
    the dependent variable and RHS is an expression in terms of the independent variable.

    Among the non constant coefficient types, not all the systems are solvable by this function. Only
    those which have either a coefficient matrix with a commutative antiderivative or those systems which
    may be divided further so that the divided systems may have coefficient matrix with commutative antiderivative.

    Parameters
    ==========

    eqs : List
        system of ODEs to be solved
    funcs : List or None
        List of dependent variables that make up the system of ODEs
    t : Symbol or None
        Independent variable in the system of ODEs
    ics : Dict or None
        Set of initial boundary/conditions for the system of ODEs
    doit : Boolean
        Evaluate the solutions if True. Default value is True. Can be
        set to false if the integral evaluation takes too much time and/or
        is not required.
    simplify: Boolean
        Simplify the solutions for the systems. Default value is True.
        Can be set to false if simplification takes too much time and/or
        is not required.

    Examples
    ========

    >>> from sympy import symbols, Eq, Function
    >>> from sympy.solvers.ode.systems import dsolve_system
    >>> f, g = symbols("f g", cls=Function)
    >>> x = symbols("x")

    >>> eqs = [Eq(f(x).diff(x), g(x)), Eq(g(x).diff(x), f(x))]
    >>> dsolve_system(eqs)
    [[Eq(f(x), -C1*exp(-x) + C2*exp(x)), Eq(g(x), C1*exp(-x) + C2*exp(x))]]

    You can also pass the initial conditions for the system of ODEs:

    >>> dsolve_system(eqs, ics={f(0): 1, g(0): 0})
    [[Eq(f(x), exp(x)/2 + exp(-x)/2), Eq(g(x), exp(x)/2 - exp(-x)/2)]]

    Optionally, you can pass the dependent variables and the independent
    variable for which the system is to be solved:

    >>> funcs = [f(x), g(x)]
    >>> dsolve_system(eqs, funcs=funcs, t=x)
    [[Eq(f(x), -C1*exp(-x) + C2*exp(x)), Eq(g(x), C1*exp(-x) + C2*exp(x))]]

    Lets look at an implicit system of ODEs:

    >>> eqs = [Eq(f(x).diff(x)**2, g(x)**2), Eq(g(x).diff(x), g(x))]
    >>> dsolve_system(eqs)
    [[Eq(f(x), C1 - C2*exp(x)), Eq(g(x), C2*exp(x))], [Eq(f(x), C1 + C2*exp(x)), Eq(g(x), C2*exp(x))]]

    Returns
    =======

    List of List of Equations

    Raises
    ======

    NotImplementedError
        When the system of ODEs is not solvable by this function.
    ValueError
        When the parameters passed are not in the required form.

    '''
