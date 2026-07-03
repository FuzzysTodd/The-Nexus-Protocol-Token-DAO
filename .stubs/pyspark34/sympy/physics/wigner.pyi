from _typeshed import Incomplete
from sympy.concrete.summations import Sum as Sum
from sympy.core.add import Add as Add
from sympy.core.function import Function as Function
from sympy.core.numbers import I as I, Integer as Integer, pi as pi
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import binomial as binomial, factorial as factorial
from sympy.functions.elementary.complexes import re as re
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin
from sympy.functions.special.spherical_harmonics import Ynm as Ynm
from sympy.matrices.dense import zeros as zeros
from sympy.matrices.immutable import ImmutableMatrix as ImmutableMatrix
from sympy.utilities.misc import as_int as as_int

def wigner_3j(j_1, j_2, j_3, m_1, m_2, m_3):
    """
    Calculate the Wigner 3j symbol `\\operatorname{Wigner3j}(j_1,j_2,j_3,m_1,m_2,m_3)`.

    Parameters
    ==========

    j_1, j_2, j_3, m_1, m_2, m_3 :
        Integer or half integer.

    Returns
    =======

    Rational number times the square root of a rational number.

    Examples
    ========

    >>> from sympy.physics.wigner import wigner_3j
    >>> wigner_3j(2, 6, 4, 0, 0, 0)
    sqrt(715)/143
    >>> wigner_3j(2, 6, 4, 0, 0, 1)
    0

    It is an error to have arguments that are not integer or half
    integer values::

        sage: wigner_3j(2.1, 6, 4, 0, 0, 0)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer
        sage: wigner_3j(2, 6, 4, 1, 0, -1.1)
        Traceback (most recent call last):
        ...
        ValueError: m values must be integer or half integer

    Notes
    =====

    The Wigner 3j symbol obeys the following symmetry rules:

    - invariant under any permutation of the columns (with the
      exception of a sign change where `J:=j_1+j_2+j_3`):

      .. math::

         \\begin{aligned}
         \\operatorname{Wigner3j}(j_1,j_2,j_3,m_1,m_2,m_3)
          &=\\operatorname{Wigner3j}(j_3,j_1,j_2,m_3,m_1,m_2) \\\\\n          &=\\operatorname{Wigner3j}(j_2,j_3,j_1,m_2,m_3,m_1) \\\\\n          &=(-1)^J \\operatorname{Wigner3j}(j_3,j_2,j_1,m_3,m_2,m_1) \\\\\n          &=(-1)^J \\operatorname{Wigner3j}(j_1,j_3,j_2,m_1,m_3,m_2) \\\\\n          &=(-1)^J \\operatorname{Wigner3j}(j_2,j_1,j_3,m_2,m_1,m_3)
         \\end{aligned}

    - invariant under space inflection, i.e.

      .. math::

         \\operatorname{Wigner3j}(j_1,j_2,j_3,m_1,m_2,m_3)
         =(-1)^J \\operatorname{Wigner3j}(j_1,j_2,j_3,-m_1,-m_2,-m_3)

    - symmetric with respect to the 72 additional symmetries based on
      the work by [Regge58]_

    - zero for `j_1`, `j_2`, `j_3` not fulfilling triangle relation

    - zero for `m_1 + m_2 + m_3 \\neq 0`

    - zero for violating any one of the conditions
      `j_1 \\ge |m_1|`,  `j_2 \\ge |m_2|`,  `j_3 \\ge |m_3|`

    Algorithm
    =========

    This function uses the algorithm of [Edmonds74]_ to calculate the
    value of the 3j symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [Rasch03]_.

    Authors
    =======

    - Jens Rasch (2009-03-24): initial version
    """
def clebsch_gordan(j_1, j_2, j_3, m_1, m_2, m_3):
    """
    Calculates the Clebsch-Gordan coefficient.
    `\\left\\langle j_1 m_1 \\; j_2 m_2 | j_3 m_3 \\right\\rangle`.

    The reference for this function is [Edmonds74]_.

    Parameters
    ==========

    j_1, j_2, j_3, m_1, m_2, m_3 :
        Integer or half integer.

    Returns
    =======

    Rational number times the square root of a rational number.

    Examples
    ========

    >>> from sympy import S
    >>> from sympy.physics.wigner import clebsch_gordan
    >>> clebsch_gordan(S(3)/2, S(1)/2, 2, S(3)/2, S(1)/2, 2)
    1
    >>> clebsch_gordan(S(3)/2, S(1)/2, 1, S(3)/2, -S(1)/2, 1)
    sqrt(3)/2
    >>> clebsch_gordan(S(3)/2, S(1)/2, 1, -S(1)/2, S(1)/2, 0)
    -sqrt(2)/2

    Notes
    =====

    The Clebsch-Gordan coefficient will be evaluated via its relation
    to Wigner 3j symbols:

    .. math::

        \\left\\langle j_1 m_1 \\; j_2 m_2 | j_3 m_3 \\right\\rangle
        =(-1)^{j_1-j_2+m_3} \\sqrt{2j_3+1}
        \\operatorname{Wigner3j}(j_1,j_2,j_3,m_1,m_2,-m_3)

    See also the documentation on Wigner 3j symbols which exhibit much
    higher symmetry relations than the Clebsch-Gordan coefficient.

    Authors
    =======

    - Jens Rasch (2009-03-24): initial version
    """
def racah(aa, bb, cc, dd, ee, ff, prec: Incomplete | None = None):
    """
    Calculate the Racah symbol `W(a,b,c,d;e,f)`.

    Parameters
    ==========

    a, ..., f :
        Integer or half integer.
    prec :
        Precision, default: ``None``. Providing a precision can
        drastically speed up the calculation.

    Returns
    =======

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    Examples
    ========

    >>> from sympy.physics.wigner import racah
    >>> racah(3,3,3,3,3,3)
    -1/14

    Notes
    =====

    The Racah symbol is related to the Wigner 6j symbol:

    .. math::

       \\operatorname{Wigner6j}(j_1,j_2,j_3,j_4,j_5,j_6)
       =(-1)^{j_1+j_2+j_4+j_5} W(j_1,j_2,j_5,j_4,j_3,j_6)

    Please see the 6j symbol for its much richer symmetries and for
    additional properties.

    Algorithm
    =========

    This function uses the algorithm of [Edmonds74]_ to calculate the
    value of the 6j symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [Rasch03]_.

    Authors
    =======

    - Jens Rasch (2009-03-24): initial version
    """
def wigner_6j(j_1, j_2, j_3, j_4, j_5, j_6, prec: Incomplete | None = None):
    """
    Calculate the Wigner 6j symbol `\\operatorname{Wigner6j}(j_1,j_2,j_3,j_4,j_5,j_6)`.

    Parameters
    ==========

    j_1, ..., j_6 :
        Integer or half integer.
    prec :
        Precision, default: ``None``. Providing a precision can
        drastically speed up the calculation.

    Returns
    =======

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    Examples
    ========

    >>> from sympy.physics.wigner import wigner_6j
    >>> wigner_6j(3,3,3,3,3,3)
    -1/14
    >>> wigner_6j(5,5,5,5,5,5)
    1/52

    It is an error to have arguments that are not integer or half
    integer values or do not fulfill the triangle relation::

        sage: wigner_6j(2.5,2.5,2.5,2.5,2.5,2.5)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation
        sage: wigner_6j(0.5,0.5,1.1,0.5,0.5,1.1)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation

    Notes
    =====

    The Wigner 6j symbol is related to the Racah symbol but exhibits
    more symmetries as detailed below.

    .. math::

       \\operatorname{Wigner6j}(j_1,j_2,j_3,j_4,j_5,j_6)
        =(-1)^{j_1+j_2+j_4+j_5} W(j_1,j_2,j_5,j_4,j_3,j_6)

    The Wigner 6j symbol obeys the following symmetry rules:

    - Wigner 6j symbols are left invariant under any permutation of
      the columns:

      .. math::

         \\begin{aligned}
         \\operatorname{Wigner6j}(j_1,j_2,j_3,j_4,j_5,j_6)
          &=\\operatorname{Wigner6j}(j_3,j_1,j_2,j_6,j_4,j_5) \\\\\n          &=\\operatorname{Wigner6j}(j_2,j_3,j_1,j_5,j_6,j_4) \\\\\n          &=\\operatorname{Wigner6j}(j_3,j_2,j_1,j_6,j_5,j_4) \\\\\n          &=\\operatorname{Wigner6j}(j_1,j_3,j_2,j_4,j_6,j_5) \\\\\n          &=\\operatorname{Wigner6j}(j_2,j_1,j_3,j_5,j_4,j_6)
         \\end{aligned}

    - They are invariant under the exchange of the upper and lower
      arguments in each of any two columns, i.e.

      .. math::

         \\operatorname{Wigner6j}(j_1,j_2,j_3,j_4,j_5,j_6)
          =\\operatorname{Wigner6j}(j_1,j_5,j_6,j_4,j_2,j_3)
          =\\operatorname{Wigner6j}(j_4,j_2,j_6,j_1,j_5,j_3)
          =\\operatorname{Wigner6j}(j_4,j_5,j_3,j_1,j_2,j_6)

    - additional 6 symmetries [Regge59]_ giving rise to 144 symmetries
      in total

    - only non-zero if any triple of `j`'s fulfill a triangle relation

    Algorithm
    =========

    This function uses the algorithm of [Edmonds74]_ to calculate the
    value of the 6j symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [Rasch03]_.

    """
def wigner_9j(j_1, j_2, j_3, j_4, j_5, j_6, j_7, j_8, j_9, prec: Incomplete | None = None):
    """
    Calculate the Wigner 9j symbol
    `\\operatorname{Wigner9j}(j_1,j_2,j_3,j_4,j_5,j_6,j_7,j_8,j_9)`.

    Parameters
    ==========

    j_1, ..., j_9 :
        Integer or half integer.
    prec : precision, default
        ``None``. Providing a precision can
        drastically speed up the calculation.

    Returns
    =======

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    Examples
    ========

    >>> from sympy.physics.wigner import wigner_9j
    >>> wigner_9j(1,1,1, 1,1,1, 1,1,0, prec=64) # ==1/18
    0.05555555...

    >>> wigner_9j(1/2,1/2,0, 1/2,3/2,1, 0,1,1, prec=64) # ==1/6
    0.1666666...

    It is an error to have arguments that are not integer or half
    integer values or do not fulfill the triangle relation::

        sage: wigner_9j(0.5,0.5,0.5, 0.5,0.5,0.5, 0.5,0.5,0.5,prec=64)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation
        sage: wigner_9j(1,1,1, 0.5,1,1.5, 0.5,1,2.5,prec=64)
        Traceback (most recent call last):
        ...
        ValueError: j values must be integer or half integer and fulfill the triangle relation

    Algorithm
    =========

    This function uses the algorithm of [Edmonds74]_ to calculate the
    value of the 3j symbol exactly. Note that the formula contains
    alternating sums over large factorials and is therefore unsuitable
    for finite precision arithmetic and only useful for a computer
    algebra system [Rasch03]_.
    """
def gaunt(l_1, l_2, l_3, m_1, m_2, m_3, prec: Incomplete | None = None):
    """
    Calculate the Gaunt coefficient.

    Explanation
    ===========

    The Gaunt coefficient is defined as the integral over three
    spherical harmonics:

    .. math::

        \\begin{aligned}
        \\operatorname{Gaunt}(l_1,l_2,l_3,m_1,m_2,m_3)
        &=\\int Y_{l_1,m_1}(\\Omega)
         Y_{l_2,m_2}(\\Omega) Y_{l_3,m_3}(\\Omega) \\,d\\Omega \\\\\n        &=\\sqrt{\\frac{(2l_1+1)(2l_2+1)(2l_3+1)}{4\\pi}}
         \\operatorname{Wigner3j}(l_1,l_2,l_3,0,0,0)
         \\operatorname{Wigner3j}(l_1,l_2,l_3,m_1,m_2,m_3)
        \\end{aligned}

    Parameters
    ==========

    l_1, l_2, l_3, m_1, m_2, m_3 :
        Integer.
    prec - precision, default: ``None``.
        Providing a precision can
        drastically speed up the calculation.

    Returns
    =======

    Rational number times the square root of a rational number
    (if ``prec=None``), or real number if a precision is given.

    Examples
    ========

    >>> from sympy.physics.wigner import gaunt
    >>> gaunt(1,0,1,1,0,-1)
    -1/(2*sqrt(pi))
    >>> gaunt(1000,1000,1200,9,3,-12).n(64)
    0.00689500421922113448...

    It is an error to use non-integer values for `l` and `m`::

        sage: gaunt(1.2,0,1.2,0,0,0)
        Traceback (most recent call last):
        ...
        ValueError: l values must be integer
        sage: gaunt(1,0,1,1.1,0,-1.1)
        Traceback (most recent call last):
        ...
        ValueError: m values must be integer

    Notes
    =====

    The Gaunt coefficient obeys the following symmetry rules:

    - invariant under any permutation of the columns

      .. math::
        \\begin{aligned}
          Y(l_1,l_2,l_3,m_1,m_2,m_3)
          &=Y(l_3,l_1,l_2,m_3,m_1,m_2) \\\\\n          &=Y(l_2,l_3,l_1,m_2,m_3,m_1) \\\\\n          &=Y(l_3,l_2,l_1,m_3,m_2,m_1) \\\\\n          &=Y(l_1,l_3,l_2,m_1,m_3,m_2) \\\\\n          &=Y(l_2,l_1,l_3,m_2,m_1,m_3)
        \\end{aligned}

    - invariant under space inflection, i.e.

      .. math::
          Y(l_1,l_2,l_3,m_1,m_2,m_3)
          =Y(l_1,l_2,l_3,-m_1,-m_2,-m_3)

    - symmetric with respect to the 72 Regge symmetries as inherited
      for the `3j` symbols [Regge58]_

    - zero for `l_1`, `l_2`, `l_3` not fulfilling triangle relation

    - zero for violating any one of the conditions: `l_1 \\ge |m_1|`,
      `l_2 \\ge |m_2|`, `l_3 \\ge |m_3|`

    - non-zero only for an even sum of the `l_i`, i.e.
      `L = l_1 + l_2 + l_3 = 2n` for `n` in `\\mathbb{N}`

    Algorithms
    ==========

    This function uses the algorithm of [Liberatodebrito82]_ to
    calculate the value of the Gaunt coefficient exactly. Note that
    the formula contains alternating sums over large factorials and is
    therefore unsuitable for finite precision arithmetic and only
    useful for a computer algebra system [Rasch03]_.

    Authors
    =======

    Jens Rasch (2009-03-24): initial version for Sage.
    """
def real_gaunt(l_1, l_2, l_3, m_1, m_2, m_3, prec: Incomplete | None = None):
    """
    Calculate the real Gaunt coefficient.

    Explanation
    ===========

    The real Gaunt coefficient is defined as the integral over three
    real spherical harmonics:

    .. math::
        \\begin{aligned}
        \\operatorname{RealGaunt}(l_1,l_2,l_3,m_1,m_2,m_3)
        &=\\int Z^{m_1}_{l_1}(\\Omega)
         Z^{m_2}_{l_2}(\\Omega) Z^{m_3}_{l_3}(\\Omega) \\,d\\Omega \\\\\n        \\end{aligned}

    Alternatively, it can be defined in terms of the standard Gaunt
    coefficient by relating the real spherical harmonics to the standard
    spherical harmonics via a unitary transformation `U`, i.e.
    `Z^{m}_{l}(\\Omega)=\\sum_{m'}U^{m}_{m'}Y^{m'}_{l}(\\Omega)` [Homeier96]_.
    The real Gaunt coefficient is then defined as

    .. math::
        \\begin{aligned}
        \\operatorname{RealGaunt}(l_1,l_2,l_3,m_1,m_2,m_3)
        &=\\int Z^{m_1}_{l_1}(\\Omega)
         Z^{m_2}_{l_2}(\\Omega) Z^{m_3}_{l_3}(\\Omega) \\,d\\Omega \\\\\n        &=\\sum_{m'_1 m'_2 m'_3} U^{m_1}_{m'_1}U^{m_2}_{m'_2}U^{m_3}_{m'_3}
         \\operatorname{Gaunt}(l_1,l_2,l_3,m'_1,m'_2,m'_3)
        \\end{aligned}

    The unitary matrix `U` has components

    .. math::
        \\begin{aligned}
        U^m_{m'} = \\delta_{|m||m'|}*(\\delta_{m'0}\\delta_{m0} + \\frac{1}{\\sqrt{2}}\\big[\\Theta(m)
        \\big(\\delta_{m'm}+(-1)^{m'}\\delta_{m'-m}\\big)+i\\Theta(-m)\\big((-1)^{-m}
        \\delta_{m'-m}-\\delta_{m'm}*(-1)^{m'-m}\\big)\\big])
        \\end{aligned}

    where `\\delta_{ij}` is the Kronecker delta symbol and `\\Theta` is a step
    function defined as

    .. math::
        \\begin{aligned}
        \\Theta(x) = \\begin{cases} 1 \\,\\text{for}\\, x > 0 \\\\ 0 \\,\\text{for}\\, x \\leq 0 \\end{cases}
        \\end{aligned}

    Parameters
    ==========

    l_1, l_2, l_3, m_1, m_2, m_3 :
        Integer.

    prec - precision, default: ``None``.
        Providing a precision can
        drastically speed up the calculation.

    Returns
    =======

    Rational number times the square root of a rational number.

    Examples
    ========

    >>> from sympy.physics.wigner import real_gaunt
    >>> real_gaunt(2,2,4,-1,-1,0)
    -2/(7*sqrt(pi))
    >>> real_gaunt(10,10,20,-9,-9,0).n(64)
    -0.00002480019791932209313156167...

    It is an error to use non-integer values for `l` and `m`::
        real_gaunt(2.8,0.5,1.3,0,0,0)
        Traceback (most recent call last):
        ...
        ValueError: l values must be integer
        real_gaunt(2,2,4,0.7,1,-3.4)
        Traceback (most recent call last):
        ...
        ValueError: m values must be integer

    Notes
    =====

    The real Gaunt coefficient inherits from the standard Gaunt coefficient,
    the invariance under any permutation of the pairs `(l_i, m_i)` and the
    requirement that the sum of the `l_i` be even to yield a non-zero value.
    It also obeys the following symmetry rules:

    - zero for `l_1`, `l_2`, `l_3` not fulfiling the condition
      `l_1 \\in \\{l_{\\text{max}}, l_{\\text{max}}-2, \\ldots, l_{\\text{min}}\\}`,
      where `l_{\\text{max}} = l_2+l_3`,

      .. math::
          \\begin{aligned}
          l_{\\text{min}} = \\begin{cases} \\kappa(l_2, l_3, m_2, m_3) & \\text{if}\\,
          \\kappa(l_2, l_3, m_2, m_3) + l_{\\text{max}}\\, \\text{is even} \\\\\n          \\kappa(l_2, l_3, m_2, m_3)+1 & \\text{if}\\, \\kappa(l_2, l_3, m_2, m_3) +
          l_{\\text{max}}\\, \\text{is odd}\\end{cases}
          \\end{aligned}

      and `\\kappa(l_2, l_3, m_2, m_3) = \\max{\\big(|l_2-l_3|, \\min{\\big(|m_2+m_3|,
      |m_2-m_3|\\big)}\\big)}`

    - zero for an odd number of negative `m_i`

    Algorithms
    ==========

    This function uses the algorithms of [Homeier96]_ and [Rasch03]_ to
    calculate the value of the real Gaunt coefficient exactly. Note that
    the formula used in [Rasch03]_ contains alternating sums over large
    factorials and is therefore unsuitable for finite precision arithmetic
    and only useful for a computer algebra system [Rasch03]_. However, this
    function can in principle use any algorithm that computes the Gaunt
    coefficient, so it is suitable for finite precision arithmetic in so far
    as the algorithm which computes the Gaunt coefficient is.
    """

class Wigner3j(Function):
    def doit(self, **hints): ...

def dot_rot_grad_Ynm(j, p, l, m, theta, phi):
    '''
    Returns dot product of rotational gradients of spherical harmonics.

    Explanation
    ===========

    This function returns the right hand side of the following expression:

    .. math ::
        \\vec{R}Y{_j^{p}} \\cdot \\vec{R}Y{_l^{m}} = (-1)^{m+p}
        \\sum\\limits_{k=|l-j|}^{l+j}Y{_k^{m+p}}  * \\alpha_{l,m,j,p,k} *
        \\frac{1}{2} (k^2-j^2-l^2+k-j-l)


    Arguments
    =========

    j, p, l, m .... indices in spherical harmonics (expressions or integers)
    theta, phi .... angle arguments in spherical harmonics

    Example
    =======

    >>> from sympy import symbols
    >>> from sympy.physics.wigner import dot_rot_grad_Ynm
    >>> theta, phi = symbols("theta phi")
    >>> dot_rot_grad_Ynm(3, 2, 2, 0, theta, phi).doit()
    3*sqrt(55)*Ynm(5, 2, theta, phi)/(11*sqrt(pi))

    '''
def wigner_d_small(J, beta):
    '''Return the small Wigner d matrix for angular momentum J.

    Explanation
    ===========

    J : An integer, half-integer, or SymPy symbol for the total angular
        momentum of the angular momentum space being rotated.
    beta : A real number representing the Euler angle of rotation about
        the so-called line of nodes. See [Edmonds74]_.

    Returns
    =======

    A matrix representing the corresponding Euler angle rotation( in the basis
    of eigenvectors of `J_z`).

    .. math ::
        \\mathcal{d}_{\\beta} = \\exp\\big( \\frac{i\\beta}{\\hbar} J_y\\big)

    The components are calculated using the general form [Edmonds74]_,
    equation 4.1.15.

    Examples
    ========

    >>> from sympy import Integer, symbols, pi, pprint
    >>> from sympy.physics.wigner import wigner_d_small
    >>> half = 1/Integer(2)
    >>> beta = symbols("beta", real=True)
    >>> pprint(wigner_d_small(half, beta), use_unicode=True)
    ⎡   ⎛β⎞      ⎛β⎞⎤
    ⎢cos⎜─⎟   sin⎜─⎟⎥
    ⎢   ⎝2⎠      ⎝2⎠⎥
    ⎢               ⎥
    ⎢    ⎛β⎞     ⎛β⎞⎥
    ⎢-sin⎜─⎟  cos⎜─⎟⎥
    ⎣    ⎝2⎠     ⎝2⎠⎦

    >>> pprint(wigner_d_small(2*half, beta), use_unicode=True)
    ⎡        2⎛β⎞              ⎛β⎞    ⎛β⎞           2⎛β⎞     ⎤
    ⎢     cos ⎜─⎟        √2⋅sin⎜─⎟⋅cos⎜─⎟        sin ⎜─⎟     ⎥
    ⎢         ⎝2⎠              ⎝2⎠    ⎝2⎠            ⎝2⎠     ⎥
    ⎢                                                        ⎥
    ⎢       ⎛β⎞    ⎛β⎞       2⎛β⎞      2⎛β⎞        ⎛β⎞    ⎛β⎞⎥
    ⎢-√2⋅sin⎜─⎟⋅cos⎜─⎟  - sin ⎜─⎟ + cos ⎜─⎟  √2⋅sin⎜─⎟⋅cos⎜─⎟⎥
    ⎢       ⎝2⎠    ⎝2⎠        ⎝2⎠       ⎝2⎠        ⎝2⎠    ⎝2⎠⎥
    ⎢                                                        ⎥
    ⎢        2⎛β⎞               ⎛β⎞    ⎛β⎞          2⎛β⎞     ⎥
    ⎢     sin ⎜─⎟        -√2⋅sin⎜─⎟⋅cos⎜─⎟       cos ⎜─⎟     ⎥
    ⎣         ⎝2⎠               ⎝2⎠    ⎝2⎠           ⎝2⎠     ⎦

    From table 4 in [Edmonds74]_

    >>> pprint(wigner_d_small(half, beta).subs({beta:pi/2}), use_unicode=True)
    ⎡ √2   √2⎤
    ⎢ ──   ──⎥
    ⎢ 2    2 ⎥
    ⎢        ⎥
    ⎢-√2   √2⎥
    ⎢────  ──⎥
    ⎣ 2    2 ⎦

    >>> pprint(wigner_d_small(2*half, beta).subs({beta:pi/2}),
    ... use_unicode=True)
    ⎡       √2      ⎤
    ⎢1/2    ──   1/2⎥
    ⎢       2       ⎥
    ⎢               ⎥
    ⎢-√2         √2 ⎥
    ⎢────   0    ── ⎥
    ⎢ 2          2  ⎥
    ⎢               ⎥
    ⎢      -√2      ⎥
    ⎢1/2   ────  1/2⎥
    ⎣       2       ⎦

    >>> pprint(wigner_d_small(3*half, beta).subs({beta:pi/2}),
    ... use_unicode=True)
    ⎡ √2    √6    √6   √2⎤
    ⎢ ──    ──    ──   ──⎥
    ⎢ 4     4     4    4 ⎥
    ⎢                    ⎥
    ⎢-√6   -√2    √2   √6⎥
    ⎢────  ────   ──   ──⎥
    ⎢ 4     4     4    4 ⎥
    ⎢                    ⎥
    ⎢ √6   -√2   -√2   √6⎥
    ⎢ ──   ────  ────  ──⎥
    ⎢ 4     4     4    4 ⎥
    ⎢                    ⎥
    ⎢-√2    √6   -√6   √2⎥
    ⎢────   ──   ────  ──⎥
    ⎣ 4     4     4    4 ⎦

    >>> pprint(wigner_d_small(4*half, beta).subs({beta:pi/2}),
    ... use_unicode=True)
    ⎡             √6            ⎤
    ⎢1/4   1/2    ──   1/2   1/4⎥
    ⎢             4             ⎥
    ⎢                           ⎥
    ⎢-1/2  -1/2   0    1/2   1/2⎥
    ⎢                           ⎥
    ⎢ √6                     √6 ⎥
    ⎢ ──    0    -1/2   0    ── ⎥
    ⎢ 4                      4  ⎥
    ⎢                           ⎥
    ⎢-1/2  1/2    0    -1/2  1/2⎥
    ⎢                           ⎥
    ⎢             √6            ⎥
    ⎢1/4   -1/2   ──   -1/2  1/4⎥
    ⎣             4             ⎦

    '''
def wigner_d(J, alpha, beta, gamma):
    '''Return the Wigner D matrix for angular momentum J.

    Explanation
    ===========

    J :
        An integer, half-integer, or SymPy symbol for the total angular
        momentum of the angular momentum space being rotated.
    alpha, beta, gamma - Real numbers representing the Euler.
        Angles of rotation about the so-called vertical, line of nodes, and
        figure axes. See [Edmonds74]_.

    Returns
    =======

    A matrix representing the corresponding Euler angle rotation( in the basis
    of eigenvectors of `J_z`).

    .. math ::
        \\mathcal{D}_{\\alpha \\beta \\gamma} =
        \\exp\\big( \\frac{i\\alpha}{\\hbar} J_z\\big)
        \\exp\\big( \\frac{i\\beta}{\\hbar} J_y\\big)
        \\exp\\big( \\frac{i\\gamma}{\\hbar} J_z\\big)

    The components are calculated using the general form [Edmonds74]_,
    equation 4.1.12.

    Examples
    ========

    The simplest possible example:

    >>> from sympy.physics.wigner import wigner_d
    >>> from sympy import Integer, symbols, pprint
    >>> half = 1/Integer(2)
    >>> alpha, beta, gamma = symbols("alpha, beta, gamma", real=True)
    >>> pprint(wigner_d(half, alpha, beta, gamma), use_unicode=True)
    ⎡  ⅈ⋅α  ⅈ⋅γ             ⅈ⋅α  -ⅈ⋅γ         ⎤
    ⎢  ───  ───             ───  ─────        ⎥
    ⎢   2    2     ⎛β⎞       2     2      ⎛β⎞ ⎥
    ⎢ ℯ   ⋅ℯ   ⋅cos⎜─⎟     ℯ   ⋅ℯ     ⋅sin⎜─⎟ ⎥
    ⎢              ⎝2⎠                    ⎝2⎠ ⎥
    ⎢                                         ⎥
    ⎢  -ⅈ⋅α   ⅈ⋅γ          -ⅈ⋅α   -ⅈ⋅γ        ⎥
    ⎢  ─────  ───          ─────  ─────       ⎥
    ⎢    2     2     ⎛β⎞     2      2      ⎛β⎞⎥
    ⎢-ℯ     ⋅ℯ   ⋅sin⎜─⎟  ℯ     ⋅ℯ     ⋅cos⎜─⎟⎥
    ⎣                ⎝2⎠                   ⎝2⎠⎦

    '''
