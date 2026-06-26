from _typeshed import Incomplete
from collections.abc import Hashable, Iterable
from datetime import date, datetime, timedelta
from matplotlib.colors import Colormap, Normalize
from numpy import ndarray
from pandas import DataFrame, Index, Series, Timedelta, Timestamp
from typing import Any, Dict, List, Mapping, Tuple

ColumnName = str | bytes | date | datetime | timedelta | bool | complex | Timestamp | Timedelta
Vector = Series | Index | ndarray
VariableSpec = ColumnName | Vector | None
VariableSpecList = List[VariableSpec] | Index | None
DataSource = DataFrame | Mapping[Hashable, Vector] | None
OrderSpec = Iterable | None
NormSpec = Tuple[float | None, float | None] | Normalize | None
PaletteSpec = str | list | dict | Colormap | None
DiscreteValueSpec = dict | list | None
ContinuousValueSpec = Tuple[float, float] | List[float] | Dict[Any, float] | None

class Default: ...

default: Incomplete
