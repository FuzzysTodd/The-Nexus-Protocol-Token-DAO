from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def composite_tensor_variant_from_components(components, metadata, name: Incomplete | None = None):
    """Encodes an `ExtensionType` value into a `variant` scalar Tensor.

  Returns a scalar variant tensor containing a single `CompositeTensorVariant`
  with the specified Tensor components and TypeSpec.

  Args:
    components: A list of `Tensor` objects.
      The component tensors for the extension type value.
    metadata: A `string`.
      String serialization for the TypeSpec.  (Note: the encoding for the TypeSpec
      may change in future versions of TensorFlow.)
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

CompositeTensorVariantFromComponents: Incomplete

def composite_tensor_variant_from_components_eager_fallback(components, metadata, name, ctx): ...
def composite_tensor_variant_to_components(encoded, metadata, Tcomponents, name: Incomplete | None = None):
    """Decodes a `variant` scalar Tensor into an `ExtensionType` value.

  Returns the Tensor components encoded in a `CompositeTensorVariant`.

  Raises an error if `type_spec_proto` doesn't match the TypeSpec
  in `encoded`.

  Args:
    encoded: A `Tensor` of type `variant`.
      A scalar `variant` Tensor containing an encoded ExtensionType value.
    metadata: A `string`.
      String serialization for the TypeSpec.  Must be compatible with the
      `TypeSpec` contained in `encoded`.  (Note: the encoding for the TypeSpec
      may change in future versions of TensorFlow.)
    Tcomponents: A list of `tf.DTypes`. Expected dtypes for components.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tcomponents`.
  """

CompositeTensorVariantToComponents: Incomplete

def composite_tensor_variant_to_components_eager_fallback(encoded, metadata, Tcomponents, name, ctx): ...
