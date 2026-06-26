import numpy as np
from _typeshed import Incomplete
from collections.abc import Generator
from pandas import Index as Index
from pandas._libs import lib as lib
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, NpDtype as NpDtype, RandomState as RandomState, T as T
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike as construct_1d_object_array_from_listlike
from pandas.core.dtypes.common import is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_extension_array_dtype as is_extension_array_dtype, is_integer as is_integer
from pandas.core.dtypes.generic import ABCExtensionArray as ABCExtensionArray, ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import iterable_not_string as iterable_not_string
from pandas.core.dtypes.missing import isna as isna
from typing import Any, Callable, Collection, Hashable, Iterable, Sequence, overload

def flatten(line) -> Generator[Incomplete, Incomplete, None]:
    """
    Flatten an arbitrarily nested sequence.

    Parameters
    ----------
    line : sequence
        The non string sequence to flatten

    Notes
    -----
    This doesn't consider strings sequences.

    Returns
    -------
    flattened : generator
    """
def consensus_name_attr(objs): ...
def is_bool_indexer(key: Any) -> bool:
    """
    Check whether `key` is a valid boolean indexer.

    Parameters
    ----------
    key : Any
        Only list-likes may be considered boolean indexers.
        All other types are not considered a boolean indexer.
        For array-like input, boolean ndarrays or ExtensionArrays
        with ``_is_boolean`` set are considered boolean indexers.

    Returns
    -------
    bool
        Whether `key` is a valid boolean indexer.

    Raises
    ------
    ValueError
        When the array is an object-dtype ndarray or ExtensionArray
        and contains missing values.

    See Also
    --------
    check_array_indexer : Check that `key` is a valid array to index,
        and convert to an ndarray.
    """
def cast_scalar_indexer(val):
    """
    Disallow indexing with a float key, even if that key is a round number.

    Parameters
    ----------
    val : scalar

    Returns
    -------
    outval : scalar
    """
def not_none(*args):
    """
    Returns a generator consisting of the arguments that are not None.
    """
def any_none(*args) -> bool:
    """
    Returns a boolean indicating if any argument is None.
    """
def all_none(*args) -> bool:
    """
    Returns a boolean indicating if all arguments are None.
    """
def any_not_none(*args) -> bool:
    """
    Returns a boolean indicating if any argument is not None.
    """
def all_not_none(*args) -> bool:
    """
    Returns a boolean indicating if all arguments are not None.
    """
def count_not_none(*args) -> int:
    """
    Returns the count of arguments that are not None.
    """
@overload
def asarray_tuplesafe(values: ArrayLike | list | tuple | zip, dtype: NpDtype | None = ...) -> np.ndarray: ...
@overload
def asarray_tuplesafe(values: Iterable, dtype: NpDtype | None = ...) -> ArrayLike: ...
def index_labels_to_array(labels: np.ndarray | Iterable, dtype: NpDtype | None = None) -> np.ndarray:
    """
    Transform label or iterable of labels to array, for use in Index.

    Parameters
    ----------
    dtype : dtype
        If specified, use as dtype of the resulting array, otherwise infer.

    Returns
    -------
    array
    """
def maybe_make_list(obj): ...
def maybe_iterable_to_list(obj: Iterable[T] | T) -> Collection[T] | T:
    """
    If obj is Iterable but not list-like, consume into list.
    """
def is_null_slice(obj) -> bool:
    """
    We have a null slice.
    """
def is_empty_slice(obj) -> bool:
    """
    We have an empty slice, e.g. no values are selected.
    """
def is_true_slices(line) -> list[bool]:
    '''
    Find non-trivial slices in "line": return a list of booleans with same length.
    '''
def is_full_slice(obj, line: int) -> bool:
    """
    We have a full length slice.
    """
def get_callable_name(obj): ...
def apply_if_callable(maybe_callable, obj, **kwargs):
    """
    Evaluate possibly callable input using obj and kwargs if it is callable,
    otherwise return as it is.

    Parameters
    ----------
    maybe_callable : possibly a callable
    obj : NDFrame
    **kwargs
    """
def standardize_mapping(into):
    """
    Helper function to standardize a supplied mapping.

    Parameters
    ----------
    into : instance or subclass of collections.abc.Mapping
        Must be a class, an initialized collections.defaultdict,
        or an instance of a collections.abc.Mapping subclass.

    Returns
    -------
    mapping : a collections.abc.Mapping subclass or other constructor
        a callable object that can accept an iterator to create
        the desired Mapping.

    See Also
    --------
    DataFrame.to_dict
    Series.to_dict
    """
@overload
def random_state(state: np.random.Generator) -> np.random.Generator: ...
@overload
def random_state(state: int | ArrayLike | np.random.BitGenerator | np.random.RandomState | None) -> np.random.RandomState: ...
def pipe(obj, func: Callable[..., T] | tuple[Callable[..., T], str], *args, **kwargs) -> T:
    """
    Apply a function ``func`` to object ``obj`` either by passing obj as the
    first argument to the function or, in the case that the func is a tuple,
    interpret the first element of the tuple as a function and pass the obj to
    that function as a keyword argument whose key is the value of the second
    element of the tuple.

    Parameters
    ----------
    func : callable or tuple of (callable, str)
        Function to apply to this object or, alternatively, a
        ``(callable, data_keyword)`` tuple where ``data_keyword`` is a
        string indicating the keyword of ``callable`` that expects the
        object.
    *args : iterable, optional
        Positional arguments passed into ``func``.
    **kwargs : dict, optional
        A dictionary of keyword arguments passed into ``func``.

    Returns
    -------
    object : the return type of ``func``.
    """
def get_rename_function(mapper):
    """
    Returns a function that will map names/labels, dependent if mapper
    is a dict, Series or just a function.
    """
def convert_to_list_like(values: Hashable | Iterable | AnyArrayLike) -> list | AnyArrayLike:
    """
    Convert list-like or scalar input to list-like. List, numpy and pandas array-like
    inputs are returned unmodified whereas others are converted to list.
    """
def temp_setattr(obj, attr: str, value) -> Generator[None, None, None]:
    """Temporarily set attribute on an object.

    Args:
        obj: Object whose attribute will be modified.
        attr: Attribute to modify.
        value: Value to temporarily set attribute to.

    Yields:
        obj with modified attribute.
    """
def require_length_match(data, index: Index) -> None:
    """
    Check the length of data matches the length of the index.
    """
def get_cython_func(arg: Callable) -> str | None:
    """
    if we define an internal function for this argument, return it
    """
def is_builtin_func(arg):
    """
    if we define a builtin function for this argument, return it,
    otherwise return the arg
    """
def fill_missing_names(names: Sequence[Hashable | None]) -> list[Hashable]:
    """
    If a name is missing then replace it by level_n, where n is the count

    .. versionadded:: 1.4.0

    Parameters
    ----------
    names : list-like
        list of column names or None values.

    Returns
    -------
    list
        list of column names with the None values replaced.
    """
