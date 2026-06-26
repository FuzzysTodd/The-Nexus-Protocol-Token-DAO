from _typeshed import Incomplete
from keras import activations as activations
from keras.engine.base_layer import Layer as Layer

class Activation(Layer):
    '''Applies an activation function to an output.

    Args:
      activation: Activation function, such as `tf.nn.relu`, or string name of
        built-in activation function, such as "relu".

    Usage:

    >>> layer = tf.keras.layers.Activation(\'relu\')
    >>> output = layer([-3.0, -1.0, 0.0, 2.0])
    >>> list(output.numpy())
    [0.0, 0.0, 0.0, 2.0]
    >>> layer = tf.keras.layers.Activation(tf.nn.relu)
    >>> output = layer([-3.0, -1.0, 0.0, 2.0])
    >>> list(output.numpy())
    [0.0, 0.0, 0.0, 2.0]

    Input shape:
      Arbitrary. Use the keyword argument `input_shape`
      (tuple of integers, does not include the batch axis)
      when using this layer as the first layer in a model.

    Output shape:
      Same shape as input.
    '''
    supports_masking: bool
    activation: Incomplete
    def __init__(self, activation, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
