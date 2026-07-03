from _typeshed import Incomplete
from sympy.core.expr import Expr

__all__ = ['CG', 'Wigner3j', 'Wigner6j', 'Wigner9j', 'cg_simp']

class Wigner3j(Expr):
    """Class for the Wigner-3j symbols.

    Explanation
    ===========

    Wigner 3j-symbols are coefficients determined by the coupling of
    two angular momenta. When created, they are expressed as symbolic
    quantities that, for numerical parameters, can be evaluated using the
    ``.doit()`` method [1]_.

    Parameters
    ==========

    j1, m1, j2, m2, j3, m3 : Number, Symbol
        Terms determining the angular momentum of coupled angular momentum
        systems.

    Examples
    ========

    Declare a Wigner-3j coefficient and calculate its value

        >>> from sympy.physics.quantum.cg import Wigner3j
        >>> w3j = Wigner3j(6,0,4,0,2,0)
        >>> w3j
        Wigner3j(6, 0, 4, 0, 2, 0)
        >>> w3j.doit()
        sqrt(715)/143

    See Also
    ========

    CG: Clebsch-Gordan coefficients

    References
    ==========

    .. [1] Varshalovich, D A, Quantum Theory of Angular Momentum. 1988.
    """
    is_commutative: bool
    def __new__(cls, j1, m1, j2, m2, j3, m3): ...
    @property
    def j1(self): ...
    @property
    def m1(self): ...
    @property
    def j2(self): ...
    @property
    def m2(self): ...
    @property
    def j3(self): ...
    @property
    def m3(self): ...
    @property
    def is_symbolic(self): ...
    def doit(self, **hints): ...

class CG(Wigner3j):
    """Class for Clebsch-Gordan coefficient.

    Explanation
    ===========

    Clebsch-Gordan coefficients describe the angular momentum coupling between
    two systems. The coefficients give the expansion of a coupled total angular
    momentum state and an uncoupled tensor product state. The Clebsch-Gordan
    coefficients are defined as [1]_:

    .. math ::
        C^{j_3,m_3}_{j_1,m_1,j_2,m_2} = \\left\\langle j_1,m_1;j_2,m_2 | j_3,m_3\\right\\rangle

    Parameters
    ==========

    j1, m1, j2, m2 : Number, Symbol
        Angular momenta of states 1 and 2.

    j3, m3: Number, Symbol
        Total angular momentum of the coupled system.

    Examples
    ========

    Define a Clebsch-Gordan coefficient and evaluate its value

        >>> from sympy.physics.quantum.cg import CG
        >>> from sympy import S
        >>> cg = CG(S(3)/2, S(3)/2, S(1)/2, -S(1)/2, 1, 1)
        >>> cg
        CG(3/2, 3/2, 1/2, -1/2, 1, 1)
        >>> cg.doit()
        sqrt(3)/2
        >>> CG(j1=S(1)/2, m1=-S(1)/2, j2=S(1)/2, m2=+S(1)/2, j3=1, m3=0).doit()
        sqrt(2)/2


    Compare [2]_.

    See Also
    ========

    Wigner3j: Wigner-3j symbols

    References
    ==========

    .. [1] Varshalovich, D A, Quantum Theory of Angular Momentum. 1988.
    .. [2] `Clebsch-Gordan Coefficients, Spherical Harmonics, and d Functions
        <https://pdg.lbl.gov/2020/reviews/rpp2020-rev-clebsch-gordan-coefs.pdf>`_
        in P.A. Zyla *et al.* (Particle Data Group), Prog. Theor. Exp. Phys.
        2020, 083C01 (2020).
    """
    precedence: Incomplete
    def doit(self, **hints): ...

class Wigner6j(Expr):
    """Class for the Wigner-6j symbols

    See Also
    ========

    Wigner3j: Wigner-3j symbols

    """
    def __new__(cls, j1, j2, j12, j3, j, j23): ...
    @property
    def j1(self): ...
    @property
    def j2(self): ...
    @property
    def j12(self): ...
    @property
    def j3(self): ...
    @property
    def j(self): ...
    @property
    def j23(self): ...
    @property
    def is_symbolic(self): ...
    def doit(self, **hints): ...

class Wigner9j(Expr):
    """Class for the Wigner-9j symbols

    See Also
    ========

    Wigner3j: Wigner-3j symbols

    """
    def __new__(cls, j1, j2, j12, j3, j4, j34, j13, j24, j): ...
    @property
    def j1(self): ...
    @property
    def j2(self): ...
    @property
    def j12(self): ...
    @property
    def j3(self): ...
    @property
    def j4(self): ...
    @property
    def j34(self): ...
    @property
    def j13(self): ...
    @property
    def j24(self): ...
    @property
    def j(self): ...
    @property
    def is_symbolic(self): ...
    def doit(self, **hints): ...

def cg_simp(e):
    """Simplify and combine CG coefficients.

    Explanation
    ===========

    This function uses various symmetry and properties of sums and
    products of Clebsch-Gordan coefficients to simplify statements
    involving these terms [1]_.

    Examples
    ========

    Simplify the sum over CG(a,alpha,0,0,a,alpha) for all alpha to
    2*a+1

        >>> from sympy.physics.quantum.cg import CG, cg_simp
        >>> a = CG(1,1,0,0,1,1)
        >>> b = CG(1,0,0,0,1,0)
        >>> c = CG(1,-1,0,0,1,-1)
        >>> cg_simp(a+b+c)
        3

    See Also
    ========

    CG: Clebsh-Gordan coefficients

    References
    ==========

    .. [1] Varshalovich, D A, Quantum Theory of Angular Momentum. 1988.
    """
