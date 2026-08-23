from tensorflow.python.ops.gen_lookup_ops import *
from _typeshed import Incomplete
from tensorflow.python.checkpoint import saveable_compat as saveable_compat
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_lookup_ops as gen_lookup_ops, math_ops as math_ops, string_ops as string_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.saved_model import registration as registration
from tensorflow.python.trackable import asset as asset, base as trackable_base, resource as resource
from tensorflow.python.training.saver import BaseSaverBuilder as BaseSaverBuilder
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def initialize_all_tables(name: str = 'init_all_tables'):
    """Returns an Op that initializes all tables of the default graph.

  Args:
    name: Optional name for the initialization op.

  Returns:
    An Op that initializes all tables.  Note that if there are
    not tables the returned Op is a NoOp.
  """
def tables_initializer(name: str = 'init_all_tables'):
    """Returns an Op that initializes all tables of the default graph.

  Args:
    name: Optional name for the initialization op.

  Returns:
    An Op that initializes all tables.  Note that if there are
    not tables the returned Op is a NoOp.

  @compatibility(TF2)
  `tf.compat.v1.tables_initializer` is no longer needed with eager execution and
  `tf.function`. In TF2, when creating an initializable table like a
  `tf.lookup.StaticHashTable`, the table will automatically be initialized on
  creation.

  #### Before & After Usage Example

  Before:

  >>> with tf.compat.v1.Session():
  ...   init = tf.compat.v1.lookup.KeyValueTensorInitializer(['a', 'b'], [1, 2])
  ...   table = tf.compat.v1.lookup.StaticHashTable(init, default_value=-1)
  ...   tf.compat.v1.tables_initializer().run()
  ...   result = table.lookup(tf.constant(['a', 'c'])).eval()
  >>> result
  array([ 1, -1], dtype=int32)

  After:

  >>> init = tf.lookup.KeyValueTensorInitializer(['a', 'b'], [1, 2])
  >>> table = tf.lookup.StaticHashTable(init, default_value=-1)
  >>> table.lookup(tf.constant(['a', 'c'])).numpy()
  array([ 1, -1], dtype=int32)

  @end_compatibility
  """
def check_table_dtypes(table, key_dtype, value_dtype) -> None:
    """Check that the given key_dtype and value_dtype matches the table dtypes.

  Args:
    table: The table to check types against to.
    key_dtype: The key data type to check.
    value_dtype: The value data type to check.

  Raises:
    TypeError: when 'key_dtype' or 'value_dtype' doesn't match the table data
      types.
  """

class LookupInterface(resource.TrackableResource):
    """Represent a lookup table that persists across different steps."""
    def __init__(self, key_dtype, value_dtype) -> None:
        """Construct a lookup table interface.

    Args:
      key_dtype: The table key type.
      value_dtype: The table value type.
    """
    @property
    def key_dtype(self):
        """The table key dtype."""
    @property
    def value_dtype(self):
        """The table value dtype."""
    @property
    def name(self):
        """The name of the table."""
    def size(self, name: Incomplete | None = None) -> None:
        """Compute the number of elements in this table."""
    def lookup(self, keys, name: Incomplete | None = None) -> None:
        """Looks up `keys` in a table, outputs the corresponding values."""
    def __getitem__(self, keys):
        """Looks up `keys` in a table, outputs the corresponding values."""

class InitializableLookupTableBase(LookupInterface):
    """Initializable lookup table interface.

  An initializable lookup tables persist across different steps.
  """
    def __init__(self, default_value, initializer) -> None:
        """Construct a table object from a table reference.

    If requires a table initializer object (subclass of `TableInitializerBase`).
    It provides the table key and value types, as well as the op to initialize
    the table. The caller is responsible to execute the initialization op.

    Args:
      default_value: The value to use if a key is missing in the table.
      initializer: The table initializer to use.
    """
    @property
    def default_value(self):
        """The default value of the table."""
    def size(self, name: Incomplete | None = None):
        """Compute the number of elements in this table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A scalar tensor containing the number of elements in this table.
    """
    def lookup(self, keys, name: Incomplete | None = None):
        """Looks up `keys` in a table, outputs the corresponding values.

    The `default_value` is used for keys not present in the table.

    Args:
      keys: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
      name: A name for the operation (optional).

    Returns:
      A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged,
      otherwise a dense `Tensor`.

    Raises:
      TypeError: when `keys` or `default_value` doesn't match the table data
        types.
    """

class InitializableLookupTableBaseV1(InitializableLookupTableBase):
    @property
    def initializer(self): ...

class StaticHashTable(InitializableLookupTableBase):
    """A generic hash table that is immutable once initialized.

  Example usage:

  >>> keys_tensor = tf.constant(['a', 'b', 'c'])
  >>> vals_tensor = tf.constant([7, 8, 9])
  >>> input_tensor = tf.constant(['a', 'f'])
  >>> table = tf.lookup.StaticHashTable(
  ...     tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor),
  ...     default_value=-1)
  >>> table.lookup(input_tensor).numpy()
  array([ 7, -1], dtype=int32)

  Or for more pythonic code:

  >>> table[input_tensor].numpy()
  array([ 7, -1], dtype=int32)

  The result of a lookup operation has the same shape as the argument:

  >>> input_tensor = tf.constant([['a', 'b'], ['c', 'd']])
  >>> table[input_tensor].numpy()
  array([[ 7,  8],
         [ 9, -1]], dtype=int32)


  """
    def __init__(self, initializer, default_value, name: Incomplete | None = None, experimental_is_anonymous: bool = False) -> None:
        """Creates a non-initialized `HashTable` object.

    Creates a table, the type of its keys and values are specified by the
    initializer.
    Before using the table you will have to initialize it. After initialization
    the table will be immutable.

    Args:
      initializer: The table initializer to use. See `HashTable` kernel for
        supported key and value types.
      default_value: The value to use if a key is missing in the table.
      name: A name for the operation (optional).
      experimental_is_anonymous: Whether to use anonymous mode for the
        table (default is False). In anonymous mode, the table
        resource can only be accessed via a resource handle. It can't
        be looked up by a name. When all resource handles pointing to
        that resource are gone, the resource will be deleted
        automatically.

    Returns:
      A `HashTable` object.
    """
    @property
    def name(self): ...
    def export(self, name: Incomplete | None = None):
        """Returns tensors of all keys and values in the table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A pair of tensors with the first tensor containing all keys and the
        second tensors containing all values in the table.
    """

class StaticHashTableV1(StaticHashTable):
    '''A generic hash table that is immutable once initialized.

  When running in graph mode, you must evaluate the tensor returned by
  `tf.tables_initializer()` before evaluating the tensor returned by
  this class\'s `lookup()` method. Example usage in graph mode:

  ```python
  keys_tensor = tf.constant([1, 2])
  vals_tensor = tf.constant([3, 4])
  input_tensor = tf.constant([1, 5])
  table = tf.lookup.StaticHashTable(
      tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1)
  out = table.lookup(input_tensor)
  with tf.Session() as sess:
      sess.run(tf.tables_initializer())
      print(sess.run(out))
  ```

  Note that in graph mode if you set `experimental_is_anonymous` to
  `True`, you should only call `Session.run` once, otherwise each
  `Session.run` will create (and destroy) a new table unrelated to
  each other, leading to errors such as "Table not initialized".
  You can do so like this:

  ```python
  keys_tensor = tf.constant([1, 2])
  vals_tensor = tf.constant([3, 4])
  input_tensor = tf.constant([1, 5])
  table = tf.lookup.StaticHashTable(
      tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1,
      experimental_is_anonymous=True)
  with tf.control_dependencies([tf.tables_initializer()]):
    out = table.lookup(input_tensor)
  with tf.Session() as sess:
    print(sess.run(out))
  ```

  In eager mode, no special code is needed to initialize the table.
  Example usage in eager mode:

  ```python
  tf.enable_eager_execution()
  keys_tensor = tf.constant([1, 2])
  vals_tensor = tf.constant([3, 4])
  input_tensor = tf.constant([1, 5])
  table = tf.lookup.StaticHashTable(
      tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor), -1)
  print(table.lookup(input_tensor))
  ```
  '''
    @property
    def initializer(self): ...

class HashTable(StaticHashTableV1):
    @property
    def init(self): ...

class TableInitializerBase(trackable_base.Trackable):
    """Base class for lookup table initializers."""
    def __init__(self, key_dtype, value_dtype) -> None:
        """Construct a table initializer object.

    Args:
      key_dtype: Type of the table keys.
      value_dtype: Type of the table values.
    """
    @property
    def key_dtype(self):
        """The expected table key dtype."""
    @property
    def value_dtype(self):
        """The expected table value dtype."""
    def initialize(self, table) -> None:
        """Returns the table initialization op."""

class KeyValueTensorInitializer(TableInitializerBase):
    """Table initializers given `keys` and `values` tensors.

  >>> keys_tensor = tf.constant(['a', 'b', 'c'])
  >>> vals_tensor = tf.constant([7, 8, 9])
  >>> input_tensor = tf.constant(['a', 'f'])
  >>> init = tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor)
  >>> table = tf.lookup.StaticHashTable(
  ...     init,
  ...     default_value=-1)
  >>> table.lookup(input_tensor).numpy()
  array([ 7, -1], dtype=int32)

  """
    def __init__(self, keys, values, key_dtype: Incomplete | None = None, value_dtype: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Constructs a table initializer object based on keys and values tensors.

    Args:
      keys: The tensor for the keys.
      values: The tensor for the values.
      key_dtype: The `keys` data type. Used when `keys` is a python array.
      value_dtype: The `values` data type. Used when `values` is a python array.
      name: A name for the operation (optional).
    """
    def initialize(self, table):
        """Initializes the given `table` with `keys` and `values` tensors.

    Args:
      table: The table to initialize.

    Returns:
      The operation that initializes the table.

    Raises:
      TypeError: when the keys and values data types do not match the table
      key and value data types.
    """

class TextFileIndex:
    """The key and value content to get from each line.

  This class defines the key and value used for `tf.lookup.TextFileInitializer`.

  The key and value content to get from each line is specified either
  by the following, or a value `>=0`.
  * `TextFileIndex.LINE_NUMBER` means use the line number starting from zero,
    expects data type int64.
  * `TextFileIndex.WHOLE_LINE` means use the whole line content, expects data
    type string.

  A value `>=0` means use the index (starting at zero) of the split line based
      on `delimiter`.
  """
    WHOLE_LINE: int
    LINE_NUMBER: int

class TextFileInitializer(TableInitializerBase):
    '''Table initializers from a text file.

  This initializer assigns one entry in the table for each line in the file.

  The key and value type of the table to initialize is given by `key_dtype` and
  `value_dtype`.

  The key and value content to get from each line is specified by
  the `key_index` and `value_index`.

  * `TextFileIndex.LINE_NUMBER` means use the line number starting from zero,
    expects data type int64.
  * `TextFileIndex.WHOLE_LINE` means use the whole line content, expects data
    type string.
  * A value `>=0` means use the index (starting at zero) of the split line based
      on `delimiter`.

  For example if we have a file with the following content:

  >>> import tempfile
  >>> f = tempfile.NamedTemporaryFile(delete=False)
  >>> content=\'\\n\'.join(["emerson 10", "lake 20", "palmer 30",])
  >>> f.file.write(content.encode(\'utf-8\'))
  >>> f.file.close()

  The following snippet initializes a table with the first column as keys and
  second column as values:

  * `emerson -> 10`
  * `lake -> 20`
  * `palmer -> 30`

  >>> init= tf.lookup.TextFileInitializer(
  ...    filename=f.name,
  ...    key_dtype=tf.string, key_index=0,
  ...    value_dtype=tf.int64, value_index=1,
  ...    delimiter=" ")
  >>> table = tf.lookup.StaticHashTable(init, default_value=-1)
  >>> table.lookup(tf.constant([\'palmer\',\'lake\',\'tarkus\'])).numpy()

  Similarly to initialize the whole line as keys and the line number as values.

  * `emerson 10 -> 0`
  * `lake 20 -> 1`
  * `palmer 30 -> 2`

  >>> init = tf.lookup.TextFileInitializer(
  ...   filename=f.name,
  ...   key_dtype=tf.string, key_index=tf.lookup.TextFileIndex.WHOLE_LINE,
  ...   value_dtype=tf.int64, value_index=tf.lookup.TextFileIndex.LINE_NUMBER)
  >>> table = tf.lookup.StaticHashTable(init, -1)
  >>> table.lookup(tf.constant(\'palmer 30\')).numpy()
  2
  '''
    def __init__(self, filename, key_dtype, key_index, value_dtype, value_index, vocab_size: Incomplete | None = None, delimiter: str = '\t', name: Incomplete | None = None, value_index_offset: int = 0) -> None:
        """Constructs a table initializer object to populate from a text file.

    It generates one key-value pair per line. The type of table key and
    value are specified by `key_dtype` and `value_dtype`, respectively.
    Similarly the content of the key and value are specified by the key_index
    and value_index.

    - TextFileIndex.LINE_NUMBER means use the line number starting from zero,
      expects data type int64.
    - TextFileIndex.WHOLE_LINE means use the whole line content, expects data
      type string or int64.
    - A value >=0 means use the index (starting at zero) of the split line based
      on `delimiter`.

    Args:
      filename: The filename of the text file to be used for initialization. The
        path must be accessible from wherever the graph is initialized (eg.
        trainer or eval workers). The filename may be a scalar `Tensor`.
      key_dtype: The `key` data type.
      key_index: the index that represents information of a line to get the
        table 'key' values from.
      value_dtype: The `value` data type.
      value_index: the index that represents information of a line to get the
        table 'value' values from.'
      vocab_size: The number of elements in the file, if known.
      delimiter: The delimiter to separate fields in a line.
      name: A name for the operation (optional).
      value_index_offset: A number to add to all indices extracted from the file
        This is useful for cases where a user would like to reserve one or more
        low index values for control characters. For instance, if you would
        like to ensure that no vocabulary item is mapped to index 0 (so you can
        reserve 0 for a masking value), you can set value_index_offset to 1;
        this will mean that the first vocabulary element is mapped to 1
        instead of 0.

    Raises:
      ValueError: when the filename is empty, or when the table key and value
      data types do not match the expected data types.
    """
    def initialize(self, table):
        """Initializes the table from a text file.

    Args:
      table: The table to be initialized.

    Returns:
      The operation that initializes the table.

    Raises:
      TypeError: when the keys and values data types do not match the table
      key and value data types.
    """

class TextFileStringTableInitializer(TextFileInitializer):
    """Table initializer for `int64` IDs to string tables from a text file."""
    def __init__(self, filename, key_column_index=..., value_column_index=..., vocab_size: Incomplete | None = None, delimiter: str = '\t', name: str = 'text_file_string_table_init') -> None:
        """Constructs an initializer for an id-to-string table from a text file.

    It populates a table that its key and value types are int64 and string,
    respectively. It generates one key-value pair per line.
    The content of the key and value are specified by `key_column_index`
    and `value_column_index`.

    - TextFileIndex.LINE_NUMBER means use the line number starting from zero,
      expects data type int64.
    - TextFileIndex.WHOLE_LINE means use the whole line content, expects data
      type string or int64.
    - A value >=0 means use the index (starting at zero) of the split line based
      on `delimiter`.

    Args:
      filename: The filename of the text file to be used for initialization. The
        path must be accessible from wherever the graph is initialized (eg.
        trainer or eval workers). The filename may be a scalar `Tensor`.
      key_column_index: The column index from the text file to get the keys
        from. The default is to use the line number, starting from zero.
      value_column_index: The column index from the text file to get the values
        from. The default is to use the whole line content.
      vocab_size: The number of elements in the file, if known.
      delimiter: The delimiter to separate fields in a line.
      name: Optional name for the op.

    Raises:
      TypeError: when the filename is empty, or when the table key and value
      data types do not match the expected data types.
    """

class TextFileIdTableInitializer(TextFileInitializer):
    """Table initializer for string to `int64` IDs tables from a text file."""
    def __init__(self, filename, key_column_index=..., value_column_index=..., vocab_size: Incomplete | None = None, delimiter: str = '\t', name: str = 'text_file_id_table_init', key_dtype=...) -> None:
        """Constructs an initializer for an string-to-id table from a text file.

    It populates a table that its key and value types are string and int64,
    respectively. It generates one key-value pair per line.
    The content of the key and value are specified by the key_index
    and value_index.

    - TextFileIndex.LINE_NUMBER means use the line number starting from zero,
      expects data type int64.
    - TextFileIndex.WHOLE_LINE means use the whole line content, expects data
      type string.
    - A value >=0 means use the index (starting at zero) of the split line based
      on `delimiter`.

    Args:
      filename: The filename of the text file to be used for initialization. The
        path must be accessible from wherever the graph is initialized (eg.
        trainer or eval workers). The filename may be a scalar `Tensor`.
      key_column_index: The column index from the text file to get the `key`
        values from. The default is to use the whole line content.
      value_column_index: The column index from the text file to get the `value`
        values from. The default is to use the line number, starting from zero.
      vocab_size: The number of elements in the file, if known.
      delimiter: The delimiter to separate fields in a line.
      name: Optional name for the op.
      key_dtype: The `key` data type.

    Raises:
      TypeError: when the filename is empty, or when the table key and value
      data types do not match the expected data types.
    """

class HasherSpec(NamedTuple('HasherSpec', [('hasher', Incomplete), ('key', Incomplete)])):
    '''A structure for the spec of the hashing function to use for hash buckets.

  `hasher` is the name of the hashing function to use (eg. "fasthash",
  "stronghash").
  `key` is optional and specify the key to use for the hash function if
  supported, currently only used by a strong hash.

  Fields:
    hasher: The hasher name to use.
    key: The key to be used by the hashing function, if required.
  '''

FastHashSpec: Incomplete

class StrongHashSpec(HasherSpec):
    """A structure to specify a key of the strong keyed hash spec.

  The strong hash requires a `key`, which is a list of 2 unsigned integer
  numbers. These should be non-zero; random numbers generated from random.org
  would be a fine choice.

  Fields:
    key: The key to be used by the keyed hashing function.
  """
    def __new__(cls, key): ...

class IdTableWithHashBuckets(LookupInterface):
    '''String to Id table wrapper that assigns out-of-vocabulary keys to buckets.

  For example, if an instance of `IdTableWithHashBuckets` is initialized with a
  string-to-id table that maps:

  * `emerson -> 0`
  * `lake -> 1`
  * `palmer -> 2`

  The `IdTableWithHashBuckets` object will performs the following mapping:

  * `emerson -> 0`
  * `lake -> 1`
  * `palmer -> 2`
  * `<other term> -> bucket_id`, where bucket_id will be between `3` and
  `3 + num_oov_buckets - 1`, calculated by:
  `hash(<term>) % num_oov_buckets + vocab_size`

  If input_tensor is `["emerson", "lake", "palmer", "king", "crimson"]`,
  the lookup result is `[0, 1, 2, 4, 7]`.

  If `table` is None, only out-of-vocabulary buckets are used.

  Example usage:

  ```python
  num_oov_buckets = 3
  input_tensor = tf.constant(["emerson", "lake", "palmer", "king", "crimnson"])
  table = tf.IdTableWithHashBuckets(
      tf.StaticHashTable(
          tf.lookup.TextFileInitializer(
              filename,
              key_dtype=tf.string,
              key_index=tf.lookup.TextFileIndex.WHOLE_LINE,
              value_dtype=tf.int64,
              value_index=tf.lookup.TextFileIndex.LINE_NUMBER,
              delimiter="\\t"),
          default_value),
      num_oov_buckets)
  out = table.lookup(input_tensor).
  table.init.run()
  print(out.eval())
  ```

  The hash function used for generating out-of-vocabulary buckets ID is handled
  by `hasher_spec`.
  '''
    def __init__(self, table, num_oov_buckets, hasher_spec=..., name: Incomplete | None = None, key_dtype: Incomplete | None = None) -> None:
        """Construct a `IdTableWithHashBuckets` object.

    Args:
      table: Table that maps `tf.string` or `tf.int64` keys to `tf.int64` ids.
      num_oov_buckets: Number of buckets to use for out-of-vocabulary keys.
      hasher_spec: A `HasherSpec` to specify the hash function to use for
        assignation of out-of-vocabulary buckets  (optional).
      name: A name for the operation (optional).
      key_dtype: Data type of keys passed to `lookup`. Defaults to
        `table.key_dtype` if `table` is specified, otherwise `tf.string`. Must
        be string or integer, and must be castable to `table.key_dtype`.

    Raises:
      ValueError: when `table` in None and `num_oov_buckets` is not positive.
      TypeError: when `hasher_spec` is invalid.
    """
    @property
    def initializer(self): ...
    @property
    def init(self): ...
    @property
    def resource_handle(self): ...
    @property
    def name(self): ...
    def size(self, name: Incomplete | None = None):
        """Compute the number of elements in this table."""
    def lookup(self, keys, name: Incomplete | None = None):
        """Looks up `keys` in the table, outputs the corresponding values.

    It assigns out-of-vocabulary keys to buckets based in their hashes.

    Args:
      keys: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
      name: Optional name for the op.

    Returns:
      A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged,
      otherwise a dense `Tensor`.

    Raises:
      TypeError: when `keys` doesn't match the table key data type.
    """

class StaticVocabularyTable(LookupInterface):
    '''String to Id table that assigns out-of-vocabulary keys to hash buckets.

  For example, if an instance of `StaticVocabularyTable` is initialized with a
  string-to-id initializer that maps:

  >>> init = tf.lookup.KeyValueTensorInitializer(
  ...     keys=tf.constant([\'emerson\', \'lake\', \'palmer\']),
  ...     values=tf.constant([0, 1, 2], dtype=tf.int64))
  >>> table = tf.lookup.StaticVocabularyTable(
  ...    init,
  ...    num_oov_buckets=5)

  The `Vocabulary` object will performs the following mapping:

  * `emerson -> 0`
  * `lake -> 1`
  * `palmer -> 2`
  * `<other term> -> bucket_id`, where `bucket_id` will be between `3` and
  `3 + num_oov_buckets - 1 = 7`, calculated by:
  `hash(<term>) % num_oov_buckets + vocab_size`

  If input_tensor is:

  >>> input_tensor = tf.constant(["emerson", "lake", "palmer",
  ...                             "king", "crimson"])
  >>> table[input_tensor].numpy()
  array([0, 1, 2, 6, 7])

  If `initializer` is None, only out-of-vocabulary buckets are used.

  Example usage:

  >>> num_oov_buckets = 3
  >>> vocab = ["emerson", "lake", "palmer", "crimnson"]
  >>> import tempfile
  >>> f = tempfile.NamedTemporaryFile(delete=False)
  >>> f.write(\'\\n\'.join(vocab).encode(\'utf-8\'))
  >>> f.close()

  >>> init = tf.lookup.TextFileInitializer(
  ...     f.name,
  ...     key_dtype=tf.string, key_index=tf.lookup.TextFileIndex.WHOLE_LINE,
  ...     value_dtype=tf.int64, value_index=tf.lookup.TextFileIndex.LINE_NUMBER)
  >>> table = tf.lookup.StaticVocabularyTable(init, num_oov_buckets)
  >>> table.lookup(tf.constant(["palmer", "crimnson" , "king",
  ...                           "tarkus", "black", "moon"])).numpy()
  array([2, 3, 5, 6, 6, 4])

  The hash function used for generating out-of-vocabulary buckets ID is
  Fingerprint64.

  Note that the out-of-vocabulary bucket IDs always range from the table `size`
  up to `size + num_oov_buckets - 1` regardless of the table values, which could
  cause unexpected collisions:

  >>> init = tf.lookup.KeyValueTensorInitializer(
  ...     keys=tf.constant(["emerson", "lake", "palmer"]),
  ...     values=tf.constant([1, 2, 3], dtype=tf.int64))
  >>> table = tf.lookup.StaticVocabularyTable(
  ...     init,
  ...     num_oov_buckets=1)
  >>> input_tensor = tf.constant(["emerson", "lake", "palmer", "king"])
  >>> table[input_tensor].numpy()
  array([1, 2, 3, 3])
  '''
    def __init__(self, initializer, num_oov_buckets, lookup_key_dtype: Incomplete | None = None, name: Incomplete | None = None, experimental_is_anonymous: bool = False) -> None:
        """Construct a `StaticVocabularyTable` object.

    Args:
      initializer: A `TableInitializerBase` object that contains the data used
        to initialize the table. If None, then we only use out-of-vocab buckets.
      num_oov_buckets: Number of buckets to use for out-of-vocabulary keys. Must
        be greater than zero. If out-of-vocab buckets are not required, use
        `StaticHashTable` instead.
      lookup_key_dtype: Data type of keys passed to `lookup`. Defaults to
        `initializer.key_dtype` if `initializer` is specified, otherwise
        `tf.string`. Must be string or integer, and must be castable to
        `initializer.key_dtype`.
      name: A name for the operation (optional).
      experimental_is_anonymous: Whether to use anonymous mode for the
        table (default is False). In anonymous mode, the table
        resource can only be accessed via a resource handle. It can't
        be looked up by a name. When all resource handles pointing to
        that resource are gone, the resource will be deleted
        automatically.

    Raises:
      ValueError: when `num_oov_buckets` is not positive.
      TypeError: when lookup_key_dtype or initializer.key_dtype are not
        integer or string. Also when initializer.value_dtype != int64.
    """
    @property
    def resource_handle(self): ...
    @property
    def name(self): ...
    def size(self, name: Incomplete | None = None):
        """Compute the number of elements in this table."""
    def lookup(self, keys, name: Incomplete | None = None):
        """Looks up `keys` in the table, outputs the corresponding values.

    It assigns out-of-vocabulary keys to buckets based in their hashes.

    Args:
      keys: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
      name: Optional name for the op.

    Returns:
      A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged,
      otherwise a dense `Tensor`.

    Raises:
      TypeError: when `keys` doesn't match the table key data type.
    """

class StaticVocabularyTableV1(StaticVocabularyTable):
    @property
    def initializer(self): ...

def index_table_from_file(vocabulary_file: Incomplete | None = None, num_oov_buckets: int = 0, vocab_size: Incomplete | None = None, default_value: int = -1, hasher_spec=..., key_dtype=..., name: Incomplete | None = None, key_column_index=..., value_column_index=..., delimiter: str = '\t'):
    '''Returns a lookup table that converts a string tensor into int64 IDs.

  This operation constructs a lookup table to convert tensor of strings into
  int64 IDs. The mapping can be initialized from a vocabulary file specified in
  `vocabulary_file`, where the whole line is the key and the zero-based line
  number is the ID.

  Any lookup of an out-of-vocabulary token will return a bucket ID based on its
  hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
  `default_value`.
  The bucket ID range is
  `[vocabulary size, vocabulary size + num_oov_buckets - 1]`.

  The underlying table must be initialized by calling
  `session.run(tf.compat.v1.tables_initializer())` or
  `session.run(table.init())` once.

  To specify multi-column vocabulary files, use key_column_index and
  value_column_index and delimiter.

  - TextFileIndex.LINE_NUMBER means use the line number starting from zero,
    expects data type int64.
  - TextFileIndex.WHOLE_LINE means use the whole line content, expects data
    type string.
  - A value >=0 means use the index (starting at zero) of the split line based
    on `delimiter`.

  Sample Usages:

  If we have a vocabulary file "test.txt" with the following content:

  ```
  emerson
  lake
  palmer
  ```

  ```python
  features = tf.constant(["emerson", "lake", "and", "palmer"])
  table = tf.lookup.index_table_from_file(
      vocabulary_file="test.txt", num_oov_buckets=1)
  ids = table.lookup(features)
  ...
  tf.compat.v1.tables_initializer().run()

  ids.eval()  ==> [0, 1, 3, 2]  # where 3 is the out-of-vocabulary bucket
  ```

  Args:
    vocabulary_file: The vocabulary filename, may be a constant scalar `Tensor`.
    num_oov_buckets: The number of out-of-vocabulary buckets.
    vocab_size: Number of the elements in the vocabulary, if known.
    default_value: The value to use for out-of-vocabulary feature values.
      Defaults to -1.
    hasher_spec: A `HasherSpec` to specify the hash function to use for
      assignation of out-of-vocabulary buckets.
    key_dtype: The `key` data type.
    name: A name for this op (optional).
    key_column_index: The column index from the text file to get the `key`
      values from. The default is to use the whole line content.
    value_column_index: The column index from the text file to get the `value`
      values from. The default is to use the line number, starting from zero.
    delimiter: The delimiter to separate fields in a line.

  Returns:
    The lookup table to map a `key_dtype` `Tensor` to index `int64` `Tensor`.

  Raises:
    ValueError: If `vocabulary_file` is not set.
    ValueError: If `num_oov_buckets` is negative or `vocab_size` is not greater
      than zero.
  '''
def index_table_from_tensor(vocabulary_list, num_oov_buckets: int = 0, default_value: int = -1, hasher_spec=..., dtype=..., name: Incomplete | None = None):
    '''Returns a lookup table that converts a string tensor into int64 IDs.

  This operation constructs a lookup table to convert tensor of strings into
  int64 IDs. The mapping can be initialized from a string `vocabulary_list` 1-D
  tensor where each element is a key and corresponding index within the tensor
  is the value.

  Any lookup of an out-of-vocabulary token will return a bucket ID based on its
  hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
  `default_value`. The bucket ID range is
  `[vocabulary list size, vocabulary list size + num_oov_buckets - 1]`.

  The underlying table must be initialized by calling
  `session.run(tf.compat.v1.tables_initializer())` or
  `session.run(table.init())` once.

  Elements in `vocabulary_list` cannot have duplicates, otherwise when executing
  the table initializer op, it will throw a `FailedPreconditionError`.

  Sample Usages:

  ```python
  vocabulary_list = tf.constant(["emerson", "lake", "palmer"])
  table = tf.lookup.index_table_from_tensor(
      vocabulary_list=vocabulary_list, num_oov_buckets=1, default_value=-1)
  features = tf.constant(["emerson", "lake", "and", "palmer"])
  ids = table.lookup(features)
  ...
  tf.compat.v1.tables_initializer().run()

  ids.eval()  ==> [0, 1, 4, 2]
  ```

  Args:
    vocabulary_list: A 1-D `Tensor` that specifies the mapping of keys to
      indices. The type of this object must be castable to `dtype`.
    num_oov_buckets: The number of out-of-vocabulary buckets.
    default_value: The value to use for out-of-vocabulary feature values.
      Defaults to -1.
    hasher_spec: A `HasherSpec` to specify the hash function to use for
      assignment of out-of-vocabulary buckets.
    dtype: The type of values passed to `lookup`. Only string and integers are
      supported.
    name: A name for this op (optional).

  Returns:
    The lookup table to map an input `Tensor` to index `int64` `Tensor`.

  Raises:
    ValueError: If `vocabulary_list` is invalid.
    ValueError: If `num_oov_buckets` is negative.
  '''
def index_to_string_table_from_file(vocabulary_file, vocab_size: Incomplete | None = None, default_value: str = 'UNK', name: Incomplete | None = None, key_column_index=..., value_column_index=..., delimiter: str = '\t'):
    '''Returns a lookup table that maps a `Tensor` of indices into strings.

  This operation constructs a lookup table to map int64 indices into string
  values. The table is initialized from a vocabulary file specified in
  `vocabulary_file`, where the whole line is the value and the
  zero-based line number is the index.

  Any input which does not have a corresponding index in the vocabulary file
  (an out-of-vocabulary entry) is assigned the `default_value`

  The underlying table must be initialized by calling
  `session.run(tf.compat.v1.tables_initializer())` or
  `session.run(table.init())` once.

  To specify multi-column vocabulary files, use key_column_index and
  value_column_index and delimiter.

  - TextFileIndex.LINE_NUMBER means use the line number starting from zero,
    expects data type int64.
  - TextFileIndex.WHOLE_LINE means use the whole line content, expects data
    type string.
  - A value >=0 means use the index (starting at zero) of the split line based
    on `delimiter`.

  Sample Usages:

  If we have a vocabulary file "test.txt" with the following content:

  ```
  emerson
  lake
  palmer
  ```

  ```python
  indices = tf.constant([1, 5], tf.int64)
  table = tf.lookup.index_to_string_table_from_file(
      vocabulary_file="test.txt", default_value="UNKNOWN")
  values = table.lookup(indices)
  ...
  tf.compat.v1.tables_initializer().run()

  values.eval() ==> ["lake", "UNKNOWN"]
  ```

  Args:
    vocabulary_file: The vocabulary filename, may be a constant scalar `Tensor`.
    vocab_size: Number of the elements in the vocabulary, if known.
    default_value: The value to use for out-of-vocabulary indices.
    name: A name for this op (optional).
    key_column_index: The column index from the text file to get the `key`
      values from. The default is to use the line number, starting from zero.
    value_column_index: The column index from the text file to get the `value`
      values from. The default is to use the whole line content.
    delimiter: The delimiter to separate fields in a line.

  Returns:
    The lookup table to map a string values associated to a given index `int64`
    `Tensors`.

  Raises:
    ValueError: when `vocabulary_file` is empty.
    ValueError: when `vocab_size` is invalid.
  '''
def index_to_string_table_from_tensor(vocabulary_list, default_value: str = 'UNK', name: Incomplete | None = None):
    '''Returns a lookup table that maps a `Tensor` of indices into strings.

  This operation constructs a lookup table to map int64 indices into string
  values. The mapping is initialized from a string `vocabulary_list` 1-D
  `Tensor` where each element is a value and the corresponding index within the
  tensor is the key.

  Any input which does not have a corresponding index in \'vocabulary_list\'
  (an out-of-vocabulary entry) is assigned the `default_value`

  The underlying table must be initialized by calling
  `session.run(tf.compat.v1.tables_initializer())` or
  `session.run(table.init())` once.

  Elements in `vocabulary_list` cannot have duplicates, otherwise when executing
  the table initializer op, it will throw a `FailedPreconditionError`.

  Sample Usages:

  ```python
  vocabulary_list = tf.constant(["emerson", "lake", "palmer"])
  indices = tf.constant([1, 5], tf.int64)
  table = tf.lookup.index_to_string_table_from_tensor(
      vocabulary_list, default_value="UNKNOWN")
  values = table.lookup(indices)
  ...
  tf.compat.v1.tables_initializer().run()

  values.eval() ==> ["lake", "UNKNOWN"]
  ```

  Args:
    vocabulary_list: A 1-D string `Tensor` that specifies the strings to map
      from indices.
    default_value: The value to use for out-of-vocabulary indices.
    name: A name for this op (optional).

  Returns:
    The lookup table to map a string values associated to a given index `int64`
    `Tensors`.

  Raises:
    ValueError: when `vocabulary_list` is not set.
  '''

class MutableHashTable(LookupInterface):
    """A generic mutable hash table implementation.

  Data can be inserted by calling the `insert` method and removed by calling the
  `remove` method. It does not support initialization via the init method.

  `MutableHashTable` requires additional memory during checkpointing and restore
  operations to create temporary key and value tensors.

  Example usage:

  >>> table = tf.lookup.experimental.MutableHashTable(key_dtype=tf.string,
  ...                                                 value_dtype=tf.int64,
  ...                                                 default_value=-1)
  >>> keys_tensor = tf.constant(['a', 'b', 'c'])
  >>> vals_tensor = tf.constant([7, 8, 9], dtype=tf.int64)
  >>> input_tensor = tf.constant(['a', 'f'])
  >>> table.insert(keys_tensor, vals_tensor)
  >>> table.lookup(input_tensor).numpy()
  array([ 7, -1])
  >>> table.remove(tf.constant(['c']))
  >>> table.lookup(keys_tensor).numpy()
  array([ 7, 8, -1])
  >>> sorted(table.export()[0].numpy())
  [b'a', b'b']
  >>> sorted(table.export()[1].numpy())
  [7, 8]
  """
    def __init__(self, key_dtype, value_dtype, default_value, name: str = 'MutableHashTable', checkpoint: bool = True, experimental_is_anonymous: bool = False) -> None:
        """Creates an empty `MutableHashTable` object.

    Creates a table, the type of its keys and values are specified by key_dtype
    and value_dtype, respectively.

    Args:
      key_dtype: the type of the key tensors.
      value_dtype: the type of the value tensors.
      default_value: The value to use if a key is missing in the table.
      name: A name for the operation (optional).
      checkpoint: if True, the contents of the table are saved to and restored
        from checkpoints. If `shared_name` is empty for a checkpointed table, it
        is shared using the table node name.
      experimental_is_anonymous: Whether to use anonymous mode for the
        table (default is False). In anonymous mode, the table
        resource can only be accessed via a resource handle. It can't
        be looked up by a name. When all resource handles pointing to
        that resource are gone, the resource will be deleted
        automatically.

    Returns:
      A `MutableHashTable` object.

    Raises:
      ValueError: If checkpoint is True and no name was specified.
    """
    @property
    def name(self): ...
    def size(self, name: Incomplete | None = None):
        """Compute the number of elements in this table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A scalar tensor containing the number of elements in this table.
    """
    def remove(self, keys, name: Incomplete | None = None):
        """Removes `keys` and its associated values from the table.

    If a key is not present in the table, it is silently ignored.

    Args:
      keys: Keys to remove. Can be a tensor of any shape. Must match the table's
        key type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
    def lookup(self, keys, dynamic_default_values: Incomplete | None = None, name: Incomplete | None = None):
        """Looks up `keys` in a table, outputs the corresponding values.

    The `default_value` is used for keys not present in the table.

    Args:
      keys: Keys to look up. Can be a tensor of any shape. Must match the
        table's key_dtype.
      dynamic_default_values: The values to use if a key is missing in the
        table. If None (by default), the `table.default_value` will be used.
        Shape of `dynamic_default_values` must be same with
        `table.default_value` or the lookup result tensor.
        In the latter case, each key will have a different default value.

        For example:

          ```python
          keys = [0, 1, 3]
          dynamic_default_values = [[1, 3, 4], [2, 3, 9], [8, 3, 0]]

          # The key '0' will use [1, 3, 4] as default value.
          # The key '1' will use [2, 3, 9] as default value.
          # The key '3' will use [8, 3, 0] as default value.
          ```

      name: A name for the operation (optional).

    Returns:
      A tensor containing the values in the same shape as `keys` using the
        table's value type.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
    def insert(self, keys, values, name: Incomplete | None = None):
        """Associates `keys` with `values`.

    Args:
      keys: Keys to insert. Can be a tensor of any shape. Must match the table's
        key type.
      values: Values to be associated with keys. Must be a tensor of the same
        shape as `keys` and match the table's value type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` or `values` doesn't match the table data
        types.
    """
    def export(self, name: Incomplete | None = None):
        """Returns tensors of all keys and values in the table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A pair of tensors with the first tensor containing all keys and the
        second tensors containing all values in the table.
    """
    class _Saveable(BaseSaverBuilder.SaveableObject):
        """SaveableObject implementation for DenseHashTable."""
        table_name: Incomplete
        def __init__(self, table, name, table_name: Incomplete | None = None) -> None: ...
        def restore(self, restored_tensors, restored_shapes): ...

class DenseHashTable(LookupInterface):
    '''A mutable hash table with faster lookups and higher memory usage.

  Data can be inserted by calling the `insert` method and removed by calling the
  `remove` method. It does not support initialization via the init method.

  Compared to `MutableHashTable`, `DenseHashTable` offers generally faster
  `insert`, `remove` and `lookup` operations, in exchange for a higher overall
  memory footprint.

  It uses "open addressing" with quadratic reprobing to resolve collisions. This
  requires specifying two keys in the key space, `empty_key` and `deleted_key`,
  that can never inserted into the table.

  Unlike `MutableHashTable`, `DenseHashTable` does not require additional memory
  for temporary tensors created during checkpointing and restore operations.

  Example usage:

  >>> table = tf.lookup.experimental.DenseHashTable(
  ...     key_dtype=tf.string,
  ...     value_dtype=tf.int64,
  ...     default_value=-1,
  ...     empty_key=\'\',
  ...     deleted_key=\'$\')
  >>> keys = tf.constant([\'a\', \'b\', \'c\'])
  >>> values = tf.constant([0, 1, 2], dtype=tf.int64)
  >>> table.insert(keys, values)
  >>> table.remove(tf.constant([\'c\']))
  >>> table.lookup(tf.constant([\'a\', \'b\', \'c\',\'d\'])).numpy()
  array([ 0,  1, -1, -1])
  '''
    def __init__(self, key_dtype, value_dtype, default_value, empty_key, deleted_key, initial_num_buckets: Incomplete | None = None, name: str = 'MutableDenseHashTable', checkpoint: bool = True, experimental_is_anonymous: bool = False) -> None:
        """Creates an empty `DenseHashTable` object.

    Creates a table, the type of its keys and values are specified by key_dtype
    and value_dtype, respectively.

    Args:
      key_dtype: the type of the key tensors.
      value_dtype: the type of the value tensors.
      default_value: The value to use if a key is missing in the table.
      empty_key: the key to use to represent empty buckets internally. Must not
        be used in insert, remove or lookup operations.
      deleted_key: the key to use to represent deleted buckets internally. Must
        not be used in insert, remove or lookup operations and be different from
        the empty_key.
      initial_num_buckets: the initial number of buckets (optional,
        default to 2^17=131072). Note that the default value is
        relatively large (~1MB), so if you are going to create many
        tables (likely the case when `experimental_is_anonymous` is
        `True`), you should set `initial_num_buckets` to a smaller
        value to reduce memory usage.
      name: A name for the operation (optional).
      checkpoint: if True, the contents of the table are saved to and restored
        from checkpoints. If `shared_name` is empty for a checkpointed table, it
        is shared using the table node name.
      experimental_is_anonymous: Whether to use anonymous mode for the
        table (default is False). In anonymous mode, the table
        resource can only be accessed via a resource handle. It can't
        be looked up by a name. When all resource handles pointing to
        that resource are gone, the resource will be deleted
        automatically.

    Returns:
      A `DenseHashTable` object.

    Raises:
      ValueError: If checkpoint is True and no name was specified.
    """
    @property
    def name(self): ...
    def size(self, name: Incomplete | None = None):
        """Compute the number of elements in this table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A scalar tensor containing the number of elements in this table.
    """
    def lookup(self, keys, name: Incomplete | None = None):
        """Looks up `keys` in a table, outputs the corresponding values.

    The `default_value` is used for keys not present in the table.

    Args:
      keys: Keys to look up. Can be a tensor of any shape. Must match the
        table's key_dtype.
      name: A name for the operation (optional).

    Returns:
      A tensor containing the values in the same shape as `keys` using the
        table's value type.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
    def insert_or_assign(self, keys, values, name: Incomplete | None = None):
        """Associates `keys` with `values`.

    Args:
      keys: Keys to insert. Can be a tensor of any shape. Must match the table's
        key type.
      values: Values to be associated with keys. Must be a tensor of the same
        shape as `keys` and match the table's value type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` or `values` doesn't match the table data
        types.
    """
    def insert(self, keys, values, name: Incomplete | None = None):
        """Associates `keys` with `values`.

    Args:
      keys: Keys to insert. Can be a tensor of any shape. Must match the table's
        key type.
      values: Values to be associated with keys. Must be a tensor of the same
        shape as `keys` and match the table's value type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` or `values` doesn't match the table data
        types.
    """
    def erase(self, keys, name: Incomplete | None = None):
        """Removes `keys` and its associated values from the table.

    If a key is not present in the table, it is silently ignored.

    Args:
      keys: Keys to remove. Can be a tensor of any shape. Must match the table's
        key type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
    def remove(self, keys, name: Incomplete | None = None):
        """Removes `keys` and its associated values from the table.

    If a key is not present in the table, it is silently ignored.

    Args:
      keys: Keys to remove. Can be a tensor of any shape. Must match the table's
        key type.
      name: A name for the operation (optional).

    Returns:
      The created Operation.

    Raises:
      TypeError: when `keys` do not match the table data types.
    """
    def export(self, name: Incomplete | None = None):
        """Returns tensors of all keys and values in the table.

    Args:
      name: A name for the operation (optional).

    Returns:
      A pair of tensors with the first tensor containing all keys and the
        second tensors containing all values in the table.
    """
    class _Saveable(BaseSaverBuilder.SaveableObject):
        """SaveableObject implementation for DenseHashTable."""
        table_name: Incomplete
        def __init__(self, table, name, table_name: Incomplete | None = None) -> None: ...
        def restore(self, restored_tensors, restored_shapes): ...
