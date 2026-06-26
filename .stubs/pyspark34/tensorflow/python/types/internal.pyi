class NativeObject:
    """Types natively supported by various TF operations.

  The most notable example of NativeObject is Tensor.
  """
class TypeSpec:
    """Interface for internal isinstance checks to framework/type_spec.py.

  This helps to avoid circular dependencies.
  """
class TensorSpec:
    """Interface for internal isinstance checks to framework/tensor_spec.py.

  This helps to avoid circular dependencies.
  """
