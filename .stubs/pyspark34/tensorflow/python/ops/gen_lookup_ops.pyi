from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def anonymous_hash_table(key_dtype, value_dtype, name: Incomplete | None = None):
    """Creates a uninitialized anonymous hash table.

  This op creates a new anonymous hash table (as a resource) everytime
  it is executed, with the specified dtype of its keys and values,
  returning the resource handle.  Before using the table you will have
  to initialize it.  After initialization the table will be
  immutable. The table is anonymous in the sense that it can only be
  accessed by the returned resource handle (e.g. it cannot be looked up
  by a name in a resource manager). The table will be automatically
  deleted when all resource handles pointing to it are gone.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

AnonymousHashTable: Incomplete

def anonymous_hash_table_eager_fallback(key_dtype, value_dtype, name, ctx): ...
def anonymous_mutable_dense_hash_table(empty_key, deleted_key, value_dtype, value_shape=[], initial_num_buckets: int = 131072, max_load_factor: float = 0.8, name: Incomplete | None = None):
    '''Creates an empty anonymous mutable hash table that uses tensors as the backing store.

  This op creates a new anonymous mutable hash table (as a resource) everytime
  it is executed, with the specified dtype of its keys and values,
  returning the resource handle. Each value must be a scalar.
  Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.

  It uses "open addressing" with quadratic reprobing to resolve
  collisions.

  The table is anonymous in the sense that it can only be
  accessed by the returned resource handle (e.g. it cannot be looked up
  by a name in a resource manager). The table will be automatically
  deleted when all resource handles pointing to it are gone.

  Args:
    empty_key: A `Tensor`.
      The key used to represent empty key buckets internally. Must not
      be used in insert or lookup operations.
    deleted_key: A `Tensor`. Must have the same type as `empty_key`.
    value_dtype: A `tf.DType`. Type of the table values.
    value_shape: An optional `tf.TensorShape` or list of `ints`. Defaults to `[]`.
      The shape of each value.
    initial_num_buckets: An optional `int`. Defaults to `131072`.
      The initial number of hash table buckets. Must be a power
      to 2.
    max_load_factor: An optional `float`. Defaults to `0.8`.
      The maximum ratio between number of entries and number of
      buckets before growing the table. Must be between 0 and 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

AnonymousMutableDenseHashTable: Incomplete

def anonymous_mutable_dense_hash_table_eager_fallback(empty_key, deleted_key, value_dtype, value_shape, initial_num_buckets, max_load_factor, name, ctx): ...
def anonymous_mutable_hash_table(key_dtype, value_dtype, name: Incomplete | None = None):
    """Creates an empty anonymous mutable hash table.

  This op creates a new anonymous mutable hash table (as a resource) everytime
  it is executed, with the specified dtype of its keys and values,
  returning the resource handle. Each value must be a scalar.
  Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.
  The table is anonymous in the sense that it can only be
  accessed by the returned resource handle (e.g. it cannot be looked up
  by a name in a resource manager). The table will be automatically
  deleted when all resource handles pointing to it are gone.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

AnonymousMutableHashTable: Incomplete

def anonymous_mutable_hash_table_eager_fallback(key_dtype, value_dtype, name, ctx): ...
def anonymous_mutable_hash_table_of_tensors(key_dtype, value_dtype, value_shape=[], name: Incomplete | None = None):
    """Creates an empty anonymous mutable hash table of vector values.

  This op creates a new anonymous mutable hash table (as a resource) everytime
  it is executed, with the specified dtype of its keys and values,
  returning the resource handle. Each value must be a vector.
  Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.
  The table is anonymous in the sense that it can only be
  accessed by the returned resource handle (e.g. it cannot be looked up
  by a name in a resource manager). The table will be automatically
  deleted when all resource handles pointing to it are gone.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    value_shape: An optional `tf.TensorShape` or list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

AnonymousMutableHashTableOfTensors: Incomplete

def anonymous_mutable_hash_table_of_tensors_eager_fallback(key_dtype, value_dtype, value_shape, name, ctx): ...
def hash_table(key_dtype, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, name: Incomplete | None = None):
    '''Creates a non-initialized hash table.

  This op creates a hash table, specifying the type of its keys and values.
  Before using the table you will have to initialize it.  After initialization the
  table will be immutable.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
      If true and shared_name is empty, the table is shared
      using the node name.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type mutable `string`.
  '''

HashTable: Incomplete

def hash_table_eager_fallback(key_dtype, value_dtype, container, shared_name, use_node_name_sharing, name, ctx) -> None: ...
def hash_table_v2(key_dtype, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, name: Incomplete | None = None):
    '''Creates a non-initialized hash table.

  This op creates a hash table, specifying the type of its keys and values.
  Before using the table you will have to initialize it.  After initialization the
  table will be immutable.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
      If true and shared_name is empty, the table is shared
      using the node name.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

HashTableV2: Incomplete

def hash_table_v2_eager_fallback(key_dtype, value_dtype, container, shared_name, use_node_name_sharing, name, ctx): ...
def initialize_table(table_handle, keys, values, name: Incomplete | None = None):
    """Table initializer that takes two tensors for keys and values respectively.

  Args:
    table_handle: A `Tensor` of type mutable `string`.
      Handle to a table which will be initialized.
    keys: A `Tensor`. Keys of type Tkey.
    values: A `Tensor`. Values of type Tval.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

InitializeTable: Incomplete

def initialize_table_eager_fallback(table_handle, keys, values, name, ctx) -> None: ...
def initialize_table_from_text_file(table_handle, filename, key_index, value_index, vocab_size: int = -1, delimiter: str = '\t', offset: int = 0, name: Incomplete | None = None):
    '''Initializes a table from a text file.

  It inserts one key-value pair into the table for each line of the file.
  The key and value is extracted from the whole line content, elements from the
  split line based on `delimiter` or the line number (starting from zero).
  Where to extract the key and value from a line is specified by `key_index` and
  `value_index`.

  - A value of -1 means use the line number(starting from zero), expects `int64`.
  - A value of -2 means use the whole line content, expects `string`.
  - A value >= 0 means use the index (starting at zero) of the split line based
    on `delimiter`.

  Args:
    table_handle: A `Tensor` of type mutable `string`.
      Handle to a table which will be initialized.
    filename: A `Tensor` of type `string`. Filename of a vocabulary text file.
    key_index: An `int` that is `>= -2`.
      Column index in a line to get the table `key` values from.
    value_index: An `int` that is `>= -2`.
      Column index that represents information of a line to get the table
      `value` values from.
    vocab_size: An optional `int` that is `>= -1`. Defaults to `-1`.
      Number of elements of the file, use -1 if unknown.
    delimiter: An optional `string`. Defaults to `"\\t"`.
      Delimiter to separate fields in a line.
    offset: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

InitializeTableFromTextFile: Incomplete

def initialize_table_from_text_file_eager_fallback(table_handle, filename, key_index, value_index, vocab_size, delimiter, offset, name, ctx) -> None: ...
def initialize_table_from_text_file_v2(table_handle, filename, key_index, value_index, vocab_size: int = -1, delimiter: str = '\t', offset: int = 0, name: Incomplete | None = None):
    '''Initializes a table from a text file.

  It inserts one key-value pair into the table for each line of the file.
  The key and value is extracted from the whole line content, elements from the
  split line based on `delimiter` or the line number (starting from zero).
  Where to extract the key and value from a line is specified by `key_index` and
  `value_index`.

  - A value of -1 means use the line number(starting from zero), expects `int64`.
  - A value of -2 means use the whole line content, expects `string`.
  - A value >= 0 means use the index (starting at zero) of the split line based
    on `delimiter`.

  Args:
    table_handle: A `Tensor` of type `resource`.
      Handle to a table which will be initialized.
    filename: A `Tensor` of type `string`. Filename of a vocabulary text file.
    key_index: An `int` that is `>= -2`.
      Column index in a line to get the table `key` values from.
    value_index: An `int` that is `>= -2`.
      Column index that represents information of a line to get the table
      `value` values from.
    vocab_size: An optional `int` that is `>= -1`. Defaults to `-1`.
      Number of elements of the file, use -1 if unknown.
    delimiter: An optional `string`. Defaults to `"\\t"`.
      Delimiter to separate fields in a line.
    offset: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

InitializeTableFromTextFileV2: Incomplete

def initialize_table_from_text_file_v2_eager_fallback(table_handle, filename, key_index, value_index, vocab_size, delimiter, offset, name, ctx): ...
def initialize_table_v2(table_handle, keys, values, name: Incomplete | None = None):
    """Table initializer that takes two tensors for keys and values respectively.

  Args:
    table_handle: A `Tensor` of type `resource`.
      Handle to a table which will be initialized.
    keys: A `Tensor`. Keys of type Tkey.
    values: A `Tensor`. Values of type Tval.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

InitializeTableV2: Incomplete

def initialize_table_v2_eager_fallback(table_handle, keys, values, name, ctx): ...

class _LookupTableExportOutput(NamedTuple):
    keys: Incomplete
    values: Incomplete

def lookup_table_export(table_handle, Tkeys, Tvalues, name: Incomplete | None = None):
    """Outputs all keys and values in the table.

  Args:
    table_handle: A `Tensor` of type mutable `string`. Handle to the table.
    Tkeys: A `tf.DType`.
    Tvalues: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (keys, values).

    keys: A `Tensor` of type `Tkeys`.
    values: A `Tensor` of type `Tvalues`.
  """

LookupTableExport: Incomplete

def lookup_table_export_eager_fallback(table_handle, Tkeys, Tvalues, name, ctx) -> None: ...

class _LookupTableExportV2Output(NamedTuple):
    keys: Incomplete
    values: Incomplete

def lookup_table_export_v2(table_handle, Tkeys, Tvalues, name: Incomplete | None = None):
    """Outputs all keys and values in the table.

  Args:
    table_handle: A `Tensor` of type `resource`. Handle to the table.
    Tkeys: A `tf.DType`.
    Tvalues: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (keys, values).

    keys: A `Tensor` of type `Tkeys`.
    values: A `Tensor` of type `Tvalues`.
  """

LookupTableExportV2: Incomplete

def lookup_table_export_v2_eager_fallback(table_handle, Tkeys, Tvalues, name, ctx): ...
def lookup_table_find(table_handle, keys, default_value, name: Incomplete | None = None):
    """Looks up keys in a table, outputs the corresponding values.

  The tensor `keys` must of the same type as the keys of the table.
  The output `values` is of the type of the table values.

  The scalar `default_value` is the value output for keys not present in the
  table. It must also be of the same type as the table values.

  Args:
    table_handle: A `Tensor` of type mutable `string`. Handle to the table.
    keys: A `Tensor`. Any shape.  Keys to look up.
    default_value: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `default_value`.
  """

LookupTableFind: Incomplete

def lookup_table_find_eager_fallback(table_handle, keys, default_value, name, ctx) -> None: ...
def lookup_table_find_v2(table_handle, keys, default_value, name: Incomplete | None = None):
    """Looks up keys in a table, outputs the corresponding values.

  The tensor `keys` must of the same type as the keys of the table.
  The output `values` is of the type of the table values.

  The scalar `default_value` is the value output for keys not present in the
  table. It must also be of the same type as the table values.

  Args:
    table_handle: A `Tensor` of type `resource`. Handle to the table.
    keys: A `Tensor`. Any shape.  Keys to look up.
    default_value: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `default_value`.
  """

LookupTableFindV2: Incomplete

def lookup_table_find_v2_eager_fallback(table_handle, keys, default_value, name, ctx): ...
def lookup_table_import(table_handle, keys, values, name: Incomplete | None = None):
    """Replaces the contents of the table with the specified keys and values.

  The tensor `keys` must be of the same type as the keys of the table.
  The tensor `values` must be of the type of the table values.

  Args:
    table_handle: A `Tensor` of type mutable `string`. Handle to the table.
    keys: A `Tensor`. Any shape.  Keys to look up.
    values: A `Tensor`. Values to associate with keys.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

LookupTableImport: Incomplete

def lookup_table_import_eager_fallback(table_handle, keys, values, name, ctx) -> None: ...
def lookup_table_import_v2(table_handle, keys, values, name: Incomplete | None = None):
    """Replaces the contents of the table with the specified keys and values.

  The tensor `keys` must be of the same type as the keys of the table.
  The tensor `values` must be of the type of the table values.

  Args:
    table_handle: A `Tensor` of type `resource`. Handle to the table.
    keys: A `Tensor`. Any shape.  Keys to look up.
    values: A `Tensor`. Values to associate with keys.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

LookupTableImportV2: Incomplete

def lookup_table_import_v2_eager_fallback(table_handle, keys, values, name, ctx): ...
def lookup_table_insert(table_handle, keys, values, name: Incomplete | None = None):
    """Updates the table to associates keys with values.

  The tensor `keys` must be of the same type as the keys of the table.
  The tensor `values` must be of the type of the table values.

  Args:
    table_handle: A `Tensor` of type mutable `string`. Handle to the table.
    keys: A `Tensor`. Any shape.  Keys to look up.
    values: A `Tensor`. Values to associate with keys.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

LookupTableInsert: Incomplete

def lookup_table_insert_eager_fallback(table_handle, keys, values, name, ctx) -> None: ...
def lookup_table_insert_v2(table_handle, keys, values, name: Incomplete | None = None):
    """Updates the table to associates keys with values.

  The tensor `keys` must be of the same type as the keys of the table.
  The tensor `values` must be of the type of the table values.

  Args:
    table_handle: A `Tensor` of type `resource`. Handle to the table.
    keys: A `Tensor`. Any shape.  Keys to look up.
    values: A `Tensor`. Values to associate with keys.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

LookupTableInsertV2: Incomplete

def lookup_table_insert_v2_eager_fallback(table_handle, keys, values, name, ctx): ...
def lookup_table_remove_v2(table_handle, keys, name: Incomplete | None = None):
    """Removes keys and its associated values from a table.

  The tensor `keys` must of the same type as the keys of the table. Keys not
  already in the table are silently ignored.

  Args:
    table_handle: A `Tensor` of type `resource`. Handle to the table.
    keys: A `Tensor`. Any shape.  Keys of the elements to remove.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

LookupTableRemoveV2: Incomplete

def lookup_table_remove_v2_eager_fallback(table_handle, keys, name, ctx): ...
def lookup_table_size(table_handle, name: Incomplete | None = None):
    """Computes the number of elements in the given table.

  Args:
    table_handle: A `Tensor` of type mutable `string`. Handle to the table.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

LookupTableSize: Incomplete

def lookup_table_size_eager_fallback(table_handle, name, ctx) -> None: ...
def lookup_table_size_v2(table_handle, name: Incomplete | None = None):
    """Computes the number of elements in the given table.

  Args:
    table_handle: A `Tensor` of type `resource`. Handle to the table.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

LookupTableSizeV2: Incomplete

def lookup_table_size_v2_eager_fallback(table_handle, name, ctx): ...
def mutable_dense_hash_table(empty_key, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, value_shape=[], initial_num_buckets: int = 131072, max_load_factor: float = 0.8, name: Incomplete | None = None):
    '''Creates an empty hash table that uses tensors as the backing store.

  It uses "open addressing" with quadratic reprobing to resolve
  collisions.

  This op creates a mutable hash table, specifying the type of its keys and
  values. Each value must be a scalar. Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.

  Args:
    empty_key: A `Tensor`.
      The key used to represent empty key buckets internally. Must not
      be used in insert or lookup operations.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
    value_shape: An optional `tf.TensorShape` or list of `ints`. Defaults to `[]`.
      The shape of each value.
    initial_num_buckets: An optional `int`. Defaults to `131072`.
      The initial number of hash table buckets. Must be a power
      to 2.
    max_load_factor: An optional `float`. Defaults to `0.8`.
      The maximum ratio between number of entries and number of
      buckets before growing the table. Must be between 0 and 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type mutable `string`.
  '''

MutableDenseHashTable: Incomplete

def mutable_dense_hash_table_eager_fallback(empty_key, value_dtype, container, shared_name, use_node_name_sharing, value_shape, initial_num_buckets, max_load_factor, name, ctx) -> None: ...
def mutable_dense_hash_table_v2(empty_key, deleted_key, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, value_shape=[], initial_num_buckets: int = 131072, max_load_factor: float = 0.8, name: Incomplete | None = None):
    '''Creates an empty hash table that uses tensors as the backing store.

  It uses "open addressing" with quadratic reprobing to resolve
  collisions.

  This op creates a mutable hash table, specifying the type of its keys and
  values. Each value must be a scalar. Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.

  Args:
    empty_key: A `Tensor`.
      The key used to represent empty key buckets internally. Must not
      be used in insert or lookup operations.
    deleted_key: A `Tensor`. Must have the same type as `empty_key`.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
    value_shape: An optional `tf.TensorShape` or list of `ints`. Defaults to `[]`.
      The shape of each value.
    initial_num_buckets: An optional `int`. Defaults to `131072`.
      The initial number of hash table buckets. Must be a power
      to 2.
    max_load_factor: An optional `float`. Defaults to `0.8`.
      The maximum ratio between number of entries and number of
      buckets before growing the table. Must be between 0 and 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

MutableDenseHashTableV2: Incomplete

def mutable_dense_hash_table_v2_eager_fallback(empty_key, deleted_key, value_dtype, container, shared_name, use_node_name_sharing, value_shape, initial_num_buckets, max_load_factor, name, ctx): ...
def mutable_hash_table(key_dtype, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, name: Incomplete | None = None):
    '''Creates an empty hash table.

  This op creates a mutable hash table, specifying the type of its keys and
  values. Each value must be a scalar. Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
      If true and shared_name is empty, the table is shared
      using the node name.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type mutable `string`.
  '''

MutableHashTable: Incomplete

def mutable_hash_table_eager_fallback(key_dtype, value_dtype, container, shared_name, use_node_name_sharing, name, ctx) -> None: ...
def mutable_hash_table_of_tensors(key_dtype, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, value_shape=[], name: Incomplete | None = None):
    '''Creates an empty hash table.

  This op creates a mutable hash table, specifying the type of its keys and
  values. Each value must be a vector. Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
    value_shape: An optional `tf.TensorShape` or list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type mutable `string`.
  '''

MutableHashTableOfTensors: Incomplete

def mutable_hash_table_of_tensors_eager_fallback(key_dtype, value_dtype, container, shared_name, use_node_name_sharing, value_shape, name, ctx) -> None: ...
def mutable_hash_table_of_tensors_v2(key_dtype, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, value_shape=[], name: Incomplete | None = None):
    '''Creates an empty hash table.

  This op creates a mutable hash table, specifying the type of its keys and
  values. Each value must be a vector. Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
    value_shape: An optional `tf.TensorShape` or list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

MutableHashTableOfTensorsV2: Incomplete

def mutable_hash_table_of_tensors_v2_eager_fallback(key_dtype, value_dtype, container, shared_name, use_node_name_sharing, value_shape, name, ctx): ...
def mutable_hash_table_v2(key_dtype, value_dtype, container: str = '', shared_name: str = '', use_node_name_sharing: bool = False, name: Incomplete | None = None):
    '''Creates an empty hash table.

  This op creates a mutable hash table, specifying the type of its keys and
  values. Each value must be a scalar. Data can be inserted into the table using
  the insert operations. It does not support the initialization operation.

  Args:
    key_dtype: A `tf.DType`. Type of the table keys.
    value_dtype: A `tf.DType`. Type of the table values.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this table is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this table is shared under the given name across
      multiple sessions.
    use_node_name_sharing: An optional `bool`. Defaults to `False`.
      If true and shared_name is empty, the table is shared
      using the node name.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

MutableHashTableV2: Incomplete

def mutable_hash_table_v2_eager_fallback(key_dtype, value_dtype, container, shared_name, use_node_name_sharing, name, ctx): ...
