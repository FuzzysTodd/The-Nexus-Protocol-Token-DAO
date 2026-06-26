from _typeshed import Incomplete
from types import TracebackType
from typing import Any, Callable, Dict, List, Mapping, TYPE_CHECKING as TYPE_CHECKING, Tuple, Type

MYPY = TYPE_CHECKING
ExcInfo = Tuple[Type[BaseException] | None, BaseException | None, TracebackType | None]
Event = Dict[str, Any]
Hint = Dict[str, Any]
Breadcrumb = Dict[str, Any]
BreadcrumbHint = Dict[str, Any]
SamplingContext = Dict[str, Any]
EventProcessor = Callable[[Event, Hint], Event | None]
ErrorProcessor = Callable[[Event, ExcInfo], Event | None]
BreadcrumbProcessor = Callable[[Breadcrumb, BreadcrumbHint], Breadcrumb | None]
TransactionProcessor = Callable[[Event, Hint], Event | None]
TracesSampler = Callable[[SamplingContext], float | int | bool]
NotImplementedType = Any
EventDataCategory: Incomplete
SessionStatus: Incomplete
EndpointType: Incomplete
DurationUnit: Incomplete
InformationUnit: Incomplete
FractionUnit: Incomplete
MeasurementUnit = DurationUnit | InformationUnit | FractionUnit | str
ProfilerMode: Incomplete
MetricType: Incomplete
MetricValue = int | float | str
MetricTagsInternal = Tuple[Tuple[str, str], ...]
MetricTagValue = str | int | float | None | List[int | str | float | None] | Tuple[int | str | float | None, ...]
MetricTags = Mapping[str, MetricTagValue]
FlushedMetricValue = int | float
BucketKey = Tuple[MetricType, str, MeasurementUnit, MetricTagsInternal]
