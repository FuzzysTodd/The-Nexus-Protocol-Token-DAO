from .exceptions import DMNonInvertibleMatrixError as DMNonInvertibleMatrixError, DMNonSquareMatrixError as DMNonSquareMatrixError, DMShapeError as DMShapeError
from sympy.polys.matrices._typing import RingElement as RingElement
from typing import Sequence, TypeVar

T = TypeVar('T')
R = TypeVar('R', bound=RingElement)

def ddm_transpose(matrix: Sequence[Sequence[T]]) -> list[list[T]]:
    """matrix transpose"""
def ddm_iadd(a: list[list[R]], b: Sequence[Sequence[R]]) -> None:
    """a += b"""
def ddm_isub(a: list[list[R]], b: Sequence[Sequence[R]]) -> None:
    """a -= b"""
def ddm_ineg(a: list[list[R]]) -> None:
    """a  <--  -a"""
def ddm_imul(a: list[list[R]], b: R) -> None: ...
def ddm_irmul(a: list[list[R]], b: R) -> None: ...
def ddm_imatmul(a: list[list[R]], b: Sequence[Sequence[R]], c: Sequence[Sequence[R]]) -> None:
    """a += b @ c"""
def ddm_irref(a, _partial_pivot: bool = False):
    """a  <--  rref(a)"""
def ddm_idet(a, K):
    """a  <--  echelon(a); return det"""
def ddm_iinv(ainv, a, K) -> None: ...
def ddm_ilu_split(L, U, K):
    """L, U  <--  LU(U)"""
def ddm_ilu(a):
    """a  <--  LU(a)"""
def ddm_ilu_solve(x, L, U, swaps, b) -> None:
    """x  <--  solve(L*U*x = swaps(b))"""
def ddm_berk(M, K): ...
