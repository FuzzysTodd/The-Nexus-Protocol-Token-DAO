from _typeshed import Incomplete
from sympy.core.symbol import Dummy as Dummy
from sympy.polys.monomials import monomial_divides as monomial_divides, monomial_lcm as monomial_lcm, monomial_mul as monomial_mul, term_div as term_div
from sympy.polys.orderings import lex as lex
from sympy.polys.polyconfig import query as query
from sympy.polys.polyerrors import DomainError as DomainError

def groebner(seq, ring, method: Incomplete | None = None):
    """
    Computes Groebner basis for a set of polynomials in `K[X]`.

    Wrapper around the (default) improved Buchberger and the other algorithms
    for computing Groebner bases. The choice of algorithm can be changed via
    ``method`` argument or :func:`sympy.polys.polyconfig.setup`, where
    ``method`` can be either ``buchberger`` or ``f5b``.

    """
def spoly(p1, p2, ring):
    """
    Compute LCM(LM(p1), LM(p2))/LM(p1)*p1 - LCM(LM(p1), LM(p2))/LM(p2)*p2
    This is the S-poly provided p1 and p2 are monic
    """
def Sign(f): ...
def Polyn(f): ...
def Num(f): ...
def sig(monomial, index): ...
def lbp(signature, polynomial, number): ...
def sig_cmp(u, v, order):
    """
    Compare two signatures by extending the term order to K[X]^n.

    u < v iff
        - the index of v is greater than the index of u
    or
        - the index of v is equal to the index of u and u[0] < v[0] w.r.t. order

    u > v otherwise
    """
def sig_key(s, order):
    """
    Key for comparing two signatures.

    s = (m, k), t = (n, l)

    s < t iff [k > l] or [k == l and m < n]
    s > t otherwise
    """
def sig_mult(s, m):
    """
    Multiply a signature by a monomial.

    The product of a signature (m, i) and a monomial n is defined as
    (m * t, i).
    """
def lbp_sub(f, g):
    """
    Subtract labeled polynomial g from f.

    The signature and number of the difference of f and g are signature
    and number of the maximum of f and g, w.r.t. lbp_cmp.
    """
def lbp_mul_term(f, cx):
    """
    Multiply a labeled polynomial with a term.

    The product of a labeled polynomial (s, p, k) by a monomial is
    defined as (m * s, m * p, k).
    """
def lbp_cmp(f, g):
    """
    Compare two labeled polynomials.

    f < g iff
        - Sign(f) < Sign(g)
    or
        - Sign(f) == Sign(g) and Num(f) > Num(g)

    f > g otherwise
    """
def lbp_key(f):
    """
    Key for comparing two labeled polynomials.
    """
def critical_pair(f, g, ring):
    """
    Compute the critical pair corresponding to two labeled polynomials.

    A critical pair is a tuple (um, f, vm, g), where um and vm are
    terms such that um * f - vm * g is the S-polynomial of f and g (so,
    wlog assume um * f > vm * g).
    For performance sake, a critical pair is represented as a tuple
    (Sign(um * f), um, f, Sign(vm * g), vm, g), since um * f creates
    a new, relatively expensive object in memory, whereas Sign(um *
    f) and um are lightweight and f (in the tuple) is a reference to
    an already existing object in memory.
    """
def cp_cmp(c, d):
    """
    Compare two critical pairs c and d.

    c < d iff
        - lbp(c[0], _, Num(c[2]) < lbp(d[0], _, Num(d[2])) (this
        corresponds to um_c * f_c and um_d * f_d)
    or
        - lbp(c[0], _, Num(c[2]) >< lbp(d[0], _, Num(d[2])) and
        lbp(c[3], _, Num(c[5])) < lbp(d[3], _, Num(d[5])) (this
        corresponds to vm_c * g_c and vm_d * g_d)

    c > d otherwise
    """
def cp_key(c, ring):
    """
    Key for comparing critical pairs.
    """
def s_poly(cp):
    """
    Compute the S-polynomial of a critical pair.

    The S-polynomial of a critical pair cp is cp[1] * cp[2] - cp[4] * cp[5].
    """
def is_rewritable_or_comparable(sign, num, B):
    """
    Check if a labeled polynomial is redundant by checking if its
    signature and number imply rewritability or comparability.

    (sign, num) is comparable if there exists a labeled polynomial
    h in B, such that sign[1] (the index) is less than Sign(h)[1]
    and sign[0] is divisible by the leading monomial of h.

    (sign, num) is rewritable if there exists a labeled polynomial
    h in B, such thatsign[1] is equal to Sign(h)[1], num < Num(h)
    and sign[0] is divisible by Sign(h)[0].
    """
def f5_reduce(f, B):
    '''
    F5-reduce a labeled polynomial f by B.

    Continuously searches for non-zero labeled polynomial h in B, such
    that the leading term lt_h of h divides the leading term lt_f of
    f and Sign(lt_h * h) < Sign(f). If such a labeled polynomial h is
    found, f gets replaced by f - lt_f / lt_h * h. If no such h can be
    found or f is 0, f is no further F5-reducible and f gets returned.

    A polynomial that is reducible in the usual sense need not be
    F5-reducible, e.g.:

    >>> from sympy.polys.groebnertools import lbp, sig, f5_reduce, Polyn
    >>> from sympy.polys import ring, QQ, lex

    >>> R, x,y,z = ring("x,y,z", QQ, lex)

    >>> f = lbp(sig((1, 1, 1), 4), x, 3)
    >>> g = lbp(sig((0, 0, 0), 2), x, 2)

    >>> Polyn(f).rem([Polyn(g)])
    0
    >>> f5_reduce(f, [g])
    (((1, 1, 1), 4), x, 3)

    '''
def red_groebner(G, ring):
    """
    Compute reduced Groebner basis, from BeckerWeispfenning93, p. 216

    Selects a subset of generators, that already generate the ideal
    and computes a reduced Groebner basis for them.
    """
def is_groebner(G, ring):
    """
    Check if G is a Groebner basis.
    """
def is_minimal(G, ring):
    """
    Checks if G is a minimal Groebner basis.
    """
def is_reduced(G, ring):
    """
    Checks if G is a reduced Groebner basis.
    """
def groebner_lcm(f, g):
    """
    Computes LCM of two polynomials using Groebner bases.

    The LCM is computed as the unique generator of the intersection
    of the two ideals generated by `f` and `g`. The approach is to
    compute a Groebner basis with respect to lexicographic ordering
    of `t*f` and `(1 - t)*g`, where `t` is an unrelated variable and
    then filtering out the solution that does not contain `t`.

    References
    ==========

    .. [1] [Cox97]_

    """
def groebner_gcd(f, g):
    """Computes GCD of two polynomials using Groebner bases. """
