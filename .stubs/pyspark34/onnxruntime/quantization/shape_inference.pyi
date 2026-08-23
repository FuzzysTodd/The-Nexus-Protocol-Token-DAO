from .quant_utils import add_pre_process_metadata as add_pre_process_metadata
from _typeshed import Incomplete
from onnxruntime.tools.symbolic_shape_infer import SymbolicShapeInference as SymbolicShapeInference

logger: Incomplete

def quant_pre_process(input_model_path: str, output_model_path: str, skip_optimization: bool = False, skip_onnx_shape: bool = False, skip_symbolic_shape: bool = False, auto_merge: bool = False, int_max: int = ..., guess_output_rank: bool = False, verbose: int = 0, save_as_external_data: bool = False, all_tensors_to_one_file: bool = False, external_data_location: str | None = None, external_data_size_threshold: int = 1024) -> None:
    '''Shape inference and model optimization, in preparation for quantization.

    Args:
        input_model_path: Path to the input model file")
        output_model_path: Path to the output model file
        skip_optimization: Skip model optimization step if true. This may result in ONNX shape
            inference failure for some models.
        skip_onnx_shape: Skip ONNX shape inference. Symbolic shape inference is most effective
            with transformer based models. Skipping all shape inferences may
            reduce the effectiveness of quantization, as a tensor with unknown
            shape can not be quantized.
        skip_symbolic_shape: Skip symbolic shape inference. Symbolic shape inference is most
            effective with transformer based models. Skipping all shape
            inferences may reduce the effectiveness of quantization, as a tensor
            with unknown shape can not be quantized.
        auto_merge: For symbolic shape inference, automatically merge symbolic dims when
            conflict happens.
        int_max: For symbolic shape inference, specify the maximum value for integer to be
            treated as boundless for ops like slice
        guess_output_rank: Guess output rank to be the same as input 0 for unknown ops
        verbose: Logs detailed info of inference, 0: turn off, 1: warnings, 3: detailed
        save_as_external_data: Saving an ONNX model to external data
        all_tensors_to_one_file: Saving all the external data to one file
        external_data_location: The file location to save the external file
        external_data_size_threshold: The size threshold for external data
    '''
