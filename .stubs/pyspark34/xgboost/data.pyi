import ctypes
from ._typing import CupyT as CupyT, DataType as DataType, FeatureNames as FeatureNames, FeatureTypes as FeatureTypes, FloatCompatible as FloatCompatible, NumpyDType as NumpyDType, PandasDType as PandasDType, c_bst_ulong as c_bst_ulong
from .compat import DataFrame as DataFrame, lazy_isinstance as lazy_isinstance
from .core import DMatrix as DMatrix, DataIter as DataIter, _ProxyDMatrix, c_array as c_array, c_str as c_str, from_pystr_to_cstr as from_pystr_to_cstr, make_jcargs as make_jcargs
from _typeshed import Incomplete
from typing import Any, Callable, Iterator, Tuple

DispatchedDataBackendReturnType = Tuple[ctypes.c_void_p, FeatureNames | None, FeatureTypes | None]
CAT_T: str

def is_nullable_dtype(dtype: PandasDType) -> bool:
    """Wether dtype is a pandas nullable type."""
def record_batch_data_iter(data_iter: Iterator) -> Callable:
    """Data iterator used to ingest Arrow columnar record batches. We are not using
    class DataIter because it is only intended for building Device DMatrix and external
    memory DMatrix.

    """
def dispatch_data_backend(data: DataType, missing: FloatCompatible, threads: int, feature_names: FeatureNames | None, feature_types: FeatureTypes | None, enable_categorical: bool = False) -> DispatchedDataBackendReturnType:
    """Dispatch data for DMatrix."""
def dispatch_meta_backend(matrix: DMatrix, data: DataType, name: str, dtype: NumpyDType | None = None) -> None:
    """Dispatch for meta info."""

class SingleBatchInternalIter(DataIter):
    """An iterator for single batch data to help creating device DMatrix.
    Transforming input directly to histogram with normal single batch data API
    can not access weight for sketching.  So this iterator acts as a staging
    area for meta info.

    """
    kwargs: Incomplete
    it: int
    def __init__(self, **kwargs: Any) -> None: ...
    def next(self, input_data: Callable) -> int: ...
    def reset(self) -> None: ...

def dispatch_proxy_set_data(proxy: _ProxyDMatrix, data: DataType, cat_codes: list | None, allow_host: bool) -> None:
    """Dispatch for DeviceQuantileDMatrix."""
