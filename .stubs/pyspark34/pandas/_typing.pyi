import numpy as np
from _typeshed import Incomplete
from datetime import datetime, tzinfo
from pandas import Interval as Interval
from pandas._libs import NaTType as NaTType, Period as Period, Timedelta as Timedelta, Timestamp as Timestamp
from pandas._libs.tslibs import BaseOffset as BaseOffset
from pandas.arrays import DatetimeArray as DatetimeArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import DataFrameGroupBy as DataFrameGroupBy, GroupBy as GroupBy, SeriesGroupBy as SeriesGroupBy
from pandas.core.indexes.base import Index as Index
from pandas.core.internals import ArrayManager as ArrayManager, BlockManager as BlockManager, SingleArrayManager as SingleArrayManager, SingleBlockManager as SingleBlockManager
from pandas.core.resample import Resampler as Resampler
from pandas.core.series import Series as Series
from pandas.core.window.rolling import BaseWindow as BaseWindow
from pandas.io.formats.format import EngFormatter as EngFormatter
from typing import Any, Callable, Dict, Hashable, Iterator, List, Mapping, Protocol, Sequence, Tuple, Type as type_t, TypeVar

ScalarLike_co = int | float | complex | str | bytes | np.generic
NumpyValueArrayLike: Incomplete
NumpySorter: Incomplete
HashableT = TypeVar('HashableT', bound=Hashable)
ArrayLike: Incomplete
AnyArrayLike: Incomplete
TimeArrayLike: Incomplete
PythonScalar = str | float | bool
DatetimeLikeScalar: Incomplete
PandasScalar: Incomplete
Scalar = PythonScalar | PandasScalar | np.datetime64 | np.timedelta64 | datetime
IntStrT = TypeVar('IntStrT', int, str)
TimestampConvertibleTypes: Incomplete
TimedeltaConvertibleTypes: Incomplete
Timezone = str | tzinfo
NDFrameT = TypeVar('NDFrameT', bound='NDFrame')
NumpyIndexT = TypeVar('NumpyIndexT', np.ndarray, 'Index')
AxisInt = int
Axis: Incomplete
IndexLabel = Hashable | Sequence[Hashable]
Level = Hashable
Shape = Tuple[int, ...]
Suffixes = Tuple[str | None, str | None]
Ordered = bool | None
JSONSerializable = PythonScalar | List | Dict | None
Frequency: Incomplete
Axes = AnyArrayLike | List | range
RandomState: Incomplete
NpDtype = str | np.dtype | type_t[str | complex | bool | object]
Dtype: Incomplete
AstypeArg: Incomplete
DtypeArg = Dtype | Dict[Hashable, Dtype]
DtypeObj: Incomplete
ConvertersArg = Dict[Hashable, Callable[[Dtype], Dtype]]
ParseDatesArg = bool | List[Hashable] | List[List[Hashable]] | Dict[Hashable, List[Hashable]]
Renamer = Mapping[Any, Hashable] | Callable[[Any], Hashable]
T = TypeVar('T')
FuncType = Callable[..., Any]
F = TypeVar('F', bound=FuncType)
ValueKeyFunc: Incomplete
IndexKeyFunc: Incomplete
AggFuncTypeBase = Callable | str
AggFuncTypeDict = Dict[Hashable, AggFuncTypeBase | List[AggFuncTypeBase]]
AggFuncType = AggFuncTypeBase | List[AggFuncTypeBase] | AggFuncTypeDict
AggObjType: Incomplete
PythonFuncType = Callable[[Any], Any]
AnyStr_co = TypeVar('AnyStr_co', str, bytes, covariant=True)
AnyStr_contra = TypeVar('AnyStr_contra', str, bytes, contravariant=True)

class BaseBuffer(Protocol):
    @property
    def mode(self) -> str: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...

class ReadBuffer(BaseBuffer, Protocol[AnyStr_co]):
    def read(self, __n: int = ...) -> AnyStr_co: ...

class WriteBuffer(BaseBuffer, Protocol[AnyStr_contra]):
    def write(self, __b: AnyStr_contra) -> Any: ...
    def flush(self) -> Any: ...

class ReadPickleBuffer(ReadBuffer[bytes], Protocol):
    def readline(self) -> bytes: ...

class WriteExcelBuffer(WriteBuffer[bytes], Protocol):
    def truncate(self, size: int | None = ...) -> int: ...

class ReadCsvBuffer(ReadBuffer[AnyStr_co], Protocol):
    def __iter__(self) -> Iterator[AnyStr_co]: ...
    def fileno(self) -> int: ...
    def readline(self) -> AnyStr_co: ...
    @property
    def closed(self) -> bool: ...

FilePath: Incomplete
StorageOptions = Dict[str, Any] | None
CompressionDict = Dict[str, Any]
CompressionOptions: Incomplete
FormattersType = List[Callable] | Tuple[Callable, ...] | Mapping[str | int, Callable]
ColspaceType = Mapping[Hashable, str | int]
FloatFormatType: Incomplete
ColspaceArgType = str | int | Sequence[str | int] | Mapping[Hashable, str | int]
FillnaOptions: Incomplete
Manager: Incomplete
SingleManager: Incomplete
Manager2D: Incomplete
ScalarIndexer = int | np.integer
SequenceIndexer = slice | List[int] | np.ndarray
PositionalIndexer = ScalarIndexer | SequenceIndexer
PositionalIndexerTuple = Tuple[PositionalIndexer, PositionalIndexer]
PositionalIndexer2D = PositionalIndexer | PositionalIndexerTuple
TakeIndexer: Incomplete
IgnoreRaise: Incomplete
WindowingRankType: Incomplete
CSVEngine: Incomplete
JSONEngine: Incomplete
XMLParsers: Incomplete
IntervalLeftRight: Incomplete
IntervalClosedType: Incomplete
DatetimeNaTType: Incomplete
DateTimeErrorChoices: Incomplete
SortKind: Incomplete
NaPosition: Incomplete
QuantileInterpolation: Incomplete
PlottingOrientation: Incomplete
AnyAll: Incomplete
MergeHow: Incomplete
JoinHow: Incomplete
MatplotlibColor = str | Sequence[float]
TimeGrouperOrigin: Incomplete
TimeAmbiguous: Incomplete
TimeNonexistent: Incomplete
DropKeep: Incomplete
CorrelationMethod: Incomplete
AlignJoin: Incomplete
DtypeBackend: Incomplete
