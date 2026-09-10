from .helpers import LineKey as LineKey, PCColumn as PCColumn
from .util import Attr as Attr, Panel as Panel, coalesce as coalesce, nested_get as nested_get, nested_set as nested_set
from .validators import AGGFUNCS as AGGFUNCS, CODE_COMPARE_DIFF as CODE_COMPARE_DIFF, FONT_SIZES as FONT_SIZES, LEGEND_POSITIONS as LEGEND_POSITIONS, LINEPLOT_STYLES as LINEPLOT_STYLES, Length as Length, OneOf as OneOf, RANGEFUNCS as RANGEFUNCS, SMOOTHING_TYPES as SMOOTHING_TYPES, TypeValidator as TypeValidator
from _typeshed import Incomplete

class UnknownPanel(Panel):
    @property
    def view_type(self) -> str: ...

class LinePlot(Panel):
    title: str | None
    x: str | None
    y: list | str | None
    range_x: list | tuple
    range_y: list | tuple
    log_x: bool | None
    log_y: bool | None
    title_x: str | None
    title_y: str | None
    ignore_outliers: bool | None
    groupby: str | None
    groupby_aggfunc: str | None
    groupby_rangefunc: str | None
    smoothing_factor: float | None
    smoothing_type: str | None
    smoothing_show_original: bool | None
    max_runs_to_show: int | None
    custom_expressions: str | None
    plot_type: str | None
    font_size: str | None
    legend_position: str | None
    legend_template: str | None
    aggregate: bool | None
    xaxis_expression: str | None
    def __init__(self, title: str | None = None, x: str | None = None, y: list | str | None = None, range_x: list | tuple = (None, None), range_y: list | tuple = (None, None), log_x: bool | None = None, log_y: bool | None = None, title_x: str | None = None, title_y: str | None = None, ignore_outliers: bool | None = None, groupby: str | None = None, groupby_aggfunc: str | None = None, groupby_rangefunc: str | None = None, smoothing_factor: float | None = None, smoothing_type: str | None = None, smoothing_show_original: bool | None = None, max_runs_to_show: int | None = None, custom_expressions: str | None = None, plot_type: str | None = None, font_size: str | None = None, legend_position: str | None = None, legend_template: str | None = None, aggregate: bool | None = None, xaxis_expression: str | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self): ...

class ScatterPlot(Panel):
    title: str | None
    x: str | None
    y: str | None
    z: str | None
    range_x: list | tuple
    range_y: list | tuple
    range_z: list | tuple
    log_x: bool | None
    log_y: bool | None
    log_z: bool | None
    running_ymin: bool | None
    running_ymax: bool | None
    running_ymean: bool | None
    legend_template: str | None
    gradient: dict | None
    font_size: str | None
    regression: bool | None
    def __init__(self, title: Incomplete | None = None, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, range_x=(None, None), range_y=(None, None), range_z=(None, None), log_x: Incomplete | None = None, log_y: Incomplete | None = None, log_z: Incomplete | None = None, running_ymin: Incomplete | None = None, running_ymax: Incomplete | None = None, running_ymean: Incomplete | None = None, legend_template: Incomplete | None = None, gradient: Incomplete | None = None, font_size: Incomplete | None = None, regression: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class BarPlot(Panel):
    title: str | None
    metrics: list | str | None
    orientation: str
    range_x: list | tuple
    title_x: str | None
    title_y: str | None
    groupby: str | None
    groupby_aggfunc: str | None
    groupby_rangefunc: str | None
    max_runs_to_show: int | None
    max_bars_to_show: int | None
    custom_expressions: str | None
    legend_template: str | None
    font_size: str | None
    line_titles: dict | None
    line_colors: dict | None
    def __init__(self, title: Incomplete | None = None, metrics: Incomplete | None = None, orientation: str = 'h', range_x=(None, None), title_x: Incomplete | None = None, title_y: Incomplete | None = None, groupby: Incomplete | None = None, groupby_aggfunc: Incomplete | None = None, groupby_rangefunc: Incomplete | None = None, max_runs_to_show: Incomplete | None = None, max_bars_to_show: Incomplete | None = None, custom_expressions: Incomplete | None = None, legend_template: Incomplete | None = None, font_size: Incomplete | None = None, line_titles: Incomplete | None = None, line_colors: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class ScalarChart(Panel):
    title: str | None
    metric: str
    groupby_aggfunc: str | None
    groupby_rangefunc: str | None
    custom_expressions: str | None
    legend_template: str | None
    font_size: str | None
    def __init__(self, title: Incomplete | None = None, metric: Incomplete | None = None, groupby_aggfunc: Incomplete | None = None, groupby_rangefunc: Incomplete | None = None, custom_expressions: Incomplete | None = None, legend_template: Incomplete | None = None, font_size: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class CodeComparer(Panel):
    diff: str | None
    def __init__(self, diff: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class ParallelCoordinatesPlot(Panel):
    columns: list
    title: str | None
    gradient: list | None
    font_size: str | None
    def __init__(self, columns: Incomplete | None = None, title: Incomplete | None = None, font_size: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class ParameterImportancePlot(Panel):
    with_respect_to: str
    def __init__(self, with_respect_to: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class RunComparer(Panel):
    diff_only: Incomplete
    def __init__(self, diff_only: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class MediaBrowser(Panel):
    num_columns: int | None
    media_keys: str | None
    def __init__(self, num_columns: Incomplete | None = None, media_keys: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class MarkdownPanel(Panel):
    markdown: str | None
    def __init__(self, markdown: Incomplete | None = None, *args, **kwargs) -> None: ...
    @property
    def view_type(self) -> str: ...

class ConfusionMatrix(Panel):
    @property
    def view_type(self) -> str: ...

class DataFrames(Panel):
    @property
    def view_type(self) -> str: ...

class MultiRunTable(Panel):
    @property
    def view_type(self) -> str: ...

class Vega(Panel):
    @property
    def view_type(self) -> str: ...

class CustomChart(Panel):
    query: dict
    chart_name: str
    chart_fields: dict
    chart_strings: dict
    def __init__(self, query: Incomplete | None = None, chart_name: str = '', chart_fields: Incomplete | None = None, chart_strings: Incomplete | None = None, *args, **kwargs) -> None: ...
    @classmethod
    def from_table(cls, table_name, chart_fields: Incomplete | None = None, chart_strings: Incomplete | None = None): ...
    @property
    def view_type(self) -> str: ...

class Vega3(Panel):
    @property
    def view_type(self) -> str: ...

class WeavePanel(Panel):
    @property
    def view_type(self) -> str: ...

class WeavePanelSummaryTable(Panel):
    table_name: str | None
    def __init__(self, table_name, *args, **kwargs) -> None: ...
    @classmethod
    def from_json(cls, spec): ...
    @property
    def view_type(self) -> str: ...

class WeavePanelArtifact(Panel):
    artifact: str | None
    tab: str
    def __init__(self, artifact, tab: str = 'overview', *args, **kwargs) -> None: ...
    @classmethod
    def from_json(cls, spec): ...
    @property
    def view_type(self) -> str: ...

class WeavePanelArtifactVersionedFile(Panel):
    artifact: str
    version: str
    file: str
    def __init__(self, artifact, version, file, *args, **kwargs) -> None: ...
    @classmethod
    def from_json(cls, spec): ...
    @property
    def view_type(self) -> str: ...

panel_mapping: Incomplete
weave_panels: Incomplete
