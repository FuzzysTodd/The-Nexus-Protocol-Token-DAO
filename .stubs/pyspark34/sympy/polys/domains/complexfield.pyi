from _typeshed import Incomplete
from sympy.core.numbers import Float as Float, I as I
from sympy.polys.domains.characteristiczero import CharacteristicZero as CharacteristicZero
from sympy.polys.domains.field import Field as Field
from sympy.polys.domains.mpelements import MPContext as MPContext
from sympy.polys.domains.simpledomain import SimpleDomain as SimpleDomain
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, DomainError as DomainError
from sympy.utilities import public as public

class ComplexField(Field, CharacteristicZero, SimpleDomain):
    """Complex numbers up to the given precision. """
    rep: str
    is_ComplexField: bool
    is_CC: bool
    is_Exact: bool
    is_Numerical: bool
    has_assoc_Ring: bool
    has_assoc_Field: bool
    @property
    def has_default_precision(self): ...
    @property
    def precision(self): ...
    @property
    def dps(self): ...
    @property
    def tolerance(self): ...
    dtype: Incomplete
    zero: Incomplete
    one: Incomplete
    def __init__(self, prec=..., dps: Incomplete | None = None, tol: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def to_sympy(self, element):
        """Convert ``element`` to SymPy number. """
    def from_sympy(self, expr):
        """Convert SymPy's number to ``dtype``. """
    def from_ZZ(self, element, base): ...
    def from_QQ(self, element, base): ...
    def from_ZZ_python(self, element, base): ...
    def from_QQ_python(self, element, base): ...
    def from_ZZ_gmpy(self, element, base): ...
    def from_QQ_gmpy(self, element, base): ...
    def from_GaussianIntegerRing(self, element, base): ...
    def from_GaussianRationalField(self, element, base): ...
    def from_AlgebraicField(self, element, base): ...
    def from_RealField(self, element, base): ...
    def from_ComplexField(self, element, base): ...
    def get_ring(self) -> None:
        """Returns a ring associated with ``self``. """
    def get_exact(self) -> None:
        """Returns an exact domain associated with ``self``. """
    def is_negative(self, element):
        """Returns ``False`` for any ``ComplexElement``. """
    def is_positive(self, element):
        """Returns ``False`` for any ``ComplexElement``. """
    def is_nonnegative(self, element):
        """Returns ``False`` for any ``ComplexElement``. """
    def is_nonpositive(self, element):
        """Returns ``False`` for any ``ComplexElement``. """
    def gcd(self, a, b):
        """Returns GCD of ``a`` and ``b``. """
    def lcm(self, a, b):
        """Returns LCM of ``a`` and ``b``. """
    def almosteq(self, a, b, tolerance: Incomplete | None = None):
        """Check if ``a`` and ``b`` are almost equal. """

CC: Incomplete
