from _typeshed import Incomplete
from sympy.polys.domains.groundtypes import GMPYInteger as GMPYInteger, SymPyInteger as SymPyInteger, gmpy_gcd as gmpy_gcd, gmpy_gcdex as gmpy_gcdex, gmpy_lcm as gmpy_lcm
from sympy.polys.domains.integerring import IntegerRing as IntegerRing
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.utilities import public as public

class GMPYIntegerRing(IntegerRing):
    """Integer ring based on GMPY's ``mpz`` type.

    This will be the implementation of :ref:`ZZ` if ``gmpy`` or ``gmpy2`` is
    installed. Elements will be of type ``gmpy.mpz``.
    """
    dtype = GMPYInteger
    zero: Incomplete
    one: Incomplete
    tp: Incomplete
    alias: str
    def __init__(self) -> None:
        """Allow instantiation of this domain. """
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's Integer to ``dtype``. """
    def from_FF_python(K1, a, K0):
        """Convert ``ModularInteger(int)`` to GMPY's ``mpz``. """
    def from_ZZ_python(K1, a, K0):
        """Convert Python's ``int`` to GMPY's ``mpz``. """
    def from_QQ(K1, a, K0):
        """Convert Python's ``Fraction`` to GMPY's ``mpz``. """
    def from_QQ_python(K1, a, K0):
        """Convert Python's ``Fraction`` to GMPY's ``mpz``. """
    def from_FF_gmpy(K1, a, K0):
        """Convert ``ModularInteger(mpz)`` to GMPY's ``mpz``. """
    def from_ZZ_gmpy(K1, a, K0):
        """Convert GMPY's ``mpz`` to GMPY's ``mpz``. """
    def from_QQ_gmpy(K1, a, K0):
        """Convert GMPY ``mpq`` to GMPY's ``mpz``. """
    def from_RealField(K1, a, K0):
        """Convert mpmath's ``mpf`` to GMPY's ``mpz``. """
    def from_GaussianIntegerRing(K1, a, K0): ...
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
