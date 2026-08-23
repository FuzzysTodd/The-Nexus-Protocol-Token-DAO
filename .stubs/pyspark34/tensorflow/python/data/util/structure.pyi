from _typeshed import Incomplete
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import composite_tensor as composite_tensor, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec, type_spec_registry as type_spec_registry
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.types import internal as internal
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

def normalize_element(element, element_signature: Incomplete | None = None):
    """Normalizes a nested structure of element components.

  * Components matching `SparseTensorSpec` are converted to `SparseTensor`.
  * Components matching `RaggedTensorSpec` are converted to `RaggedTensor`.
  * Components matching `VariableSpec` are converted to `Tensor`.
  * Components matching `DatasetSpec` or `TensorArraySpec` are passed through.
  * `CompositeTensor` components are passed through.
  * All other components are converted to `Tensor`.

  Args:
    element: A nested structure of individual components.
    element_signature: (Optional.) A nested structure of `tf.DType` objects
      corresponding to each component of `element`. If specified, it will be
      used to set the exact type of output tensor when converting input
      components which are not tensors themselves (e.g. numpy arrays, native
      python types, etc.)

  Returns:
    A nested structure of `Tensor`, `Variable`, `Dataset`, `SparseTensor`,
    `RaggedTensor`, or `TensorArray` objects.
  """
def convert_legacy_structure(output_types, output_shapes, output_classes):
    '''Returns a `Structure` that represents the given legacy structure.

  This method provides a way to convert from the existing `Dataset` and
  `Iterator` structure-related properties to a `Structure` object. A "legacy"
  structure is represented by the `tf.data.Dataset.output_types`,
  `tf.data.Dataset.output_shapes`, and `tf.data.Dataset.output_classes`
  properties.

  TODO(b/110122868): Remove this function once `Structure` is used throughout
  `tf.data`.

  Args:
    output_types: A nested structure of `tf.DType` objects corresponding to
      each component of a structured value.
    output_shapes: A nested structure of `tf.TensorShape` objects
      corresponding to each component a structured value.
    output_classes: A nested structure of Python `type` objects corresponding
      to each component of a structured value.

  Returns:
    A `Structure`.

  Raises:
    TypeError: If a structure cannot be built from the arguments, because one of
      the component classes in `output_classes` is not supported.
  '''
def from_compatible_tensor_list(element_spec, tensor_list):
    """Returns an element constructed from the given spec and tensor list.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.
    tensor_list: A list of tensors to use for constructing the value.

  Returns:
    An element constructed from the given spec and tensor list.

  Raises:
    ValueError: If the number of tensors needed to construct an element for
      the given spec does not match the given number of tensors.
  """
def from_tensor_list(element_spec, tensor_list):
    """Returns an element constructed from the given spec and tensor list.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.
    tensor_list: A list of tensors to use for constructing the value.

  Returns:
    An element constructed from the given spec and tensor list.

  Raises:
    ValueError: If the number of tensors needed to construct an element for
      the given spec does not match the given number of tensors or the given
      spec is not compatible with the tensor list.
  """
def get_flat_tensor_specs(element_spec):
    """Returns a list `tf.TypeSpec`s for the element tensor representation.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.

  Returns:
    A list `tf.TypeSpec`s for the element tensor representation.
  """
def get_flat_tensor_shapes(element_spec):
    """Returns a list `tf.TensorShapes`s for the element tensor representation.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.

  Returns:
    A list `tf.TensorShapes`s for the element tensor representation.
  """
def get_flat_tensor_types(element_spec):
    """Returns a list `tf.DType`s for the element tensor representation.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.

  Returns:
    A list `tf.DType`s for the element tensor representation.
  """
def to_batched_tensor_list(element_spec, element):
    """Returns a tensor list representation of the element.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.
    element: The element to convert to tensor list representation.

  Returns:
    A tensor list representation of `element`.

  Raises:
    ValueError: If `element_spec` and `element` do not have the same number of
      elements or if the two structures are not nested in the same way or the
      rank of any of the tensors in the tensor list representation is 0.
    TypeError: If `element_spec` and `element` differ in the type of sequence
      in any of their substructures.
  """
def to_tensor_list(element_spec, element):
    """Returns a tensor list representation of the element.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.
    element: The element to convert to tensor list representation.

  Returns:
    A tensor list representation of `element`.

  Raises:
    ValueError: If `element_spec` and `element` do not have the same number of
      elements or if the two structures are not nested in the same way.
    TypeError: If `element_spec` and `element` differ in the type of sequence
      in any of their substructures.
  """
def are_compatible(spec1, spec2):
    """Indicates whether two type specifications are compatible.

  Two type specifications are compatible if they have the same nested structure
  and the their individual components are pair-wise compatible.

  Args:
    spec1: A `tf.TypeSpec` object to compare.
    spec2: A `tf.TypeSpec` object to compare.

  Returns:
    `True` if the two type specifications are compatible and `False` otherwise.
  """
def type_spec_from_value(element, use_fallback: bool = True):
    """Creates a type specification for the given value.

  Args:
    element: The element to create the type specification for.
    use_fallback: Whether to fall back to converting the element to a tensor
      in order to compute its `TypeSpec`.

  Returns:
    A nested structure of `TypeSpec`s that represents the type specification
    of `element`.

  Raises:
    TypeError: If a `TypeSpec` cannot be built for `element`, because its type
      is not supported.
  """

class NoneTensor(composite_tensor.CompositeTensor):
    """Composite tensor representation for `None` value."""

class NoneTensorSpec(type_spec.BatchableTypeSpec):
    """Type specification for `None` value."""
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...
    def most_specific_compatible_shape(self, other): ...
