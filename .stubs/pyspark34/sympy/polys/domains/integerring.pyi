from _typeshed import Incomplete
from sympy.external.gmpy import HAS_GMPY as HAS_GMPY, MPZ as MPZ
from sympy.polys.domains.characteristiczero import CharacteristicZero as CharacteristicZero
from sympy.polys.domains.groundtypes import SymPyInteger as SymPyInteger, factorial as factorial, gcd as gcd, gcdex as gcdex, lcm as lcm, sqrt as sqrt
from sympy.polys.domains.ring import Ring as Ring
from sympy.polys.domains.simpledomain import SimpleDomain as SimpleDomain
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.utilities import public as public

class IntegerRing(Ring, CharacteristicZero, SimpleDomain):
    """The domain ``ZZ`` representing the integers `\\mathbb{Z}`.

    The :py:class:`IntegerRing` class represents the ring of integers as a
    :py:class:`~.Domain` in the domain system. :py:class:`IntegerRing` is a
    super class of :py:class:`PythonIntegerRing` and
    :py:class:`GMPYIntegerRing` one of which will be the implementation for
    :ref:`ZZ` depending on whether or not ``gmpy`` or ``gmpy2`` is installed.

    See also
    ========

    Domain
    """
    rep: str
    alias: str
    dtype = MPZ
    zero: Incomplete
    one: Incomplete
    tp: Incomplete
    is_IntegerRing: bool
    is_ZZ: bool
    is_Numerical: bool
    is_PID: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    def __init__(self) -> None:
        """Allow instantiation of this domain. """
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
    def from_sympy(self, a):
        """Convert SymPy's Integer to ``dtype``. """
    def get_field(self):
        """Return the associated field of fractions :ref:`QQ`

        Returns
        =======

        :ref:`QQ`:
            The associated field of fractions :ref:`QQ`, a
            :py:class:`~.Domain` representing the rational numbers
            `\\mathbb{Q}`.

        Examples
        ========

        >>> from sympy import ZZ
        >>> ZZ.get_field()
        QQ
        """
    def algebraic_field(self, *extension, alias: Incomplete | None = None):
        """Returns an algebraic field, i.e. `\\mathbb{Q}(\\alpha, \\ldots)`.

        Parameters
        ==========

        *extension : One or more :py:class:`~.Expr`.
            Generators of the extension. These should be expressions that are
            algebraic over `\\mathbb{Q}`.

        alias : str, :py:class:`~.Symbol`, None, optional (default=None)
            If provided, this will be used as the alias symbol for the
            primitive element of the returned :py:class:`~.AlgebraicField`.

        Returns
        =======

        :py:class:`~.AlgebraicField`
            A :py:class:`~.Domain` representing the algebraic field extension.

        Examples
        ========

        >>> from sympy import ZZ, sqrt
        >>> ZZ.algebraic_field(sqrt(2))
        QQ<sqrt(2)>
        """
    def from_AlgebraicField(K1, a, K0):
        """Convert a :py:class:`~.ANP` object to :ref:`ZZ`.

        See :py:meth:`~.Domain.convert`.
        """
    def log(self, a, b):
        """Logarithm of *a* to the base *b*.

        Parameters
        ==========

        a: number
        b: number

        Returns
        =======

        $\\\\lfloor\\log(a, b)\\\\rfloor$:
            Floor of the logarithm of *a* to the base *b*

        Examples
        ========

        >>> from sympy import ZZ
        >>> ZZ.log(ZZ(8), ZZ(2))
        3
        >>> ZZ.log(ZZ(9), ZZ(2))
        3

        Notes
        =====

        This function uses ``math.log`` which is based on ``float`` so it will
        fail for large integer arguments.
        """
    def from_FF(K1, a, K0):
        """Convert ``ModularInteger(int)`` to GMPY's ``mpz``. """
    def from_FF_python(K1, a, K0):
        """Convert ``ModularInteger(int)`` to GMPY's ``mpz``. """
    def from_ZZ(K1, a, K0):
        """Convert Python's ``int`` to GMPY's ``mpz``. """
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

ZZ: Incomplete
