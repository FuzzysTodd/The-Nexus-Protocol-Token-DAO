import fsspec
import io
import requests
from . import logging as logging
from .. import __version__ as __version__, config as config
from ..download.download_config import DownloadConfig as DownloadConfig
from .extract import ExtractManager as ExtractManager
from .filelock import FileLock as FileLock
from _typeshed import Incomplete
from pathlib import Path
from typing import TypeVar

logger: Incomplete
INCOMPLETE_SUFFIX: str
T = TypeVar('T', str, Path)

def init_hf_modules(hf_modules_cache: Path | str | None = None) -> str:
    """
    Add hf_modules_cache to the python path.
    By default hf_modules_cache='~/.cache/huggingface/modules'.
    It can also be set with the environment variable HF_MODULES_CACHE.
    This is used to add modules such as `datasets_modules`
    """
def is_remote_url(url_or_filename: str) -> bool: ...
def is_local_path(url_or_filename: str) -> bool: ...
def is_relative_path(url_or_filename: str) -> bool: ...
def relative_to_absolute_path(path: T) -> T:
    """Convert relative path to absolute path."""
def hf_bucket_url(identifier: str, filename: str, use_cdn: bool = False, dataset: bool = True) -> str: ...
def head_hf_s3(identifier: str, filename: str, use_cdn: bool = False, dataset: bool = True, max_retries: int = 0) -> requests.Response | Exception: ...
def hf_github_url(path: str, name: str, dataset: bool = True, revision: str | None = None) -> str: ...
def url_or_path_join(base_name: str, *pathnames: str) -> str: ...
def url_or_path_parent(url_or_path: str) -> str: ...
def hash_url_to_filename(url, etag: Incomplete | None = None):
    """
    Convert `url` into a hashed filename in a repeatable way.
    If `etag` is specified, append its hash to the url's, delimited
    by a period.
    If the url ends with .h5 (Keras HDF5 weights) adds '.h5' to the name
    so that TF 2.0 can identify it as a HDF5 file
    (see https://github.com/tensorflow/tensorflow/blob/00fad90125b18b80fe054de1055770cfb8fe4ba3/tensorflow/python/keras/engine/network.py#L1380)
    """
def cached_path(url_or_filename, download_config: Incomplete | None = None, **download_kwargs) -> str:
    """
    Given something that might be a URL (or might be a local path),
    determine which. If it's a URL, download the file and cache it, and
    return the path to the cached file. If it's already a local path,
    make sure the file exists and then return the path.

    Return:
        Local path (string)

    Raises:
        FileNotFoundError: in case of non-recoverable file
            (non-existent or no cache on disk)
        ConnectionError: in case of unreachable url
            and no cache on disk
        ValueError: if it couldn't parse the url or filename correctly
        requests.exceptions.ConnectionError: in case of internet connection issue
    """
def get_datasets_user_agent(user_agent: str | dict | None = None) -> str: ...
def get_authentication_headers_for_url(url: str, token: str | bool | None = None, use_auth_token: str | bool | None = 'deprecated') -> dict:
    """Handle the HF authentication"""

class OfflineModeIsEnabled(ConnectionError): ...

def fsspec_head(url, storage_options: Incomplete | None = None): ...

class TqdmCallback(fsspec.callbacks.TqdmCallback):
    def __init__(self, tqdm_kwargs: Incomplete | None = None, *args, **kwargs) -> None: ...

def fsspec_get(url, temp_file, storage_options: Incomplete | None = None, desc: Incomplete | None = None) -> None: ...
def ftp_head(url, timeout: float = 10.0): ...
def ftp_get(url, temp_file, timeout: float = 10.0) -> None: ...
def http_get(url, temp_file, proxies: Incomplete | None = None, resume_size: int = 0, headers: Incomplete | None = None, cookies: Incomplete | None = None, timeout: float = 100.0, max_retries: int = 0, desc: Incomplete | None = None) -> None: ...
def http_head(url, proxies: Incomplete | None = None, headers: Incomplete | None = None, cookies: Incomplete | None = None, allow_redirects: bool = True, timeout: float = 10.0, max_retries: int = 0) -> requests.Response: ...
def request_etag(url: str, token: str | bool | None = None, use_auth_token: str | bool | None = 'deprecated') -> str | None: ...
def get_from_cache(url, cache_dir: Incomplete | None = None, force_download: bool = False, proxies: Incomplete | None = None, etag_timeout: int = 100, resume_download: bool = False, user_agent: Incomplete | None = None, local_files_only: bool = False, use_etag: bool = True, max_retries: int = 0, token: Incomplete | None = None, use_auth_token: str = 'deprecated', ignore_url_params: bool = False, storage_options: Incomplete | None = None, download_desc: Incomplete | None = None) -> str:
    """
    Given a URL, look for the corresponding file in the local cache.
    If it's not there, download it. Then return the path to the cached file.

    Return:
        Local path (string)

    Raises:
        FileNotFoundError: in case of non-recoverable file
            (non-existent or no cache on disk)
        ConnectionError: in case of unreachable url
            and no cache on disk
    """
def add_start_docstrings(*docstr): ...
def add_end_docstrings(*docstr): ...
def estimate_dataset_size(paths): ...
def readline(f: io.RawIOBase): ...
