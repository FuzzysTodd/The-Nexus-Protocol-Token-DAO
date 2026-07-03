import numpy
from .calibrate import CalibraterBase as CalibraterBase, CalibrationDataReader as CalibrationDataReader
from .onnx_model import ONNXModel as ONNXModel
from .quant_utils import DEQUANT_OP_NAME as DEQUANT_OP_NAME, DEQUANT_OUTPUT_SUFFIX as DEQUANT_OUTPUT_SUFFIX, QUANT_INPUT_SUFFIX as QUANT_INPUT_SUFFIX, TENSOR_NAME_QUANT_SUFFIX as TENSOR_NAME_QUANT_SUFFIX, find_by_name as find_by_name, load_model_with_shape_infer as load_model_with_shape_infer
from _typeshed import Incomplete
from pathlib import Path
from typing import Callable, Dict, List, Sequence

def modify_model_output_intermediate_tensors(input_model_path: str | Path, output_model_path: str | Path, op_types_for_saving: Sequence[str] | None = None, save_as_external_data: bool = False) -> None:
    """Augment a given ONNX model to save node input/output tensors.

    Add all input/output tensors of operator nodes to model outputs
    so that their values can be retrieved for debugging purposes.

    Args:
        input_model: the path to load the model.
        op_types_for_saving: Operator types for which the
                input/output should be saved. By default, saving all the
                float32/float16 tensors.

    Returns:
        The augmented ONNX model
    """
def collect_activations(augmented_model: str, input_reader: CalibrationDataReader, session_options: Incomplete | None = None, execution_providers: Sequence[str] | None = None) -> Dict[str, List[numpy.ndarray]]:
    """Run augmented model and collect activations tensors.

    Args:
        augmented_model: Path to augmented model created by modify_model_output_intermediate_tensors ()
        input_reader: Logic for reading input for the model, augmented model have the same
            input with the original model.
        session_options: Optional OnnxRuntime session options for controlling model run.
            By default graph optimization is turned off
        execution_providers: Collection of execution providers for running the model.
            Only CPU EP is used by default.

    Returns:
        A dictionary where the key is tensor name and values are list of tensors from each batch
    """
def create_activation_matching(qdq_activations: Dict[str, Sequence[numpy.ndarray]], float_activations: Dict[str, Sequence[numpy.ndarray]] | None = None) -> Dict[str, Dict[str, Sequence[numpy.ndarray]]]:
    """Comparing activation values to help debugging accuracy loss due to quantization.

    This functions takes saved activations from the QDQ model and (optionally) the
    float point model, and provides a data structure for comparing:
        * from the qdq model, activation values before and after QDQ operation
        * across both models, activations from the orignal model vs the corresponding
          activations in the QDQ model

    Arg:
        qdq_activations: Output of `collect_activations`. This must be from a quantized
            model with QDQ format.
        float_activations: Output of `collect_activations`. This must be from the float
            point model.

    Returns:
        Dict for comparing pre and post quantized activation tensors. E.g.
        ```
        qdq_cmp = cmp_qdq_input_output(qdq_activations)
        print(qdq_cmp['activation1']['pre_qdq'][0])
        print(qdq_cmp['activation1'][`post_qdq'][0])


        qdq_cmp = cmp_qdq_input_output(qdq_activations, float_activations)
        print(qdq_cmp['activation1']['float'][0])
        print(qdq_cmp['activation1']['pre_qdq'][0])
        print(qdq_cmp['activation1'][`post_qdq'][0])
        ```
    """
def create_weight_matching(float_model_path: str, qdq_model_path: str) -> Dict[str, Dict[str, numpy.ndarray]]:
    """Comparing weight values to help debugging accuracy loss due to quantization.

    This functions takes the float model and the qdq model, and provides a data structure for comparing
    their corresponding weights to locate quantization errors

    Arg:
        float_model_path: Path points to the float point model.
        qdq_model_path: Path points to the qdq model.

    Returns:
        Dict for comparing weight tensors. E.g.
        ```
        qdq_weight_cmp = create_weight_matching(float_model, qdq_model)
        print(qdq_weight_cmp['activation1']['float'])
        print(qdq_weight_cmp['activation1']['dequantized'])
        ```
    """
def compute_signal_to_quantization_noice_ratio(x: Sequence[numpy.ndarray] | numpy.ndarray, y: Sequence[numpy.ndarray] | numpy.ndarray) -> float: ...
def compute_weight_error(weights_match: Dict[str, Dict[str, numpy.ndarray]], err_func: Callable[[numpy.ndarray, numpy.ndarray], float] = ...) -> Dict[str, float]: ...
def compute_activation_error(activations_match: Dict[str, Dict[str, Sequence[numpy.ndarray]]], err_func: Callable[[Sequence[numpy.ndarray], Sequence[numpy.ndarray]], float] = ...) -> Dict[str, Dict[str, float]]: ...
