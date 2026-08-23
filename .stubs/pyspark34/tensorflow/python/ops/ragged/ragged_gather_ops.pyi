from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_ragged_array_ops as gen_ragged_array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_array_ops as ragged_array_ops, ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor
from tensorflow.python.util import dispatch as dispatch

def gather(params: ragged_tensor.RaggedOrDense, indices: ragged_tensor.RaggedOrDense, validate_indices: Incomplete | None = None, axis: Incomplete | None = None, batch_dims: int = 0, name: Incomplete | None = None):
    """Gathers ragged slices from `params` axis `0` according to `indices`.

  See `tf.gather` for full documentation.  (This version has the same API
  as `tf.gather`, but supports ragged `params` and `indices`.)

  Examples:

  >>> params = tf.constant(['a', 'b', 'c', 'd', 'e'])
  >>> indices = tf.constant([3, 1, 2, 1, 0])
  >>> ragged_params = tf.ragged.constant([['a', 'b', 'c'], ['d'], [], ['e']])
  >>> ragged_indices = tf.ragged.constant([[3, 1, 2], [1], [], [0]])

  >>> tf.gather(params, ragged_indices)
  <tf.RaggedTensor [[b'd', b'b', b'c'], [b'b'], [], [b'a']]>

  >>> tf.gather(ragged_params, indices)
  <tf.RaggedTensor [[b'e'], [b'd'], [], [b'd'], [b'a', b'b', b'c']]>

  >>> tf.gather(ragged_params, ragged_indices)
  <tf.RaggedTensor [[[b'e'], [b'd'], []], [[b'd']], [], [[b'a', b'b', b'c']]]>

  Args:
    params: The potentially ragged tensor from which to gather values. Must be
      at least rank 1.
    indices: The potentially ragged tensor indicating which values to gather.
      Must have dtype `int32` or `int64`.  Values must be in the range `[0,
      params.shape[0]]`.
    validate_indices: Ignored.
    axis: The axis in `params` to gather `indices` from.
    batch_dims: The number of batch dimensions.
    name: A name for the operation (optional).

  Returns:
    A `RaggedTensor`, where `output.dtype=params.dtype` and
    `output.shape=indices.shape + params.shape[1:]` and
    `output.ragged_rank=indices.shape.ndims + params.ragged_rank`.

  Raises:
    ValueError: If indices.shape.ndims is not known statically.
  """
def gather_nd(params: ragged_tensor.RaggedOrDense, indices: ragged_tensor.RaggedOrDense, batch_dims: int = 0, name: Incomplete | None = None):
    """Gather slices from `params` using `n`-dimensional indices.

  This operation is similar to `gather`, but it uses the innermost dimension
  of `indices` to define a slice into `params`.  In particular, if:

  * `indices` has shape `[A1...AN, I]`
  * `params` has shape `[B1...BM]`

  Then:

  * `result` has shape `[A1...AN, B_{I+1}...BM]`.
  * `result[a1...aN] = params[indices[a1...aN, :]]`

  Args:
    params: A potentially ragged tensor with shape `[A1...AN, I]`.
    indices: A potentially ragged tensor with shape `[B1...BM]`.
    batch_dims: Must be zero.
    name: A name for the operation (optional).

  Returns:
    A potentially ragged tensor with shape `[A1...AN, B_{I+1}...BM]`.

  #### Examples:

  >>> params = tf.ragged.constant(
  ...     [ [ ['000', '001'], ['010'              ]          ],
  ...       [ ['100'       ], ['110', '111', '112'], ['120'] ],
  ...       [ [            ], ['210'              ]          ] ])

  >>> # Gather 2D slices from a 3D tensor
  >>> tf.gather_nd(params, [[2], [0]])
  <tf.RaggedTensor [[[], [b'210']], [[b'000', b'001'], [b'010']]]>

  >>> # Gather 1D slices from a 3D tensor
  >>> tf.gather_nd(params, [[2, 1], [0, 0]])
  <tf.RaggedTensor [[b'210'], [b'000', b'001']]>

  >>> # Gather scalars from a 3D tensor
  >>> tf.gather_nd(params, [[0, 0, 1], [1, 1, 2]]).numpy()
  array([b'001', b'112'], dtype=object)
  """
