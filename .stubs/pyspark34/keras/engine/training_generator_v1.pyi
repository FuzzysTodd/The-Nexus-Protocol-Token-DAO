from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import training_utils as training_utils, training_utils_v1 as training_utils_v1
from keras.utils import data_utils as data_utils, generic_utils as generic_utils
from keras.utils.mode_keys import ModeKeys as ModeKeys

def model_iteration(model, data, steps_per_epoch: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_data: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, class_weight: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False, shuffle: bool = False, initial_epoch: int = 0, mode=..., batch_size: Incomplete | None = None, steps_name: str = 'steps', **kwargs):
    """Loop function for arrays of data with modes TRAIN/TEST/PREDICT.

    Args:
        model: Keras Model instance.
        data: Either a tuple of NumPy/Tensor inputs (i.e. `(x,)` or `(x, y)` or
          `(x, y, sample_weights)`) or a generator or
          `keras.utils.data_utils.Sequence` object or Eager Iterator or Dataset.
        steps_per_epoch: Total number of steps (batches of samples) before
          declaring one epoch finished and starting the next epoch. Ignored with
          the default value of `None`.
        epochs: Number of times to iterate over the data.
        verbose: 0, 1, or 2. Verbosity mode.
          0 = silent, 1 = progress bar, 2 = one line per epoch.
          Note that the progress bar is not particularly useful when
          logged to a file, so verbose=2 is recommended when not running
          interactively (eg, in a production environment).
        callbacks: List of callbacks to be called during training.
        validation_data: Either a tuple of NumPy/Tensor inputs (i.e. `(x,)` or
          `(x, y)` or `(x, y, sample_weights)`) or a generator or
          `keras.utils.data_utils.Sequence` object or Eager Iterator or Dataset.
        validation_steps: Total number of steps (batches of samples) before
          declaring validation finished.
        validation_freq: Only relevant if validation data is provided. Integer
          or `collections.abc.Container` instance (e.g. list, tuple, etc.). If
          an integer, specifies how many training epochs to run before a new
          validation run is performed, e.g. `validation_freq=2` runs validation
          every 2 epochs. If a Container, specifies the epochs on which to run
          validation, e.g. `validation_freq=[1, 2, 10]` runs validation at the
          end of the 1st, 2nd, and 10th epochs.
        class_weight: Dictionary mapping class indices to a weight for the
            class.
        max_queue_size: Integer. Maximum size for the generator queue. If
          unspecified, `max_queue_size` will default to 10.
        workers: Integer. Maximum number of processes to spin up when using
          process-based threading. If unspecified, `workers` will default to 1.
          If 0, will execute the generator on the main thread.
        use_multiprocessing: Boolean. If `True`, use process-based threading. If
          unspecified, `use_multiprocessing` will default to `False`. Note that
          because this implementation relies on multiprocessing, you should not
          pass non-picklable arguments to the generator as they can't be passed
          easily to children processes.
        shuffle: Boolean. Whether to shuffle the order of the batches at the
          beginning of each epoch. Only used with instances of `Sequence`
          (`keras.utils.Sequence`). Has no effect when `steps_per_epoch` is not
          `None`.
        initial_epoch: Epoch at which to start training (useful for resuming a
          previous training run).
        mode: One of ModeKeys.TRAIN/ModeKeys.TEST/ModeKeys.PREDICT.
        batch_size: Integer batch size or None if unknown. Will only be used if
          `data` is in NumPy/Tensor format.
        steps_name: The string name of the steps argument, either `steps`,
          `validation_steps`, or `steps_per_epoch`. Only used for error message
          formatting.
        **kwargs: Additional arguments for backwards compatibility. `steps` is
          accepted as an alias for `steps_per_epoch`.

    Returns:
        - In TRAIN mode: `History` object.
        - In TEST mode: Evaluation metrics.
        - In PREDICT mode: Outputs of the Model called on inputs.

    Raises:
        ValueError: in case of invalid arguments.
    """

fit_generator: Incomplete
evaluate_generator: Incomplete
predict_generator: Incomplete

def convert_to_generator_like(data, batch_size: Incomplete | None = None, steps_per_epoch: Incomplete | None = None, epochs: int = 1, shuffle: bool = False):
    """Make a generator out of NumPy or EagerTensor inputs.

    Args:
      data: Either a generator or `keras.utils.data_utils.Sequence` object or
        `Dataset`, `Iterator`, or a {1,2,3}-tuple of NumPy arrays or
        EagerTensors.  If a tuple, the elements represent `(x, y,
        sample_weights)` and may be `None` or `[None]`.
      batch_size: Used when creating a generator out of tuples of NumPy arrays
        or EagerTensors.
      steps_per_epoch: Steps of the generator to run each epoch. If `None` the
        number of steps will be read from the data (for
        `keras.utils.data_utils.Sequence` types).
      epochs: Total number of epochs to run.
      shuffle: Whether the data should be shuffled.

    Returns:
      - Generator, `keras.utils.data_utils.Sequence`, or `Iterator`.

    Raises:
      - ValueError: If `batch_size` is not provided for NumPy or EagerTensor
        inputs.
    """

class GeneratorOrSequenceTrainingLoop(training_utils_v1.TrainingLoop):
    """Generator-like.

    Input is Python generator, or Sequence object.

    The difference between this class and `GeneratorLikeTrainingFunction` is
    that this class only handles inputs that with x, y and sample_weight fused
    into one param.
    """
    def fit(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_split: float = 0.0, validation_data: Incomplete | None = None, shuffle: bool = True, class_weight: Incomplete | None = None, sample_weight: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False): ...
    def evaluate(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, sample_weight: Incomplete | None = None, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False): ...
    def predict(self, model, x, batch_size: Incomplete | None = None, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None, max_queue_size: int = 10, workers: int = 1, use_multiprocessing: bool = False): ...

class EagerDatasetOrIteratorTrainingLoop(training_utils_v1.TrainingLoop):
    """A non-distributed Dataset or iterator in eager execution."""
    def fit(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_split: float = 0.0, validation_data: Incomplete | None = None, shuffle: bool = True, class_weight: Incomplete | None = None, sample_weight: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, **kwargs): ...
    def evaluate(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, sample_weight: Incomplete | None = None, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs): ...
    def predict(self, model, x, batch_size: Incomplete | None = None, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs): ...

class GeneratorLikeTrainingLoop(training_utils_v1.TrainingLoop):
    """TrainingLoop that handle inputs like python generator.

    This is the default handler for most of the input data types, includes
    symbolic tensors or Numpy array-like, Datasets and iterators in graph mode
    (since they generate symbolic tensors). This Function is used to handle
    model with `run_eagerly` = True.
    """
    def fit(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_split: float = 0.0, validation_data: Incomplete | None = None, shuffle: bool = True, class_weight: Incomplete | None = None, sample_weight: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, **kwargs): ...
    def evaluate(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, sample_weight: Incomplete | None = None, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs): ...
    def predict(self, model, x, batch_size: Incomplete | None = None, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs): ...
