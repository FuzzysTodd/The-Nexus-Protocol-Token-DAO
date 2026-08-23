from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer_utils as base_layer_utils
from keras.layers.merging.base_merge import _Merge
from keras.utils import tf_utils as tf_utils

class Dot(_Merge):
    """Layer that computes a dot product between samples in two tensors.

    E.g. if applied to a list of two tensors `a` and `b` of shape
    `(batch_size, n)`, the output will be a tensor of shape `(batch_size, 1)`
    where each entry `i` will be the dot product between
    `a[i]` and `b[i]`.

    >>> x = np.arange(10).reshape(1, 5, 2)
    >>> print(x)
    [[[0 1]
      [2 3]
      [4 5]
      [6 7]
      [8 9]]]
    >>> y = np.arange(10, 20).reshape(1, 2, 5)
    >>> print(y)
    [[[10 11 12 13 14]
      [15 16 17 18 19]]]
    >>> tf.keras.layers.Dot(axes=(1, 2))([x, y])
    <tf.Tensor: shape=(1, 2, 2), dtype=int64, numpy=
    array([[[260, 360],
            [320, 445]]])>

    >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
    >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
    >>> dotted = tf.keras.layers.Dot(axes=1)([x1, x2])
    >>> dotted.shape
    TensorShape([5, 1])


    """
    axes: Incomplete
    normalize: Incomplete
    supports_masking: bool
    def __init__(self, axes, normalize: bool = False, **kwargs) -> None:
        """Initializes a layer that computes the element-wise dot product.

          >>> x = np.arange(10).reshape(1, 5, 2)
          >>> print(x)
          [[[0 1]
            [2 3]
            [4 5]
            [6 7]
            [8 9]]]
          >>> y = np.arange(10, 20).reshape(1, 2, 5)
          >>> print(y)
          [[[10 11 12 13 14]
            [15 16 17 18 19]]]
          >>> tf.keras.layers.Dot(axes=(1, 2))([x, y])
          <tf.Tensor: shape=(1, 2, 2), dtype=int64, numpy=
          array([[[260, 360],
                  [320, 445]]])>

        Args:
          axes: Integer or tuple of integers,
            axis or axes along which to take the dot product. If a tuple, should
            be two integers corresponding to the desired axis from the first
            input and the desired axis from the second input, respectively. Note
            that the size of the two selected axes must match.
          normalize: Whether to L2-normalize samples along the
            dot product axis before taking the dot product.
            If set to True, then the output of the dot product
            is the cosine proximity between the two samples.
          **kwargs: Standard layer keyword arguments.
        """
    def build(self, input_shape) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None) -> None: ...
    def get_config(self): ...

def dot(inputs, axes, normalize: bool = False, **kwargs):
    """Functional interface to the `Dot` layer.

    Args:
        inputs: A list of input tensors (at least 2).
        axes: Integer or tuple of integers,
            axis or axes along which to take the dot product.
        normalize: Whether to L2-normalize samples along the
            dot product axis before taking the dot product.
            If set to True, then the output of the dot product
            is the cosine proximity between the two samples.
        **kwargs: Standard layer keyword arguments.

    Returns:
        A tensor, the dot product of the samples from the inputs.
    """
