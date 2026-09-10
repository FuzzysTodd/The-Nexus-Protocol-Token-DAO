from sympy.polys.domains.finitefield import FiniteField as FiniteField
from sympy.polys.domains.gmpyintegerring import GMPYIntegerRing as GMPYIntegerRing
from sympy.utilities import public as public

class GMPYFiniteField(FiniteField):
    """Finite field based on GMPY integers. """
    alias: str
    def __init__(self, mod, symmetric: bool = True) -> None: ...
