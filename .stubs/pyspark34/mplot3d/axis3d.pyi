from . import art3d as art3d, proj3d as proj3d
from _typeshed import Incomplete
from matplotlib import axis as maxis

def move_from_center(coord, centers, deltas, axmask=(True, True, True)):
    """
    For each coordinate where *axmask* is True, move *coord* away from
    *centers* by *deltas*.
    """
def tick_update_position(tick, tickxs, tickys, labelpos) -> None:
    """Update tick line and label position and style."""

class Axis(maxis.XAxis):
    """An Axis class for the 3D plots."""
    def __init__(self, *args, **kwargs) -> None: ...
    adir: Incomplete
    def init3d(self) -> None: ...
    def get_major_ticks(self, numticks: Incomplete | None = None): ...
    def get_minor_ticks(self, numticks: Incomplete | None = None): ...
    def set_pane_pos(self, xys) -> None:
        """Set pane position."""
    stale: bool
    def set_pane_color(self, color, alpha: Incomplete | None = None) -> None:
        """
        Set pane color.

        Parameters
        ----------
        color : color
            Color for axis pane.
        alpha : float, optional
            Alpha value for axis pane. If None, base it on *color*.
        """
    def set_rotate_label(self, val) -> None:
        """
        Whether to rotate the axis label: True, False or None.
        If set to None the label will be rotated if longer than 4 chars.
        """
    def get_rotate_label(self, text): ...
    def draw_pane(self, renderer) -> None:
        """
        Draw pane.

        Parameters
        ----------
        renderer : `~matplotlib.backend_bases.RendererBase` subclass
        """
    def draw(self, renderer) -> None: ...
    def get_tightbbox(self, renderer: Incomplete | None = None, *, for_layout_only: bool = False): ...
    d_interval: Incomplete
    v_interval: Incomplete

class XAxis(Axis):
    axis_name: str
    get_view_interval: Incomplete
    set_view_interval: Incomplete
    get_data_interval: Incomplete
    set_data_interval: Incomplete

class YAxis(Axis):
    axis_name: str
    get_view_interval: Incomplete
    set_view_interval: Incomplete
    get_data_interval: Incomplete
    set_data_interval: Incomplete

class ZAxis(Axis):
    axis_name: str
    get_view_interval: Incomplete
    set_view_interval: Incomplete
    get_data_interval: Incomplete
    set_data_interval: Incomplete
