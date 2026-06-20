from ._chart import ChartBase as ChartBase
from .axis import NumericAxis as NumericAxis, TextAxis as TextAxis
from .label import DataLabelList as DataLabelList
from .series import XYSeries as XYSeries
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedNoneSet as NestedNoneSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class ScatterChart(ChartBase):
    tagname: str
    scatterStyle: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, scatterStyle: Incomplete | None = None, varyColors: Incomplete | None = None, ser=(), dLbls: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...
