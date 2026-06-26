import enum
from _typeshed import Incomplete
from tensorflow.lite.python import lite_constants as lite_constants, util as util, wrap_toco as wrap_toco
from tensorflow.lite.python.convert_phase import Component as Component, ConverterError as ConverterError, SubComponent as SubComponent, convert_phase as convert_phase
from tensorflow.lite.toco import types_pb2 as _types_pb2
from tensorflow.lite.tools import flatbuffer_utils as flatbuffer_utils
from tensorflow.python.framework import dtypes as dtypes, tensor_shape as tensor_shape
from tensorflow.python.util import deprecation as deprecation

def convert_tensor_tf_type_to_tflite_type(tf_type: dtypes.DType, usage: str = '') -> _types_pb2.IODataType:
    """Convert tensor type from tf type to tflite type.

  Args:
    tf_type: TensorFlow type.
    usage: Text describing the reason for invoking this function.

  Raises:
    ValueError: If `tf_type` is unsupported.

  Returns:
    tflite_type: TFLite type. Refer to lite/toco/types.proto.
  """
def convert_inference_tf_type_to_tflite_type(tf_type: dtypes.DType, usage: str = '') -> _types_pb2.IODataType:
    """Convert inference type from tf type to tflite type.

  Args:
    tf_type: TensorFlow type.
    usage: Text describing the reason for invoking this function.

  Raises:
    ValueError: If `tf_type` is unsupported.

  Returns:
    tflite_type: TFLite type. Refer to lite/toco/types.proto.
  """

class OpsSet(enum.Enum):
    """Enum class defining the sets of ops available to generate TFLite models.

  WARNING: Experimental interface, subject to change.
  """
    TFLITE_BUILTINS: str
    SELECT_TF_OPS: str
    TFLITE_BUILTINS_INT8: str
    EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8: str
    EXPERIMENTAL_STABLEHLO_OPS: str
    @staticmethod
    def get_options():
        """Returns a list of OpsSet options as a list of strings."""

def mlir_quantize(input_data_str, disable_per_channel: bool = False, fully_quantize: bool = False, inference_type=..., input_data_type=..., output_data_type=..., enable_numeric_verify: bool = False, enable_whole_model_verify: bool = False, denylisted_ops: Incomplete | None = None, denylisted_nodes: Incomplete | None = None, enable_variable_quantization: bool = False):
    """Quantize `input_data_str` with calibration results.

  Args:
    input_data_str: Input data in serialized form (e.g. a TFLITE model with
      calibration results).
    disable_per_channel: Bool indicating whether to do per-channel or per-tensor
      quantization
    fully_quantize: Bool indicating whether to fully quantize the model. Besides
      model body, the input/output will be quantized as well.
    inference_type: Data type for the activations. The default value is int8.
    input_data_type: Data type for the inputs. The default value is float32.
    output_data_type: Data type for the outputs. The default value is float32.
    enable_numeric_verify: Experimental. Subject to change. Bool indicating
      whether to add NumericVerify ops into the debug mode quantized model.
    enable_whole_model_verify: Experimental. Subject to change. Bool indicating
      whether to add verification for layer by layer, or on whole model. When
      disabled (per-layer) float and quantized ops will be run from same input
      (output of previous quantized layer). When enabled, float and quantized
      ops will run with respective float and quantized output of previous ops.
    denylisted_ops: Experimental. Subject to change. Set of ops to denylist.
    denylisted_nodes: Experimental. Subject to change. Set of notes to denylist.
    enable_variable_quantization: Experimental. Subject to change. Bool
      indicating whether to enable quantization of the residual variables
      remaining after the variable freezing pass.

  Returns:
    Quantized model in serialized form (e.g. a TFLITE model) with floating-point
    inputs and outputs.
  """
def mlir_sparsify(input_data_str):
    """Sparsify `input_data_str` to encode sparse tensor with proper format.

  Args:
    input_data_str: Input data in serialized form (e.g. a TFLITE model).

  Returns:
    Sparsified model in serialized form (e.g. a TFLITE model).
  """
def register_custom_opdefs(custom_opdefs_list):
    """Register the given custom opdefs to the TensorFlow global op registry.

  Args:
    custom_opdefs_list: String representing the custom ops OpDefs that are
      included in the GraphDef.

  Returns:
    True if the registration is successfully completed.
  """
def convert(model_flags_str, conversion_flags_str, input_data_str, debug_info_str: Incomplete | None = None, enable_mlir_converter: bool = True):
    """Converts `input_data_str` to a TFLite model.

  Args:
    model_flags_str: Serialized proto describing model properties, see
      `model_flags.proto`.
    conversion_flags_str: Serialized proto describing conversion properties, see
      `toco/toco_flags.proto`.
    input_data_str: Input data in serialized form (e.g. a graphdef is common, or
      it can be hlo text or proto)
    debug_info_str: Serialized `GraphDebugInfo` proto describing logging
      information. (default None)
    enable_mlir_converter: Enables MLIR-based conversion. (default True)

  Returns:
    Converted model in serialized form (e.g. a TFLITE model is common).
  Raises:
    ConverterError: When conversion fails in TFLiteConverter, usually due to
      ops not being supported.
    RuntimeError: When conversion fails, an exception is raised with the error
      message embedded.
  """
def build_model_flags(change_concat_input_ranges: bool = False, allow_nonexistent_arrays: bool = False, saved_model_dir: Incomplete | None = None, saved_model_version: int = 0, saved_model_tags: Incomplete | None = None, saved_model_exported_names: Incomplete | None = None, **_):
    """Builds the model flags object from params.

  Args:
    change_concat_input_ranges: Boolean to change behavior of min/max ranges for
      inputs and outputs of the concat operator for quantized models. Changes
      the ranges of concat operator overlap when true. (default False)
    allow_nonexistent_arrays: Allow specifying array names that don't exist or
      are unused in the final graph. (default False)
    saved_model_dir: Filepath of the saved model to be converted. This value
      will be non-empty only when the saved model import path will be used.
      Otherwises, the graph def-based conversion will be processed.
    saved_model_version: SavedModel file format version of The saved model file
      to be converted. This value will be set only when the SavedModel import
      path will be used.
    saved_model_tags: Set of string saved model tags, formatted in the
      comma-separated value. This value will be set only when the SavedModel
      import path will be used.
    saved_model_exported_names: Names to be exported (default: export all) when
      the saved model import path is on. This value will be set only when the
      SavedModel import path will be used.

  Returns:
    model_flags: protocol buffer describing the model.
  """
def build_conversion_flags(inference_type=..., inference_input_type: Incomplete | None = None, input_format=..., output_format=..., default_ranges_stats: Incomplete | None = None, drop_control_dependency: bool = True, reorder_across_fake_quant: bool = False, allow_custom_ops: bool = False, post_training_quantize: bool = False, quantize_to_float16: bool = False, dump_graphviz_dir: Incomplete | None = None, dump_graphviz_video: bool = False, target_ops: Incomplete | None = None, conversion_summary_dir: Incomplete | None = None, select_user_tf_ops: Incomplete | None = None, allow_all_select_tf_ops: bool = False, enable_tflite_resource_variables: bool = True, unfold_batchmatmul: bool = True, lower_tensor_list_ops: bool = True, default_to_single_batch_in_tensor_list_ops: bool = False, accumulation_type: Incomplete | None = None, allow_bfloat16: bool = False, unfold_large_splat_constant: bool = False, supported_backends: Incomplete | None = None, disable_per_channel_quantization: bool = False, enable_mlir_dynamic_range_quantizer: bool = False, tf_quantization_mode: Incomplete | None = None, disable_infer_tensor_range: bool = False, use_fake_quant_num_bits: bool = False, enable_dynamic_update_slice: bool = False, preserve_assert_op: bool = False, guarantee_all_funcs_one_use: bool = False, enable_mlir_variable_quantization: bool = False, **_):
    '''Builds protocol buffer describing a conversion of a model.

  Typically this is to convert from TensorFlow GraphDef to TFLite, in which
  case the default `input_format` and `output_format` are sufficient.

  Args:
    inference_type: Data type of numeric arrays, excluding the input layer.
      (default tf.float32, must be in {tf.float32, tf.int8, tf.uint8})
    inference_input_type: Data type of the numeric arrays in the input layer. If
      `inference_input_type` is in {tf.int8, tf.uint8}, then
      `quantized_input_stats` must be provided. (default is the value assigned
      to `inference_type`, must be in {tf.float32, tf.int8, tf.uint8})
    input_format: Type of data to read. (default TENSORFLOW_GRAPHDEF, must be in
      {TENSORFLOW_GRAPHDEF})
    output_format: Output file format. (default TFLITE, must be in {TFLITE,
      GRAPHVIZ_DOT})
    default_ranges_stats: Tuple of integers representing (min, max) range values
      for all arrays without a specified range. Intended for experimenting with
      quantization via "dummy quantization". (default None)
    drop_control_dependency: Boolean indicating whether to drop control
      dependencies silently. This is due to TFLite not supporting control
      dependencies. (default True)
    reorder_across_fake_quant: Boolean indicating whether to reorder FakeQuant
      nodes in unexpected locations. Used when the location of the FakeQuant
      nodes is preventing graph transformations necessary to convert the graph.
      Results in a graph that differs from the quantized training graph,
      potentially causing differing arithmetic behavior. (default False)
    allow_custom_ops: Boolean indicating whether to allow custom operations.
      When false any unknown operation is an error. When true, custom ops are
      created for any op that is unknown. The developer will need to provide
      these to the TensorFlow Lite runtime with a custom resolver. (default
      False)
    post_training_quantize: Boolean indicating whether to quantize the weights
      of the converted float model. Model size will be reduced and there will be
      latency improvements (at the cost of accuracy). (default False)
    quantize_to_float16: Boolean indicating whether to convert float buffers to
      float16. (default False)
    dump_graphviz_dir: Full filepath of folder to dump the graphs at various
      stages of processing GraphViz .dot files. Preferred over
      --output_format=GRAPHVIZ_DOT in order to keep the requirements of the
      output file. (default None)
    dump_graphviz_video: Boolean indicating whether to dump the graph after
      every graph transformation. (default False)
    target_ops: Experimental flag, subject to change. Set of OpsSet options
      indicating which converter to use. (default set([OpsSet.TFLITE_BUILTINS]))
    conversion_summary_dir: A string, the path to the generated conversion logs.
    select_user_tf_ops: List of user\'s defined TensorFlow ops need to be
      supported in the TensorFlow Lite runtime. These ops will be supported as
      select TensorFlow ops.
    allow_all_select_tf_ops: If True, automatically add all TF ops (including
      custom TF ops) to the converted model as flex ops.
    enable_tflite_resource_variables: Experimental flag, subject to change.
      Enables conversion of resource variables. (default False)
    unfold_batchmatmul: Whether to unfold tf.BatchMatMul to a set of
      tfl.fully_connected ops. If not, translate to tfl.batch_matmul.
    lower_tensor_list_ops: Whether to lower tensor list ops to builtin ops. If
      not, use Flex tensor list ops.
    default_to_single_batch_in_tensor_list_ops: Whether to force to use batch
      size one when the tensor list ops has the unspecified batch size.
    accumulation_type: Data type of the accumulators in quantized inference.
      Typically used for float16 quantization and is either fp16 or fp32.
    allow_bfloat16: Whether the converted model supports reduced precision
      inference with the bfloat16 type.
    unfold_large_splat_constant: Whether to unfold large splat constant tensors
      in the flatbuffer model to reduce size.
    supported_backends: List of TFLite backends which needs to check
      compatibility.
    disable_per_channel_quantization: Disable per-channel quantized weights for
      dynamic range quantization. Only per-tensor quantization will be used.
    enable_mlir_dynamic_range_quantizer: Enable MLIR dynamic range quantization.
      If False, the old converter dynamic range quantizer is used.
    tf_quantization_mode: Indicates the mode of TF Quantization when the output
      model is used for TF Quantization.
    disable_infer_tensor_range: Disable infering tensor ranges.
    use_fake_quant_num_bits: Allow quantization parameters to be calculated from
      num_bits attribute.
    enable_dynamic_update_slice: Enable to convert to DynamicUpdateSlice op.
      (default: False).
    preserve_assert_op: Whether to preserve `TF::AssertOp` (default: False).
    guarantee_all_funcs_one_use: Whether to clone functions so that each
      function only has a single use. This option will be helpful if the
      conversion fails when the `PartitionedCall` or `StatefulPartitionedCall`
      can\'t be properly inlined (default: False).
    enable_mlir_variable_quantization: Enable MLIR variable quantization. There
      is a variable freezing pass, but some variables may not be fully frozen by
      it. This flag enables quantization of those residual variables in the MLIR
      graph.

  Returns:
    conversion_flags: protocol buffer describing the conversion process.
  Raises:
    ValueError, if the input tensor type is unknown.
  '''
def convert_graphdef_with_arrays(input_data, input_arrays_with_shape, output_arrays, control_output_arrays, **kwargs):
    '''Convert a frozen GraphDef that can\'t be loaded in TF.

  Conversion can be customized by providing arguments that are forwarded to
  `build_model_flags` and `build_conversion_flags` (see documentation).

  Args:
    input_data: Input data (i.e. often `sess.graph_def`),
    input_arrays_with_shape: Tuple of strings representing input tensor names
      and list of integers representing input shapes (e.g., [("foo" : [1, 16,
      16, 3])]). Use only when graph cannot be loaded into TensorFlow and when
      `input_tensors` is None.
    output_arrays: List of output tensors to freeze graph with. Use only when
      graph cannot be loaded into TensorFlow and when `output_tensors` is None.
    control_output_arrays: Control output node names. This is used when
      converting a Graph with no output tensors. For example, if the graph\'s
      last operation is a Print op, just specify that op\'s name in this field.
      This can be used together with the `output_arrays` parameter.
    **kwargs: See `build_model_flags` and `build_conversion_flags`.

  Returns:
    The converted data. For example if TFLite was the destination, then
    this will be a tflite flatbuffer in a bytes array.

  Raises:
    Defined in `build_conversion_flags`.
  '''
def convert_graphdef(input_data, input_tensors, output_tensors, **kwargs):
    """Convert a frozen GraphDef model using the TF Lite converter.

  Conversion can be customized by providing arguments that are forwarded to
  `build_model_flags` and `build_conversion_flags` (see documentation).

  Args:
    input_data: Input data (i.e. often `sess.graph_def`),
   input_tensors: List of input tensors. Type and shape are computed using
     `foo.shape` and `foo.dtype`.
    output_tensors: List of output tensors (only .name is used from this).
    **kwargs: See `build_model_flags` and `build_conversion_flags`.

  Returns:
    The converted data. For example if TFLite was the destination, then
    this will be a tflite flatbuffer in a bytes array.

  Raises:
    Defined in `build_conversion_flags`.
  """
def convert_saved_model(**kwargs):
    """Converts a SavedModel using TF Lite converter."""
def convert_jax_hlo(input_content, input_names, is_proto_format, **kwargs):
    """Converts a Jax hlo-based model using TFLite converter."""
def toco_convert(input_data, input_tensors, output_tensors, *args, **kwargs):
    """Convert a TensorFlow GraphDef to TFLite.

  This function is deprecated. Please use `tf.lite.TFLiteConverter` API instead.
  Conversion can be customized by providing arguments that are forwarded to
  `build_model_flags` and `build_conversion_flags` (see documentation for
  details).
  Args:
    input_data: Input data (i.e. often `sess.graph_def`).
    input_tensors: List of input tensors. Type and shape are computed using
      `foo.shape` and `foo.dtype`.
    output_tensors: List of output tensors (only .name is used from this).
    *args: See `build_model_flags` and `build_conversion_flags`.
    **kwargs: See `build_model_flags` and `build_conversion_flags`.

  Returns:
    The converted TensorFlow Lite model in a bytes array.

  Raises:
    Defined in `convert`.
  """
def deduplicate_readonly_buffers(tflite_model):
    """Generates a new model byte array after deduplicating readonly buffers.

  This function should be invoked after the model optimization toolkit. The
  model optimization toolkit assumes that each tensor object owns its each
  buffer separately.

  Args:
    tflite_model: TFLite flatbuffer in a byte array to be deduplicated.

  Returns:
    TFLite flatbuffer in a bytes array, processed with the deduplication method.
  """
