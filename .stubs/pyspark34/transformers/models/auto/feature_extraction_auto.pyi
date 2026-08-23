import os
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...dynamic_module_utils import get_class_from_dynamic_module as get_class_from_dynamic_module
from ...feature_extraction_utils import FeatureExtractionMixin as FeatureExtractionMixin
from ...utils import CONFIG_NAME as CONFIG_NAME, FEATURE_EXTRACTOR_NAME as FEATURE_EXTRACTOR_NAME, get_file_from_repo as get_file_from_repo, logging as logging
from .configuration_auto import AutoConfig as AutoConfig, CONFIG_MAPPING_NAMES as CONFIG_MAPPING_NAMES, model_type_to_module_name as model_type_to_module_name, replace_list_option_in_docstrings as replace_list_option_in_docstrings
from _typeshed import Incomplete
from typing import Dict, Optional, Union

logger: Incomplete
FEATURE_EXTRACTOR_MAPPING_NAMES: Incomplete
FEATURE_EXTRACTOR_MAPPING: Incomplete

def feature_extractor_class_from_name(class_name: str): ...
def get_feature_extractor_config(pretrained_model_name_or_path: Union[str, os.PathLike], cache_dir: Optional[Union[str, os.PathLike]] = None, force_download: bool = False, resume_download: bool = False, proxies: Optional[Dict[str, str]] = None, use_auth_token: Optional[Union[bool, str]] = None, revision: Optional[str] = None, local_files_only: bool = False, **kwargs):
    '''
    Loads the tokenizer configuration from a pretrained model tokenizer configuration.

    Args:
        pretrained_model_name_or_path (`str` or `os.PathLike`):
            This can be either:

            - a string, the *model id* of a pretrained model configuration hosted inside a model repo on
              huggingface.co. Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced
              under a user or organization name, like `dbmdz/bert-base-german-cased`.
            - a path to a *directory* containing a configuration file saved using the
              [`~PreTrainedTokenizer.save_pretrained`] method, e.g., `./my_model_directory/`.

        cache_dir (`str` or `os.PathLike`, *optional*):
            Path to a directory in which a downloaded pretrained model configuration should be cached if the standard
            cache should not be used.
        force_download (`bool`, *optional*, defaults to `False`):
            Whether or not to force to (re-)download the configuration files and override the cached versions if they
            exist.
        resume_download (`bool`, *optional*, defaults to `False`):
            Whether or not to delete incompletely received file. Attempts to resume the download if such a file exists.
        proxies (`Dict[str, str]`, *optional*):
            A dictionary of proxy servers to use by protocol or endpoint, e.g., `{\'http\': \'foo.bar:3128\',
            \'http://hostname\': \'foo.bar:4012\'}.` The proxies are used on each request.
        use_auth_token (`str` or *bool*, *optional*):
            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
            when running `huggingface-cli login` (stored in `~/.huggingface`).
        revision (`str`, *optional*, defaults to `"main"`):
            The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
            git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
            identifier allowed by git.
        local_files_only (`bool`, *optional*, defaults to `False`):
            If `True`, will only try to load the tokenizer configuration from local files.

    <Tip>

    Passing `use_auth_token=True` is required when you want to use a private model.

    </Tip>

    Returns:
        `Dict`: The configuration of the tokenizer.

    Examples:

    ```python
    # Download configuration from huggingface.co and cache.
    tokenizer_config = get_tokenizer_config("bert-base-uncased")
    # This model does not have a tokenizer config so the result will be an empty dict.
    tokenizer_config = get_tokenizer_config("xlm-roberta-base")

    # Save a pretrained tokenizer locally and you can reload its config
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    tokenizer.save_pretrained("tokenizer-test")
    tokenizer_config = get_tokenizer_config("tokenizer-test")
    ```'''

class AutoFeatureExtractor:
    """
    This is a generic feature extractor class that will be instantiated as one of the feature extractor classes of the
    library when created with the [`AutoFeatureExtractor.from_pretrained`] class method.

    This class cannot be instantiated directly using `__init__()` (throws an error).
    """
    def __init__(self) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, **kwargs):
        '''
        Instantiate one of the feature extractor classes of the library from a pretrained model vocabulary.

        The feature extractor class to instantiate is selected based on the `model_type` property of the config object
        (either passed as an argument or loaded from `pretrained_model_name_or_path` if possible), or when it\'s
        missing, by falling back to using pattern matching on `pretrained_model_name_or_path`:

        List options

        Params:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                This can be either:

                - a string, the *model id* of a pretrained feature_extractor hosted inside a model repo on
                  huggingface.co. Valid model ids can be located at the root-level, like `bert-base-uncased`, or
                  namespaced under a user or organization name, like `dbmdz/bert-base-german-cased`.
                - a path to a *directory* containing a feature extractor file saved using the
                  [`~feature_extraction_utils.FeatureExtractionMixin.save_pretrained`] method, e.g.,
                  `./my_model_directory/`.
                - a path or url to a saved feature extractor JSON *file*, e.g.,
                  `./my_model_directory/preprocessor_config.json`.
            cache_dir (`str` or `os.PathLike`, *optional*):
                Path to a directory in which a downloaded pretrained model feature extractor should be cached if the
                standard cache should not be used.
            force_download (`bool`, *optional*, defaults to `False`):
                Whether or not to force to (re-)download the feature extractor files and override the cached versions
                if they exist.
            resume_download (`bool`, *optional*, defaults to `False`):
                Whether or not to delete incompletely received file. Attempts to resume the download if such a file
                exists.
            proxies (`Dict[str, str]`, *optional*):
                A dictionary of proxy servers to use by protocol or endpoint, e.g., `{\'http\': \'foo.bar:3128\',
                \'http://hostname\': \'foo.bar:4012\'}.` The proxies are used on each request.
            use_auth_token (`str` or *bool*, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
                when running `huggingface-cli login` (stored in `~/.huggingface`).
            revision (`str`, *optional*, defaults to `"main"`):
                The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
                git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
                identifier allowed by git.
            return_unused_kwargs (`bool`, *optional*, defaults to `False`):
                If `False`, then this function returns just the final feature extractor object. If `True`, then this
                functions returns a `Tuple(feature_extractor, unused_kwargs)` where *unused_kwargs* is a dictionary
                consisting of the key/value pairs whose keys are not feature extractor attributes: i.e., the part of
                `kwargs` which has not been used to update `feature_extractor` and is otherwise ignored.
            trust_remote_code (`bool`, *optional*, defaults to `False`):
                Whether or not to allow for custom models defined on the Hub in their own modeling files. This option
                should only be set to `True` for repositories you trust and in which you have read the code, as it will
                execute code present on the Hub on your local machine.
            kwargs (`Dict[str, Any]`, *optional*):
                The values in kwargs of any keys which are feature extractor attributes will be used to override the
                loaded values. Behavior concerning key/value pairs whose keys are *not* feature extractor attributes is
                controlled by the `return_unused_kwargs` keyword parameter.

        <Tip>

        Passing `use_auth_token=True` is required when you want to use a private model.

        </Tip>

        Examples:

        ```python
        >>> from transformers import AutoFeatureExtractor

        >>> # Download feature extractor from huggingface.co and cache.
        >>> feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-base-960h")

        >>> # If feature extractor files are in a directory (e.g. feature extractor was saved using *save_pretrained(\'./test/saved_model/\')*)
        >>> feature_extractor = AutoFeatureExtractor.from_pretrained("./test/saved_model/")
        ```'''
    @staticmethod
    def register(config_class, feature_extractor_class) -> None:
        """
        Register a new feature extractor for this class.

        Args:
            config_class ([`PretrainedConfig`]):
                The configuration corresponding to the model to register.
            feature_extractor_class ([`FeatureExtractorMixin`]): The feature extractor to register.
        """
