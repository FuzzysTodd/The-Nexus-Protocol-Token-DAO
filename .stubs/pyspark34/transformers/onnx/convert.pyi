from ..feature_extraction_utils import FeatureExtractionMixin as FeatureExtractionMixin
from ..modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel
from ..modeling_utils import PreTrainedModel as PreTrainedModel
from ..processing_utils import ProcessorMixin as ProcessorMixin
from ..pytorch_utils import is_torch_less_than_1_11 as is_torch_less_than_1_11
from ..tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ..tokenization_utils_base import PreTrainedTokenizerBase as PreTrainedTokenizerBase
from ..utils import TensorType as TensorType, is_tf_available as is_tf_available, is_torch_available as is_torch_available, is_torch_onnx_dict_inputs_support_available as is_torch_onnx_dict_inputs_support_available, logging as logging
from .config import OnnxConfig as OnnxConfig
from _typeshed import Incomplete
from packaging.version import Version as Version
from pathlib import Path
from typing import Iterable, List, Tuple, Union

logger: Incomplete
ORT_QUANTIZE_MINIMUM_VERSION: Incomplete

def check_onnxruntime_requirements(minimum_version: Version):
    """
    Check onnxruntime is installed and if the installed version match is recent enough

    Raises:
        ImportError: If onnxruntime is not installed or too old version is found
    """
def export_pytorch(preprocessor: Union['PreTrainedTokenizer', 'FeatureExtractionMixin', 'ProcessorMixin'], model: PreTrainedModel, config: OnnxConfig, opset: int, output: Path, tokenizer: PreTrainedTokenizer = None, device: str = 'cpu') -> Tuple[List[str], List[str]]:
    """
    Export a PyTorch model to an ONNX Intermediate Representation (IR)

    Args:
        preprocessor: ([`PreTrainedTokenizer`], [`FeatureExtractionMixin`] or [`ProcessorMixin`]):
            The preprocessor used for encoding the data.
        model ([`PreTrainedModel`]):
            The model to export.
        config ([`~onnx.config.OnnxConfig`]):
            The ONNX configuration associated with the exported model.
        opset (`int`):
            The version of the ONNX operator set to use.
        output (`Path`):
            Directory to store the exported ONNX model.
        device (`str`, *optional*, defaults to `cpu`):
            The device on which the ONNX model will be exported. Either `cpu` or `cuda`.

    Returns:
        `Tuple[List[str], List[str]]`: A tuple with an ordered list of the model's inputs, and the named inputs from
        the ONNX configuration.
    """
def export_tensorflow(preprocessor: Union['PreTrainedTokenizer', 'FeatureExtractionMixin'], model: TFPreTrainedModel, config: OnnxConfig, opset: int, output: Path, tokenizer: PreTrainedTokenizer = None) -> Tuple[List[str], List[str]]:
    """
    Export a TensorFlow model to an ONNX Intermediate Representation (IR)

    Args:
        preprocessor: ([`PreTrainedTokenizer`] or [`FeatureExtractionMixin`]):
            The preprocessor used for encoding the data.
        model ([`TFPreTrainedModel`]):
            The model to export.
        config ([`~onnx.config.OnnxConfig`]):
            The ONNX configuration associated with the exported model.
        opset (`int`):
            The version of the ONNX operator set to use.
        output (`Path`):
            Directory to store the exported ONNX model.

    Returns:
        `Tuple[List[str], List[str]]`: A tuple with an ordered list of the model's inputs, and the named inputs from
        the ONNX configuration.
    """
def export(preprocessor: Union['PreTrainedTokenizer', 'FeatureExtractionMixin', 'ProcessorMixin'], model: Union['PreTrainedModel', 'TFPreTrainedModel'], config: OnnxConfig, opset: int, output: Path, tokenizer: PreTrainedTokenizer = None, device: str = 'cpu') -> Tuple[List[str], List[str]]:
    """
    Export a Pytorch or TensorFlow model to an ONNX Intermediate Representation (IR)

    Args:
        preprocessor: ([`PreTrainedTokenizer`], [`FeatureExtractionMixin`] or [`ProcessorMixin`]):
            The preprocessor used for encoding the data.
        model ([`PreTrainedModel`] or [`TFPreTrainedModel`]):
            The model to export.
        config ([`~onnx.config.OnnxConfig`]):
            The ONNX configuration associated with the exported model.
        opset (`int`):
            The version of the ONNX operator set to use.
        output (`Path`):
            Directory to store the exported ONNX model.
        device (`str`, *optional*, defaults to `cpu`):
            The device on which the ONNX model will be exported. Either `cpu` or `cuda`. Only PyTorch is supported for
            export on CUDA devices.

    Returns:
        `Tuple[List[str], List[str]]`: A tuple with an ordered list of the model's inputs, and the named inputs from
        the ONNX configuration.
    """
def validate_model_outputs(config: OnnxConfig, preprocessor: Union['PreTrainedTokenizer', 'FeatureExtractionMixin', 'ProcessorMixin'], reference_model: Union['PreTrainedModel', 'TFPreTrainedModel'], onnx_model: Path, onnx_named_outputs: List[str], atol: float, tokenizer: PreTrainedTokenizer = None): ...
def ensure_model_and_config_inputs_match(model: Union['PreTrainedModel', 'TFPreTrainedModel'], model_inputs: Iterable[str]) -> Tuple[bool, List[str]]:
    """

    :param model_inputs: :param config_inputs: :return:
    """
