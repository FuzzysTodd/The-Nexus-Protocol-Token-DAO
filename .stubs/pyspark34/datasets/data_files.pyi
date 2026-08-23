import huggingface_hub
from . import config as config
from .download import DownloadConfig as DownloadConfig
from .download.streaming_download_manager import xbasename as xbasename, xjoin as xjoin
from .splits import Split as Split
from .utils import logging as logging
from .utils.file_utils import is_local_path as is_local_path, is_relative_path as is_relative_path
from .utils.py_utils import glob_pattern_to_regex as glob_pattern_to_regex, string_to_dict as string_to_dict
from _typeshed import Incomplete
from typing import Dict, List, Tuple

SANITIZED_DEFAULT_SPLIT: Incomplete
logger: Incomplete

class Url(str): ...
class EmptyDatasetError(FileNotFoundError): ...

SPLIT_PATTERN_SHARDED: str
SPLIT_KEYWORDS: Incomplete
NON_WORDS_CHARS: str
KEYWORDS_IN_PATH_NAME_BASE_PATTERNS: Incomplete
DEFAULT_SPLITS: Incomplete
DEFAULT_PATTERNS_SPLIT_IN_PATH_NAME: Incomplete
DEFAULT_PATTERNS_ALL: Incomplete
ALL_SPLIT_PATTERNS: Incomplete
ALL_DEFAULT_PATTERNS: Incomplete
METADATA_PATTERNS: Incomplete
WILDCARD_CHARACTERS: str
FILES_TO_IGNORE: Incomplete

def contains_wildcards(pattern: str) -> bool: ...
def sanitize_patterns(patterns: Dict | List | str) -> Dict[str, List[str] | DataFilesList]:
    '''
    Take the data_files patterns from the user, and format them into a dictionary.
    Each key is the name of the split, and each value is a list of data files patterns (paths or urls).
    The default split is "train".

    Returns:
        patterns: dictionary of split_name -> list of patterns
    '''
def resolve_pattern(pattern: str, base_path: str, allowed_extensions: List[str] | None = None, download_config: DownloadConfig | None = None) -> List[str]:
    '''
    Resolve the paths and URLs of the data files from the pattern passed by the user.

    You can use patterns to resolve multiple local files. Here are a few examples:
    - *.csv to match all the CSV files at the first level
    - **.csv to match all the CSV files at any level
    - data/* to match all the files inside "data"
    - data/** to match all the files inside "data" and its subdirectories

    The patterns are resolved using the fsspec glob.

    glob.glob, Path.glob, Path.match or fnmatch do not support ** with a prefix/suffix other than a forward slash /.
    For instance, this means **.json is the same as *.json. On the contrary, the fsspec glob has no limits regarding the ** prefix/suffix,
    resulting in **.json being equivalent to **/*.json.

    More generally:
    - \'*\' matches any character except a forward-slash (to match just the file or directory name)
    - \'**\' matches any character including a forward-slash /

    Hidden files and directories (i.e. whose names start with a dot) are ignored, unless they are explicitly requested.
    The same applies to special directories that start with a double underscore like "__pycache__".
    You can still include one if the pattern explicilty mentions it:
    - to include a hidden file: "*/.hidden.txt" or "*/.*"
    - to include a hidden directory: ".hidden/*" or ".*/*"
    - to include a special directory: "__special__/*" or "__*/*"

    Example::

        >>> from datasets.data_files import resolve_pattern
        >>> base_path = "."
        >>> resolve_pattern("docs/**/*.py", base_path)
        [/Users/mariosasko/Desktop/projects/datasets/docs/source/_config.py\']

    Args:
        pattern (str): Unix pattern or paths or URLs of the data files to resolve.
            The paths can be absolute or relative to base_path.
            Remote filesystems using fsspec are supported, e.g. with the hf:// protocol.
        base_path (str): Base path to use when resolving relative paths.
        allowed_extensions (Optional[list], optional): White-list of file extensions to use. Defaults to None (all extensions).
            For example: allowed_extensions=[".csv", ".json", ".txt", ".parquet"]
    Returns:
        List[str]: List of paths or URLs to the local or remote files that match the patterns.
    '''
def get_data_patterns(base_path: str, download_config: DownloadConfig | None = None) -> Dict[str, List[str]]:
    '''
    Get the default pattern from a directory testing all the supported patterns.
    The first patterns to return a non-empty list of data files is returned.

    Some examples of supported patterns:

    Input:

        my_dataset_repository/
        ├── README.md
        └── dataset.csv

    Output:

        {"train": ["**"]}

    Input:

        my_dataset_repository/
        ├── README.md
        ├── train.csv
        └── test.csv

        my_dataset_repository/
        ├── README.md
        └── data/
            ├── train.csv
            └── test.csv

        my_dataset_repository/
        ├── README.md
        ├── train_0.csv
        ├── train_1.csv
        ├── train_2.csv
        ├── train_3.csv
        ├── test_0.csv
        └── test_1.csv

    Output:

        {\'train\': [\'train[-._ 0-9/]**\', \'**/*[-._ 0-9/]train[-._ 0-9/]**\', \'training[-._ 0-9/]**\', \'**/*[-._ 0-9/]training[-._ 0-9/]**\'],
         \'test\': [\'test[-._ 0-9/]**\', \'**/*[-._ 0-9/]test[-._ 0-9/]**\', \'testing[-._ 0-9/]**\', \'**/*[-._ 0-9/]testing[-._ 0-9/]**\', ...]}

    Input:

        my_dataset_repository/
        ├── README.md
        └── data/
            ├── train/
            │   ├── shard_0.csv
            │   ├── shard_1.csv
            │   ├── shard_2.csv
            │   └── shard_3.csv
            └── test/
                ├── shard_0.csv
                └── shard_1.csv

    Output:

        {\'train\': [\'train[-._ 0-9/]**\', \'**/*[-._ 0-9/]train[-._ 0-9/]**\', \'training[-._ 0-9/]**\', \'**/*[-._ 0-9/]training[-._ 0-9/]**\'],
         \'test\': [\'test[-._ 0-9/]**\', \'**/*[-._ 0-9/]test[-._ 0-9/]**\', \'testing[-._ 0-9/]**\', \'**/*[-._ 0-9/]testing[-._ 0-9/]**\', ...]}

    Input:

        my_dataset_repository/
        ├── README.md
        └── data/
            ├── train-00000-of-00003.csv
            ├── train-00001-of-00003.csv
            ├── train-00002-of-00003.csv
            ├── test-00000-of-00001.csv
            ├── random-00000-of-00003.csv
            ├── random-00001-of-00003.csv
            └── random-00002-of-00003.csv

    Output:

        {\'train\': [\'data/train-[0-9][0-9][0-9][0-9][0-9]-of-[0-9][0-9][0-9][0-9][0-9]*.*\'],
         \'test\': [\'data/test-[0-9][0-9][0-9][0-9][0-9]-of-[0-9][0-9][0-9][0-9][0-9]*.*\'],
         \'random\': [\'data/random-[0-9][0-9][0-9][0-9][0-9]-of-[0-9][0-9][0-9][0-9][0-9]*.*\']}

    In order, it first tests if SPLIT_PATTERN_SHARDED works, otherwise it tests the patterns in ALL_DEFAULT_PATTERNS.
    '''
def get_metadata_patterns(base_path: str, download_config: DownloadConfig | None = None) -> List[str]:
    """
    Get the supported metadata patterns from a local directory.
    """

class DataFilesList(List[str]):
    """
    List of data files (absolute local paths or URLs).
    It has two construction methods given the user's data files patterns :
    - ``from_hf_repo``: resolve patterns inside a dataset repository
    - ``from_local_or_remote``: resolve patterns from a local path

    Moreover DataFilesList has an additional attribute ``origin_metadata``.
    It can store:
    - the last modified time of local files
    - ETag of remote files
    - commit sha of a dataset repository

    Thanks to this additional attribute, it is possible to hash the list
    and get a different hash if and only if at least one file changed.
    This is useful for caching Dataset objects that are obtained from a list of data files.
    """
    origin_metadata: Incomplete
    def __init__(self, data_files: List[str], origin_metadata: List[Tuple[str]]) -> None: ...
    def __add__(self, other): ...
    @classmethod
    def from_hf_repo(cls, patterns: List[str], dataset_info: huggingface_hub.hf_api.DatasetInfo, base_path: str | None = None, allowed_extensions: List[str] | None = None, download_config: DownloadConfig | None = None) -> DataFilesList: ...
    @classmethod
    def from_local_or_remote(cls, patterns: List[str], base_path: str | None = None, allowed_extensions: List[str] | None = None, download_config: DownloadConfig | None = None) -> DataFilesList: ...
    @classmethod
    def from_patterns(cls, patterns: List[str], base_path: str | None = None, allowed_extensions: List[str] | None = None, download_config: DownloadConfig | None = None) -> DataFilesList: ...
    def filter_extensions(self, extensions: List[str]) -> DataFilesList: ...

class DataFilesDict(Dict[str, DataFilesList]):
    """
    Dict of split_name -> list of data files (absolute local paths or URLs).
    It has two construction methods given the user's data files patterns :
    - ``from_hf_repo``: resolve patterns inside a dataset repository
    - ``from_local_or_remote``: resolve patterns from a local path

    Moreover each list is a DataFilesList. It is possible to hash the dictionary
    and get a different hash if and only if at least one file changed.
    For more info, see ``DataFilesList``.

    This is useful for caching Dataset objects that are obtained from a list of data files.

    Changing the order of the keys of this dictionary also doesn't change its hash.
    """
    @classmethod
    def from_local_or_remote(cls, patterns: Dict[str, List[str] | DataFilesList], base_path: str | None = None, allowed_extensions: List[str] | None = None, download_config: DownloadConfig | None = None) -> DataFilesDict: ...
    @classmethod
    def from_hf_repo(cls, patterns: Dict[str, List[str] | DataFilesList], dataset_info: huggingface_hub.hf_api.DatasetInfo, base_path: str | None = None, allowed_extensions: List[str] | None = None, download_config: DownloadConfig | None = None) -> DataFilesDict: ...
    @classmethod
    def from_patterns(cls, patterns: Dict[str, List[str] | DataFilesList], base_path: str | None = None, allowed_extensions: List[str] | None = None, download_config: DownloadConfig | None = None) -> DataFilesDict: ...
    def filter_extensions(self, extensions: List[str]) -> DataFilesDict: ...
