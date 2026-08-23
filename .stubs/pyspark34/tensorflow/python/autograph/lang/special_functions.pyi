from _typeshed import Incomplete
from tensorflow.python.autograph.operators import data_structures as data_structures
from tensorflow.python.framework import constant_op as constant_op, tensor_util as tensor_util

def match_staging_level(value, like_value):
    """Casts a value to be staged at the same level as another."""
def tensor_list(elements, element_dtype: Incomplete | None = None, element_shape: Incomplete | None = None, use_tensor_array: bool = False):
    """Creates an tensor list and populates it with the given elements.

  This function provides a more uniform access to tensor lists and tensor
  arrays, and allows optional initialization.

  Note: this function is a simplified wrapper. If you need greater control,
  it is recommended to use the underlying implementation directly.

  Args:
    elements: Iterable[tf.Tensor, ...], the elements to initially fill the list
        with
    element_dtype: Optional[tf.DType], data type for the elements in the list;
        required if the list is empty
    element_shape: Optional[tf.TensorShape], shape for the elements in the list;
        required if the list is empty
    use_tensor_array: bool, whether to use the more compatible but restrictive
        tf.TensorArray implementation
  Returns:
    Union[tf.Tensor, tf.TensorArray], the new list.
  Raises:
    ValueError: for invalid arguments
  """
def stack(list_or_tensor, element_dtype: Incomplete | None = None, strict: bool = True):
    """Stacks the input, if it admits the notion of stacking.

  For example, a list of tensors can be stacked into a larger tensor. This
  function is similar to tf.stack, but it accepts non-lists and lists of
  non-tensors as arguments. In the latter case, the function does nothing.

  Args:
    list_or_tensor: Any
    element_dtype: tf.DType, optional dtypedtype for the elements in the list.
        Required if the input is stackable, and the list is untyped.
    strict: bool, if True an error is raised if the input is not stackable.
        Otherwise the function is a no-op.

  Returns:
    Any, if the input is stackable, the result will be a tf.Tensor. Otherwise,
    if strict=False, the result will be list_or_tensor.

  Raises:
    ValueError: if strict=True and the input is not stackable.
  """
