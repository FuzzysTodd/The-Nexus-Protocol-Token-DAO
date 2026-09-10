from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import util as util
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from typing import NamedTuple

def wrap_and_check_input_tensors(tensors, field_name, allow_int_keys: bool = False):
    """Ensure that tensors is a dict of str to Tensor mappings.

  Args:
    tensors: dict of `str` (or `int`s if `allow_int_keys=True`) to `Tensors`, or
      a single `Tensor`.
    field_name: name of the member field of `ServingInputReceiver` whose value
      is being passed to `tensors`.
    allow_int_keys: If set to true, the `tensor` dict keys may also be `int`s.

  Returns:
    dict of str to Tensors; this is the original dict if one was passed, or
    the original tensor wrapped in a dictionary.

  Raises:
    ValueError: if tensors is None, or has non-string keys,
      or non-Tensor values
  """

class ServingInputReceiver(NamedTuple('ServingInputReceiver', [('features', Incomplete), ('receiver_tensors', Incomplete), ('receiver_tensors_alternatives', Incomplete)])):
    """A return type for a serving_input_receiver_fn.

  Attributes:
    features: A `Tensor`, `SparseTensor`, or dict of string or int to `Tensor`
      or `SparseTensor`, specifying the features to be passed to the model.
      Note: if `features` passed is not a dict, it will be wrapped in a dict
        with a single entry, using 'feature' as the key.  Consequently, the
        model
      must accept a feature dict of the form {'feature': tensor}.  You may use
        `TensorServingInputReceiver` if you want the tensor to be passed as is.
    receiver_tensors: A `Tensor`, `SparseTensor`, or dict of string to `Tensor`
      or `SparseTensor`, specifying input nodes where this receiver expects to
      be fed by default.  Typically, this is a single placeholder expecting
      serialized `tf.Example` protos.
    receiver_tensors_alternatives: a dict of string to additional groups of
      receiver tensors, each of which may be a `Tensor`, `SparseTensor`, or dict
      of string to `Tensor` or`SparseTensor`. These named receiver tensor
      alternatives generate additional serving signatures, which may be used to
      feed inputs at different points within the input receiver subgraph.  A
      typical usage is to allow feeding raw feature `Tensor`s *downstream* of
      the tf.parse_example() op. Defaults to None.
  """
    def __new__(cls, features, receiver_tensors, receiver_tensors_alternatives: Incomplete | None = None): ...

class TensorServingInputReceiver(NamedTuple('TensorServingInputReceiver', [('features', Incomplete), ('receiver_tensors', Incomplete), ('receiver_tensors_alternatives', Incomplete)])):
    """A return type for a serving_input_receiver_fn.

  This is for use with models that expect a single `Tensor` or `SparseTensor`
  as an input feature, as opposed to a dict of features.

  The normal `ServingInputReceiver` always returns a feature dict, even if it
  contains only one entry, and so can be used only with models that accept such
  a dict.  For models that accept only a single raw feature, the
  `serving_input_receiver_fn` provided to `Estimator.export_saved_model()`
  should return this `TensorServingInputReceiver` instead.  See:
  https://github.com/tensorflow/tensorflow/issues/11674

  Note that the receiver_tensors and receiver_tensor_alternatives arguments
  will be automatically converted to the dict representation in either case,
  because the SavedModel format requires each input `Tensor` to have a name
  (provided by the dict key).

  Attributes:
    features: A single `Tensor` or `SparseTensor`, representing the feature to
      be passed to the model.
    receiver_tensors: A `Tensor`, `SparseTensor`, or dict of string to `Tensor`
      or `SparseTensor`, specifying input nodes where this receiver expects to
      be fed by default.  Typically, this is a single placeholder expecting
      serialized `tf.Example` protos.
    receiver_tensors_alternatives: a dict of string to additional groups of
      receiver tensors, each of which may be a `Tensor`, `SparseTensor`, or dict
      of string to `Tensor` or`SparseTensor`. These named receiver tensor
      alternatives generate additional serving signatures, which may be used to
      feed inputs at different points within the input receiver subgraph.  A
      typical usage is to allow feeding raw feature `Tensor`s *downstream* of
      the tf.parse_example() op. Defaults to None.
  """
    def __new__(cls, features, receiver_tensors, receiver_tensors_alternatives: Incomplete | None = None): ...

class UnsupervisedInputReceiver(ServingInputReceiver):
    """A return type for a training_input_receiver_fn or eval_input_receiver_fn.

  This differs from SupervisedInputReceiver in that it does not require a set
  of labels.

  Attributes:
    features: A `Tensor`, `SparseTensor`, or dict of string to `Tensor` or
      `SparseTensor`, specifying the features to be passed to the model.
    receiver_tensors: A `Tensor`, `SparseTensor`, or dict of string to `Tensor`
      or `SparseTensor`, specifying input nodes where this receiver expects to
      be fed by default.  Typically, this is a single placeholder expecting
      serialized `tf.Example` protos.
  """
    def __new__(cls, features, receiver_tensors): ...

class SupervisedInputReceiver(NamedTuple('SupervisedInputReceiver', [('features', Incomplete), ('labels', Incomplete), ('receiver_tensors', Incomplete)])):
    """A return type for a training_input_receiver_fn or eval_input_receiver_fn.

  This differs from a ServingInputReceiver in that (1) this receiver expects
  a set of labels to be passed in with features, and (2) this receiver does
  not support receiver_tensors_alternatives, which are primarily used for
  serving.

  The expected return values are:
    features: A `Tensor`, `SparseTensor`, or dict of string or int to `Tensor`
      or `SparseTensor`, specifying the features to be passed to the model.
    labels: A `Tensor`, `SparseTensor`, or dict of string or int to `Tensor` or
      `SparseTensor`, specifying the labels to be passed to the model.
    receiver_tensors: A `Tensor`, `SparseTensor`, or dict of string to `Tensor`
      or `SparseTensor`, specifying input nodes where this receiver expects to
      be fed by default.  Typically, this is a single placeholder expecting
      serialized `tf.Example` protos.

  """
    def __new__(cls, features, labels, receiver_tensors): ...

def build_parsing_serving_input_receiver_fn(feature_spec, default_batch_size: Incomplete | None = None):
    """Build a serving_input_receiver_fn expecting fed tf.Examples.

  Creates a serving_input_receiver_fn that expects a serialized tf.Example fed
  into a string placeholder.  The function parses the tf.Example according to
  the provided feature_spec, and returns all parsed Tensors as features.

  Args:
    feature_spec: a dict of string to `VarLenFeature`/`FixedLenFeature`.
    default_batch_size: the number of query examples expected per batch. Leave
      unset for variable batch size (recommended).

  Returns:
    A serving_input_receiver_fn suitable for use in serving.
  """
def build_raw_serving_input_receiver_fn(features, default_batch_size: Incomplete | None = None):
    """Build a serving_input_receiver_fn expecting feature Tensors.

  Creates an serving_input_receiver_fn that expects all features to be fed
  directly.

  Args:
    features: a dict of string to `Tensor`.
    default_batch_size: the number of query examples expected per batch. Leave
      unset for variable batch size (recommended).

  Returns:
    A serving_input_receiver_fn.
  """
def build_raw_supervised_input_receiver_fn(features, labels, default_batch_size: Incomplete | None = None):
    """Build a supervised_input_receiver_fn for raw features and labels.

  This function wraps tensor placeholders in a supervised_receiver_fn
  with the expectation that the features and labels appear precisely as
  the model_fn expects them. Features and labels can therefore be dicts of
  tensors, or raw tensors.

  Args:
    features: a dict of string to `Tensor` or `Tensor`.
    labels: a dict of string to `Tensor` or `Tensor`.
    default_batch_size: the number of query examples expected per batch. Leave
      unset for variable batch size (recommended).

  Returns:
    A supervised_input_receiver_fn.

  Raises:
    ValueError: if features and labels have overlapping keys.
  """
def build_supervised_input_receiver_fn_from_input_fn(input_fn, **input_fn_args):
    """Get a function that returns a SupervisedInputReceiver matching an input_fn.

  Note that this function calls the input_fn in a local graph in order to
  extract features and labels. Placeholders are then created from those
  features and labels in the default graph.

  Args:
    input_fn: An Estimator input_fn, which is a function that returns one of:
      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a tuple
        (features, labels) with same constraints as below.
      * A tuple (features, labels): Where `features` is a `Tensor` or a
        dictionary of string feature name to `Tensor` and `labels` is a `Tensor`
        or a dictionary of string label name to `Tensor`. Both `features` and
        `labels` are consumed by `model_fn`. They should satisfy the expectation
        of `model_fn` from inputs.
    **input_fn_args: set of kwargs to be passed to the input_fn. Note that these
      will not be checked or validated here, and any errors raised by the
      input_fn will be thrown to the top.

  Returns:
    A function taking no arguments that, when called, returns a
    SupervisedInputReceiver. This function can be passed in as part of the
    input_receiver_map when exporting SavedModels from Estimator with multiple
    modes.
  """

build_all_signature_defs: Incomplete
get_temp_export_dir: Incomplete
get_timestamped_export_dir: Incomplete
