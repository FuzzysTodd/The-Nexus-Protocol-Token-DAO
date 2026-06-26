from _typeshed import Incomplete
from plotly import exceptions as exceptions, optional_imports as optional_imports
from plotly.figure_factory import utils as utils
from plotly.graph_objs import graph_objs as graph_objs

np: Incomplete
pd: Incomplete
scipy: Incomplete
scipy_stats: Incomplete
DEFAULT_HISTNORM: str
ALTERNATIVE_HISTNORM: str

def validate_distplot(hist_data, curve_type) -> None:
    """
    Distplot-specific validations

    :raises: (PlotlyError) If hist_data is not a list of lists
    :raises: (PlotlyError) If curve_type is not valid (i.e. not 'kde' or
        'normal').
    """
def create_distplot(hist_data, group_labels, bin_size: float = 1.0, curve_type: str = 'kde', colors: Incomplete | None = None, rug_text: Incomplete | None = None, histnorm=..., show_hist: bool = True, show_curve: bool = True, show_rug: bool = True):
    '''
    Function that creates a distplot similar to seaborn.distplot;
    **this function is deprecated**, use instead :mod:`plotly.express`
    functions, for example

    >>> import plotly.express as px
    >>> tips = px.data.tips()
    >>> fig = px.histogram(tips, x="total_bill", y="tip", color="sex", marginal="rug",
    ...                    hover_data=tips.columns)
    >>> fig.show()


    The distplot can be composed of all or any combination of the following
    3 components: (1) histogram, (2) curve: (a) kernel density estimation
    or (b) normal curve, and (3) rug plot. Additionally, multiple distplots
    (from multiple datasets) can be created in the same plot.

    :param (list[list]) hist_data: Use list of lists to plot multiple data
        sets on the same plot.
    :param (list[str]) group_labels: Names for each data set.
    :param (list[float]|float) bin_size: Size of histogram bins.
        Default = 1.
    :param (str) curve_type: \'kde\' or \'normal\'. Default = \'kde\'
    :param (str) histnorm: \'probability density\' or \'probability\'
        Default = \'probability density\'
    :param (bool) show_hist: Add histogram to distplot? Default = True
    :param (bool) show_curve: Add curve to distplot? Default = True
    :param (bool) show_rug: Add rug to distplot? Default = True
    :param (list[str]) colors: Colors for traces.
    :param (list[list]) rug_text: Hovertext values for rug_plot,
    :return (dict): Representation of a distplot figure.

    Example 1: Simple distplot of 1 data set

    >>> from plotly.figure_factory import create_distplot

    >>> hist_data = [[1.1, 1.1, 2.5, 3.0, 3.5,
    ...               3.5, 4.1, 4.4, 4.5, 4.5,
    ...               5.0, 5.0, 5.2, 5.5, 5.5,
    ...               5.5, 5.5, 5.5, 6.1, 7.0]]
    >>> group_labels = [\'distplot example\']
    >>> fig = create_distplot(hist_data, group_labels)
    >>> fig.show()


    Example 2: Two data sets and added rug text

    >>> from plotly.figure_factory import create_distplot
    >>> # Add histogram data
    >>> hist1_x = [0.8, 1.2, 0.2, 0.6, 1.6,
    ...            -0.9, -0.07, 1.95, 0.9, -0.2,
    ...            -0.5, 0.3, 0.4, -0.37, 0.6]
    >>> hist2_x = [0.8, 1.5, 1.5, 0.6, 0.59,
    ...            1.0, 0.8, 1.7, 0.5, 0.8,
    ...            -0.3, 1.2, 0.56, 0.3, 2.2]

    >>> # Group data together
    >>> hist_data = [hist1_x, hist2_x]

    >>> group_labels = [\'2012\', \'2013\']

    >>> # Add text
    >>> rug_text_1 = [\'a1\', \'b1\', \'c1\', \'d1\', \'e1\',
    ...       \'f1\', \'g1\', \'h1\', \'i1\', \'j1\',
    ...       \'k1\', \'l1\', \'m1\', \'n1\', \'o1\']

    >>> rug_text_2 = [\'a2\', \'b2\', \'c2\', \'d2\', \'e2\',
    ...       \'f2\', \'g2\', \'h2\', \'i2\', \'j2\',
    ...       \'k2\', \'l2\', \'m2\', \'n2\', \'o2\']

    >>> # Group text together
    >>> rug_text_all = [rug_text_1, rug_text_2]

    >>> # Create distplot
    >>> fig = create_distplot(
    ...     hist_data, group_labels, rug_text=rug_text_all, bin_size=.2)

    >>> # Add title
    >>> fig.update_layout(title=\'Dist Plot\') # doctest: +SKIP
    >>> fig.show()


    Example 3: Plot with normal curve and hide rug plot

    >>> from plotly.figure_factory import create_distplot
    >>> import numpy as np

    >>> x1 = np.random.randn(190)
    >>> x2 = np.random.randn(200)+1
    >>> x3 = np.random.randn(200)-1
    >>> x4 = np.random.randn(210)+2

    >>> hist_data = [x1, x2, x3, x4]
    >>> group_labels = [\'2012\', \'2013\', \'2014\', \'2015\']

    >>> fig = create_distplot(
    ...     hist_data, group_labels, curve_type=\'normal\',
    ...     show_rug=False, bin_size=.4)


    Example 4: Distplot with Pandas

    >>> from plotly.figure_factory import create_distplot
    >>> import numpy as np
    >>> import pandas as pd

    >>> df = pd.DataFrame({\'2012\': np.random.randn(200),
    ...                    \'2013\': np.random.randn(200)+1})
    >>> fig = create_distplot([df[c] for c in df.columns], df.columns)
    >>> fig.show()
    '''

class _Distplot:
    """
    Refer to TraceFactory.create_distplot() for docstring
    """
    hist_data: Incomplete
    histnorm: Incomplete
    group_labels: Incomplete
    bin_size: Incomplete
    show_hist: Incomplete
    show_curve: Incomplete
    trace_number: Incomplete
    rug_text: Incomplete
    start: Incomplete
    end: Incomplete
    colors: Incomplete
    curve_x: Incomplete
    curve_y: Incomplete
    def __init__(self, hist_data, histnorm, group_labels, bin_size, curve_type, colors, rug_text, show_hist, show_curve) -> None: ...
    def make_hist(self):
        """
        Makes the histogram(s) for FigureFactory.create_distplot().

        :rtype (list) hist: list of histogram representations
        """
    def make_kde(self):
        """
        Makes the kernel density estimation(s) for create_distplot().

        This is called when curve_type = 'kde' in create_distplot().

        :rtype (list) curve: list of kde representations
        """
    def make_normal(self):
        """
        Makes the normal curve(s) for create_distplot().

        This is called when curve_type = 'normal' in create_distplot().

        :rtype (list) curve: list of normal curve representations
        """
    def make_rug(self):
        """
        Makes the rug plot(s) for create_distplot().

        :rtype (list) rug: list of rug plot representations
        """
