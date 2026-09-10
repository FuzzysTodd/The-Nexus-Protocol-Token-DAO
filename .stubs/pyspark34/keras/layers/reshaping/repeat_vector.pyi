from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec

class RepeatVector(Layer):
    """Repeats the input n times.

    Example:

    ```python
    model = Sequential()
    model.add(Dense(32, input_dim=32))
    # now: model.output_shape == (None, 32)
    # note: `None` is the batch dimension

    model.add(RepeatVector(3))
    # now: model.output_shape == (None, 3, 32)
    ```

    Args:
      n: Integer, repetition factor.
    Input shape: 2D tensor of shape `(num_samples, features)`.
    Output shape: 3D tensor of shape `(num_samples, n, features)`.
    """
    n: Incomplete
    input_spec: Incomplete
    def __init__(self, n, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
