from _typeshed import Incomplete
from sympy.core import Add as Add, Mul as Mul, S as S
from sympy.core.assumptions import StdFactKB as StdFactKB
from sympy.core.decorators import call_highest_priority as call_highest_priority
from sympy.core.expr import Expr as Expr
from sympy.integrals.integrals import Integral as Integral
from sympy.vector.vector import BaseVector as BaseVector

class BasisDependent(Expr):
    """
    Super class containing functionality common to vectors and
    dyadics.
    Named so because the representation of these quantities in
    sympy.vector is dependent on the basis they are expressed in.
    """
    zero: BasisDependentZero
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __neg__(self): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def evalf(self, n: int = 15, subs: Incomplete | None = None, maxn: int = 100, chop: bool = False, strict: bool = False, quad: Incomplete | None = None, verbose: bool = False):
        """
        Implements the SymPy evalf routine for this quantity.

        evalf's documentation
        =====================

        """
    n = evalf
    def simplify(self, **kwargs):
        """
        Implements the SymPy simplify routine for this quantity.

        simplify's documentation
        ========================

        """
    def trigsimp(self, **opts):
        """
        Implements the SymPy trigsimp routine, for this quantity.

        trigsimp's documentation
        ========================

        """
    def as_numer_denom(self):
        """
        Returns the expression as a tuple wrt the following
        transformation -

        expression -> a/b -> a, b

        """
    def factor(self, *args, **kwargs):
        """
        Implements the SymPy factor routine, on the scalar parts
        of a basis-dependent expression.

        factor's documentation
        ========================

        """
    def as_coeff_Mul(self, rational: bool = False):
        """Efficiently extract the coefficient of a product."""
    def as_coeff_add(self, *deps):
        """Efficiently extract the coefficient of a summation."""
    def diff(self, *args, **kwargs):
        """
        Implements the SymPy diff routine, for vectors.

        diff's documentation
        ========================

        """
    def doit(self, **hints):
        """Calls .doit() on each term in the Dyadic"""

class BasisDependentAdd(BasisDependent, Add):
    """
    Denotes sum of basis dependent quantities such that they cannot
    be expressed as base or Mul instances.
    """
    def __new__(cls, *args, **options): ...

class BasisDependentMul(BasisDependent, Mul):
    """
    Denotes product of base- basis dependent quantity with a scalar.
    """
    def __new__(cls, *args, **options): ...

class BasisDependentZero(BasisDependent):
    """
    Class to denote a zero basis dependent instance.
    """
    components: dict['BaseVector', Expr]
    def __new__(cls): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    __req__ = __eq__
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __neg__(self): ...
    def normalize(self):
        """
        Returns the normalized version of this vector.
        """
