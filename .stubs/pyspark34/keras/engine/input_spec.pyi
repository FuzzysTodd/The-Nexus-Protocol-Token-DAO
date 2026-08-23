from _typeshed import Incomplete
from keras import backend as backend

class InputSpec:
    """Specifies the rank, dtype and shape of every input to a layer.

    Layers can expose (if appropriate) an `input_spec` attribute:
    an instance of `InputSpec`, or a nested structure of `InputSpec` instances
    (one per input tensor). These objects enable the layer to run input
    compatibility checks for input structure, input rank, input shape, and
    input dtype.

    A None entry in a shape is compatible with any dimension,
    a None shape is compatible with any shape.

    Args:
      dtype: Expected DataType of the input.
      shape: Shape tuple, expected shape of the input
        (may include None for unchecked axes). Includes the batch size.
      ndim: Integer, expected rank of the input.
      max_ndim: Integer, maximum rank of the input.
      min_ndim: Integer, minimum rank of the input.
      axes: Dictionary mapping integer axes to
        a specific dimension value.
      allow_last_axis_squeeze: If True, then allow inputs of rank N+1 as long
        as the last axis of the input is 1, as well as inputs of rank N-1
        as long as the last axis of the spec is 1.
      name: Expected key corresponding to this input when passing data as
        a dictionary.

    Example:

    ```python
    class MyLayer(Layer):
        def __init__(self):
            super(MyLayer, self).__init__()
            # The layer will accept inputs with
            # shape (?, 28, 28) & (?, 28, 28, 1)
            # and raise an appropriate error message otherwise.
            self.input_spec = InputSpec(
                shape=(None, 28, 28, 1),
                allow_last_axis_squeeze=True)
    ```
    """
    dtype: Incomplete
    ndim: Incomplete
    shape: Incomplete
    max_ndim: Incomplete
    min_ndim: Incomplete
    name: Incomplete
    allow_last_axis_squeeze: Incomplete
    axes: Incomplete
    def __init__(self, dtype: Incomplete | None = None, shape: Incomplete | None = None, ndim: Incomplete | None = None, max_ndim: Incomplete | None = None, min_ndim: Incomplete | None = None, axes: Incomplete | None = None, allow_last_axis_squeeze: bool = False, name: Incomplete | None = None) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

def to_tensor_shape(spec):
    """Returns a tf.TensorShape object that matches the shape specifications.

    If the InputSpec's shape or ndim is defined, this method will return a fully
    or partially-known shape. Otherwise, the returned TensorShape is None.

    Args:
      spec: an InputSpec object.

    Returns:
      a tf.TensorShape object
    """
def assert_input_compatibility(input_spec, inputs, layer_name) -> None:
    """Checks compatibility between the layer and provided inputs.

    This checks that the tensor(s) `inputs` verify the input assumptions
    of a layer (if any). If not, a clear and actional exception gets raised.

    Args:
        input_spec: An InputSpec instance, list of InputSpec instances, a nested
            structure of InputSpec instances, or None.
        inputs: Input tensor, list of input tensors, or a nested structure of
            input tensors.
        layer_name: String, name of the layer (for error message formatting).

    Raises:
        ValueError: in case of mismatch between
            the provided inputs and the expectations of the layer.
    """
def display_shape(shape): ...
def to_tensor_spec(input_spec, default_dtype: Incomplete | None = None):
    """Converts a Keras InputSpec object to a TensorSpec."""
