from sympy.physics.quantum import Bra, Ket, Operator

__all__ = ['BosonOp', 'BosonFockKet', 'BosonFockBra', 'BosonCoherentKet', 'BosonCoherentBra']

class BosonOp(Operator):
    '''A bosonic operator that satisfies [a, Dagger(a)] == 1.

    Parameters
    ==========

    name : str
        A string that labels the bosonic mode.

    annihilation : bool
        A bool that indicates if the bosonic operator is an annihilation (True,
        default value) or creation operator (False)

    Examples
    ========

    >>> from sympy.physics.quantum import Dagger, Commutator
    >>> from sympy.physics.quantum.boson import BosonOp
    >>> a = BosonOp("a")
    >>> Commutator(a, Dagger(a)).doit()
    1
    '''
    @property
    def name(self): ...
    @property
    def is_annihilation(self): ...
    @classmethod
    def default_args(self): ...
    def __new__(cls, *args, **hints): ...
    def __mul__(self, other): ...

class BosonFockKet(Ket):
    """Fock state ket for a bosonic mode.

    Parameters
    ==========

    n : Number
        The Fock state number.

    """
    def __new__(cls, n): ...
    @property
    def n(self): ...
    @classmethod
    def dual_class(self): ...

class BosonFockBra(Bra):
    """Fock state bra for a bosonic mode.

    Parameters
    ==========

    n : Number
        The Fock state number.

    """
    def __new__(cls, n): ...
    @property
    def n(self): ...
    @classmethod
    def dual_class(self): ...

class BosonCoherentKet(Ket):
    """Coherent state ket for a bosonic mode.

    Parameters
    ==========

    alpha : Number, Symbol
        The complex amplitude of the coherent state.

    """
    def __new__(cls, alpha): ...
    @property
    def alpha(self): ...
    @classmethod
    def dual_class(self): ...

class BosonCoherentBra(Bra):
    """Coherent state bra for a bosonic mode.

    Parameters
    ==========

    alpha : Number, Symbol
        The complex amplitude of the coherent state.

    """
    def __new__(cls, alpha): ...
    @property
    def alpha(self): ...
    @classmethod
    def dual_class(self): ...
