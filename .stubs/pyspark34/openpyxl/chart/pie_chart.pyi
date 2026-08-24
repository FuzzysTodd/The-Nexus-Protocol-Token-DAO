from ._chart import ChartBase as ChartBase
from .axis import ChartLines as ChartLines
from .descriptors import NestedGapAmount as NestedGapAmount
from .label import DataLabelList as DataLabelList
from .series import Series as Series
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Float as Float, Integer as Integer, MinMax as MinMax, NoneSet as NoneSet, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList, Percentage as Percentage
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedFloat as NestedFloat, NestedInteger as NestedInteger, NestedMinMax as NestedMinMax, NestedNoneSet as NestedNoneSet, NestedSet as NestedSet
from openpyxl.descriptors.sequence import ValueSequence as ValueSequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class _PieChartBase(ChartBase):
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dataLabels: Incomplete
    __elements__: Incomplete
    def __init__(self, varyColors: bool = True, ser=(), dLbls: Incomplete | None = None) -> None: ...

class PieChart(_PieChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    firstSliceAng: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, firstSliceAng: int = 0, extLst: Incomplete | None = None, **kw) -> None: ...

class PieChart3D(_PieChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    extLst: Incomplete
    __elements__: Incomplete

class DoughnutChart(_PieChartBase):
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    firstSliceAng: Incomplete
    holeSize: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, firstSliceAng: int = 0, holeSize: int = 10, extLst: Incomplete | None = None, **kw) -> None: ...

class CustomSplit(Serialisable):
    tagname: str
    secondPiePt: Incomplete
    __elements__: Incomplete
    def __init__(self, secondPiePt=()) -> None: ...

class ProjectedPieChart(_PieChartBase):
    """
    From the spec 21.2.2.126

    This element contains the pie of pie or bar of pie series on this
    chart. Only the first series shall be displayed. The splitType element
    shall determine whether the splitPos and custSplit elements apply.
    """
    tagname: str
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    ofPieType: Incomplete
    type: Incomplete
    gapWidth: Incomplete
    splitType: Incomplete
    splitPos: Incomplete
    custSplit: Incomplete
    secondPieSize: Incomplete
    serLines: Incomplete
    join_lines: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, ofPieType: str = 'pie', gapWidth: Incomplete | None = None, splitType: str = 'auto', splitPos: Incomplete | None = None, custSplit: Incomplete | None = None, secondPieSize: int = 75, serLines: Incomplete | None = None, extLst: Incomplete | None = None, **kw) -> None: ...
