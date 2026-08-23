from ..exporter import Exporter as Exporter
from .base import Renderer as Renderer
from _typeshed import Incomplete

class VegaRenderer(Renderer):
    props: Incomplete
    figwidth: Incomplete
    figheight: Incomplete
    data: Incomplete
    scales: Incomplete
    axes: Incomplete
    marks: Incomplete
    def open_figure(self, fig, props) -> None: ...
    def open_axes(self, ax, props) -> None: ...
    def draw_line(self, data, coordinates, style, label, mplobj: Incomplete | None = None) -> None: ...
    def draw_markers(self, data, coordinates, style, label, mplobj: Incomplete | None = None) -> None: ...
    def draw_text(self, text, position, coordinates, style, text_type: Incomplete | None = None, mplobj: Incomplete | None = None) -> None: ...

class VegaHTML:
    specification: Incomplete
    def __init__(self, renderer) -> None: ...
    def html(self):
        """Build the HTML representation for IPython."""

def fig_to_vega(fig, notebook: bool = False):
    """Convert a matplotlib figure to vega dictionary

    if notebook=True, then return an object which will display in a notebook
    otherwise, return an HTML string.
    """

VEGA_TEMPLATE: str
