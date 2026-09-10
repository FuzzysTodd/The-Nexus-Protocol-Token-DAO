from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import Tuple

def is_sparse(A):
    """Check if tensor A is a sparse tensor"""
def get_floating_dtype(A):
    """Return the floating point dtype of tensor A.

    Integer types map to float32.
    """
def matmul(A: Tensor | None, B: Tensor) -> Tensor:
    """Multiply two matrices.

    If A is None, return B. A can be sparse or dense. B is always
    dense.
    """
def conjugate(A):
    """Return conjugate of tensor A.

    .. note:: If A's dtype is not complex, A is returned.
    """
def transpose(A):
    """Return transpose of a matrix or batches of matrices."""
def transjugate(A):
    """Return transpose conjugate of a matrix or batches of matrices."""
def bform(X: Tensor, A: Tensor | None, Y: Tensor) -> Tensor:
    """Return bilinear form of matrices: :math:`X^T A Y`."""
def qform(A: Tensor | None, S: Tensor):
    """Return quadratic form :math:`S^T A S`."""
def basis(A):
    """Return orthogonal basis of A columns."""
def symeig(A: Tensor, largest: bool | None = False) -> Tuple[Tensor, Tensor]:
    """Return eigenpairs of A with specified ordering."""
def matrix_rank(input, tol: Incomplete | None = None, symmetric: bool = False, *, out: Incomplete | None = None) -> Tensor: ...
def solve(input: Tensor, A: Tensor, *, out: Incomplete | None = None) -> Tuple[Tensor, Tensor]: ...
def lstsq(input: Tensor, A: Tensor, *, out: Incomplete | None = None) -> Tuple[Tensor, Tensor]: ...
def eig(self, eigenvectors: bool = False, *, e: Incomplete | None = None, v: Incomplete | None = None) -> Tuple[Tensor, Tensor]: ...
