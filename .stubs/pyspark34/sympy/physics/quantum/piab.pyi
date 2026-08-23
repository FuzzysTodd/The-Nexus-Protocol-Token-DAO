from sympy.physics.quantum.operator import HermitianOperator
from sympy.physics.quantum.state import Bra, Ket

__all__ = ['PIABHamiltonian', 'PIABKet', 'PIABBra']

class PIABHamiltonian(HermitianOperator):
    """Particle in a box Hamiltonian operator."""

class PIABKet(Ket):
    """Particle in a box eigenket."""
    @classmethod
    def dual_class(self): ...

class PIABBra(Bra):
    """Particle in a box eigenbra."""
    @classmethod
    def dual_class(self): ...
