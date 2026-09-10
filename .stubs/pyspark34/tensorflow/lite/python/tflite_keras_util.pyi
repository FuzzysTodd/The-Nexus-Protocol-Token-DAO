from _typeshed import Incomplete
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.util import keras_deps as keras_deps, nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc

def model_input_signature(model, keep_original_batch_size: bool = False):
    """Inspect model to get its input signature.

  The model's input signature is a list with a single (possibly-nested) object.
  This is due to the Keras-enforced restriction that tensor inputs must be
  passed in as the first argument.

  For example, a model with input {'feature1': <Tensor>, 'feature2': <Tensor>}
  will have input signature: [{'feature1': TensorSpec, 'feature2': TensorSpec}]

  Args:
    model: Keras Model object.
    keep_original_batch_size: A boolean indicating whether we want to keep using
      the original batch size or set it to None. Default is `False`, which means
      that the batch dim of the returned input signature will always be set to
      `None`.

  Returns:
    A list containing either a single TensorSpec or an object with nested
    TensorSpecs. This list does not contain the `training` argument.
  """
def raise_model_input_error(model) -> None: ...
def create_pseudo_output_names(outputs):
    """Create pseudo output names for a subclassed Model."""
def trace_model_call(model, input_signature: Incomplete | None = None):
    """Trace the model call to create a tf.function for exporting a Keras model.

  Args:
    model: A Keras model.
    input_signature: optional, a list of tf.TensorSpec objects specifying the
      inputs to the model.

  Returns:
    A tf.function wrapping the model's call function with input signatures set.

  Raises:
    ValueError: if input signature cannot be inferred from the model.
  """
