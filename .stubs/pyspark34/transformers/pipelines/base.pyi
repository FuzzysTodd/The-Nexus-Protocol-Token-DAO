import abc
import torch
from ..dynamic_module_utils import custom_object_save as custom_object_save
from ..feature_extraction_utils import PreTrainedFeatureExtractor as PreTrainedFeatureExtractor
from ..modelcard import ModelCard as ModelCard
from ..modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel
from ..modeling_utils import PreTrainedModel as PreTrainedModel
from ..models.auto.configuration_auto import AutoConfig as AutoConfig
from ..models.auto.modeling_auto import AutoModel as AutoModel
from ..models.auto.modeling_tf_auto import TFAutoModel as TFAutoModel
from ..tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ..utils import ModelOutput as ModelOutput, add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from .pt_utils import KeyDataset as KeyDataset
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator
from transformers.pipelines.pt_utils import PipelineChunkIterator as PipelineChunkIterator, PipelineDataset as PipelineDataset, PipelineIterator as PipelineIterator, PipelinePackIterator as PipelinePackIterator
from typing import Any, Dict, List, Optional, Tuple, Union

GenericTensor: Incomplete
logger: Incomplete

def no_collate_fn(items): ...
def pad_collate_fn(tokenizer, feature_extractor): ...
def infer_framework_load_model(model, config: AutoConfig, model_classes: Optional[Dict[str, Tuple[type]]] = None, task: Optional[str] = None, framework: Optional[str] = None, **model_kwargs):
    """
    Select framework (TensorFlow or PyTorch) to use from the `model` passed. Returns a tuple (framework, model).

    If `model` is instantiated, this function will just infer the framework from the model class. Otherwise `model` is
    actually a checkpoint name and this method will try to instantiate it using `model_classes`. Since we don't want to
    instantiate the model twice, this model is returned for use by the pipeline.

    If both frameworks are installed and available for `model`, PyTorch is selected.

    Args:
        model (`str`, [`PreTrainedModel`] or [`TFPreTrainedModel`]):
            The model to infer the framework from. If `str`, a checkpoint name. The model to infer the framewrok from.
        config ([`AutoConfig`]):
            The config associated with the model to help using the correct class
        model_classes (dictionary `str` to `type`, *optional*):
            A mapping framework to class.
        task (`str`):
            The task defining which pipeline will be returned.
        model_kwargs:
            Additional dictionary of keyword arguments passed along to the model's `from_pretrained(...,
            **model_kwargs)` function.

    Returns:
        `Tuple`: A tuple framework, model.
    """
def infer_framework_from_model(model, model_classes: Optional[Dict[str, Tuple[type]]] = None, task: Optional[str] = None, framework: Optional[str] = None, **model_kwargs):
    """
    Select framework (TensorFlow or PyTorch) to use from the `model` passed. Returns a tuple (framework, model).

    If `model` is instantiated, this function will just infer the framework from the model class. Otherwise `model` is
    actually a checkpoint name and this method will try to instantiate it using `model_classes`. Since we don't want to
    instantiate the model twice, this model is returned for use by the pipeline.

    If both frameworks are installed and available for `model`, PyTorch is selected.

    Args:
        model (`str`, [`PreTrainedModel`] or [`TFPreTrainedModel`]):
            The model to infer the framework from. If `str`, a checkpoint name. The model to infer the framewrok from.
        model_classes (dictionary `str` to `type`, *optional*):
            A mapping framework to class.
        task (`str`):
            The task defining which pipeline will be returned.
        model_kwargs:
            Additional dictionary of keyword arguments passed along to the model's `from_pretrained(...,
            **model_kwargs)` function.

    Returns:
        `Tuple`: A tuple framework, model.
    """
def get_framework(model, revision: Optional[str] = None):
    """
    Select framework (TensorFlow or PyTorch) to use.

    Args:
        model (`str`, [`PreTrainedModel`] or [`TFPreTrainedModel`]):
            If both frameworks are installed, picks the one corresponding to the model passed (either a model class or
            the model name). If no specific model is provided, defaults to using PyTorch.
    """
def get_default_model_and_revision(targeted_task: Dict, framework: Optional[str], task_options: Optional[Any]) -> Union[str, Tuple[str, str]]:
    '''
    Select a default model to use for a given task. Defaults to pytorch if ambiguous.

    Args:
        targeted_task (`Dict` ):
           Dictionary representing the given task, that should contain default models

        framework (`str`, None)
           "pt", "tf" or None, representing a specific framework if it was specified, or None if we don\'t know yet.

        task_options (`Any`, None)
           Any further value required by the task to get fully specified, for instance (SRC, TGT) languages for
           translation task.

    Returns

        `str` The model string representing the default model for this pipeline
    '''

class PipelineException(Exception):
    """
    Raised by a [`Pipeline`] when handling __call__.

    Args:
        task (`str`): The task of the pipeline.
        model (`str`): The model used by the pipeline.
        reason (`str`): The error message to display.
    """
    task: Incomplete
    model: Incomplete
    def __init__(self, task: str, model: str, reason: str) -> None: ...

class ArgumentHandler(ABC, metaclass=abc.ABCMeta):
    """
    Base interface for handling arguments for each [`~pipelines.Pipeline`].
    """
    @abstractmethod
    def __call__(self, *args, **kwargs): ...

class PipelineDataFormat(metaclass=abc.ABCMeta):
    """
    Base class for all the pipeline supported data format both for reading and writing. Supported data formats
    currently includes:

    - JSON
    - CSV
    - stdin/stdout (pipe)

    `PipelineDataFormat` also includes some utilities to work with multi-columns like mapping from datasets columns to
    pipelines keyword arguments through the `dataset_kwarg_1=dataset_column_1` format.

    Args:
        output_path (`str`, *optional*): Where to save the outgoing data.
        input_path (`str`, *optional*): Where to look for the input data.
        column (`str`, *optional*): The column to read.
        overwrite (`bool`, *optional*, defaults to `False`):
            Whether or not to overwrite the `output_path`.
    """
    SUPPORTED_FORMATS: Incomplete
    output_path: Incomplete
    input_path: Incomplete
    column: Incomplete
    is_multi_columns: Incomplete
    def __init__(self, output_path: Optional[str], input_path: Optional[str], column: Optional[str], overwrite: bool = False) -> None: ...
    @abstractmethod
    def __iter__(self): ...
    @abstractmethod
    def save(self, data: Union[dict, List[dict]]):
        """
        Save the provided data object with the representation for the current [`~pipelines.PipelineDataFormat`].

        Args:
            data (`dict` or list of `dict`): The data to store.
        """
    def save_binary(self, data: Union[dict, List[dict]]) -> str:
        """
        Save the provided data object as a pickle-formatted binary data on the disk.

        Args:
            data (`dict` or list of `dict`): The data to store.

        Returns:
            `str`: Path where the data has been saved.
        """
    @staticmethod
    def from_str(format: str, output_path: Optional[str], input_path: Optional[str], column: Optional[str], overwrite: bool = False) -> PipelineDataFormat:
        '''
        Creates an instance of the right subclass of [`~pipelines.PipelineDataFormat`] depending on `format`.

        Args:
            format: (`str`):
                The format of the desired pipeline. Acceptable values are `"json"`, `"csv"` or `"pipe"`.
            output_path (`str`, *optional*):
                Where to save the outgoing data.
            input_path (`str`, *optional*):
                Where to look for the input data.
            column (`str`, *optional*):
                The column to read.
            overwrite (`bool`, *optional*, defaults to `False`):
                Whether or not to overwrite the `output_path`.

        Returns:
            [`~pipelines.PipelineDataFormat`]: The proper data format.
        '''

class CsvPipelineDataFormat(PipelineDataFormat):
    """
    Support for pipelines using CSV data format.

    Args:
        output_path (`str`, *optional*): Where to save the outgoing data.
        input_path (`str`, *optional*): Where to look for the input data.
        column (`str`, *optional*): The column to read.
        overwrite (`bool`, *optional*, defaults to `False`):
            Whether or not to overwrite the `output_path`.
    """
    def __init__(self, output_path: Optional[str], input_path: Optional[str], column: Optional[str], overwrite: bool = False) -> None: ...
    def __iter__(self): ...
    def save(self, data: List[dict]):
        """
        Save the provided data object with the representation for the current [`~pipelines.PipelineDataFormat`].

        Args:
            data (`List[dict]`): The data to store.
        """

class JsonPipelineDataFormat(PipelineDataFormat):
    """
    Support for pipelines using JSON file format.

    Args:
        output_path (`str`, *optional*): Where to save the outgoing data.
        input_path (`str`, *optional*): Where to look for the input data.
        column (`str`, *optional*): The column to read.
        overwrite (`bool`, *optional*, defaults to `False`):
            Whether or not to overwrite the `output_path`.
    """
    def __init__(self, output_path: Optional[str], input_path: Optional[str], column: Optional[str], overwrite: bool = False) -> None: ...
    def __iter__(self): ...
    def save(self, data: dict):
        """
        Save the provided data object in a json file.

        Args:
            data (`dict`): The data to store.
        """

class PipedPipelineDataFormat(PipelineDataFormat):
    """
    Read data from piped input to the python process. For multi columns data, columns should separated by \t

    If columns are provided, then the output will be a dictionary with {column_x: value_x}

    Args:
        output_path (`str`, *optional*): Where to save the outgoing data.
        input_path (`str`, *optional*): Where to look for the input data.
        column (`str`, *optional*): The column to read.
        overwrite (`bool`, *optional*, defaults to `False`):
            Whether or not to overwrite the `output_path`.
    """
    def __iter__(self): ...
    def save(self, data: dict):
        """
        Print the data.

        Args:
            data (`dict`): The data to store.
        """
    def save_binary(self, data: Union[dict, List[dict]]) -> str: ...

class _ScikitCompat(ABC, metaclass=abc.ABCMeta):
    """
    Interface layer for the Scikit and Keras compatibility.
    """
    @abstractmethod
    def transform(self, X): ...
    @abstractmethod
    def predict(self, X): ...

PIPELINE_INIT_ARGS: str

class Pipeline(_ScikitCompat, metaclass=abc.ABCMeta):
    """
    The Pipeline class is the class from which all pipelines inherit. Refer to this class for methods shared across
    different pipelines.

    Base class implementing pipelined operations. Pipeline workflow is defined as a sequence of the following
    operations:

        Input -> Tokenization -> Model Inference -> Post-Processing (task dependent) -> Output

    Pipeline supports running on CPU or GPU through the device argument (see below).

    Some pipeline, like for instance [`FeatureExtractionPipeline`] (`'feature-extraction'`) output large tensor object
    as nested-lists. In order to avoid dumping such large structure as textual data we provide the `binary_output`
    constructor argument. If set to `True`, the output will be stored in the pickle format.
    """
    default_input_names: Incomplete
    task: Incomplete
    model: Incomplete
    tokenizer: Incomplete
    feature_extractor: Incomplete
    modelcard: Incomplete
    framework: Incomplete
    device: Incomplete
    torch_dtype: Incomplete
    binary_output: Incomplete
    call_count: int
    def __init__(self, model: Union['PreTrainedModel', 'TFPreTrainedModel'], tokenizer: Optional[PreTrainedTokenizer] = None, feature_extractor: Optional[PreTrainedFeatureExtractor] = None, modelcard: Optional[ModelCard] = None, framework: Optional[str] = None, task: str = '', args_parser: ArgumentHandler = None, device: Union[int, str, 'torch.device'] = -1, torch_dtype: Optional[Union[str, 'torch.dtype']] = None, binary_output: bool = False, **kwargs) -> None: ...
    def save_pretrained(self, save_directory: str):
        """
        Save the pipeline's model and tokenizer.

        Args:
            save_directory (`str`):
                A path to the directory where to saved. It will be created if it doesn't exist.
        """
    def transform(self, X):
        """
        Scikit / Keras interface to transformers' pipelines. This method will forward to __call__().
        """
    def predict(self, X):
        """
        Scikit / Keras interface to transformers' pipelines. This method will forward to __call__().
        """
    def device_placement(self) -> Generator[None, None, None]:
        """
        Context Manager allowing tensor allocation on the user-specified device in framework agnostic way.

        Returns:
            Context manager

        Examples:

        ```python
        # Explicitly ask for tensor allocation on CUDA device :0
        pipe = pipeline(..., device=0)
        with pipe.device_placement():
            # Every framework specific tensor allocation will be done on the request device
            output = pipe(...)
        ```"""
    def ensure_tensor_on_device(self, **inputs):
        """
        Ensure PyTorch tensors are on the specified device.

        Args:
            inputs (keyword arguments that should be `torch.Tensor`, the rest is ignored):
                The tensors to place on `self.device`.
            Recursive on lists **only**.

        Return:
            `Dict[str, torch.Tensor]`: The same as `inputs` but on the proper device.
        """
    def check_model_type(self, supported_models: Union[List[str], dict]):
        """
        Check if the model class is in supported by the pipeline.

        Args:
            supported_models (`List[str]` or `dict`):
                The list of models supported by the pipeline, or a dictionary with model class values.
        """
    @abstractmethod
    def preprocess(self, input_: Any, **preprocess_parameters: Dict) -> Dict[str, GenericTensor]:
        """
        Preprocess will take the `input_` of a specific pipeline and return a dictionary of everything necessary for
        `_forward` to run properly. It should contain at least one tensor, but might have arbitrary other items.
        """
    @abstractmethod
    def postprocess(self, model_outputs: ModelOutput, **postprocess_parameters: Dict) -> Any:
        """
        Postprocess will receive the raw outputs of the `_forward` method, generally tensors, and reformat them into
        something more friendly. Generally it will output a list or a dict or results (containing just strings and
        numbers).
        """
    def get_inference_context(self): ...
    def forward(self, model_inputs, **forward_params): ...
    def get_iterator(self, inputs, num_workers: int, batch_size: int, preprocess_params, forward_params, postprocess_params): ...
    def __call__(self, inputs, *args, num_workers: Incomplete | None = None, batch_size: Incomplete | None = None, **kwargs): ...
    def run_multi(self, inputs, preprocess_params, forward_params, postprocess_params): ...
    def run_single(self, inputs, preprocess_params, forward_params, postprocess_params): ...
    def iterate(self, inputs, preprocess_params, forward_params, postprocess_params) -> Generator[Incomplete, None, None]: ...

class ChunkPipeline(Pipeline, metaclass=abc.ABCMeta):
    def run_single(self, inputs, preprocess_params, forward_params, postprocess_params): ...
    def get_iterator(self, inputs, num_workers: int, batch_size: int, preprocess_params, forward_params, postprocess_params): ...

class PipelineRegistry:
    supported_tasks: Incomplete
    task_aliases: Incomplete
    def __init__(self, supported_tasks: Dict[str, Any], task_aliases: Dict[str, str]) -> None: ...
    def get_supported_tasks(self) -> List[str]: ...
    def check_task(self, task: str) -> Tuple[str, Dict, Any]: ...
    def register_pipeline(self, task: str, pipeline_class: type, pt_model: Optional[Union[type, Tuple[type]]] = None, tf_model: Optional[Union[type, Tuple[type]]] = None, default: Optional[Dict] = None, type: Optional[str] = None) -> None: ...
    def to_dict(self): ...
