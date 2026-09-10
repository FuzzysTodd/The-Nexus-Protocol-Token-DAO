from .axis_artist import AxisArtist as AxisArtist
from .axislines import AxisArtistHelper as AxisArtistHelper, GridHelperBase as GridHelperBase
from .grid_finder import GridFinder as GridFinder
from _typeshed import Incomplete
from collections.abc import Generator

class FixedAxisArtistHelper(AxisArtistHelper.Fixed):
    """
    Helper class for a fixed axis.
    """
    grid_helper: Incomplete
    nth_coord_ticks: Incomplete
    side: Incomplete
    def __init__(self, grid_helper, side, nth_coord_ticks: Incomplete | None = None) -> None:
        """
        nth_coord = along which coordinate value varies.
         nth_coord = 0 ->  x axis, nth_coord = 1 -> y axis
        """
    def update_lim(self, axes) -> None: ...
    def get_tick_transform(self, axes): ...
    def get_tick_iterators(self, axes):
        """tick_loc, tick_angle, tick_label"""

class FloatingAxisArtistHelper(AxisArtistHelper.Floating):
    value: Incomplete
    grid_helper: Incomplete
    def __init__(self, grid_helper, nth_coord, value, axis_direction: Incomplete | None = None) -> None:
        """
        nth_coord = along which coordinate value varies.
         nth_coord = 0 ->  x axis, nth_coord = 1 -> y axis
        """
    def set_extremes(self, e1, e2) -> None: ...
    def update_lim(self, axes) -> None: ...
    def get_axislabel_transform(self, axes): ...
    def get_axislabel_pos_angle(self, axes): ...
    def get_tick_transform(self, axes): ...
    def get_tick_iterators(self, axes):
        """tick_loc, tick_angle, tick_label, (optionally) tick_label"""
    def get_line_transform(self, axes): ...
    def get_line(self, axes): ...

class GridHelperCurveLinear(GridHelperBase):
    grid_finder: Incomplete
    def __init__(self, aux_trans, extreme_finder: Incomplete | None = None, grid_locator1: Incomplete | None = None, grid_locator2: Incomplete | None = None, tick_formatter1: Incomplete | None = None, tick_formatter2: Incomplete | None = None) -> None:
        """
        aux_trans : a transform from the source (curved) coordinate to
        target (rectilinear) coordinate. An instance of MPL's Transform
        (inverse transform should be defined) or a tuple of two callable
        objects which defines the transform and its inverse. The callables
        need take two arguments of array of source coordinates and
        should return two target coordinates.

        e.g., ``x2, y2 = trans(x1, y1)``
        """
    def update_grid_finder(self, aux_trans: Incomplete | None = None, **kwargs) -> None: ...
    def new_fixed_axis(self, loc, nth_coord: Incomplete | None = None, axis_direction: Incomplete | None = None, offset: Incomplete | None = None, axes: Incomplete | None = None): ...
    def new_floating_axis(self, nth_coord, value, axes: Incomplete | None = None, axis_direction: str = 'bottom'): ...
    def get_gridlines(self, which: str = 'major', axis: str = 'both'): ...
    def get_tick_iterator(self, nth_coord, axis_side, minor: bool = False) -> Generator[Incomplete, None, None]: ...
