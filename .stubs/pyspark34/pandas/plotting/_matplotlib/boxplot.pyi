from _typeshed import Incomplete
from matplotlib.axes import Axes as Axes
from matplotlib.lines import Line2D as Line2D
from pandas._typing import MatplotlibColor as MatplotlibColor
from pandas.core.dtypes.common import is_dict_like as is_dict_like
from pandas.core.dtypes.missing import remove_na_arraylike as remove_na_arraylike
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.plotting._matplotlib.core import LinePlot as LinePlot, MPLPlot as MPLPlot
from pandas.plotting._matplotlib.groupby import create_iter_data_given_by as create_iter_data_given_by
from pandas.plotting._matplotlib.style import get_standard_colors as get_standard_colors
from pandas.plotting._matplotlib.tools import create_subplots as create_subplots, flatten_axes as flatten_axes, maybe_adjust_figure as maybe_adjust_figure
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Literal, NamedTuple

class BoxPlot(LinePlot):
    class BP(NamedTuple):
        ax: Axes
        lines: dict[str, list[Line2D]]
    return_type: Incomplete
    def __init__(self, data, return_type: str = 'axes', **kwargs) -> None: ...
    def maybe_color_bp(self, bp) -> None: ...
    @property
    def orientation(self) -> Literal['horizontal', 'vertical']: ...
    @property
    def result(self): ...

def boxplot(data, column: Incomplete | None = None, by: Incomplete | None = None, ax: Incomplete | None = None, fontsize: Incomplete | None = None, rot: int = 0, grid: bool = True, figsize: Incomplete | None = None, layout: Incomplete | None = None, return_type: Incomplete | None = None, **kwds): ...
def boxplot_frame(self, column: Incomplete | None = None, by: Incomplete | None = None, ax: Incomplete | None = None, fontsize: Incomplete | None = None, rot: int = 0, grid: bool = True, figsize: Incomplete | None = None, layout: Incomplete | None = None, return_type: Incomplete | None = None, **kwds): ...
def boxplot_frame_groupby(grouped, subplots: bool = True, column: Incomplete | None = None, fontsize: Incomplete | None = None, rot: int = 0, grid: bool = True, ax: Incomplete | None = None, figsize: Incomplete | None = None, layout: Incomplete | None = None, sharex: bool = False, sharey: bool = True, **kwds): ...
