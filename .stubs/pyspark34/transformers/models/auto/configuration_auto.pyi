from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...dynamic_module_utils import get_class_from_dynamic_module as get_class_from_dynamic_module
from ...utils import CONFIG_NAME as CONFIG_NAME, logging as logging
from _typeshed import Incomplete
from collections import OrderedDict

logger: Incomplete
CONFIG_MAPPING_NAMES: Incomplete
CONFIG_ARCHIVE_MAP_MAPPING_NAMES: Incomplete
MODEL_NAMES_MAPPING: Incomplete
SPECIAL_MODEL_TYPE_TO_MODULE_NAME: Incomplete

def model_type_to_module_name(key):
    """Converts a config key to the corresponding module."""
def config_class_to_model_type(config):
    """Converts a config class name to the corresponding model type"""

class _LazyConfigMapping(OrderedDict):
    """
    A dictionary that lazily load its values when they are requested.
    """
    def __init__(self, mapping) -> None: ...
    def __getitem__(self, key): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def __iter__(self): ...
    def __contains__(self, item) -> bool: ...
    def register(self, key, value) -> None:
        """
        Register a new configuration in this mapping.
        """

CONFIG_MAPPING: Incomplete

class _LazyLoadAllMappings(OrderedDict):
    """
    A mapping that will load all pairs of key values at the first access (either by indexing, requestions keys, values,
    etc.)

    Args:
        mapping: The mapping to load.
    """
    def __init__(self, mapping) -> None: ...
    def __getitem__(self, key): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def __iter__(self): ...
    def __contains__(self, item) -> bool: ...

ALL_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

def replace_list_option_in_docstrings(config_to_class: Incomplete | None = None, use_model_types: bool = True): ...

class AutoConfig:
    """
    This is a generic configuration class that will be instantiated as one of the configuration classes of the library
    when created with the [`~AutoConfig.from_pretrained`] class method.

    This class cannot be instantiated directly using `__init__()` (throws an error).
    """
    def __init__(self) -> None: ...
    @classmethod
    def for_model(cls, model_type: str, *args, **kwargs): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, **kwargs):
        '''
        Instantiate one of the configuration classes of the library from a pretrained model configuration.

        The configuration class to instantiate is selected based on the `model_type` property of the config object that
        is loaded, or when it\'s missing, by falling back to using pattern matching on `pretrained_model_name_or_path`:

        List options

        Args:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                Can be either:

                    - A string, the *model id* of a pretrained model configuration hosted inside a model repo on
                      huggingface.co. Valid model ids can be located at the root-level, like `bert-base-uncased`, or
                      namespaced under a user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing a configuration file saved using the
                      [`~PretrainedConfig.save_pretrained`] method, or the [`~PreTrainedModel.save_pretrained`] method,
                      e.g., `./my_model_directory/`.
                    - A path or url to a saved configuration JSON *file*, e.g.,
                      `./my_model_directory/configuration.json`.
            cache_dir (`str` or `os.PathLike`, *optional*):
                Path to a directory in which a downloaded pretrained model configuration should be cached if the
                standard cache should not be used.
            force_download (`bool`, *optional*, defaults to `False`):
                Whether or not to force the (re-)download the model weights and configuration files and override the
                cached versions if they exist.
            resume_download (`bool`, *optional*, defaults to `False`):
                Whether or not to delete incompletely received files. Will attempt to resume the download if such a
                file exists.
            proxies (`Dict[str, str]`, *optional*):
                A dictionary of proxy servers to use by protocol or endpoint, e.g., `{\'http\': \'foo.bar:3128\',
                \'http://hostname\': \'foo.bar:4012\'}`. The proxies are used on each request.
            revision (`str`, *optional*, defaults to `"main"`):
                The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
                git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
                identifier allowed by git.
            return_unused_kwargs (`bool`, *optional*, defaults to `False`):
                If `False`, then this function returns just the final configuration object.

                If `True`, then this functions returns a `Tuple(config, unused_kwargs)` where *unused_kwargs* is a
                dictionary consisting of the key/value pairs whose keys are not configuration attributes: i.e., the
                part of `kwargs` which has not been used to update `config` and is otherwise ignored.
            trust_remote_code (`bool`, *optional*, defaults to `False`):
                Whether or not to allow for custom models defined on the Hub in their own modeling files. This option
                should only be set to `True` for repositories you trust and in which you have read the code, as it will
                execute code present on the Hub on your local machine.
            kwargs(additional keyword arguments, *optional*):
                The values in kwargs of any keys which are configuration attributes will be used to override the loaded
                values. Behavior concerning key/value pairs whose keys are *not* configuration attributes is controlled
                by the `return_unused_kwargs` keyword parameter.

        Examples:

        ```python
        >>> from transformers import AutoConfig

        >>> # Download configuration from huggingface.co and cache.
        >>> config = AutoConfig.from_pretrained("bert-base-uncased")

        >>> # Download configuration from huggingface.co (user-uploaded) and cache.
        >>> config = AutoConfig.from_pretrained("dbmdz/bert-base-german-cased")

        >>> # If configuration file is in a directory (e.g., was saved using *save_pretrained(\'./test/saved_model/\')*).
        >>> config = AutoConfig.from_pretrained("./test/bert_saved_model/")

        >>> # Load a specific configuration file.
        >>> config = AutoConfig.from_pretrained("./test/bert_saved_model/my_configuration.json")

        >>> # Change some config attributes when loading a pretrained config.
        >>> config = AutoConfig.from_pretrained("bert-base-uncased", output_attentions=True, foo=False)
        >>> config.output_attentions
        True

        >>> config, unused_kwargs = AutoConfig.from_pretrained(
        ...     "bert-base-uncased", output_attentions=True, foo=False, return_unused_kwargs=True
        ... )
        >>> config.output_attentions
        True

        >>> unused_kwargs
        {\'foo\': False}
        ```'''
    @staticmethod
    def register(model_type, config) -> None:
        '''
        Register a new configuration for this class.

        Args:
            model_type (`str`): The model type like "bert" or "gpt".
            config ([`PretrainedConfig`]): The config to register.
        '''
