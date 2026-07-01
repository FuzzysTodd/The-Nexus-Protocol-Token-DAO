from ._chart import ChartBase as ChartBase
from .axis import ChartLines as ChartLines, NumericAxis as NumericAxis, SeriesAxis as SeriesAxis, TextAxis as TextAxis
from .descriptors import NestedGapAmount as NestedGapAmount
from .label import DataLabelList as DataLabelList
from .series import Series as Series
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, Sequence as Sequence, Set as Set, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedMinMax as NestedMinMax, NestedSet as NestedSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class _AreaChartBase(ChartBase):
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    dropLines: Incomplete
    __elements__: Incomplete
    def __init__(self, grouping: str = 'standard', varyColors: Incomplete | None = None, ser=(), dLbls: Incomplete | None = None, dropLines: Incomplete | None = None) -> None: ...

class AreaChart(_AreaChartBase):
    tagname: str
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, axId: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...

class AreaChart3D(AreaChart):
    tagname: str
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    gapDepth: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    z_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, gapDepth: Incomplete | None = None, **kw) -> None: ...
