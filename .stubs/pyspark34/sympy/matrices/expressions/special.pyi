from .matexpr import MatrixExpr as MatrixExpr
from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.matrices.common import NonInvertibleMatrixError as NonInvertibleMatrixError

class ZeroMatrix(MatrixExpr):
    """The Matrix Zero 0 - additive identity

    Examples
    ========

    >>> from sympy import MatrixSymbol, ZeroMatrix
    >>> A = MatrixSymbol('A', 3, 5)
    >>> Z = ZeroMatrix(3, 5)
    >>> A + Z
    A
    >>> Z*A.T
    0
    """
    is_ZeroMatrix: bool
    def __new__(cls, m, n): ...
    @property
    def shape(self): ...

class GenericZeroMatrix(ZeroMatrix):
    """
    A zero matrix without a specified shape

    This exists primarily so MatAdd() with no arguments can return something
    meaningful.
    """
    def __new__(cls): ...
    @property
    def rows(self) -> None: ...
    @property
    def cols(self) -> None: ...
    @property
    def shape(self) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class Identity(MatrixExpr):
    """The Matrix Identity I - multiplicative identity

    Examples
    ========

    >>> from sympy import Identity, MatrixSymbol
    >>> A = MatrixSymbol('A', 3, 5)
    >>> I = Identity(3)
    >>> I*A
    A
    """
    is_Identity: bool
    def __new__(cls, n): ...
    @property
    def rows(self): ...
    @property
    def cols(self): ...
    @property
    def shape(self): ...
    @property
    def is_square(self): ...

class GenericIdentity(Identity):
    """
    An identity matrix without a specified shape

    This exists primarily so MatMul() with no arguments can return something
    meaningful.
    """
    def __new__(cls): ...
    @property
    def rows(self) -> None: ...
    @property
    def cols(self) -> None: ...
    @property
    def shape(self) -> None: ...
    @property
    def is_square(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class OneMatrix(MatrixExpr):
    """
    Matrix whose all entries are ones.
    """
    def __new__(cls, m, n, evaluate: bool = False): ...
    @property
    def shape(self): ...
    @property
    def is_Identity(self): ...
    def as_explicit(self): ...
    def doit(self, **hints): ...
