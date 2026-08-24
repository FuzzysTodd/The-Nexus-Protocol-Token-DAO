from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_preprocessing_layer as base_preprocessing_layer

class Normalization(base_preprocessing_layer.PreprocessingLayer):
    """A preprocessing layer which normalizes continuous features.

    This layer will shift and scale inputs into a distribution centered around
    0 with standard deviation 1. It accomplishes this by precomputing the mean
    and variance of the data, and calling `(input - mean) / sqrt(var)` at
    runtime.

    The mean and variance values for the layer must be either supplied on
    construction or learned via `adapt()`. `adapt()` will compute the mean and
    variance of the data and store them as the layer's weights. `adapt()` should
    be called before `fit()`, `evaluate()`, or `predict()`.

    For an overview and full list of preprocessing layers, see the preprocessing
    [guide](https://www.tensorflow.org/guide/keras/preprocessing_layers).

    Args:
        axis: Integer, tuple of integers, or None. The axis or axes that should
          have a separate mean and variance for each index in the shape. For
          example, if shape is `(None, 5)` and `axis=1`, the layer will track 5
          separate mean and variance values for the last axis. If `axis` is set
          to `None`, the layer will normalize all elements in the input by a
          scalar mean and variance. Defaults to -1, where the last axis of the
          input is assumed to be a feature dimension and is normalized per
          index. Note that in the specific case of batched scalar inputs where
          the only axis is the batch axis, the default will normalize each index
          in the batch separately. In this case, consider passing `axis=None`.
        mean: The mean value(s) to use during normalization. The passed value(s)
          will be broadcast to the shape of the kept axes above; if the value(s)
          cannot be broadcast, an error will be raised when this layer's
          `build()` method is called.
        variance: The variance value(s) to use during normalization. The passed
          value(s) will be broadcast to the shape of the kept axes above; if the
          value(s) cannot be broadcast, an error will be raised when this
          layer's `build()` method is called.
        invert: If True, this layer will apply the inverse transformation
          to its inputs: it would turn a normalized input back into its
          original form.

    Examples:

    Calculate a global mean and variance by analyzing the dataset in `adapt()`.

    >>> adapt_data = np.array([1., 2., 3., 4., 5.], dtype='float32')
    >>> input_data = np.array([1., 2., 3.], dtype='float32')
    >>> layer = tf.keras.layers.Normalization(axis=None)
    >>> layer.adapt(adapt_data)
    >>> layer(input_data)
    <tf.Tensor: shape=(3,), dtype=float32, numpy=
    array([-1.4142135, -0.70710677, 0.], dtype=float32)>

    Calculate a mean and variance for each index on the last axis.

    >>> adapt_data = np.array([[0., 7., 4.],
    ...                        [2., 9., 6.],
    ...                        [0., 7., 4.],
    ...                        [2., 9., 6.]], dtype='float32')
    >>> input_data = np.array([[0., 7., 4.]], dtype='float32')
    >>> layer = tf.keras.layers.Normalization(axis=-1)
    >>> layer.adapt(adapt_data)
    >>> layer(input_data)
    <tf.Tensor: shape=(1, 3), dtype=float32, numpy=
    array([-1., -1., -1.], dtype=float32)>

    Pass the mean and variance directly.

    >>> input_data = np.array([[1.], [2.], [3.]], dtype='float32')
    >>> layer = tf.keras.layers.Normalization(mean=3., variance=2.)
    >>> layer(input_data)
    <tf.Tensor: shape=(3, 1), dtype=float32, numpy=
    array([[-1.4142135 ],
           [-0.70710677],
           [ 0.        ]], dtype=float32)>

    Use the layer to de-normalize inputs (after adapting the layer).

    >>> adapt_data = np.array([[0., 7., 4.],
    ...                        [2., 9., 6.],
    ...                        [0., 7., 4.],
    ...                        [2., 9., 6.]], dtype='float32')
    >>> input_data = np.array([[1., 2., 3.]], dtype='float32')
    >>> layer = tf.keras.layers.Normalization(axis=-1, invert=True)
    >>> layer.adapt(adapt_data)
    >>> layer(input_data)
    <tf.Tensor: shape=(1, 3), dtype=float32, numpy=
    array([2., 10., 8.], dtype=float32)>
    """
    axis: Incomplete
    input_mean: Incomplete
    input_variance: Incomplete
    invert: Incomplete
    def __init__(self, axis: int = -1, mean: Incomplete | None = None, variance: Incomplete | None = None, invert: bool = False, **kwargs) -> None: ...
    adapt_mean: Incomplete
    adapt_variance: Incomplete
    count: Incomplete
    mean: Incomplete
    variance: Incomplete
    def build(self, input_shape) -> None: ...
    def adapt(self, data, batch_size: Incomplete | None = None, steps: Incomplete | None = None) -> None:
        """Computes the mean and variance of values in a dataset.

        Calling `adapt()` on a `Normalization` layer is an alternative to
        passing in `mean` and `variance` arguments during layer construction. A
        `Normalization` layer should always either be adapted over a dataset or
        passed `mean` and `variance`.

        During `adapt()`, the layer will compute a `mean` and `variance`
        separately for each position in each axis specified by the `axis`
        argument. To calculate a single `mean` and `variance` over the input
        data, simply pass `axis=None`.

        In order to make `Normalization` efficient in any distribution context,
        the computed mean and variance are kept static with respect to any
        compiled `tf.Graph`s that call the layer. As a consequence, if the layer
        is adapted a second time, any models using the layer should be
        re-compiled. For more information see
        `tf.keras.layers.experimental.preprocessing.PreprocessingLayer.adapt`.

        `adapt()` is meant only as a single machine utility to compute layer
        state.  To analyze a dataset that cannot fit on a single machine, see
        [Tensorflow Transform](
        https://www.tensorflow.org/tfx/transform/get_started)
        for a multi-machine, map-reduce solution.

        Arguments:
          data: The data to train on. It can be passed either as a
              `tf.data.Dataset`, or as a numpy array.
          batch_size: Integer or `None`.
              Number of samples per state update.
              If unspecified, `batch_size` will default to 32.
              Do not specify the `batch_size` if your data is in the
              form of datasets, generators, or `keras.utils.Sequence` instances
              (since they generate batches).
          steps: Integer or `None`.
              Total number of steps (batches of samples)
              When training with input tensors such as
              TensorFlow data tensors, the default `None` is equal to
              the number of samples in your dataset divided by
              the batch size, or 1 if that cannot be determined. If x is a
              `tf.data` dataset, and 'steps' is None, the epoch will run until
              the input dataset is exhausted. When passing an infinitely
              repeating dataset, you must specify the `steps` argument. This
              argument is not supported with array inputs.
        """
    def update_state(self, data) -> None: ...
    def reset_state(self) -> None: ...
    def finalize_state(self) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def compute_output_signature(self, input_spec): ...
    def get_config(self): ...
