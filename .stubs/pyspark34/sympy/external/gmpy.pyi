from .pythonmpq import PythonMPQ
from _typeshed import Incomplete
from typing import Tuple as tTuple, Type

__all__ = ['GROUND_TYPES', 'HAS_GMPY', 'SYMPY_INTS', 'MPQ', 'MPZ', 'factorial', 'sqrt']

GROUND_TYPES: Incomplete
SYMPY_INTS: tTuple[Type, ...]
HAS_GMPY: int
MPZ: Incomplete
MPQ: Incomplete
factorial: Incomplete
sqrt: Incomplete
MPZ = int
MPQ = PythonMPQ
