from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def random_index_shuffle(index, seed, max_index, rounds: int = 4, name: Incomplete | None = None):
    """Outputs the position of `value` in a permutation of [0, ..., max_index].

  Output values are a bijection of the `index` for any combination and `seed` and `max_index`.

  If multiple inputs are vectors (matrix in case of seed) then the size of the
  first dimension must match.

  The outputs are deterministic.

  Args:
    index: A `Tensor`. Must be one of the following types: `int32`, `uint32`, `int64`, `uint64`.
      A scalar tensor or a vector of dtype `dtype`. The index (or indices) to be shuffled. Must be within [0, max_index].
    seed: A `Tensor`. Must be one of the following types: `int32`, `uint32`, `int64`, `uint64`.
      A tensor of dtype `Tseed` and shape [3] or [n, 3]. The random seed.
    max_index: A `Tensor`. Must have the same type as `index`.
      A scalar tensor or vector of dtype `dtype`. The upper bound(s) of the interval (inclusive).
    rounds: An optional `int`. Defaults to `4`.
      The number of rounds to use the in block cipher.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `index`.
  """

RandomIndexShuffle: Incomplete

def random_index_shuffle_eager_fallback(index, seed, max_index, rounds, name, ctx): ...
