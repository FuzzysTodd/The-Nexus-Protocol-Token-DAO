from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.distribute import reduce_util as reduce_util
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.keras import backend as backend, callbacks as callbacks, optimizers as optimizers
from tensorflow.python.keras.engine import training_utils_v1 as training_utils_v1
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.keras.utils import tf_contextlib as tf_contextlib
from tensorflow.python.keras.utils.mode_keys import ModeKeys as ModeKeys
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, sparse_ops as sparse_ops, variables as variables
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import nest as nest

def set_weights(distribution_strategy, dist_model, weights) -> None:
    """Sets the weights of the replicated models.

  The weights of the replicated models are set to the weights of the original
  model. The weights of the replicated model are Mirrored variables and hence
  we need to use the `update` call within a DistributionStrategy scope.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training
        and validation.
    dist_model: The replicated models on the different devices.
    weights: The weights of the original model.
  """
def unwrap_values(distribution_strategy, grouped_inputs, grouped_outputs, grouped_updates: Incomplete | None = None, grouped_session_args: Incomplete | None = None, with_loss_tensor: bool = False):
    """Unwrap the list of values contained in the PerReplica parameters.

  This function calls `flatten_per_replica_values` to parse each of the input
  parameters into a list of values on the different devices. If we set
  `with_loss_tensor` to be True, we also call `reduce` on the list of losses on
  the different devices to give us one loss tensor.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training and
        validation.
    grouped_inputs: PerReplica inputs returned from the train or test function
        that we ran on each device.
    grouped_outputs: PerReplica outputs returned from the train or test function
        that we ran on each device.
    grouped_updates: PerReplica updates returned from the train or test function
        that we ran on each device.
    grouped_session_args: PerReplica session args returned from the train or
        test function that we ran on each device.
    with_loss_tensor: Boolean that indicates if we need to add the reduced loss
        tensor as one of the outputs.

  Returns:
    Values of each of the PerReplica parameters.

  """
def unwrap_output_dict(strategy, grouped_outputs, mode):
    """Unwrap the list of outputs contained in the PerReplica parameters."""
def unwrap_outputs(distribution_strategy, grouped_outputs, with_loss_tensor: bool = False):
    """Unwrap the list of outputs contained in the PerReplica parameters.

  This function calls `flatten_per_replica_values` to parse each of the input
  parameters into a list of outputs on the different devices. If we set
  `with_loss_tensor` to be True, we also call `reduce` on the list of losses on
  the different devices to give us one loss tensor.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training and
        validation.
    grouped_outputs: PerReplica outputs returned from the train or test function
        that we ran on each device.
    with_loss_tensor: Boolean that indicates if we need to add the reduced loss
        tensor as one of the outputs.

  Returns:
    Values of each of the PerReplica outputs.

  """
def flatten_per_replica_values(distribution_strategy, per_replica_values):
    """Unwraps and flattens a nest of PerReplica parameters.

  PerReplica values have one value associated with each device. Each entry in
  the PerReplica dict has a device `key` and the corresponding value on the
  device as the `value`. In this function we take a PerReplica value or a list
  of PerReplica values and return all the values in the PerReplica dict.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training and
      validation.
    per_replica_values: List of PerReplica object or a single PerReplica object.

  Returns:
    List of values of all the PerReplica objects.

  """
def validate_callbacks(input_callbacks, optimizer) -> None:
    """Validate whether given callbacks are supported by DistributionStrategy.

  Args:
    input_callbacks: List of callbacks passed by the user to fit.
    optimizer: Optimizer instance used to train the model.

  Raises:
    ValueError: If `LearningRateScheduler` or `ReduceLROnPlateau` is one of the
        callbacks passed.
    ValueError: If `write_grads` is one of the parameters passed as part of the
        TensorBoard callback.
  """
def validate_distributed_dataset_inputs(distribution_strategy, x, y, sample_weights: Incomplete | None = None):
    """Validate all the components of a DistributedValue Dataset input.

  Args:
    distribution_strategy: The current DistributionStrategy used to call
        `fit`/`evaluate`.
    x: Input Dataset DistributedValue object. For example, when we use
        `MirroredStrategy` this is a PerReplica object with a tensor for each
        device set in the dict. x can also be a tuple or dict. The keys of the
        dict should match the names of the input layers of the model.
    y: Target Dataset DistributedValue object. For example, when we use
        `MirroredStrategy` this is a PerReplica object with a tensor for each
        device set in the dict. y can also be a tuple or dict. The keys of the
        dict should match the names of the output layers of the model.
    sample_weights: Sample weights Dataset DistributedValue object. For example,
        when we use `MirroredStrategy` this is a PerReplica object with a tensor
        for each device set in the dict.

  Returns:
    The unwrapped values list of the x and y DistributedValues inputs.

  Raises:
    ValueError: If x and y do not have support for being evaluated as tensors.
        or if x and y contain elements that are not tensors or if x and y
        contain elements that have a shape or dtype mismatch.
  """
def validate_per_replica_inputs(distribution_strategy, x):
    """Validates PerReplica dataset input list.

  Args:
    distribution_strategy: The current DistributionStrategy used to call
      `fit`, `evaluate` and `predict`.
    x: A list of PerReplica objects that represent the input or
      target values.

  Returns:
    List containing the first element of each of the PerReplica objects in
    the input list.

  Raises:
    ValueError: If any of the objects in the `per_replica_list` is not a tensor.

  """
def validate_all_tensor_types(x, x_values) -> None: ...
def validate_all_tensor_shapes(x, x_values) -> None: ...
def init_restore_or_wait_for_variables() -> None:
    """Initialize or restore variables or wait for variables to be initialized."""
def validate_inputs(x, y) -> None:
    """Validate inputs when using DistributionStrategy.

  Args:
    x: Model Inputs.
    y: Model Targets.

  Raises:
    ValueError: if input is not a Dataset or a numpy array(when we use
      MirroredStrategy).
  """
def is_dataset_shape_fully_defined(dataset):
    """Returns whether a dataset contains a final partial batch."""
def process_batch_and_step_size(strategy, inputs, batch_size, steps_per_epoch, mode, validation_split: float = 0.0):
    """Process the batch size and step size based on input and dist strategy."""
def get_input_params(distribution_strategy, num_samples, steps, batch_size, mode: Incomplete | None = None):
    """Calculate the number of batches and steps/steps_per_epoch.

  Args:
    distribution_strategy: The DistributionStrategy used to compile the model.
    num_samples: The number of samples from which we determine the batch size
      and steps.
    steps:  The specified number of steps.
    batch_size: The specified batch_size.
    mode: ModeKey representing whether input will be used for training,
      evaluation, or prediction. This is used to relax the constraints on
      consuming all the training samples to keep compatibility till we support
      partial batches. If none, then partial batches are not allowed.

  Returns:
    steps: The steps or steps_per_epoch argument depending on if a user is
        calling `fit`, `evaluate` or `predict`. If the is_training flag is set
        we don't require the number of samples to be used completely.
    batch_size: The batch size to be used in model iterations.

  Raises:
    ValueError: If the number of batches or steps evaluates to 0.

  """
def get_batch_dimension(iterator): ...
def get_iterator(dataset, distribution_strategy): ...
def initialize_iterator(iterator, distribution_strategy) -> None: ...
def is_distributing_by_cloning(model):
    """Decide whether this model is going to be distributed via cloning.

  We are going to distribute the model by cloning in graph mode.

  Args:
    model: Keras model to distribute.

  Returns:
    True if the `model` is going to be distributed using cloning and False
    otherwise.
  """
def clone_model_on_replicas(model, strategy, mode, inputs: Incomplete | None = None, targets: Incomplete | None = None) -> None:
    """Create a cloned model on each replica."""
def get_distributed_model(model, mode): ...
def set_distributed_model(model, mode, distributed_model) -> None: ...
def get_distributed_function(model, mode): ...
def set_distributed_function(model, mode, distributed_function) -> None: ...
def distributed_scope(strategy, learning_phase) -> Generator[None, None, None]: ...
def is_current_worker_chief(): ...
def filter_distributed_callbacks(callbacks_list, model):
    """Filter Callbacks based on the worker context when running multi-worker.

  Args:
    callbacks_list: A list of `Callback` instances.
    model: Keras model instance.

  Returns:
    The list of `Callback` instances that should be run on this worker.
  """
def concat_along_batch_dimension(outputs):
    """Concats prediction outputs along the batch dimension."""
