from ..libmp.backend import xrange as xrange
from _typeshed import Incomplete

class OptimizationMethods:
    def __init__(ctx) -> None: ...

class Newton:
    """
    1d-solver generating pairs of approximative root and error.

    Needs starting points x0 close to the root.

    Pro:

    * converges fast
    * sometimes more robust than secant with bad second starting point

    Contra:

    * converges slowly for multiple roots
    * needs first derivative
    * 2 function evaluations per iteration
    """
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Secant:
    """
    1d-solver generating pairs of approximative root and error.

    Needs starting points x0 and x1 close to the root.
    x1 defaults to x0 + 0.25.

    Pro:

    * converges fast

    Contra:

    * converges slowly for multiple roots
    """
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    x1: Incomplete
    f: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class MNewton:
    """
    1d-solver generating pairs of approximative root and error.

    Needs starting point x0 close to the root.
    Uses modified Newton's method that converges fast regardless of the
    multiplicity of the root.

    Pro:

    * converges fast for multiple roots

    Contra:

    * needs first and second derivative of f
    * 3 function evaluations per iteration
    """
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    d2f: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Halley:
    """
    1d-solver generating pairs of approximative root and error.

    Needs a starting point x0 close to the root.
    Uses Halley's method with cubic convergence rate.

    Pro:

    * converges even faster the Newton's method
    * useful when computing with *many* digits

    Contra:

    * needs first and second derivative of f
    * 3 function evaluations per iteration
    * converges slowly for multiple roots
    """
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    d2f: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Muller:
    """
    1d-solver generating pairs of approximative root and error.

    Needs starting points x0, x1 and x2 close to the root.
    x1 defaults to x0 + 0.25; x2 to x1 + 0.25.
    Uses Muller's method that converges towards complex roots.

    Pro:

    * converges fast (somewhat faster than secant)
    * can find complex roots

    Contra:

    * converges slowly for multiple roots
    * may have complex values for real starting points and real roots

    http://en.wikipedia.org/wiki/Muller's_method
    """
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    x1: Incomplete
    x2: Incomplete
    f: Incomplete
    verbose: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Bisection:
    """
    1d-solver generating pairs of approximative root and error.

    Uses bisection method to find a root of f in [a, b].
    Might fail for multiple roots (needs sign change).

    Pro:

    * robust and reliable

    Contra:

    * converges slowly
    * needs sign change
    """
    maxsteps: int
    ctx: Incomplete
    f: Incomplete
    a: Incomplete
    b: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class Illinois:
    """
    1d-solver generating pairs of approximative root and error.

    Uses Illinois method or similar to find a root of f in [a, b].
    Might fail for multiple roots (needs sign change).
    Combines bisect with secant (improved regula falsi).

    The only difference between the methods is the scaling factor m, which is
    used to ensure convergence (you can choose one using the 'method' keyword):

    Illinois method ('illinois'):
        m = 0.5

    Pegasus method ('pegasus'):
        m = fb/(fb + fz)

    Anderson-Bjoerk method ('anderson'):
        m = 1 - fz/fb if positive else 0.5

    Pro:

    * converges very fast

    Contra:

    * has problems with multiple roots
    * needs sign change
    """
    maxsteps: int
    ctx: Incomplete
    a: Incomplete
    b: Incomplete
    f: Incomplete
    tol: Incomplete
    verbose: Incomplete
    method: Incomplete
    getm: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

def Pegasus(*args, **kwargs):
    """
    1d-solver generating pairs of approximative root and error.

    Uses Pegasus method to find a root of f in [a, b].
    Wrapper for illinois to use method='pegasus'.
    """
def Anderson(*args, **kwargs):
    """
    1d-solver generating pairs of approximative root and error.

    Uses Anderson-Bjoerk method to find a root of f in [a, b].
    Wrapper for illinois to use method='pegasus'.
    """

class Ridder:
    """
    1d-solver generating pairs of approximative root and error.

    Ridders' method to find a root of f in [a, b].
    Is told to perform as well as Brent's method while being simpler.

    Pro:

    * very fast
    * simpler than Brent's method

    Contra:

    * two function evaluations per step
    * has problems with multiple roots
    * needs sign change

    http://en.wikipedia.org/wiki/Ridders'_method
    """
    maxsteps: int
    ctx: Incomplete
    f: Incomplete
    x1: Incomplete
    x2: Incomplete
    verbose: Incomplete
    tol: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

class ANewton:
    """
    EXPERIMENTAL 1d-solver generating pairs of approximative root and error.

    Uses Newton's method modified to use Steffensens method when convergence is
    slow. (I.e. for multiple roots.)
    """
    maxsteps: int
    ctx: Incomplete
    x0: Incomplete
    f: Incomplete
    df: Incomplete
    phi: Incomplete
    verbose: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

def jacobian(ctx, f, x):
    """
    Calculate the Jacobian matrix of a function at the point x0.

    This is the first derivative of a vectorial function:

        f : R^m -> R^n with m >= n
    """

class MDNewton:
    """
    Find the root of a vector function numerically using Newton's method.

    f is a vector function representing a nonlinear equation system.

    x0 is the starting point close to the root.

    J is a function returning the Jacobian matrix for a point.

    Supports overdetermined systems.

    Use the 'norm' keyword to specify which norm to use. Defaults to max-norm.
    The function to calculate the Jacobian matrix can be given using the
    keyword 'J'. Otherwise it will be calculated numerically.

    Please note that this method converges only locally. Especially for high-
    dimensional systems it is not trivial to find a good starting point being
    close enough to the root.

    It is recommended to use a faster, low-precision solver from SciPy [1] or
    OpenOpt [2] to get an initial guess. Afterwards you can use this method for
    root-polishing to any precision.

    [1] http://scipy.org

    [2] http://openopt.org/Welcome
    """
    maxsteps: int
    ctx: Incomplete
    f: Incomplete
    x0: Incomplete
    J: Incomplete
    norm: Incomplete
    verbose: Incomplete
    def __init__(self, ctx, f, x0, **kwargs) -> None: ...
    def __iter__(self): ...

str2solver: Incomplete

def findroot(ctx, f, x0, solver: str = 'secant', tol: Incomplete | None = None, verbose: bool = False, verify: bool = True, **kwargs):
    """
    Find an approximate solution to `f(x) = 0`, using *x0* as starting point or
    interval for *x*.

    Multidimensional overdetermined systems are supported.
    You can specify them using a function or a list of functions.

    Mathematically speaking, this function returns `x` such that
    `|f(x)|^2 \\leq \\mathrm{tol}` is true within the current working precision.
    If the computed value does not meet this criterion, an exception is raised.
    This exception can be disabled with *verify=False*.

    For interval arithmetic (``iv.findroot()``), please note that
    the returned interval ``x`` is not guaranteed to contain `f(x)=0`!
    It is only some `x` for which `|f(x)|^2 \\leq \\mathrm{tol}` certainly holds
    regardless of numerical error. This may be improved in the future.

    **Arguments**

    *f*
        one dimensional function
    *x0*
        starting point, several starting points or interval (depends on solver)
    *tol*
        the returned solution has an error smaller than this
    *verbose*
        print additional information for each iteration if true
    *verify*
        verify the solution and raise a ValueError if `|f(x)|^2 > \\mathrm{tol}`
    *solver*
        a generator for *f* and *x0* returning approximative solution and error
    *maxsteps*
        after how many steps the solver will cancel
    *df*
        first derivative of *f* (used by some solvers)
    *d2f*
        second derivative of *f* (used by some solvers)
    *multidimensional*
        force multidimensional solving
    *J*
        Jacobian matrix of *f* (used by multidimensional solvers)
    *norm*
        used vector norm (used by multidimensional solvers)

    solver has to be callable with ``(f, x0, **kwargs)`` and return an generator
    yielding pairs of approximative solution and estimated error (which is
    expected to be positive).
    You can use the following string aliases:
    'secant', 'mnewton', 'halley', 'muller', 'illinois', 'pegasus', 'anderson',
    'ridder', 'anewton', 'bisect'

    See mpmath.calculus.optimization for their documentation.

    **Examples**

    The function :func:`~mpmath.findroot` locates a root of a given function using the
    secant method by default. A simple example use of the secant method is to
    compute `\\pi` as the root of `\\sin x` closest to `x_0 = 3`::

        >>> from mpmath import *
        >>> mp.dps = 30; mp.pretty = True
        >>> findroot(sin, 3)
        3.14159265358979323846264338328

    The secant method can be used to find complex roots of analytic functions,
    although it must in that case generally be given a nonreal starting value
    (or else it will never leave the real line)::

        >>> mp.dps = 15
        >>> findroot(lambda x: x**3 + 2*x + 1, j)
        (0.226698825758202 + 1.46771150871022j)

    A nice application is to compute nontrivial roots of the Riemann zeta
    function with many digits (good initial values are needed for convergence)::

        >>> mp.dps = 30
        >>> findroot(zeta, 0.5+14j)
        (0.5 + 14.1347251417346937904572519836j)

    The secant method can also be used as an optimization algorithm, by passing
    it a derivative of a function. The following example locates the positive
    minimum of the gamma function::

        >>> mp.dps = 20
        >>> findroot(lambda x: diff(gamma, x), 1)
        1.4616321449683623413

    Finally, a useful application is to compute inverse functions, such as the
    Lambert W function which is the inverse of `w e^w`, given the first
    term of the solution's asymptotic expansion as the initial value. In basic
    cases, this gives identical results to mpmath's built-in ``lambertw``
    function::

        >>> def lambert(x):
        ...     return findroot(lambda w: w*exp(w) - x, log(1+x))
        ...
        >>> mp.dps = 15
        >>> lambert(1); lambertw(1)
        0.567143290409784
        0.567143290409784
        >>> lambert(1000); lambert(1000)
        5.2496028524016
        5.2496028524016

    Multidimensional functions are also supported::

        >>> f = [lambda x1, x2: x1**2 + x2,
        ...      lambda x1, x2: 5*x1**2 - 3*x1 + 2*x2 - 3]
        >>> findroot(f, (0, 0))
        [-0.618033988749895]
        [-0.381966011250105]
        >>> findroot(f, (10, 10))
        [ 1.61803398874989]
        [-2.61803398874989]

    You can verify this by solving the system manually.

    Please note that the following (more general) syntax also works::

        >>> def f(x1, x2):
        ...     return x1**2 + x2, 5*x1**2 - 3*x1 + 2*x2 - 3
        ...
        >>> findroot(f, (0, 0))
        [-0.618033988749895]
        [-0.381966011250105]


    **Multiple roots**

    For multiple roots all methods of the Newtonian family (including secant)
    converge slowly. Consider this example::

        >>> f = lambda x: (x - 1)**99
        >>> findroot(f, 0.9, verify=False)
        0.918073542444929

    Even for a very close starting point the secant method converges very
    slowly. Use ``verbose=True`` to illustrate this.

    It is possible to modify Newton's method to make it converge regardless of
    the root's multiplicity::

        >>> findroot(f, -10, solver='mnewton')
        1.0

    This variant uses the first and second derivative of the function, which is
    not very efficient.

    Alternatively you can use an experimental Newtonian solver that keeps track
    of the speed of convergence and accelerates it using Steffensen's method if
    necessary::

        >>> findroot(f, -10, solver='anewton', verbose=True)
        x:     -9.88888888888888888889
        error: 0.111111111111111111111
        converging slowly
        x:     -9.77890011223344556678
        error: 0.10998877665544332211
        converging slowly
        x:     -9.67002233332199662166
        error: 0.108877778911448945119
        converging slowly
        accelerating convergence
        x:     -9.5622443299551077669
        error: 0.107778003366888854764
        converging slowly
        x:     0.99999999999999999214
        error: 10.562244329955107759
        x:     1.0
        error: 7.8598304758094664213e-18
        ZeroDivisionError: canceled with x = 1.0
        1.0

    **Complex roots**

    For complex roots it's recommended to use Muller's method as it converges
    even for real starting points very fast::

        >>> findroot(lambda x: x**4 + x + 1, (0, 1, 2), solver='muller')
        (0.727136084491197 + 0.934099289460529j)


    **Intersection methods**

    When you need to find a root in a known interval, it's highly recommended to
    use an intersection-based solver like ``'anderson'`` or ``'ridder'``.
    Usually they converge faster and more reliable. They have however problems
    with multiple roots and usually need a sign change to find a root::

        >>> findroot(lambda x: x**3, (-1, 1), solver='anderson')
        0.0

    Be careful with symmetric functions::

        >>> findroot(lambda x: x**2, (-1, 1), solver='anderson') #doctest:+ELLIPSIS
        Traceback (most recent call last):
          ...
        ZeroDivisionError

    It fails even for better starting points, because there is no sign change::

        >>> findroot(lambda x: x**2, (-1, .5), solver='anderson')
        Traceback (most recent call last):
          ...
        ValueError: Could not find root within given tolerance. (1.0 > 2.16840434497100886801e-19)
        Try another starting point or tweak arguments.

    """
def multiplicity(ctx, f, root, tol: Incomplete | None = None, maxsteps: int = 10, **kwargs):
    """
    Return the multiplicity of a given root of f.

    Internally, numerical derivatives are used. This might be inefficient for
    higher order derviatives. Due to this, ``multiplicity`` cancels after
    evaluating 10 derivatives by default. You can be specify the n-th derivative
    using the dnf keyword.

    >>> from mpmath import *
    >>> multiplicity(lambda x: sin(x) - 1, pi/2)
    2

    """
def steffensen(f):
    """
    linear convergent function -> quadratic convergent function

    Steffensen's method for quadratic convergence of a linear converging
    sequence.
    Don not use it for higher rates of convergence.
    It may even work for divergent sequences.

    Definition:
    F(x) = (x*f(f(x)) - f(x)**2) / (f(f(x)) - 2*f(x) + x)

    Example
    .......

    You can use Steffensen's method to accelerate a fixpoint iteration of linear
    (or less) convergence.

    x* is a fixpoint of the iteration x_{k+1} = phi(x_k) if x* = phi(x*). For
    phi(x) = x**2 there are two fixpoints: 0 and 1.

    Let's try Steffensen's method:

    >>> f = lambda x: x**2
    >>> from mpmath.calculus.optimization import steffensen
    >>> F = steffensen(f)
    >>> for x in [0.5, 0.9, 2.0]:
    ...     fx = Fx = x
    ...     for i in xrange(9):
    ...         try:
    ...             fx = f(fx)
    ...         except OverflowError:
    ...             pass
    ...         try:
    ...             Fx = F(Fx)
    ...         except ZeroDivisionError:
    ...             pass
    ...         print('%20g  %20g' % (fx, Fx))
                    0.25                  -0.5
                  0.0625                   0.1
              0.00390625            -0.0011236
             1.52588e-05           1.41691e-09
             2.32831e-10          -2.84465e-27
             5.42101e-20           2.30189e-80
             2.93874e-39          -1.2197e-239
             8.63617e-78                     0
            7.45834e-155                     0
                    0.81               1.02676
                  0.6561               1.00134
                0.430467                     1
                0.185302                     1
               0.0343368                     1
              0.00117902                     1
             1.39008e-06                     1
             1.93233e-12                     1
             3.73392e-24                     1
                       4                   1.6
                      16                1.2962
                     256               1.10194
                   65536               1.01659
             4.29497e+09               1.00053
             1.84467e+19                     1
             3.40282e+38                     1
             1.15792e+77                     1
            1.34078e+154                     1

    Unmodified, the iteration converges only towards 0. Modified it converges
    not only much faster, it converges even to the repelling fixpoint 1.
    """
