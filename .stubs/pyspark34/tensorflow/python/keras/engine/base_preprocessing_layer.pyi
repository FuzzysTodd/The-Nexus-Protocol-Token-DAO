import abc
from _typeshed import Incomplete
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import data_adapter as data_adapter
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.utils import tf_utils as tf_utils, version_utils as version_utils
from tensorflow.python.ops import math_ops as math_ops, sparse_ops as sparse_ops, variables as variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util.tf_export import keras_export as keras_export

class PreprocessingLayer(Layer, metaclass=abc.ABCMeta):
    """Base class for Preprocessing Layers.

  **Don't use this class directly: it's an abstract base class!** You may
  be looking for one of the many built-in
  [preprocessing layers](https://keras.io/guides/preprocessing_layers/)
  instead.

  Preprocessing layers are layers whose state gets computed before model
  training starts. They do not get updated during training.
  Most preprocessing layers implement an `adapt()` method for state computation.

  The `PreprocessingLayer` class is the base class you would subclass to
  implement your own preprocessing layers.

  Attributes:
    streaming: Whether a layer can be adapted multiple times without resetting
      the state of the layer.
  """
    def __init__(self, streaming: bool = True, **kwargs) -> None: ...
    @property
    def streaming(self):
        """Whether `adapt` can be called twice without resetting the state."""
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
    def merge_state(self, layers) -> None:
        """Merge the statistics of multiple preprocessing layers.

    This layer will contain the merged state.

    Arguments:
      layers: Layers whose statistics should be merge with the statistics of
        this layer.
    """
    def finalize_state(self) -> None:
        """Finalize the statistics for the preprocessing layer.

    This method is called at the end of `adapt` or after restoring a serialized
    preprocessing layer's state. This method handles any one-time operations
    that should occur on the layer's state before `Layer.__call__`.
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
      run_eagerly: Bool. Defaults to `False`. If `True`, this `Model`'s logic
        will not be wrapped in a `tf.function`. Recommended to leave this as
        `None` unless your `Model` cannot be run inside a `tf.function`.
        steps_per_execution: Int. Defaults to 1. The number of batches to run
          during each `tf.function` call. Running multiple batches inside a
          single `tf.function` call can greatly improve performance on TPUs or
          small models with a large Python overhead.
    """
    def adapt(self, data, batch_size: Incomplete | None = None, steps: Incomplete | None = None, reset_state: bool = True) -> None:
        """Fits the state of the preprocessing layer to the data being passed.

    After calling `adapt` on a layer, a preprocessing layer's state will not
    update during training. In order to make preprocessing layers efficient in
    any distribution context, they are kept constant with respect to any
    compiled `tf.Graph`s that call the layer. This does not affect the layer use
    when adapting each layer only once, but if you adapt a layer multiple times
    you will need to take care to re-compile any compiled functions as follows:

     * If you are adding a preprocessing layer to a `keras.Model`, you need to
       call `model.compile` after each subsequent call to `adapt`.
     * If you are calling a preprocessing layer inside `tf.data.Dataset.map`,
       you should call `map` again on the input `tf.data.Dataset` after each
       `adapt`.
     * If you are using a `tf.function` directly which calls a preprocessing
       layer, you need to call `tf.function` again on your callable after
       each subsequent call to `adapt`.

    `tf.keras.Model` example with multiple adapts:

    >>> layer = tf.keras.layers.experimental.preprocessing.Normalization(
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

    >>> layer = tf.keras.layers.experimental.preprocessing.Normalization(
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

    Arguments:
        data: The data to train on. It can be passed either as a tf.data
          Dataset, or as a numpy array.
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
        reset_state: Optional argument specifying whether to clear the state of
          the layer at the start of the call to `adapt`, or whether to start
          from the existing state. This argument may not be relevant to all
          preprocessing layers: a subclass of PreprocessingLayer may choose to
          throw if 'reset_state' is set to False.
    """

class CombinerPreprocessingLayer(PreprocessingLayer):
    """Base class for PreprocessingLayers that do computation using a Combiner.

  This class provides several helper methods to make creating a
  PreprocessingLayer easier. It assumes that the core of your computation will
  be done via a Combiner object. Subclassing this class to create a
  PreprocessingLayer allows your layer to be compatible with distributed
  computation.

  This class is compatible with Tensorflow 2.0+.
  """
    state_variables: Incomplete
    def __init__(self, combiner, **kwargs) -> None: ...
    def reset_state(self) -> None: ...
    def update_state(self, data) -> None: ...
    def merge_state(self, layers) -> None: ...
    def finalize_state(self) -> None: ...
    def compile(self, run_eagerly: Incomplete | None = None, steps_per_execution: Incomplete | None = None) -> None: ...
    def adapt(self, data, batch_size: Incomplete | None = None, steps: Incomplete | None = None, reset_state: bool = True) -> None: ...

def convert_to_list(values, sparse_default_value: Incomplete | None = None):
    """Convert a TensorLike, CompositeTensor, or ndarray into a Python list."""

class Combiner(metaclass=abc.ABCMeta):
    """Functional object that defines a shardable computation.

  This object defines functions required to create and manipulate data objects.
  These data objects, referred to below as 'accumulators', are computation-
  specific and may be implemented alongside concrete subclasses of Combiner
  (if necessary - some computations may be simple enough that standard Python
  types can be used as accumulators).

  The intent for this class is that by describing computations in this way, we
  can arbitrarily shard a dataset, perform computations on a subset, and then
  merge the computation into a final result. This enables distributed
  computation.

  The combiner itself does not own any state - all computational state is owned
  by the accumulator objects. This is so that we can have an arbitrary number of
  Combiners (thus sharding the computation N ways) without risking any change
  to the underlying computation. These accumulator objects are uniquely
  associated with each Combiner; a Combiner defines what the accumulator object
  should be and will only work with accumulators of that type.
  """
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def compute(self, batch_values, accumulator: Incomplete | None = None):
        """Compute a step in this computation, returning a new accumulator.

    This method computes a step of the computation described by this Combiner.
    If an accumulator is passed, the data in that accumulator is also used; so
    compute(batch_values) results in f(batch_values), while
    compute(batch_values, accumulator) results in
    merge(f(batch_values), accumulator).

    Args:
      batch_values: A list of ndarrays representing the values of the inputs for
        this step of the computation.
      accumulator: the current accumulator. Can be None.

    Returns:
      An accumulator that includes the passed batch of inputs.
    """
    @abc.abstractmethod
    def merge(self, accumulators):
        """Merge several accumulators to a single accumulator.

    This method takes the partial values in several accumulators and combines
    them into a single accumulator. This computation must not be order-specific
    (that is, merge([a, b]) must return the same result as merge([b, a]).

    Args:
      accumulators: the accumulators to merge, as a list.

    Returns:
      A merged accumulator.
    """
    @abc.abstractmethod
    def extract(self, accumulator):
        """Convert an accumulator into a dict of output values.

    Args:
      accumulator: The accumulator to convert.

    Returns:
      A dict of ndarrays representing the data in this accumulator.
    """
    @abc.abstractmethod
    def restore(self, output):
        """Create an accumulator based on 'output'.

    This method creates a new accumulator with identical internal state to the
    one used to create the data in 'output'. This means that if you do

    output_data = combiner.extract(accumulator_1)
    accumulator_2 = combiner.restore(output_data)

    then accumulator_1 and accumulator_2 will have identical internal state, and
    computations using either of them will be equivalent.

    Args:
      output: The data output from a previous computation. Should be in the same
        form as provided by 'extract_output'.

    Returns:
      A new accumulator.
    """
    @abc.abstractmethod
    def serialize(self, accumulator):
        """Serialize an accumulator for a remote call.

    This function serializes an accumulator to be sent to a remote process.

    Args:
      accumulator: The accumulator to serialize.

    Returns:
      A byte string representing the passed accumulator.
    """
    @abc.abstractmethod
    def deserialize(self, encoded_accumulator):
        """Deserialize an accumulator received from 'serialize()'.

    This function deserializes an accumulator serialized by 'serialize()'.

    Args:
      encoded_accumulator: A byte string representing an accumulator.

    Returns:
      The accumulator represented by the passed byte_string.
    """
