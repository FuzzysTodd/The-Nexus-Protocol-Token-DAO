from . import axislines as axislines, grid_helper_curvelinear as grid_helper_curvelinear
from .axis_artist import AxisArtist as AxisArtist
from .grid_finder import ExtremeFinderSimple as ExtremeFinderSimple
from _typeshed import Incomplete

class FloatingAxisArtistHelper(grid_helper_curvelinear.FloatingAxisArtistHelper): ...

class FixedAxisArtistHelper(grid_helper_curvelinear.FloatingAxisArtistHelper):
    nth_coord_ticks: Incomplete
    value: Incomplete
    grid_helper: Incomplete
    def __init__(self, grid_helper, side, nth_coord_ticks: Incomplete | None = None) -> None:
        """
        nth_coord = along which coordinate value varies.
         nth_coord = 0 ->  x axis, nth_coord = 1 -> y axis
        """
    def update_lim(self, axes) -> None: ...
    def get_tick_iterators(self, axes):
        """tick_loc, tick_angle, tick_label, (optionally) tick_label"""
    def get_line(self, axes): ...

class ExtremeFinderFixed(ExtremeFinderSimple):
    def __init__(self, extremes) -> None:
        """
        This subclass always returns the same bounding box.

        Parameters
        ----------
        extremes : (float, float, float, float)
            The bounding box that this helper always returns.
        """
    def __call__(self, transform_xy, x1, y1, x2, y2): ...

class GridHelperCurveLinear(grid_helper_curvelinear.GridHelperCurveLinear):
    def __init__(self, aux_trans, extremes, grid_locator1: Incomplete | None = None, grid_locator2: Incomplete | None = None, tick_formatter1: Incomplete | None = None, tick_formatter2: Incomplete | None = None) -> None: ...
    def get_data_boundary(self, side):
        """
        Return v=0, nth=1.
        """
    def new_fixed_axis(self, loc, nth_coord: Incomplete | None = None, axis_direction: Incomplete | None = None, offset: Incomplete | None = None, axes: Incomplete | None = None): ...
    def get_gridlines(self, which: str = 'major', axis: str = 'both'): ...

class FloatingAxesBase:
    def __init__(self, *args, grid_helper, **kwargs) -> None: ...
    def clear(self) -> None: ...
    def adjust_axes_lim(self) -> None: ...

floatingaxes_class_factory: Incomplete
FloatingAxes: Incomplete
FloatingSubplot = FloatingAxes
