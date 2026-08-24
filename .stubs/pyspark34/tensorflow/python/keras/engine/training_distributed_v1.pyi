from _typeshed import Incomplete
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context, input_lib as input_lib
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, errors as errors, ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import training_arrays_v1 as training_arrays_v1, training_utils_v1 as training_utils_v1
from tensorflow.python.keras.utils.generic_utils import Progbar as Progbar
from tensorflow.python.keras.utils.mode_keys import ModeKeys as ModeKeys
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops

def experimental_tpu_fit_loop(model, dataset, epochs: int = 100, verbose: int = 1, callbacks: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, val_dataset: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1):
    """Fit loop for training with TPU tf.distribute.Strategy.

  Args:
      model: Keras Model instance.
      dataset: Dataset that returns inputs and targets
      epochs: Number of times to iterate over the data
      verbose: Integer, Verbosity mode, 0, 1 or 2
      callbacks: List of callbacks to be called during training
      initial_epoch: Epoch at which to start training
          (useful for resuming a previous training run)
      steps_per_epoch: Total number of steps (batches of samples)
          before declaring one epoch finished and starting the
          next epoch. Ignored with the default value of `None`.
      val_dataset: Dataset for validation data.
      validation_steps: Number of steps to run validation for
          (only if doing validation from data tensors).
          Ignored with the default value of `None`.
      validation_freq: Only relevant if validation data is provided. Integer or
          `collections.abc.Container` instance (e.g. list, tuple, etc.). If an
          integer, specifies how many training epochs to run before a new
          validation run is performed, e.g. `validation_freq=2` runs
          validation every 2 epochs. If a Container, specifies the epochs on
          which to run validation, e.g. `validation_freq=[1, 2, 10]` runs
          validation at the end of the 1st, 2nd, and 10th epochs.

  Returns:
      Returns `None`.

  Raises:
      ValueError: in case of invalid arguments.
  """
def experimental_tpu_test_loop(model, dataset, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None):
    """Test loop for evaluating with TPU tf.distribute.Strategy.

  Args:
      model: Keras Model instance.
      dataset: Dataset for input data.
      verbose: Integer, Verbosity mode 0 or 1.
      steps: Total number of steps (batches of samples)
          before declaring predictions finished.
          Ignored with the default value of `None`.
      callbacks: List of callbacks to be called during training

  Returns:
      Scalar loss (if the model has a single output and no metrics)
      or list of scalars (if the model has multiple outputs
      and/or metrics). The attribute `model.metrics_names` will give you
      the display labels for the outputs.
  """
def experimental_tpu_predict_loop(model, dataset, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None):
    """Predict loop for predicting with TPU tf.distribute.Strategy.

  Args:
      model: Keras Model instance.
      dataset: Dataset for input data.
      verbose: Integer, Verbosity mode 0 or 1.
      steps: Total number of steps (batches of samples)
          before declaring `_predict_loop` finished.
          Ignored with the default value of `None`.
      callbacks: List of callbacks to be called during training

  Returns:
      Array of predictions (if the model has a single output)
      or list of arrays of predictions
      (if the model has multiple outputs).
  """

class DistributionSingleWorkerTrainingLoop(training_utils_v1.TrainingLoop):
    """Training loop for distribution strategy with single worker."""
    def fit(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, epochs: int = 1, verbose: int = 1, callbacks: Incomplete | None = None, validation_split: float = 0.0, validation_data: Incomplete | None = None, shuffle: bool = True, class_weight: Incomplete | None = None, sample_weight: Incomplete | None = None, initial_epoch: int = 0, steps_per_epoch: Incomplete | None = None, validation_steps: Incomplete | None = None, validation_freq: int = 1, **kwargs):
        """Fit loop for Distribution Strategies."""
    def evaluate(self, model, x: Incomplete | None = None, y: Incomplete | None = None, batch_size: Incomplete | None = None, verbose: int = 1, sample_weight: Incomplete | None = None, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs):
        """Evaluate loop for Distribution Strategies."""
    def predict(self, model, x, batch_size: Incomplete | None = None, verbose: int = 0, steps: Incomplete | None = None, callbacks: Incomplete | None = None, **kwargs):
        """Predict loop for Distribution Strategies."""

class DistributionMultiWorkerTrainingLoop(training_utils_v1.TrainingLoop):
    """Training loop for distribution strategy with multiple worker."""
    def __init__(self, single_worker_loop) -> None: ...
    def fit(self, *args, **kwargs): ...
    def evaluate(self, *args, **kwargs): ...
    def predict(self, *args, **kwargs): ...
