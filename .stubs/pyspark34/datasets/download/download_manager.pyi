import enum
import io
from .. import config as config
from ..utils.deprecation_utils import DeprecatedEnum as DeprecatedEnum, deprecated as deprecated
from ..utils.file_utils import cached_path as cached_path, get_from_cache as get_from_cache, hash_url_to_filename as hash_url_to_filename, is_relative_path as is_relative_path, url_or_path_join as url_or_path_join
from ..utils.info_utils import get_size_checksum_dict as get_size_checksum_dict
from ..utils.logging import get_logger as get_logger, is_progress_bar_enabled as is_progress_bar_enabled, tqdm as tqdm
from ..utils.py_utils import NestedDataStructure as NestedDataStructure, map_nested as map_nested, size_str as size_str
from .download_config import DownloadConfig as DownloadConfig
from _typeshed import Incomplete
from typing import Callable, Iterable, List

logger: Incomplete
BASE_KNOWN_EXTENSIONS: Incomplete
MAGIC_NUMBER_TO_COMPRESSION_PROTOCOL: Incomplete
MAGIC_NUMBER_TO_UNSUPPORTED_COMPRESSION_PROTOCOL: Incomplete
MAGIC_NUMBER_MAX_LENGTH: Incomplete

class DownloadMode(enum.Enum):
    """`Enum` for how to treat pre-existing downloads and data.

    The default mode is `REUSE_DATASET_IF_EXISTS`, which will reuse both
    raw downloads and the prepared dataset if they exist.

    The generations modes:

    |                                     | Downloads | Dataset |
    |-------------------------------------|-----------|---------|
    | `REUSE_DATASET_IF_EXISTS` (default) | Reuse     | Reuse   |
    | `REUSE_CACHE_IF_EXISTS`             | Reuse     | Fresh   |
    | `FORCE_REDOWNLOAD`                  | Fresh     | Fresh   |

    """
    REUSE_DATASET_IF_EXISTS: str
    REUSE_CACHE_IF_EXISTS: str
    FORCE_REDOWNLOAD: str

class GenerateMode(DeprecatedEnum):
    REUSE_DATASET_IF_EXISTS: str
    REUSE_CACHE_IF_EXISTS: str
    FORCE_REDOWNLOAD: str
    @property
    def help_message(self): ...

class _IterableFromGenerator(Iterable):
    """Utility class to create an iterable from a generator function, in order to reset the generator when needed."""
    generator: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, generator: Callable, *args, **kwargs) -> None: ...
    def __iter__(self): ...

class ArchiveIterable(_IterableFromGenerator):
    """An iterable of (path, fileobj) from a TAR archive, used by `iter_archive`"""
    @classmethod
    def from_buf(cls, fileobj) -> ArchiveIterable: ...
    @classmethod
    def from_path(cls, urlpath_or_buf) -> ArchiveIterable: ...

class FilesIterable(_IterableFromGenerator):
    """An iterable of paths from a list of directories or files"""
    @classmethod
    def from_paths(cls, urlpaths) -> FilesIterable: ...

class DownloadManager:
    is_streaming: bool
    record_checksums: Incomplete
    download_config: Incomplete
    downloaded_paths: Incomplete
    extracted_paths: Incomplete
    def __init__(self, dataset_name: str | None = None, data_dir: str | None = None, download_config: DownloadConfig | None = None, base_path: str | None = None, record_checksums: bool = True) -> None:
        """Download manager constructor.

        Args:
            data_dir:
                can be used to specify a manual directory to get the files from.
            dataset_name (`str`):
                name of dataset this instance will be used for. If
                provided, downloads will contain which datasets they were used for.
            download_config (`DownloadConfig`):
                to specify the cache directory and other
                download options
            base_path (`str`):
                base path that is used when relative paths are used to
                download files. This can be a remote url.
            record_checksums (`bool`, defaults to `True`):
                Whether to record the checksums of the downloaded files. If None, the value is inferred from the builder.
        """
    @property
    def manual_dir(self): ...
    @property
    def downloaded_size(self):
        """Returns the total size of downloaded files."""
    @staticmethod
    def ship_files_with_pipeline(downloaded_path_or_paths, pipeline):
        """Ship the files using Beam FileSystems to the pipeline temp dir.

        Args:
            downloaded_path_or_paths (`str` or `list[str]` or `dict[str, str]`):
                Nested structure containing the
                downloaded path(s).
            pipeline ([`utils.beam_utils.BeamPipeline`]):
                Apache Beam Pipeline.

        Returns:
            `str` or `list[str]` or `dict[str, str]`
        """
    def download_custom(self, url_or_urls, custom_download):
        """
        Download given urls(s) by calling `custom_download`.

        Args:
            url_or_urls (`str` or `list` or `dict`):
                URL or `list` or `dict` of URLs to download and extract. Each URL is a `str`.
            custom_download (`Callable[src_url, dst_path]`):
                The source URL and destination path. For example
                `tf.io.gfile.copy`, that lets you download from  Google storage.

        Returns:
            downloaded_path(s): `str`, The downloaded paths matching the given input
                `url_or_urls`.

        Example:

        ```py
        >>> downloaded_files = dl_manager.download_custom('s3://my-bucket/data.zip', custom_download_for_my_private_bucket)
        ```
        """
    def download(self, url_or_urls):
        """Download given URL(s).

        By default, only one process is used for download. Pass customized `download_config.num_proc` to change this behavior.

        Args:
            url_or_urls (`str` or `list` or `dict`):
                URL or `list` or `dict` of URLs to download. Each URL is a `str`.

        Returns:
            `str` or `list` or `dict`:
                The downloaded paths matching the given input `url_or_urls`.

        Example:

        ```py
        >>> downloaded_files = dl_manager.download('https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz')
        ```
        """
    def iter_archive(self, path_or_buf: str | io.BufferedReader):
        """Iterate over files within an archive.

        Args:
            path_or_buf (`str` or `io.BufferedReader`):
                Archive path or archive binary file object.

        Yields:
            `tuple[str, io.BufferedReader]`:
                2-tuple (path_within_archive, file_object).
                File object is opened in binary mode.

        Example:

        ```py
        >>> archive = dl_manager.download('https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz')
        >>> files = dl_manager.iter_archive(archive)
        ```
        """
    def iter_files(self, paths: str | List[str]):
        """Iterate over file paths.

        Args:
            paths (`str` or `list` of `str`):
                Root paths.

        Yields:
            `str`: File path.

        Example:

        ```py
        >>> files = dl_manager.download_and_extract('https://huggingface.co/datasets/beans/resolve/main/data/train.zip')
        >>> files = dl_manager.iter_files(files)
        ```
        """
    def extract(self, path_or_paths, num_proc: str = 'deprecated'):
        '''Extract given path(s).

        Args:
            path_or_paths (path or `list` or `dict`):
                Path of file to extract. Each path is a `str`.
            num_proc (`int`):
                Use multi-processing if `num_proc` > 1 and the length of
                `path_or_paths` is larger than `num_proc`.

                <Deprecated version="2.6.2">

                Pass `DownloadConfig(num_proc=<num_proc>)` to the initializer instead.

                </Deprecated>

        Returns:
            extracted_path(s): `str`, The extracted paths matching the given input
            path_or_paths.

        Example:

        ```py
        >>> downloaded_files = dl_manager.download(\'https://storage.googleapis.com/seldon-datasets/sentence_polarity_v1/rt-polaritydata.tar.gz\')
        >>> extracted_files = dl_manager.extract(downloaded_files)
        ```
        '''
    def download_and_extract(self, url_or_urls):
        """Download and extract given `url_or_urls`.

        Is roughly equivalent to:

        ```
        extracted_paths = dl_manager.extract(dl_manager.download(url_or_urls))
        ```

        Args:
            url_or_urls (`str` or `list` or `dict`):
                URL or `list` or `dict` of URLs to download and extract. Each URL is a `str`.

        Returns:
            extracted_path(s): `str`, extracted paths of given URL(s).
        """
    def get_recorded_sizes_checksums(self): ...
    def delete_extracted_files(self) -> None: ...
    def manage_extracted_files(self) -> None: ...
