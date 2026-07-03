from _typeshed import Incomplete
from keras.saving import saving_lib as saving_lib
from keras.utils import generic_utils as generic_utils, losses_utils as losses_utils, tf_utils as tf_utils

class Container:
    """Base Container class."""
    def __init__(self, output_names: Incomplete | None = None) -> None: ...
    def build(self, y_pred) -> None: ...

class LossesContainer(Container):
    """A container class for losses passed to `Model.compile()`.

    Args:
      losses: Struct of loss function(s). See `Model.compile()` doc for more
        information.
      loss_weights: Weights of the losses contributions of different model
        outputs. See `Model.compile()` doc for more information.
      output_names: List of string. Per-output metric names.
      total_loss_mean: A `keras.metrics.Mean` instance that is used to track the
        mean of all losses (including compiled and regularization losses).
    """
    def __init__(self, losses, loss_weights: Incomplete | None = None, output_names: Incomplete | None = None, total_loss_mean: Incomplete | None = None) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config):
        """Returns the `LossesContainer` instance given the `config`."""
    @property
    def metrics(self):
        """Per-output loss metrics."""
    def build(self, y_pred) -> None:
        """One-time setup of loss objects."""
    @property
    def built(self): ...
    def __call__(self, y_true, y_pred, sample_weight: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Computes the overall loss.

        Args:
          y_true: An arbitrary structure of Tensors representing the ground
            truth.
          y_pred: An arbitrary structure of Tensors representing a Model's
            outputs.
          sample_weight: An arbitrary structure of Tensors representing the
            per-sample loss weights. If one Tensor is passed, it is used for all
            losses. If multiple Tensors are passed, the structure should match
            `y_pred`.
          regularization_losses: Additional losses to be added to the total
            loss.

        Returns:
          The total loss as a `tf.Tensor`, or `None` if no loss results.
        """
    def reset_state(self) -> None:
        """Resets the state of loss metrics."""

class MetricsContainer(Container):
    """A container class for metrics passed to `Model.compile`."""
    def __init__(self, metrics: Incomplete | None = None, weighted_metrics: Incomplete | None = None, output_names: Incomplete | None = None, from_serialized: bool = False) -> None:
        """Initializes a container for metrics.

        Arguments:
          metrics: see the `metrics` argument from `tf.keras.Model.compile`.
          weighted_metrics: see the `weighted_metrics` argument from
            `tf.keras.Model.compile`.
          output_names: A list of strings of names of outputs for the model.
          from_serialized: Whether the model being compiled is from a serialized
            model.  Used to avoid redundantly applying pre-processing renaming
            steps.
        """
    @property
    def metrics(self):
        """All metrics in this container."""
    @property
    def unweighted_metrics(self):
        """Metrics in the container that should not be passed sample_weight."""
    @property
    def weighted_metrics(self):
        """Metrics in this container that should be passed `sample_weight`."""
    def build(self, y_pred, y_true) -> None:
        """One-time setup of metric objects."""
    @property
    def built(self): ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None) -> None:
        """Updates the state of per-output metrics."""
    def reset_state(self) -> None:
        """Resets the state of all `Metric`s in this container."""

def create_pseudo_output_names(outputs):
    """Create pseudo output names for a subclassed Model."""
def create_pseudo_input_names(inputs):
    """Create pseudo input names for a subclassed Model."""
def map_to_output_names(y_pred, output_names, struct):
    """Maps a dict to a list using `output_names` as keys.

    This is a convenience feature only. When a `Model`'s outputs
    are a list, you can specify per-output losses and metrics as
    a dict, where the keys are the output names. If you specify
    per-output losses and metrics via the same structure as the
    `Model`'s outputs (recommended), no mapping is performed.

    For the Functional API, the output names are the names of the
    last layer of each output. For the Subclass API, the output names
    are determined by `create_pseudo_output_names` (For example:
    `['output_1', 'output_2']` for a list of outputs).

    This mapping preserves backwards compatibility for `compile` and
    `fit`.

    Args:
      y_pred: Sample outputs of the Model, to determine if this convenience
        feature should be applied (`struct` is returned unmodified if `y_pred`
        isn't a flat list).
      output_names: List. The names of the outputs of the Model.
      struct: The structure to map.

    Returns:
      `struct` mapped to a list in same order as `output_names`.
    """
def map_missing_dict_keys(y_pred, struct):
    """Replaces missing dict keys in `struct` with `None` placeholders."""
def match_dtype_and_rank(y_t, y_p, sw):
    """Match dtype and rank of predictions."""
def get_custom_object_name(obj):
    """Returns the name to use for a custom loss or metric callable.

    Args:
      obj: Custom loss of metric callable

    Returns:
      Name to use, or `None` if the object was not recognized.
    """
