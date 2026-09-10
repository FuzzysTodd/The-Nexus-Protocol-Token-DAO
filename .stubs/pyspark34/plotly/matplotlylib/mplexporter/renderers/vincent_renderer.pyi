from ..exporter import Exporter as Exporter
from .base import Renderer as Renderer
from _typeshed import Incomplete

class VincentRenderer(Renderer):
    chart: Incomplete
    figwidth: Incomplete
    figheight: Incomplete
    def open_figure(self, fig, props) -> None: ...
    def draw_line(self, data, coordinates, style, label, mplobj: Incomplete | None = None) -> None: ...
    def draw_markers(self, data, coordinates, style, label, mplobj: Incomplete | None = None) -> None: ...

def fig_to_vincent(fig):
    """Convert a matplotlib figure to a vincent object"""
