import dill
import multiprocess.pool
import multiprocessing.pool
from . import logging as logging
from .. import config as config
from ..parallel import parallel_map as parallel_map
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Callable, Dict, Iterable, Tuple, TypeVar

logger: Incomplete
memoize: Incomplete

def size_str(size_in_bytes):
    '''Returns a human readable size string.

    If size_in_bytes is None, then returns "Unknown size".

    For example `size_str(1.5 * datasets.units.GiB) == "1.50 GiB"`.

    Args:
        size_in_bytes: `int` or `None`, the size, in bytes, that we want to
            format as a human-readable size string.
    '''
def convert_file_size_to_int(size: int | str) -> int:
    '''
    Converts a size expressed as a string with digits an unit (like `"50MB"`) to an integer (in bytes).

    Args:
        size (`int` or `str`): The size to convert. Will be directly returned if an `int`.

    Example:

    ```py
    >>> convert_file_size_to_int("1MiB")
    1048576
    ```
    '''
def glob_pattern_to_regex(pattern): ...
def string_to_dict(string: str, pattern: str) -> Dict[str, str]:
    """Un-format a string using a python f-string pattern.
    From https://stackoverflow.com/a/36838374

    Example::

        >>> p = 'hello, my name is {name} and I am a {age} year old {what}'
        >>> s = p.format(name='cody', age=18, what='quarterback')
        >>> s
        'hello, my name is cody and I am a 18 year old quarterback'
        >>> string_to_dict(s, p)
        {'age': '18', 'name': 'cody', 'what': 'quarterback'}

    Args:
        string (str): input string
        pattern (str): pattern formatted like a python f-string

    Returns:
        Dict[str, str]: dictionary of variable -> value, retrieved from the input using the pattern

    Raises:
        ValueError: if the string doesn't match the pattern
    """
def asdict(obj):
    '''Convert an object to its dictionary representation recursively.

    <Added version="2.4.0"/>
    '''
def temporary_assignment(obj, attr, value) -> Generator[None, None, None]:
    """Temporarily assign obj.attr to value."""
def temp_seed(seed: int, set_pytorch: bool = False, set_tensorflow: bool = False):
    """Temporarily set the random seed. This works for python numpy, pytorch and tensorflow."""
def unique_values(values) -> Generator[Incomplete, None, None]:
    """Iterate over iterable and return only unique values in order."""
def no_op_if_value_is_null(func):
    """If the value is None, return None, else call `func`."""
def first_non_null_value(iterable):
    """Return the index and the value of the first non-null value in the iterable. If all values are None, return -1 as index."""
def zip_dict(*dicts) -> Generator[Incomplete, None, None]:
    """Iterate over items of dictionaries grouped by their keys."""

class NonMutableDict(dict):
    """Dict where keys can only be added but not modified.

    Will raise an error if the user try to overwrite one key. The error message
    can be customized during construction. It will be formatted using {key} for
    the overwritten key.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def update(self, other): ...

class classproperty(property):
    """Descriptor to be used as decorator for @classmethods."""
    def __get__(self, obj, objtype: Incomplete | None = None): ...

def map_nested(function: Callable[[Any], Any], data_struct: Any, dict_only: bool = False, map_list: bool = True, map_tuple: bool = False, map_numpy: bool = False, num_proc: int | None = None, parallel_min_length: int = 2, types: tuple | None = None, disable_tqdm: bool = True, desc: str | None = None) -> Any:
    '''Apply a function recursively to each element of a nested data struct.

    Use multiprocessing if num_proc > 1 and the length of data_struct is greater than or equal to
    `parallel_min_length`.

    <Changed version="2.5.0">

    Before version 2.5.0, multiprocessing was not used if `num_proc` was greater than or equal to ``len(iterable)``.

    Now, if `num_proc` is greater than or equal to ``len(iterable)``, `num_proc` is set to ``len(iterable)`` and
    multiprocessing is used.

    </Changed>

    Args:
        function (`Callable`): Function to be applied to `data_struct`.
        data_struct (`Any`): Data structure to apply `function` to.
        dict_only (`bool`, default `False`): Whether only apply `function` recursively to `dict` values in
            `data_struct`.
        map_list (`bool`, default `True`): Whether also apply `function` recursively to `list` elements (besides `dict`
            values).
        map_tuple (`bool`, default `False`): Whether also apply `function` recursively to `tuple` elements (besides
            `dict` values).
        map_numpy (`bool, default `False`): Whether also apply `function` recursively to `numpy.array` elements (besides
            `dict` values).
        num_proc (`int`, *optional*): Number of processes.
        parallel_min_length (`int`, default `2`): Minimum length of `data_struct` required for parallel
            processing.
            <Added version="2.5.0"/>
        types (`tuple`, *optional*): Additional types (besides `dict` values) to apply `function` recursively to their
            elements.
        disable_tqdm (`bool`, default `True`): Whether to disable the tqdm progressbar.
        desc (`str`, *optional*): Prefix for the tqdm progressbar.

    Returns:
        `Any`
    '''

class NestedDataStructure:
    data: Incomplete
    def __init__(self, data: Incomplete | None = None) -> None: ...
    def flatten(self, data: Incomplete | None = None): ...

def has_sufficient_disk_space(needed_bytes, directory: str = '.'): ...
def get_imports(file_path: str) -> Tuple[str, str, str, str]:
    '''Find whether we should import or clone additional files for a given processing script.
        And list the import.

    We allow:
    - library dependencies,
    - local dependencies and
    - external dependencies whose url is specified with a comment starting from "# From:\' followed by the raw url to a file, an archive or a github repository.
        external dependencies will be downloaded (and extracted if needed in the dataset folder).
        We also add an `__init__.py` to each sub-folder of a downloaded folder so the user can import from them in the script.

    Note that only direct import in the dataset processing script will be handled
    We don\'t recursively explore the additional import to download further files.

    Example::

        import tensorflow
        import .c4_utils
        import .clicr.dataset-code.build_json_dataset  # From: https://raw.githubusercontent.com/clips/clicr/master/dataset-code/build_json_dataset
    '''

class Pickler(dill.Pickler):
    """Same Pickler as the one from dill, but improved for notebooks and shells"""
    dispatch: Incomplete
    def save(self, obj, save_persistent_id: bool = True): ...
    def memoize(self, obj) -> None: ...

def dump(obj, file) -> None:
    """pickle an object to a file"""
def dumps(obj):
    """pickle an object to a string"""
def pklregister(t): ...
def save_code(pickler, obj) -> None: ...
def save_function(pickler, obj) -> None:
    """
        From dill._dill.save_function
        This is a modified version that make globs deterministic since the order of
        the keys in the output dictionary of globalvars can change.
        """
def copyfunc(func): ...
Y = TypeVar('Y')

def iflatmap_unordered(pool: multiprocessing.pool.Pool | multiprocess.pool.Pool, func: Callable[..., Iterable[Y]], *, kwargs_iterable: Iterable[dict]) -> Iterable[Y]: ...
