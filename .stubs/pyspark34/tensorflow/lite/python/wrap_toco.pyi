from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow

def wrapped_toco_convert(model_flags_str, toco_flags_str, input_data_str, debug_info_str, enable_mlir_converter):
    """Wraps TocoConvert with lazy loader."""
def wrapped_experimental_mlir_quantize(input_data_str, disable_per_channel, fully_quantize, inference_type, input_data_type, output_data_type, enable_numeric_verify, enable_whole_model_verify, denylisted_ops, denylisted_nodes, enable_variable_quantization):
    """Wraps experimental mlir quantize model."""
def wrapped_experimental_mlir_sparsify(input_data_str):
    """Wraps experimental mlir sparsify model."""
def wrapped_register_custom_opdefs(custom_opdefs_list):
    """Wraps RegisterCustomOpdefs with lazy loader."""
def wrapped_retrieve_collected_errors():
    """Wraps RetrieveCollectedErrors with lazy loader."""
def wrapped_flat_buffer_file_to_mlir(model, input_is_filepath):
    """Wraps FlatBufferFileToMlir with lazy loader."""
