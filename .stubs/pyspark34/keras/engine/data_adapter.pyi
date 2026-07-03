import abc
from _typeshed import Incomplete
from collections.abc import Generator
from keras import backend as backend
from keras.distribute import distributed_training_utils as distributed_training_utils
from keras.engine import training_utils as training_utils
from keras.utils import data_utils as data_utils, dataset_creator as dataset_creator, tf_utils as tf_utils

keras_data_adapter_gauge: Incomplete

class DataAdapter(metaclass=abc.ABCMeta):
    '''Base class for input data adapter.

    In TF 2.0, tf.data is the preferred API for user to feed in data. In order
    to simplify the training code path, all the input data object will be
    converted to `tf.data.Dataset` if possible.

    Note that since this class is mainly targeted for TF 2.0, it might have a
    lot of assumptions under the hood, e.g. eager context by default,
    distribution strategy, etc. In the meantime, some legacy feature support
    might be dropped, eg, Iterator from dataset API in v1, etc.

    The sample usage of this class is like:

    ```
    x = tf.data.Dataset.range(100)
    adapter_cls = [NumpyArrayDataAdapter, ..., DatasetAdapter]
    applicable_adapters = [cls for cls in adapter_cls if cls.can_handle(x)]
    if len(applicable_adapters) != 1:
      raise ValueError("Expect only one adapter class to handle the input")

    dataset = applicable_adapters[0](x).get_dataset()
    for data in dataset:
      # training
    ```
    '''
    @staticmethod
    def can_handle(x, y: Incomplete | None = None) -> None:
        """Whether the current DataAdapter could handle the input x and y.

        Structure wise, x and y can be single object, or list of objects if
        there multiple input/output, or dictionary of objects when the
        input/output are named.

        Args:
          x: input features.
          y: target labels. Note that y could be None in the case of prediction.

        Returns:
          boolean
        """
    @abc.abstractmethod
    def __init__(self, x, y: Incomplete | None = None, **kwargs):
        """Create a DataAdapter based on data inputs.

        The caller must make sure to call `can_handle()` first before invoking
        this method. Provide unsupported data type will result into unexpected
        behavior.

        Args:
          x: input features.
          y: target labels. Note that y could be None in the case of prediction.
          **kwargs: Other keyword arguments for DataAdapter during the
            construction of the tf.dataset.Dataset. For example:
            - Numpy data might have `sample_weights` which will be used for
              weighting the loss function during training.
            - Numpy data might need to have `batch_size` parameter when
              constructing the dataset and iterator.
            - Certain input might need to be distribution strategy aware. When
              `distribution_strategy` is passed, the created dataset need to
              respect the strategy.
            DataAdapter might choose to ignore any keyword argument if it
            doesn't use it, or raise exception if any required argument is not
            provided.
        """
    @abc.abstractmethod
    def get_dataset(self):
        """Get a dataset instance for the current DataAdapter.

        Note that the dataset returned does not repeat for epoch, so caller
        might need to create new iterator for the same dataset at the beginning
        of the epoch. This behavior might change in the future.

        Returns:
          A `tf.data.Dataset`. Caller might use the dataset in different
          context, e.g. iter(dataset) in eager to get the value directly, or in
          graph mode, provide the iterator tensor to Keras model function.
        """
    @abc.abstractmethod
    def get_size(self):
        """Return the size (number of batches) for the dataset created.

        For certain type of the data input, the number of batches is known, eg
        for Numpy data, the size is same as (number_of_element / batch_size).
        Whereas for dataset or python generator, the size is unknown since it
        may or may not have an end state.

        Returns:
          int, the number of batches for the dataset, or None if it is unknown.
          The caller could use this to control the loop of training, show
          progress bar, or handle unexpected StopIteration error.
        """
    @abc.abstractmethod
    def batch_size(self):
        """Return the batch size of the dataset created.

        For certain type of the data input, the batch size is known, and even
        required, like numpy array. Whereas for dataset, the batch is unknown
        unless we take a peek.

        Returns:
          int, the batch size of the dataset, or None if it is unknown.
        """
    def representative_batch_size(self):
        """Return a representative size for batches in the dataset.

        This is not guaranteed to be the batch size for all batches in the
        dataset. It just needs to be a rough approximation for batch sizes in
        the dataset.

        Returns:
          int, a representative size for batches found in the dataset,
          or None if it is unknown.
        """
    @abc.abstractmethod
    def has_partial_batch(self):
        """Whether the dataset has partial batch at the end."""
    @abc.abstractmethod
    def partial_batch_size(self):
        """The size of the final partial batch for dataset.

        Will return None if has_partial_batch is False or batch_size is None.
        """
    @abc.abstractmethod
    def should_recreate_iterator(self):
        """Returns whether a new iterator should be created every epoch."""
    def get_samples(self):
        """Returns number of samples in the data, or `None`."""
    def on_epoch_end(self) -> None:
        """A hook called after each epoch."""

class TensorLikeDataAdapter(DataAdapter):
    """Adapter that handles Tensor-like objects, e.g. EagerTensor and NumPy."""
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def __init__(self, x, y: Incomplete | None = None, sample_weights: Incomplete | None = None, sample_weight_modes: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, steps: Incomplete | None = None, shuffle: bool = False, **kwargs) -> None: ...
    def slice_inputs(self, indices_dataset, inputs):
        """Slice inputs into a Dataset of batches.

        Given a Dataset of batch indices and the unsliced inputs,
        this step slices the inputs in a parallelized fashion
        and produces a dataset of input batches.

        Args:
          indices_dataset: A Dataset of batched indices
          inputs: A python data structure that contains the inputs, targets,
            and possibly sample weights.

        Returns:
          A Dataset of input batches matching the batch indices.
        """
    def get_dataset(self): ...
    def get_size(self): ...
    def batch_size(self): ...
    def has_partial_batch(self): ...
    def partial_batch_size(self): ...
    def should_recreate_iterator(self): ...

class GenericArrayLikeDataAdapter(TensorLikeDataAdapter):
    """Adapter that handles array-like data without forcing it into memory.

    This adapter handles array-like datasets that may be too big to fully
    fit into memory.

    Specifically, this adapter handles any Python class which implements:
    `__get_item__`, `__len__`, `shape`, and `dtype` with the same meanings
    as Numpy, but it ignores any case where all the inputs are Tensors or Numpy
    arrays (because that case is handled by the base TensorLikeDataAdapter).

    It ignores scipy sparse matrices and Composite Tensors because those are
    handled by the CompositeTensorDataAdapter.

    It also does not handle lists/tuples of scalars, because those are handled
    by the ListsOfScalarsDataAdapter.
    """
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def slice_inputs(self, indices_dataset, inputs):
        """Slice inputs into a Dataset of batches.

        Given a Dataset of batch indices and the unsliced inputs,
        this step slices the inputs in a parallelized fashion
        and produces a dataset of input batches.

        Args:
          indices_dataset: A Dataset of batched indices
          inputs: A python data structure that contains the inputs, targets,
            and possibly sample weights.

        Returns:
          A Dataset of input batches matching the batch indices.
        """

class DatasetCreatorAdapter(DataAdapter):
    """Adapter that handles dataset functions."""
    dataset_creator: Incomplete
    steps: Incomplete
    strategy: Incomplete
    def __init__(self, x, y, steps: Incomplete | None = None, distribution_strategy: Incomplete | None = None, **kwargs) -> None: ...
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def should_recreate_iterator(self): ...
    def get_size(self) -> None: ...
    def get_dataset(self): ...
    def batch_size(self) -> None: ...
    def has_partial_batch(self) -> None: ...
    def partial_batch_size(self) -> None: ...

class CompositeTensorDataAdapter(DataAdapter):
    """Adapter that handles composite tensor."""
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def __init__(self, x, y: Incomplete | None = None, sample_weights: Incomplete | None = None, sample_weight_modes: Incomplete | None = None, batch_size: Incomplete | None = None, steps: Incomplete | None = None, shuffle: bool = False, **kwargs) -> None: ...
    def get_dataset(self): ...
    def get_size(self): ...
    def batch_size(self): ...
    def has_partial_batch(self): ...
    def partial_batch_size(self): ...
    def should_recreate_iterator(self): ...

class ListsOfScalarsDataAdapter(DataAdapter):
    """Adapter that handles lists of scalars and lists of lists of scalars."""
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def __init__(self, x, y: Incomplete | None = None, sample_weights: Incomplete | None = None, sample_weight_modes: Incomplete | None = None, batch_size: Incomplete | None = None, shuffle: bool = False, **kwargs) -> None: ...
    def get_dataset(self): ...
    def get_size(self): ...
    def batch_size(self): ...
    def has_partial_batch(self): ...
    def partial_batch_size(self): ...
    def should_recreate_iterator(self): ...

class DatasetAdapter(DataAdapter):
    """Adapter that handles `tf.data.Dataset`."""
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def __init__(self, x, y: Incomplete | None = None, sample_weights: Incomplete | None = None, steps: Incomplete | None = None, **kwargs) -> None: ...
    def get_dataset(self): ...
    def get_size(self) -> None: ...
    def batch_size(self) -> None: ...
    def has_partial_batch(self): ...
    def partial_batch_size(self) -> None: ...
    def should_recreate_iterator(self): ...

class GeneratorDataAdapter(DataAdapter):
    """Adapter that handles python generators and iterators."""
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def __init__(self, x, y: Incomplete | None = None, sample_weights: Incomplete | None = None, workers: int = 1, use_multiprocessing: bool = False, max_queue_size: int = 10, model: Incomplete | None = None, **kwargs) -> None: ...
    def get_dataset(self): ...
    def get_size(self) -> None: ...
    def batch_size(self) -> None: ...
    def representative_batch_size(self): ...
    def has_partial_batch(self): ...
    def partial_batch_size(self) -> None: ...
    def should_recreate_iterator(self): ...

class KerasSequenceAdapter(GeneratorDataAdapter):
    """Adapter that handles `keras.utils.Sequence`."""
    @staticmethod
    def can_handle(x, y: Incomplete | None = None): ...
    def __init__(self, x, y: Incomplete | None = None, sample_weights: Incomplete | None = None, shuffle: bool = False, workers: int = 1, use_multiprocessing: bool = False, max_queue_size: int = 10, model: Incomplete | None = None, **kwargs) -> None: ...
    def get_size(self): ...
    def should_recreate_iterator(self): ...
    def on_epoch_end(self) -> None: ...

ALL_ADAPTER_CLS: Incomplete

def select_data_adapter(x, y):
    """Selects a data adapter that can handle a given x and y."""
def is_none_or_empty(inputs): ...
def broadcast_sample_weight_modes(target_structure, sample_weight_modes):
    """Match sample_weight_modes structure with output structure."""

class DataHandler:
    """Handles iterating over epoch-level `tf.data.Iterator` objects."""
    def __init__(self, x, y: Incomplete | None = None, sample_weight: Incomplete | None = None, batch_size: Incomplete | None = None, steps_per_epoch: Incomplete | None = None, initial_epoch: int = 0, epochs: int = 1, shuffle: bool = False, class_weight: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, model: Incomplete | None = None, steps_per_execution: Incomplete | None = None, distribute: bool = True) -> None:
        """Initializes a `DataHandler`.

        Arguments:
          x: See `Model.fit`.
          y: See `Model.fit`.
          sample_weight: See `Model.fit`.
          batch_size: See `Model.fit`.
          steps_per_epoch: See `Model.fit`.
          initial_epoch: See `Model.fit`.
          epochs: See `Model.fit`.
          shuffle: See `Model.fit`.
          class_weight: See `Model.fit`.
          max_queue_size: See `Model.fit`.
          workers: See `Model.fit`.
          use_multiprocessing: See `Model.fit`.
          model: The `Model` instance. Needed in order to correctly `build` the
            `Model` using generator-like inputs (see `GeneratorDataAdapter`).
          steps_per_execution: See `Model.compile`.
          distribute: Whether to distribute the `tf.dataset`.
            `PreprocessingLayer.adapt` does not support distributed datasets,
            `Model` should always set this to `True`.
        """
    def enumerate_epochs(self) -> Generator[Incomplete, None, None]:
        """Yields `(epoch, tf.data.Iterator)`."""
    def sync(self) -> None: ...
    def catch_stop_iteration(self) -> Generator[None, None, None]:
        """Catches errors when an iterator runs out of data."""
    def steps(self) -> Generator[Incomplete, None, None]:
        """Yields steps for the current epoch."""
    @property
    def step_increment(self):
        """The number to increment the step for `on_batch_end` methods."""
    @property
    def inferred_steps(self):
        """The inferred steps per epoch of the created `Dataset`.

        This will be `None` in the case where:

        (1) A `Dataset` of unknown cardinality was passed to the `DataHandler`,
        (2) `steps_per_epoch` was not provided, and
        (3) The first epoch of iteration has not yet completed.

        Returns:
          The inferred steps per epoch of the created `Dataset`.
        """
    @property
    def should_sync(self): ...

class _ClusterCoordinatorDataHandler(DataHandler):
    """A `DataHandler` that is compatible with `ClusterCoordinator`."""
    def __init__(self, x, y: Incomplete | None = None, **kwargs) -> None: ...
    def sync(self) -> None: ...

def get_data_handler(*args, **kwargs):
    """Creates a `DataHandler`, providing standardized access to a `Dataset`.

    See `DataHandler` for the list and definition of the arguments. See the
    implementation of `Model.fit()`, `evaluate()`, or `predict()` methods
    for complete usage examples. As a rule of tumb, `get_data_handler()` accepts
    the same inputs as the `x` argument of `Model.fit()`.

    Example:

    ```python
      def step(iterator):
        data = next(iterator)
        # result <= Do something with data
        return result
      tf_step = tf.function(step, reduce_retracing=True)

      # Assume x is a tf.data Dataset.
      data_handler = data_adapter.get_data_handler(x=x)
      # Epoch iteration
      for epo_idx, iterator in data_handler.enumerate_epochs():
          # Stop on dataset exhaustion.
          with data_handler.catch_stop_iteration():
            for step in data_handler.steps(): # Step iteration
                step_result = step(iterator)
    ```

    Args:
      *args: Arguments passed to the `DataHandler` constructor.
      **kwargs: Arguments passed to the `DataHandler` constructor.

    Returns:
      A `DataHandler` object. If the model's cluster coordinate is set (e.g. the
      model was defined under a parameter-server strategy), returns a
      `_ClusterCoordinatorDataHandler`.

    """
def train_validation_split(arrays, validation_split):
    """Split arrays into train and validation subsets in deterministic order.

    The last part of data will become validation data.

    Args:
      arrays: Tensors to split. Allowed inputs are arbitrarily nested structures
        of Tensors and NumPy arrays.
      validation_split: Float between 0 and 1. The proportion of the dataset to
        include in the validation split. The rest of the dataset will be
        included in the training split.
    Returns:
      `(train_arrays, validation_arrays)`
    """
def unpack_x_y_sample_weight(data):
    """Unpacks user-provided data tuple.

    This is a convenience utility to be used when overriding
    `Model.train_step`, `Model.test_step`, or `Model.predict_step`.
    This utility makes it easy to support data of the form `(x,)`,
    `(x, y)`, or `(x, y, sample_weight)`.

    Standalone usage:

    >>> features_batch = tf.ones((10, 5))
    >>> labels_batch = tf.zeros((10, 5))
    >>> data = (features_batch, labels_batch)
    >>> # `y` and `sample_weight` will default to `None` if not provided.
    >>> x, y, sample_weight = tf.keras.utils.unpack_x_y_sample_weight(data)
    >>> sample_weight is None
    True

    Example in overridden `Model.train_step`:

    ```python
    class MyModel(tf.keras.Model):

      def train_step(self, data):
        # If `sample_weight` is not provided, all samples will be weighted
        # equally.
        x, y, sample_weight = tf.keras.utils.unpack_x_y_sample_weight(data)

        with tf.GradientTape() as tape:
          y_pred = self(x, training=True)
          loss = self.compiled_loss(
            y, y_pred, sample_weight, regularization_losses=self.losses)
          trainable_variables = self.trainable_variables
          gradients = tape.gradient(loss, trainable_variables)
          self.optimizer.apply_gradients(zip(gradients, trainable_variables))

        self.compiled_metrics.update_state(y, y_pred, sample_weight)
        return {m.name: m.result() for m in self.metrics}
    ```

    Args:
      data: A tuple of the form `(x,)`, `(x, y)`, or `(x, y, sample_weight)`.

    Returns:
      The unpacked tuple, with `None`s for `y` and `sample_weight` if they are
      not provided.
    """
def pack_x_y_sample_weight(x, y: Incomplete | None = None, sample_weight: Incomplete | None = None):
    """Packs user-provided data into a tuple.

    This is a convenience utility for packing data into the tuple formats
    that `Model.fit` uses.

    Standalone usage:

    >>> x = tf.ones((10, 1))
    >>> data = tf.keras.utils.pack_x_y_sample_weight(x)
    >>> isinstance(data, tf.Tensor)
    True
    >>> y = tf.ones((10, 1))
    >>> data = tf.keras.utils.pack_x_y_sample_weight(x, y)
    >>> isinstance(data, tuple)
    True
    >>> x, y = data

    Args:
      x: Features to pass to `Model`.
      y: Ground-truth targets to pass to `Model`.
      sample_weight: Sample weight for each element.

    Returns:
      Tuple in the format used in `Model.fit`.
    """
def single_batch_iterator(strategy, x, y: Incomplete | None = None, sample_weight: Incomplete | None = None, class_weight: Incomplete | None = None):
    """Creates a single-batch dataset."""
