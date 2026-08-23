from .libmp import NoConvergence as NoConvergence
from .libmp.backend import xrange as xrange
from _typeshed import Incomplete
from colorsys import hsv_to_rgb as hsv_to_rgb

class VisualizationMethods:
    plot_ignore: Incomplete

def plot(ctx, f, xlim=[-5, 5], ylim: Incomplete | None = None, points: int = 200, file: Incomplete | None = None, dpi: Incomplete | None = None, singularities=[], axes: Incomplete | None = None) -> None:
    """
    Shows a simple 2D plot of a function `f(x)` or list of functions
    `[f_0(x), f_1(x), \\ldots, f_n(x)]` over a given interval
    specified by *xlim*. Some examples::

        plot(lambda x: exp(x)*li(x), [1, 4])
        plot([cos, sin], [-4, 4])
        plot([fresnels, fresnelc], [-4, 4])
        plot([sqrt, cbrt], [-4, 4])
        plot(lambda t: zeta(0.5+t*j), [-20, 20])
        plot([floor, ceil, abs, sign], [-5, 5])

    Points where the function raises a numerical exception or
    returns an infinite value are removed from the graph.
    Singularities can also be excluded explicitly
    as follows (useful for removing erroneous vertical lines)::

        plot(cot, ylim=[-5, 5])   # bad
        plot(cot, ylim=[-5, 5], singularities=[-pi, 0, pi])  # good

    For parts where the function assumes complex values, the
    real part is plotted with dashes and the imaginary part
    is plotted with dots.

    .. note :: This function requires matplotlib (pylab).
    """
def default_color_function(ctx, z): ...

blue_orange_colors: Incomplete

def phase_color_function(ctx, z): ...
def cplot(ctx, f, re=[-5, 5], im=[-5, 5], points: int = 2000, color: Incomplete | None = None, verbose: bool = False, file: Incomplete | None = None, dpi: Incomplete | None = None, axes: Incomplete | None = None) -> None:
    '''
    Plots the given complex-valued function *f* over a rectangular part
    of the complex plane specified by the pairs of intervals *re* and *im*.
    For example::

        cplot(lambda z: z, [-2, 2], [-10, 10])
        cplot(exp)
        cplot(zeta, [0, 1], [0, 50])

    By default, the complex argument (phase) is shown as color (hue) and
    the magnitude is show as brightness. You can also supply a
    custom color function (*color*). This function should take a
    complex number as input and return an RGB 3-tuple containing
    floats in the range 0.0-1.0.

    Alternatively, you can select a builtin color function by passing
    a string as *color*:

      * "default" - default color scheme
      * "phase" - a color scheme that only renders the phase of the function,
         with white for positive reals, black for negative reals, gold in the
         upper half plane, and blue in the lower half plane.

    To obtain a sharp image, the number of points may need to be
    increased to 100,000 or thereabout. Since evaluating the
    function that many times is likely to be slow, the \'verbose\'
    option is useful to display progress.

    .. note :: This function requires matplotlib (pylab).
    '''
def splot(ctx, f, u=[-5, 5], v=[-5, 5], points: int = 100, keep_aspect: bool = True, wireframe: bool = False, file: Incomplete | None = None, dpi: Incomplete | None = None, axes: Incomplete | None = None) -> None:
    """
    Plots the surface defined by `f`.

    If `f` returns a single component, then this plots the surface
    defined by `z = f(x,y)` over the rectangular domain with
    `x = u` and `y = v`.

    If `f` returns three components, then this plots the parametric
    surface `x, y, z = f(u,v)` over the pairs of intervals `u` and `v`.

    For example, to plot a simple function::

        >>> from mpmath import *
        >>> f = lambda x, y: sin(x+y)*cos(y)
        >>> splot(f, [-pi,pi], [-pi,pi])    # doctest: +SKIP

    Plotting a donut::

        >>> r, R = 1, 2.5
        >>> f = lambda u, v: [r*cos(u), (R+r*sin(u))*cos(v), (R+r*sin(u))*sin(v)]
        >>> splot(f, [0, 2*pi], [0, 2*pi])    # doctest: +SKIP

    .. note :: This function requires matplotlib (pylab) 0.98.5.3 or higher.
    """
