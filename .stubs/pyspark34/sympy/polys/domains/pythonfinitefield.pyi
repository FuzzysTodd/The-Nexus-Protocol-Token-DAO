from sympy.polys.domains.finitefield import FiniteField as FiniteField
from sympy.polys.domains.pythonintegerring import PythonIntegerRing as PythonIntegerRing
from sympy.utilities import public as public

class PythonFiniteField(FiniteField):
    """Finite field based on Python's integers. """
    alias: str
    def __init__(self, mod, symmetric: bool = True) -> None: ...
