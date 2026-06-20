import numpy as np
import pandas as pd
from .utils import get_logger as get_logger
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Iterator, List, NamedTuple, Sequence, Tuple
from xgboost import DMatrix as DMatrix, DataIter as DataIter, QuantileDMatrix as QuantileDMatrix
from xgboost.compat import concat as concat

def stack_series(series: pd.Series) -> np.ndarray:
    """Stack a series of arrays."""

class Alias(NamedTuple):
    data: Incomplete
    label: Incomplete
    weight: Incomplete
    margin: Incomplete
    valid: Incomplete
    qid: Incomplete

alias: Incomplete

def concat_or_none(seq: Sequence[np.ndarray] | None) -> np.ndarray | None:
    """Concatenate the data if it's not None."""
def cache_partitions(iterator: Iterator[pd.DataFrame], append: Callable[[pd.DataFrame, str, bool], None]) -> None:
    """Extract partitions from pyspark iterator. `append` is a user defined function for
    accepting new partition."""

class PartIter(DataIter):
    """Iterator for creating Quantile DMatrix from partitions."""
    def __init__(self, data: Dict[str, List], device_id: int | None, **kwargs: Any) -> None: ...
    def next(self, input_data: Callable) -> int: ...
    def reset(self) -> None: ...

def make_qdm(data: Dict[str, List[np.ndarray]], gpu_id: int | None, meta: Dict[str, Any], ref: DMatrix | None, params: Dict[str, Any]) -> DMatrix:
    """Handle empty partition for QuantileDMatrix."""
def create_dmatrix_from_partitions(iterator: Iterator[pd.DataFrame], feature_cols: Sequence[str] | None, gpu_id: int | None, use_qdm: bool, kwargs: Dict[str, Any], enable_sparse_data_optim: bool, has_validation_col: bool) -> Tuple[DMatrix, DMatrix | None]:
    """Create DMatrix from spark data partitions.

    Parameters
    ----------
    iterator :
        Pyspark partition iterator.
    feature_cols:
        A sequence of feature names, used only when rapids plugin is enabled.
    gpu_id:
        Device ordinal, used when GPU is enabled.
    use_qdm :
        Whether QuantileDMatrix should be used instead of DMatrix.
    kwargs :
        Metainfo for DMatrix.
    enable_sparse_data_optim :
        Whether sparse data should be unwrapped
    has_validation:
        Whether there's validation data.

    Returns
    -------
    Training DMatrix and an optional validation DMatrix.
    """
