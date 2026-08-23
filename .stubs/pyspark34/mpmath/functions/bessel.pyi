from .functions import defun as defun, defun_wrapped as defun_wrapped

def j0(ctx, x):
    """Computes the Bessel function `J_0(x)`. See :func:`~mpmath.besselj`."""
def j1(ctx, x):
    """Computes the Bessel function `J_1(x)`.  See :func:`~mpmath.besselj`."""
def besselj(ctx, n, z, derivative: int = 0, **kwargs): ...
def besseli(ctx, n, z, derivative: int = 0, **kwargs): ...
def bessely(ctx, n, z, derivative: int = 0, **kwargs): ...
def besselk(ctx, n, z, **kwargs): ...
def hankel1(ctx, n, x, **kwargs): ...
def hankel2(ctx, n, x, **kwargs): ...
def whitm(ctx, k, m, z, **kwargs): ...
def whitw(ctx, k, m, z, **kwargs): ...
def hyperu(ctx, a, b, z, **kwargs): ...
def struveh(ctx, n, z, **kwargs): ...
def struvel(ctx, n, z, **kwargs): ...
def angerj(ctx, v, z, **kwargs): ...
def webere(ctx, v, z, **kwargs): ...
def lommels1(ctx, u, v, z, **kwargs): ...
def lommels2(ctx, u, v, z, **kwargs): ...
def ber(ctx, n, z, **kwargs): ...
def bei(ctx, n, z, **kwargs): ...
def ker(ctx, n, z, **kwargs): ...
def kei(ctx, n, z, **kwargs): ...
def c_memo(f): ...
def airyai(ctx, z, derivative: int = 0, **kwargs): ...
def airybi(ctx, z, derivative: int = 0, **kwargs): ...
def airyaizero(ctx, k, derivative: int = 0): ...
def airybizero(ctx, k, derivative: int = 0, complex: bool = False): ...
def scorergi(ctx, z, **kwargs): ...
def scorerhi(ctx, z, **kwargs): ...
def coulombc(ctx, l, eta, _cache={}): ...
def coulombf(ctx, l, eta, z, w: int = 1, chop: bool = True, **kwargs): ...
def coulombg(ctx, l, eta, z, w: int = 1, chop: bool = True, **kwargs): ...
def mcmahon(ctx, kind, prime, v, m):
    """
    Computes an estimate for the location of the Bessel function zero
    j_{v,m}, y_{v,m}, j'_{v,m} or y'_{v,m} using McMahon's asymptotic
    expansion (Abramowitz & Stegun 9.5.12-13, DLMF 20.21(vi)).

    Returns (r,err) where r is the estimated location of the root
    and err is a positive number estimating the error of the
    asymptotic expansion.
    """
def generalized_bisection(ctx, f, a, b, n):
    """
    Given f known to have exactly n simple roots within [a,b],
    return a list of n intervals isolating the roots
    and having opposite signs at the endpoints.

    TODO: this can be optimized, e.g. by reusing evaluation points.
    """
def find_in_interval(ctx, f, ab): ...
def bessel_zero(ctx, kind, prime, v, m, isoltol: float = 0.01, _interval_cache={}): ...
def besseljzero(ctx, v, m, derivative: int = 0):
    """
    For a real order `\\nu \\ge 0` and a positive integer `m`, returns
    `j_{\\nu,m}`, the `m`-th positive zero of the Bessel function of the
    first kind `J_{\\nu}(z)` (see :func:`~mpmath.besselj`). Alternatively,
    with *derivative=1*, gives the first nonnegative simple zero
    `j'_{\\nu,m}` of `J'_{\\nu}(z)`.

    The indexing convention is that used by Abramowitz & Stegun
    and the DLMF. Note the special case `j'_{0,1} = 0`, while all other
    zeros are positive. In effect, only simple zeros are counted
    (all zeros of Bessel functions are simple except possibly `z = 0`)
    and `j_{\\nu,m}` becomes a monotonic function of both `\\nu`
    and `m`.

    The zeros are interlaced according to the inequalities

    .. math ::

        j'_{\\nu,k} < j_{\\nu,k} < j'_{\\nu,k+1}

        j_{\\nu,1} < j_{\\nu+1,2} < j_{\\nu,2} < j_{\\nu+1,2} < j_{\\nu,3} < \\cdots

    **Examples**

    Initial zeros of the Bessel functions `J_0(z), J_1(z), J_2(z)`::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> besseljzero(0,1); besseljzero(0,2); besseljzero(0,3)
        2.404825557695772768621632
        5.520078110286310649596604
        8.653727912911012216954199
        >>> besseljzero(1,1); besseljzero(1,2); besseljzero(1,3)
        3.831705970207512315614436
        7.01558666981561875353705
        10.17346813506272207718571
        >>> besseljzero(2,1); besseljzero(2,2); besseljzero(2,3)
        5.135622301840682556301402
        8.417244140399864857783614
        11.61984117214905942709415

    Initial zeros of `J'_0(z), J'_1(z), J'_2(z)`::

        0.0
        3.831705970207512315614436
        7.01558666981561875353705
        >>> besseljzero(1,1,1); besseljzero(1,2,1); besseljzero(1,3,1)
        1.84118378134065930264363
        5.331442773525032636884016
        8.536316366346285834358961
        >>> besseljzero(2,1,1); besseljzero(2,2,1); besseljzero(2,3,1)
        3.054236928227140322755932
        6.706133194158459146634394
        9.969467823087595793179143

    Zeros with large index::

        >>> besseljzero(0,100); besseljzero(0,1000); besseljzero(0,10000)
        313.3742660775278447196902
        3140.807295225078628895545
        31415.14114171350798533666
        >>> besseljzero(5,100); besseljzero(5,1000); besseljzero(5,10000)
        321.1893195676003157339222
        3148.657306813047523500494
        31422.9947255486291798943
        >>> besseljzero(0,100,1); besseljzero(0,1000,1); besseljzero(0,10000,1)
        311.8018681873704508125112
        3139.236339643802482833973
        31413.57032947022399485808

    Zeros of functions with large order::

        >>> besseljzero(50,1)
        57.11689916011917411936228
        >>> besseljzero(50,2)
        62.80769876483536093435393
        >>> besseljzero(50,100)
        388.6936600656058834640981
        >>> besseljzero(50,1,1)
        52.99764038731665010944037
        >>> besseljzero(50,2,1)
        60.02631933279942589882363
        >>> besseljzero(50,100,1)
        387.1083151608726181086283

    Zeros of functions with fractional order::

        >>> besseljzero(0.5,1); besseljzero(1.5,1); besseljzero(2.25,4)
        3.141592653589793238462643
        4.493409457909064175307881
        15.15657692957458622921634

    Both `J_{\\nu}(z)` and `J'_{\\nu}(z)` can be expressed as infinite
    products over their zeros::

        >>> v,z = 2, mpf(1)
        >>> (z/2)**v/gamma(v+1) * \\\n        ...     nprod(lambda k: 1-(z/besseljzero(v,k))**2, [1,inf])
        ...
        0.1149034849319004804696469
        >>> besselj(v,z)
        0.1149034849319004804696469
        >>> (z/2)**(v-1)/2/gamma(v) * \\\n        ...     nprod(lambda k: 1-(z/besseljzero(v,k,1))**2, [1,inf])
        ...
        0.2102436158811325550203884
        >>> besselj(v,z,1)
        0.2102436158811325550203884

    """
def besselyzero(ctx, v, m, derivative: int = 0):
    """
    For a real order `\\nu \\ge 0` and a positive integer `m`, returns
    `y_{\\nu,m}`, the `m`-th positive zero of the Bessel function of the
    second kind `Y_{\\nu}(z)` (see :func:`~mpmath.bessely`). Alternatively,
    with *derivative=1*, gives the first positive zero `y'_{\\nu,m}` of
    `Y'_{\\nu}(z)`.

    The zeros are interlaced according to the inequalities

    .. math ::

        y_{\\nu,k} < y'_{\\nu,k} < y_{\\nu,k+1}

        y_{\\nu,1} < y_{\\nu+1,2} < y_{\\nu,2} < y_{\\nu+1,2} < y_{\\nu,3} < \\cdots

    **Examples**

    Initial zeros of the Bessel functions `Y_0(z), Y_1(z), Y_2(z)`::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> besselyzero(0,1); besselyzero(0,2); besselyzero(0,3)
        0.8935769662791675215848871
        3.957678419314857868375677
        7.086051060301772697623625
        >>> besselyzero(1,1); besselyzero(1,2); besselyzero(1,3)
        2.197141326031017035149034
        5.429681040794135132772005
        8.596005868331168926429606
        >>> besselyzero(2,1); besselyzero(2,2); besselyzero(2,3)
        3.384241767149593472701426
        6.793807513268267538291167
        10.02347797936003797850539

    Initial zeros of `Y'_0(z), Y'_1(z), Y'_2(z)`::

        >>> besselyzero(0,1,1); besselyzero(0,2,1); besselyzero(0,3,1)
        2.197141326031017035149034
        5.429681040794135132772005
        8.596005868331168926429606
        >>> besselyzero(1,1,1); besselyzero(1,2,1); besselyzero(1,3,1)
        3.683022856585177699898967
        6.941499953654175655751944
        10.12340465543661307978775
        >>> besselyzero(2,1,1); besselyzero(2,2,1); besselyzero(2,3,1)
        5.002582931446063945200176
        8.350724701413079526349714
        11.57419546521764654624265

    Zeros with large index::

        >>> besselyzero(0,100); besselyzero(0,1000); besselyzero(0,10000)
        311.8034717601871549333419
        3139.236498918198006794026
        31413.57034538691205229188
        >>> besselyzero(5,100); besselyzero(5,1000); besselyzero(5,10000)
        319.6183338562782156235062
        3147.086508524556404473186
        31421.42392920214673402828
        >>> besselyzero(0,100,1); besselyzero(0,1000,1); besselyzero(0,10000,1)
        313.3726705426359345050449
        3140.807136030340213610065
        31415.14112579761578220175

    Zeros of functions with large order::

        >>> besselyzero(50,1)
        53.50285882040036394680237
        >>> besselyzero(50,2)
        60.11244442774058114686022
        >>> besselyzero(50,100)
        387.1096509824943957706835
        >>> besselyzero(50,1,1)
        56.96290427516751320063605
        >>> besselyzero(50,2,1)
        62.74888166945933944036623
        >>> besselyzero(50,100,1)
        388.6923300548309258355475

    Zeros of functions with fractional order::

        >>> besselyzero(0.5,1); besselyzero(1.5,1); besselyzero(2.25,4)
        1.570796326794896619231322
        2.798386045783887136720249
        13.56721208770735123376018

    """
