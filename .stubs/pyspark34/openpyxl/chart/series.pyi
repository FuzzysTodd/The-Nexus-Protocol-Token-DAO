from .data_source import AxDataSource as AxDataSource, NumDataSource as NumDataSource, NumRef as NumRef, StrRef as StrRef
from .error_bar import ErrorBars as ErrorBars
from .label import DataLabelList as DataLabelList
from .marker import DataPoint as DataPoint, Marker as Marker, PictureOptions as PictureOptions
from .shapes import GraphicalProperties as GraphicalProperties
from .trendline import Trendline as Trendline
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, Sequence as Sequence, String as String, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedInteger as NestedInteger, NestedNoneSet as NestedNoneSet, NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

attribute_mapping: Incomplete

class SeriesLabel(Serialisable):
    tagname: str
    strRef: Incomplete
    v: Incomplete
    value: Incomplete
    __elements__: Incomplete
    def __init__(self, strRef: Incomplete | None = None, v: Incomplete | None = None) -> None: ...

class Series(Serialisable):
    """
    Generic series object. Should not be instantiated directly.
    User the chart.Series factory instead.
    """
    tagname: str
    idx: Incomplete
    order: Incomplete
    tx: Incomplete
    title: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    pictureOptions: Incomplete
    dPt: Incomplete
    data_points: Incomplete
    dLbls: Incomplete
    labels: Incomplete
    trendline: Incomplete
    errBars: Incomplete
    cat: Incomplete
    identifiers: Incomplete
    val: Incomplete
    extLst: Incomplete
    invertIfNegative: Incomplete
    shape: Incomplete
    xVal: Incomplete
    yVal: Incomplete
    bubbleSize: Incomplete
    zVal: Incomplete
    bubble3D: Incomplete
    marker: Incomplete
    smooth: Incomplete
    explosion: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = 0, order: int = 0, tx: Incomplete | None = None, spPr: Incomplete | None = None, pictureOptions: Incomplete | None = None, dPt=(), dLbls: Incomplete | None = None, trendline: Incomplete | None = None, errBars: Incomplete | None = None, cat: Incomplete | None = None, val: Incomplete | None = None, invertIfNegative: Incomplete | None = None, shape: Incomplete | None = None, xVal: Incomplete | None = None, yVal: Incomplete | None = None, bubbleSize: Incomplete | None = None, bubble3D: Incomplete | None = None, marker: Incomplete | None = None, smooth: Incomplete | None = None, explosion: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None):
        """The index can need rebasing"""

class XYSeries(Series):
    """Dedicated series for charts that have x and y series"""
    idx: Incomplete
    order: Incomplete
    tx: Incomplete
    spPr: Incomplete
    dPt: Incomplete
    dLbls: Incomplete
    trendline: Incomplete
    errBars: Incomplete
    xVal: Incomplete
    yVal: Incomplete
    invertIfNegative: Incomplete
    bubbleSize: Incomplete
    bubble3D: Incomplete
    marker: Incomplete
    smooth: Incomplete
