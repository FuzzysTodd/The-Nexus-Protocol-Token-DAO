from ._chart import ChartBase as ChartBase
from .axis import NumericAxis as NumericAxis, TextAxis as TextAxis
from .label import DataLabelList as DataLabelList
from .series import Series as Series
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedInteger as NestedInteger, NestedSet as NestedSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class RadarChart(ChartBase):
    tagname: str
    radarStyle: Incomplete
    type: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, radarStyle: str = 'standard', varyColors: Incomplete | None = None, ser=(), dLbls: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...
