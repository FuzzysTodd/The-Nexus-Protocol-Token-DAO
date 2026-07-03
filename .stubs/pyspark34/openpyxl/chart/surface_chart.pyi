from ._3d import _3DBase
from ._chart import ChartBase as ChartBase
from .axis import NumericAxis as NumericAxis, SeriesAxis as SeriesAxis, TextAxis as TextAxis
from .series import Series as Series
from .shapes import GraphicalProperties as GraphicalProperties
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Integer as Integer, Sequence as Sequence, Typed as Typed
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedInteger as NestedInteger
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class BandFormat(Serialisable):
    tagname: str
    idx: Incomplete
    spPr: Incomplete
    graphicalProperties: Incomplete
    __elements__: Incomplete
    def __init__(self, idx: int = 0, spPr: Incomplete | None = None) -> None: ...

class BandFormatList(Serialisable):
    tagname: str
    bandFmt: Incomplete
    __elements__: Incomplete
    def __init__(self, bandFmt=()) -> None: ...

class _SurfaceChartBase(ChartBase):
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    __elements__: Incomplete
    def __init__(self, wireframe: Incomplete | None = None, ser=(), bandFmts: Incomplete | None = None, **kw) -> None: ...

class SurfaceChart3D(_SurfaceChartBase, _3DBase):
    tagname: str
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    extLst: Incomplete
    x_axis: Incomplete
    y_axis: Incomplete
    z_axis: Incomplete
    __elements__: Incomplete
    def __init__(self, **kw) -> None: ...

class SurfaceChart(SurfaceChart3D):
    tagname: str
    wireframe: Incomplete
    ser: Incomplete
    bandFmts: Incomplete
    extLst: Incomplete
    __elements__: Incomplete
    def __init__(self, **kw) -> None: ...
