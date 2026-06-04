from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def empty_tensor_list(element_shape, max_num_elements, element_dtype, name: Incomplete | None = None):
    """Creates and returns an empty tensor list.

  All list elements must be tensors of dtype element_dtype and shape compatible
  with element_shape.

  handle: an empty tensor list.
  element_dtype: the type of elements in the list.
  element_shape: a shape compatible with that of elements in the list.

  Args:
    element_shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    max_num_elements: A `Tensor` of type `int32`.
    element_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

EmptyTensorList: Incomplete

def empty_tensor_list_eager_fallback(element_shape, max_num_elements, element_dtype, name, ctx): ...

class _TensorListConcatOutput(NamedTuple):
    tensor: Incomplete
    lengths: Incomplete

def tensor_list_concat(input_handle, element_dtype, element_shape: Incomplete | None = None, name: Incomplete | None = None):
    """Concats all tensors in the list along the 0th dimension.

  Requires that all tensors have the same shape except the first dimension.

  input_handle: The input list.
  tensor: The concated result.
  lengths: Output tensor containing sizes of the 0th dimension of tensors in the list, used for computing the gradient.

  Args:
    input_handle: A `Tensor` of type `variant`.
    element_dtype: A `tf.DType`.
    element_shape: An optional `tf.TensorShape` or list of `ints`. Defaults to `None`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (tensor, lengths).

    tensor: A `Tensor` of type `element_dtype`.
    lengths: A `Tensor` of type `int64`.
  """

TensorListConcat: Incomplete

def tensor_list_concat_eager_fallback(input_handle, element_dtype, element_shape, name, ctx): ...
def tensor_list_concat_lists(input_a, input_b, element_dtype, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_a: A `Tensor` of type `variant`.
    input_b: A `Tensor` of type `variant`.
    element_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListConcatLists: Incomplete

def tensor_list_concat_lists_eager_fallback(input_a, input_b, element_dtype, name, ctx): ...

class _TensorListConcatV2Output(NamedTuple):
    tensor: Incomplete
    lengths: Incomplete

def tensor_list_concat_v2(input_handle, element_shape, leading_dims, element_dtype, name: Incomplete | None = None):
    """Concats all tensors in the list along the 0th dimension.

  Requires that all tensors have the same shape except the first dimension.

  input_handle: The input list.
  element_shape: The shape of the uninitialized elements in the list. If the first
    dimension is not -1, it is assumed that all list elements have the same
    leading dim.
  leading_dims: The list of leading dims of uninitialized list elements. Used if
    the leading dim of input_handle.element_shape or the element_shape input arg
    is not already set.
  tensor: The concated result.
  lengths: Output tensor containing sizes of the 0th dimension of tensors in the list, used for computing the gradient.

  Args:
    input_handle: A `Tensor` of type `variant`.
    element_shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    leading_dims: A `Tensor` of type `int64`.
    element_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (tensor, lengths).

    tensor: A `Tensor` of type `element_dtype`.
    lengths: A `Tensor` of type `int64`.
  """

TensorListConcatV2: Incomplete

def tensor_list_concat_v2_eager_fallback(input_handle, element_shape, leading_dims, element_dtype, name, ctx): ...
def tensor_list_element_shape(input_handle, shape_type, name: Incomplete | None = None):
    """The shape of the elements of the given list, as a tensor.

    input_handle: the list
    element_shape: the shape of elements of the list

  Args:
    input_handle: A `Tensor` of type `variant`.
    shape_type: A `tf.DType` from: `tf.int32, tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `shape_type`.
  """

TensorListElementShape: Incomplete

def tensor_list_element_shape_eager_fallback(input_handle, shape_type, name, ctx): ...
def tensor_list_from_tensor(tensor, element_shape, name: Incomplete | None = None):
    """Creates a TensorList which, when stacked, has the value of `tensor`.

  Each tensor in the result list corresponds to one row of the input tensor.

  tensor: The input tensor.
  output_handle: The list.

  Args:
    tensor: A `Tensor`.
    element_shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListFromTensor: Incomplete

def tensor_list_from_tensor_eager_fallback(tensor, element_shape, name, ctx): ...
def tensor_list_gather(input_handle, indices, element_shape, element_dtype, name: Incomplete | None = None):
    """Creates a Tensor by indexing into the TensorList.

  Each row in the produced Tensor corresponds to the element in the TensorList
  specified by the given index (see `tf.gather`).

  input_handle: The input tensor list.
  indices: The indices used to index into the list.
  values: The tensor.

  Args:
    input_handle: A `Tensor` of type `variant`.
    indices: A `Tensor` of type `int32`.
    element_shape: A `Tensor` of type `int32`.
    element_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `element_dtype`.
  """

TensorListGather: Incomplete

def tensor_list_gather_eager_fallback(input_handle, indices, element_shape, element_dtype, name, ctx): ...
def tensor_list_get_item(input_handle, index, element_shape, element_dtype, name: Incomplete | None = None):
    """Returns the item in the list with the given index.

  input_handle: the list
  index: the position in the list from which an element will be retrieved
  item: the element at that position

  Args:
    input_handle: A `Tensor` of type `variant`.
    index: A `Tensor` of type `int32`.
    element_shape: A `Tensor` of type `int32`.
    element_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `element_dtype`.
  """

TensorListGetItem: Incomplete

def tensor_list_get_item_eager_fallback(input_handle, index, element_shape, element_dtype, name, ctx): ...
def tensor_list_length(input_handle, name: Incomplete | None = None):
    """Returns the number of tensors in the input tensor list.

  input_handle: the input list
  length: the number of tensors in the list

  Args:
    input_handle: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

TensorListLength: Incomplete

def tensor_list_length_eager_fallback(input_handle, name, ctx): ...

class _TensorListPopBackOutput(NamedTuple):
    output_handle: Incomplete
    tensor: Incomplete

def tensor_list_pop_back(input_handle, element_shape, element_dtype, name: Incomplete | None = None):
    """Returns the last element of the input list as well as a list with all but that element.

  Fails if the list is empty.

  input_handle: the input list
  tensor: the withdrawn last element of the list
  element_dtype: the type of elements in the list
  element_shape: the shape of the output tensor

  Args:
    input_handle: A `Tensor` of type `variant`.
    element_shape: A `Tensor` of type `int32`.
    element_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_handle, tensor).

    output_handle: A `Tensor` of type `variant`.
    tensor: A `Tensor` of type `element_dtype`.
  """

TensorListPopBack: Incomplete

def tensor_list_pop_back_eager_fallback(input_handle, element_shape, element_dtype, name, ctx): ...
def tensor_list_push_back(input_handle, tensor, name: Incomplete | None = None):
    """Returns a list which has the passed-in `Tensor` as last element and the other elements of the given list in `input_handle`.

  tensor: The tensor to put on the list.
  input_handle: The old list.
  output_handle: A list with the elements of the old list followed by tensor.
  element_dtype: the type of elements in the list.
  element_shape: a shape compatible with that of elements in the list.

  Args:
    input_handle: A `Tensor` of type `variant`.
    tensor: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListPushBack: Incomplete

def tensor_list_push_back_eager_fallback(input_handle, tensor, name, ctx): ...
def tensor_list_push_back_batch(input_handles, tensor, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input_handles: A `Tensor` of type `variant`.
    tensor: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListPushBackBatch: Incomplete

def tensor_list_push_back_batch_eager_fallback(input_handles, tensor, name, ctx): ...
def tensor_list_reserve(element_shape, num_elements, element_dtype, name: Incomplete | None = None):
    """List of the given size with empty elements.

  element_shape: the shape of the future elements of the list
  num_elements: the number of elements to reserve
  handle: the output list
  element_dtype: the desired type of elements in the list.

  Args:
    element_shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    num_elements: A `Tensor` of type `int32`.
    element_dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListReserve: Incomplete

def tensor_list_reserve_eager_fallback(element_shape, num_elements, element_dtype, name, ctx): ...
def tensor_list_resize(input_handle, size, name: Incomplete | None = None):
    """Resizes the list.

  
  input_handle: the input list
  size: size of the output list

  Args:
    input_handle: A `Tensor` of type `variant`.
    size: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListResize: Incomplete

def tensor_list_resize_eager_fallback(input_handle, size, name, ctx): ...
def tensor_list_scatter(tensor, indices, element_shape, name: Incomplete | None = None):
    """Creates a TensorList by indexing into a Tensor.

  Each member of the TensorList corresponds to one row of the input tensor,
  specified by the given index (see `tf.gather`).

  tensor: The input tensor.
  indices: The indices used to index into the list.
  element_shape: The shape of the elements in the list (can be less specified than
    the shape of the tensor).
  output_handle: The TensorList.

  Args:
    tensor: A `Tensor`.
    indices: A `Tensor` of type `int32`.
    element_shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListScatter: Incomplete

def tensor_list_scatter_eager_fallback(tensor, indices, element_shape, name, ctx): ...
def tensor_list_scatter_into_existing_list(input_handle, tensor, indices, name: Incomplete | None = None):
    """Scatters tensor at indices in an input list.

  Each member of the TensorList corresponds to one row of the input tensor,
  specified by the given index (see `tf.gather`).

  input_handle: The list to scatter into.
  tensor: The input tensor.
  indices: The indices used to index into the list.
  output_handle: The TensorList.

  Args:
    input_handle: A `Tensor` of type `variant`.
    tensor: A `Tensor`.
    indices: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListScatterIntoExistingList: Incomplete

def tensor_list_scatter_into_existing_list_eager_fallback(input_handle, tensor, indices, name, ctx): ...
def tensor_list_scatter_v2(tensor, indices, element_shape, num_elements, name: Incomplete | None = None):
    """Creates a TensorList by indexing into a Tensor.

  Each member of the TensorList corresponds to one row of the input tensor,
  specified by the given index (see `tf.gather`).

  tensor: The input tensor.
  indices: The indices used to index into the list.
  element_shape: The shape of the elements in the list (can be less specified than
    the shape of the tensor).
  num_elements: The size of the output list. Must be large enough to accommodate
    the largest index in indices. If -1, the list is just large enough to include
    the largest index in indices.
  output_handle: The TensorList.

  Args:
    tensor: A `Tensor`.
    indices: A `Tensor` of type `int32`.
    element_shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    num_elements: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListScatterV2: Incomplete

def tensor_list_scatter_v2_eager_fallback(tensor, indices, element_shape, num_elements, name, ctx): ...
def tensor_list_set_item(input_handle, index, item, name: Incomplete | None = None):
    """Sets the index-th position of the list to contain the given tensor.

  input_handle: the list
  index: the position in the list to which the tensor will be assigned
  item: the element to be assigned to that position
  output_handle: the new list, with the element in the proper position

  Args:
    input_handle: A `Tensor` of type `variant`.
    index: A `Tensor` of type `int32`.
    item: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListSetItem: Incomplete

def tensor_list_set_item_eager_fallback(input_handle, index, item, name, ctx): ...
def tensor_list_split(tensor, element_shape, lengths, name: Incomplete | None = None):
    """Splits a tensor into a list.

  list[i] corresponds to lengths[i] tensors from the input tensor.
  The tensor must have rank at least 1 and contain exactly sum(lengths) elements.

  tensor: The input tensor.
  element_shape: A shape compatible with that of elements in the tensor.
  lengths: Vector of sizes of the 0th dimension of tensors in the list.
  output_handle: The list.

  Args:
    tensor: A `Tensor`.
    element_shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    lengths: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

TensorListSplit: Incomplete

def tensor_list_split_eager_fallback(tensor, element_shape, lengths, name, ctx): ...
def tensor_list_stack(input_handle, element_shape, element_dtype, num_elements: int = -1, name: Incomplete | None = None):
    """Stacks all tensors in the list.

  Requires that all tensors have the same shape.

  input_handle: the input list
  tensor: the gathered result
  num_elements: optional. If not -1, the number of elements in the list.

  Args:
    input_handle: A `Tensor` of type `variant`.
    element_shape: A `Tensor` of type `int32`.
    element_dtype: A `tf.DType`.
    num_elements: An optional `int`. Defaults to `-1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `element_dtype`.
  """

TensorListStack: Incomplete

def tensor_list_stack_eager_fallback(input_handle, element_shape, element_dtype, num_elements, name, ctx): ...
