from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers.rnn.base_wrapper import Wrapper as Wrapper
from keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, tf_utils as tf_utils

class TimeDistributed(Wrapper):
    """This wrapper allows to apply a layer to every temporal slice of an input.

    Every input should be at least 3D, and the dimension of index one of the
    first input will be considered to be the temporal dimension.

    Consider a batch of 32 video samples, where each sample is a 128x128 RGB
    image with `channels_last` data format, across 10 timesteps.
    The batch input shape is `(32, 10, 128, 128, 3)`.

    You can then use `TimeDistributed` to apply the same `Conv2D` layer to each
    of the 10 timesteps, independently:

    >>> inputs = tf.keras.Input(shape=(10, 128, 128, 3))
    >>> conv_2d_layer = tf.keras.layers.Conv2D(64, (3, 3))
    >>> outputs = tf.keras.layers.TimeDistributed(conv_2d_layer)(inputs)
    >>> outputs.shape
    TensorShape([None, 10, 126, 126, 64])

    Because `TimeDistributed` applies the same instance of `Conv2D` to each of
    the timestamps, the same set of weights are used at each timestamp.

    Args:
      layer: a `tf.keras.layers.Layer` instance.

    Call arguments:
      inputs: Input tensor of shape (batch, time, ...) or nested tensors,
        and each of which has shape (batch, time, ...).
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode. This argument is passed to the
        wrapped layer (only if the layer supports this argument).
      mask: Binary tensor of shape `(samples, timesteps)` indicating whether
        a given timestep should be masked. This argument is passed to the
        wrapped layer (only if the layer supports this argument).

    Raises:
      ValueError: If not initialized with a `tf.keras.layers.Layer` instance.
    """
    supports_masking: bool
    def __init__(self, layer, **kwargs) -> None: ...
    input_spec: Incomplete
    built: bool
    def build(self, input_shape): ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs, training: Incomplete | None = None, mask: Incomplete | None = None): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None):
        '''Computes an output mask tensor for Embedding layer.

        This is based on the inputs, mask, and the inner layer.
        If batch size is specified:
        Simply return the input `mask`. (An rnn-based implementation with
        more than one rnn inputs is required but not supported in tf.keras yet.)
        Otherwise we call `compute_mask` of the inner layer at each time step.
        If the output mask at each time step is not `None`:
        (E.g., inner layer is Masking or RNN)
        Concatenate all of them and return the concatenation.
        If the output mask at each time step is `None` and the input mask is not
        `None`:(E.g., inner layer is Dense)
        Reduce the input_mask to 2 dimensions and return it.
        Otherwise (both the output mask and the input mask are `None`):
        (E.g., `mask` is not used at all)
        Return `None`.

        Args:
          inputs: Tensor with shape [batch size, timesteps, ...] indicating the
            input to TimeDistributed. If static shape information is available
            for "batch size", `mask` is returned unmodified.
          mask: Either None (indicating no masking) or a Tensor indicating the
            input mask for TimeDistributed. The shape can be static or dynamic.

        Returns:
          Either None (no masking), or a [batch size, timesteps, ...] Tensor
          with an output mask for the TimeDistributed layer with the shape
          beyond the second dimension being the value of the input mask shape(if
          the computed output mask is none), an output mask with the shape
          beyond the first dimension being the value of the mask shape(if mask
          is not None) or output mask with the shape beyond the first dimension
          being the value of the computed output shape.

        '''
