from .arrow_dataset import Dataset as Dataset
from .info import DatasetInfo as DatasetInfo
from .naming import INVALID_WINDOWS_CHARACTERS_IN_PATH as INVALID_WINDOWS_CHARACTERS_IN_PATH
from .table import ConcatenationTable as ConcatenationTable, InMemoryTable as InMemoryTable, MemoryMappedTable as MemoryMappedTable, Table as Table
from .utils.deprecation_utils import deprecated as deprecated
from .utils.logging import get_logger as get_logger
from .utils.py_utils import asdict as asdict, dumps as dumps
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Tuple

logger: Incomplete

class _TempDirWithCustomCleanup:
    """
    A temporary directory with a custom cleanup function.
    We need a custom temporary directory cleanup in order to delete the dataset objects that have
    cache files in the temporary directory before deleting the dorectory itself.
    """
    name: Incomplete
    def __init__(self, cleanup_func: Incomplete | None = None, *cleanup_func_args, **cleanup_func_kwargs) -> None: ...
    def cleanup(self) -> None: ...

def maybe_register_dataset_for_temp_dir_deletion(dataset) -> None:
    """
    This function registers the datasets that have cache files in _TEMP_DIR_FOR_TEMP_CACHE_FILES in order
    to properly delete them before deleting the temporary directory.
    The temporary directory _TEMP_DIR_FOR_TEMP_CACHE_FILES is used when caching is disabled.
    """
def get_datasets_with_cache_file_in_temp_dir(): ...
def enable_caching() -> None:
    """
    When applying transforms on a dataset, the data are stored in cache files.
    The caching mechanism allows to reload an existing cache file if it's already been computed.

    Reloading a dataset is possible since the cache files are named using the dataset fingerprint, which is updated
    after each transform.

    If disabled, the library will no longer reload cached datasets files when applying transforms to the datasets.
    More precisely, if the caching is disabled:
    - cache files are always recreated
    - cache files are written to a temporary directory that is deleted when session closes
    - cache files are named using a random hash instead of the dataset fingerprint
    - use [`~datasets.Dataset.save_to_disk`] to save a transformed dataset or it will be deleted when session closes
    - caching doesn't affect [`~datasets.load_dataset`]. If you want to regenerate a dataset from scratch you should use
    the `download_mode` parameter in [`~datasets.load_dataset`].
    """
def disable_caching() -> None:
    """
    When applying transforms on a dataset, the data are stored in cache files.
    The caching mechanism allows to reload an existing cache file if it's already been computed.

    Reloading a dataset is possible since the cache files are named using the dataset fingerprint, which is updated
    after each transform.

    If disabled, the library will no longer reload cached datasets files when applying transforms to the datasets.
    More precisely, if the caching is disabled:
    - cache files are always recreated
    - cache files are written to a temporary directory that is deleted when session closes
    - cache files are named using a random hash instead of the dataset fingerprint
    - use [`~datasets.Dataset.save_to_disk`] to save a transformed dataset or it will be deleted when session closes
    - caching doesn't affect [`~datasets.load_dataset`]. If you want to regenerate a dataset from scratch you should use
    the `download_mode` parameter in [`~datasets.load_dataset`].
    """
def set_caching_enabled(boolean: bool):
    """
    When applying transforms on a dataset, the data are stored in cache files.
    The caching mechanism allows to reload an existing cache file if it's already been computed.

    Reloading a dataset is possible since the cache files are named using the dataset fingerprint, which is updated
    after each transform.

    If disabled, the library will no longer reload cached datasets files when applying transforms to the datasets.
    More precisely, if the caching is disabled:
    - cache files are always recreated
    - cache files are written to a temporary directory that is deleted when session closes
    - cache files are named using a random hash instead of the dataset fingerprint
    - use :func:`datasets.Dataset.save_to_disk` to save a transformed dataset or it will be deleted when session closes
    - caching doesn't affect :func:`datasets.load_dataset`. If you want to regenerate a dataset from scratch you should use
    the ``download_mode`` parameter in :func:`datasets.load_dataset`.
    """
def is_caching_enabled() -> bool:
    """
    When applying transforms on a dataset, the data are stored in cache files.
    The caching mechanism allows to reload an existing cache file if it's already been computed.

    Reloading a dataset is possible since the cache files are named using the dataset fingerprint, which is updated
    after each transform.

    If disabled, the library will no longer reload cached datasets files when applying transforms to the datasets.
    More precisely, if the caching is disabled:
    - cache files are always recreated
    - cache files are written to a temporary directory that is deleted when session closes
    - cache files are named using a random hash instead of the dataset fingerprint
    - use [`~datasets.Dataset.save_to_disk`]] to save a transformed dataset or it will be deleted when session closes
    - caching doesn't affect [`~datasets.load_dataset`]. If you want to regenerate a dataset from scratch you should use
    the `download_mode` parameter in [`~datasets.load_dataset`].
    """
def get_temporary_cache_files_directory() -> str:
    """Return a directory that is deleted when session closes."""
def hashregister(*types): ...

class Hasher:
    """Hasher that accepts python objects as inputs."""
    dispatch: Dict
    m: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def hash_bytes(cls, value: bytes | List[bytes]) -> str: ...
    @classmethod
    def hash_default(cls, value: Any) -> str: ...
    @classmethod
    def hash(cls, value: Any) -> str: ...
    def update(self, value: Any) -> None: ...
    def hexdigest(self) -> str: ...

fingerprint_warnings: Dict[str, bool]

def generate_fingerprint(dataset) -> str: ...
def generate_random_fingerprint(nbits: int = 64) -> str: ...
def update_fingerprint(fingerprint, transform, transform_args): ...
def validate_fingerprint(fingerprint: str, max_length: int = 64):
    """
    Make sure the fingerprint is a non-empty string that is not longer that max_length=64 by default,
    so that the fingerprint can be used to name cache files without issues.
    """
def format_transform_for_fingerprint(func: Callable, version: str | None = None) -> str:
    """
    Format a transform to the format that will be used to update the fingerprint.
    """
def format_kwargs_for_fingerprint(func: Callable, args: Tuple, kwargs: Dict[str, Any], use_kwargs: List[str] | None = None, ignore_kwargs: List[str] | None = None, randomized_function: bool = False) -> Dict[str, Any]:
    """
    Format the kwargs of a transform to the format that will be used to update the fingerprint.
    """
def fingerprint_transform(inplace: bool, use_kwargs: List[str] | None = None, ignore_kwargs: List[str] | None = None, fingerprint_names: List[str] | None = None, randomized_function: bool = False, version: str | None = None):
    '''
    Wrapper for dataset transforms to update the dataset fingerprint using ``update_fingerprint``
    Args:
        inplace (:obj:`bool`):  If inplace is True, the fingerprint of the dataset is updated inplace.
            Otherwise, a parameter "new_fingerprint" is passed to the wrapped method that should take care of
            setting the fingerprint of the returned Dataset.
        use_kwargs (:obj:`List[str]`, optional): optional white list of argument names to take into account
            to update the fingerprint to the wrapped method that should take care of
            setting the fingerprint of the returned Dataset. By default all the arguments are used.
        ignore_kwargs (:obj:`List[str]`, optional): optional black list of argument names to take into account
            to update the fingerprint. Note that ignore_kwargs prevails on use_kwargs.
        fingerprint_names (:obj:`List[str]`, optional, defaults to ["new_fingerprint"]):
            If the dataset transforms is not inplace and returns a DatasetDict, then it can require
            several fingerprints (one per dataset in the DatasetDict). By specifying fingerprint_names,
            one fingerprint named after each element of fingerprint_names is going to be passed.
        randomized_function (:obj:`bool`, defaults to False): If the dataset transform is random and has
            optional parameters "seed" and "generator", then you can set randomized_function to True.
            This way, even if users set "seed" and "generator" to None, then the fingerprint is
            going to be randomly generated depending on numpy\'s current state. In this case, the
            generator is set to np.random.default_rng(np.random.get_state()[1][0]).
        version (:obj:`str`, optional): version of the transform. The version is taken into account when
            computing the fingerprint. If a datase transform changes (or at least if the output data
            that are cached changes), then one should increase the version. If the version stays the
            same, then old cached data could be reused that are not compatible with the new transform.
            It should be in the format "MAJOR.MINOR.PATCH".
    '''
