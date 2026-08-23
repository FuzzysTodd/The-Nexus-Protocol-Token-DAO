import abc
import dataclasses
from ..configuration_utils import PretrainedConfig as PretrainedConfig
from ..feature_extraction_utils import FeatureExtractionMixin as FeatureExtractionMixin
from ..image_processing_utils import ImageProcessingMixin as ImageProcessingMixin
from ..tokenization_utils_base import PreTrainedTokenizerBase as PreTrainedTokenizerBase
from ..utils import TensorType as TensorType, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging
from .utils import ParameterFormat as ParameterFormat, compute_effective_axis_dimension as compute_effective_axis_dimension, compute_serialized_parameters_size as compute_serialized_parameters_size
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Tuple, Union

logger: Incomplete
DEFAULT_ONNX_OPSET: int
EXTERNAL_DATA_FORMAT_SIZE_LIMIT: Incomplete

@dataclasses.dataclass
class PatchingSpec:
    """
    Data class that holds patching specifications.

    Args:
        o: Module / object where the op to patch is located
        name: Name of the op to monkey patch
        custom_op: Custom op that patches the original op
        orig_op: Original op that is being patched
        op_wrapper: Wrapper (optional) that wraps both the original and custom ops.
            It is useful for ops that are class or static methods for instance.
    """
    o: Any
    name: str
    custom_op: Callable
    orig_op: Optional[Callable] = ...
    op_wrapper: Optional[Callable] = ...
    def __init__(self, o, name, custom_op, orig_op, op_wrapper) -> None: ...

class OnnxConfig(ABC, metaclass=abc.ABCMeta):
    """
    Base class for ONNX exportable model describing metadata on how to export the model through the ONNX format.
    """
    default_fixed_batch: int
    default_fixed_sequence: int
    default_fixed_num_choices: int
    torch_onnx_minimum_version: Incomplete
    task: Incomplete
    def __init__(self, config: PretrainedConfig, task: str = 'default', patching_specs: List[PatchingSpec] = None) -> None: ...
    @classmethod
    def from_model_config(cls, config: PretrainedConfig, task: str = 'default') -> OnnxConfig:
        """
        Instantiate a OnnxConfig for a specific model

        Args:
            config: The model's configuration to use when exporting to ONNX

        Returns:
            OnnxConfig for this model
        """
    @property
    @abstractmethod
    def inputs(self) -> Mapping[str, Mapping[int, str]]:
        """
        Mapping containing the axis definition of the input tensors to provide to the model

        Returns:
            For each input: its name associated to the axes symbolic name and the axis position within the tensor
        """
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]:
        """
        Mapping containing the axis definition of the output tensors to provide to the model

        Returns:
            For each output: its name associated to the axes symbolic name and the axis position within the tensor
        """
    @property
    def values_override(self) -> Optional[Mapping[str, Any]]:
        """
        Dictionary of keys to override in the model's config before exporting

        Returns:
            Dictionary with the keys (and their corresponding values) to override
        """
    @property
    def default_batch_size(self) -> int:
        """
        The default batch size to use if no other indication

        Returns:
            Integer > 0
        """
    @property
    def default_sequence_length(self) -> int:
        """
        The default sequence length to use if no other indication

        Returns:
            Integer > 0
        """
    @property
    def default_num_choices(self) -> int:
        """
        The default number of choices to use if no other indication

        Returns:
            Integer > 0
        """
    @property
    def default_onnx_opset(self) -> int:
        """
        Which onnx opset to use when exporting the model

        Returns:
            Integer ONNX Opset version
        """
    @property
    def atol_for_validation(self) -> float:
        """
        What absolute tolerance value to use during model conversion validation.

        Returns:
            Float absolute tolerance value.
        """
    @property
    def is_torch_support_available(self) -> bool:
        """
        The minimum PyTorch version required to export the model.

        Returns:
            `bool`: Whether the installed version of PyTorch is compatible with the model.
        """
    @staticmethod
    def use_external_data_format(num_parameters: int) -> bool:
        """
        Flag indicating if the model requires using external data format

        Args:
            num_parameters: Number of parameter on the model

        Returns:
            True if model.num_parameters() * size_of(float32) >= 2Gb False otherwise
        """
    def generate_dummy_inputs(self, preprocessor: Union['PreTrainedTokenizerBase', 'FeatureExtractionMixin', 'ImageProcessingMixin'], batch_size: int = -1, seq_length: int = -1, num_choices: int = -1, is_pair: bool = False, framework: Optional[TensorType] = None, num_channels: int = 3, image_width: int = 40, image_height: int = 40, sampling_rate: int = 22050, time_duration: float = 5.0, frequency: int = 220, tokenizer: PreTrainedTokenizerBase = None) -> Mapping[str, Any]:
        """
        Generate inputs to provide to the ONNX exporter for the specific framework

        Args:
            preprocessor: ([`PreTrainedTokenizerBase`], [`FeatureExtractionMixin`], or [`ImageProcessingMixin`]):
                The preprocessor associated with this model configuration.
            batch_size (`int`, *optional*, defaults to -1):
                The batch size to export the model for (-1 means dynamic axis).
            num_choices (`int`, *optional*, defaults to -1):
                The number of candidate answers provided for multiple choice task (-1 means dynamic axis).
            seq_length (`int`, *optional*, defaults to -1):
                The sequence length to export the model for (-1 means dynamic axis).
            is_pair (`bool`, *optional*, defaults to `False`):
                Indicate if the input is a pair (sentence 1, sentence 2)
            framework (`TensorType`, *optional*, defaults to `None`):
                The framework (PyTorch or TensorFlow) that the tokenizer will generate tensors for.
            num_channels (`int`, *optional*, defaults to 3):
                The number of channels of the generated images.
            image_width (`int`, *optional*, defaults to 40):
                The width of the generated images.
            image_height (`int`, *optional*, defaults to 40):
                The height of the generated images.
            sampling_rate (`int`, *optional* defaults to 22050)
                The sampling rate for audio data generation.
            time_duration (`float`, *optional* defaults to 5.0)
                Total seconds of sampling for audio data generation.
            frequency (`int`, *optional* defaults to 220)
                The desired natural frequency of generated audio.

        Returns:
            Mapping[str, Tensor] holding the kwargs to provide to the model's forward function
        """
    def generate_dummy_inputs_onnxruntime(self, reference_model_inputs: Mapping[str, Any]) -> Mapping[str, Any]:
        """
        Generate inputs for ONNX Runtime using the reference model inputs. Override this to run inference with seq2seq
        models which have the encoder and decoder exported as separate ONNX files.

        Args:
            reference_model_inputs ([`Mapping[str, Tensor]`):
                Reference inputs for the model.

        Returns:
            `Mapping[str, Tensor]`: The mapping holding the kwargs to provide to the model's forward function
        """
    def patch_ops(self) -> None: ...
    def restore_ops(self) -> None: ...
    @classmethod
    def flatten_output_collection_property(cls, name: str, field: Iterable[Any]) -> Dict[str, Any]:
        """
        Flatten any potential nested structure expanding the name of the field with the index of the element within the
        structure.

        Args:
            name: The name of the nested structure
            field: The structure to, potentially, be flattened

        Returns:
            (Dict[str, Any]): Outputs with flattened structure and key mapping this new structure.

        """

class OnnxConfigWithPast(OnnxConfig, ABC, metaclass=abc.ABCMeta):
    use_past: Incomplete
    def __init__(self, config: PretrainedConfig, task: str = 'default', patching_specs: List[PatchingSpec] = None, use_past: bool = False) -> None: ...
    @classmethod
    def with_past(cls, config: PretrainedConfig, task: str = 'default') -> OnnxConfigWithPast:
        """
        Instantiate a OnnxConfig with `use_past` attribute set to True

        Args:
            config: The underlying model's config to use when exporting to ONNX

        Returns:
            OnnxConfig with `.use_past = True`
        """
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def values_override(self) -> Optional[Mapping[str, Any]]: ...
    @property
    def num_layers(self) -> int:
        """
        The number of layers attribute retrieved from the model config. Override this for model configs where the
        number of layers attribute is not called `num_layers`.
        """
    @property
    def num_attention_heads(self) -> int:
        """
        The number of attention heads attribute retrieved from the model config. Override this for model configs where
        the number of attention heads attribute is not called `num_attention_heads`.
        """
    def generate_dummy_inputs(self, tokenizer: PreTrainedTokenizerBase, batch_size: int = -1, seq_length: int = -1, is_pair: bool = False, framework: Optional[TensorType] = None) -> Mapping[str, Any]: ...
    def fill_with_past_key_values_(self, inputs_or_outputs: Mapping[str, Mapping[int, str]], direction: str, inverted_values_shape: bool = False):
        '''
        Fill the input_or_outputs mapping with past_key_values dynamic axes considering.

        Args:
            inputs_or_outputs: The mapping to fill.
            direction: either "inputs" or "outputs", it specifies whether input_or_outputs is the input mapping or the
                output mapping, this is important for axes naming.
            inverted_values_shape:
                If `True`, store values on dynamic axis 1, else on axis 2.

        '''
    def flatten_output_collection_property(self, name: str, field: Iterable[Any]) -> Dict[str, Any]: ...

class OnnxSeq2SeqConfigWithPast(OnnxConfigWithPast, metaclass=abc.ABCMeta):
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def num_layers(self) -> Tuple[int]: ...
    @property
    def num_attention_heads(self) -> Tuple[int]: ...
    def generate_dummy_inputs(self, tokenizer: PreTrainedTokenizerBase, batch_size: int = -1, seq_length: int = -1, is_pair: bool = False, framework: Optional[TensorType] = None) -> Mapping[str, Any]: ...
    def fill_with_past_key_values_(self, inputs_or_outputs: Mapping[str, Mapping[int, str]], direction: str): ...
