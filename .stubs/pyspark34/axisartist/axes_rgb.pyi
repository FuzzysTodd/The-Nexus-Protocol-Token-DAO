from .axislines import Axes as Axes
from mpl_toolkits.axes_grid1.axes_rgb import RGBAxes as _RGBAxes, make_rgb_axes as make_rgb_axes

class RGBAxes(_RGBAxes):
    """
    Subclass of `~.axes_grid1.axes_rgb.RGBAxes` with
    ``_defaultAxesClass`` = `.axislines.Axes`.
    """
