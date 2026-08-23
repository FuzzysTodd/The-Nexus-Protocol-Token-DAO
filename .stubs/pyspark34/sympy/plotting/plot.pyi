from .experimental_lambdify import lambdify as lambdify, vectorized_lambdify as vectorized_lambdify
from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import Function as Function, arity as arity
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.external import import_module as import_module
from sympy.plotting.textplot import textplot as textplot
from sympy.printing.latex import latex as latex
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence as is_sequence

def unset_show() -> None:
    """
    Disable show(). For use in the tests.
    """

class Plot:
    '''The central class of the plotting module.

    Explanation
    ===========

    For interactive work the function :func:`plot()` is better suited.

    This class permits the plotting of SymPy expressions using numerous
    backends (:external:mod:`matplotlib`, textplot, the old pyglet module for SymPy, Google
    charts api, etc).

    The figure can contain an arbitrary number of plots of SymPy expressions,
    lists of coordinates of points, etc. Plot has a private attribute _series that
    contains all data series to be plotted (expressions for lines or surfaces,
    lists of points, etc (all subclasses of BaseSeries)). Those data series are
    instances of classes not imported by ``from sympy import *``.

    The customization of the figure is on two levels. Global options that
    concern the figure as a whole (e.g. title, xlabel, scale, etc) and
    per-data series options (e.g. name) and aesthetics (e.g. color, point shape,
    line type, etc.).

    The difference between options and aesthetics is that an aesthetic can be
    a function of the coordinates (or parameters in a parametric plot). The
    supported values for an aesthetic are:

    - None (the backend uses default values)
    - a constant
    - a function of one variable (the first coordinate or parameter)
    - a function of two variables (the first and second coordinate or parameters)
    - a function of three variables (only in nonparametric 3D plots)

    Their implementation depends on the backend so they may not work in some
    backends.

    If the plot is parametric and the arity of the aesthetic function permits
    it the aesthetic is calculated over parameters and not over coordinates.
    If the arity does not permit calculation over parameters the calculation is
    done over coordinates.

    Only cartesian coordinates are supported for the moment, but you can use
    the parametric plots to plot in polar, spherical and cylindrical
    coordinates.

    The arguments for the constructor Plot must be subclasses of BaseSeries.

    Any global option can be specified as a keyword argument.

    The global options for a figure are:

    - title : str
    - xlabel : str or Symbol
    - ylabel : str or Symbol
    - zlabel : str or Symbol
    - legend : bool
    - xscale : {\'linear\', \'log\'}
    - yscale : {\'linear\', \'log\'}
    - axis : bool
    - axis_center : tuple of two floats or {\'center\', \'auto\'}
    - xlim : tuple of two floats
    - ylim : tuple of two floats
    - aspect_ratio : tuple of two floats or {\'auto\'}
    - autoscale : bool
    - margin : float in [0, 1]
    - backend : {\'default\', \'matplotlib\', \'text\'} or a subclass of BaseBackend
    - size : optional tuple of two floats, (width, height); default: None

    The per data series options and aesthetics are:
    There are none in the base series. See below for options for subclasses.

    Some data series support additional aesthetics or options:

    :class:`~.LineOver1DRangeSeries`, :class:`~.Parametric2DLineSeries`, and
    :class:`~.Parametric3DLineSeries` support the following:

    Aesthetics:

    - line_color : string, or float, or function, optional
        Specifies the color for the plot, which depends on the backend being
        used.

        For example, if ``MatplotlibBackend`` is being used, then
        Matplotlib string colors are acceptable (``"red"``, ``"r"``,
        ``"cyan"``, ``"c"``, ...).
        Alternatively, we can use a float number, 0 < color < 1, wrapped in a
        string (for example, ``line_color="0.5"``) to specify grayscale colors.
        Alternatively, We can specify a function returning a single
        float value: this will be used to apply a color-loop (for example,
        ``line_color=lambda x: math.cos(x)``).

        Note that by setting line_color, it would be applied simultaneously
        to all the series.

    Options:

    - label : str
    - steps : bool
    - integers_only : bool

    :class:`~.SurfaceOver2DRangeSeries` and :class:`~.ParametricSurfaceSeries`
    support the following:

    Aesthetics:

    - surface_color : function which returns a float.
    '''
    title: Incomplete
    xlabel: Incomplete
    ylabel: Incomplete
    zlabel: Incomplete
    aspect_ratio: Incomplete
    axis_center: Incomplete
    axis: Incomplete
    xscale: Incomplete
    yscale: Incomplete
    legend: Incomplete
    autoscale: Incomplete
    margin: Incomplete
    annotations: Incomplete
    markers: Incomplete
    rectangles: Incomplete
    fill: Incomplete
    backend: Incomplete
    xlim: Incomplete
    ylim: Incomplete
    size: Incomplete
    def __init__(self, *args, title: Incomplete | None = None, xlabel: Incomplete | None = None, ylabel: Incomplete | None = None, zlabel: Incomplete | None = None, aspect_ratio: str = 'auto', xlim: Incomplete | None = None, ylim: Incomplete | None = None, axis_center: str = 'auto', axis: bool = True, xscale: str = 'linear', yscale: str = 'linear', legend: bool = False, autoscale: bool = True, margin: int = 0, annotations: Incomplete | None = None, markers: Incomplete | None = None, rectangles: Incomplete | None = None, fill: Incomplete | None = None, backend: str = 'default', size: Incomplete | None = None, **kwargs) -> None: ...
    def show(self) -> None: ...
    def save(self, path) -> None: ...
    def __getitem__(self, index): ...
    def __setitem__(self, index, *args) -> None: ...
    def __delitem__(self, index) -> None: ...
    def append(self, arg) -> None:
        """Adds an element from a plot's series to an existing plot.

        Examples
        ========

        Consider two ``Plot`` objects, ``p1`` and ``p2``. To add the
        second plot's first series object to the first, use the
        ``append`` method, like so:

        .. plot::
           :format: doctest
           :include-source: True

           >>> from sympy import symbols
           >>> from sympy.plotting import plot
           >>> x = symbols('x')
           >>> p1 = plot(x*x, show=False)
           >>> p2 = plot(x, show=False)
           >>> p1.append(p2[0])
           >>> p1
           Plot object containing:
           [0]: cartesian line: x**2 for x over (-10.0, 10.0)
           [1]: cartesian line: x for x over (-10.0, 10.0)
           >>> p1.show()

        See Also
        ========

        extend

        """
    def extend(self, arg) -> None:
        """Adds all series from another plot.

        Examples
        ========

        Consider two ``Plot`` objects, ``p1`` and ``p2``. To add the
        second plot to the first, use the ``extend`` method, like so:

        .. plot::
           :format: doctest
           :include-source: True

           >>> from sympy import symbols
           >>> from sympy.plotting import plot
           >>> x = symbols('x')
           >>> p1 = plot(x**2, show=False)
           >>> p2 = plot(x, -x, show=False)
           >>> p1.extend(p2)
           >>> p1
           Plot object containing:
           [0]: cartesian line: x**2 for x over (-10.0, 10.0)
           [1]: cartesian line: x for x over (-10.0, 10.0)
           [2]: cartesian line: -x for x over (-10.0, 10.0)
           >>> p1.show()

        """

class PlotGrid:
    """This class helps to plot subplots from already created SymPy plots
    in a single figure.

    Examples
    ========

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> from sympy import symbols
        >>> from sympy.plotting import plot, plot3d, PlotGrid
        >>> x, y = symbols('x, y')
        >>> p1 = plot(x, x**2, x**3, (x, -5, 5))
        >>> p2 = plot((x**2, (x, -6, 6)), (x, (x, -5, 5)))
        >>> p3 = plot(x**3, (x, -5, 5))
        >>> p4 = plot3d(x*y, (x, -5, 5), (y, -5, 5))

    Plotting vertically in a single line:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(2, 1, p1, p2)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x for x over (-5.0, 5.0)
        [1]: cartesian line: x**2 for x over (-5.0, 5.0)
        [2]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)

    Plotting horizontally in a single line:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(1, 3, p2, p3, p4)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[2]:Plot object containing:
        [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)

    Plotting in a grid form:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(2, 2, p1, p2, p3, p4)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x for x over (-5.0, 5.0)
        [1]: cartesian line: x**2 for x over (-5.0, 5.0)
        [2]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)
        Plot[2]:Plot object containing:
        [0]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[3]:Plot object containing:
        [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)

    """
    nrows: Incomplete
    ncolumns: Incomplete
    args: Incomplete
    backend: Incomplete
    size: Incomplete
    def __init__(self, nrows, ncolumns, *args, show: bool = True, size: Incomplete | None = None, **kwargs) -> None:
        """
        Parameters
        ==========

        nrows :
            The number of rows that should be in the grid of the
            required subplot.
        ncolumns :
            The number of columns that should be in the grid
            of the required subplot.

        nrows and ncolumns together define the required grid.

        Arguments
        =========

        A list of predefined plot objects entered in a row-wise sequence
        i.e. plot objects which are to be in the top row of the required
        grid are written first, then the second row objects and so on

        Keyword arguments
        =================

        show : Boolean
            The default value is set to ``True``. Set show to ``False`` and
            the function will not display the subplot. The returned instance
            of the ``PlotGrid`` class can then be used to save or display the
            plot by calling the ``save()`` and ``show()`` methods
            respectively.
        size : (float, float), optional
            A tuple in the form (width, height) in inches to specify the size of
            the overall figure. The default value is set to ``None``, meaning
            the size will be set by the default backend.
        """
    def show(self) -> None: ...
    def save(self, path) -> None: ...

class BaseSeries:
    """Base class for the data objects containing stuff to be plotted.

    Explanation
    ===========

    The backend should check if it supports the data series that is given.
    (e.g. TextBackend supports only LineOver1DRangeSeries).
    It is the backend responsibility to know how to use the class of
    data series that is given.

    Some data series classes are grouped (using a class attribute like is_2Dline)
    according to the api they present (based only on convention). The backend is
    not obliged to use that api (e.g. LineOver1DRangeSeries belongs to the
    is_2Dline group and presents the get_points method, but the
    TextBackend does not use the get_points method).
    """
    is_2Dline: bool
    is_3Dline: bool
    is_3Dsurface: bool
    is_contour: bool
    is_implicit: bool
    is_parametric: bool
    def __init__(self) -> None: ...
    @property
    def is_3D(self): ...
    @property
    def is_line(self): ...

class Line2DBaseSeries(BaseSeries):
    """A base class for 2D lines.

    - adding the label, steps and only_integers options
    - making is_2Dline true
    - defining get_segments and get_color_array
    """
    is_2Dline: bool
    label: Incomplete
    steps: bool
    only_integers: bool
    line_color: Incomplete
    def __init__(self) -> None: ...
    def get_data(self):
        """ Return lists of coordinates for plotting the line.

        Returns
        =======
            x : list
                List of x-coordinates

            y : list
                List of y-coordinates

            z : list
                List of z-coordinates in case of Parametric3DLineSeries
        """
    def get_segments(self): ...
    def get_color_array(self): ...

class List2DSeries(Line2DBaseSeries):
    """Representation for a line consisting of list of points."""
    list_x: Incomplete
    list_y: Incomplete
    label: str
    def __init__(self, list_x, list_y) -> None: ...
    def get_points(self): ...

class LineOver1DRangeSeries(Line2DBaseSeries):
    """Representation for a line consisting of a SymPy expression over a range."""
    expr: Incomplete
    label: Incomplete
    var: Incomplete
    start: Incomplete
    end: Incomplete
    nb_of_points: Incomplete
    adaptive: Incomplete
    depth: Incomplete
    line_color: Incomplete
    xscale: Incomplete
    def __init__(self, expr, var_start_end, **kwargs) -> None: ...
    def get_points(self):
        """ Return lists of coordinates for plotting. Depending on the
        ``adaptive`` option, this function will either use an adaptive algorithm
        or it will uniformly sample the expression over the provided range.

        Returns
        =======
            x : list
                List of x-coordinates

            y : list
                List of y-coordinates


        Explanation
        ===========

        The adaptive sampling is done by recursively checking if three
        points are almost collinear. If they are not collinear, then more
        points are added between those points.

        References
        ==========

        .. [1] Adaptive polygonal approximation of parametric curves,
               Luiz Henrique de Figueiredo.

        """

class Parametric2DLineSeries(Line2DBaseSeries):
    """Representation for a line consisting of two parametric SymPy expressions
    over a range."""
    is_parametric: bool
    expr_x: Incomplete
    expr_y: Incomplete
    label: Incomplete
    var: Incomplete
    start: Incomplete
    end: Incomplete
    nb_of_points: Incomplete
    adaptive: Incomplete
    depth: Incomplete
    line_color: Incomplete
    def __init__(self, expr_x, expr_y, var_start_end, **kwargs) -> None: ...
    def get_parameter_points(self): ...
    def get_points(self):
        """ Return lists of coordinates for plotting. Depending on the
        ``adaptive`` option, this function will either use an adaptive algorithm
        or it will uniformly sample the expression over the provided range.

        Returns
        =======
            x : list
                List of x-coordinates

            y : list
                List of y-coordinates


        Explanation
        ===========

        The adaptive sampling is done by recursively checking if three
        points are almost collinear. If they are not collinear, then more
        points are added between those points.

        References
        ==========

        .. [1] Adaptive polygonal approximation of parametric curves,
            Luiz Henrique de Figueiredo.

        """

class Line3DBaseSeries(Line2DBaseSeries):
    """A base class for 3D lines.

    Most of the stuff is derived from Line2DBaseSeries."""
    is_2Dline: bool
    is_3Dline: bool
    def __init__(self) -> None: ...

class Parametric3DLineSeries(Line3DBaseSeries):
    """Representation for a 3D line consisting of three parametric SymPy
    expressions and a range."""
    is_parametric: bool
    expr_x: Incomplete
    expr_y: Incomplete
    expr_z: Incomplete
    label: Incomplete
    var: Incomplete
    start: Incomplete
    end: Incomplete
    nb_of_points: Incomplete
    line_color: Incomplete
    def __init__(self, expr_x, expr_y, expr_z, var_start_end, **kwargs) -> None: ...
    def get_parameter_points(self): ...
    def get_points(self): ...

class SurfaceBaseSeries(BaseSeries):
    """A base class for 3D surfaces."""
    is_3Dsurface: bool
    surface_color: Incomplete
    def __init__(self) -> None: ...
    def get_color_array(self): ...

class SurfaceOver2DRangeSeries(SurfaceBaseSeries):
    """Representation for a 3D surface consisting of a SymPy expression and 2D
    range."""
    expr: Incomplete
    var_x: Incomplete
    start_x: Incomplete
    end_x: Incomplete
    var_y: Incomplete
    start_y: Incomplete
    end_y: Incomplete
    nb_of_points_x: Incomplete
    nb_of_points_y: Incomplete
    surface_color: Incomplete
    def __init__(self, expr, var_start_end_x, var_start_end_y, **kwargs) -> None: ...
    def get_meshes(self): ...

class ParametricSurfaceSeries(SurfaceBaseSeries):
    """Representation for a 3D surface consisting of three parametric SymPy
    expressions and a range."""
    is_parametric: bool
    expr_x: Incomplete
    expr_y: Incomplete
    expr_z: Incomplete
    var_u: Incomplete
    start_u: Incomplete
    end_u: Incomplete
    var_v: Incomplete
    start_v: Incomplete
    end_v: Incomplete
    nb_of_points_u: Incomplete
    nb_of_points_v: Incomplete
    surface_color: Incomplete
    def __init__(self, expr_x, expr_y, expr_z, var_start_end_u, var_start_end_v, **kwargs) -> None: ...
    def get_parameter_meshes(self): ...
    def get_meshes(self): ...

class ContourSeries(BaseSeries):
    """Representation for a contour plot."""
    is_contour: bool
    nb_of_points_x: int
    nb_of_points_y: int
    expr: Incomplete
    var_x: Incomplete
    start_x: Incomplete
    end_x: Incomplete
    var_y: Incomplete
    start_y: Incomplete
    end_y: Incomplete
    get_points: Incomplete
    def __init__(self, expr, var_start_end_x, var_start_end_y) -> None: ...
    def get_meshes(self): ...

class BaseBackend:
    '''Base class for all backends. A backend represents the plotting library,
    which implements the necessary functionalities in order to use SymPy
    plotting functions.

    How the plotting module works:

    1. Whenever a plotting function is called, the provided expressions are
        processed and a list of instances of the :class:`BaseSeries` class is
        created, containing the necessary information to plot the expressions
        (e.g. the expression, ranges, series name, ...). Eventually, these
        objects will generate the numerical data to be plotted.
    2. A :class:`~.Plot` object is instantiated, which stores the list of
        series and the main attributes of the plot (e.g. axis labels, title, ...).
    3. When the ``show`` command is executed, a new backend is instantiated,
        which loops through each series object to generate and plot the
        numerical data. The backend is also going to set the axis labels, title,
        ..., according to the values stored in the Plot instance.

    The backend should check if it supports the data series that it is given
    (e.g. :class:`TextBackend` supports only :class:`LineOver1DRangeSeries`).

    It is the backend responsibility to know how to use the class of data series
    that it\'s given. Note that the current implementation of the ``*Series``
    classes is "matplotlib-centric": the numerical data returned by the
    ``get_points`` and ``get_meshes`` methods is meant to be used directly by
    Matplotlib. Therefore, the new backend will have to pre-process the
    numerical data to make it compatible with the chosen plotting library.
    Keep in mind that future SymPy versions may improve the ``*Series`` classes
    in order to return numerical data "non-matplotlib-centric", hence if you code
    a new backend you have the responsibility to check if its working on each
    SymPy release.

    Please explore the :class:`MatplotlibBackend` source code to understand how a
    backend should be coded.

    Methods
    =======

    In order to be used by SymPy plotting functions, a backend must implement
    the following methods:

    * show(self): used to loop over the data series, generate the numerical
        data, plot it and set the axis labels, title, ...
    * save(self, path): used to save the current plot to the specified file
        path.
    * close(self): used to close the current plot backend (note: some plotting
        library does not support this functionality. In that case, just raise a
        warning).

    See also
    ========

    MatplotlibBackend
    '''
    parent: Incomplete
    def __init__(self, parent) -> None: ...
    def show(self) -> None: ...
    def save(self, path) -> None: ...
    def close(self) -> None: ...

class MatplotlibBackend(BaseBackend):
    """ This class implements the functionalities to use Matplotlib with SymPy
    plotting functions.
    """
    matplotlib: Incomplete
    plt: Incomplete
    cm: Incomplete
    LineCollection: Incomplete
    ax: Incomplete
    fig: Incomplete
    def __init__(self, parent) -> None: ...
    @staticmethod
    def get_segments(x, y, z: Incomplete | None = None):
        """ Convert two list of coordinates to a list of segments to be used
        with Matplotlib's :external:class:`~matplotlib.collections.LineCollection`.

        Parameters
        ==========
            x : list
                List of x-coordinates

            y : list
                List of y-coordinates

            z : list
                List of z-coordinates for a 3D line.
        """
    def process_series(self) -> None:
        """
        Iterates over every ``Plot`` object and further calls
        _process_series()
        """
    def show(self) -> None: ...
    def save(self, path) -> None: ...
    def close(self) -> None: ...

class TextBackend(BaseBackend):
    def __init__(self, parent) -> None: ...
    def show(self) -> None: ...
    def close(self) -> None: ...

class DefaultBackend(BaseBackend):
    def __new__(cls, parent): ...

plot_backends: Incomplete

def centers_of_segments(array): ...
def centers_of_faces(array): ...
def flat(x, y, z, eps: float = 0.001):
    """Checks whether three points are almost collinear"""
def plot(*args, show: bool = True, **kwargs):
    """Plots a function of a single variable as a curve.

    Parameters
    ==========

    args :
        The first argument is the expression representing the function
        of single variable to be plotted.

        The last argument is a 3-tuple denoting the range of the free
        variable. e.g. ``(x, 0, 5)``

        Typical usage examples are in the following:

        - Plotting a single expression with a single range.
            ``plot(expr, range, **kwargs)``
        - Plotting a single expression with the default range (-10, 10).
            ``plot(expr, **kwargs)``
        - Plotting multiple expressions with a single range.
            ``plot(expr1, expr2, ..., range, **kwargs)``
        - Plotting multiple expressions with multiple ranges.
            ``plot((expr1, range1), (expr2, range2), ..., **kwargs)``

        It is best practice to specify range explicitly because default
        range may change in the future if a more advanced default range
        detection algorithm is implemented.

    show : bool, optional
        The default value is set to ``True``. Set show to ``False`` and
        the function will not display the plot. The returned instance of
        the ``Plot`` class can then be used to save or display the plot
        by calling the ``save()`` and ``show()`` methods respectively.

    line_color : string, or float, or function, optional
        Specifies the color for the plot.
        See ``Plot`` to see how to set color for the plots.
        Note that by setting ``line_color``, it would be applied simultaneously
        to all the series.

    title : str, optional
        Title of the plot. It is set to the latex representation of
        the expression, if the plot has only one expression.

    label : str, optional
        The label of the expression in the plot. It will be used when
        called with ``legend``. Default is the name of the expression.
        e.g. ``sin(x)``

    xlabel : str or expression, optional
        Label for the x-axis.

    ylabel : str or expression, optional
        Label for the y-axis.

    xscale : 'linear' or 'log', optional
        Sets the scaling of the x-axis.

    yscale : 'linear' or 'log', optional
        Sets the scaling of the y-axis.

    axis_center : (float, float), optional
        Tuple of two floats denoting the coordinates of the center or
        {'center', 'auto'}

    xlim : (float, float), optional
        Denotes the x-axis limits, ``(min, max)```.

    ylim : (float, float), optional
        Denotes the y-axis limits, ``(min, max)```.

    annotations : list, optional
        A list of dictionaries specifying the type of annotation
        required. The keys in the dictionary should be equivalent
        to the arguments of the :external:mod:`matplotlib`'s
        :external:meth:`~matplotlib.axes.Axes.annotate` method.

    markers : list, optional
        A list of dictionaries specifying the type the markers required.
        The keys in the dictionary should be equivalent to the arguments
        of the :external:mod:`matplotlib`'s :external:func:`~matplotlib.pyplot.plot()` function
        along with the marker related keyworded arguments.

    rectangles : list, optional
        A list of dictionaries specifying the dimensions of the
        rectangles to be plotted. The keys in the dictionary should be
        equivalent to the arguments of the :external:mod:`matplotlib`'s
        :external:class:`~matplotlib.patches.Rectangle` class.

    fill : dict, optional
        A dictionary specifying the type of color filling required in
        the plot. The keys in the dictionary should be equivalent to the
        arguments of the :external:mod:`matplotlib`'s
        :external:meth:`~matplotlib.axes.Axes.fill_between` method.

    adaptive : bool, optional
        The default value is set to ``True``. Set adaptive to ``False``
        and specify ``nb_of_points`` if uniform sampling is required.

        The plotting uses an adaptive algorithm which samples
        recursively to accurately plot. The adaptive algorithm uses a
        random point near the midpoint of two points that has to be
        further sampled. Hence the same plots can appear slightly
        different.

    depth : int, optional
        Recursion depth of the adaptive algorithm. A depth of value
        `n` samples a maximum of `2^{n}` points.

        If the ``adaptive`` flag is set to ``False``, this will be
        ignored.

    nb_of_points : int, optional
        Used when the ``adaptive`` is set to ``False``. The function
        is uniformly sampled at ``nb_of_points`` number of points.

        If the ``adaptive`` flag is set to ``True``, this will be
        ignored.

    size : (float, float), optional
        A tuple in the form (width, height) in inches to specify the size of
        the overall figure. The default value is set to ``None``, meaning
        the size will be set by the default backend.

    Examples
    ========

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> from sympy import symbols
       >>> from sympy.plotting import plot
       >>> x = symbols('x')

    Single Plot

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot(x**2, (x, -5, 5))
       Plot object containing:
       [0]: cartesian line: x**2 for x over (-5.0, 5.0)

    Multiple plots with single range.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot(x, x**2, x**3, (x, -5, 5))
       Plot object containing:
       [0]: cartesian line: x for x over (-5.0, 5.0)
       [1]: cartesian line: x**2 for x over (-5.0, 5.0)
       [2]: cartesian line: x**3 for x over (-5.0, 5.0)

    Multiple plots with different ranges.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot((x**2, (x, -6, 6)), (x, (x, -5, 5)))
       Plot object containing:
       [0]: cartesian line: x**2 for x over (-6.0, 6.0)
       [1]: cartesian line: x for x over (-5.0, 5.0)

    No adaptive sampling.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot(x**2, adaptive=False, nb_of_points=400)
       Plot object containing:
       [0]: cartesian line: x**2 for x over (-10.0, 10.0)

    See Also
    ========

    Plot, LineOver1DRangeSeries

    """
def plot_parametric(*args, show: bool = True, **kwargs):
    """
    Plots a 2D parametric curve.

    Parameters
    ==========

    args
        Common specifications are:

        - Plotting a single parametric curve with a range
            ``plot_parametric((expr_x, expr_y), range)``
        - Plotting multiple parametric curves with the same range
            ``plot_parametric((expr_x, expr_y), ..., range)``
        - Plotting multiple parametric curves with different ranges
            ``plot_parametric((expr_x, expr_y, range), ...)``

        ``expr_x`` is the expression representing $x$ component of the
        parametric function.

        ``expr_y`` is the expression representing $y$ component of the
        parametric function.

        ``range`` is a 3-tuple denoting the parameter symbol, start and
        stop. For example, ``(u, 0, 5)``.

        If the range is not specified, then a default range of (-10, 10)
        is used.

        However, if the arguments are specified as
        ``(expr_x, expr_y, range), ...``, you must specify the ranges
        for each expressions manually.

        Default range may change in the future if a more advanced
        algorithm is implemented.

    adaptive : bool, optional
        Specifies whether to use the adaptive sampling or not.

        The default value is set to ``True``. Set adaptive to ``False``
        and specify ``nb_of_points`` if uniform sampling is required.

    depth :  int, optional
        The recursion depth of the adaptive algorithm. A depth of
        value $n$ samples a maximum of $2^n$ points.

    nb_of_points : int, optional
        Used when the ``adaptive`` flag is set to ``False``.

        Specifies the number of the points used for the uniform
        sampling.

    line_color : string, or float, or function, optional
        Specifies the color for the plot.
        See ``Plot`` to see how to set color for the plots.
        Note that by setting ``line_color``, it would be applied simultaneously
        to all the series.

    label : str, optional
        The label of the expression in the plot. It will be used when
        called with ``legend``. Default is the name of the expression.
        e.g. ``sin(x)``

    xlabel : str, optional
        Label for the x-axis.

    ylabel : str, optional
        Label for the y-axis.

    xscale : 'linear' or 'log', optional
        Sets the scaling of the x-axis.

    yscale : 'linear' or 'log', optional
        Sets the scaling of the y-axis.

    axis_center : (float, float), optional
        Tuple of two floats denoting the coordinates of the center or
        {'center', 'auto'}

    xlim : (float, float), optional
        Denotes the x-axis limits, ``(min, max)```.

    ylim : (float, float), optional
        Denotes the y-axis limits, ``(min, max)```.

    size : (float, float), optional
        A tuple in the form (width, height) in inches to specify the size of
        the overall figure. The default value is set to ``None``, meaning
        the size will be set by the default backend.

    Examples
    ========

    .. plot::
       :context: reset
       :format: doctest
       :include-source: True

       >>> from sympy import plot_parametric, symbols, cos, sin
       >>> u = symbols('u')

    A parametric plot with a single expression:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot_parametric((cos(u), sin(u)), (u, -5, 5))
       Plot object containing:
       [0]: parametric cartesian line: (cos(u), sin(u)) for u over (-5.0, 5.0)

    A parametric plot with multiple expressions with the same range:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot_parametric((cos(u), sin(u)), (u, cos(u)), (u, -10, 10))
       Plot object containing:
       [0]: parametric cartesian line: (cos(u), sin(u)) for u over (-10.0, 10.0)
       [1]: parametric cartesian line: (u, cos(u)) for u over (-10.0, 10.0)

    A parametric plot with multiple expressions with different ranges
    for each curve:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot_parametric((cos(u), sin(u), (u, -5, 5)),
       ...     (cos(u), u, (u, -5, 5)))
       Plot object containing:
       [0]: parametric cartesian line: (cos(u), sin(u)) for u over (-5.0, 5.0)
       [1]: parametric cartesian line: (cos(u), u) for u over (-5.0, 5.0)

    Notes
    =====

    The plotting uses an adaptive algorithm which samples recursively to
    accurately plot the curve. The adaptive algorithm uses a random point
    near the midpoint of two points that has to be further sampled.
    Hence, repeating the same plot command can give slightly different
    results because of the random sampling.

    If there are multiple plots, then the same optional arguments are
    applied to all the plots drawn in the same canvas. If you want to
    set these options separately, you can index the returned ``Plot``
    object and set it.

    For example, when you specify ``line_color`` once, it would be
    applied simultaneously to both series.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> from sympy import pi
        >>> expr1 = (u, cos(2*pi*u)/2 + 1/2)
        >>> expr2 = (u, sin(2*pi*u)/2 + 1/2)
        >>> p = plot_parametric(expr1, expr2, (u, 0, 1), line_color='blue')

    If you want to specify the line color for the specific series, you
    should index each item and apply the property manually.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> p[0].line_color = 'red'
        >>> p.show()

    See Also
    ========

    Plot, Parametric2DLineSeries
    """
def plot3d_parametric_line(*args, show: bool = True, **kwargs):
    """
    Plots a 3D parametric line plot.

    Usage
    =====

    Single plot:

    ``plot3d_parametric_line(expr_x, expr_y, expr_z, range, **kwargs)``

    If the range is not specified, then a default range of (-10, 10) is used.

    Multiple plots.

    ``plot3d_parametric_line((expr_x, expr_y, expr_z, range), ..., **kwargs)``

    Ranges have to be specified for every expression.

    Default range may change in the future if a more advanced default range
    detection algorithm is implemented.

    Arguments
    =========

    expr_x : Expression representing the function along x.

    expr_y : Expression representing the function along y.

    expr_z : Expression representing the function along z.

    range : (:class:`~.Symbol`, float, float)
        A 3-tuple denoting the range of the parameter variable, e.g., (u, 0, 5).

    Keyword Arguments
    =================

    Arguments for ``Parametric3DLineSeries`` class.

    nb_of_points : The range is uniformly sampled at ``nb_of_points``
    number of points.

    Aesthetics:

    line_color : string, or float, or function, optional
        Specifies the color for the plot.
        See ``Plot`` to see how to set color for the plots.
        Note that by setting ``line_color``, it would be applied simultaneously
        to all the series.

    label : str
        The label to the plot. It will be used when called with ``legend=True``
        to denote the function with the given label in the plot.

    If there are multiple plots, then the same series arguments are applied to
    all the plots. If you want to set these options separately, you can index
    the returned ``Plot`` object and set it.

    Arguments for ``Plot`` class.

    title : str
        Title of the plot.

    size : (float, float), optional
        A tuple in the form (width, height) in inches to specify the size of
        the overall figure. The default value is set to ``None``, meaning
        the size will be set by the default backend.

    Examples
    ========

    .. plot::
       :context: reset
       :format: doctest
       :include-source: True

       >>> from sympy import symbols, cos, sin
       >>> from sympy.plotting import plot3d_parametric_line
       >>> u = symbols('u')

    Single plot.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot3d_parametric_line(cos(u), sin(u), u, (u, -5, 5))
       Plot object containing:
       [0]: 3D parametric cartesian line: (cos(u), sin(u), u) for u over (-5.0, 5.0)


    Multiple plots.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot3d_parametric_line((cos(u), sin(u), u, (u, -5, 5)),
       ...     (sin(u), u**2, u, (u, -5, 5)))
       Plot object containing:
       [0]: 3D parametric cartesian line: (cos(u), sin(u), u) for u over (-5.0, 5.0)
       [1]: 3D parametric cartesian line: (sin(u), u**2, u) for u over (-5.0, 5.0)


    See Also
    ========

    Plot, Parametric3DLineSeries

    """
def plot3d(*args, show: bool = True, **kwargs):
    """
    Plots a 3D surface plot.

    Usage
    =====

    Single plot

    ``plot3d(expr, range_x, range_y, **kwargs)``

    If the ranges are not specified, then a default range of (-10, 10) is used.

    Multiple plot with the same range.

    ``plot3d(expr1, expr2, range_x, range_y, **kwargs)``

    If the ranges are not specified, then a default range of (-10, 10) is used.

    Multiple plots with different ranges.

    ``plot3d((expr1, range_x, range_y), (expr2, range_x, range_y), ..., **kwargs)``

    Ranges have to be specified for every expression.

    Default range may change in the future if a more advanced default range
    detection algorithm is implemented.

    Arguments
    =========

    expr : Expression representing the function along x.

    range_x : (:class:`~.Symbol`, float, float)
        A 3-tuple denoting the range of the x variable, e.g. (x, 0, 5).

    range_y : (:class:`~.Symbol`, float, float)
        A 3-tuple denoting the range of the y variable, e.g. (y, 0, 5).

    Keyword Arguments
    =================

    Arguments for ``SurfaceOver2DRangeSeries`` class:

    nb_of_points_x : int
        The x range is sampled uniformly at ``nb_of_points_x`` of points.

    nb_of_points_y : int
        The y range is sampled uniformly at ``nb_of_points_y`` of points.

    Aesthetics:

    surface_color : Function which returns a float
        Specifies the color for the surface of the plot.
        See :class:`~.Plot` for more details.

    If there are multiple plots, then the same series arguments are applied to
    all the plots. If you want to set these options separately, you can index
    the returned ``Plot`` object and set it.

    Arguments for ``Plot`` class:

    title : str
        Title of the plot.

    size : (float, float), optional
        A tuple in the form (width, height) in inches to specify the size of the
        overall figure. The default value is set to ``None``, meaning the size will
        be set by the default backend.

    Examples
    ========

    .. plot::
       :context: reset
       :format: doctest
       :include-source: True

       >>> from sympy import symbols
       >>> from sympy.plotting import plot3d
       >>> x, y = symbols('x y')

    Single plot

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot3d(x*y, (x, -5, 5), (y, -5, 5))
       Plot object containing:
       [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)


    Multiple plots with same range

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot3d(x*y, -x*y, (x, -5, 5), (y, -5, 5))
       Plot object containing:
       [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)
       [1]: cartesian surface: -x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)


    Multiple plots with different ranges.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot3d((x**2 + y**2, (x, -5, 5), (y, -5, 5)),
       ...     (x*y, (x, -3, 3), (y, -3, 3)))
       Plot object containing:
       [0]: cartesian surface: x**2 + y**2 for x over (-5.0, 5.0) and y over (-5.0, 5.0)
       [1]: cartesian surface: x*y for x over (-3.0, 3.0) and y over (-3.0, 3.0)


    See Also
    ========

    Plot, SurfaceOver2DRangeSeries

    """
def plot3d_parametric_surface(*args, show: bool = True, **kwargs):
    """
    Plots a 3D parametric surface plot.

    Explanation
    ===========

    Single plot.

    ``plot3d_parametric_surface(expr_x, expr_y, expr_z, range_u, range_v, **kwargs)``

    If the ranges is not specified, then a default range of (-10, 10) is used.

    Multiple plots.

    ``plot3d_parametric_surface((expr_x, expr_y, expr_z, range_u, range_v), ..., **kwargs)``

    Ranges have to be specified for every expression.

    Default range may change in the future if a more advanced default range
    detection algorithm is implemented.

    Arguments
    =========

    expr_x : Expression representing the function along ``x``.

    expr_y : Expression representing the function along ``y``.

    expr_z : Expression representing the function along ``z``.

    range_u : (:class:`~.Symbol`, float, float)
        A 3-tuple denoting the range of the u variable, e.g. (u, 0, 5).

    range_v : (:class:`~.Symbol`, float, float)
        A 3-tuple denoting the range of the v variable, e.g. (v, 0, 5).

    Keyword Arguments
    =================

    Arguments for ``ParametricSurfaceSeries`` class:

    nb_of_points_u : int
        The ``u`` range is sampled uniformly at ``nb_of_points_v`` of points

    nb_of_points_y : int
        The ``v`` range is sampled uniformly at ``nb_of_points_y`` of points

    Aesthetics:

    surface_color : Function which returns a float
        Specifies the color for the surface of the plot. See
        :class:`~Plot` for more details.

    If there are multiple plots, then the same series arguments are applied for
    all the plots. If you want to set these options separately, you can index
    the returned ``Plot`` object and set it.


    Arguments for ``Plot`` class:

    title : str
        Title of the plot.

    size : (float, float), optional
        A tuple in the form (width, height) in inches to specify the size of the
        overall figure. The default value is set to ``None``, meaning the size will
        be set by the default backend.

    Examples
    ========

    .. plot::
       :context: reset
       :format: doctest
       :include-source: True

       >>> from sympy import symbols, cos, sin
       >>> from sympy.plotting import plot3d_parametric_surface
       >>> u, v = symbols('u v')

    Single plot.

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

       >>> plot3d_parametric_surface(cos(u + v), sin(u - v), u - v,
       ...     (u, -5, 5), (v, -5, 5))
       Plot object containing:
       [0]: parametric cartesian surface: (cos(u + v), sin(u - v), u - v) for u over (-5.0, 5.0) and v over (-5.0, 5.0)


    See Also
    ========

    Plot, ParametricSurfaceSeries

    """
def plot_contour(*args, show: bool = True, **kwargs):
    """
    Draws contour plot of a function

    Usage
    =====

    Single plot

    ``plot_contour(expr, range_x, range_y, **kwargs)``

    If the ranges are not specified, then a default range of (-10, 10) is used.

    Multiple plot with the same range.

    ``plot_contour(expr1, expr2, range_x, range_y, **kwargs)``

    If the ranges are not specified, then a default range of (-10, 10) is used.

    Multiple plots with different ranges.

    ``plot_contour((expr1, range_x, range_y), (expr2, range_x, range_y), ..., **kwargs)``

    Ranges have to be specified for every expression.

    Default range may change in the future if a more advanced default range
    detection algorithm is implemented.

    Arguments
    =========

    expr : Expression representing the function along x.

    range_x : (:class:`Symbol`, float, float)
        A 3-tuple denoting the range of the x variable, e.g. (x, 0, 5).

    range_y : (:class:`Symbol`, float, float)
        A 3-tuple denoting the range of the y variable, e.g. (y, 0, 5).

    Keyword Arguments
    =================

    Arguments for ``ContourSeries`` class:

    nb_of_points_x : int
        The x range is sampled uniformly at ``nb_of_points_x`` of points.

    nb_of_points_y : int
        The y range is sampled uniformly at ``nb_of_points_y`` of points.

    Aesthetics:

    surface_color : Function which returns a float
        Specifies the color for the surface of the plot. See
        :class:`sympy.plotting.Plot` for more details.

    If there are multiple plots, then the same series arguments are applied to
    all the plots. If you want to set these options separately, you can index
    the returned ``Plot`` object and set it.

    Arguments for ``Plot`` class:

    title : str
        Title of the plot.

    size : (float, float), optional
        A tuple in the form (width, height) in inches to specify the size of
        the overall figure. The default value is set to ``None``, meaning
        the size will be set by the default backend.

    See Also
    ========

    Plot, ContourSeries

    """
def check_arguments(args, expr_len, nb_of_free_symbols):
    """
    Checks the arguments and converts into tuples of the
    form (exprs, ranges).

    Examples
    ========

    .. plot::
       :context: reset
       :format: doctest
       :include-source: True

       >>> from sympy import cos, sin, symbols
       >>> from sympy.plotting.plot import check_arguments
       >>> x = symbols('x')
       >>> check_arguments([cos(x), sin(x)], 2, 1)
           [(cos(x), sin(x), (x, -10, 10))]

       >>> check_arguments([x, x**2], 1, 1)
           [(x, (x, -10, 10)), (x**2, (x, -10, 10))]
    """
