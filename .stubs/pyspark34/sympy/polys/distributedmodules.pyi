from _typeshed import Incomplete
from sympy.core.singleton import S as S
from sympy.core.sympify import sympify as sympify
from sympy.polys.monomials import monomial_deg as monomial_deg, monomial_div as monomial_div, monomial_lcm as monomial_lcm, monomial_mul as monomial_mul
from sympy.polys.polytools import Poly as Poly
from sympy.polys.polyutils import parallel_dict_from_expr as parallel_dict_from_expr

def sdm_monomial_mul(M, X):
    """
    Multiply tuple ``X`` representing a monomial of `K[X]` into the tuple
    ``M`` representing a monomial of `F`.

    Examples
    ========

    Multiplying `xy^3` into `x f_1` yields `x^2 y^3 f_1`:

    >>> from sympy.polys.distributedmodules import sdm_monomial_mul
    >>> sdm_monomial_mul((1, 1, 0), (1, 3))
    (1, 2, 3)
    """
def sdm_monomial_deg(M):
    """
    Return the total degree of ``M``.

    Examples
    ========

    For example, the total degree of `x^2 y f_5` is 3:

    >>> from sympy.polys.distributedmodules import sdm_monomial_deg
    >>> sdm_monomial_deg((5, 2, 1))
    3
    """
def sdm_monomial_lcm(A, B):
    '''
    Return the "least common multiple" of ``A`` and ``B``.

    IF `A = M e_j` and `B = N e_j`, where `M` and `N` are polynomial monomials,
    this returns `\\lcm(M, N) e_j`. Note that ``A`` and ``B`` involve distinct
    monomials.

    Otherwise the result is undefined.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_monomial_lcm
    >>> sdm_monomial_lcm((1, 2, 3), (1, 0, 5))
    (1, 2, 5)
    '''
def sdm_monomial_divides(A, B):
    """
    Does there exist a (polynomial) monomial X such that XA = B?

    Examples
    ========

    Positive examples:

    In the following examples, the monomial is given in terms of x, y and the
    generator(s), f_1, f_2 etc. The tuple form of that monomial is used in
    the call to sdm_monomial_divides.
    Note: the generator appears last in the expression but first in the tuple
    and other factors appear in the same order that they appear in the monomial
    expression.

    `A = f_1` divides `B = f_1`

    >>> from sympy.polys.distributedmodules import sdm_monomial_divides
    >>> sdm_monomial_divides((1, 0, 0), (1, 0, 0))
    True

    `A = f_1` divides `B = x^2 y f_1`

    >>> sdm_monomial_divides((1, 0, 0), (1, 2, 1))
    True

    `A = xy f_5` divides `B = x^2 y f_5`

    >>> sdm_monomial_divides((5, 1, 1), (5, 2, 1))
    True

    Negative examples:

    `A = f_1` does not divide `B = f_2`

    >>> sdm_monomial_divides((1, 0, 0), (2, 0, 0))
    False

    `A = x f_1` does not divide `B = f_1`

    >>> sdm_monomial_divides((1, 1, 0), (1, 0, 0))
    False

    `A = xy^2 f_5` does not divide `B = y f_5`

    >>> sdm_monomial_divides((5, 1, 2), (5, 0, 1))
    False
    """
def sdm_LC(f, K):
    """Returns the leading coefficient of ``f``. """
def sdm_to_dict(f):
    """Make a dictionary from a distributed polynomial. """
def sdm_from_dict(d, O):
    """
    Create an sdm from a dictionary.

    Here ``O`` is the monomial order to use.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_from_dict
    >>> from sympy.polys import QQ, lex
    >>> dic = {(1, 1, 0): QQ(1), (1, 0, 0): QQ(2), (0, 1, 0): QQ(0)}
    >>> sdm_from_dict(dic, lex)
    [((1, 1, 0), 1), ((1, 0, 0), 2)]
    """
def sdm_sort(f, O):
    """Sort terms in ``f`` using the given monomial order ``O``. """
def sdm_strip(f):
    """Remove terms with zero coefficients from ``f`` in ``K[X]``. """
def sdm_add(f, g, O, K):
    """
    Add two module elements ``f``, ``g``.

    Addition is done over the ground field ``K``, monomials are ordered
    according to ``O``.

    Examples
    ========

    All examples use lexicographic order.

    `(xy f_1) + (f_2) = f_2 + xy f_1`

    >>> from sympy.polys.distributedmodules import sdm_add
    >>> from sympy.polys import lex, QQ
    >>> sdm_add([((1, 1, 1), QQ(1))], [((2, 0, 0), QQ(1))], lex, QQ)
    [((2, 0, 0), 1), ((1, 1, 1), 1)]

    `(xy f_1) + (-xy f_1)` = 0`

    >>> sdm_add([((1, 1, 1), QQ(1))], [((1, 1, 1), QQ(-1))], lex, QQ)
    []

    `(f_1) + (2f_1) = 3f_1`

    >>> sdm_add([((1, 0, 0), QQ(1))], [((1, 0, 0), QQ(2))], lex, QQ)
    [((1, 0, 0), 3)]

    `(yf_1) + (xf_1) = xf_1 + yf_1`

    >>> sdm_add([((1, 0, 1), QQ(1))], [((1, 1, 0), QQ(1))], lex, QQ)
    [((1, 1, 0), 1), ((1, 0, 1), 1)]
    """
def sdm_LM(f):
    """
    Returns the leading monomial of ``f``.

    Only valid if `f \\ne 0`.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_LM, sdm_from_dict
    >>> from sympy.polys import QQ, lex
    >>> dic = {(1, 2, 3): QQ(1), (4, 0, 0): QQ(1), (4, 0, 1): QQ(1)}
    >>> sdm_LM(sdm_from_dict(dic, lex))
    (4, 0, 1)
    """
def sdm_LT(f):
    """
    Returns the leading term of ``f``.

    Only valid if `f \\ne 0`.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_LT, sdm_from_dict
    >>> from sympy.polys import QQ, lex
    >>> dic = {(1, 2, 3): QQ(1), (4, 0, 0): QQ(2), (4, 0, 1): QQ(3)}
    >>> sdm_LT(sdm_from_dict(dic, lex))
    ((4, 0, 1), 3)
    """
def sdm_mul_term(f, term, O, K):
    """
    Multiply a distributed module element ``f`` by a (polynomial) term ``term``.

    Multiplication of coefficients is done over the ground field ``K``, and
    monomials are ordered according to ``O``.

    Examples
    ========

    `0 f_1 = 0`

    >>> from sympy.polys.distributedmodules import sdm_mul_term
    >>> from sympy.polys import lex, QQ
    >>> sdm_mul_term([((1, 0, 0), QQ(1))], ((0, 0), QQ(0)), lex, QQ)
    []

    `x 0 = 0`

    >>> sdm_mul_term([], ((1, 0), QQ(1)), lex, QQ)
    []

    `(x) (f_1) = xf_1`

    >>> sdm_mul_term([((1, 0, 0), QQ(1))], ((1, 0), QQ(1)), lex, QQ)
    [((1, 1, 0), 1)]

    `(2xy) (3x f_1 + 4y f_2) = 8xy^2 f_2 + 6x^2y f_1`

    >>> f = [((2, 0, 1), QQ(4)), ((1, 1, 0), QQ(3))]
    >>> sdm_mul_term(f, ((1, 1), QQ(2)), lex, QQ)
    [((2, 1, 2), 8), ((1, 2, 1), 6)]
    """
def sdm_zero():
    """Return the zero module element."""
def sdm_deg(f):
    """
    Degree of ``f``.

    This is the maximum of the degrees of all its monomials.
    Invalid if ``f`` is zero.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_deg
    >>> sdm_deg([((1, 2, 3), 1), ((10, 0, 1), 1), ((2, 3, 4), 4)])
    7
    """
def sdm_from_vector(vec, O, K, **opts):
    """
    Create an sdm from an iterable of expressions.

    Coefficients are created in the ground field ``K``, and terms are ordered
    according to monomial order ``O``. Named arguments are passed on to the
    polys conversion code and can be used to specify for example generators.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_from_vector
    >>> from sympy.abc import x, y, z
    >>> from sympy.polys import QQ, lex
    >>> sdm_from_vector([x**2+y**2, 2*z], lex, QQ)
    [((1, 0, 0, 1), 2), ((0, 2, 0, 0), 1), ((0, 0, 2, 0), 1)]
    """
def sdm_to_vector(f, gens, K, n: Incomplete | None = None):
    """
    Convert sdm ``f`` into a list of polynomial expressions.

    The generators for the polynomial ring are specified via ``gens``. The rank
    of the module is guessed, or passed via ``n``. The ground field is assumed
    to be ``K``.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_to_vector
    >>> from sympy.abc import x, y, z
    >>> from sympy.polys import QQ
    >>> f = [((1, 0, 0, 1), QQ(2)), ((0, 2, 0, 0), QQ(1)), ((0, 0, 2, 0), QQ(1))]
    >>> sdm_to_vector(f, [x, y, z], QQ)
    [x**2 + y**2, 2*z]
    """
def sdm_spoly(f, g, O, K, phantom: Incomplete | None = None):
    """
    Compute the generalized s-polynomial of ``f`` and ``g``.

    The ground field is assumed to be ``K``, and monomials ordered according to
    ``O``.

    This is invalid if either of ``f`` or ``g`` is zero.

    If the leading terms of `f` and `g` involve different basis elements of
    `F`, their s-poly is defined to be zero. Otherwise it is a certain linear
    combination of `f` and `g` in which the leading terms cancel.
    See [SCA, defn 2.3.6] for details.

    If ``phantom`` is not ``None``, it should be a pair of module elements on
    which to perform the same operation(s) as on ``f`` and ``g``. The in this
    case both results are returned.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_spoly
    >>> from sympy.polys import QQ, lex
    >>> f = [((2, 1, 1), QQ(1)), ((1, 0, 1), QQ(1))]
    >>> g = [((2, 3, 0), QQ(1))]
    >>> h = [((1, 2, 3), QQ(1))]
    >>> sdm_spoly(f, h, lex, QQ)
    []
    >>> sdm_spoly(f, g, lex, QQ)
    [((1, 2, 1), 1)]
    """
def sdm_ecart(f):
    """
    Compute the ecart of ``f``.

    This is defined to be the difference of the total degree of `f` and the
    total degree of the leading monomial of `f` [SCA, defn 2.3.7].

    Invalid if f is zero.

    Examples
    ========

    >>> from sympy.polys.distributedmodules import sdm_ecart
    >>> sdm_ecart([((1, 2, 3), 1), ((1, 0, 1), 1)])
    0
    >>> sdm_ecart([((2, 2, 1), 1), ((1, 5, 1), 1)])
    3
    """
def sdm_nf_mora(f, G, O, K, phantom: Incomplete | None = None):
    '''
    Compute a weak normal form of ``f`` with respect to ``G`` and order ``O``.

    The ground field is assumed to be ``K``, and monomials ordered according to
    ``O``.

    Weak normal forms are defined in [SCA, defn 2.3.3]. They are not unique.
    This function deterministically computes a weak normal form, depending on
    the order of `G`.

    The most important property of a weak normal form is the following: if
    `R` is the ring associated with the monomial ordering (if the ordering is
    global, we just have `R = K[x_1, \\ldots, x_n]`, otherwise it is a certain
    localization thereof), `I` any ideal of `R` and `G` a standard basis for
    `I`, then for any `f \\in R`, we have `f \\in I` if and only if
    `NF(f | G) = 0`.

    This is the generalized Mora algorithm for computing weak normal forms with
    respect to arbitrary monomial orders [SCA, algorithm 2.3.9].

    If ``phantom`` is not ``None``, it should be a pair of "phantom" arguments
    on which to perform the same computations as on ``f``, ``G``, both results
    are then returned.
    '''
def sdm_nf_buchberger(f, G, O, K, phantom: Incomplete | None = None):
    '''
    Compute a weak normal form of ``f`` with respect to ``G`` and order ``O``.

    The ground field is assumed to be ``K``, and monomials ordered according to
    ``O``.

    This is the standard Buchberger algorithm for computing weak normal forms with
    respect to *global* monomial orders [SCA, algorithm 1.6.10].

    If ``phantom`` is not ``None``, it should be a pair of "phantom" arguments
    on which to perform the same computations as on ``f``, ``G``, both results
    are then returned.
    '''
def sdm_nf_buchberger_reduced(f, G, O, K):
    '''
    Compute a reduced normal form of ``f`` with respect to ``G`` and order ``O``.

    The ground field is assumed to be ``K``, and monomials ordered according to
    ``O``.

    In contrast to weak normal forms, reduced normal forms *are* unique, but
    their computation is more expensive.

    This is the standard Buchberger algorithm for computing reduced normal forms
    with respect to *global* monomial orders [SCA, algorithm 1.6.11].

    The ``pantom`` option is not supported, so this normal form cannot be used
    as a normal form for the "extended" groebner algorithm.
    '''
def sdm_groebner(G, NF, O, K, extended: bool = False):
    '''
    Compute a minimal standard basis of ``G`` with respect to order ``O``.

    The algorithm uses a normal form ``NF``, for example ``sdm_nf_mora``.
    The ground field is assumed to be ``K``, and monomials ordered according
    to ``O``.

    Let `N` denote the submodule generated by elements of `G`. A standard
    basis for `N` is a subset `S` of `N`, such that `in(S) = in(N)`, where for
    any subset `X` of `F`, `in(X)` denotes the submodule generated by the
    initial forms of elements of `X`. [SCA, defn 2.3.2]

    A standard basis is called minimal if no subset of it is a standard basis.

    One may show that standard bases are always generating sets.

    Minimal standard bases are not unique. This algorithm computes a
    deterministic result, depending on the particular order of `G`.

    If ``extended=True``, also compute the transition matrix from the initial
    generators to the groebner basis. That is, return a list of coefficient
    vectors, expressing the elements of the groebner basis in terms of the
    elements of ``G``.

    This functions implements the "sugar" strategy, see

    Giovini et al: "One sugar cube, please" OR Selection strategies in
    Buchberger algorithm.
    '''
