import abc
import numpy as np
from _typeshed import Incomplete
from abc import ABC
from matplotlib.artist import Artist as Artist
from matplotlib.axes import Axes as Axes
from matplotlib.axis import Axis as Axis
from pandas._typing import IndexLabel as IndexLabel, PlottingOrientation as PlottingOrientation, npt as npt
from pandas.core.dtypes.common import is_any_real_numeric_dtype as is_any_real_numeric_dtype, is_categorical_dtype as is_categorical_dtype, is_extension_array_dtype as is_extension_array_dtype, is_float as is_float, is_float_dtype as is_float_dtype, is_hashable as is_hashable, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_iterator as is_iterator, is_list_like as is_list_like, is_number as is_number, is_numeric_dtype as is_numeric_dtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCMultiIndex as ABCMultiIndex, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.frame import DataFrame as DataFrame
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.plotting._matplotlib import tools as tools
from pandas.plotting._matplotlib.converter import register_pandas_matplotlib_converters as register_pandas_matplotlib_converters
from pandas.plotting._matplotlib.groupby import reconstruct_data_with_by as reconstruct_data_with_by
from pandas.plotting._matplotlib.misc import unpack_single_str_list as unpack_single_str_list
from pandas.plotting._matplotlib.style import get_standard_colors as get_standard_colors
from pandas.plotting._matplotlib.timeseries import decorate_axes as decorate_axes, format_dateaxis as format_dateaxis, maybe_convert_index as maybe_convert_index, maybe_resample as maybe_resample, use_dynamic_x as use_dynamic_x
from pandas.plotting._matplotlib.tools import create_subplots as create_subplots, flatten_axes as flatten_axes, format_date_labels as format_date_labels, get_all_lines as get_all_lines, get_xlim as get_xlim, handle_shared_axes as handle_shared_axes
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util.version import Version as Version
from typing import Hashable, Literal, Sequence

class MPLPlot(ABC, metaclass=abc.ABCMeta):
    """
    Base class for assembling a pandas plot using matplotlib

    Parameters
    ----------
    data :

    """
    @property
    def orientation(self) -> str | None: ...
    axes: np.ndarray
    data: Incomplete
    by: Incomplete
    columns: Incomplete
    kind: Incomplete
    subplots: Incomplete
    sharex: bool
    sharey: Incomplete
    figsize: Incomplete
    layout: Incomplete
    xticks: Incomplete
    yticks: Incomplete
    xlim: Incomplete
    ylim: Incomplete
    title: Incomplete
    use_index: Incomplete
    xlabel: Incomplete
    ylabel: Incomplete
    fontsize: Incomplete
    rot: Incomplete
    grid: Incomplete
    legend: Incomplete
    legend_handles: Incomplete
    legend_labels: Incomplete
    logx: Incomplete
    logy: Incomplete
    loglog: Incomplete
    label: Incomplete
    style: Incomplete
    mark_right: Incomplete
    stacked: Incomplete
    ax: Incomplete
    fig: Incomplete
    errors: Incomplete
    secondary_y: Incomplete
    colormap: Incomplete
    table: Incomplete
    include_bool: Incomplete
    kwds: Incomplete
    def __init__(self, data, kind: Incomplete | None = None, by: IndexLabel | None = None, subplots: bool | Sequence[Sequence[str]] = False, sharex: Incomplete | None = None, sharey: bool = False, use_index: bool = True, figsize: Incomplete | None = None, grid: Incomplete | None = None, legend: bool | str = True, rot: Incomplete | None = None, ax: Incomplete | None = None, fig: Incomplete | None = None, title: Incomplete | None = None, xlim: Incomplete | None = None, ylim: Incomplete | None = None, xticks: Incomplete | None = None, yticks: Incomplete | None = None, xlabel: Hashable | None = None, ylabel: Hashable | None = None, fontsize: Incomplete | None = None, secondary_y: bool | tuple | list | np.ndarray = False, colormap: Incomplete | None = None, table: bool = False, layout: Incomplete | None = None, include_bool: bool = False, column: IndexLabel | None = None, **kwds) -> None: ...
    @property
    def nseries(self) -> int: ...
    def draw(self) -> None: ...
    def generate(self) -> None: ...
    @property
    def result(self):
        """
        Return result axes
        """
    @property
    def legend_title(self) -> str | None: ...
    def plt(self): ...
    @classmethod
    def get_default_ax(cls, ax) -> None: ...
    def on_right(self, i): ...

class PlanePlot(MPLPlot, ABC, metaclass=abc.ABCMeta):
    """
    Abstract class for plotting on plane, currently scatter and hexbin.
    """
    x: Incomplete
    y: Incomplete
    def __init__(self, data, x, y, **kwargs) -> None: ...
    @property
    def nseries(self) -> int: ...

class ScatterPlot(PlanePlot):
    c: Incomplete
    def __init__(self, data, x, y, s: Incomplete | None = None, c: Incomplete | None = None, **kwargs) -> None: ...

class HexBinPlot(PlanePlot):
    C: Incomplete
    def __init__(self, data, x, y, C: Incomplete | None = None, **kwargs) -> None: ...

class LinePlot(MPLPlot):
    @property
    def orientation(self) -> PlottingOrientation: ...
    data: Incomplete
    x_compat: Incomplete
    def __init__(self, data, **kwargs) -> None: ...

class AreaPlot(LinePlot):
    def __init__(self, data, **kwargs) -> None: ...

class BarPlot(MPLPlot):
    @property
    def orientation(self) -> PlottingOrientation: ...
    bar_width: Incomplete
    tick_pos: Incomplete
    bottom: Incomplete
    left: Incomplete
    log: Incomplete
    tickoffset: Incomplete
    lim_offset: Incomplete
    ax_pos: Incomplete
    def __init__(self, data, **kwargs) -> None: ...

class BarhPlot(BarPlot):
    @property
    def orientation(self) -> Literal['horizontal']: ...

class PiePlot(MPLPlot):
    def __init__(self, data, kind: Incomplete | None = None, **kwargs) -> None: ...
