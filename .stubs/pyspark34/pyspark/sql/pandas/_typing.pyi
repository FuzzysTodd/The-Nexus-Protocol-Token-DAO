from _typeshed import Incomplete
from numpy import ndarray as NDArray
from pandas.core.frame import DataFrame as PandasDataFrame
from pandas.core.series import Series as PandasSeries
from pyspark.sql._typing import LiteralType as LiteralType
from pyspark.sql.streaming.state import GroupState as GroupState
from typing import Any, Callable, Iterable, Tuple, TypeVar
from typing_extensions import Protocol

ArrayLike = NDArray
DataFrameLike = PandasDataFrame
SeriesLike = PandasSeries
DataFrameOrSeriesLike = DataFrameLike | SeriesLike
DataFrameOrSeriesLike_ = TypeVar('DataFrameOrSeriesLike_', bound=DataFrameOrSeriesLike)
PandasScalarUDFType: Incomplete
PandasGroupedMapUDFType: Incomplete
PandasGroupedAggUDFType: Incomplete
PandasWindowAggUDFType: Incomplete
PandasScalarIterUDFType: Incomplete
PandasMapIterUDFType: Incomplete
PandasCogroupedMapUDFType: Incomplete
ArrowMapIterUDFType: Incomplete
PandasGroupedMapUDFWithStateType: Incomplete

class PandasVariadicScalarToScalarFunction(Protocol):
    def __call__(self, *_: DataFrameOrSeriesLike_) -> DataFrameOrSeriesLike_: ...
PandasScalarToScalarFunction = PandasVariadicScalarToScalarFunction | Callable[[DataFrameOrSeriesLike_], DataFrameOrSeriesLike_] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameOrSeriesLike_] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameOrSeriesLike_] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], SeriesLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], SeriesLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], SeriesLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], SeriesLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], SeriesLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], SeriesLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], SeriesLike]

class PandasVariadicScalarToStructFunction(Protocol):
    def __call__(self, *_: DataFrameOrSeriesLike_) -> DataFrameLike: ...
PandasScalarToStructFunction = PandasVariadicScalarToStructFunction | Callable[[DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike] | Callable[[DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_, DataFrameOrSeriesLike_], DataFrameLike]
PandasScalarIterFunction = Callable[[Iterable[DataFrameOrSeriesLike_]], Iterable[SeriesLike]] | Callable[[Tuple[DataFrameOrSeriesLike_, ...]], Iterable[SeriesLike]]
PandasGroupedMapFunction = Callable[[DataFrameLike], DataFrameLike] | Callable[[Any, DataFrameLike], DataFrameLike]
PandasGroupedMapFunctionWithState = Callable[[Any, Iterable[DataFrameLike], GroupState], Iterable[DataFrameLike]]

class PandasVariadicGroupedAggFunction(Protocol):
    def __call__(self, *_: SeriesLike) -> LiteralType: ...
PandasGroupedAggFunction = Callable[[SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType] | Callable[[SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike, SeriesLike], LiteralType] | PandasVariadicGroupedAggFunction
PandasMapIterFunction = Callable[[Iterable[DataFrameLike]], Iterable[DataFrameLike]]
ArrowMapIterFunction: Incomplete
PandasCogroupedMapFunction = Callable[[DataFrameLike, DataFrameLike], DataFrameLike] | Callable[[Any, DataFrameLike, DataFrameLike], DataFrameLike]
GroupedMapPandasUserDefinedFunction: Incomplete
