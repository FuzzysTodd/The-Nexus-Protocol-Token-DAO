import numpy as np
from pandas import Categorical as Categorical, DataFrame as DataFrame, Index as Index, MultiIndex as MultiIndex, Series as Series
from pandas._libs import lib as lib
from pandas._libs.hashing import hash_object_array as hash_object_array
from pandas._typing import ArrayLike as ArrayLike, npt as npt
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_list_like as is_list_like
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCExtensionArray as ABCExtensionArray, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries
from typing import Hashable, Iterable, Iterator

def combine_hash_arrays(arrays: Iterator[np.ndarray], num_items: int) -> npt.NDArray[np.uint64]:
    """
    Parameters
    ----------
    arrays : Iterator[np.ndarray]
    num_items : int

    Returns
    -------
    np.ndarray[uint64]

    Should be the same as CPython's tupleobject.c
    """
def hash_pandas_object(obj: Index | DataFrame | Series, index: bool = True, encoding: str = 'utf8', hash_key: str | None = ..., categorize: bool = True) -> Series:
    """
    Return a data hash of the Index/Series/DataFrame.

    Parameters
    ----------
    obj : Index, Series, or DataFrame
    index : bool, default True
        Include the index in the hash (if Series/DataFrame).
    encoding : str, default 'utf8'
        Encoding for data & key when strings.
    hash_key : str, default _default_hash_key
        Hash_key for string key to encode.
    categorize : bool, default True
        Whether to first categorize object arrays before hashing. This is more
        efficient when the array contains duplicate values.

    Returns
    -------
    Series of uint64, same length as the object
    """
def hash_tuples(vals: MultiIndex | Iterable[tuple[Hashable, ...]], encoding: str = 'utf8', hash_key: str = ...) -> npt.NDArray[np.uint64]:
    """
    Hash an MultiIndex / listlike-of-tuples efficiently.

    Parameters
    ----------
    vals : MultiIndex or listlike-of-tuples
    encoding : str, default 'utf8'
    hash_key : str, default _default_hash_key

    Returns
    -------
    ndarray[np.uint64] of hashed values
    """
def hash_array(vals: ArrayLike, encoding: str = 'utf8', hash_key: str = ..., categorize: bool = True) -> npt.NDArray[np.uint64]:
    """
    Given a 1d array, return an array of deterministic integers.

    Parameters
    ----------
    vals : ndarray or ExtensionArray
    encoding : str, default 'utf8'
        Encoding for data & key when strings.
    hash_key : str, default _default_hash_key
        Hash_key for string key to encode.
    categorize : bool, default True
        Whether to first categorize object arrays before hashing. This is more
        efficient when the array contains duplicate values.

    Returns
    -------
    ndarray[np.uint64, ndim=1]
        Hashed values, same length as the vals.
    """
