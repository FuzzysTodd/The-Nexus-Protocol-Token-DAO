from _typeshed import Incomplete
from tensorflow.python.data.experimental.ops.cardinality import assert_cardinality as assert_cardinality
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import lookup_ops as lookup_ops, math_ops as math_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class DatasetInitializer(lookup_ops.TableInitializerBase):
    '''Creates a table initializer from a `tf.data.Dataset`.

  Sample usage:

  >>> keys = tf.data.Dataset.range(100)
  >>> values = tf.data.Dataset.range(100).map(
  ...     lambda x: tf.strings.as_string(x * 2))
  >>> ds = tf.data.Dataset.zip((keys, values))
  >>> init = tf.data.experimental.DatasetInitializer(ds)
  >>> table = tf.lookup.StaticHashTable(init, "")
  >>> table.lookup(tf.constant([0, 1, 2], dtype=tf.int64)).numpy()
  array([b\'0\', b\'2\', b\'4\'], dtype=object)

  Attributes:
    dataset: A `tf.data.Dataset` object that produces tuples of scalars. The
      first scalar is treated as a key and the second as value.
  Raises: ValueError if `dataset` doesn\'t conform to specifications.
  '''
    dataset: Incomplete
    def __init__(self, dataset) -> None:
        """Creates a table initializer from a `tf.data.Dataset`.

    Args:
      dataset: A `tf.data.Dataset` object that produces tuples of scalars. The
        first scalar is treated as a key and the second as value.
    Raises: ValueError if `dataset` doesn't conform to specifications.
    Returns: A `DatasetInitializer` object
    """
    def initialize(self, table): ...

def table_from_dataset(dataset: Incomplete | None = None, num_oov_buckets: int = 0, vocab_size: Incomplete | None = None, default_value: Incomplete | None = None, hasher_spec=..., key_dtype=..., name: Incomplete | None = None):
    """Returns a lookup table based on the given dataset.

  This operation constructs a lookup table based on the given dataset of pairs
  of (key, value).

  Any lookup of an out-of-vocabulary token will return a bucket ID based on its
  hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
  `default_value`.
  The bucket ID range is
  `[vocabulary size, vocabulary size + num_oov_buckets - 1]`.

  Sample Usages:

  >>> keys = tf.data.Dataset.range(100)
  >>> values = tf.data.Dataset.range(100).map(
  ...     lambda x: tf.strings.as_string(x * 2))
  >>> ds = tf.data.Dataset.zip((keys, values))
  >>> table = tf.data.experimental.table_from_dataset(
  ...                               ds, default_value='n/a', key_dtype=tf.int64)
  >>> table.lookup(tf.constant([0, 1, 2], dtype=tf.int64)).numpy()
  array([b'0', b'2', b'4'], dtype=object)

  Args:
    dataset: A dataset containing (key, value) pairs.
    num_oov_buckets: The number of out-of-vocabulary buckets.
    vocab_size: Number of the elements in the vocabulary, if known.
    default_value: The value to use for out-of-vocabulary feature values.
      Defaults to -1.
    hasher_spec: A `HasherSpec` to specify the hash function to use for
      assignation of out-of-vocabulary buckets.
    key_dtype: The `key` data type.
    name: A name for this op (optional).

  Returns:
    The lookup table based on the given dataset.

  Raises:
    ValueError: If
      * `dataset` does not contain pairs
      * The 2nd item in the `dataset` pairs has a dtype which is incompatible
        with `default_value`
      * `num_oov_buckets` is negative
      * `vocab_size` is not greater than zero
      * The `key_dtype` is not integer or string
  """
def index_table_from_dataset(dataset: Incomplete | None = None, num_oov_buckets: int = 0, vocab_size: Incomplete | None = None, default_value: int = -1, hasher_spec=..., key_dtype=..., name: Incomplete | None = None):
    """Returns an index lookup table based on the given dataset.

  This operation constructs a lookup table based on the given dataset of keys.

  Any lookup of an out-of-vocabulary token will return a bucket ID based on its
  hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
  `default_value`.
  The bucket ID range is
  `[vocabulary size, vocabulary size + num_oov_buckets - 1]`.

  Sample Usages:

  >>> ds = tf.data.Dataset.range(100).map(lambda x: tf.strings.as_string(x * 2))
  >>> table = tf.data.experimental.index_table_from_dataset(
  ...                                     ds, key_dtype=dtypes.int64)
  >>> table.lookup(tf.constant(['0', '2', '4'], dtype=tf.string)).numpy()
  array([0, 1, 2])

  Args:
    dataset: A dataset of keys.
    num_oov_buckets: The number of out-of-vocabulary buckets.
    vocab_size: Number of the elements in the vocabulary, if known.
    default_value: The value to use for out-of-vocabulary feature values.
      Defaults to -1.
    hasher_spec: A `HasherSpec` to specify the hash function to use for
      assignation of out-of-vocabulary buckets.
    key_dtype: The `key` data type.
    name: A name for this op (optional).

  Returns:
    The lookup table based on the given dataset.

  Raises:
    ValueError: If
      * `num_oov_buckets` is negative
      * `vocab_size` is not greater than zero
      * The `key_dtype` is not integer or string
  """
