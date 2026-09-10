from .experimental_lambdify import experimental_lambdify as experimental_lambdify, vectorized_lambdify as vectorized_lambdify
from .intervalmath import interval as interval
from .plot import BaseSeries as BaseSeries, Plot as Plot
from _typeshed import Incomplete
from sympy.core.containers import Tuple as Tuple
from sympy.core.relational import Eq as Eq, Equality as Equality, GreaterThan as GreaterThan, LessThan as LessThan, Relational as Relational, StrictGreaterThan as StrictGreaterThan, StrictLessThan as StrictLessThan
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.external import import_module as import_module
from sympy.logic.boolalg import BooleanFunction as BooleanFunction
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.iterables import flatten as flatten

class ImplicitSeries(BaseSeries):
    """ Representation for Implicit plot """
    is_implicit: bool
    expr: Incomplete
    label: Incomplete
    var_x: Incomplete
    start_x: Incomplete
    end_x: Incomplete
    var_y: Incomplete
    start_y: Incomplete
    end_y: Incomplete
    get_points: Incomplete
    has_equality: Incomplete
    nb_of_points: Incomplete
    use_interval_math: Incomplete
    depth: Incomplete
    line_color: Incomplete
    def __init__(self, expr, var_start_end_x, var_start_end_y, has_equality, use_interval_math, depth, nb_of_points, line_color) -> None: ...
    def get_raster(self): ...

def plot_implicit(expr, x_var: Incomplete | None = None, y_var: Incomplete | None = None, adaptive: bool = True, depth: int = 0, points: int = 300, line_color: str = 'blue', show: bool = True, **kwargs):
    '''A plot function to plot implicit equations / inequalities.

    Arguments
    =========

    - expr : The equation / inequality that is to be plotted.
    - x_var (optional) : symbol to plot on x-axis or tuple giving symbol
      and range as ``(symbol, xmin, xmax)``
    - y_var (optional) : symbol to plot on y-axis or tuple giving symbol
      and range as ``(symbol, ymin, ymax)``

    If neither ``x_var`` nor ``y_var`` are given then the free symbols in the
    expression will be assigned in the order they are sorted.

    The following keyword arguments can also be used:

    - ``adaptive`` Boolean. The default value is set to True. It has to be
        set to False if you want to use a mesh grid.

    - ``depth`` integer. The depth of recursion for adaptive mesh grid.
        Default value is 0. Takes value in the range (0, 4).

    - ``points`` integer. The number of points if adaptive mesh grid is not
        used. Default value is 300.

    - ``show`` Boolean. Default value is True. If set to False, the plot will
        not be shown. See ``Plot`` for further information.

    - ``title`` string. The title for the plot.

    - ``xlabel`` string. The label for the x-axis

    - ``ylabel`` string. The label for the y-axis

    Aesthetics options:

    - ``line_color``: float or string. Specifies the color for the plot.
        See ``Plot`` to see how to set color for the plots.
        Default value is "Blue"

    plot_implicit, by default, uses interval arithmetic to plot functions. If
    the expression cannot be plotted using interval arithmetic, it defaults to
    a generating a contour using a mesh grid of fixed number of points. By
    setting adaptive to False, you can force plot_implicit to use the mesh
    grid. The mesh grid method can be effective when adaptive plotting using
    interval arithmetic, fails to plot with small line width.

    Examples
    ========

    Plot expressions:

    .. plot::
        :context: reset
        :format: doctest
        :include-source: True

        >>> from sympy import plot_implicit, symbols, Eq, And
        >>> x, y = symbols(\'x y\')

    Without any ranges for the symbols in the expression:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p1 = plot_implicit(Eq(x**2 + y**2, 5))

    With the range for the symbols:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p2 = plot_implicit(
        ...     Eq(x**2 + y**2, 3), (x, -3, 3), (y, -3, 3))

    With depth of recursion as argument:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p3 = plot_implicit(
        ...     Eq(x**2 + y**2, 5), (x, -4, 4), (y, -4, 4), depth = 2)

    Using mesh grid and not using adaptive meshing:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p4 = plot_implicit(
        ...     Eq(x**2 + y**2, 5), (x, -5, 5), (y, -2, 2),
        ...     adaptive=False)

    Using mesh grid without using adaptive meshing with number of points
    specified:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p5 = plot_implicit(
        ...     Eq(x**2 + y**2, 5), (x, -5, 5), (y, -2, 2),
        ...     adaptive=False, points=400)

    Plotting regions:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p6 = plot_implicit(y > x**2)

    Plotting Using boolean conjunctions:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p7 = plot_implicit(And(y > x, y > -x))

    When plotting an expression with a single variable (y - 1, for example),
    specify the x or the y variable explicitly:

    .. plot::
        :context: close-figs
        :format: doctest
        :include-source: True

        >>> p8 = plot_implicit(y - 1, y_var=y)
        >>> p9 = plot_implicit(x - 1, x_var=x)
    '''
