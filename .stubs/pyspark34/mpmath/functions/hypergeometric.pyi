from ..libmp.backend import xrange as xrange
from .functions import defun as defun, defun_wrapped as defun_wrapped
from _typeshed import Incomplete

def hypercomb(ctx, function, params=[], discard_known_zeros: bool = True, **kwargs): ...
def hyper(ctx, a_s, b_s, z, **kwargs):
    """
    Hypergeometric function, general case.
    """
def hyp0f1(ctx, b, z, **kwargs): ...
def hyp1f1(ctx, a, b, z, **kwargs): ...
def hyp1f2(ctx, a1, b1, b2, z, **kwargs): ...
def hyp2f1(ctx, a, b, c, z, **kwargs): ...
def hyp2f2(ctx, a1, a2, b1, b2, z, **kwargs): ...
def hyp2f3(ctx, a1, a2, b1, b2, b3, z, **kwargs): ...
def hyp2f0(ctx, a, b, z, **kwargs): ...
def hyp3f2(ctx, a1, a2, a3, b1, b2, z, **kwargs): ...
def meijerg(ctx, a_s, b_s, z, r: int = 1, series: Incomplete | None = None, **kwargs): ...
def appellf1(ctx, a, b1, b2, c, x, y, **kwargs): ...
def appellf2(ctx, a, b1, b2, c1, c2, x, y, **kwargs): ...
def appellf3(ctx, a1, a2, b1, b2, c, x, y, **kwargs): ...
def appellf4(ctx, a, b, c1, c2, x, y, **kwargs): ...
def hyper2d(ctx, a, b, x, y, **kwargs):
    """
    Sums the generalized 2D hypergeometric series

    .. math ::

        \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
            \\frac{P((a),m,n)}{Q((b),m,n)}
            \\frac{x^m y^n} {m! n!}

    where `(a) = (a_1,\\ldots,a_r)`, `(b) = (b_1,\\ldots,b_s)` and where
    `P` and `Q` are products of rising factorials such as `(a_j)_n` or
    `(a_j)_{m+n}`. `P` and `Q` are specified in the form of dicts, with
    the `m` and `n` dependence as keys and parameter lists as values.
    The supported rising factorials are given in the following table
    (note that only a few are supported in `Q`):

    +------------+-------------------+--------+
    | Key        |  Rising factorial | `Q`    |
    +============+===================+========+
    | ``'m'``    |   `(a_j)_m`       | Yes    |
    +------------+-------------------+--------+
    | ``'n'``    |   `(a_j)_n`       | Yes    |
    +------------+-------------------+--------+
    | ``'m+n'``  |   `(a_j)_{m+n}`   | Yes    |
    +------------+-------------------+--------+
    | ``'m-n'``  |   `(a_j)_{m-n}`   | No     |
    +------------+-------------------+--------+
    | ``'n-m'``  |   `(a_j)_{n-m}`   | No     |
    +------------+-------------------+--------+
    | ``'2m+n'`` |   `(a_j)_{2m+n}`  | No     |
    +------------+-------------------+--------+
    | ``'2m-n'`` |   `(a_j)_{2m-n}`  | No     |
    +------------+-------------------+--------+
    | ``'2n-m'`` |   `(a_j)_{2n-m}`  | No     |
    +------------+-------------------+--------+

    For example, the Appell F1 and F4 functions

    .. math ::

        F_1 = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
              \\frac{(a)_{m+n} (b)_m (c)_n}{(d)_{m+n}}
              \\frac{x^m y^n}{m! n!}

        F_4 = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
              \\frac{(a)_{m+n} (b)_{m+n}}{(c)_m (d)_{n}}
              \\frac{x^m y^n}{m! n!}

    can be represented respectively as

        ``hyper2d({'m+n':[a], 'm':[b], 'n':[c]}, {'m+n':[d]}, x, y)``

        ``hyper2d({'m+n':[a,b]}, {'m':[c], 'n':[d]}, x, y)``

    More generally, :func:`~mpmath.hyper2d` can evaluate any of the 34 distinct
    convergent second-order (generalized Gaussian) hypergeometric
    series enumerated by Horn, as well as the Kampe de Feriet
    function.

    The series is computed by rewriting it so that the inner
    series (i.e. the series containing `n` and `y`) has the form of an
    ordinary generalized hypergeometric series and thereby can be
    evaluated efficiently using :func:`~mpmath.hyper`. If possible,
    manually swapping `x` and `y` and the corresponding parameters
    can sometimes give better results.

    **Examples**

    Two separable cases: a product of two geometric series, and a
    product of two Gaussian hypergeometric functions::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> x, y = mpf(0.25), mpf(0.5)
        >>> hyper2d({'m':1,'n':1}, {}, x,y)
        2.666666666666666666666667
        >>> 1/(1-x)/(1-y)
        2.666666666666666666666667
        >>> hyper2d({'m':[1,2],'n':[3,4]}, {'m':[5],'n':[6]}, x,y)
        4.164358531238938319669856
        >>> hyp2f1(1,2,5,x)*hyp2f1(3,4,6,y)
        4.164358531238938319669856

    Some more series that can be done in closed form::

        >>> hyper2d({'m':1,'n':1},{'m+n':1},x,y)
        2.013417124712514809623881
        >>> (exp(x)*x-exp(y)*y)/(x-y)
        2.013417124712514809623881

    Six of the 34 Horn functions, G1-G3 and H1-H3::

        >>> from mpmath import *
        >>> mp.dps = 10; mp.pretty = True
        >>> x, y = 0.0625, 0.125
        >>> a1,a2,b1,b2,c1,c2,d = 1.1,-1.2,-1.3,-1.4,1.5,-1.6,1.7
        >>> hyper2d({'m+n':a1,'n-m':b1,'m-n':b2},{},x,y)  # G1
        1.139090746
        >>> nsum(lambda m,n: rf(a1,m+n)*rf(b1,n-m)*rf(b2,m-n)*\\\n        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        1.139090746
        >>> hyper2d({'m':a1,'n':a2,'n-m':b1,'m-n':b2},{},x,y)  # G2
        0.9503682696
        >>> nsum(lambda m,n: rf(a1,m)*rf(a2,n)*rf(b1,n-m)*rf(b2,m-n)*\\\n        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        0.9503682696
        >>> hyper2d({'2n-m':a1,'2m-n':a2},{},x,y)  # G3
        1.029372029
        >>> nsum(lambda m,n: rf(a1,2*n-m)*rf(a2,2*m-n)*\\\n        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        1.029372029
        >>> hyper2d({'m-n':a1,'m+n':b1,'n':c1},{'m':d},x,y)  # H1
        -1.605331256
        >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m+n)*rf(c1,n)/rf(d,m)*\\\n        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        -1.605331256
        >>> hyper2d({'m-n':a1,'m':b1,'n':[c1,c2]},{'m':d},x,y)  # H2
        -2.35405404
        >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m)*rf(c1,n)*rf(c2,n)/rf(d,m)*\\\n        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        -2.35405404
        >>> hyper2d({'2m+n':a1,'n':b1},{'m+n':c1},x,y)  # H3
        0.974479074
        >>> nsum(lambda m,n: rf(a1,2*m+n)*rf(b1,n)/rf(c1,m+n)*\\\n        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        0.974479074

    **References**

    1. [SrivastavaKarlsson]_
    2. [Weisstein]_ http://mathworld.wolfram.com/HornFunction.html
    3. [Weisstein]_ http://mathworld.wolfram.com/AppellHypergeometricFunction.html

    """
def bihyper(ctx, a_s, b_s, z, **kwargs):
    '''
    Evaluates the bilateral hypergeometric series

    .. math ::

        \\,_AH_B(a_1, \\ldots, a_k; b_1, \\ldots, b_B; z) =
            \\sum_{n=-\\infty}^{\\infty}
            \\frac{(a_1)_n \\ldots (a_A)_n}
                 {(b_1)_n \\ldots (b_B)_n} \\, z^n

    where, for direct convergence, `A = B` and `|z| = 1`, although a
    regularized sum exists more generally by considering the
    bilateral series as a sum of two ordinary hypergeometric
    functions. In order for the series to make sense, none of the
    parameters may be integers.

    **Examples**

    The value of `\\,_2H_2` at `z = 1` is given by Dougall\'s formula::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a,b,c,d = 0.5, 1.5, 2.25, 3.25
        >>> bihyper([a,b],[c,d],1)
        -14.49118026212345786148847
        >>> gammaprod([c,d,1-a,1-b,c+d-a-b-1],[c-a,d-a,c-b,d-b])
        -14.49118026212345786148847

    The regularized function `\\,_1H_0` can be expressed as the
    sum of one `\\,_2F_0` function and one `\\,_1F_1` function::

        >>> a = mpf(0.25)
        >>> z = mpf(0.75)
        >>> bihyper([a], [], z)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)
        >>> hyper([a,1],[],z) + (hyper([1],[1-a],-1/z)-1)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)
        >>> hyper([a,1],[],z) + hyper([1],[2-a],-1/z)/z/(a-1)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)

    **References**

    1. [Slater]_ (chapter 6: "Bilateral Series", pp. 180-189)
    2. [Wikipedia]_ http://en.wikipedia.org/wiki/Bilateral_hypergeometric_series

    '''
