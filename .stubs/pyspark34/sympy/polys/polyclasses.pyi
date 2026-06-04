from _typeshed import Incomplete
from sympy.core.numbers import oo as oo
from sympy.core.sympify import CantSympify as CantSympify
from sympy.polys.densearith import dmp_abs as dmp_abs, dmp_add as dmp_add, dmp_add_ground as dmp_add_ground, dmp_add_mul as dmp_add_mul, dmp_div as dmp_div, dmp_exquo as dmp_exquo, dmp_exquo_ground as dmp_exquo_ground, dmp_l1_norm as dmp_l1_norm, dmp_l2_norm_squared as dmp_l2_norm_squared, dmp_max_norm as dmp_max_norm, dmp_mul as dmp_mul, dmp_mul_ground as dmp_mul_ground, dmp_neg as dmp_neg, dmp_pdiv as dmp_pdiv, dmp_pexquo as dmp_pexquo, dmp_pow as dmp_pow, dmp_pquo as dmp_pquo, dmp_prem as dmp_prem, dmp_quo as dmp_quo, dmp_quo_ground as dmp_quo_ground, dmp_rem as dmp_rem, dmp_sqr as dmp_sqr, dmp_sub as dmp_sub, dmp_sub_ground as dmp_sub_ground, dmp_sub_mul as dmp_sub_mul, dup_add as dup_add, dup_mul as dup_mul, dup_neg as dup_neg, dup_pow as dup_pow, dup_rem as dup_rem, dup_sub as dup_sub
from sympy.polys.densebasic import dmp_convert as dmp_convert, dmp_deflate as dmp_deflate, dmp_degree_in as dmp_degree_in, dmp_degree_list as dmp_degree_list, dmp_eject as dmp_eject, dmp_exclude as dmp_exclude, dmp_from_dict as dmp_from_dict, dmp_from_sympy as dmp_from_sympy, dmp_ground as dmp_ground, dmp_ground_LC as dmp_ground_LC, dmp_ground_TC as dmp_ground_TC, dmp_ground_nth as dmp_ground_nth, dmp_ground_p as dmp_ground_p, dmp_inject as dmp_inject, dmp_list_terms as dmp_list_terms, dmp_negative_p as dmp_negative_p, dmp_normal as dmp_normal, dmp_one as dmp_one, dmp_one_p as dmp_one_p, dmp_permute as dmp_permute, dmp_slice_in as dmp_slice_in, dmp_terms_gcd as dmp_terms_gcd, dmp_to_dict as dmp_to_dict, dmp_to_tuple as dmp_to_tuple, dmp_validate as dmp_validate, dmp_zero_p as dmp_zero_p, dup_LC as dup_LC, dup_TC as dup_TC, dup_convert as dup_convert, dup_degree as dup_degree, dup_from_dict as dup_from_dict, dup_normal as dup_normal, dup_strip as dup_strip
from sympy.polys.densetools import dmp_clear_denoms as dmp_clear_denoms, dmp_compose as dmp_compose, dmp_diff_in as dmp_diff_in, dmp_eval_in as dmp_eval_in, dmp_ground_content as dmp_ground_content, dmp_ground_monic as dmp_ground_monic, dmp_ground_primitive as dmp_ground_primitive, dmp_ground_trunc as dmp_ground_trunc, dmp_integrate_in as dmp_integrate_in, dmp_lift as dmp_lift, dup_decompose as dup_decompose, dup_revert as dup_revert, dup_shift as dup_shift, dup_transform as dup_transform
from sympy.polys.euclidtools import dmp_cancel as dmp_cancel, dmp_discriminant as dmp_discriminant, dmp_gcd as dmp_gcd, dmp_inner_gcd as dmp_inner_gcd, dmp_lcm as dmp_lcm, dmp_resultant as dmp_resultant, dmp_subresultants as dmp_subresultants, dup_gcdex as dup_gcdex, dup_half_gcdex as dup_half_gcdex, dup_invert as dup_invert
from sympy.polys.factortools import dmp_factor_list as dmp_factor_list, dmp_factor_list_include as dmp_factor_list_include, dmp_irreducible_p as dmp_irreducible_p, dup_cyclotomic_p as dup_cyclotomic_p
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, NotInvertible as NotInvertible, NotReversible as NotReversible, PolynomialError as PolynomialError, UnificationFailed as UnificationFailed
from sympy.polys.polyutils import PicklableWithSlots as PicklableWithSlots
from sympy.polys.rootisolation import dup_cauchy_lower_bound as dup_cauchy_lower_bound, dup_cauchy_upper_bound as dup_cauchy_upper_bound, dup_count_complex_roots as dup_count_complex_roots, dup_count_real_roots as dup_count_real_roots, dup_isolate_all_roots as dup_isolate_all_roots, dup_isolate_all_roots_sqf as dup_isolate_all_roots_sqf, dup_isolate_real_roots as dup_isolate_real_roots, dup_isolate_real_roots_sqf as dup_isolate_real_roots_sqf, dup_mignotte_sep_bound_squared as dup_mignotte_sep_bound_squared, dup_refine_real_root as dup_refine_real_root, dup_sturm as dup_sturm
from sympy.polys.sqfreetools import dmp_norm as dmp_norm, dmp_sqf_list as dmp_sqf_list, dmp_sqf_list_include as dmp_sqf_list_include, dmp_sqf_norm as dmp_sqf_norm, dmp_sqf_p as dmp_sqf_p, dmp_sqf_part as dmp_sqf_part, dup_gff_list as dup_gff_list

class GenericPoly(PicklableWithSlots):
    """Base class for low-level polynomial representations. """
    def ground_to_ring(f):
        """Make the ground domain a ring. """
    def ground_to_field(f):
        """Make the ground domain a field. """
    def ground_to_exact(f):
        """Make the ground domain exact. """

def init_normal_DMP(rep, lev, dom): ...

class DMP(PicklableWithSlots, CantSympify):
    """Dense Multivariate Polynomials over `K`. """
    rep: Incomplete
    lev: Incomplete
    dom: Incomplete
    ring: Incomplete
    def __init__(self, rep, dom, lev: Incomplete | None = None, ring: Incomplete | None = None) -> None: ...
    def __hash__(f): ...
    def unify(f, g):
        """Unify representations of two multivariate polynomials. """
    def per(f, rep, dom: Incomplete | None = None, kill: bool = False, ring: Incomplete | None = None):
        """Create a DMP out of the given representation. """
    @classmethod
    def zero(cls, lev, dom, ring: Incomplete | None = None): ...
    @classmethod
    def one(cls, lev, dom, ring: Incomplete | None = None): ...
    @classmethod
    def from_list(cls, rep, lev, dom):
        """Create an instance of ``cls`` given a list of native coefficients. """
    @classmethod
    def from_sympy_list(cls, rep, lev, dom):
        """Create an instance of ``cls`` given a list of SymPy coefficients. """
    def to_dict(f, zero: bool = False):
        """Convert ``f`` to a dict representation with native coefficients. """
    def to_sympy_dict(f, zero: bool = False):
        """Convert ``f`` to a dict representation with SymPy coefficients. """
    def to_list(f):
        """Convert ``f`` to a list representation with native coefficients. """
    def to_sympy_list(f):
        """Convert ``f`` to a list representation with SymPy coefficients. """
    def to_tuple(f):
        """
        Convert ``f`` to a tuple representation with native coefficients.

        This is needed for hashing.
        """
    @classmethod
    def from_dict(cls, rep, lev, dom):
        """Construct and instance of ``cls`` from a ``dict`` representation. """
    @classmethod
    def from_monoms_coeffs(cls, monoms, coeffs, lev, dom, ring: Incomplete | None = None): ...
    def to_ring(f):
        """Make the ground domain a ring. """
    def to_field(f):
        """Make the ground domain a field. """
    def to_exact(f):
        """Make the ground domain exact. """
    def convert(f, dom):
        """Convert the ground domain of ``f``. """
    def slice(f, m, n, j: int = 0):
        """Take a continuous subsequence of terms of ``f``. """
    def coeffs(f, order: Incomplete | None = None):
        """Returns all non-zero coefficients from ``f`` in lex order. """
    def monoms(f, order: Incomplete | None = None):
        """Returns all non-zero monomials from ``f`` in lex order. """
    def terms(f, order: Incomplete | None = None):
        """Returns all non-zero terms from ``f`` in lex order. """
    def all_coeffs(f):
        """Returns all coefficients from ``f``. """
    def all_monoms(f):
        """Returns all monomials from ``f``. """
    def all_terms(f):
        """Returns all terms from a ``f``. """
    def lift(f):
        """Convert algebraic coefficients to rationals. """
    def deflate(f):
        """Reduce degree of `f` by mapping `x_i^m` to `y_i`. """
    def inject(f, front: bool = False):
        """Inject ground domain generators into ``f``. """
    def eject(f, dom, front: bool = False):
        """Eject selected generators into the ground domain. """
    def exclude(f):
        """
        Remove useless generators from ``f``.

        Returns the removed generators and the new excluded ``f``.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMP
        >>> from sympy.polys.domains import ZZ

        >>> DMP([[[ZZ(1)]], [[ZZ(1)], [ZZ(2)]]], ZZ).exclude()
        ([2], DMP([[1], [1, 2]], ZZ, None))

        """
    def permute(f, P):
        """
        Returns a polynomial in `K[x_{P(1)}, ..., x_{P(n)}]`.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMP
        >>> from sympy.polys.domains import ZZ

        >>> DMP([[[ZZ(2)], [ZZ(1), ZZ(0)]], [[]]], ZZ).permute([1, 0, 2])
        DMP([[[2], []], [[1, 0], []]], ZZ, None)

        >>> DMP([[[ZZ(2)], [ZZ(1), ZZ(0)]], [[]]], ZZ).permute([1, 2, 0])
        DMP([[[1], []], [[2, 0], []]], ZZ, None)

        """
    def terms_gcd(f):
        """Remove GCD of terms from the polynomial ``f``. """
    def add_ground(f, c):
        """Add an element of the ground domain to ``f``. """
    def sub_ground(f, c):
        """Subtract an element of the ground domain from ``f``. """
    def mul_ground(f, c):
        """Multiply ``f`` by a an element of the ground domain. """
    def quo_ground(f, c):
        """Quotient of ``f`` by a an element of the ground domain. """
    def exquo_ground(f, c):
        """Exact quotient of ``f`` by a an element of the ground domain. """
    def abs(f):
        """Make all coefficients in ``f`` positive. """
    def neg(f):
        """Negate all coefficients in ``f``. """
    def add(f, g):
        """Add two multivariate polynomials ``f`` and ``g``. """
    def sub(f, g):
        """Subtract two multivariate polynomials ``f`` and ``g``. """
    def mul(f, g):
        """Multiply two multivariate polynomials ``f`` and ``g``. """
    def sqr(f):
        """Square a multivariate polynomial ``f``. """
    def pow(f, n):
        """Raise ``f`` to a non-negative power ``n``. """
    def pdiv(f, g):
        """Polynomial pseudo-division of ``f`` and ``g``. """
    def prem(f, g):
        """Polynomial pseudo-remainder of ``f`` and ``g``. """
    def pquo(f, g):
        """Polynomial pseudo-quotient of ``f`` and ``g``. """
    def pexquo(f, g):
        """Polynomial exact pseudo-quotient of ``f`` and ``g``. """
    def div(f, g):
        """Polynomial division with remainder of ``f`` and ``g``. """
    def rem(f, g):
        """Computes polynomial remainder of ``f`` and ``g``. """
    def quo(f, g):
        """Computes polynomial quotient of ``f`` and ``g``. """
    def exquo(f, g):
        """Computes polynomial exact quotient of ``f`` and ``g``. """
    def degree(f, j: int = 0):
        """Returns the leading degree of ``f`` in ``x_j``. """
    def degree_list(f):
        """Returns a list of degrees of ``f``. """
    def total_degree(f):
        """Returns the total degree of ``f``. """
    def homogenize(f, s):
        """Return homogeneous polynomial of ``f``"""
    def homogeneous_order(f):
        """Returns the homogeneous order of ``f``. """
    def LC(f):
        """Returns the leading coefficient of ``f``. """
    def TC(f):
        """Returns the trailing coefficient of ``f``. """
    def nth(f, *N):
        """Returns the ``n``-th coefficient of ``f``. """
    def max_norm(f):
        """Returns maximum norm of ``f``. """
    def l1_norm(f):
        """Returns l1 norm of ``f``. """
    def l2_norm_squared(f):
        """Return squared l2 norm of ``f``. """
    def clear_denoms(f):
        """Clear denominators, but keep the ground domain. """
    def integrate(f, m: int = 1, j: int = 0):
        """Computes the ``m``-th order indefinite integral of ``f`` in ``x_j``. """
    def diff(f, m: int = 1, j: int = 0):
        """Computes the ``m``-th order derivative of ``f`` in ``x_j``. """
    def eval(f, a, j: int = 0):
        """Evaluates ``f`` at the given point ``a`` in ``x_j``. """
    def half_gcdex(f, g):
        """Half extended Euclidean algorithm, if univariate. """
    def gcdex(f, g):
        """Extended Euclidean algorithm, if univariate. """
    def invert(f, g):
        """Invert ``f`` modulo ``g``, if possible. """
    def revert(f, n):
        """Compute ``f**(-1)`` mod ``x**n``. """
    def subresultants(f, g):
        """Computes subresultant PRS sequence of ``f`` and ``g``. """
    def resultant(f, g, includePRS: bool = False):
        """Computes resultant of ``f`` and ``g`` via PRS. """
    def discriminant(f):
        """Computes discriminant of ``f``. """
    def cofactors(f, g):
        """Returns GCD of ``f`` and ``g`` and their cofactors. """
    def gcd(f, g):
        """Returns polynomial GCD of ``f`` and ``g``. """
    def lcm(f, g):
        """Returns polynomial LCM of ``f`` and ``g``. """
    def cancel(f, g, include: bool = True):
        """Cancel common factors in a rational function ``f/g``. """
    def trunc(f, p):
        """Reduce ``f`` modulo a constant ``p``. """
    def monic(f):
        """Divides all coefficients by ``LC(f)``. """
    def content(f):
        """Returns GCD of polynomial coefficients. """
    def primitive(f):
        """Returns content and a primitive form of ``f``. """
    def compose(f, g):
        """Computes functional composition of ``f`` and ``g``. """
    def decompose(f):
        """Computes functional decomposition of ``f``. """
    def shift(f, a):
        """Efficiently compute Taylor shift ``f(x + a)``. """
    def transform(f, p, q):
        """Evaluate functional transformation ``q**n * f(p/q)``."""
    def sturm(f):
        """Computes the Sturm sequence of ``f``. """
    def cauchy_upper_bound(f):
        """Computes the Cauchy upper bound on the roots of ``f``. """
    def cauchy_lower_bound(f):
        """Computes the Cauchy lower bound on the nonzero roots of ``f``. """
    def mignotte_sep_bound_squared(f):
        """Computes the squared Mignotte bound on root separations of ``f``. """
    def gff_list(f):
        """Computes greatest factorial factorization of ``f``. """
    def norm(f):
        """Computes ``Norm(f)``."""
    def sqf_norm(f):
        """Computes square-free norm of ``f``. """
    def sqf_part(f):
        """Computes square-free part of ``f``. """
    def sqf_list(f, all: bool = False):
        """Returns a list of square-free factors of ``f``. """
    def sqf_list_include(f, all: bool = False):
        """Returns a list of square-free factors of ``f``. """
    def factor_list(f):
        """Returns a list of irreducible factors of ``f``. """
    def factor_list_include(f):
        """Returns a list of irreducible factors of ``f``. """
    def intervals(f, all: bool = False, eps: Incomplete | None = None, inf: Incomplete | None = None, sup: Incomplete | None = None, fast: bool = False, sqf: bool = False):
        """Compute isolating intervals for roots of ``f``. """
    def refine_root(f, s, t, eps: Incomplete | None = None, steps: Incomplete | None = None, fast: bool = False):
        """
        Refine an isolating interval to the given precision.

        ``eps`` should be a rational number.

        """
    def count_real_roots(f, inf: Incomplete | None = None, sup: Incomplete | None = None):
        """Return the number of real roots of ``f`` in ``[inf, sup]``. """
    def count_complex_roots(f, inf: Incomplete | None = None, sup: Incomplete | None = None):
        """Return the number of complex roots of ``f`` in ``[inf, sup]``. """
    @property
    def is_zero(f):
        """Returns ``True`` if ``f`` is a zero polynomial. """
    @property
    def is_one(f):
        """Returns ``True`` if ``f`` is a unit polynomial. """
    @property
    def is_ground(f):
        """Returns ``True`` if ``f`` is an element of the ground domain. """
    @property
    def is_sqf(f):
        """Returns ``True`` if ``f`` is a square-free polynomial. """
    @property
    def is_monic(f):
        """Returns ``True`` if the leading coefficient of ``f`` is one. """
    @property
    def is_primitive(f):
        """Returns ``True`` if the GCD of the coefficients of ``f`` is one. """
    @property
    def is_linear(f):
        """Returns ``True`` if ``f`` is linear in all its variables. """
    @property
    def is_quadratic(f):
        """Returns ``True`` if ``f`` is quadratic in all its variables. """
    @property
    def is_monomial(f):
        """Returns ``True`` if ``f`` is zero or has only one term. """
    @property
    def is_homogeneous(f):
        """Returns ``True`` if ``f`` is a homogeneous polynomial. """
    @property
    def is_irreducible(f):
        """Returns ``True`` if ``f`` has no factors over its domain. """
    @property
    def is_cyclotomic(f):
        """Returns ``True`` if ``f`` is a cyclotomic polynomial. """
    def __abs__(f): ...
    def __neg__(f): ...
    def __add__(f, g): ...
    def __radd__(f, g): ...
    def __sub__(f, g): ...
    def __rsub__(f, g): ...
    def __mul__(f, g): ...
    def __truediv__(f, g): ...
    def __rtruediv__(f, g): ...
    def __rmul__(f, g): ...
    def __pow__(f, n): ...
    def __divmod__(f, g): ...
    def __mod__(f, g): ...
    def __floordiv__(f, g): ...
    def __eq__(f, g): ...
    def __ne__(f, g): ...
    def eq(f, g, strict: bool = False): ...
    def ne(f, g, strict: bool = False): ...
    def __lt__(f, g): ...
    def __le__(f, g): ...
    def __gt__(f, g): ...
    def __ge__(f, g): ...
    def __bool__(f) -> bool: ...

def init_normal_DMF(num, den, lev, dom): ...

class DMF(PicklableWithSlots, CantSympify):
    """Dense Multivariate Fractions over `K`. """
    num: Incomplete
    den: Incomplete
    lev: Incomplete
    dom: Incomplete
    ring: Incomplete
    def __init__(self, rep, dom, lev: Incomplete | None = None, ring: Incomplete | None = None) -> None: ...
    @classmethod
    def new(cls, rep, dom, lev: Incomplete | None = None, ring: Incomplete | None = None): ...
    def __hash__(f): ...
    def poly_unify(f, g):
        """Unify a multivariate fraction and a polynomial. """
    def frac_unify(f, g):
        """Unify representations of two multivariate fractions. """
    def per(f, num, den, cancel: bool = True, kill: bool = False, ring: Incomplete | None = None):
        """Create a DMF out of the given representation. """
    def half_per(f, rep, kill: bool = False):
        """Create a DMP out of the given representation. """
    @classmethod
    def zero(cls, lev, dom, ring: Incomplete | None = None): ...
    @classmethod
    def one(cls, lev, dom, ring: Incomplete | None = None): ...
    def numer(f):
        """Returns the numerator of ``f``. """
    def denom(f):
        """Returns the denominator of ``f``. """
    def cancel(f):
        """Remove common factors from ``f.num`` and ``f.den``. """
    def neg(f):
        """Negate all coefficients in ``f``. """
    def add(f, g):
        """Add two multivariate fractions ``f`` and ``g``. """
    def sub(f, g):
        """Subtract two multivariate fractions ``f`` and ``g``. """
    def mul(f, g):
        """Multiply two multivariate fractions ``f`` and ``g``. """
    def pow(f, n):
        """Raise ``f`` to a non-negative power ``n``. """
    def quo(f, g):
        """Computes quotient of fractions ``f`` and ``g``. """
    exquo = quo
    def invert(f, check: bool = True):
        """Computes inverse of a fraction ``f``. """
    @property
    def is_zero(f):
        """Returns ``True`` if ``f`` is a zero fraction. """
    @property
    def is_one(f):
        """Returns ``True`` if ``f`` is a unit fraction. """
    def __neg__(f): ...
    def __add__(f, g): ...
    def __radd__(f, g): ...
    def __sub__(f, g): ...
    def __rsub__(f, g): ...
    def __mul__(f, g): ...
    def __rmul__(f, g): ...
    def __pow__(f, n): ...
    def __truediv__(f, g): ...
    def __rtruediv__(self, g): ...
    def __eq__(f, g): ...
    def __ne__(f, g): ...
    def __lt__(f, g): ...
    def __le__(f, g): ...
    def __gt__(f, g): ...
    def __ge__(f, g): ...
    def __bool__(f) -> bool: ...

def init_normal_ANP(rep, mod, dom): ...

class ANP(PicklableWithSlots, CantSympify):
    """Dense Algebraic Number Polynomials over a field. """
    rep: Incomplete
    mod: Incomplete
    dom: Incomplete
    def __init__(self, rep, mod, dom) -> None: ...
    def __hash__(f): ...
    def unify(f, g):
        """Unify representations of two algebraic numbers. """
    def per(f, rep, mod: Incomplete | None = None, dom: Incomplete | None = None): ...
    @classmethod
    def zero(cls, mod, dom): ...
    @classmethod
    def one(cls, mod, dom): ...
    def to_dict(f):
        """Convert ``f`` to a dict representation with native coefficients. """
    def to_sympy_dict(f):
        """Convert ``f`` to a dict representation with SymPy coefficients. """
    def to_list(f):
        """Convert ``f`` to a list representation with native coefficients. """
    def to_sympy_list(f):
        """Convert ``f`` to a list representation with SymPy coefficients. """
    def to_tuple(f):
        """
        Convert ``f`` to a tuple representation with native coefficients.

        This is needed for hashing.
        """
    @classmethod
    def from_list(cls, rep, mod, dom): ...
    def neg(f): ...
    def add(f, g): ...
    def sub(f, g): ...
    def mul(f, g): ...
    def pow(f, n):
        """Raise ``f`` to a non-negative power ``n``. """
    def div(f, g): ...
    def rem(f, g): ...
    def quo(f, g): ...
    exquo = quo
    def LC(f):
        """Returns the leading coefficient of ``f``. """
    def TC(f):
        """Returns the trailing coefficient of ``f``. """
    @property
    def is_zero(f):
        """Returns ``True`` if ``f`` is a zero algebraic number. """
    @property
    def is_one(f):
        """Returns ``True`` if ``f`` is a unit algebraic number. """
    @property
    def is_ground(f):
        """Returns ``True`` if ``f`` is an element of the ground domain. """
    def __pos__(f): ...
    def __neg__(f): ...
    def __add__(f, g): ...
    def __radd__(f, g): ...
    def __sub__(f, g): ...
    def __rsub__(f, g): ...
    def __mul__(f, g): ...
    def __rmul__(f, g): ...
    def __pow__(f, n): ...
    def __divmod__(f, g): ...
    def __mod__(f, g): ...
    def __truediv__(f, g): ...
    def __eq__(f, g): ...
    def __ne__(f, g): ...
    def __lt__(f, g): ...
    def __le__(f, g): ...
    def __gt__(f, g): ...
    def __ge__(f, g): ...
    def __bool__(f) -> bool: ...
