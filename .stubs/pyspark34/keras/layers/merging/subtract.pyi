from keras.layers.merging.base_merge import _Merge
from keras.utils import tf_utils as tf_utils

class Subtract(_Merge):
    """Layer that subtracts two inputs.

    It takes as input a list of tensors of size 2, both of the same shape, and
    returns a single tensor, (inputs[0] - inputs[1]), also of the same shape.

    Examples:

    ```python
        import keras

        input1 = keras.layers.Input(shape=(16,))
        x1 = keras.layers.Dense(8, activation='relu')(input1)
        input2 = keras.layers.Input(shape=(32,))
        x2 = keras.layers.Dense(8, activation='relu')(input2)
        # Equivalent to subtracted = keras.layers.subtract([x1, x2])
        subtracted = keras.layers.Subtract()([x1, x2])

        out = keras.layers.Dense(4)(subtracted)
        model = keras.models.Model(inputs=[input1, input2], outputs=out)
    ```
    """
    def build(self, input_shape) -> None: ...

def subtract(inputs, **kwargs):
    """Functional interface to the `Subtract` layer.

    Args:
        inputs: A list of input tensors (exactly 2).
        **kwargs: Standard layer keyword arguments.

    Returns:
        A tensor, the difference of the inputs.

    Examples:

    ```python
        import keras

        input1 = keras.layers.Input(shape=(16,))
        x1 = keras.layers.Dense(8, activation='relu')(input1)
        input2 = keras.layers.Input(shape=(32,))
        x2 = keras.layers.Dense(8, activation='relu')(input2)
        subtracted = keras.layers.subtract([x1, x2])

        out = keras.layers.Dense(4)(subtracted)
        model = keras.models.Model(inputs=[input1, input2], outputs=out)
    ```
    """
