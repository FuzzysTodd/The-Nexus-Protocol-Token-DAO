from ._chart import ChartBase as ChartBase
from .axis import ChartLines as ChartLines, NumericAxis as NumericAxis, TextAxis as TextAxis
from .label import DataLabelList as DataLabelList
from .series import Series as Series
from .updown_bars import UpDownBars as UpDownBars
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class StockChart(ChartBase):
    tagname: str
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    dropLines: Incomplete
    hiLowLines: Incomplete
    upDownBars: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, ser=(), dLbls: Incomplete | None = None, dropLines: Incomplete | None = None, hiLowLines: Incomplete | None = None, upDownBars: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...
