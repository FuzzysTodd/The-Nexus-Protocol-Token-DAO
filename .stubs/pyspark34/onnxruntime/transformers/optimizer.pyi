from _typeshed import Incomplete
from fusion_options import FusionOptions
from onnx import ModelProto as ModelProto
from typing import Dict, List

logger: Incomplete
MODEL_TYPES: Incomplete

def optimize_by_onnxruntime(onnx_model_path: str, use_gpu: bool = False, optimized_model_path: str | None = None, opt_level: int | None = 99, disabled_optimizers: List[str] = [], verbose: bool = False, save_as_external_data: bool = False, external_data_filename: str = '', external_data_file_threshold: int = 1024) -> str:
    """
    Use onnxruntime to optimize model.

    Args:
        onnx_model_path (str): the path of input onnx model.
        use_gpu (bool): whether the optimized model is targeted to run in GPU.
        optimized_model_path (str or None): the path of optimized model.
        opt_level (int): graph optimization level.
        disabled_optimizers (List[str]): a list of names of disabled optimizers
        save_as_external_data (bool): whether to save external data outside of ONNX model
        external_data_filename (str): name of external data file. If not provided, name is automatically created from ONNX model.
        external_data_file_threshold (int): threshold to decide whether to save tensor in ONNX model or in external data file
    Returns:
        optimized_model_path (str): the path of optimized model
    """
def optimize_by_fusion(model: ModelProto, model_type: str = 'bert', num_heads: int = 0, hidden_size: int = 0, optimization_options: FusionOptions | None = None):
    """Optimize Model by graph fusion logic.

    Note that ONNXRuntime graph optimizations (like constant folding) will not be applied. So it is better to enable
    constant folding during exporting ONNX model, or run optimize_by_onnxruntime on the model first like optimize_model.

    For BERT model, num_heads and hidden_size are optional. For other model types, you need to specify these parameters.

    Args:
        model (ModelProto): model object
        model_type (str, optional): model type - like bert, bert_tf, bert_keras or gpt2. Defaults to 'bert'.
        num_heads (int, optional): number of attention heads. Defaults to 0.
                                   0 allows detect the parameter from graph automatically.
        hidden_size (int, optional): hidden size. Defaults to 0.
                                     0 allows detect the parameter from graph automatically.
        optimization_options (FusionOptions, optional): optimization options that turn on/off some fusions.
                                                        Defaults to None.

     Returns:
        object of an optimizer class.
    """
def optimize_model(input: str, model_type: str = 'bert', num_heads: int = 0, hidden_size: int = 0, optimization_options: FusionOptions | None = None, opt_level: int | None = None, use_gpu: bool = False, only_onnxruntime: bool = False, verbose: bool = False):
    """Optimize Model by OnnxRuntime and/or python fusion logic.

    ONNX Runtime has graph optimizations (https://onnxruntime.ai/docs/performance/model-optimizations/graph-optimizations.html).
    However, the coverage is limited. We also have graph fusions that implemented in Python to improve the coverage.
    They can combined: ONNX Runtime will run first when opt_level > 0, then graph fusions in Python will be applied.

    To use ONNX Runtime only and no Python fusion logic, use only_onnxruntime flag and a positive opt_level like
        optimize_model(input, opt_level=1, use_gpu=False, only_onnxruntime=True)

    When opt_level is None, we will choose default optimization level according to model type.

    When opt_level is 0 and only_onnxruntime is False, only python fusion logic is used and onnxruntime is disabled.

    When opt_level > 1, use_gpu shall set properly
    since the optimized graph might contain operators for GPU or CPU only.

    If your model is intended for GPU inference only (especially float16 or mixed precision model), it is recommended to
    set use_gpu to be True, otherwise the model is not optimized for GPU inference.

    For BERT model, num_heads and hidden_size are optional. For other model types, you need specify these parameters.

    Args:
        input (str): input model path.
        model_type (str, optional): model type - like bert, bert_tf, bert_keras or gpt2. Defaults to 'bert'.
        num_heads (int, optional): number of attention heads. Defaults to 0.
            0 allows detect the parameter from graph automatically.
        hidden_size (int, optional): hidden size. Defaults to 0.
            0 allows detect the parameter from graph automatically.
        optimization_options (FusionOptions, optional): optimization options that turn on/off some fusions.
            Defaults to None.
        opt_level (int, optional): onnxruntime graph optimization level (0, 1, 2 or 99) or None. Defaults to None.
            When the value is None, default value (1 for bert and gpt2, 0 for other model types) will be used.
            When the level > 0, onnxruntime will be used to optimize model first.
        use_gpu (bool, optional): use gpu or not for onnxruntime. Defaults to False.
        only_onnxruntime (bool, optional): only use onnxruntime to optimize model, and no python fusion.
            Defaults to False.

     Returns:
        object of an optimizer class.
    """
def get_fusion_statistics(optimized_model_path: str) -> Dict[str, int]:
    """
    Get counter of fused operators in optimized model.

    Args:
        optimized_model_path (str): the path of onnx model.

    Returns:
        A dictionary with operator type as key, and count as value
    """
def main() -> None: ...
