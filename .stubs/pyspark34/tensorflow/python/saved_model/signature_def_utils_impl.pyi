from _typeshed import Incomplete
from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.saved_model import signature_constants as signature_constants
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

def build_signature_def(inputs: Incomplete | None = None, outputs: Incomplete | None = None, method_name: Incomplete | None = None):
    """Utility function to build a SignatureDef protocol buffer.

  Args:
    inputs: Inputs of the SignatureDef defined as a proto map of string to
        tensor info.
    outputs: Outputs of the SignatureDef defined as a proto map of string to
        tensor info.
    method_name: Method name of the SignatureDef as a string.

  Returns:
    A SignatureDef protocol buffer constructed based on the supplied arguments.
  """
def regression_signature_def(examples, predictions):
    """Creates regression signature from given examples and predictions.

  This function produces signatures intended for use with the TensorFlow Serving
  Regress API (tensorflow_serving/apis/prediction_service.proto), and so
  constrains the input and output types to those allowed by TensorFlow Serving.

  Args:
    examples: A string `Tensor`, expected to accept serialized tf.Examples.
    predictions: A float `Tensor`.

  Returns:
    A regression-flavored signature_def.

  Raises:
    ValueError: If examples is `None`.
  """
def classification_signature_def(examples, classes, scores):
    """Creates classification signature from given examples and predictions.

  This function produces signatures intended for use with the TensorFlow Serving
  Classify API (tensorflow_serving/apis/prediction_service.proto), and so
  constrains the input and output types to those allowed by TensorFlow Serving.

  Args:
    examples: A string `Tensor`, expected to accept serialized tf.Examples.
    classes: A string `Tensor`.  Note that the ClassificationResponse message
      requires that class labels are strings, not integers or anything else.
    scores: a float `Tensor`.

  Returns:
    A classification-flavored signature_def.

  Raises:
    ValueError: If examples is `None`.
  """
def predict_signature_def(inputs, outputs):
    """Creates prediction signature from given inputs and outputs.

  This function produces signatures intended for use with the TensorFlow Serving
  Predict API (tensorflow_serving/apis/prediction_service.proto). This API
  imposes no constraints on the input and output types.

  Args:
    inputs: dict of string to `Tensor`.
    outputs: dict of string to `Tensor`.

  Returns:
    A prediction-flavored signature_def.

  Raises:
    ValueError: If inputs or outputs is `None`.
  """
def supervised_train_signature_def(inputs, loss, predictions: Incomplete | None = None, metrics: Incomplete | None = None): ...
def supervised_eval_signature_def(inputs, loss, predictions: Incomplete | None = None, metrics: Incomplete | None = None): ...
def is_valid_signature(signature_def):
    """Determine whether a SignatureDef can be served by TensorFlow Serving."""
def op_signature_def(op, key):
    """Creates a signature def with the output pointing to an op.

  Note that op isn't strictly enforced to be an Op object, and may be a Tensor.
  It is recommended to use the build_signature_def() function for Tensors.

  Args:
    op: An Op (or possibly Tensor).
    key: Key to graph element in the SignatureDef outputs.

  Returns:
    A SignatureDef with a single output pointing to the op.
  """
def load_op_from_signature_def(signature_def, key, import_scope: Incomplete | None = None):
    """Load an Op from a SignatureDef created by op_signature_def().

  Args:
    signature_def: a SignatureDef proto
    key: string key to op in the SignatureDef outputs.
    import_scope: Scope used to import the op

  Returns:
    Op (or possibly Tensor) in the graph with the same name as saved in the
      SignatureDef.

  Raises:
    NotFoundError: If the op could not be found in the graph.
  """
