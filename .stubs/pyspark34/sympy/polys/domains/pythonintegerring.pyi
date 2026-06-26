from _typeshed import Incomplete
from sympy.polys.domains.groundtypes import PythonInteger as PythonInteger, SymPyInteger as SymPyInteger, python_gcd as python_gcd, python_gcdex as python_gcdex, python_lcm as python_lcm
from sympy.polys.domains.integerring import IntegerRing as IntegerRing
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.utilities import public as public

class PythonIntegerRing(IntegerRing):
    """Integer ring based on Python's ``int`` type.

    This will be used as :ref:`ZZ` if ``gmpy`` and ``gmpy2`` are not
    installed. Elements are instances of the standard Python ``int`` type.
    """
    dtype = PythonInteger
    zero: Incomplete
    one: Incomplete
    alias: str
    def __init__(self) -> None:
        """Allow instantiation of this domain. """
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's Integer to ``dtype``. """
    def from_FF_python(K1, a, K0):
        """Convert ``ModularInteger(int)`` to Python's ``int``. """
    def from_ZZ_python(K1, a, K0):
        """Convert Python's ``int`` to Python's ``int``. """
    def from_QQ(K1, a, K0):
        """Convert Python's ``Fraction`` to Python's ``int``. """
    def from_QQ_python(K1, a, K0):
        """Convert Python's ``Fraction`` to Python's ``int``. """
    def from_FF_gmpy(K1, a, K0):
        """Convert ``ModularInteger(mpz)`` to Python's ``int``. """
    def from_ZZ_gmpy(K1, a, K0):
        """Convert GMPY's ``mpz`` to Python's ``int``. """
    def from_QQ_gmpy(K1, a, K0):
        """Convert GMPY's ``mpq`` to Python's ``int``. """
    def from_RealField(K1, a, K0):
        """Convert mpmath's ``mpf`` to Python's ``int``. """
    def gcdex(self, a, b):
        """Compute extended GCD of ``a`` and ``b``. """
    def gcd(self, a, b):
        """Compute GCD of ``a`` and ``b``. """
    def lcm(self, a, b):
        """Compute LCM of ``a`` and ``b``. """
    def sqrt(self, a):
        """Compute square root of ``a``. """
    def factorial(self, a):
        """Compute factorial of ``a``. """
