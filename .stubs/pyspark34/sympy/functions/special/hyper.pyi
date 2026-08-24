from sympy.core import Mod as Mod, S as S, ilcm as ilcm
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Derivative as Derivative, Function as Function
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, oo as oo, pi as pi, zoo as zoo
from sympy.core.relational import Ne as Ne
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import Dummy as Dummy
from sympy.functions import RisingFactorial as RisingFactorial, acosh as acosh, acoth as acoth, asin as asin, asinh as asinh, atan as atan, atanh as atanh, cos as cos, cosh as cosh, exp as exp, factorial as factorial, log as log, sin as sin, sinh as sinh, sqrt as sqrt
from sympy.functions.elementary.complexes import Abs as Abs, re as re, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp_polar as exp_polar
from sympy.functions.elementary.integers import ceiling as ceiling
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.logic.boolalg import And as And, Or as Or

class TupleArg(Tuple):
    def limit(self, x, xlim, dir: str = '+'):
        """ Compute limit x->xlim.
        """

class TupleParametersBase(Function):
    """ Base class that takes care of differentiation, when some of
        the arguments are actually tuples. """
    is_commutative: bool

class hyper(TupleParametersBase):
    """
    The generalized hypergeometric function is defined by a series where
    the ratios of successive terms are a rational function of the summation
    index. When convergent, it is continued analytically to the largest
    possible domain.

    Explanation
    ===========

    The hypergeometric function depends on two vectors of parameters, called
    the numerator parameters $a_p$, and the denominator parameters
    $b_q$. It also has an argument $z$. The series definition is

    .. math ::
        {}_pF_q\\left(\\begin{matrix} a_1, \\cdots, a_p \\\\ b_1, \\cdots, b_q \\end{matrix}
                     \\middle| z \\right)
        = \\sum_{n=0}^\\infty \\frac{(a_1)_n \\cdots (a_p)_n}{(b_1)_n \\cdots (b_q)_n}
                            \\frac{z^n}{n!},

    where $(a)_n = (a)(a+1)\\cdots(a+n-1)$ denotes the rising factorial.

    If one of the $b_q$ is a non-positive integer then the series is
    undefined unless one of the $a_p$ is a larger (i.e., smaller in
    magnitude) non-positive integer. If none of the $b_q$ is a
    non-positive integer and one of the $a_p$ is a non-positive
    integer, then the series reduces to a polynomial. To simplify the
    following discussion, we assume that none of the $a_p$ or
    $b_q$ is a non-positive integer. For more details, see the
    references.

    The series converges for all $z$ if $p \\le q$, and thus
    defines an entire single-valued function in this case. If $p =
    q+1$ the series converges for $|z| < 1$, and can be continued
    analytically into a half-plane. If $p > q+1$ the series is
    divergent for all $z$.

    Please note the hypergeometric function constructor currently does *not*
    check if the parameters actually yield a well-defined function.

    Examples
    ========

    The parameters $a_p$ and $b_q$ can be passed as arbitrary
    iterables, for example:

    >>> from sympy import hyper
    >>> from sympy.abc import x, n, a
    >>> hyper((1, 2, 3), [3, 4], x)
    hyper((1, 2, 3), (3, 4), x)

    There is also pretty printing (it looks better using Unicode):

    >>> from sympy import pprint
    >>> pprint(hyper((1, 2, 3), [3, 4], x), use_unicode=False)
      _
     |_  /1, 2, 3 |  \\\n     |   |        | x|
    3  2 \\  3, 4  |  /

    The parameters must always be iterables, even if they are vectors of
    length one or zero:

    >>> hyper((1, ), [], x)
    hyper((1,), (), x)

    But of course they may be variables (but if they depend on $x$ then you
    should not expect much implemented functionality):

    >>> hyper((n, a), (n**2,), x)
    hyper((n, a), (n**2,), x)

    The hypergeometric function generalizes many named special functions.
    The function ``hyperexpand()`` tries to express a hypergeometric function
    using named special functions. For example:

    >>> from sympy import hyperexpand
    >>> hyperexpand(hyper([], [], x))
    exp(x)

    You can also use ``expand_func()``:

    >>> from sympy import expand_func
    >>> expand_func(x*hyper([1, 1], [2], -x))
    log(x + 1)

    More examples:

    >>> from sympy import S
    >>> hyperexpand(hyper([], [S(1)/2], -x**2/4))
    cos(x)
    >>> hyperexpand(x*hyper([S(1)/2, S(1)/2], [S(3)/2], x**2))
    asin(x)

    We can also sometimes ``hyperexpand()`` parametric functions:

    >>> from sympy.abc import a
    >>> hyperexpand(hyper([-a], [], x))
    (1 - x)**a

    See Also
    ========

    sympy.simplify.hyperexpand
    gamma
    meijerg

    References
    ==========

    .. [1] Luke, Y. L. (1969), The Special Functions and Their Approximations,
           Volume 1
    .. [2] https://en.wikipedia.org/wiki/Generalized_hypergeometric_function

    """
    def __new__(cls, ap, bq, z, **kwargs): ...
    @classmethod
    def eval(cls, ap, bq, z): ...
    def fdiff(self, argindex: int = 3): ...
    @property
    def argument(self):
        """ Argument of the hypergeometric function. """
    @property
    def ap(self):
        """ Numerator parameters of the hypergeometric function. """
    @property
    def bq(self):
        """ Denominator parameters of the hypergeometric function. """
    @property
    def eta(self):
        """ A quantity related to the convergence of the series. """
    @property
    def radius_of_convergence(self):
        """
        Compute the radius of convergence of the defining series.

        Explanation
        ===========

        Note that even if this is not ``oo``, the function may still be
        evaluated outside of the radius of convergence by analytic
        continuation. But if this is zero, then the function is not actually
        defined anywhere else.

        Examples
        ========

        >>> from sympy import hyper
        >>> from sympy.abc import z
        >>> hyper((1, 2), [3], z).radius_of_convergence
        1
        >>> hyper((1, 2, 3), [4], z).radius_of_convergence
        0
        >>> hyper((1, 2), (3, 4), z).radius_of_convergence
        oo

        """
    @property
    def convergence_statement(self):
        """ Return a condition on z under which the series converges. """

class meijerg(TupleParametersBase):
    '''
    The Meijer G-function is defined by a Mellin-Barnes type integral that
    resembles an inverse Mellin transform. It generalizes the hypergeometric
    functions.

    Explanation
    ===========

    The Meijer G-function depends on four sets of parameters. There are
    "*numerator parameters*"
    $a_1, \\ldots, a_n$ and $a_{n+1}, \\ldots, a_p$, and there are
    "*denominator parameters*"
    $b_1, \\ldots, b_m$ and $b_{m+1}, \\ldots, b_q$.
    Confusingly, it is traditionally denoted as follows (note the position
    of $m$, $n$, $p$, $q$, and how they relate to the lengths of the four
    parameter vectors):

    .. math ::
        G_{p,q}^{m,n} \\left(\\begin{matrix}a_1, \\cdots, a_n & a_{n+1}, \\cdots, a_p \\\\\n                                        b_1, \\cdots, b_m & b_{m+1}, \\cdots, b_q
                          \\end{matrix} \\middle| z \\right).

    However, in SymPy the four parameter vectors are always available
    separately (see examples), so that there is no need to keep track of the
    decorating sub- and super-scripts on the G symbol.

    The G function is defined as the following integral:

    .. math ::
         \\frac{1}{2 \\pi i} \\int_L \\frac{\\prod_{j=1}^m \\Gamma(b_j - s)
         \\prod_{j=1}^n \\Gamma(1 - a_j + s)}{\\prod_{j=m+1}^q \\Gamma(1- b_j +s)
         \\prod_{j=n+1}^p \\Gamma(a_j - s)} z^s \\mathrm{d}s,

    where $\\Gamma(z)$ is the gamma function. There are three possible
    contours which we will not describe in detail here (see the references).
    If the integral converges along more than one of them, the definitions
    agree. The contours all separate the poles of $\\Gamma(1-a_j+s)$
    from the poles of $\\Gamma(b_k-s)$, so in particular the G function
    is undefined if $a_j - b_k \\in \\mathbb{Z}_{>0}$ for some
    $j \\le n$ and $k \\le m$.

    The conditions under which one of the contours yields a convergent integral
    are complicated and we do not state them here, see the references.

    Please note currently the Meijer G-function constructor does *not* check any
    convergence conditions.

    Examples
    ========

    You can pass the parameters either as four separate vectors:

    >>> from sympy import meijerg, Tuple, pprint
    >>> from sympy.abc import x, a
    >>> pprint(meijerg((1, 2), (a, 4), (5,), [], x), use_unicode=False)
     __1, 2 /1, 2  a, 4 |  \\\n    /__     |           | x|
    \\_|4, 1 \\ 5         |  /

    Or as two nested vectors:

    >>> pprint(meijerg([(1, 2), (3, 4)], ([5], Tuple()), x), use_unicode=False)
     __1, 2 /1, 2  3, 4 |  \\\n    /__     |           | x|
    \\_|4, 1 \\ 5         |  /

    As with the hypergeometric function, the parameters may be passed as
    arbitrary iterables. Vectors of length zero and one also have to be
    passed as iterables. The parameters need not be constants, but if they
    depend on the argument then not much implemented functionality should be
    expected.

    All the subvectors of parameters are available:

    >>> from sympy import pprint
    >>> g = meijerg([1], [2], [3], [4], x)
    >>> pprint(g, use_unicode=False)
     __1, 1 /1  2 |  \\\n    /__     |     | x|
    \\_|2, 2 \\3  4 |  /
    >>> g.an
    (1,)
    >>> g.ap
    (1, 2)
    >>> g.aother
    (2,)
    >>> g.bm
    (3,)
    >>> g.bq
    (3, 4)
    >>> g.bother
    (4,)

    The Meijer G-function generalizes the hypergeometric functions.
    In some cases it can be expressed in terms of hypergeometric functions,
    using Slater\'s theorem. For example:

    >>> from sympy import hyperexpand
    >>> from sympy.abc import a, b, c
    >>> hyperexpand(meijerg([a], [], [c], [b], x), allow_hyper=True)
    x**c*gamma(-a + c + 1)*hyper((-a + c + 1,),
                                 (-b + c + 1,), -x)/gamma(-b + c + 1)

    Thus the Meijer G-function also subsumes many named functions as special
    cases. You can use ``expand_func()`` or ``hyperexpand()`` to (try to)
    rewrite a Meijer G-function in terms of named special functions. For
    example:

    >>> from sympy import expand_func, S
    >>> expand_func(meijerg([[],[]], [[0],[]], -x))
    exp(x)
    >>> hyperexpand(meijerg([[],[]], [[S(1)/2],[0]], (x/2)**2))
    sin(x)/sqrt(pi)

    See Also
    ========

    hyper
    sympy.simplify.hyperexpand

    References
    ==========

    .. [1] Luke, Y. L. (1969), The Special Functions and Their Approximations,
           Volume 1
    .. [2] https://en.wikipedia.org/wiki/Meijer_G-function

    '''
    def __new__(cls, *args, **kwargs): ...
    def fdiff(self, argindex: int = 3): ...
    def get_period(self):
        """
        Return a number $P$ such that $G(x*exp(I*P)) == G(x)$.

        Examples
        ========

        >>> from sympy import meijerg, pi, S
        >>> from sympy.abc import z

        >>> meijerg([1], [], [], [], z).get_period()
        2*pi
        >>> meijerg([pi], [], [], [], z).get_period()
        oo
        >>> meijerg([1, 2], [], [], [], z).get_period()
        oo
        >>> meijerg([1,1], [2], [1, S(1)/2, S(1)/3], [1], z).get_period()
        12*pi

        """
    def integrand(self, s):
        """ Get the defining integrand D(s). """
    @property
    def argument(self):
        """ Argument of the Meijer G-function. """
    @property
    def an(self):
        """ First set of numerator parameters. """
    @property
    def ap(self):
        """ Combined numerator parameters. """
    @property
    def aother(self):
        """ Second set of numerator parameters. """
    @property
    def bm(self):
        """ First set of denominator parameters. """
    @property
    def bq(self):
        """ Combined denominator parameters. """
    @property
    def bother(self):
        """ Second set of denominator parameters. """
    @property
    def nu(self):
        """ A quantity related to the convergence region of the integral,
            c.f. references. """
    @property
    def delta(self):
        """ A quantity related to the convergence region of the integral,
            c.f. references. """
    @property
    def is_number(self):
        """ Returns true if expression has numeric data only. """

class HyperRep(Function):
    '''
    A base class for "hyper representation functions".

    This is used exclusively in ``hyperexpand()``, but fits more logically here.

    pFq is branched at 1 if p == q+1. For use with slater-expansion, we want
    define an "analytic continuation" to all polar numbers, which is
    continuous on circles and on the ray t*exp_polar(I*pi). Moreover, we want
    a "nice" expression for the various cases.

    This base class contains the core logic, concrete derived classes only
    supply the actual functions.

    '''
    @classmethod
    def eval(cls, *args): ...

class HyperRep_power1(HyperRep):
    """ Return a representative for hyper([-a], [], z) == (1 - z)**a. """
class HyperRep_power2(HyperRep):
    """ Return a representative for hyper([a, a - 1/2], [2*a], z). """
class HyperRep_log1(HyperRep):
    """ Represent -z*hyper([1, 1], [2], z) == log(1 - z). """
class HyperRep_atanh(HyperRep):
    """ Represent hyper([1/2, 1], [3/2], z) == atanh(sqrt(z))/sqrt(z). """
class HyperRep_asin1(HyperRep):
    """ Represent hyper([1/2, 1/2], [3/2], z) == asin(sqrt(z))/sqrt(z). """
class HyperRep_asin2(HyperRep):
    """ Represent hyper([1, 1], [3/2], z) == asin(sqrt(z))/sqrt(z)/sqrt(1-z). """
class HyperRep_sqrts1(HyperRep):
    """ Return a representative for hyper([-a, 1/2 - a], [1/2], z). """
class HyperRep_sqrts2(HyperRep):
    """ Return a representative for
          sqrt(z)/2*[(1-sqrt(z))**2a - (1 + sqrt(z))**2a]
          == -2*z/(2*a+1) d/dz hyper([-a - 1/2, -a], [1/2], z)"""
class HyperRep_log2(HyperRep):
    """ Represent log(1/2 + sqrt(1 - z)/2) == -z/4*hyper([3/2, 1, 1], [2, 2], z) """
class HyperRep_cosasin(HyperRep):
    """ Represent hyper([a, -a], [1/2], z) == cos(2*a*asin(sqrt(z))). """
class HyperRep_sinasin(HyperRep):
    """ Represent 2*a*z*hyper([1 - a, 1 + a], [3/2], z)
        == sqrt(z)/sqrt(1-z)*sin(2*a*asin(sqrt(z))) """

class appellf1(Function):
    """
    This is the Appell hypergeometric function of two variables as:

    .. math ::
        F_1(a,b_1,b_2,c,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
        \\frac{(a)_{m+n} (b_1)_m (b_2)_n}{(c)_{m+n}}
        \\frac{x^m y^n}{m! n!}.

    Examples
    ========

    >>> from sympy import appellf1, symbols
    >>> x, y, a, b1, b2, c = symbols('x y a b1 b2 c')
    >>> appellf1(2., 1., 6., 4., 5., 6.)
    0.0063339426292673
    >>> appellf1(12., 12., 6., 4., 0.5, 0.12)
    172870711.659936
    >>> appellf1(40, 2, 6, 4, 15, 60)
    appellf1(40, 2, 6, 4, 15, 60)
    >>> appellf1(20., 12., 10., 3., 0.5, 0.12)
    15605338197184.4
    >>> appellf1(40, 2, 6, 4, x, y)
    appellf1(40, 2, 6, 4, x, y)
    >>> appellf1(a, b1, b2, c, x, y)
    appellf1(a, b1, b2, c, x, y)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Appell_series
    .. [2] https://functions.wolfram.com/HypergeometricFunctions/AppellF1/

    """
    @classmethod
    def eval(cls, a, b1, b2, c, x, y): ...
    def fdiff(self, argindex: int = 5): ...
