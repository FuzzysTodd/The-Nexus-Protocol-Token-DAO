from .area_chart import AreaChart as AreaChart, AreaChart3D as AreaChart3D
from .axis import DateAxis as DateAxis, NumericAxis as NumericAxis, SeriesAxis as SeriesAxis, TextAxis as TextAxis
from .bar_chart import BarChart as BarChart, BarChart3D as BarChart3D
from .bubble_chart import BubbleChart as BubbleChart
from .layout import Layout as Layout
from .line_chart import LineChart as LineChart, LineChart3D as LineChart3D
from .pie_chart import DoughnutChart as DoughnutChart, PieChart as PieChart, PieChart3D as PieChart3D, ProjectedPieChart as ProjectedPieChart
from .radar_chart import RadarChart as RadarChart
from .scatter_chart import ScatterChart as ScatterChart
from .shapes import GraphicalProperties as GraphicalProperties
from .stock_chart import StockChart as StockChart
from .surface_chart import SurfaceChart as SurfaceChart, SurfaceChart3D as SurfaceChart3D
from .text import RichText as RichText
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool
from openpyxl.descriptors.sequence import MultiSequence as MultiSequence, MultiSequencePart as MultiSequencePart
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class DataTable(Serialisable):
    tagname: str
    showHorzBorder: Incomplete
    showVertBorder: Incomplete
    showOutline: Incomplete
    showKeys: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    txPr: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, showHorzBorder: Incomplete | None = None, showVertBorder: Incomplete | None = None, showOutline: Incomplete | None = None, showKeys: Incomplete | None = None, spPr: Incomplete | None = None, txPr: Incomplete | None = None, extLst: Incomplete | None = None) -> None: ...

class PlotArea(Serialisable):
    tagname: str
    layout: Incomplete
    dTable: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    extLst: Incomplete
    areaChart: Incomplete
    area3DChart: Incomplete
    lineChart: Incomplete
    line3DChart: Incomplete
    stockChart: Incomplete
    radarChart: Incomplete
    scatterChart: Incomplete
    pieChart: Incomplete
    pie3DChart: Incomplete
    doughnutChart: Incomplete
    barChart: Incomplete
    bar3DChart: Incomplete
    ofPieChart: Incomplete
    surfaceChart: Incomplete
    surface3DChart: Incomplete
    bubbleChart: Incomplete
    valAx: Incomplete
    catAx: Incomplete
    dateAx: Incomplete
    serAx: Incomplete
    __elements__: Incomplete
    def __init__(self, layout: Incomplete | None = None, dTable: Incomplete | None = None, spPr: Incomplete | None = None, _charts=(), _axes=(), extLst: Incomplete | None = None) -> None: ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...
    @classmethod
    def from_tree(cls, node): ...
