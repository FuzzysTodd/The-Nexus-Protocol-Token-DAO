from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer

class Reshape(Layer):
    """Layer that reshapes inputs into the given shape.

    Input shape:
      Arbitrary, although all dimensions in the input shape must be known/fixed.
      Use the keyword argument `input_shape` (tuple of integers, does not
      include the samples/batch size axis) when using this layer as the first
      layer in a model.

    Output shape:
      `(batch_size,) + target_shape`

    Example:

    >>> # as first layer in a Sequential model
    >>> model = tf.keras.Sequential()
    >>> model.add(tf.keras.layers.Reshape((3, 4), input_shape=(12,)))
    >>> # model.output_shape == (None, 3, 4), `None` is the batch size.
    >>> model.output_shape
    (None, 3, 4)

    >>> # as intermediate layer in a Sequential model
    >>> model.add(tf.keras.layers.Reshape((6, 2)))
    >>> model.output_shape
    (None, 6, 2)

    >>> # also supports shape inference using `-1` as dimension
    >>> model.add(tf.keras.layers.Reshape((-1, 2, 2)))
    >>> model.output_shape
    (None, 3, 2, 2)
    """
    target_shape: Incomplete
    def __init__(self, target_shape, **kwargs) -> None:
        """Creates a `tf.keras.layers.Reshape`  layer instance.

        Args:
          target_shape: Target shape. Tuple of integers, does not include the
            samples dimension (batch size).
          **kwargs: Any additional layer keyword arguments.
        """
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
