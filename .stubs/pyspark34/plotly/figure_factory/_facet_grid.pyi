from _typeshed import Incomplete
from plotly import exceptions as exceptions, optional_imports as optional_imports
from plotly.figure_factory import utils as utils
from plotly.subplots import make_subplots as make_subplots

pd: Incomplete
TICK_COLOR: str
AXIS_TITLE_COLOR: str
AXIS_TITLE_SIZE: int
GRID_COLOR: str
LEGEND_COLOR: str
PLOT_BGCOLOR: str
ANNOT_RECT_COLOR: str
LEGEND_BORDER_WIDTH: int
LEGEND_ANNOT_X: float
LEGEND_ANNOT_Y: float
MAX_TICKS_PER_AXIS: int
THRES_FOR_FLIPPED_FACET_TITLES: int
GRID_WIDTH: int
VALID_TRACE_TYPES: Incomplete
CUSTOM_LABEL_ERROR: str

def create_facet_grid(df, x: Incomplete | None = None, y: Incomplete | None = None, facet_row: Incomplete | None = None, facet_col: Incomplete | None = None, color_name: Incomplete | None = None, colormap: Incomplete | None = None, color_is_cat: bool = False, facet_row_labels: Incomplete | None = None, facet_col_labels: Incomplete | None = None, height: Incomplete | None = None, width: Incomplete | None = None, trace_type: str = 'scatter', scales: str = 'fixed', dtick_x: Incomplete | None = None, dtick_y: Incomplete | None = None, show_boxes: bool = True, ggplot2: bool = False, binsize: int = 1, **kwargs):
    """
    Returns figure for facet grid; **this function is deprecated**, since
    plotly.express functions should be used instead, for example

    >>> import plotly.express as px
    >>> tips = px.data.tips()
    >>> fig = px.scatter(tips,
    ...     x='total_bill',
    ...     y='tip',
    ...     facet_row='sex',
    ...     facet_col='smoker',
    ...     color='size')


    :param (pd.DataFrame) df: the dataframe of columns for the facet grid.
    :param (str) x: the name of the dataframe column for the x axis data.
    :param (str) y: the name of the dataframe column for the y axis data.
    :param (str) facet_row: the name of the dataframe column that is used to
        facet the grid into row panels.
    :param (str) facet_col: the name of the dataframe column that is used to
        facet the grid into column panels.
    :param (str) color_name: the name of your dataframe column that will
        function as the colormap variable.
    :param (str|list|dict) colormap: the param that determines how the
        color_name column colors the data. If the dataframe contains numeric
        data, then a dictionary of colors will group the data categorically
        while a Plotly Colorscale name or a custom colorscale will treat it
        numerically. To learn more about colors and types of colormap, run
        `help(plotly.colors)`.
    :param (bool) color_is_cat: determines whether a numerical column for the
        colormap will be treated as categorical (True) or sequential (False).
            Default = False.
    :param (str|dict) facet_row_labels: set to either 'name' or a dictionary
        of all the unique values in the faceting row mapped to some text to
        show up in the label annotations. If None, labeling works like usual.
    :param (str|dict) facet_col_labels: set to either 'name' or a dictionary
        of all the values in the faceting row mapped to some text to show up
        in the label annotations. If None, labeling works like usual.
    :param (int) height: the height of the facet grid figure.
    :param (int) width: the width of the facet grid figure.
    :param (str) trace_type: decides the type of plot to appear in the
        facet grid. The options are 'scatter', 'scattergl', 'histogram',
        'bar', and 'box'.
        Default = 'scatter'.
    :param (str) scales: determines if axes have fixed ranges or not. Valid
        settings are 'fixed' (all axes fixed), 'free_x' (x axis free only),
        'free_y' (y axis free only) or 'free' (both axes free).
    :param (float) dtick_x: determines the distance between each tick on the
        x-axis. Default is None which means dtick_x is set automatically.
    :param (float) dtick_y: determines the distance between each tick on the
        y-axis. Default is None which means dtick_y is set automatically.
    :param (bool) show_boxes: draws grey boxes behind the facet titles.
    :param (bool) ggplot2: draws the facet grid in the style of `ggplot2`. See
        http://ggplot2.tidyverse.org/reference/facet_grid.html for reference.
        Default = False
    :param (int) binsize: groups all data into bins of a given length.
    :param (dict) kwargs: a dictionary of scatterplot arguments.

    Examples 1: One Way Faceting

    >>> import plotly.figure_factory as ff
    >>> import pandas as pd
    >>> mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

    >>> fig = ff.create_facet_grid(
    ...     mpg,
    ...     x='displ',
    ...     y='cty',
    ...     facet_col='cyl',
    ... )
    >>> fig.show()

    Example 2: Two Way Faceting

    >>> import plotly.figure_factory as ff

    >>> import pandas as pd

    >>> mpg = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/mpg_2017.txt')

    >>> fig = ff.create_facet_grid(
    ...     mpg,
    ...     x='displ',
    ...     y='cty',
    ...     facet_row='drv',
    ...     facet_col='cyl',
    ... )
    >>> fig.show()

    Example 3: Categorical Coloring

    >>> import plotly.figure_factory as ff
    >>> import pandas as pd
    >>> mtcars = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/mtcars.csv')
    >>> mtcars.cyl = mtcars.cyl.astype(str)
    >>> fig = ff.create_facet_grid(
    ...     mtcars,
    ...     x='mpg',
    ...     y='wt',
    ...     facet_col='cyl',
    ...     color_name='cyl',
    ...     color_is_cat=True,
    ... )
    >>> fig.show()


    """
