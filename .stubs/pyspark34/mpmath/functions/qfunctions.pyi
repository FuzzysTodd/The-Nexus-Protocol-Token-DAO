from .functions import defun as defun, defun_wrapped as defun_wrapped
from _typeshed import Incomplete

def qp(ctx, a, q: Incomplete | None = None, n: Incomplete | None = None, **kwargs):
    """
    Evaluates the q-Pochhammer symbol (or q-rising factorial)

    .. math ::

        (a; q)_n = \\prod_{k=0}^{n-1} (1-a q^k)

    where `n = \\infty` is permitted if `|q| < 1`. Called with two arguments,
    ``qp(a,q)`` computes `(a;q)_{\\infty}`; with a single argument, ``qp(q)``
    computes `(q;q)_{\\infty}`. The special case

    .. math ::

        \\phi(q) = (q; q)_{\\infty} = \\prod_{k=1}^{\\infty} (1-q^k) =
            \\sum_{k=-\\infty}^{\\infty} (-1)^k q^{(3k^2-k)/2}

    is also known as the Euler function, or (up to a factor `q^{-1/24}`)
    the Dedekind eta function.

    **Examples**

    If `n` is a positive integer, the function amounts to a finite product::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qp(2,3,5)
        -725305.0
        >>> fprod(1-2*3**k for k in range(5))
        -725305.0
        >>> qp(2,3,0)
        1.0

    Complex arguments are allowed::

        >>> qp(2-1j, 0.75j)
        (0.4628842231660149089976379 + 4.481821753552703090628793j)

    The regular Pochhammer symbol `(a)_n` is obtained in the
    following limit as `q \\to 1`::

        >>> a, n = 4, 7
        >>> limit(lambda q: qp(q**a,q,n) / (1-q)**n, 1)
        604800.0
        >>> rf(a,n)
        604800.0

    The Taylor series of the reciprocal Euler function gives
    the partition function `P(n)`, i.e. the number of ways of writing
    `n` as a sum of positive integers::

        >>> taylor(lambda q: 1/qp(q), 0, 10)
        [1.0, 1.0, 2.0, 3.0, 5.0, 7.0, 11.0, 15.0, 22.0, 30.0, 42.0]

    Special values include::

        >>> qp(0)
        1.0
        >>> findroot(diffun(qp), -0.4)   # location of maximum
        -0.4112484791779547734440257
        >>> qp(_)
        1.228348867038575112586878

    The q-Pochhammer symbol is related to the Jacobi theta functions.
    For example, the following identity holds::

        >>> q = mpf(0.5)    # arbitrary
        >>> qp(q)
        0.2887880950866024212788997
        >>> root(3,-2)*root(q,-24)*jtheta(2,pi/6,root(q,6))
        0.2887880950866024212788997

    """
def qgamma(ctx, z, q, **kwargs):
    """
    Evaluates the q-gamma function

    .. math ::

        \\Gamma_q(z) = \\frac{(q; q)_{\\infty}}{(q^z; q)_{\\infty}} (1-q)^{1-z}.


    **Examples**

    Evaluation for real and complex arguments::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qgamma(4,0.75)
        4.046875
        >>> qgamma(6,6)
        121226245.0
        >>> qgamma(3+4j, 0.5j)
        (0.1663082382255199834630088 + 0.01952474576025952984418217j)

    The q-gamma function satisfies a functional equation similar
    to that of the ordinary gamma function::

        >>> q = mpf(0.25)
        >>> z = mpf(2.5)
        >>> qgamma(z+1,q)
        1.428277424823760954685912
        >>> (1-q**z)/(1-q)*qgamma(z,q)
        1.428277424823760954685912

    """
def qfac(ctx, z, q, **kwargs):
    """
    Evaluates the q-factorial,

    .. math ::

        [n]_q! = (1+q)(1+q+q^2)\\cdots(1+q+\\cdots+q^{n-1})

    or more generally

    .. math ::

        [z]_q! = \\frac{(q;q)_z}{(1-q)^z}.

    **Examples**

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qfac(0,0)
        1.0
        >>> qfac(4,3)
        2080.0
        >>> qfac(5,6)
        121226245.0
        >>> qfac(1+1j, 2+1j)
        (0.4370556551322672478613695 + 0.2609739839216039203708921j)

    """
def qhyper(ctx, a_s, b_s, q, z, **kwargs):
    """
    Evaluates the basic hypergeometric series or hypergeometric q-series

    .. math ::

        \\,_r\\phi_s \\left[\\begin{matrix}
            a_1 & a_2 & \\ldots & a_r \\\\\n            b_1 & b_2 & \\ldots & b_s
        \\end{matrix} ; q,z \\right] =
        \\sum_{n=0}^\\infty
        \\frac{(a_1;q)_n, \\ldots, (a_r;q)_n}
             {(b_1;q)_n, \\ldots, (b_s;q)_n}
        \\left((-1)^n q^{n\\choose 2}\\right)^{1+s-r}
        \\frac{z^n}{(q;q)_n}

    where `(a;q)_n` denotes the q-Pochhammer symbol (see :func:`~mpmath.qp`).

    **Examples**

    Evaluation works for real and complex arguments::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qhyper([0.5], [2.25], 0.25, 4)
        -0.1975849091263356009534385
        >>> qhyper([0.5], [2.25], 0.25-0.25j, 4)
        (2.806330244925716649839237 + 3.568997623337943121769938j)
        >>> qhyper([1+j], [2,3+0.5j], 0.25, 3+4j)
        (9.112885171773400017270226 - 1.272756997166375050700388j)

    Comparing with a summation of the defining series, using
    :func:`~mpmath.nsum`::

        >>> b, q, z = 3, 0.25, 0.5
        >>> qhyper([], [b], q, z)
        0.6221136748254495583228324
        >>> nsum(lambda n: z**n / qp(q,q,n)/qp(b,q,n) * q**(n*(n-1)), [0,inf])
        0.6221136748254495583228324

    """
