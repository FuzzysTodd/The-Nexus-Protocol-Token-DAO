from _typeshed import Incomplete
from keras import backend as backend, losses as losses, optimizers as optimizers
from keras.engine import base_layer_utils as base_layer_utils
from keras.optimizers import optimizer_v1 as optimizer_v1
from keras.saving.legacy import serialization as serialization
from keras.utils import version_utils as version_utils
from keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite

def extract_model_metrics(model):
    """Convert metrics from a Keras model `compile` API to dictionary.

    This is used for converting Keras models to Estimators and SavedModels.

    Args:
      model: A `tf.keras.Model` object.

    Returns:
      Dictionary mapping metric names to metric instances. May return `None` if
      the model does not contain any metrics.
    """
def model_call_inputs(model, keep_original_batch_size: bool = False):
    """Inspect model to get its input signature.

    The model's input signature is a list with a single (possibly-nested)
    object. This is due to the Keras-enforced restriction that tensor inputs
    must be passed in as the first argument.

    For example, a model with input {'feature1': <Tensor>, 'feature2': <Tensor>}
    will have input signature:
    [{'feature1': TensorSpec, 'feature2': TensorSpec}]

    Args:
      model: Keras Model object.
      keep_original_batch_size: A boolean indicating whether we want to keep
        using the original batch size or set it to None. Default is `False`,
        which means that the batch dim of the returned input signature will
        always be set to `None`.

    Returns:
      A tuple containing `(args, kwargs)` TensorSpecs of the model call function
      inputs.
      `kwargs` does not contain the `training` argument.
    """
def raise_model_input_error(model) -> None: ...
def trace_model_call(model, input_signature: Incomplete | None = None):
    """Trace the model call to create a tf.function for exporting a Keras model.

    Args:
      model: A Keras model.
      input_signature: optional, a list of tf.TensorSpec objects specifying the
        inputs to the model.

    Returns:
      A tf.function wrapping the model's call function with input signatures
      set.

    Raises:
      ValueError: if input signature cannot be inferred from the model.
    """
def model_metadata(model, include_optimizer: bool = True, require_config: bool = True):
    """Returns a dictionary containing the model metadata."""
def should_overwrite(filepath, overwrite):
    """Returns whether the filepath should be overwritten."""
def compile_args_from_training_config(training_config, custom_objects: Incomplete | None = None):
    """Return model.compile arguments from training config."""
def try_build_compiled_arguments(model) -> None: ...
def is_hdf5_filepath(filepath): ...
