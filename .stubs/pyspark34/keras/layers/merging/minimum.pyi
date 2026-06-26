from keras.layers.merging.base_merge import _Merge

class Minimum(_Merge):
    """Layer that computes the minimum (element-wise) a list of inputs.

    It takes as input a list of tensors, all of the same shape, and returns
    a single tensor (also of the same shape).

    >>> tf.keras.layers.Minimum()([np.arange(5).reshape(5, 1),
    ...                            np.arange(5, 10).reshape(5, 1)])
    <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
    array([[0],
         [1],
         [2],
         [3],
         [4]])>

    >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
    >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
    >>> minned = tf.keras.layers.Minimum()([x1, x2])
    >>> minned.shape
    TensorShape([5, 8])
    """

def minimum(inputs, **kwargs):
    """Functional interface to the `Minimum` layer.

    Args:
        inputs: A list of input tensors.
        **kwargs: Standard layer keyword arguments.

    Returns:
        A tensor, the element-wise minimum of the inputs.
    """
