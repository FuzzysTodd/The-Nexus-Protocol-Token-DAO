import abc
from _typeshed import Incomplete
from collections.abc import Generator
from keras import backend as backend, losses as losses
from keras.utils import data_utils as data_utils, generic_utils as generic_utils, losses_utils as losses_utils, tf_inspect as tf_inspect

def is_composite_or_composite_value(tensor):
    """Returns true if 'tensor' is a CompositeTensor or a CT Value object."""

class Aggregator(metaclass=abc.ABCMeta):
    """Abstract base class used to aggregate batch-level outputs of a loop.

    Attributes:
      use_steps: Whether the loop is using `step` or `batch_size`.
      num_samples: Total number of samples: `batch_size * num_batches`.
      steps: Total number of steps.
      batch_size: Batch size. It is used for validation checks between inputs
        and outputs.
      results: What to return at the end of the aggregation loop.
    """
    use_steps: Incomplete
    num_samples: Incomplete
    steps: Incomplete
    batch_size: Incomplete
    results: Incomplete
    def __init__(self, use_steps, num_samples: Incomplete | None = None, steps: Incomplete | None = None, batch_size: Incomplete | None = None) -> None: ...
    @abc.abstractmethod
    def create(self, batch_outs):
        """Creates the initial results from the first batch outputs.

        Args:
          batch_outs: A list of batch-level outputs.
        """
    @abc.abstractmethod
    def aggregate(self, batch_outs, batch_start: Incomplete | None = None, batch_end: Incomplete | None = None):
        """Aggregates batch-level results into total results.

        Args:
          batch_outs: A list of batch-level outputs.
          batch_start: The start index of this batch. Always `None` if
            `use_steps` is `True`.
          batch_end: The end index of this batch. Always `None` if `use_steps`
            is `True`.
        """
    @abc.abstractmethod
    def finalize(self):
        """Prepares the total results to be returned."""

class MetricsAggregator(Aggregator):
    """Aggregator that calculates loss and metrics info.

    Attributes:
      use_steps: Whether the loop is using `step` or `batch_size`.
      num_samples: Total number of samples: `batch_size*num_batches`.
      steps: Total number of steps, ie number of times to iterate over a dataset
        to cover all samples.
    """
    def __init__(self, use_steps, num_samples: Incomplete | None = None, steps: Incomplete | None = None) -> None: ...
    results: Incomplete
    def create(self, batch_outs) -> None: ...
    def aggregate(self, batch_outs, batch_start: Incomplete | None = None, batch_end: Incomplete | None = None) -> None: ...
    def finalize(self) -> None: ...

class ConcatAggregator(Aggregator):
    """Combine tensor-likes which cannot be merged on the fly.

    This class expects to aggregate a single tensor-like rather than a nested
    structure of tensor-likes.
    """
    composite: Incomplete
    def __init__(self, batch_size) -> None: ...
    def create(self, batch_element) -> None: ...
    def aggregate(self, batch_element, batch_start: Incomplete | None = None, batch_end: Incomplete | None = None) -> None: ...
    results: Incomplete
    def finalize(self) -> None: ...

def get_copy_pool():
    """Shared threadpool for copying arrays.

    Pool instantiation takes ~ 2ms, so a singleton pool is used rather than
    creating a pool per SliceAggregator.

    Returns:
      The global copy threadpool.
    """

class SliceAggregator(Aggregator):
    """Combine arrays where the final size is known.

    This class expects to aggregate a single tensor-like rather than a nested
    structure of tensor-likes.

    NumPy copies are an operation that threads handle quite well because all of
    the heavy lifting is in c and does not need the GIL. Moreover, we can
    perform lock-free writes to the same buffer in multiple threads because the
    nature of result aggregation guarantees that either the indices are disjoint
    or the aggregator will throw an exception in finalize. Moreover, because
    aggregation is performed on the slowest varying dimension, assignments for a
    given batch will write to contiguous blocks of memory, further minimizing
    contention.

    There is, however, some scheduling and context switching overhead which will
    offset the gains from pipelining the slice assignment. Below a given
    threshold it is faster to simply assign in the main thread rather than
    enqueue the assignment in a side thread. The exact threshold will vary from
    system to system, but the time is not very sensitive to the exact transition
    so a value of 2 ** 14 was chosen which should be reasonable on most systems.
    """
    def __init__(self, num_samples, batch_size) -> None: ...
    results: Incomplete
    def create(self, batch_element) -> None: ...
    def aggregate(self, batch_element, batch_start, batch_end) -> None: ...
    def finalize(self) -> None: ...

class OutputsAggregator(Aggregator):
    """Aggregator that concatenates outputs."""
    def create(self, batch_outs): ...
    def aggregate(self, batch_outs, batch_start: Incomplete | None = None, batch_end: Incomplete | None = None) -> None: ...
    results: Incomplete
    def finalize(self) -> None: ...

def get_progbar(model, count_mode, include_metrics: bool = True):
    """Get Progbar."""
def check_num_samples(ins, batch_size: Incomplete | None = None, steps: Incomplete | None = None, steps_name: str = 'steps'):
    """Determine the number of samples provided for training and evaluation.

    The number of samples is not defined when running with `steps`,
    in which case the number of samples is set to `None`.

    Args:
        ins: List of tensors to be fed to the Keras function.
        batch_size: Integer batch size or `None` if not defined.
        steps: Total number of steps (batches of samples) before declaring
          `_predict_loop` finished. Ignored with the default value of `None`.
        steps_name: The public API's parameter name for `steps`.

    Raises:
        ValueError: when `steps` is `None` and the attribute `ins.shape`
        does not exist. Also raises ValueError when `steps` is not `None`
        and `batch_size` is not `None` because they are mutually
        exclusive.

    Returns:
        When steps is `None`, returns the number of samples to be
        processed based on the size of the first dimension of the
        first input numpy array. When steps is not `None` and
        `batch_size` is `None`, returns `None`.
    """
def standardize_single_array(x, expected_shape: Incomplete | None = None):
    """Expand data of shape (x,) to (x, 1), unless len(expected_shape)==1."""
def get_composite_shape(tensor):
    """Returns the shape of the passed composite tensor."""
def standardize_input_data(data, names, shapes: Incomplete | None = None, check_batch_axis: bool = True, exception_prefix: str = ''):
    """Normalizes inputs and targets provided by users.

    Users may pass data as a list of arrays, dictionary of arrays,
    or as a single array. We normalize this to an ordered list of
    arrays (same order as `names`), while checking that the provided
    arrays have shapes that match the network's expectations.

    Args:
        data: User-provided input data (polymorphic).
        names: List of expected array names.
        shapes: Optional list of expected array shapes.
        check_batch_axis: Boolean; whether to check that the batch axis of the
          arrays matches the expected value found in `shapes`.
        exception_prefix: String prefix used for exception formatting.

    Returns:
        List of standardized input arrays (one array per model input).

    Raises:
        ValueError: in case of improperly formatted user-provided data.
    """
def standardize_sample_or_class_weights(x_weight, output_names, weight_type):
    """Maps `sample_weight` or `class_weight` to model outputs.

    Args:
        x_weight: User-provided `sample_weight` or `class_weight` argument.
        output_names: List of output names (strings) in the model.
        weight_type: A string used purely for exception printing.

    Returns:
        A list of `sample_weight` or `class_weight` where there are exactly
            one element per model output.

    Raises:
        ValueError: In case of invalid user-provided argument.
    """
def standardize_class_weights(class_weight, output_names): ...
def standardize_sample_weights(sample_weight, output_names): ...
def check_array_lengths(inputs, targets, weights: Incomplete | None = None):
    """Does user input validation for numpy arrays.

    Args:
        inputs: list of Numpy arrays of inputs.
        targets: list of Numpy arrays of targets.
        weights: list of Numpy arrays of sample weights.

    Raises:
        ValueError: in case of incorrectly formatted data.
    """
def check_loss_and_target_compatibility(targets, loss_fns, output_shapes) -> None:
    """Does validation on the compatibility of targets and loss functions.

    This helps prevent users from using loss functions incorrectly. This check
    is purely for UX purposes.

    Args:
        targets: list of Numpy arrays of targets.
        loss_fns: list of loss functions.
        output_shapes: list of shapes of model outputs.

    Raises:
        ValueError: if a loss function or target array
            is incompatible with an output.
    """
def collect_per_output_metric_info(metrics, output_names, output_shapes, loss_fns, from_serialized: bool = False, is_weighted: bool = False):
    '''Maps metric names and functions to model outputs.

    Args:
        metrics: a list or a list of lists or a dict of metric functions.
        output_names: a list of the names (strings) of model outputs.
        output_shapes: a list of the shapes (strings) of model outputs.
        loss_fns: a list of the loss functions corresponding to the model
          outputs.
        from_serialized: whether the model the metrics are being sourced from is
          being initialized from a serialized format.
        is_weighted: Boolean indicating whether the given metrics are weighted.

    Returns:
        A list (one entry per model output) of dicts.
        For instance, if the model has 2 outputs, and for the first output
        we want to compute "binary_accuracy" and "binary_crossentropy",
        and just "binary_accuracy" for the second output,
        the list would look like: `[{
            \'acc\': binary_accuracy(),
            \'ce\': binary_crossentropy(),
          }, {
            \'acc\': binary_accuracy(),
          }]`

    Raises:
        TypeError: if an incorrect type is passed for the `metrics` argument.
    '''
def batch_shuffle(index_array, batch_size):
    """Shuffles an array in a batch-wise fashion.

    Useful for shuffling HDF5 arrays
    (where one cannot access arbitrary indices).

    Args:
        index_array: array of indices to be shuffled.
        batch_size: integer.

    Returns:
        The `index_array` array, shuffled in a batch-wise fashion.
    """
def standardize_weights(y, sample_weight: Incomplete | None = None, class_weight: Incomplete | None = None, sample_weight_mode: Incomplete | None = None):
    '''Performs sample weight validation and standardization.

    Everything gets normalized to a single sample-wise (or timestep-wise)
    weight array. If both `sample_weight` and `class_weight` are provided,
    the weights are multiplied.

    Args:
        y: Numpy array or Tensor of model targets to be weighted.
        sample_weight: User-provided `sample_weight` argument.
        class_weight: User-provided `class_weight` argument.
        sample_weight_mode: One of `None` or `"temporal"`. `"temporal"`
          indicated that we expect 2D weight data that will be applied to the
          last 2 dimensions of the targets (i.e. we are weighting timesteps, not
          samples).

    Returns:
        A numpy array of target weights, one entry per sample to weight.

    Raises:
        ValueError: In case of invalid user-provided arguments.
    '''
def has_symbolic_tensors(ls): ...
def has_tensors(ls):
    """Returns true if `ls` contains tensors."""
def get_metric_name(metric, weighted: bool = False):
    """Returns the name corresponding to the given metric input.

    Args:
      metric: Metric function name or reference.
      weighted: Boolean indicating if the given metric is weighted.

    Returns:
        The metric name.
    """
def get_metric_function(metric, output_shape: Incomplete | None = None, loss_fn: Incomplete | None = None):
    """Returns the metric function corresponding to the given metric input.

    Args:
        metric: Metric function name or reference.
        output_shape: The shape of the output that this metric will be
          calculated for.
        loss_fn: The loss function used.

    Returns:
        The metric function.
    """
def call_metric_function(metric_fn, y_true, y_pred: Incomplete | None = None, weights: Incomplete | None = None, mask: Incomplete | None = None):
    """Invokes metric function and returns the metric result tensor."""
def get_loss_function(loss):
    """Returns the loss corresponding to the loss input in `compile` API."""
def validate_dataset_input(x, y, sample_weight, validation_split: Incomplete | None = None) -> None:
    """Validates user input arguments when a dataset iterator is passed.

    Args:
      x: Input data. A `tf.data` dataset or iterator.
      y: Target data. It could be either Numpy array(s) or TensorFlow tensor(s).
        Expected to be `None` when `x` is a dataset iterator.
      sample_weight: An optional sample-weight array passed by the user to
        weight the importance of each sample in `x`. Expected to be `None` when
        `x` is a dataset iterator
      validation_split: Float between 0 and 1. Fraction of the training data to
        be used as validation data. Expected to be `None` when `x` is a dataset
        iterator.

    Raises:
      ValueError: if argument `y` or `sample_weight` or `validation_split` are
          provided by user.
    """
def validate_input_types(inp, orig_inp, allow_dict: bool = True, field_name: str = 'inputs') -> None:
    """Helper function to validate either inputs or targets."""
def check_generator_arguments(y: Incomplete | None = None, sample_weight: Incomplete | None = None, validation_split: Incomplete | None = None) -> None:
    """Validates arguments passed when using a generator."""
def check_steps_argument(input_data, steps, steps_name):
    """Validates `steps` argument based on input data's type.

    The cases when `steps` value must be provided are when
      1. input data passed is an iterator.
      2. model was built on top of symbolic tensors, input data is not
         required and is `None`.
      3. input data passed is a symbolic tensor.

    Args:
        input_data: Input data. Can be Numpy array(s) or TensorFlow tensor(s) or
          tf.data.Dataset iterator or `None`.
        steps: Integer or `None`. Total number of steps (batches of samples) to
          execute.
        steps_name: The public API's parameter name for `steps`.

    Returns:
      boolean, True if `steps` argument is required, else False.

    Raises:
        ValueError: if `steps` argument is required for given input data type
          but not provided.
    """
def cast_single_tensor(x, dtype: Incomplete | None = None): ...
def cast_if_floating_dtype_and_mismatch(targets, outputs):
    """Returns target data tensors using correct datatype.

    Checks that each target and output pair are the same datatype. If not, casts
    the target to the output's datatype.

    Args:
      targets: tensor or list of targets.
      outputs: tensor or list of outputs.

    Returns:
      Targets in appropriate datatype.
    """
def cast_if_floating_dtype(x, dtype: Incomplete | None = None):
    """Casts the given data tensors to the default floating point type.

    Casts only if the input is already a floating point type.
    Args:
      x: tensor or list/tuple of tensors.
      dtype: The dtype to which Tensors should be cast.

    Returns:
      Converted input.
    """
def cast_to_model_input_dtypes(x, model):
    """Casts the given data tensors to the dtypes of the model inputs.

    Args:
      x: tensor or list/tuple of tensors.
      model: The model.

    Returns:
      Converted input. Each tensor is casted to the corresponding input in
      `model.inputs`.
    """
def prepare_sample_weight_modes(training_endpoints, sample_weight_mode) -> None:
    """Prepares sample weight modes for the model.

    Args:
      training_endpoints: List of model _TrainingEndpoints.
      sample_weight_mode: sample weight mode user input passed from compile API.

    Raises:
      ValueError: In case of invalid `sample_weight_mode` input.
    """
def prepare_loss_functions(loss, output_names):
    """Converts loss to a list of loss functions.

    Args:
        loss: String (name of objective function), objective function or
          `tf.keras.losses.Loss` instance. See `tf.keras.losses`.
          If the model has multiple
          outputs, you can use a different loss on each output by passing a
          dictionary or a list of losses. The loss value that will be minimized
          by the model will then be the sum of all individual losses.
        output_names: List of model output names.

    Returns:
        A list of loss objective functions.

    Raises:
        ValueError: If loss is a dict with keys not in model output names,
            or if loss is a list with len not equal to model outputs.
    """
def prepare_loss_weights(training_endpoints, loss_weights: Incomplete | None = None) -> None:
    """Converts loss weights to a list of loss weights.

    The result loss weights will be populated on the training endpoint.

    Args:
        training_endpoints: List of model training endpoints.
        loss_weights: Optional list or dictionary specifying scalar coefficients
          (Python floats) to weight the loss contributions of different model
          outputs. The loss value that will be minimized by the model will then
          be the *weighted sum* of all individual losses, weighted by the
          `loss_weights` coefficients. If a list, it is expected to have a 1:1
          mapping to the model's outputs. If a dict, it is expected to map
          output names (strings) to scalar coefficients.

    Raises:
        ValueError: If loss weight is a dict with key not in model output names,
            or if loss is a list with len not equal to model outputs.
    """
def is_feature_layer(layer):
    """Returns whether `layer` is a FeatureLayer or not."""
def is_eager_dataset_or_iterator(data): ...
def get_dataset_graph_def(dataset): ...
def verify_dataset_shuffled(x):
    """Verifies that the dataset is shuffled.

    Args:
      x: Dataset passed as an input to the model.

    Returns:
      boolean, whether the input dataset is shuffled or not.
    """
def is_dataset_or_iterator(data): ...
def get_iterator(dataset):
    """Create and initialize an iterator from a dataset."""
def initialize_iterator(iterator) -> None: ...
def extract_tensors_from_dataset(dataset):
    """Extract tuple of tensors `inputs, targets, sample_weight` from a dataset.

    Args:
      dataset: Dataset instance.

    Returns:
      Tuple of tensors `x, y, weights`. `y` and `weights` entry may be None.
    """
def unpack_iterator_input(iterator):
    """Convert a dataset iterator to a tuple of tensors `x, y, sample_weights`.

    Args:
      iterator: Instance of a dataset iterator.

    Returns:
      Tuple of tensors `x, y, weights`. `y` and `weights` entry may be None.
    """
def infer_steps_for_dataset(model, dataset, steps, epochs: int = 1, steps_name: str = 'steps'):
    """Infers steps_per_epoch needed to loop through a dataset.

    Args:
        model: Keras model instance.
        dataset: Input data of type tf.data.Dataset.
        steps: Number of steps to draw from the dataset (may be None if
          unknown).
        epochs: Number of times to iterate over the dataset.
        steps_name: The string name of the steps argument, either `steps`,
          `validation_steps`, or `steps_per_epoch`. Only used for error message
          formatting.

    Returns:
      Integer or `None`. Inferred number of steps to loop through the dataset.
      `None` is returned if 1) the size of the dataset is unknown and `steps`
      was not specified, or 2) this is multi-worker training and auto sharding
      is enabled.

    Raises:
      ValueError: In case of invalid argument values.
    """

class ModelInputs:
    """Encapsulates model inputs.

    Allows for transforming model inputs while keeping the same structure.
    """
    def __init__(self, inputs) -> None: ...
    def get_input_names(self):
        """Returns keys to name inputs by.

        In case inputs provided were a list, tuple or single entry, we make up a
        key 'input_%d'. For dictionary case, we return a sorted list of keys.
        """
    def get_symbolic_inputs(self, return_single_as_list: bool = False):
        """Returns inputs to be set as self.inputs for a model."""
    def as_dict(self) -> Generator[Incomplete, None, None]:
        """An iterable over a dictionary version of inputs."""
    def as_list(self):
        """Returning the inputs as a list."""

def generic_output_names(outputs_list): ...
def should_run_validation(validation_freq, epoch):
    """Checks if validation should be run this epoch.

    Args:
      validation_freq: Integer or list. If an integer, specifies how many
        training epochs to run before a new validation run is performed. If a
        list, specifies the epochs on which to run validation.
      epoch: Integer, the number of the training epoch just completed.

    Returns:
      Bool, True if validation should be run.

    Raises:
      ValueError: if `validation_freq` is an Integer and less than 1, or if
      it is neither an Integer nor a Sequence.
    """
def split_training_and_validation_data(x, y, sample_weights, validation_split):
    """Split input data into train/eval section based on validation_split."""
def unpack_validation_data(validation_data, raise_if_ambiguous: bool = True):
    """Unpack validation data based input type.

    The validation data is not touched if its dataset or dataset iterator.
    For other type of input (Numpy or tensor), it will be unpacked into tuple of
    3 which is x, y and sample weights.

    Args:
      validation_data: dataset, dataset iterator, or numpy, tensor tuple.
      raise_if_ambiguous: boolean on whether to fail if validation_data cannot
        be parsed. Otherwise simply return validation_data, None, None and defer
        the decision to the caller.

    Returns:
      tuple of 3, (x, y, sample_weights) for numpy and tensor input.
    """

class TrainingLoop:
    """TrainingLoop is a wrapper class around the training logic.

    This class is trying to encapsulate the different logic of fit/eval/predict
    with regard to different data input and model condition.

    Note that TrainingLoop is stateless, which means it doesn't contain any
    internal field and can be reused with different model and inputs.
    """
    def fit(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_split: float = 0.0, validation_data: Incomplete | None = None, shuffle: bool = True, class_weight: Incomplete | None = None, sample_weight: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, **kwargs) -> None:
        """Train the model with the inputs and targets."""
    def evaluate(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, sample_weight: Incomplete | None = None, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs) -> None:
        """Returns the loss value & metrics values for the model in test
        mode."""
    def predict(self, model, x, batch_size: Incomplete | None = None, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs) -> None: ...
