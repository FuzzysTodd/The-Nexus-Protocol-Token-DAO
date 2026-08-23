from ._chart import ChartBase as ChartBase
from .axis import NumericAxis as NumericAxis, TextAxis as TextAxis
from .label import DataLabelList as DataLabelList
from .series import XYSeries as XYSeries
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, MinMax as MinMax, Sequence as Sequence, Set as Set, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedMinMax as NestedMinMax, NestedNoneSet as NestedNoneSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class BubbleChart(ChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    bubble3D: Incomplete
    bubbleScale: Incomplete
    showNegBubbles: Incomplete
    sizeRepresents: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, varyColors: Incomplete | None = None, ser=(), dLbls: Incomplete | None = None, bubble3D: Incomplete | None = None, bubbleScale: Incomplete | None = None, showNegBubbles: Incomplete | None = None, sizeRepresents: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...
