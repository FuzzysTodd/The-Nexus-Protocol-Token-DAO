from _typeshed import Incomplete
from keras import backend as backend
from keras.layers.merging.base_merge import _Merge
from keras.utils import tf_utils as tf_utils

class Concatenate(_Merge):
    """Layer that concatenates a list of inputs.

    It takes as input a list of tensors, all of the same shape except
    for the concatenation axis, and returns a single tensor that is the
    concatenation of all inputs.

    >>> x = np.arange(20).reshape(2, 2, 5)
    >>> print(x)
    [[[ 0  1  2  3  4]
      [ 5  6  7  8  9]]
     [[10 11 12 13 14]
      [15 16 17 18 19]]]
    >>> y = np.arange(20, 30).reshape(2, 1, 5)
    >>> print(y)
    [[[20 21 22 23 24]]
     [[25 26 27 28 29]]]
    >>> tf.keras.layers.Concatenate(axis=1)([x, y])
    <tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
    array([[[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [20, 21, 22, 23, 24]],
           [[10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [25, 26, 27, 28, 29]]])>

    >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
    >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
    >>> concatted = tf.keras.layers.Concatenate()([x1, x2])
    >>> concatted.shape
    TensorShape([5, 16])

    """
    axis: Incomplete
    supports_masking: bool
    def __init__(self, axis: int = -1, **kwargs) -> None:
        """Instantiates a Concatenate layer.

        >>> x = np.arange(20).reshape(2, 2, 5)
        >>> print(x)
        [[[ 0  1  2  3  4]
          [ 5  6  7  8  9]]
         [[10 11 12 13 14]
          [15 16 17 18 19]]]
        >>> y = np.arange(20, 30).reshape(2, 1, 5)
        >>> print(y)
        [[[20 21 22 23 24]]
         [[25 26 27 28 29]]]
        >>> tf.keras.layers.Concatenate(axis=1)([x, y])
        <tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
        array([[[ 0,  1,  2,  3,  4],
                [ 5,  6,  7,  8,  9],
                [20, 21, 22, 23, 24]],
               [[10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19],
                [25, 26, 27, 28, 29]]])>

        Args:
          axis: Axis along which to concatenate.
          **kwargs: standard layer keyword arguments.
        """
    def build(self, input_shape) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...
    def get_config(self): ...

def concatenate(inputs, axis: int = -1, **kwargs):
    """Functional interface to the `Concatenate` layer.

    >>> x = np.arange(20).reshape(2, 2, 5)
    >>> print(x)
    [[[ 0  1  2  3  4]
      [ 5  6  7  8  9]]
     [[10 11 12 13 14]
      [15 16 17 18 19]]]
    >>> y = np.arange(20, 30).reshape(2, 1, 5)
    >>> print(y)
    [[[20 21 22 23 24]]
     [[25 26 27 28 29]]]
    >>> tf.keras.layers.concatenate([x, y],
    ...                             axis=1)
    <tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
    array([[[ 0,  1,  2,  3,  4],
          [ 5,  6,  7,  8,  9],
          [20, 21, 22, 23, 24]],
         [[10, 11, 12, 13, 14],
          [15, 16, 17, 18, 19],
          [25, 26, 27, 28, 29]]])>

    Args:
        inputs: A list of input tensors.
        axis: Concatenation axis.
        **kwargs: Standard layer keyword arguments.

    Returns:
        A tensor, the concatenation of the inputs alongside axis `axis`.
    """
