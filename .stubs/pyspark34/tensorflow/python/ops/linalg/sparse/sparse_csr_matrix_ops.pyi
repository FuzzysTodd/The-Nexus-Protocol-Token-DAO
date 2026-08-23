from tensorflow.python.ops.linalg.sparse.gen_sparse_csr_matrix_ops import *
import abc
from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['SparseMatrix', 'CSRSparseMatrix', 'matmul', 'dense_shape_and_type']

class DenseShapeAndType(NamedTuple('DenseShapeAndType', [('shape', Incomplete), ('dtype', Incomplete)])): ...

def dense_shape_and_type(matrix):
    """Get dense shape and dtype of the tf.Tensor containing the matrix.

  Args:
    matrix: A `tf.Tensor` of type `tf.variant` storing a sparse matrix.

  Returns:
    An instance of `ShapeAndType` with properties `shape` (a `tf.TensorShape`)
    and `dtype` (a `tf.DType`).

  Raises:
    TypeError: if `matrix` is not a tensor or its dtype is not variant.
    ValueError: if `matrix` lacks static handle data containing the dense
      shape and dtype.
  """
def matmul(a, b, transpose_a: bool = False, transpose_b: bool = False, adjoint_a: bool = False, adjoint_b: bool = False, name: Incomplete | None = None):
    """Perform a sparse matrix matmul between `a` and `b`.

  Performs a contraction between `a` and `b` along the two innermost dimensions.
  If both `a` and `b` are instances of `SparseMatrix`, returns a new instance
  of `SparseMatrix` (same type as `a`).  If one is not an instance of
  `SparseMatrix`, returns a dense `Tensor`:

  ```
  c = opA(a) . opB(b)
  ```
  where `opA` (resp. `opB`) is the transpose or hermitian transpose depending
  on the values of `transpose_a` (resp. `transpose_b`) and `adjoint_a`
  (resp. `adjoint_b`).

  Args:
    a: `Tensor` or `SparseMatrix`, having rank `2` or `3`.
    b: `Tensor` or `SparseMatrix`, having rank `2` or `3`.
    transpose_a: Python `bool`.
    transpose_b: Python `bool`.
    adjoint_a: Python `bool`.
    adjoint_b: Python `bool`.
    name: Optional name to use when creating ops.

  Returns:
    A `SparseMatrix` if both `a` and `b` are instances of `SparseMatrix`,
    otherwise a dense `Tensor`.
  """

class SparseMatrix(metaclass=abc.ABCMeta):
    """Abstract class for sparse matrix types."""
    @abc.abstractmethod
    def __init__(self): ...
    @abc.abstractmethod
    def to_dense(self): ...
    @abc.abstractmethod
    def to_sparse_tensor(self): ...
    @property
    def graph(self): ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    @property
    def eager_handle_data(self):
        """Return the matrix's handle data iff in eager mode."""
    def conj(self): ...
    def hermitian_transpose(self):
        """Return the hermitian transpose of the matrix."""
    def nnz(self):
        """Number of stored values, including explicit zeros."""
    nonzero = nnz
    def sorted_indices(self): ...
    def transpose(self): ...

class CSRSparseMatrix(SparseMatrix):
    """(Optionally batched) CSR Sparse Matrix."""
    def __init__(self, value, indices: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Construct a CSRSparseMatrix from a dense matrix or SparseTensor.

    Args:
      value: A dense `2D` or `3D` Tensor or `SparseTensor`.
      indices: The nonzero indices of `value`
        (if `value` is not a `SparseTensor`).
      name: Optional op name.

    Raises:
      ValueError: if `value` is a `SparseTensor` and `indices` is not `None`.
    """
    def to_dense(self): ...
    def to_sparse_tensor(self): ...
