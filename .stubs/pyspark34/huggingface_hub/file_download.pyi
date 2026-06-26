from . import __version__ as __version__
from .constants import DEFAULT_REVISION as DEFAULT_REVISION, ENDPOINT as ENDPOINT, HF_HUB_DISABLE_SYMLINKS_WARNING as HF_HUB_DISABLE_SYMLINKS_WARNING, HF_HUB_ENABLE_HF_TRANSFER as HF_HUB_ENABLE_HF_TRANSFER, HUGGINGFACE_CO_URL_TEMPLATE as HUGGINGFACE_CO_URL_TEMPLATE, HUGGINGFACE_HEADER_X_LINKED_ETAG as HUGGINGFACE_HEADER_X_LINKED_ETAG, HUGGINGFACE_HEADER_X_LINKED_SIZE as HUGGINGFACE_HEADER_X_LINKED_SIZE, HUGGINGFACE_HEADER_X_REPO_COMMIT as HUGGINGFACE_HEADER_X_REPO_COMMIT, HUGGINGFACE_HUB_CACHE as HUGGINGFACE_HUB_CACHE, REPO_ID_SEPARATOR as REPO_ID_SEPARATOR, REPO_TYPES as REPO_TYPES, REPO_TYPES_URL_PREFIXES as REPO_TYPES_URL_PREFIXES
from .utils import EntryNotFoundError as EntryNotFoundError, FileMetadataError as FileMetadataError, GatedRepoError as GatedRepoError, LocalEntryNotFoundError as LocalEntryNotFoundError, RepositoryNotFoundError as RepositoryNotFoundError, RevisionNotFoundError as RevisionNotFoundError, SoftTemporaryDirectory as SoftTemporaryDirectory, build_hf_headers as build_hf_headers, get_fastai_version as get_fastai_version, get_fastcore_version as get_fastcore_version, get_graphviz_version as get_graphviz_version, get_jinja_version as get_jinja_version, get_pydot_version as get_pydot_version, get_tf_version as get_tf_version, get_torch_version as get_torch_version, hf_raise_for_status as hf_raise_for_status, http_backoff as http_backoff, is_fastai_available as is_fastai_available, is_fastcore_available as is_fastcore_available, is_graphviz_available as is_graphviz_available, is_jinja_available as is_jinja_available, is_pydot_available as is_pydot_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging, tqdm as tqdm, validate_hf_hub_args as validate_hf_hub_args
from .utils._typing import HTTP_METHOD_T as HTTP_METHOD_T
from _typeshed import Incomplete
from dataclasses import dataclass
from huggingface_hub import constants as constants
from pathlib import Path
from typing import BinaryIO, Dict, Literal, Tuple

logger: Incomplete
HEADER_FILENAME_PATTERN: Incomplete

def are_symlinks_supported(cache_dir: str | Path | None = None) -> bool:
    """Return whether the symlinks are supported on the machine.

    Since symlinks support can change depending on the mounted disk, we need to check
    on the precise cache folder. By default, the default HF cache directory is checked.

    Args:
        cache_dir (`str`, `Path`, *optional*):
            Path to the folder where cached files are stored.

    Returns: [bool] Whether symlinks are supported in the directory.
    """

REGEX_COMMIT_HASH: Incomplete

@dataclass(frozen=True)
class HfFileMetadata:
    """Data structure containing information about a file versioned on the Hub.

    Returned by [`get_hf_file_metadata`] based on a URL.

    Args:
        commit_hash (`str`, *optional*):
            The commit_hash related to the file.
        etag (`str`, *optional*):
            Etag of the file on the server.
        location (`str`):
            Location where to download the file. Can be a Hub url or not (CDN).
        size (`size`):
            Size of the file. In case of an LFS file, contains the size of the actual
            LFS file, not the pointer.
    """
    commit_hash: str | None
    etag: str | None
    location: str
    size: int | None
    def __init__(self, commit_hash, etag, location, size) -> None: ...

def hf_hub_url(repo_id: str, filename: str, *, subfolder: str | None = None, repo_type: str | None = None, revision: str | None = None, endpoint: str | None = None) -> str:
    '''Construct the URL of a file from the given information.

    The resolved address can either be a huggingface.co-hosted url, or a link to
    Cloudfront (a Content Delivery Network, or CDN) for large files which are
    more than a few MBs.

    Args:
        repo_id (`str`):
            A namespace (user or an organization) name and a repo name separated
            by a `/`.
        filename (`str`):
            The name of the file in the repo.
        subfolder (`str`, *optional*):
            An optional value corresponding to a folder inside the repo.
        repo_type (`str`, *optional*):
            Set to `"dataset"` or `"space"` if downloading from a dataset or space,
            `None` or `"model"` if downloading from a model. Default is `None`.
        revision (`str`, *optional*):
            An optional Git revision id which can be a branch name, a tag, or a
            commit hash.
        endpoint (`str`, *optional*):
            Hugging Face Hub base url. Will default to https://huggingface.co/. Otherwise, one can set the `HF_ENDPOINT`
            environment variable.

    Example:

    ```python
    >>> from huggingface_hub import hf_hub_url

    >>> hf_hub_url(
    ...     repo_id="julien-c/EsperBERTo-small", filename="pytorch_model.bin"
    ... )
    \'https://huggingface.co/julien-c/EsperBERTo-small/resolve/main/pytorch_model.bin\'
    ```

    <Tip>

    Notes:

        Cloudfront is replicated over the globe so downloads are way faster for
        the end user (and it also lowers our bandwidth costs).

        Cloudfront aggressively caches files by default (default TTL is 24
        hours), however this is not an issue here because we implement a
        git-based versioning system on huggingface.co, which means that we store
        the files on S3/Cloudfront in a content-addressable way (i.e., the file
        name is its hash). Using content-addressable filenames means cache can\'t
        ever be stale.

        In terms of client-side caching from this library, we base our caching
        on the objects\' entity tag (`ETag`), which is an identifier of a
        specific version of a resource [1]_. An object\'s ETag is: its git-sha1
        if stored in git, or its sha256 if stored in git-lfs.

    </Tip>

    References:

    -  [1] https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag
    '''
def url_to_filename(url: str, etag: str | None = None) -> str:
    """Generate a local filename from a url.

    Convert `url` into a hashed filename in a reproducible way. If `etag` is
    specified, append its hash to the url's, delimited by a period. If the url
    ends with .h5 (Keras HDF5 weights) adds '.h5' to the name so that TF 2.0 can
    identify it as a HDF5 file (see
    https://github.com/tensorflow/tensorflow/blob/00fad90125b18b80fe054de1055770cfb8fe4ba3/tensorflow/python/keras/engine/network.py#L1380)

    Args:
        url (`str`):
            The address to the file.
        etag (`str`, *optional*):
            The ETag of the file.

    Returns:
        The generated filename.
    """
def filename_to_url(filename, cache_dir: str | None = None, legacy_cache_layout: bool = False) -> Tuple[str, str]:
    """
    Return the url and etag (which may be `None`) stored for `filename`. Raise
    `EnvironmentError` if `filename` or its stored metadata do not exist.

    Args:
        filename (`str`):
            The name of the file
        cache_dir (`str`, *optional*):
            The cache directory to use instead of the default one.
        legacy_cache_layout (`bool`, *optional*, defaults to `False`):
            If `True`, uses the legacy file cache layout i.e. just call `hf_hub_url`
            then `cached_download`. This is deprecated as the new cache layout is
            more powerful.
    """
def http_user_agent(*, library_name: str | None = None, library_version: str | None = None, user_agent: Dict | str | None = None) -> str:
    """Deprecated in favor of [`build_hf_headers`]."""

class OfflineModeIsEnabled(ConnectionError): ...

def http_get(url: str, temp_file: BinaryIO, *, proxies: Incomplete | None = None, resume_size: float = 0, headers: Dict[str, str] | None = None, timeout: float | None = 10.0, max_retries: int = 0, expected_size: int | None = None):
    """
    Download a remote file. Do not gobble up errors, and will return errors tailored to the Hugging Face Hub.
    """
def cached_download(url: str, *, library_name: str | None = None, library_version: str | None = None, cache_dir: str | Path | None = None, user_agent: Dict | str | None = None, force_download: bool = False, force_filename: str | None = None, proxies: Dict | None = None, etag_timeout: float = 10, resume_download: bool = False, token: bool | str | None = None, local_files_only: bool = False, legacy_cache_layout: bool = False) -> str:
    """
    Download from a given URL and cache it if it's not already present in the
    local cache.

    Given a URL, this function looks for the corresponding file in the local
    cache. If it's not there, download it. Then return the path to the cached
    file.

    Will raise errors tailored to the Hugging Face Hub.

    Args:
        url (`str`):
            The path to the file to be downloaded.
        library_name (`str`, *optional*):
            The name of the library to which the object corresponds.
        library_version (`str`, *optional*):
            The version of the library.
        cache_dir (`str`, `Path`, *optional*):
            Path to the folder where cached files are stored.
        user_agent (`dict`, `str`, *optional*):
            The user-agent info in the form of a dictionary or a string.
        force_download (`bool`, *optional*, defaults to `False`):
            Whether the file should be downloaded even if it already exists in
            the local cache.
        force_filename (`str`, *optional*):
            Use this name instead of a generated file name.
        proxies (`dict`, *optional*):
            Dictionary mapping protocol to the URL of the proxy passed to
            `requests.request`.
        etag_timeout (`float`, *optional* defaults to `10`):
            When fetching ETag, how many seconds to wait for the server to send
            data before giving up which is passed to `requests.request`.
        resume_download (`bool`, *optional*, defaults to `False`):
            If `True`, resume a previously interrupted download.
        token (`bool`, `str`, *optional*):
            A token to be used for the download.
                - If `True`, the token is read from the HuggingFace config
                  folder.
                - If a string, it's used as the authentication token.
        local_files_only (`bool`, *optional*, defaults to `False`):
            If `True`, avoid downloading the file and return the path to the
            local cached file if it exists.
        legacy_cache_layout (`bool`, *optional*, defaults to `False`):
            Set this parameter to `True` to mention that you'd like to continue
            the old cache layout. Putting this to `True` manually will not raise
            any warning when using `cached_download`. We recommend using
            `hf_hub_download` to take advantage of the new cache.

    Returns:
        Local path (string) of file or if networking is off, last version of
        file cached on disk.

    <Tip>

    Raises the following errors:

        - [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError)
          if `token=True` and the token cannot be found.
        - [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError)
          if ETag cannot be determined.
        - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
          if some parameter value is invalid
        - [`~utils.RepositoryNotFoundError`]
          If the repository to download from cannot be found. This may be because it doesn't exist,
          or because it is set to `private` and you do not have access.
        - [`~utils.RevisionNotFoundError`]
          If the revision to download from cannot be found.
        - [`~utils.EntryNotFoundError`]
          If the file to download cannot be found.
        - [`~utils.LocalEntryNotFoundError`]
          If network is disabled or unavailable and file is not found in cache.

    </Tip>
    """
def repo_folder_name(*, repo_id: str, repo_type: str) -> str:
    """Return a serialized version of a hf.co repo name and type, safe for disk storage
    as a single non-nested folder.

    Example: models--julien-c--EsperBERTo-small
    """
def hf_hub_download(repo_id: str, filename: str, *, subfolder: str | None = None, repo_type: str | None = None, revision: str | None = None, endpoint: str | None = None, library_name: str | None = None, library_version: str | None = None, cache_dir: str | Path | None = None, local_dir: str | Path | None = None, local_dir_use_symlinks: bool | Literal['auto'] = 'auto', user_agent: Dict | str | None = None, force_download: bool = False, force_filename: str | None = None, proxies: Dict | None = None, etag_timeout: float = 10, resume_download: bool = False, token: bool | str | None = None, local_files_only: bool = False, legacy_cache_layout: bool = False) -> str:
    '''Download a given file if it\'s not already present in the local cache.

    The new cache file layout looks like this:
    - The cache directory contains one subfolder per repo_id (namespaced by repo type)
    - inside each repo folder:
        - refs is a list of the latest known revision => commit_hash pairs
        - blobs contains the actual file blobs (identified by their git-sha or sha256, depending on
          whether they\'re LFS files or not)
        - snapshots contains one subfolder per commit, each "commit" contains the subset of the files
          that have been resolved at that particular commit. Each filename is a symlink to the blob
          at that particular commit.

    If `local_dir` is provided, the file structure from the repo will be replicated in this location. You can configure
    how you want to move those files:
      - If `local_dir_use_symlinks="auto"` (default), files are downloaded and stored in the cache directory as blob
        files. Small files (<5MB) are duplicated in `local_dir` while a symlink is created for bigger files. The goal
        is to be able to manually edit and save small files without corrupting the cache while saving disk space for
        binary files. The 5MB threshold can be configured with the `HF_HUB_LOCAL_DIR_AUTO_SYMLINK_THRESHOLD`
        environment variable.
      - If `local_dir_use_symlinks=True`, files are downloaded, stored in the cache directory and symlinked in `local_dir`.
        This is optimal in term of disk usage but files must not be manually edited.
      - If `local_dir_use_symlinks=False` and the blob files exist in the cache directory, they are duplicated in the
        local dir. This means disk usage is not optimized.
      - Finally, if `local_dir_use_symlinks=False` and the blob files do not exist in the cache directory, then the
        files are downloaded and directly placed under `local_dir`. This means if you need to download them again later,
        they will be re-downloaded entirely.

    ```
    [  96]  .
    └── [ 160]  models--julien-c--EsperBERTo-small
        ├── [ 160]  blobs
        │   ├── [321M]  403450e234d65943a7dcf7e05a771ce3c92faa84dd07db4ac20f592037a1e4bd
        │   ├── [ 398]  7cb18dc9bafbfcf74629a4b760af1b160957a83e
        │   └── [1.4K]  d7edf6bd2a681fb0175f7735299831ee1b22b812
        ├── [  96]  refs
        │   └── [  40]  main
        └── [ 128]  snapshots
            ├── [ 128]  2439f60ef33a0d46d85da5001d52aeda5b00ce9f
            │   ├── [  52]  README.md -> ../../blobs/d7edf6bd2a681fb0175f7735299831ee1b22b812
            │   └── [  76]  pytorch_model.bin -> ../../blobs/403450e234d65943a7dcf7e05a771ce3c92faa84dd07db4ac20f592037a1e4bd
            └── [ 128]  bbc77c8132af1cc5cf678da3f1ddf2de43606d48
                ├── [  52]  README.md -> ../../blobs/7cb18dc9bafbfcf74629a4b760af1b160957a83e
                └── [  76]  pytorch_model.bin -> ../../blobs/403450e234d65943a7dcf7e05a771ce3c92faa84dd07db4ac20f592037a1e4bd
    ```

    Args:
        repo_id (`str`):
            A user or an organization name and a repo name separated by a `/`.
        filename (`str`):
            The name of the file in the repo.
        subfolder (`str`, *optional*):
            An optional value corresponding to a folder inside the model repo.
        repo_type (`str`, *optional*):
            Set to `"dataset"` or `"space"` if downloading from a dataset or space,
            `None` or `"model"` if downloading from a model. Default is `None`.
        revision (`str`, *optional*):
            An optional Git revision id which can be a branch name, a tag, or a
            commit hash.
        endpoint (`str`, *optional*):
            Hugging Face Hub base url. Will default to https://huggingface.co/. Otherwise, one can set the `HF_ENDPOINT`
            environment variable.
        library_name (`str`, *optional*):
            The name of the library to which the object corresponds.
        library_version (`str`, *optional*):
            The version of the library.
        cache_dir (`str`, `Path`, *optional*):
            Path to the folder where cached files are stored.
        local_dir (`str` or `Path`, *optional*):
            If provided, the downloaded file will be placed under this directory, either as a symlink (default) or
            a regular file (see description for more details).
        local_dir_use_symlinks (`"auto"` or `bool`, defaults to `"auto"`):
            To be used with `local_dir`. If set to "auto", the cache directory will be used and the file will be either
            duplicated or symlinked to the local directory depending on its size. It set to `True`, a symlink will be
            created, no matter the file size. If set to `False`, the file will either be duplicated from cache (if
            already exists) or downloaded from the Hub and not cached. See description for more details.
        user_agent (`dict`, `str`, *optional*):
            The user-agent info in the form of a dictionary or a string.
        force_download (`bool`, *optional*, defaults to `False`):
            Whether the file should be downloaded even if it already exists in
            the local cache.
        proxies (`dict`, *optional*):
            Dictionary mapping protocol to the URL of the proxy passed to
            `requests.request`.
        etag_timeout (`float`, *optional*, defaults to `10`):
            When fetching ETag, how many seconds to wait for the server to send
            data before giving up which is passed to `requests.request`.
        resume_download (`bool`, *optional*, defaults to `False`):
            If `True`, resume a previously interrupted download.
        token (`str`, `bool`, *optional*):
            A token to be used for the download.
                - If `True`, the token is read from the HuggingFace config
                  folder.
                - If a string, it\'s used as the authentication token.
        local_files_only (`bool`, *optional*, defaults to `False`):
            If `True`, avoid downloading the file and return the path to the
            local cached file if it exists.
        legacy_cache_layout (`bool`, *optional*, defaults to `False`):
            If `True`, uses the legacy file cache layout i.e. just call [`hf_hub_url`]
            then `cached_download`. This is deprecated as the new cache layout is
            more powerful.

    Returns:
        Local path (string) of file or if networking is off, last version of
        file cached on disk.

    <Tip>

    Raises the following errors:

        - [`EnvironmentError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError)
          if `token=True` and the token cannot be found.
        - [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError)
          if ETag cannot be determined.
        - [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
          if some parameter value is invalid
        - [`~utils.RepositoryNotFoundError`]
          If the repository to download from cannot be found. This may be because it doesn\'t exist,
          or because it is set to `private` and you do not have access.
        - [`~utils.RevisionNotFoundError`]
          If the revision to download from cannot be found.
        - [`~utils.EntryNotFoundError`]
          If the file to download cannot be found.
        - [`~utils.LocalEntryNotFoundError`]
          If network is disabled or unavailable and file is not found in cache.

    </Tip>
    '''
def try_to_load_from_cache(repo_id: str, filename: str, cache_dir: str | Path | None = None, revision: str | None = None, repo_type: str | None = None) -> str | _CACHED_NO_EXIST_T | None:
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
        repo_type (`str`, *optional*):
            The type of the repository. Will default to `"model"`.

    Returns:
        `Optional[str]` or `_CACHED_NO_EXIST`:
            Will return `None` if the file was not cached. Otherwise:
            - The exact path to the cached file if it\'s found in the cache
            - A special value `_CACHED_NO_EXIST` if the file does not exist at the given commit hash and this fact was
              cached.

    Example:

    ```python
    from huggingface_hub import try_to_load_from_cache, _CACHED_NO_EXIST

    filepath = try_to_load_from_cache()
    if isinstance(filepath, str):
        # file exists and is cached
        ...
    elif filepath is _CACHED_NO_EXIST:
        # non-existence of file is cached
        ...
    else:
        # file is not cached
        ...
    ```
    '''
def get_hf_file_metadata(url: str, token: bool | str | None = None, proxies: Dict | None = None, timeout: float | None = 10.0) -> HfFileMetadata:
    """Fetch metadata of a file versioned on the Hub for a given url.

    Args:
        url (`str`):
            File url, for example returned by [`hf_hub_url`].
        token (`str` or `bool`, *optional*):
            A token to be used for the download.
                - If `True`, the token is read from the HuggingFace config
                  folder.
                - If `False` or `None`, no token is provided.
                - If a string, it's used as the authentication token.
        proxies (`dict`, *optional*):
            Dictionary mapping protocol to the URL of the proxy passed to
            `requests.request`.
        timeout (`float`, *optional*, defaults to 10):
            How many seconds to wait for the server to send metadata before giving up.

    Returns:
        A [`HfFileMetadata`] object containing metadata such as location, etag, size and
        commit_hash.
    """
