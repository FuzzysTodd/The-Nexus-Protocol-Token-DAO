from ._3d import _3DBase
from ._chart import ChartBase as ChartBase
from .axis import ChartLines as ChartLines, NumericAxis as NumericAxis, SeriesAxis as SeriesAxis, TextAxis as TextAxis
from .descriptors import NestedGapAmount as NestedGapAmount, NestedOverlap as NestedOverlap
from .label import DataLabelList as DataLabelList
from .legend import Legend as Legend
from .series import Series as Series
from .shapes import GraphicalProperties as GraphicalProperties
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedInteger as NestedInteger, NestedMinMax as NestedMinMax, NestedNoneSet as NestedNoneSet, NestedSet as NestedSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class _BarChartBase(ChartBase):
    barDir: Incomplete
    type: Incomplete
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    __elements__: Incomplete
    def __init__(self, barDir: str = 'col', grouping: str = 'clustered', varyColors: Incomplete | None = None, ser=(), dLbls: Incomplete | None = None, **kw) -> None: ...

class BarChart(_BarChartBase):
    tagname: str
    barDir: Incomplete
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    gapWidth: Incomplete
    overlap: Incomplete
    serLines: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    legend: Incomplete
    def __init__(self, gapWidth: int = 150, overlap: Incomplete | None = None, serLines: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...

class BarChart3D(_BarChartBase, _3DBase):
    tagname: str
    barDir: Incomplete
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    view3D: Incomplete
    floor: Incomplete
    sideWall: Incomplete
    backWall: Incomplete
    gapWidth: Incomplete
    gapDepth: Incomplete
    shape: Incomplete
    serLines: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    z_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, gapWidth: int = 150, gapDepth: int = 150, shape: Incomplete | None = None, serLines: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...
