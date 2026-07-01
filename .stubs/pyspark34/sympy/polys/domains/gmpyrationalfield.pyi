from _typeshed import Incomplete
from sympy.polys.domains.groundtypes import GMPYRational as GMPYRational, SymPyRational as SymPyRational, gmpy_denom as gmpy_denom, gmpy_numer as gmpy_numer
from sympy.polys.domains.rationalfield import RationalField as RationalField
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.utilities import public as public

class GMPYRationalField(RationalField):
    """Rational field based on GMPY's ``mpq`` type.

    This will be the implementation of :ref:`QQ` if ``gmpy`` or ``gmpy2`` is
    installed. Elements will be of type ``gmpy.mpq``.
    """
    dtype = GMPYRational
    zero: Incomplete
    one: Incomplete
    tp: Incomplete
    alias: str
    def __init__(self) -> None: ...
    def get_ring(self):
        """Returns ring associated with ``self``. """
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's Integer to ``dtype``. """
    def from_ZZ_python(K1, a, K0):
        """Convert a Python ``int`` object to ``dtype``. """
    def from_QQ_python(K1, a, K0):
        """Convert a Python ``Fraction`` object to ``dtype``. """
    def from_ZZ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpz`` object to ``dtype``. """
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpq`` object to ``dtype``. """
    def from_GaussianRationalField(K1, a, K0):
        """Convert a ``GaussianElement`` object to ``dtype``. """
    def from_RealField(K1, a, K0):
        """Convert a mpmath ``mpf`` object to ``dtype``. """
    def exquo(self, a, b):
        """Exact quotient of ``a`` and ``b``, implies ``__truediv__``.  """
    def quo(self, a, b):
        """Quotient of ``a`` and ``b``, implies ``__truediv__``. """
    def rem(self, a, b):
        """Remainder of ``a`` and ``b``, implies nothing.  """
    def div(self, a, b):
        """Division of ``a`` and ``b``, implies ``__truediv__``. """
    def numer(self, a):
        """Returns numerator of ``a``. """
    def denom(self, a):
        """Returns denominator of ``a``. """
    def factorial(self, a):
        """Returns factorial of ``a``. """
