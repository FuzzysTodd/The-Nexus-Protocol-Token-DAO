from _typeshed import Incomplete
from pandas.plotting._matplotlib import AreaPlot as PandasAreaPlot, BarPlot as PandasBarPlot, BarhPlot as PandasBarhPlot, BoxPlot as PandasBoxPlot, HistPlot as PandasHistPlot, KdePlot as PandasKdePlot, LinePlot as PandasLinePlot, PiePlot as PandasPiePlot, ScatterPlot as PandasScatterPlot
from pyspark.pandas.plot import BoxPlotBase as BoxPlotBase, HistogramPlotBase as HistogramPlotBase, KdePlotBase as KdePlotBase, SampledPlotBase as SampledPlotBase, TopNPlotBase as TopNPlotBase, unsupported_function as unsupported_function

class PandasOnSparkBarPlot(PandasBarPlot, TopNPlotBase):
    def __init__(self, data, **kwargs) -> None: ...

class PandasOnSparkBoxPlot(PandasBoxPlot, BoxPlotBase):
    def boxplot(self, ax, bxpstats, notch: Incomplete | None = None, sym: Incomplete | None = None, vert: Incomplete | None = None, whis: Incomplete | None = None, positions: Incomplete | None = None, widths: Incomplete | None = None, patch_artist: Incomplete | None = None, bootstrap: Incomplete | None = None, usermedians: Incomplete | None = None, conf_intervals: Incomplete | None = None, meanline: Incomplete | None = None, showmeans: Incomplete | None = None, showcaps: Incomplete | None = None, showbox: Incomplete | None = None, showfliers: Incomplete | None = None, boxprops: Incomplete | None = None, labels: Incomplete | None = None, flierprops: Incomplete | None = None, medianprops: Incomplete | None = None, meanprops: Incomplete | None = None, capprops: Incomplete | None = None, whiskerprops: Incomplete | None = None, manage_ticks: Incomplete | None = None, manage_xticks: Incomplete | None = None, autorange: bool = False, zorder: Incomplete | None = None, precision: Incomplete | None = None): ...
    @staticmethod
    def rc_defaults(notch: Incomplete | None = None, vert: Incomplete | None = None, whis: Incomplete | None = None, patch_artist: Incomplete | None = None, bootstrap: Incomplete | None = None, meanline: Incomplete | None = None, showmeans: Incomplete | None = None, showcaps: Incomplete | None = None, showbox: Incomplete | None = None, showfliers: Incomplete | None = None, **kwargs): ...

class PandasOnSparkHistPlot(PandasHistPlot, HistogramPlotBase): ...

class PandasOnSparkPiePlot(PandasPiePlot, TopNPlotBase):
    def __init__(self, data, **kwargs) -> None: ...

class PandasOnSparkAreaPlot(PandasAreaPlot, SampledPlotBase):
    def __init__(self, data, **kwargs) -> None: ...

class PandasOnSparkLinePlot(PandasLinePlot, SampledPlotBase):
    def __init__(self, data, **kwargs) -> None: ...

class PandasOnSparkBarhPlot(PandasBarhPlot, TopNPlotBase):
    def __init__(self, data, **kwargs) -> None: ...

class PandasOnSparkScatterPlot(PandasScatterPlot, TopNPlotBase):
    def __init__(self, data, x, y, **kwargs) -> None: ...

class PandasOnSparkKdePlot(PandasKdePlot, KdePlotBase): ...

def plot_pandas_on_spark(data, kind, **kwargs): ...
def plot_series(data, kind: str = 'line', ax: Incomplete | None = None, figsize: Incomplete | None = None, use_index: bool = True, title: Incomplete | None = None, grid: Incomplete | None = None, legend: bool = False, style: Incomplete | None = None, logx: bool = False, logy: bool = False, loglog: bool = False, xticks: Incomplete | None = None, yticks: Incomplete | None = None, xlim: Incomplete | None = None, ylim: Incomplete | None = None, rot: Incomplete | None = None, fontsize: Incomplete | None = None, colormap: Incomplete | None = None, table: bool = False, yerr: Incomplete | None = None, xerr: Incomplete | None = None, label: Incomplete | None = None, secondary_y: bool = False, **kwds):
    '''
    Make plots of Series using matplotlib / pylab.

    Each plot kind has a corresponding method on the
    ``Series.plot`` accessor:
    ``s.plot(kind=\'line\')`` is equivalent to
    ``s.plot.line()``.

    Parameters
    ----------
    data : Series

    kind : str
        - \'line\' : line plot (default)
        - \'bar\' : vertical bar plot
        - \'barh\' : horizontal bar plot
        - \'hist\' : histogram
        - \'box\' : boxplot
        - \'kde\' : Kernel Density Estimation plot
        - \'density\' : same as \'kde\'
        - \'area\' : area plot
        - \'pie\' : pie plot

    ax : matplotlib axes object
        If not passed, uses gca()
    figsize : a tuple (width, height) in inches
    use_index : boolean, default True
        Use index as ticks for x axis
    title : string or list
        Title to use for the plot. If a string is passed, print the string at
        the top of the figure. If a list is passed and `subplots` is True,
        print each item in the list above the corresponding subplot.
    grid : boolean, default None (matlab style default)
        Axis grid lines
    legend : False/True/\'reverse\'
        Place legend on axis subplots
    style : list or dict
        matplotlib line style per column
    logx : boolean, default False
        Use log scaling on x axis
    logy : boolean, default False
        Use log scaling on y axis
    loglog : boolean, default False
        Use log scaling on both x and y axes
    xticks : sequence
        Values to use for the xticks
    yticks : sequence
        Values to use for the yticks
    xlim : 2-tuple/list
    ylim : 2-tuple/list
    rot : int, default None
        Rotation for ticks (xticks for vertical, yticks for horizontal plots)
    fontsize : int, default None
        Font size for xticks and yticks
    colormap : str or matplotlib colormap object, default None
        Colormap to select colors from. If string, load colormap with that name
        from matplotlib.
    colorbar : boolean, optional
        If True, plot colorbar (only relevant for \'scatter\' and \'hexbin\' plots)
    position : float
        Specify relative alignments for bar plot layout.
        From 0 (left/bottom-end) to 1 (right/top-end). Default is 0.5 (center)
    table : boolean, Series or DataFrame, default False
        If True, draw a table using the data in the DataFrame and the data will
        be transposed to meet matplotlib\'s default layout.
        If a Series or DataFrame is passed, use passed data to draw a table.
    yerr : DataFrame, Series, array-like, dict and str
        See :ref:`Plotting with Error Bars <visualization.errorbars>` for
        detail.
    xerr : same types as yerr.
    label : label argument to provide to plot
    secondary_y : boolean or sequence of ints, default False
        If True then y-axis will be on the right
    mark_right : boolean, default True
        When using a secondary_y axis, automatically mark the column
        labels with "(right)" in the legend
    **kwds : keywords
        Options to pass to matplotlib plotting method

    Returns
    -------
    axes : :class:`matplotlib.axes.Axes` or numpy.ndarray of them

    Notes
    -----

    - See matplotlib documentation online for more on this subject
    - If `kind` = \'bar\' or \'barh\', you can specify relative alignments
      for bar plot layout by `position` keyword.
      From 0 (left/bottom-end) to 1 (right/top-end). Default is 0.5 (center)
    '''
def plot_frame(data, x: Incomplete | None = None, y: Incomplete | None = None, kind: str = 'line', ax: Incomplete | None = None, subplots: bool = False, sharex: Incomplete | None = None, sharey: bool = False, layout: Incomplete | None = None, figsize: Incomplete | None = None, use_index: bool = True, title: Incomplete | None = None, grid: Incomplete | None = None, legend: bool = True, style: Incomplete | None = None, logx: bool = False, logy: bool = False, loglog: bool = False, xticks: Incomplete | None = None, yticks: Incomplete | None = None, xlim: Incomplete | None = None, ylim: Incomplete | None = None, rot: Incomplete | None = None, fontsize: Incomplete | None = None, colormap: Incomplete | None = None, table: bool = False, yerr: Incomplete | None = None, xerr: Incomplete | None = None, secondary_y: bool = False, sort_columns: bool = False, **kwds):
    '''
    Make plots of DataFrames using matplotlib / pylab.

    Each plot kind has a corresponding method on the
    ``DataFrame.plot`` accessor:
    ``psdf.plot(kind=\'line\')`` is equivalent to
    ``psdf.plot.line()``.

    Parameters
    ----------
    data : DataFrame

    kind : str
        - \'line\' : line plot (default)
        - \'bar\' : vertical bar plot
        - \'barh\' : horizontal bar plot
        - \'hist\' : histogram
        - \'box\' : boxplot
        - \'kde\' : Kernel Density Estimation plot
        - \'density\' : same as \'kde\'
        - \'area\' : area plot
        - \'pie\' : pie plot
        - \'scatter\' : scatter plot
    ax : matplotlib axes object
        If not passed, uses gca()
    x : label or position, default None
    y : label, position or list of label, positions, default None
        Allows plotting of one column versus another.
    figsize : a tuple (width, height) in inches
    use_index : boolean, default True
        Use index as ticks for x axis
    title : string or list
        Title to use for the plot. If a string is passed, print the string at
        the top of the figure. If a list is passed and `subplots` is True,
        print each item in the list above the corresponding subplot.
    grid : boolean, default None (matlab style default)
        Axis grid lines
    legend : False/True/\'reverse\'
        Place legend on axis subplots
    style : list or dict
        matplotlib line style per column
    logx : boolean, default False
        Use log scaling on x axis
    logy : boolean, default False
        Use log scaling on y axis
    loglog : boolean, default False
        Use log scaling on both x and y axes
    xticks : sequence
        Values to use for the xticks
    yticks : sequence
        Values to use for the yticks
    xlim : 2-tuple/list
    ylim : 2-tuple/list
    sharex: bool or None, default is None
        Whether to share x axis or not.
    sharey: bool, default is False
        Whether to share y axis or not.
    rot : int, default None
        Rotation for ticks (xticks for vertical, yticks for horizontal plots)
    fontsize : int, default None
        Font size for xticks and yticks
    colormap : str or matplotlib colormap object, default None
        Colormap to select colors from. If string, load colormap with that name
        from matplotlib.
    colorbar : boolean, optional
        If True, plot colorbar (only relevant for \'scatter\' and \'hexbin\' plots)
    position : float
        Specify relative alignments for bar plot layout.
        From 0 (left/bottom-end) to 1 (right/top-end). Default is 0.5 (center)
    table : boolean, Series or DataFrame, default False
        If True, draw a table using the data in the DataFrame and the data will
        be transposed to meet matplotlib\'s default layout.
        If a Series or DataFrame is passed, use passed data to draw a table.
    yerr : DataFrame, Series, array-like, dict and str
        See :ref:`Plotting with Error Bars <visualization.errorbars>` for
        detail.
    xerr : same types as yerr.
    label : label argument to provide to plot
    secondary_y : boolean or sequence of ints, default False
        If True then y-axis will be on the right
    mark_right : boolean, default True
        When using a secondary_y axis, automatically mark the column
        labels with "(right)" in the legend
    sort_columns: bool, default is False
        When True, will sort values on plots.

        .. deprecated:: 3.4.0

    **kwds : keywords
        Options to pass to matplotlib plotting method

    Returns
    -------
    axes : :class:`matplotlib.axes.Axes` or numpy.ndarray of them

    Notes
    -----

    - See matplotlib documentation online for more on this subject
    - If `kind` = \'bar\' or \'barh\', you can specify relative alignments
      for bar plot layout by `position` keyword.
      From 0 (left/bottom-end) to 1 (right/top-end). Default is 0.5 (center)
    '''
