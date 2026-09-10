from _typeshed import Incomplete
from pandas.core.base import PandasObject
from pyspark.ml.feature import Bucketizer as Bucketizer
from pyspark.mllib.stat import KernelDensity as KernelDensity
from pyspark.pandas.config import get_option as get_option
from pyspark.pandas.missing import unsupported_function as unsupported_function
from pyspark.pandas.utils import name_like_string as name_like_string

class TopNPlotBase:
    partial: bool
    def get_top_n(self, data): ...
    def set_result_text(self, ax) -> None: ...

class SampledPlotBase:
    fraction: Incomplete
    def get_sampled(self, data): ...
    def set_result_text(self, ax) -> None: ...

class NumericPlotBase:
    @staticmethod
    def prepare_numeric_data(data): ...

class HistogramPlotBase(NumericPlotBase):
    @staticmethod
    def prepare_hist_data(data, bins): ...
    @staticmethod
    def get_bins(sdf, bins): ...
    @staticmethod
    def compute_hist(psdf, bins): ...

class BoxPlotBase:
    @staticmethod
    def compute_multicol_stats(data, colnames, whis, precision): ...
    @staticmethod
    def compute_stats(data, colname, whis, precision): ...
    @staticmethod
    def multicol_outliers(data, multicol_stats): ...
    @staticmethod
    def outliers(data, colname, lfence, ufence): ...
    @staticmethod
    def calc_multicol_whiskers(colnames, multicol_outliers): ...
    @staticmethod
    def calc_whiskers(colname, outliers): ...
    @staticmethod
    def get_fliers(colname, outliers, min_val): ...

class KdePlotBase(NumericPlotBase):
    @staticmethod
    def prepare_kde_data(data): ...
    @staticmethod
    def get_ind(sdf, ind): ...
    @staticmethod
    def compute_kde(sdf, bw_method: Incomplete | None = None, ind: Incomplete | None = None): ...

class PandasOnSparkPlotAccessor(PandasObject):
    """
    Series/Frames plotting accessor and method.

    Uses the backend specified by the
    option ``plotting.backend``. By default, plotly is used.

    Plotting methods can also be accessed by calling the accessor as a method
    with the ``kind`` argument:
    ``s.plot(kind='hist')`` is equivalent to ``s.plot.hist()``
    """
    pandas_plot_data_map: Incomplete
    data: Incomplete
    def __init__(self, data) -> None: ...
    def __call__(self, kind: str = 'line', backend: Incomplete | None = None, **kwargs): ...
    def line(self, x: Incomplete | None = None, y: Incomplete | None = None, **kwargs):
        """
        Plot DataFrame/Series as lines.

        This function is useful to plot lines using Series's values
        as coordinates.

        Parameters
        ----------
        x : int or str, optional
            Columns to use for the horizontal axis.
            Either the location or the label of the columns to be used.
            By default, it will use the DataFrame indices.
        y : int, str, or list of them, optional
            The values to be plotted.
            Either the location or the label of the columns to be used.
            By default, it will use the remaining DataFrame numeric columns.
        **kwds
            Keyword arguments to pass on to :meth:`Series.plot` or :meth:`DataFrame.plot`.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        See Also
        --------
        plotly.express.line : Plot y versus x as lines and/or markers (plotly).
        matplotlib.pyplot.plot : Plot y versus x as lines and/or markers (matplotlib).

        Examples
        --------
        Basic plot.

        For Series:

        .. plotly::

            >>> s = ps.Series([1, 3, 2])
            >>> s.plot.line()  # doctest: +SKIP

        For DataFrame:

        .. plotly::

            The following example shows the populations for some animals
            over the years.

            >>> df = ps.DataFrame({'pig': [20, 18, 489, 675, 1776],
            ...                    'horse': [4, 25, 281, 600, 1900]},
            ...                   index=[1990, 1997, 2003, 2009, 2014])
            >>> df.plot.line()  # doctest: +SKIP

        .. plotly::

            The following example shows the relationship between both
            populations.

            >>> df = ps.DataFrame({'pig': [20, 18, 489, 675, 1776],
            ...                    'horse': [4, 25, 281, 600, 1900]},
            ...                   index=[1990, 1997, 2003, 2009, 2014])
            >>> df.plot.line(x='pig', y='horse')  # doctest: +SKIP
        """
    def bar(self, x: Incomplete | None = None, y: Incomplete | None = None, **kwds):
        """
        Vertical bar plot.

        Parameters
        ----------
        x : label or position, optional
            Allows plotting of one column versus another.
            If not specified, the index of the DataFrame is used.
        y : label or position, optional
            Allows plotting of one column versus another.
            If not specified, all numerical columns are used.
        **kwds : optional
            Additional keyword arguments are documented in
            :meth:`pyspark.pandas.Series.plot` or
            :meth:`pyspark.pandas.DataFrame.plot`.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        Examples
        --------
        Basic plot.

        For Series:

        .. plotly::

            >>> s = ps.Series([1, 3, 2])
            >>> s.plot.bar()  # doctest: +SKIP

        For DataFrame:

        .. plotly::

            >>> df = ps.DataFrame({'lab': ['A', 'B', 'C'], 'val': [10, 30, 20]})
            >>> df.plot.bar(x='lab', y='val')  # doctest: +SKIP

        Plot a whole dataframe to a bar plot. Each column is stacked with a
        distinct color along the horizontal axis.

        .. plotly::

            >>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
            >>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
            >>> index = ['snail', 'pig', 'elephant',
            ...          'rabbit', 'giraffe', 'coyote', 'horse']
            >>> df = ps.DataFrame({'speed': speed,
            ...                    'lifespan': lifespan}, index=index)
            >>> df.plot.bar()  # doctest: +SKIP

        Instead of stacking, the figure can be split by column with plotly
        APIs.

        .. plotly::

            >>> from plotly.subplots import make_subplots
            >>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
            >>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
            >>> index = ['snail', 'pig', 'elephant',
            ...          'rabbit', 'giraffe', 'coyote', 'horse']
            >>> df = ps.DataFrame({'speed': speed,
            ...                    'lifespan': lifespan}, index=index)
            >>> fig = (make_subplots(rows=2, cols=1)
            ...        .add_trace(df.plot.bar(y='speed').data[0], row=1, col=1)
            ...        .add_trace(df.plot.bar(y='speed').data[0], row=1, col=1)
            ...        .add_trace(df.plot.bar(y='lifespan').data[0], row=2, col=1))
            >>> fig  # doctest: +SKIP

        Plot a single column.

        .. plotly::

            >>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
            >>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
            >>> index = ['snail', 'pig', 'elephant',
            ...          'rabbit', 'giraffe', 'coyote', 'horse']
            >>> df = ps.DataFrame({'speed': speed,
            ...                    'lifespan': lifespan}, index=index)
            >>> df.plot.bar(y='speed')  # doctest: +SKIP

        Plot only selected categories for the DataFrame.

        .. plotly::

            >>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
            >>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
            >>> index = ['snail', 'pig', 'elephant',
            ...          'rabbit', 'giraffe', 'coyote', 'horse']
            >>> df = ps.DataFrame({'speed': speed,
            ...                    'lifespan': lifespan}, index=index)
            >>> df.plot.bar(x='lifespan')  # doctest: +SKIP
        """
    def barh(self, x: Incomplete | None = None, y: Incomplete | None = None, **kwargs):
        """
        Make a horizontal bar plot.

        A horizontal bar plot is a plot that presents quantitative data with
        rectangular bars with lengths proportional to the values that they
        represent. A bar plot shows comparisons among discrete categories. One
        axis of the plot shows the specific categories being compared, and the
        other axis represents a measured value.

        Parameters
        ----------
        x : label or position, default DataFrame.index
            Column to be used for categories.
        y : label or position, default All numeric columns in dataframe
            Columns to be plotted from the DataFrame.
        **kwds
            Keyword arguments to pass on to
            :meth:`pyspark.pandas.DataFrame.plot` or :meth:`pyspark.pandas.Series.plot`.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        See Also
        --------
        plotly.express.bar : Plot a vertical bar plot using plotly.
        matplotlib.axes.Axes.bar : Plot a vertical bar plot using matplotlib.

        Examples
        --------
        For Series:

        .. plotly::

            >>> df = ps.DataFrame({'lab': ['A', 'B', 'C'], 'val': [10, 30, 20]})
            >>> df.val.plot.barh()  # doctest: +SKIP

        For DataFrame:

        .. plotly::

            >>> df = ps.DataFrame({'lab': ['A', 'B', 'C'], 'val': [10, 30, 20]})
            >>> df.plot.barh(x='lab', y='val')  # doctest: +SKIP

        Plot a whole DataFrame to a horizontal bar plot

        .. plotly::

            >>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
            >>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
            >>> index = ['snail', 'pig', 'elephant',
            ...          'rabbit', 'giraffe', 'coyote', 'horse']
            >>> df = ps.DataFrame({'speed': speed,
            ...                    'lifespan': lifespan}, index=index)
            >>> df.plot.barh()  # doctest: +SKIP

        Plot a column of the DataFrame to a horizontal bar plot

        .. plotly::

            >>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
            >>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
            >>> index = ['snail', 'pig', 'elephant',
            ...          'rabbit', 'giraffe', 'coyote', 'horse']
            >>> df = ps.DataFrame({'speed': speed,
            ...                    'lifespan': lifespan}, index=index)
            >>> df.plot.barh(y='speed')  # doctest: +SKIP

        Plot DataFrame versus the desired column

        .. plotly::

            >>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
            >>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
            >>> index = ['snail', 'pig', 'elephant',
            ...          'rabbit', 'giraffe', 'coyote', 'horse']
            >>> df = ps.DataFrame({'speed': speed,
            ...                    'lifespan': lifespan}, index=index)
            >>> df.plot.barh(x='lifespan')  # doctest: +SKIP
        """
    def box(self, **kwds):
        """
        Make a box plot of the Series columns.

        Parameters
        ----------
        **kwds : optional
            Additional keyword arguments are documented in
            :meth:`pyspark.pandas.Series.plot`.

        precision: scalar, default = 0.01
            This argument is used by pandas-on-Spark to compute approximate statistics
            for building a boxplot. Use *smaller* values to get more precise
            statistics (matplotlib-only).

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        Notes
        -----
        There are behavior differences between pandas-on-Spark and pandas.

        * pandas-on-Spark computes approximate statistics - expect differences between
          pandas and pandas-on-Spark boxplots, especially regarding 1st and 3rd quartiles.
        * The `whis` argument is only supported as a single number.
        * pandas-on-Spark doesn't support the following argument(s) (matplotlib-only).

          * `bootstrap` argument is not supported
          * `autorange` argument is not supported

        Examples
        --------
        Draw a box plot from a DataFrame with four columns of randomly
        generated data.

        For Series:

        .. plotly::

            >>> data = np.random.randn(25, 4)
            >>> df = ps.DataFrame(data, columns=list('ABCD'))
            >>> df['A'].plot.box()  # doctest: +SKIP

        This is an unsupported function for DataFrame type
        """
    def hist(self, bins: int = 10, **kwds):
        """
        Draw one histogram of the DataFrame’s columns.
        A `histogram`_ is a representation of the distribution of data.
        This function calls :meth:`plotting.backend.plot`,
        on each series in the DataFrame, resulting in one histogram per column.

        .. _histogram: https://en.wikipedia.org/wiki/Histogram

        Parameters
        ----------
        bins : integer or sequence, default 10
            Number of histogram bins to be used. If an integer is given, bins + 1
            bin edges are calculated and returned. If bins is a sequence, it gives
            bin edges, including left edge of first bin and right edge of last
            bin. In this case, bins are returned unmodified.
        **kwds
            All other plotting keyword arguments to be passed to
            plotting backend.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        Examples
        --------
        Basic plot.

        For Series:

        .. plotly::

            >>> s = ps.Series([1, 3, 2])
            >>> s.plot.hist()  # doctest: +SKIP

        For DataFrame:

        .. plotly::

            >>> df = pd.DataFrame(
            ...     np.random.randint(1, 7, 6000),
            ...     columns=['one'])
            >>> df['two'] = df['one'] + np.random.randint(1, 7, 6000)
            >>> df = ps.from_pandas(df)
            >>> df.plot.hist(bins=12, alpha=0.5)  # doctest: +SKIP
        """
    def kde(self, bw_method: Incomplete | None = None, ind: Incomplete | None = None, **kwargs):
        """
        Generate Kernel Density Estimate plot using Gaussian kernels.

        Parameters
        ----------
        bw_method : scalar
            The method used to calculate the estimator bandwidth.
            See KernelDensity in PySpark for more information.
        ind : NumPy array or integer, optional
            Evaluation points for the estimated PDF. If None (default),
            1000 equally spaced points are used. If `ind` is a NumPy array, the
            KDE is evaluated at the points passed. If `ind` is an integer,
            `ind` number of equally spaced points are used.
        **kwargs : optional
            Keyword arguments to pass on to :meth:`pandas-on-Spark.Series.plot`.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        Examples
        --------
        A scalar bandwidth should be specified. Using a small bandwidth value can
        lead to over-fitting, while using a large bandwidth value may result
        in under-fitting:

        .. plotly::

            >>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
            >>> s.plot.kde(bw_method=0.3)  # doctest: +SKIP

        .. plotly::

            >>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
            >>> s.plot.kde(bw_method=3)  # doctest: +SKIP

        The `ind` parameter determines the evaluation points for the
        plot of the estimated KDF:

        .. plotly::

            >>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
            >>> s.plot.kde(ind=[1, 2, 3, 4, 5], bw_method=0.3)  # doctest: +SKIP

        For DataFrame, it works in the same way as Series:

        .. plotly::

            >>> df = ps.DataFrame({
            ...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
            ...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
            ... })
            >>> df.plot.kde(bw_method=0.3)  # doctest: +SKIP

        .. plotly::

            >>> df = ps.DataFrame({
            ...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
            ...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
            ... })
            >>> df.plot.kde(bw_method=3)  # doctest: +SKIP

        .. plotly::

            >>> df = ps.DataFrame({
            ...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
            ...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
            ... })
            >>> df.plot.kde(ind=[1, 2, 3, 4, 5, 6], bw_method=0.3)  # doctest: +SKIP
        """
    density = kde
    def area(self, x: Incomplete | None = None, y: Incomplete | None = None, **kwds):
        """
        Draw a stacked area plot.

        An area plot displays quantitative data visually.
        This function wraps the plotly area function.

        Parameters
        ----------
        x : label or position, optional
            Coordinates for the X axis. By default it uses the index.
        y : label or position, optional
            Column to plot. By default it uses all columns.
        stacked : bool, default True
            Area plots are stacked by default. Set to False to create an
            unstacked plot (matplotlib-only).
        **kwds : optional
            Additional keyword arguments are documented in
            :meth:`DataFrame.plot`.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        Examples
        --------

        For Series

        .. plotly::

            >>> df = ps.DataFrame({
            ...     'sales': [3, 2, 3, 9, 10, 6],
            ...     'signups': [5, 5, 6, 12, 14, 13],
            ...     'visits': [20, 42, 28, 62, 81, 50],
            ... }, index=pd.date_range(start='2018/01/01', end='2018/07/01',
            ...                        freq='M'))
            >>> df.sales.plot.area()  # doctest: +SKIP

        For DataFrame

        .. plotly::

            >>> df = ps.DataFrame({
            ...     'sales': [3, 2, 3, 9, 10, 6],
            ...     'signups': [5, 5, 6, 12, 14, 13],
            ...     'visits': [20, 42, 28, 62, 81, 50],
            ... }, index=pd.date_range(start='2018/01/01', end='2018/07/01',
            ...                        freq='M'))
            >>> df.plot.area()  # doctest: +SKIP
        """
    def pie(self, **kwds):
        """
        Generate a pie plot.

        A pie plot is a proportional representation of the numerical data in a
        column. This function wraps :meth:`plotly.express.pie` for the
        specified column.

        Parameters
        ----------
        y : int or label, optional
            Label or position of the column to plot.
            If not provided, ``subplots=True`` argument must be passed (matplotlib-only).
        **kwds
            Keyword arguments to pass on to :meth:`pandas-on-Spark.Series.plot`.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        Examples
        --------

        For Series:

        .. plotly::

            >>> df = ps.DataFrame({'mass': [0.330, 4.87, 5.97],
            ...                    'radius': [2439.7, 6051.8, 6378.1]},
            ...                   index=['Mercury', 'Venus', 'Earth'])
            >>> df.mass.plot.pie()  # doctest: +SKIP


        For DataFrame:

        .. plotly::

            >>> df = ps.DataFrame({'mass': [0.330, 4.87, 5.97],
            ...                    'radius': [2439.7, 6051.8, 6378.1]},
            ...                   index=['Mercury', 'Venus', 'Earth'])
            >>> df.plot.pie(y='mass')  # doctest: +SKIP
        """
    def scatter(self, x, y, **kwds):
        '''
        Create a scatter plot with varying marker point size and color.

        The coordinates of each point are defined by two dataframe columns and
        filled circles are used to represent each point. This kind of plot is
        useful to see complex correlations between two variables. Points could
        be for instance natural 2D coordinates like longitude and latitude in
        a map or, in general, any pair of metrics that can be plotted against
        each other.

        Parameters
        ----------
        x : int or str
            The column name or column position to be used as horizontal
            coordinates for each point.
        y : int or str
            The column name or column position to be used as vertical
            coordinates for each point.
        s : scalar or array_like, optional
            (matplotlib-only).
        c : str, int or array_like, optional
            (matplotlib-only).

        **kwds: Optional
            Keyword arguments to pass on to :meth:`pyspark.pandas.DataFrame.plot`.

        Returns
        -------
        :class:`plotly.graph_objs.Figure`
            Return an custom object when ``backend!=plotly``.
            Return an ndarray when ``subplots=True`` (matplotlib-only).

        See Also
        --------
        plotly.express.scatter : Scatter plot using multiple input data
            formats (plotly).
        matplotlib.pyplot.scatter : Scatter plot using multiple input data
            formats (matplotlib).

        Examples
        --------
        Let\'s see how to draw a scatter plot using coordinates from the values
        in a DataFrame\'s columns.

        .. plotly::

            >>> df = ps.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
            ...                    [6.4, 3.2, 1], [5.9, 3.0, 2]],
            ...                   columns=[\'length\', \'width\', \'species\'])
            >>> df.plot.scatter(x=\'length\', y=\'width\')  # doctest: +SKIP

        And now with dark scheme:

        .. plotly::

            >>> df = ps.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
            ...                    [6.4, 3.2, 1], [5.9, 3.0, 2]],
            ...                   columns=[\'length\', \'width\', \'species\'])
            >>> fig = df.plot.scatter(x=\'length\', y=\'width\')
            >>> fig.update_layout(template="plotly_dark")  # doctest: +SKIP
        '''
    def hexbin(self, **kwds): ...
