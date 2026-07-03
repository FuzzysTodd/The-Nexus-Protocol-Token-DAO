from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.lite.python import interpreter as interpreter, lite as lite
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.grappler import tf_optimizer as tf_optimizer
from tensorflow.python.training import saver as saver

def grappler_optimize(graph, fetches: Incomplete | None = None, config_proto: Incomplete | None = None):
    """Tries to optimize the provided graph using grappler.

  Args:
    graph: A `tf.Graph` instance containing the graph to optimize.
    fetches: An optional list of `Tensor`s to fetch (i.e. not optimize away).
      Grappler uses the 'train_op' collection to look for fetches, so if not
      provided this collection should be non-empty.
    config_proto: An optional `tf.compat.v1.ConfigProto` to use when rewriting
      the graph.

  Returns:
    A `tf.compat.v1.GraphDef` containing the rewritten graph.
  """
def tflite_convert(fn, input_templates):
    """Converts the provided fn to tf.lite model.

  Args:
    fn: A callable that expects a list of inputs like input_templates that
      returns a tensor or structure of tensors.
    input_templates: A list of Tensors, ndarrays or TensorSpecs describing the
      inputs that fn expects. The actual values of the Tensors or ndarrays are
      unused.

  Returns:
    The serialized tf.lite model.
  """
def evaluate_tflite_model(tflite_model, input_ndarrays):
    """Evaluates the provided tf.lite model with the given input ndarrays.

  Args:
    tflite_model: bytes. The serialized tf.lite model.
    input_ndarrays: A list of NumPy arrays to feed as input to the model.

  Returns:
    A list of ndarrays produced by the model.

  Raises:
    ValueError: If the number of input arrays does not match the number of
      inputs the model expects.
  """
