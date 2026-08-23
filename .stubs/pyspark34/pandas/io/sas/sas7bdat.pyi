import numpy as np
from _typeshed import Incomplete
from collections import abc
from pandas import DataFrame as DataFrame, isna as isna
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.errors import EmptyDataError as EmptyDataError, OutOfBoundsDatetime as OutOfBoundsDatetime
from pandas.io.common import get_handle as get_handle
from pandas.io.sas._byteswap import read_double_with_byteswap as read_double_with_byteswap, read_float_with_byteswap as read_float_with_byteswap, read_uint16_with_byteswap as read_uint16_with_byteswap, read_uint32_with_byteswap as read_uint32_with_byteswap, read_uint64_with_byteswap as read_uint64_with_byteswap
from pandas.io.sas._sas import Parser as Parser, get_subheader_index as get_subheader_index
from pandas.io.sas.sasreader import ReaderBase as ReaderBase

class _Column:
    col_id: int
    name: str | bytes
    label: str | bytes
    format: str | bytes
    ctype: bytes
    length: int
    def __init__(self, col_id: int, name: str | bytes, label: str | bytes, format: str | bytes, ctype: bytes, length: int) -> None: ...

class SAS7BDATReader(ReaderBase, abc.Iterator):
    """
    Read SAS files in SAS7BDAT format.

    Parameters
    ----------
    path_or_buf : path name or buffer
        Name of SAS file or file-like object pointing to SAS file
        contents.
    index : column identifier, defaults to None
        Column to use as index.
    convert_dates : bool, defaults to True
        Attempt to convert dates to Pandas datetime values.  Note that
        some rarely used SAS date formats may be unsupported.
    blank_missing : bool, defaults to True
        Convert empty strings to missing values (SAS uses blanks to
        indicate missing character variables).
    chunksize : int, defaults to None
        Return SAS7BDATReader object for iterations, returns chunks
        with given number of lines.
    encoding : str, 'infer', defaults to None
        String encoding acc. to Python standard encodings,
        encoding='infer' tries to detect the encoding from the file header,
        encoding=None will leave the data in binary format.
    convert_text : bool, defaults to True
        If False, text variables are left as raw bytes.
    convert_header_text : bool, defaults to True
        If False, header text, including column names, are left as raw
        bytes.
    """
    index: Incomplete
    convert_dates: Incomplete
    blank_missing: Incomplete
    chunksize: Incomplete
    encoding: Incomplete
    convert_text: Incomplete
    convert_header_text: Incomplete
    default_encoding: str
    compression: bytes
    column_names_raw: Incomplete
    column_names: Incomplete
    column_formats: Incomplete
    columns: Incomplete
    handles: Incomplete
    def __init__(self, path_or_buf: FilePath | ReadBuffer[bytes], index: Incomplete | None = None, convert_dates: bool = True, blank_missing: bool = True, chunksize: int | None = None, encoding: str | None = None, convert_text: bool = True, convert_header_text: bool = True, compression: CompressionOptions = 'infer') -> None: ...
    def column_data_lengths(self) -> np.ndarray:
        """Return a numpy int64 array of the column data lengths"""
    def column_data_offsets(self) -> np.ndarray:
        """Return a numpy int64 array of the column offsets"""
    def column_types(self) -> np.ndarray:
        """
        Returns a numpy character array of the column types:
           s (string) or d (double)
        """
    def close(self) -> None: ...
    def __next__(self) -> DataFrame: ...
    def read(self, nrows: int | None = None) -> DataFrame: ...
