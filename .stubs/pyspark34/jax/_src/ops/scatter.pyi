import numpy as np
from collections.abc import Sequence
from jax import config as config, lax as lax
from jax._src import core as core, dtypes as dtypes, util as util
from jax._src.numpy import reductions as reductions
from jax._src.numpy.util import check_arraylike as check_arraylike, promote_dtypes as promote_dtypes
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from types import EllipsisType

SingleIndex = None | int | slice | Sequence[int] | Array | EllipsisType
Index = SingleIndex | tuple[SingleIndex, ...]
Scalar = complex | float | int | np.number

def segment_sum(data: ArrayLike, segment_ids: ArrayLike, num_segments: int | None = None, indices_are_sorted: bool = False, unique_indices: bool = False, bucket_size: int | None = None, mode: lax.GatherScatterMode | None = None) -> Array:
    """Computes the sum within segments of an array.

  Similar to TensorFlow's `segment_sum
  <https://www.tensorflow.org/api_docs/python/tf/math/segment_sum>`_

  Args:
    data: an array with the values to be summed.
    segment_ids: an array with integer dtype that indicates the segments of
      `data` (along its leading axis) to be summed. Values can be repeated and
      need not be sorted.
    num_segments: optional, an int with nonnegative value indicating the number
      of segments. The default is set to be the minimum number of segments that
      would support all indices in ``segment_ids``, calculated as
      ``max(segment_ids) + 1``.
      Since `num_segments` determines the size of the output, a static value
      must be provided to use ``segment_sum`` in a JIT-compiled function.
    indices_are_sorted: whether ``segment_ids`` is known to be sorted.
    unique_indices: whether `segment_ids` is known to be free of duplicates.
    bucket_size: size of bucket to group indices into. ``segment_sum`` is
      performed on each bucket separately to improve numerical stability of
      addition. Default ``None`` means no bucketing.
    mode: a :class:`jax.lax.GatherScatterMode` value describing how
      out-of-bounds indices should be handled. By default, values outside of the
      range [0, num_segments) are dropped and do not contribute to the sum.

  Returns:
    An array with shape :code:`(num_segments,) + data.shape[1:]` representing the
    segment sums.

  Examples:
    Simple 1D segment sum:

    >>> data = jnp.arange(5)
    >>> segment_ids = jnp.array([0, 0, 1, 1, 2])
    >>> segment_sum(data, segment_ids)
    Array([1, 5, 4], dtype=int32)

    Using JIT requires static `num_segments`:

    >>> from jax import jit
    >>> jit(segment_sum, static_argnums=2)(data, segment_ids, 3)
    Array([1, 5, 4], dtype=int32)
  """
def segment_prod(data: ArrayLike, segment_ids: ArrayLike, num_segments: int | None = None, indices_are_sorted: bool = False, unique_indices: bool = False, bucket_size: int | None = None, mode: lax.GatherScatterMode | None = None) -> Array:
    """Computes the product within segments of an array.

  Similar to TensorFlow's `segment_prod
  <https://www.tensorflow.org/api_docs/python/tf/math/segment_prod>`_

  Args:
    data: an array with the values to be reduced.
    segment_ids: an array with integer dtype that indicates the segments of
      `data` (along its leading axis) to be reduced. Values can be repeated and
      need not be sorted. Values outside of the range [0, num_segments) are
      dropped and do not contribute to the result.
    num_segments: optional, an int with nonnegative value indicating the number
      of segments. The default is set to be the minimum number of segments that
      would support all indices in ``segment_ids``, calculated as
      ``max(segment_ids) + 1``.
      Since `num_segments` determines the size of the output, a static value
      must be provided to use ``segment_prod`` in a JIT-compiled function.
    indices_are_sorted: whether ``segment_ids`` is known to be sorted.
    unique_indices: whether `segment_ids` is known to be free of duplicates.
    bucket_size: size of bucket to group indices into. ``segment_prod`` is
      performed on each bucket separately to improve numerical stability of
      addition. Default ``None`` means no bucketing.
    mode: a :class:`jax.lax.GatherScatterMode` value describing how
      out-of-bounds indices should be handled. By default, values outside of the
      range [0, num_segments) are dropped and do not contribute to the sum.

  Returns:
    An array with shape :code:`(num_segments,) + data.shape[1:]` representing the
    segment products.

  Examples:
    Simple 1D segment product:

    >>> data = jnp.arange(6)
    >>> segment_ids = jnp.array([0, 0, 1, 1, 2, 2])
    >>> segment_prod(data, segment_ids)
    Array([ 0,  6, 20], dtype=int32)

    Using JIT requires static `num_segments`:

    >>> from jax import jit
    >>> jit(segment_prod, static_argnums=2)(data, segment_ids, 3)
    Array([ 0,  6, 20], dtype=int32)
  """
def segment_max(data: ArrayLike, segment_ids: ArrayLike, num_segments: int | None = None, indices_are_sorted: bool = False, unique_indices: bool = False, bucket_size: int | None = None, mode: lax.GatherScatterMode | None = None) -> Array:
    """Computes the maximum within segments of an array.

  Similar to TensorFlow's `segment_max
  <https://www.tensorflow.org/api_docs/python/tf/math/segment_max>`_

  Args:
    data: an array with the values to be reduced.
    segment_ids: an array with integer dtype that indicates the segments of
      `data` (along its leading axis) to be reduced. Values can be repeated and
      need not be sorted. Values outside of the range [0, num_segments) are
      dropped and do not contribute to the result.
    num_segments: optional, an int with nonnegative value indicating the number
      of segments. The default is set to be the minimum number of segments that
      would support all indices in ``segment_ids``, calculated as
      ``max(segment_ids) + 1``.
      Since `num_segments` determines the size of the output, a static value
      must be provided to use ``segment_max`` in a JIT-compiled function.
    indices_are_sorted: whether ``segment_ids`` is known to be sorted.
    unique_indices: whether `segment_ids` is known to be free of duplicates.
    bucket_size: size of bucket to group indices into. ``segment_max`` is
      performed on each bucket separately. Default ``None`` means no bucketing.
    mode: a :class:`jax.lax.GatherScatterMode` value describing how
      out-of-bounds indices should be handled. By default, values outside of the
      range [0, num_segments) are dropped and do not contribute to the sum.

  Returns:
    An array with shape :code:`(num_segments,) + data.shape[1:]` representing the
    segment maximums.

  Examples:
    Simple 1D segment max:

    >>> data = jnp.arange(6)
    >>> segment_ids = jnp.array([0, 0, 1, 1, 2, 2])
    >>> segment_max(data, segment_ids)
    Array([1, 3, 5], dtype=int32)

    Using JIT requires static `num_segments`:

    >>> from jax import jit
    >>> jit(segment_max, static_argnums=2)(data, segment_ids, 3)
    Array([1, 3, 5], dtype=int32)
  """
def segment_min(data: ArrayLike, segment_ids: ArrayLike, num_segments: int | None = None, indices_are_sorted: bool = False, unique_indices: bool = False, bucket_size: int | None = None, mode: lax.GatherScatterMode | None = None) -> Array:
    """Computes the minimum within segments of an array.

  Similar to TensorFlow's `segment_min
  <https://www.tensorflow.org/api_docs/python/tf/math/segment_min>`_

  Args:
    data: an array with the values to be reduced.
    segment_ids: an array with integer dtype that indicates the segments of
      `data` (along its leading axis) to be reduced. Values can be repeated and
      need not be sorted. Values outside of the range [0, num_segments) are
      dropped and do not contribute to the result.
    num_segments: optional, an int with nonnegative value indicating the number
      of segments. The default is set to be the minimum number of segments that
      would support all indices in ``segment_ids``, calculated as
      ``max(segment_ids) + 1``.
      Since `num_segments` determines the size of the output, a static value
      must be provided to use ``segment_min`` in a JIT-compiled function.
    indices_are_sorted: whether ``segment_ids`` is known to be sorted.
    unique_indices: whether `segment_ids` is known to be free of duplicates.
    bucket_size: size of bucket to group indices into. ``segment_min`` is
      performed on each bucket separately. Default ``None`` means no bucketing.
    mode: a :class:`jax.lax.GatherScatterMode` value describing how
      out-of-bounds indices should be handled. By default, values outside of the
      range [0, num_segments) are dropped and do not contribute to the sum.

  Returns:
    An array with shape :code:`(num_segments,) + data.shape[1:]` representing the
    segment minimums.

  Examples:
    Simple 1D segment min:

    >>> data = jnp.arange(6)
    >>> segment_ids = jnp.array([0, 0, 1, 1, 2, 2])
    >>> segment_min(data, segment_ids)
    Array([0, 2, 4], dtype=int32)

    Using JIT requires static `num_segments`:

    >>> from jax import jit
    >>> jit(segment_min, static_argnums=2)(data, segment_ids, 3)
    Array([0, 2, 4], dtype=int32)
  """
