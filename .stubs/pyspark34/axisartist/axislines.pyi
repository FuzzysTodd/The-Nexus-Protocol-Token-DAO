import matplotlib.axes as maxes
from .axis_artist import AxisArtist as AxisArtist, GridlinesCollection as GridlinesCollection
from .axisline_style import AxislineStyle as AxislineStyle
from _typeshed import Incomplete

class AxisArtistHelper:
    """
    Axis helpers should define the methods listed below.  The *axes* argument
    will be the axes attribute of the caller artist.

    ::

        # Construct the spine.

        def get_line_transform(self, axes):
            return transform

        def get_line(self, axes):
            return path

        # Construct the label.

        def get_axislabel_transform(self, axes):
            return transform

        def get_axislabel_pos_angle(self, axes):
            return (x, y), angle

        # Construct the ticks.

        def get_tick_transform(self, axes):
            return transform

        def get_tick_iterators(self, axes):
            # A pair of iterables (one for major ticks, one for minor ticks)
            # that yield (tick_position, tick_angle, tick_label).
            return iter_major, iter_minor
    """
    class _Base:
        """Base class for axis helper."""
        def update_lim(self, axes) -> None: ...
        delta1: Incomplete
        delta2: Incomplete
    class Fixed(_Base):
        """Helper class for a fixed (in the axes coordinate) axis."""
        passthru_pt: Incomplete
        nth_coord: Incomplete
        def __init__(self, loc, nth_coord: Incomplete | None = None) -> None:
            """``nth_coord = 0``: x-axis; ``nth_coord = 1``: y-axis."""
        def get_nth_coord(self): ...
        def get_line(self, axes): ...
        def get_line_transform(self, axes): ...
        def get_axislabel_transform(self, axes): ...
        def get_axislabel_pos_angle(self, axes):
            """
            Return the label reference position in transAxes.

            get_label_transform() returns a transform of (transAxes+offset)
            """
        def get_tick_transform(self, axes): ...
    class Floating(_Base):
        nth_coord: Incomplete
        def __init__(self, nth_coord, value) -> None: ...
        def get_nth_coord(self): ...
        def get_line(self, axes) -> None: ...

class AxisArtistHelperRectlinear:
    class Fixed(AxisArtistHelper.Fixed):
        axis: Incomplete
        def __init__(self, axes, loc, nth_coord: Incomplete | None = None) -> None:
            """
            nth_coord = along which coordinate value varies
            in 2D, nth_coord = 0 ->  x axis, nth_coord = 1 -> y axis
            """
        def get_tick_iterators(self, axes):
            """tick_loc, tick_angle, tick_label"""
    class Floating(AxisArtistHelper.Floating):
        axis: Incomplete
        def __init__(self, axes, nth_coord, passingthrough_point, axis_direction: str = 'bottom') -> None: ...
        def get_line(self, axes): ...
        def get_line_transform(self, axes): ...
        def get_axislabel_transform(self, axes): ...
        def get_axislabel_pos_angle(self, axes):
            """
            Return the label reference position in transAxes.

            get_label_transform() returns a transform of (transAxes+offset)
            """
        def get_tick_transform(self, axes): ...
        def get_tick_iterators(self, axes):
            """tick_loc, tick_angle, tick_label"""

class GridHelperBase:
    def __init__(self) -> None: ...
    def update_lim(self, axes) -> None: ...
    def get_gridlines(self, which, axis):
        '''
        Return list of grid lines as a list of paths (list of points).

        Parameters
        ----------
        which : {"both", "major", "minor"}
        axis : {"both", "x", "y"}
        '''
    def new_gridlines(self, ax):
        '''
        Create and return a new GridlineCollection instance.

        *which* : "major" or "minor"
        *axis* : "both", "x" or "y"

        '''

class GridHelperRectlinear(GridHelperBase):
    axes: Incomplete
    def __init__(self, axes) -> None: ...
    def new_fixed_axis(self, loc, nth_coord: Incomplete | None = None, axis_direction: Incomplete | None = None, offset: Incomplete | None = None, axes: Incomplete | None = None): ...
    def new_floating_axis(self, nth_coord, value, axis_direction: str = 'bottom', axes: Incomplete | None = None): ...
    def get_gridlines(self, which: str = 'major', axis: str = 'both'):
        '''
        Return list of gridline coordinates in data coordinates.

        Parameters
        ----------
        which : {"both", "major", "minor"}
        axis : {"both", "x", "y"}
        '''

class Axes(maxes.Axes):
    def __call__(self, *args, **kwargs): ...
    def __init__(self, *args, grid_helper: Incomplete | None = None, **kwargs) -> None: ...
    def toggle_axisline(self, b: Incomplete | None = None) -> None: ...
    @property
    def axis(self): ...
    def new_gridlines(self, grid_helper: Incomplete | None = None):
        '''
        Create and return a new GridlineCollection instance.

        *which* : "major" or "minor"
        *axis* : "both", "x" or "y"

        '''
    gridlines: Incomplete
    def clear(self) -> None: ...
    def get_grid_helper(self): ...
    def grid(self, visible: Incomplete | None = None, which: str = 'major', axis: str = 'both', **kwargs) -> None:
        """
        Toggle the gridlines, and optionally set the properties of the lines.
        """
    def get_children(self): ...
    def new_fixed_axis(self, loc, offset: Incomplete | None = None): ...
    def new_floating_axis(self, nth_coord, value, axis_direction: str = 'bottom'): ...

class AxesZero(Axes):
    def clear(self) -> None: ...
Subplot = Axes
SubplotZero = AxesZero
