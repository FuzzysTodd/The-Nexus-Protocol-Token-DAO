from ._chart import ChartBase as ChartBase
from .axis import ChartLines as ChartLines, NumericAxis as NumericAxis, SeriesAxis as SeriesAxis, TextAxis as TextAxis
from .descriptors import NestedGapAmount as NestedGapAmount
from .label import DataLabelList as DataLabelList
from .series import Series as Series
from .updown_bars import UpDownBars as UpDownBars
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedSet as NestedSet

class _LineChartBase(ChartBase):
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    dropLines: Incomplete
    __elements__: Incomplete
    def __init__(self, grouping: str = 'standard', varyColors: Incomplete | None = None, ser=(), dLbls: Incomplete | None = None, dropLines: Incomplete | None = None, **kw) -> None: ...

class LineChart(_LineChartBase):
    tagname: str
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    hiLowLines: Incomplete
    upDownBars: Incomplete
    marker: Incomplete
    smooth: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, hiLowLines: Incomplete | None = None, upDownBars: Incomplete | None = None, marker: Incomplete | None = None, smooth: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...

class LineChart3D(_LineChartBase):
    tagname: str
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    gapDepth: Incomplete
    hiLowLines: Incomplete
    upDownBars: Incomplete
    marker: Incomplete
    smooth: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    z_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, gapDepth: Incomplete | None = None, hiLowLines: Incomplete | None = None, upDownBars: Incomplete | None = None, marker: Incomplete | None = None, smooth: Incomplete | None = None, **kw) -> None: ...
