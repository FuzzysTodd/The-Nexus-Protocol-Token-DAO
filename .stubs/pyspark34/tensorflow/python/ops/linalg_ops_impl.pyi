from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.util import compat as compat

def eye(num_rows, num_columns: Incomplete | None = None, batch_shape: Incomplete | None = None, dtype=..., name: Incomplete | None = None):
    """Construct an identity matrix, or a batch of matrices.

  See `linalg_ops.eye`.
  """
