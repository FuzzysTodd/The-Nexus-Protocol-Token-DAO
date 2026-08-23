from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def empty_tensor_map(name: Incomplete | None = None):
    """Creates and returns an empty tensor map.

  handle: an empty tensor map

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

EmptyTensorMap: Incomplete

def empty_tensor_map_eager_fallback(name, ctx): ...
def tensor_map_erase(input_handle, key, value_dtype, name: Incomplete | None = None):
    """Returns a tensor map with item from given key erased.

  input_handle: the original map
  output_handle: the map with value from given key removed
  key: the key of the value to be erased

  Args:
    input_handle: A `Tensor` of type `variant`.
    key: A `Tensor`.
    value_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorMapErase: Incomplete

def tensor_map_erase_eager_fallback(input_handle, key, value_dtype, name, ctx): ...
def tensor_map_has_key(input_handle, key, name: Incomplete | None = None):
    """Returns whether the given key exists in the map.

  input_handle: the input map
  key: the key to check
  has_key: whether the key is already in the map or not

  Args:
    input_handle: A `Tensor` of type `variant`.
    key: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

TensorMapHasKey: Incomplete

def tensor_map_has_key_eager_fallback(input_handle, key, name, ctx): ...
def tensor_map_insert(input_handle, key, value, name: Incomplete | None = None):
    """Returns a map that is the 'input_handle' with the given key-value pair inserted.

  input_handle: the original map
  output_handle: the map with key and value inserted
  key: the key to be inserted
  value: the value to be inserted

  Args:
    input_handle: A `Tensor` of type `variant`.
    key: A `Tensor`.
    value: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorMapInsert: Incomplete

def tensor_map_insert_eager_fallback(input_handle, key, value, name, ctx): ...
def tensor_map_lookup(input_handle, key, value_dtype, name: Incomplete | None = None):
    """Returns the value from a given key in a tensor map.

  input_handle: the input map
  key: the key to be looked up
  value: the value found from the given key

  Args:
    input_handle: A `Tensor` of type `variant`.
    key: A `Tensor`.
    value_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `value_dtype`.
  """

TensorMapLookup: Incomplete

def tensor_map_lookup_eager_fallback(input_handle, key, value_dtype, name, ctx): ...
def tensor_map_size(input_handle, name: Incomplete | None = None):
    """Returns the number of tensors in the input tensor map.

  input_handle: the input map
  size: the number of tensors in the map

  Args:
    input_handle: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

TensorMapSize: Incomplete

def tensor_map_size_eager_fallback(input_handle, name, ctx): ...
def tensor_map_stack_keys(input_handle, key_dtype, name: Incomplete | None = None):
    """Returns a Tensor stack of all keys in a tensor map.

  input_handle: the input map
  keys: the returned Tensor of all keys in the map

  Args:
    input_handle: A `Tensor` of type `variant`.
    key_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `key_dtype`.
  """

TensorMapStackKeys: Incomplete

def tensor_map_stack_keys_eager_fallback(input_handle, key_dtype, name, ctx): ...
