from _typeshed import Incomplete
from collections import abc
from pandas import Index as Index, MultiIndex as MultiIndex
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, ReadCsvBuffer as ReadCsvBuffer, Scalar as Scalar
from pandas.core.dtypes.common import is_integer as is_integer
from pandas.core.dtypes.inference import is_dict_like as is_dict_like
from pandas.errors import EmptyDataError as EmptyDataError, ParserError as ParserError
from pandas.io.common import dedup_names as dedup_names, is_potential_multi_index as is_potential_multi_index
from pandas.io.parsers.base_parser import ParserBase as ParserBase, parser_defaults as parser_defaults
from typing import Hashable, IO, Literal, Mapping, Sequence

class PythonParser(ParserBase):
    data: Incomplete
    buf: Incomplete
    pos: int
    line_pos: int
    skiprows: Incomplete
    skipfunc: Incomplete
    skipfooter: Incomplete
    delimiter: Incomplete
    quotechar: Incomplete
    escapechar: Incomplete
    doublequote: Incomplete
    skipinitialspace: Incomplete
    lineterminator: Incomplete
    quoting: Incomplete
    skip_blank_lines: Incomplete
    names_passed: Incomplete
    has_index_names: bool
    verbose: Incomplete
    thousands: Incomplete
    decimal: Incomplete
    comment: Incomplete
    orig_names: Incomplete
    index_names: Incomplete
    num: Incomplete
    def __init__(self, f: ReadCsvBuffer[str] | list, **kwds) -> None:
        """
        Workhorse function for processing nested list into DataFrame
        """
    def read(self, rows: int | None = None) -> tuple[Index | None, Sequence[Hashable] | MultiIndex, Mapping[Hashable, ArrayLike]]: ...
    def get_chunk(self, size: int | None = None) -> tuple[Index | None, Sequence[Hashable] | MultiIndex, Mapping[Hashable, ArrayLike]]: ...

class FixedWidthReader(abc.Iterator):
    """
    A reader of fixed-width lines.
    """
    f: Incomplete
    buffer: Incomplete
    delimiter: Incomplete
    comment: Incomplete
    colspecs: Incomplete
    def __init__(self, f: IO[str] | ReadCsvBuffer[str], colspecs: list[tuple[int, int]] | Literal['infer'], delimiter: str | None, comment: str | None, skiprows: set[int] | None = None, infer_nrows: int = 100) -> None: ...
    def get_rows(self, infer_nrows: int, skiprows: set[int] | None = None) -> list[str]:
        """
        Read rows from self.f, skipping as specified.

        We distinguish buffer_rows (the first <= infer_nrows
        lines) from the rows returned to detect_colspecs
        because it's simpler to leave the other locations
        with skiprows logic alone than to modify them to
        deal with the fact we skipped some rows here as
        well.

        Parameters
        ----------
        infer_nrows : int
            Number of rows to read from self.f, not counting
            rows that are skipped.
        skiprows: set, optional
            Indices of rows to skip.

        Returns
        -------
        detect_rows : list of str
            A list containing the rows to read.

        """
    def detect_colspecs(self, infer_nrows: int = 100, skiprows: set[int] | None = None) -> list[tuple[int, int]]: ...
    def __next__(self) -> list[str]: ...

class FixedWidthFieldParser(PythonParser):
    """
    Specialization that Converts fixed-width fields into DataFrames.
    See PythonParser for details.
    """
    colspecs: Incomplete
    infer_nrows: Incomplete
    def __init__(self, f: ReadCsvBuffer[str], **kwds) -> None: ...

def count_empty_vals(vals) -> int: ...
