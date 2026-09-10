from _typeshed import Incomplete
from sympy.polys.densearith import dup_l2_norm_squared as dup_l2_norm_squared, dup_neg as dup_neg, dup_rem as dup_rem, dup_rshift as dup_rshift
from sympy.polys.densebasic import dup_LC as dup_LC, dup_TC as dup_TC, dup_convert as dup_convert, dup_degree as dup_degree, dup_reverse as dup_reverse, dup_strip as dup_strip, dup_terms_gcd as dup_terms_gcd
from sympy.polys.densetools import dmp_eval_in as dmp_eval_in, dup_clear_denoms as dup_clear_denoms, dup_diff as dup_diff, dup_eval as dup_eval, dup_mirror as dup_mirror, dup_real_imag as dup_real_imag, dup_scale as dup_scale, dup_shift as dup_shift, dup_sign_variations as dup_sign_variations, dup_transform as dup_transform
from sympy.polys.euclidtools import dup_discriminant as dup_discriminant
from sympy.polys.factortools import dup_factor_list as dup_factor_list
from sympy.polys.polyerrors import DomainError as DomainError, PolynomialError as PolynomialError, RefinementFailed as RefinementFailed
from sympy.polys.sqfreetools import dup_sqf_list as dup_sqf_list, dup_sqf_part as dup_sqf_part

def dup_sturm(f, K):
    '''
    Computes the Sturm sequence of ``f`` in ``F[x]``.

    Given a univariate, square-free polynomial ``f(x)`` returns the
    associated Sturm sequence ``f_0(x), ..., f_n(x)`` defined by::

       f_0(x), f_1(x) = f(x), f\'(x)
       f_n = -rem(f_{n-2}(x), f_{n-1}(x))

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> R.dup_sturm(x**3 - 2*x**2 + x - 3)
    [x**3 - 2*x**2 + x - 3, 3*x**2 - 4*x + 1, 2/9*x + 25/9, -2079/4]

    References
    ==========

    .. [1] [Davenport88]_

    '''
def dup_root_upper_bound(f, K):
    '''Compute the LMQ upper bound for the positive roots of `f`;
       LMQ (Local Max Quadratic) was developed by Akritas-Strzebonski-Vigklas.

    References
    ==========
    .. [1] Alkiviadis G. Akritas: "Linear and Quadratic Complexity Bounds on the
        Values of the Positive Roots of Polynomials"
        Journal of Universal Computer Science, Vol. 15, No. 3, 523-537, 2009.
    '''
def dup_root_lower_bound(f, K):
    '''Compute the LMQ lower bound for the positive roots of `f`;
       LMQ (Local Max Quadratic) was developed by Akritas-Strzebonski-Vigklas.

       References
       ==========
       .. [1] Alkiviadis G. Akritas: "Linear and Quadratic Complexity Bounds on the
              Values of the Positive Roots of Polynomials"
              Journal of Universal Computer Science, Vol. 15, No. 3, 523-537, 2009.
    '''
def dup_cauchy_upper_bound(f, K):
    """
    Compute the Cauchy upper bound on the absolute value of all roots of f,
    real or complex.

    References
    ==========
    .. [1] https://en.wikipedia.org/wiki/Geometrical_properties_of_polynomial_roots#Lagrange's_and_Cauchy's_bounds
    """
def dup_cauchy_lower_bound(f, K):
    """Compute the Cauchy lower bound on the absolute value of all non-zero
       roots of f, real or complex."""
def dup_mignotte_sep_bound_squared(f, K):
    '''
    Return the square of the Mignotte lower bound on separation between
    distinct roots of f. The square is returned so that the bound lies in
    K or its quotient field.

    References
    ==========

    .. [1] Mignotte, Maurice. "Some useful bounds." Computer algebra.
        Springer, Vienna, 1982. 259-263.
        https://people.dm.unipi.it/gianni/AC-EAG/Mignotte.pdf
    '''
def dup_step_refine_real_root(f, M, K, fast: bool = False):
    """One step of positive real root refinement algorithm. """
def dup_inner_refine_real_root(f, M, K, eps: Incomplete | None = None, steps: Incomplete | None = None, disjoint: Incomplete | None = None, fast: bool = False, mobius: bool = False):
    """Refine a positive root of `f` given a Mobius transform or an interval. """
def dup_outer_refine_real_root(f, s, t, K, eps: Incomplete | None = None, steps: Incomplete | None = None, disjoint: Incomplete | None = None, fast: bool = False):
    """Refine a positive root of `f` given an interval `(s, t)`. """
def dup_refine_real_root(f, s, t, K, eps: Incomplete | None = None, steps: Incomplete | None = None, disjoint: Incomplete | None = None, fast: bool = False):
    """Refine real root's approximating interval to the given precision. """
def dup_inner_isolate_real_roots(f, K, eps: Incomplete | None = None, fast: bool = False):
    """Internal function for isolation positive roots up to given precision.

       References
       ==========
           1. Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative Study of Two Real Root
           Isolation Methods . Nonlinear Analysis: Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
           2. Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S. Vigklas: Improving the
           Performance of the Continued Fractions Method Using new Bounds of Positive Roots. Nonlinear
           Analysis: Modelling and Control, Vol. 13, No. 3, 265-279, 2008.
    """
def dup_inner_isolate_positive_roots(f, K, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, fast: bool = False, mobius: bool = False):
    """Iteratively compute disjoint positive root isolation intervals. """
def dup_inner_isolate_negative_roots(f, K, inf: Incomplete | None = None, sup: Incomplete | None = None, eps: Incomplete | None = None, fast: bool = False, mobius: bool = False):
    """Iteratively compute disjoint negative root isolation intervals. """
def dup_isolate_real_roots_sqf(f, K, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, fast: bool = False, blackbox: bool = False):
    """Isolate real roots of a square-free polynomial using the Vincent-Akritas-Strzebonski (VAS) CF approach.

       References
       ==========
       .. [1] Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative
              Study of Two Real Root Isolation Methods. Nonlinear Analysis:
              Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
       .. [2] Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S.
              Vigklas: Improving the Performance of the Continued Fractions
              Method Using New Bounds of Positive Roots. Nonlinear Analysis:
              Modelling and Control, Vol. 13, No. 3, 265-279, 2008.

    """
def dup_isolate_real_roots(f, K, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, basis: bool = False, fast: bool = False):
    """Isolate real roots using Vincent-Akritas-Strzebonski (VAS) continued fractions approach.

       References
       ==========

       .. [1] Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative
              Study of Two Real Root Isolation Methods. Nonlinear Analysis:
              Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
       .. [2] Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S.
              Vigklas: Improving the Performance of the Continued Fractions
              Method Using New Bounds of Positive Roots.
              Nonlinear Analysis: Modelling and Control, Vol. 13, No. 3, 265-279, 2008.

    """
def dup_isolate_real_roots_list(polys, K, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, strict: bool = False, basis: bool = False, fast: bool = False):
    """Isolate real roots of a list of square-free polynomial using Vincent-Akritas-Strzebonski (VAS) CF approach.

       References
       ==========

       .. [1] Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative
              Study of Two Real Root Isolation Methods. Nonlinear Analysis:
              Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
       .. [2] Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S.
              Vigklas: Improving the Performance of the Continued Fractions
              Method Using New Bounds of Positive Roots.
              Nonlinear Analysis: Modelling and Control, Vol. 13, No. 3, 265-279, 2008.

    """
def dup_count_real_roots(f, K, inf: Incomplete | None = None, sup: Incomplete | None = None):
    """Returns the number of distinct real roots of ``f`` in ``[inf, sup]``. """

OO: str
Q1: str
Q2: str
Q3: str
Q4: str
A1: str
A2: str
A3: str
A4: str

def dup_count_complex_roots(f, K, inf: Incomplete | None = None, sup: Incomplete | None = None, exclude: Incomplete | None = None):
    """Count all roots in [u + v*I, s + t*I] rectangle using Collins-Krandick algorithm. """
def dup_isolate_complex_roots_sqf(f, K, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, blackbox: bool = False):
    """Isolate complex roots of a square-free polynomial using Collins-Krandick algorithm. """
def dup_isolate_all_roots_sqf(f, K, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, fast: bool = False, blackbox: bool = False):
    """Isolate real and complex roots of a square-free polynomial ``f``. """
def dup_isolate_all_roots(f, K, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, fast: bool = False):
    """Isolate real and complex roots of a non-square-free polynomial ``f``. """

class RealInterval:
    """A fully qualified representation of a real isolation interval. """
    neg: bool
    mobius: Incomplete
    def __init__(self, data, f, dom) -> None:
        """Initialize new real interval with complete information. """
    @property
    def func(self): ...
    @property
    def args(self): ...
    def __eq__(self, other): ...
    @property
    def a(self):
        """Return the position of the left end. """
    @property
    def b(self):
        """Return the position of the right end. """
    @property
    def dx(self):
        """Return width of the real isolating interval. """
    @property
    def center(self):
        """Return the center of the real isolating interval. """
    @property
    def max_denom(self):
        """Return the largest denominator occurring in either endpoint. """
    def as_tuple(self):
        """Return tuple representation of real isolating interval. """
    def __contains__(self, item) -> bool:
        """
        Say whether a complex number belongs to this real interval.

        Parameters
        ==========

        item : pair (re, im) or number re
            Either a pair giving the real and imaginary parts of the number,
            or else a real number.

        """
    def is_disjoint(self, other):
        """Return ``True`` if two isolation intervals are disjoint. """
    def refine_disjoint(self, other):
        """Refine an isolating interval until it is disjoint with another one. """
    def refine_size(self, dx):
        """Refine an isolating interval until it is of sufficiently small size. """
    def refine_step(self, steps: int = 1):
        """Perform several steps of real root refinement algorithm. """
    def refine(self):
        """Perform one step of real root refinement algorithm. """

class ComplexInterval:
    """A fully qualified representation of a complex isolation interval.
    The printed form is shown as (ax, bx) x (ay, by) where (ax, ay)
    and (bx, by) are the coordinates of the southwest and northeast
    corners of the interval's rectangle, respectively.

    Examples
    ========

    >>> from sympy import CRootOf, S
    >>> from sympy.abc import x
    >>> CRootOf.clear_cache()  # for doctest reproducibility
    >>> root = CRootOf(x**10 - 2*x + 3, 9)
    >>> i = root._get_interval(); i
    (3/64, 3/32) x (9/8, 75/64)

    The real part of the root lies within the range [0, 3/4] while
    the imaginary part lies within the range [9/8, 3/2]:

    >>> root.n(3)
    0.0766 + 1.14*I

    The width of the ranges in the x and y directions on the complex
    plane are:

    >>> i.dx, i.dy
    (3/64, 3/64)

    The center of the range is

    >>> i.center
    (9/128, 147/128)

    The northeast coordinate of the rectangle bounding the root in the
    complex plane is given by attribute b and the x and y components
    are accessed by bx and by:

    >>> i.b, i.bx, i.by
    ((3/32, 75/64), 3/32, 75/64)

    The southwest coordinate is similarly given by i.a

    >>> i.a, i.ax, i.ay
    ((3/64, 9/8), 3/64, 9/8)

    Although the interval prints to show only the real and imaginary
    range of the root, all the information of the underlying root
    is contained as properties of the interval.

    For example, an interval with a nonpositive imaginary range is
    considered to be the conjugate. Since the y values of y are in the
    range [0, 1/4] it is not the conjugate:

    >>> i.conj
    False

    The conjugate's interval is

    >>> ic = i.conjugate(); ic
    (3/64, 3/32) x (-75/64, -9/8)

        NOTE: the values printed still represent the x and y range
        in which the root -- conjugate, in this case -- is located,
        but the underlying a and b values of a root and its conjugate
        are the same:

        >>> assert i.a == ic.a and i.b == ic.b

        What changes are the reported coordinates of the bounding rectangle:

        >>> (i.ax, i.ay), (i.bx, i.by)
        ((3/64, 9/8), (3/32, 75/64))
        >>> (ic.ax, ic.ay), (ic.bx, ic.by)
        ((3/64, -75/64), (3/32, -9/8))

    The interval can be refined once:

    >>> i  # for reference, this is the current interval
    (3/64, 3/32) x (9/8, 75/64)

    >>> i.refine()
    (3/64, 3/32) x (9/8, 147/128)

    Several refinement steps can be taken:

    >>> i.refine_step(2)  # 2 steps
    (9/128, 3/32) x (9/8, 147/128)

    It is also possible to refine to a given tolerance:

    >>> tol = min(i.dx, i.dy)/2
    >>> i.refine_size(tol)
    (9/128, 21/256) x (9/8, 291/256)

    A disjoint interval is one whose bounding rectangle does not
    overlap with another. An interval, necessarily, is not disjoint with
    itself, but any interval is disjoint with a conjugate since the
    conjugate rectangle will always be in the lower half of the complex
    plane and the non-conjugate in the upper half:

    >>> i.is_disjoint(i), i.is_disjoint(i.conjugate())
    (False, True)

    The following interval j is not disjoint from i:

    >>> close = CRootOf(x**10 - 2*x + 300/S(101), 9)
    >>> j = close._get_interval(); j
    (75/1616, 75/808) x (225/202, 1875/1616)
    >>> i.is_disjoint(j)
    False

    The two can be made disjoint, however:

    >>> newi, newj = i.refine_disjoint(j)
    >>> newi
    (39/512, 159/2048) x (2325/2048, 4653/4096)
    >>> newj
    (3975/51712, 2025/25856) x (29325/25856, 117375/103424)

    Even though the real ranges overlap, the imaginary do not, so
    the roots have been resolved as distinct. Intervals are disjoint
    when either the real or imaginary component of the intervals is
    distinct. In the case above, the real components have not been
    resolved (so we do not know, yet, which root has the smaller real
    part) but the imaginary part of ``close`` is larger than ``root``:

    >>> close.n(3)
    0.0771 + 1.13*I
    >>> root.n(3)
    0.0766 + 1.14*I
    """
    dom: Incomplete
    conj: Incomplete
    def __init__(self, a, b, I, Q, F1, F2, f1, f2, dom, conj: bool = False) -> None:
        """Initialize new complex interval with complete information. """
    @property
    def func(self): ...
    @property
    def args(self): ...
    def __eq__(self, other): ...
    @property
    def ax(self):
        """Return ``x`` coordinate of south-western corner. """
    @property
    def ay(self):
        """Return ``y`` coordinate of south-western corner. """
    @property
    def bx(self):
        """Return ``x`` coordinate of north-eastern corner. """
    @property
    def by(self):
        """Return ``y`` coordinate of north-eastern corner. """
    @property
    def dx(self):
        """Return width of the complex isolating interval. """
    @property
    def dy(self):
        """Return height of the complex isolating interval. """
    @property
    def center(self):
        """Return the center of the complex isolating interval. """
    @property
    def max_denom(self):
        """Return the largest denominator occurring in either endpoint. """
    def as_tuple(self):
        """Return tuple representation of the complex isolating
        interval's SW and NE corners, respectively. """
    def conjugate(self):
        """This complex interval really is located in lower half-plane. """
    def __contains__(self, item) -> bool:
        """
        Say whether a complex number belongs to this complex rectangular
        region.

        Parameters
        ==========

        item : pair (re, im) or number re
            Either a pair giving the real and imaginary parts of the number,
            or else a real number.

        """
    def is_disjoint(self, other):
        """Return ``True`` if two isolation intervals are disjoint. """
    def refine_disjoint(self, other):
        """Refine an isolating interval until it is disjoint with another one. """
    def refine_size(self, dx, dy: Incomplete | None = None):
        """Refine an isolating interval until it is of sufficiently small size. """
    def refine_step(self, steps: int = 1):
        """Perform several steps of complex root refinement algorithm. """
    def refine(self):
        """Perform one step of complex root refinement algorithm. """
