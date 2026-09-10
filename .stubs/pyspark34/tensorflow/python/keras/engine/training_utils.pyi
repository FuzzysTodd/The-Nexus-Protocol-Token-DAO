from tensorflow.python.framework import tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util import nest as nest

def slice_arrays(arrays, indices, contiguous: bool = True):
    """Slices batches out of provided arrays (workaround for eager tensors).

  Unfortunately eager tensors don't have the same slicing behavior as
  Numpy arrays (they follow the same slicing behavior as symbolic TF tensors),
  hence we cannot use `generic_utils.slice_arrays` directly
  and we have to implement this workaround based on `concat`. This has a
  performance cost.

  Args:
    arrays: Single array or list of arrays.
    indices: List of indices in the array that should be included in the output
      batch.
    contiguous: Boolean flag indicating whether the indices are contiguous.

  Returns:
    Slice of data (either single array or list of arrays).
  """
def handle_partial_sample_weights(outputs, sample_weights, sample_weight_modes, check_all_flat: bool = False):
    """Adds 1.0 as sample weights for the outputs for which there is no weight.

  Args:
    outputs: List of model outputs.
    sample_weights: List of sample weight inputs.
    sample_weight_modes: List of sample weight modes or None.
    check_all_flat: Ensure that inputs are not nested structures. This is not
      a free check, so we may not want to run it eagerly every iteration.

  Returns:
    Tuple of sample weights, one sample weight for every output, and booleans
    describing the raw sample weights.
  """

class RespectCompiledTrainableState:
    """Set and restore trainable state if it has changed since compile.

  The keras API guarantees that the value of each Layer's `trainable` property
  at `Model.compile` time will be used when training that model. In order to
  respect this requirement, it may be necessary to set the trainable value of
  layers to their compile time values before beginning a training endpoint and
  restore the values before returing from said endpoint. This scope checks if
  any layer's trainable state has changed since Model compile, and performs this
  set and un-set bookkeeping.

  However, the trainable state of a layer changes quite infrequently, if ever,
  for many kinds of workflows. Moreover, updating every layer in a model is an
  expensive operation. As a result, we will only explicitly set and unset the
  trainable state of a model if a trainable value has changed since compile.
  """
    def __init__(self, model) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_arg: type[BaseException] | None, value_arg: BaseException | None, traceback_arg: types.TracebackType | None): ...

def get_input_shape_and_dtype(layer):
    """Retrieves input shape and input dtype of layer if applicable.

  Args:
    layer: Layer (or model) instance.

  Returns:
    Tuple (input_shape, input_dtype). Both could be None if the layer
      does not have a defined input shape.

  Raises:
    ValueError: in case an empty Sequential or Functional model is passed.
  """
def get_static_batch_size(layer):
    """Gets the static batch size of a Layer.

  Args:
    layer: a `Layer` instance.

  Returns:
    The static batch size of a Layer.
  """
def list_to_tuple(maybe_list):
    """Datasets will stack the list of tensor, so switch them to tuples."""
