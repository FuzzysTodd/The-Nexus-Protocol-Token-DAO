from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...dynamic_module_utils import get_class_from_dynamic_module as get_class_from_dynamic_module
from ...utils import copy_func as copy_func, logging as logging
from .configuration_auto import AutoConfig as AutoConfig, model_type_to_module_name as model_type_to_module_name, replace_list_option_in_docstrings as replace_list_option_in_docstrings
from _typeshed import Incomplete
from collections import OrderedDict

logger: Incomplete
CLASS_DOCSTRING: str
FROM_CONFIG_DOCSTRING: str
FROM_PRETRAINED_TORCH_DOCSTRING: str
FROM_PRETRAINED_TF_DOCSTRING: str
FROM_PRETRAINED_FLAX_DOCSTRING: str

class _BaseAutoModelClass:
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def from_config(cls, config, **kwargs): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs): ...
    @classmethod
    def register(cls, config_class, model_class) -> None:
        """
        Register a new model for this class.

        Args:
            config_class ([`PretrainedConfig`]):
                The configuration corresponding to the model to register.
            model_class ([`PreTrainedModel`]):
                The model to register.
        """

def insert_head_doc(docstring, head_doc: str = ''): ...
def auto_class_update(cls, checkpoint_for_example: str = 'bert-base-cased', head_doc: str = ''): ...
def get_values(model_mapping): ...
def getattribute_from_module(module, attr): ...

class _LazyAutoMapping(OrderedDict):
    '''
    " A mapping config to object (model or tokenizer for instance) that will load keys and values when it is accessed.

    Args:
        - config_mapping: The map model type to config class
        - model_mapping: The map model type to model (or tokenizer) class
    '''
    def __init__(self, config_mapping, model_mapping) -> None: ...
    def __getitem__(self, key): ...
    def keys(self): ...
    def get(self, key, default): ...
    def __bool__(self) -> bool: ...
    def values(self): ...
    def items(self): ...
    def __iter__(self): ...
    def __contains__(self, item) -> bool: ...
    def register(self, key, value) -> None:
        """
        Register a new model in this mapping.
        """
