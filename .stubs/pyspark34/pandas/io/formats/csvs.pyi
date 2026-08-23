import numpy as np
from _typeshed import Incomplete
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, FloatFormatType as FloatFormatType, IndexLabel as IndexLabel, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.dtypes.generic import ABCDatetimeIndex as ABCDatetimeIndex, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCPeriodIndex as ABCPeriodIndex
from pandas.core.dtypes.missing import notna as notna
from pandas.core.indexes.api import Index as Index
from pandas.io.common import get_handle as get_handle
from pandas.io.formats.format import DataFrameFormatter as DataFrameFormatter
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Hashable, Sequence

class CSVFormatter:
    cols: np.ndarray
    fmt: Incomplete
    obj: Incomplete
    filepath_or_buffer: Incomplete
    encoding: Incomplete
    compression: Incomplete
    mode: Incomplete
    storage_options: Incomplete
    sep: Incomplete
    index_label: Incomplete
    errors: Incomplete
    quoting: Incomplete
    quotechar: Incomplete
    doublequote: Incomplete
    escapechar: Incomplete
    lineterminator: Incomplete
    date_format: Incomplete
    chunksize: Incomplete
    def __init__(self, formatter: DataFrameFormatter, path_or_buf: FilePath | WriteBuffer[str] | WriteBuffer[bytes] = '', sep: str = ',', cols: Sequence[Hashable] | None = None, index_label: IndexLabel | None = None, mode: str = 'w', encoding: str | None = None, errors: str = 'strict', compression: CompressionOptions = 'infer', quoting: int | None = None, lineterminator: str | None = '\n', chunksize: int | None = None, quotechar: str | None = '"', date_format: str | None = None, doublequote: bool = True, escapechar: str | None = None, storage_options: StorageOptions = None) -> None: ...
    @property
    def na_rep(self) -> str: ...
    @property
    def float_format(self) -> FloatFormatType | None: ...
    @property
    def decimal(self) -> str: ...
    @property
    def header(self) -> bool | Sequence[str]: ...
    @property
    def index(self) -> bool: ...
    @property
    def has_mi_columns(self) -> bool: ...
    def data_index(self) -> Index: ...
    @property
    def nlevels(self) -> int: ...
    @property
    def write_cols(self) -> Sequence[Hashable]: ...
    @property
    def encoded_labels(self) -> list[Hashable]: ...
    writer: Incomplete
    def save(self) -> None:
        """
        Create the writer & save.
        """
