import abc
from _typeshed import Incomplete
from keras.engine import data_adapter as data_adapter
from keras.engine.base_layer import Layer as Layer
from keras.utils import version_utils as version_utils

keras_kpl_gauge: Incomplete

class PreprocessingLayer(Layer, metaclass=abc.ABCMeta):
    """Base class for Preprocessing Layers.

    **Don't use this class directly: it's an abstract base class!** You may
    be looking for one of the many built-in
    [preprocessing layers](https://keras.io/guides/preprocessing_layers/)
    instead.

    Preprocessing layers are layers whose state gets computed before model
    training starts. They do not get updated during training. Most
    preprocessing layers implement an `adapt()` method for state computation.

    The `PreprocessingLayer` class is the base class you would subclass to
    implement your own preprocessing layers.
    """
    def __init__(self, **kwargs) -> None: ...
    @property
    def is_adapted(self):
        """Whether the layer has been fit to data already."""
    def update_state(self, data) -> None:
        """Accumulates statistics for the preprocessing layer.

        Arguments:
          data: A mini-batch of inputs to the layer.
        """
    def reset_state(self) -> None:
        """Resets the statistics of the preprocessing layer."""
    def finalize_state(self) -> None:
        """Finalize the statistics for the preprocessing layer.

        This method is called at the end of `adapt` or after restoring a
        serialized preprocessing layer's state. This method handles any one-time
        operations that should occur on the layer's state before
        `Layer.__call__`.
        """
    def make_adapt_function(self):
        """Creates a function to execute one step of `adapt`.

        This method can be overridden to support custom adapt logic.
        This method is called by `PreprocessingLayer.adapt`.

        Typically, this method directly controls `tf.function` settings,
        and delegates the actual state update logic to
        `PreprocessingLayer.update_state`.

        This function is cached the first time `PreprocessingLayer.adapt`
        is called. The cache is cleared whenever `PreprocessingLayer.compile`
        is called.

        Returns:
          Function. The function created by this method should accept a
          `tf.data.Iterator`, retrieve a batch, and update the state of the
          layer.
        """
    def compile(self, run_eagerly: Incomplete | None = None, steps_per_execution: Incomplete | None = None) -> None:
        """Configures the layer for `adapt`.

        Arguments:
          run_eagerly: Bool. Defaults to `False`. If `True`, this `Model`'s
            logic will not be wrapped in a `tf.function`. Recommended to leave
            this as `None` unless your `Model` cannot be run inside a
            `tf.function`.
          steps_per_execution: Int. Defaults to 1. The number of batches to run
            during each `tf.function` call. Running multiple batches inside a
            single `tf.function` call can greatly improve performance on TPUs or
            small models with a large Python overhead.
        """
    def adapt(self, data, batch_size: Incomplete | None = None, steps: Incomplete | None = None) -> None:
        """Fits the state of the preprocessing layer to the data being passed.

        After calling `adapt` on a layer, a preprocessing layer's state will not
        update during training. In order to make preprocessing layers efficient
        in any distribution context, they are kept constant with respect to any
        compiled `tf.Graph`s that call the layer. This does not affect the layer
        use when adapting each layer only once, but if you adapt a layer
        multiple times you will need to take care to re-compile any compiled
        functions as follows:

         * If you are adding a preprocessing layer to a `keras.Model`, you need
           to call `model.compile` after each subsequent call to `adapt`.
         * If you are calling a preprocessing layer inside
          `tf.data.Dataset.map`, you should call `map` again on the input
          `tf.data.Dataset` after each `adapt`.
         * If you are using a `tf.function` directly which calls a preprocessing
           layer, you need to call `tf.function` again on your callable after
           each subsequent call to `adapt`.

        `tf.keras.Model` example with multiple adapts:

        >>> layer = tf.keras.layers.Normalization(
        ...     axis=None)
        >>> layer.adapt([0, 2])
        >>> model = tf.keras.Sequential(layer)
        >>> model.predict([0, 1, 2])
        array([-1.,  0.,  1.], dtype=float32)
        >>> layer.adapt([-1, 1])
        >>> model.compile() # This is needed to re-compile model.predict!
        >>> model.predict([0, 1, 2])
        array([0., 1., 2.], dtype=float32)

        `tf.data.Dataset` example with multiple adapts:

        >>> layer = tf.keras.layers.Normalization(
        ...     axis=None)
        >>> layer.adapt([0, 2])
        >>> input_ds = tf.data.Dataset.range(3)
        >>> normalized_ds = input_ds.map(layer)
        >>> list(normalized_ds.as_numpy_iterator())
        [array([-1.], dtype=float32),
         array([0.], dtype=float32),
         array([1.], dtype=float32)]
        >>> layer.adapt([-1, 1])
        >>> normalized_ds = input_ds.map(layer) # Re-map over the input dataset.
        >>> list(normalized_ds.as_numpy_iterator())
        [array([0.], dtype=float32),
         array([1.], dtype=float32),
         array([2.], dtype=float32)]

        `adapt()` is meant only as a single machine utility to compute layer
        state.  To analyze a dataset that cannot fit on a single machine, see
        [Tensorflow Transform](
        https://www.tensorflow.org/tfx/transform/get_started)
        for a multi-machine, map-reduce solution.

        Arguments:
            data: The data to train on. It can be passed either as a tf.data
              Dataset, or as a numpy array.
            batch_size: Integer or `None`.
                Number of samples per state update. If unspecified,
                `batch_size` will default to 32.  Do not specify the
                `batch_size` if your data is in the form of datasets,
                generators, or `keras.utils.Sequence` instances (since they
                generate batches).
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
