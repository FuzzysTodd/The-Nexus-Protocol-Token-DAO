import pandas as pd
from pandas._libs.lib import infer_dtype as infer_dtype
from pandas._libs.tslibs import iNaT as iNaT
from pandas.api.types import is_categorical_dtype as is_categorical_dtype, is_string_dtype as is_string_dtype
from pandas.core.interchange.buffer import PandasBuffer as PandasBuffer
from pandas.core.interchange.dataframe_protocol import Column as Column, ColumnBuffers as ColumnBuffers, ColumnNullType as ColumnNullType, DtypeKind as DtypeKind
from pandas.core.interchange.utils import ArrowCTypes as ArrowCTypes, Endianness as Endianness, dtype_to_arrow_c_fmt as dtype_to_arrow_c_fmt
from pandas.errors import NoBufferPresent as NoBufferPresent
from pandas.util._decorators import cache_readonly as cache_readonly

class PandasColumn(Column):
    """
    A column object, with only the methods and properties required by the
    interchange protocol defined.
    A column can contain one or more chunks. Each chunk can contain up to three
    buffers - a data buffer, a mask buffer (depending on null representation),
    and an offsets buffer (if variable-size binary; e.g., variable-length
    strings).
    Note: this Column object can only be produced by ``__dataframe__``, so
          doesn't need its own version or ``__column__`` protocol.
    """
    def __init__(self, column: pd.Series, allow_copy: bool = True) -> None:
        """
        Note: doesn't deal with extension arrays yet, just assume a regular
        Series/ndarray for now.
        """
    def size(self) -> int:
        """
        Size of the column, in elements.
        """
    @property
    def offset(self) -> int:
        """
        Offset of first element. Always zero.
        """
    def dtype(self) -> tuple[DtypeKind, int, str, str]: ...
    @property
    def describe_categorical(self):
        '''
        If the dtype is categorical, there are two options:
        - There are only values in the data buffer.
        - There is a separate non-categorical Column encoding for categorical values.

        Raises TypeError if the dtype is not categorical

        Content of returned dict:
            - "is_ordered" : bool, whether the ordering of dictionary indices is
                             semantically meaningful.
            - "is_dictionary" : bool, whether a dictionary-style mapping of
                                categorical values to other objects exists
            - "categories" : Column representing the (implicit) mapping of indices to
                             category values (e.g. an array of cat1, cat2, ...).
                             None if not a dictionary-style categorical.
        '''
    @property
    def describe_null(self): ...
    def null_count(self) -> int:
        """
        Number of null elements. Should always be known.
        """
    @property
    def metadata(self) -> dict[str, pd.Index]:
        """
        Store specific metadata of the column.
        """
    def num_chunks(self) -> int:
        """
        Return the number of chunks the column consists of.
        """
    def get_chunks(self, n_chunks: int | None = None):
        """
        Return an iterator yielding the chunks.
        See `DataFrame.get_chunks` for details on ``n_chunks``.
        """
    def get_buffers(self) -> ColumnBuffers:
        '''
        Return a dictionary containing the underlying buffers.
        The returned dictionary has the following contents:
            - "data": a two-element tuple whose first element is a buffer
                      containing the data and whose second element is the data
                      buffer\'s associated dtype.
            - "validity": a two-element tuple whose first element is a buffer
                          containing mask values indicating missing data and
                          whose second element is the mask value buffer\'s
                          associated dtype. None if the null representation is
                          not a bit or byte mask.
            - "offsets": a two-element tuple whose first element is a buffer
                         containing the offset values for variable-size binary
                         data (e.g., variable-length strings) and whose second
                         element is the offsets buffer\'s associated dtype. None
                         if the data buffer does not have an associated offsets
                         buffer.
        '''
