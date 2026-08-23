import os
from . import __version__ as __version__, logging as logging
from .generic import working_or_temp_dir as working_or_temp_dir
from .import_utils import ENV_VARS_TRUE_VALUES as ENV_VARS_TRUE_VALUES, is_tf_available as is_tf_available, is_torch_available as is_torch_available, is_training_run_on_sagemaker as is_training_run_on_sagemaker
from _typeshed import Incomplete
from pathlib import Path
from transformers.utils.logging import tqdm as tqdm
from typing import Dict, List, Optional, Tuple, Union

logger: Incomplete

def is_offline_mode(): ...

torch_cache_home: Incomplete
old_default_cache_path: Incomplete
hf_cache_home: Incomplete
default_cache_path: Incomplete
PYTORCH_PRETRAINED_BERT_CACHE: Incomplete
PYTORCH_TRANSFORMERS_CACHE: Incomplete
HUGGINGFACE_HUB_CACHE: Incomplete
TRANSFORMERS_CACHE: Incomplete
HF_MODULES_CACHE: Incomplete
TRANSFORMERS_DYNAMIC_MODULE_NAME: str
SESSION_ID: Incomplete
DISABLE_TELEMETRY: Incomplete
S3_BUCKET_PREFIX: str
CLOUDFRONT_DISTRIB_PREFIX: str
HUGGINGFACE_CO_RESOLVE_ENDPOINT: Incomplete
HUGGINGFACE_CO_PREFIX: Incomplete
HUGGINGFACE_CO_EXAMPLES_TELEMETRY: Incomplete

def is_remote_url(url_or_filename): ...
def get_cached_models(cache_dir: Union[str, Path] = None) -> List[Tuple]:
    """
    Returns a list of tuples representing model binaries that are cached locally. Each tuple has shape `(model_url,
    etag, size_MB)`. Filenames in `cache_dir` are use to get the metadata for each model, only urls ending with *.bin*
    are added.

    Args:
        cache_dir (`Union[str, Path]`, *optional*):
            The cache directory to search for models within. Will default to the transformers cache if unset.

    Returns:
        List[Tuple]: List of tuples each with shape `(model_url, etag, size_MB)`
    """
def define_sagemaker_information(): ...
def http_user_agent(user_agent: Union[Dict, str, None] = None) -> str:
    """
    Formats a user-agent string with basic info about a request.
    """
def extract_commit_hash(resolved_file: Optional[str], commit_hash: Optional[str]):
    """
    Extracts the commit hash from a resolved filename toward a cache file.
    """
def try_to_load_from_cache(repo_id: str, filename: str, cache_dir: Union[str, Path, None] = None, revision: Optional[str] = None) -> Optional[str]:
    '''
    Explores the cache to return the latest cached file for a given revision if found.

    This function will not raise any exception if the file in not cached.

    Args:
        cache_dir (`str` or `os.PathLike`):
            The folder where the cached files lie.
        repo_id (`str`):
            The ID of the repo on huggingface.co.
        filename (`str`):
            The filename to look for inside `repo_id`.
        revision (`str`, *optional*):
            The specific model version to use. Will default to `"main"` if it\'s not provided and no `commit_hash` is
            provided either.

    Returns:
        `Optional[str]` or `_CACHED_NO_EXIST`:
            Will return `None` if the file was not cached. Otherwise:
            - The exact path to the cached file if it\'s found in the cache
            - A special value `_CACHED_NO_EXIST` if the file does not exist at the given commit hash and this fact was
              cached.
    '''
def cached_file(path_or_repo_id: Union[str, os.PathLike], filename: str, cache_dir: Optional[Union[str, os.PathLike]] = None, force_download: bool = False, resume_download: bool = False, proxies: Optional[Dict[str, str]] = None, use_auth_token: Optional[Union[bool, str]] = None, revision: Optional[str] = None, local_files_only: bool = False, subfolder: str = '', user_agent: Optional[Union[str, Dict[str, str]]] = None, _raise_exceptions_for_missing_entries: bool = True, _raise_exceptions_for_connection_errors: bool = True, _commit_hash: Optional[str] = None):
    '''
    Tries to locate a file in a local folder and repo, downloads and cache it if necessary.

    Args:
        path_or_repo_id (`str` or `os.PathLike`):
            This can be either:

            - a string, the *model id* of a model repo on huggingface.co.
            - a path to a *directory* potentially containing the file.
        filename (`str`):
            The name of the file to locate in `path_or_repo`.
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
        subfolder (`str`, *optional*, defaults to `""`):
            In case the relevant files are located inside a subfolder of the model repo on huggingface.co, you can
            specify the folder name here.

    <Tip>

    Passing `use_auth_token=True` is required when you want to use a private model.

    </Tip>

    Returns:
        `Optional[str]`: Returns the resolved file (to the cache folder if downloaded from a repo).

    Examples:

    ```python
    # Download a model weight from the Hub and cache it.
    model_weights_file = cached_file("bert-base-uncased", "pytorch_model.bin")
    ```'''
def get_file_from_repo(path_or_repo: Union[str, os.PathLike], filename: str, cache_dir: Optional[Union[str, os.PathLike]] = None, force_download: bool = False, resume_download: bool = False, proxies: Optional[Dict[str, str]] = None, use_auth_token: Optional[Union[bool, str]] = None, revision: Optional[str] = None, local_files_only: bool = False, subfolder: str = ''):
    '''
    Tries to locate a file in a local folder and repo, downloads and cache it if necessary.

    Args:
        path_or_repo (`str` or `os.PathLike`):
            This can be either:

            - a string, the *model id* of a model repo on huggingface.co.
            - a path to a *directory* potentially containing the file.
        filename (`str`):
            The name of the file to locate in `path_or_repo`.
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
        subfolder (`str`, *optional*, defaults to `""`):
            In case the relevant files are located inside a subfolder of the model repo on huggingface.co, you can
            specify the folder name here.

    <Tip>

    Passing `use_auth_token=True` is required when you want to use a private model.

    </Tip>

    Returns:
        `Optional[str]`: Returns the resolved file (to the cache folder if downloaded from a repo) or `None` if the
        file does not exist.

    Examples:

    ```python
    # Download a tokenizer configuration from huggingface.co and cache.
    tokenizer_config = get_file_from_repo("bert-base-uncased", "tokenizer_config.json")
    # This model does not have a tokenizer config so the result will be None.
    tokenizer_config = get_file_from_repo("xlm-roberta-base", "tokenizer_config.json")
    ```'''
def download_url(url, proxies: Incomplete | None = None):
    """
    Downloads a given url in a temporary file. This function is not safe to use in multiple processes. Its only use is
    for deprecated behavior allowing to download config/models with a single url instead of using the Hub.

    Args:
        url (`str`): The url of the file to download.
        proxies (`Dict[str, str]`, *optional*):
            A dictionary of proxy servers to use by protocol or endpoint, e.g., `{'http': 'foo.bar:3128',
            'http://hostname': 'foo.bar:4012'}.` The proxies are used on each request.

    Returns:
        `str`: The location of the temporary file where the url was downloaded.
    """
def has_file(path_or_repo: Union[str, os.PathLike], filename: str, revision: Optional[str] = None, proxies: Optional[Dict[str, str]] = None, use_auth_token: Optional[Union[bool, str]] = None):
    """
    Checks if a repo contains a given file wihtout downloading it. Works for remote repos and local folders.

    <Tip warning={false}>

    This function will raise an error if the repository `path_or_repo` is not valid or if `revision` does not exist for
    this repo, but will return False for regular connection errors.

    </Tip>
    """

class PushToHubMixin:
    """
    A Mixin containing the functionality to push a model or tokenizer to the hub.
    """
    def push_to_hub(self, repo_id: str, use_temp_dir: Optional[bool] = None, commit_message: Optional[str] = None, private: Optional[bool] = None, use_auth_token: Optional[Union[bool, str]] = None, max_shard_size: Optional[Union[int, str]] = '10GB', create_pr: bool = False, **deprecated_kwargs) -> str:
        '''
        Upload the {object_files} to the 🤗 Model Hub while synchronizing a local clone of the repo in
        `repo_path_or_name`.

        Parameters:
            repo_id (`str`):
                The name of the repository you want to push your {object} to. It should contain your organization name
                when pushing to a given organization.
            use_temp_dir (`bool`, *optional*):
                Whether or not to use a temporary directory to store the files saved before they are pushed to the Hub.
                Will default to `True` if there is no directory named like `repo_id`, `False` otherwise.
            commit_message (`str`, *optional*):
                Message to commit while pushing. Will default to `"Upload {object}"`.
            private (`bool`, *optional*):
                Whether or not the repository created should be private.
            use_auth_token (`bool` or `str`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
                when running `huggingface-cli login` (stored in `~/.huggingface`). Will default to `True` if `repo_url`
                is not specified.
            max_shard_size (`int` or `str`, *optional*, defaults to `"10GB"`):
                Only applicable for models. The maximum size for a checkpoint before being sharded. Checkpoints shard
                will then be each of size lower than this size. If expressed as a string, needs to be digits followed
                by a unit (like `"5MB"`).
            create_pr (`bool`, *optional*, defaults to `False`):
                Whether or not to create a PR with the uploaded files or directly commit.

        Examples:

        ```python
        from transformers import {object_class}

        {object} = {object_class}.from_pretrained("bert-base-cased")

        # Push the {object} to your namespace with the name "my-finetuned-bert".
        {object}.push_to_hub("my-finetuned-bert")

        # Push the {object} to an organization with the name "my-finetuned-bert".
        {object}.push_to_hub("huggingface/my-finetuned-bert")
        ```
        '''

def get_full_repo_name(model_id: str, organization: Optional[str] = None, token: Optional[str] = None): ...
def send_example_telemetry(example_name, *example_args, framework: str = 'pytorch') -> None:
    '''
    Sends telemetry that helps tracking the examples use.

    Args:
        example_name (`str`): The name of the example.
        *example_args (dataclasses or `argparse.ArgumentParser`): The arguments to the script. This function will only
            try to extract the model and dataset name from those. Nothing else is tracked.
        framework (`str`, *optional*, defaults to `"pytorch"`): The framework for the example.
    '''
def convert_file_size_to_int(size: Union[int, str]):
    '''
    Converts a size expressed as a string with digits an unit (like `"5MB"`) to an integer (in bytes).

    Args:
        size (`int` or `str`): The size to convert. Will be directly returned if an `int`.

    Example:
    ```py
    >>> convert_file_size_to_int("1MiB")
    1048576
    ```
    '''
def get_checkpoint_shard_files(pretrained_model_name_or_path, index_filename, cache_dir: Incomplete | None = None, force_download: bool = False, proxies: Incomplete | None = None, resume_download: bool = False, local_files_only: bool = False, use_auth_token: Incomplete | None = None, user_agent: Incomplete | None = None, revision: Incomplete | None = None, subfolder: str = '', _commit_hash: Incomplete | None = None):
    """
    For a given model:

    - download and cache all the shards of a sharded checkpoint if `pretrained_model_name_or_path` is a model ID on the
      Hub
    - returns the list of paths to all the shards, as well as some metadata.

    For the description of each arg, see [`PreTrainedModel.from_pretrained`]. `index_filename` is the full path to the
    index (downloaded and cached if `pretrained_model_name_or_path` is a model ID on the Hub).
    """
def get_all_cached_files(cache_dir: Incomplete | None = None):
    """
    Returns a list for all files cached with appropriate metadata.
    """
def extract_info_from_url(url):
    """
    Extract repo_name, revision and filename from an url.
    """
def clean_files_for(file) -> None:
    """
    Remove, if they exist, file, file.json and file.lock
    """
def move_to_new_cache(file, repo, filename, revision, etag, commit_hash) -> None:
    """
    Move file to repo following the new huggingface hub cache organization.
    """
def move_cache(cache_dir: Incomplete | None = None, new_cache_dir: Incomplete | None = None, token: Incomplete | None = None) -> None: ...

cache_version_file: Incomplete
cache_version: int
cache_is_not_empty: Incomplete
trace: Incomplete
