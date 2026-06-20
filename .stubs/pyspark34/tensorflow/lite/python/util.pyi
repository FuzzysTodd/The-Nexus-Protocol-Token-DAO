from _typeshed import Incomplete
from tensorflow.core.protobuf import graph_debug_info_pb2 as graph_debug_info_pb2
from tensorflow.lite.python import schema_util as schema_util
from tensorflow.lite.python.op_hint import convert_op_hints_to_stubs as convert_op_hints_to_stubs, find_all_hinted_output_nodes as find_all_hinted_output_nodes
from tensorflow.lite.tools import flatbuffer_utils as flatbuffer_utils
from tensorflow.python.eager import function as function
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.grappler import tf_optimizer as tf_optimizer

CONVERSION_METADATA_FIELD_NAME: str
model_input_signature: Incomplete
trace_model_call: Incomplete

def get_tf_type_name(tf_type):
    '''Converts tf.dtype (eg: tf.float32) to str (eg: "tf.float32").'''
def get_tensor_name(tensor):
    """Returns name of the input tensor.

  Args:
    tensor: tf.Tensor

  Returns:
    str
  """
def get_tensors_from_tensor_names(graph, tensor_names):
    """Gets the Tensors associated with the `tensor_names` in the provided graph.

  Args:
    graph: TensorFlow Graph.
    tensor_names: List of strings that represent names of tensors in the graph.

  Returns:
    A list of Tensor objects in the same order the names are provided.

  Raises:
    ValueError:
      tensor_names contains an invalid tensor name.
  """
def set_tensor_shapes(tensors, shapes) -> None:
    '''Sets Tensor shape for each tensor if the shape is defined.

  Args:
    tensors: TensorFlow ops.Tensor.
    shapes: Dict of strings representing input tensor names to list of
      integers representing input shapes (e.g., {"foo": : [1, 16, 16, 3]}).

  Raises:
    ValueError:
      `shapes` contains an invalid tensor.
      `shapes` contains an invalid shape for a valid tensor.
  '''
def get_grappler_config(optimizers_list):
    """Creates a tf.compat.v1.ConfigProto for configuring Grappler.

  Args:
    optimizers_list: List of strings that represents the list of optimizers.

  Returns:
    tf.ConfigProto.
  """
def run_graph_optimizations(graph_def, input_arrays, output_arrays, config, graph: Incomplete | None = None):
    """Apply standard TensorFlow optimizations to the graph_def.

  Args:
    graph_def: Frozen GraphDef to be optimized.
    input_arrays: List of arrays that are considered inputs of the graph.
    output_arrays: List of arrays that are considered outputs of the graph.
    config: tf.ConfigProto.
    graph: TensorFlow Graph. Required when Eager mode is enabled. (default None)

  Returns:
    A new, optimized GraphDef.
  """
def freeze_graph(sess, input_tensors, output_tensors):
    """Returns a frozen GraphDef.

  Runs a Grappler pass and freezes a graph with Variables in it. Otherwise the
  existing GraphDef is returned. The Grappler pass is only run on models that
  are frozen in order to inline the functions in the graph.
  If OpHints is present, it will try to convert the OpHint graph.

  Args:
    sess: TensorFlow Session.
    input_tensors: List of input tensors.
    output_tensors: List of output tensors (only .name is used from this).

  Returns:
    Frozen GraphDef.
  """
def is_frozen_graph(sess):
    """Determines if the graph is frozen.

  Determines if a graph has previously been frozen by checking for any
  operations of type Variable*. If variables are found, the graph is not frozen.

  Args:
    sess: TensorFlow Session.

  Returns:
    Bool.
  """
def build_debug_info_func(original_graph):
    """Returns a method to retrieve the `GraphDebugInfo` from the original graph.

  Args:
    original_graph: The original `Graph` containing all the op stack traces.

  Returns:
    A function which retrieves the stack traces from the original graph and
    converts them to a `GraphDebugInfo` for a given set of nodes.
  """
def convert_debug_info_func(saved_debug_info):
    """Returns a method to retrieve the `GraphDebugInfo` from the original graph.

  Args:
    saved_debug_info: The `GraphDebugInfo` containing all the debug info.

  Returns:
    A function which retrieves the stack traces from the original graph and
    converts them to a `GraphDebugInfo` for a given set of nodes.
  """
def get_debug_info(nodes_to_debug_info_func, converted_graph):
    """Returns the debug info for the original nodes in the `converted_graph`.

  Args:
    nodes_to_debug_info_func: The method to collect the op debug info for the
      nodes.
    converted_graph: A `GraphDef` after optimization and transformation.

  Returns:
    `GraphDebugInfo` for all the original nodes in `converted_graph`.
  """
def convert_bytes_to_c_source(data, array_name, max_line_width: int = 80, include_guard: Incomplete | None = None, include_path: Incomplete | None = None, use_tensorflow_license: bool = False):
    """Returns strings representing a C constant array containing `data`.

  Args:
    data: Byte array that will be converted into a C constant.
    array_name: String to use as the variable name for the constant array.
    max_line_width: The longest line length, for formatting purposes.
    include_guard: Name to use for the include guard macro definition.
    include_path: Optional path to include in the source file.
    use_tensorflow_license: Whether to include the standard TensorFlow Apache2
      license in the generated files.

  Returns:
    Text that can be compiled as a C source file to link in the data as a
    literal array of values.
    Text that can be used as a C header file to reference the literal array.
  """
def get_quantize_opcode_idx(model):
    """Returns the quantize op idx."""
def get_dequantize_opcode_idx(model):
    """Returns the quantize op idx."""
def modify_model_io_type(model, inference_input_type=..., inference_output_type=...):
    """Modify the input/output type of a tflite model.

  Args:
    model: A tflite model.
    inference_input_type: tf.DType representing modified input type.
      (default tf.float32. If model input is int8 quantized, it must be in
      {tf.float32, tf.int8,tf.uint8}, else if model input is int16 quantized,
      it must be in {tf.float32, tf.int16}, else it must be tf.float32)
    inference_output_type: tf.DType representing modified output type.
      (default tf.float32. If model output is int8 dequantized, it must be in
      {tf.float32, tf.int8,tf.uint8}, else if model output is int16 dequantized,
      it must be in {tf.float32, tf.int16}, else it must be tf.float32)
  Returns:
    A tflite model with modified input/output type.

  Raises:
    ValueError: If `inference_input_type`/`inference_output_type` is unsupported
      or a supported integer type is specified for a model whose input/output is
      not quantized/dequantized.
    RuntimeError: If the modification was unsuccessful.

  """
def get_sparsity_modes(model_object):
    """Get sparsity modes used in a tflite model.

  The sparsity modes are listed in conversion_metadata.fbs file.

  Args:
    model_object: A tflite model in object form.

  Returns:
    The list of sparsity modes used in the model.
  """
def populate_conversion_metadata(model_object, metadata):
    """Add or update conversion metadata to a tflite model.

  Args:
    model_object: A tflite model in object form.
    metadata: The conversion metadata.

  Returns:
    A tflite model object with embedded conversion metadata.
  """
def get_conversion_metadata(model_buffer):
    """Read conversion metadata from a tflite model.

  Args:
    model_buffer: A tflite model.

  Returns:
    The conversion metadata or None if it is not populated.
  """
