from _typeshed import Incomplete
from tensorflow.python.ops import lookup_ops
from tensorflow.python.training.saver import BaseSaverBuilder

class _MutableDenseHashTable(lookup_ops.LookupInterface):
    """Copy of tf.contrib.lookup.MutableDenseHashTable."""
    def __init__(self, key_dtype, value_dtype, default_value, empty_key, deleted_key, initial_num_buckets: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'MutableDenseHashTable', checkpoint: bool = True) -> None:
        """Creates an empty `_MutableDenseHashTable` object.

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
      initial_num_buckets: the initial number of buckets.
      shared_name: If non-empty, this table will be shared under the given name
        across multiple sessions.
      name: A name for the operation (optional).
      checkpoint: if True, the contents of the table are saved to and restored
        from checkpoints. If `shared_name` is empty for a checkpointed table, it
        is shared using the table node name.

    Returns:
      A `_MutableDenseHashTable` object.

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
        """SaveableObject implementation for _MutableDenseHashTable."""
        def __init__(self, table, name) -> None: ...
        def restore(self, restored_tensors, restored_shapes): ...

class _ShardedMutableDenseHashTable:
    """A sharded version of _MutableDenseHashTable.

  It is designed to be interface compatible with LookupInterface and
  MutableDenseHashTable, with the exception of the export method, which is
  replaced by an export_sharded method.

  The _ShardedMutableDenseHashTable keeps `num_shards` _MutableDenseHashTable
  internally. The shard is computed via the modulo operation on the key.
  """
    def __init__(self, key_dtype, value_dtype, default_value, empty_key, deleted_key, num_shards: int = 1, checkpoint: bool = True, name: str = 'ShardedMutableHashTable') -> None: ...
    @property
    def name(self): ...
    @property
    def table_shards(self): ...
    def size(self, name: Incomplete | None = None): ...
    def lookup(self, keys, name: Incomplete | None = None):
        """Looks up `keys` in a table, outputs the corresponding values."""
    def insert(self, keys, values, name: Incomplete | None = None):
        """Inserts `keys` in a table."""
    def export_sharded(self, name: Incomplete | None = None):
        """Returns lists of the keys and values tensors in the sharded table.

    Args:
      name: name of the table.

    Returns:
      A pair of lists with the first list containing the key tensors and the
        second list containing the value tensors from each shard.
    """
