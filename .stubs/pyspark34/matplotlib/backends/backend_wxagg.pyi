from .backend_agg import FigureCanvasAgg as FigureCanvasAgg
from .backend_wx import FigureFrameWx as FigureFrameWx, _BackendWx, _FigureCanvasWxBase
from _typeshed import Incomplete

class FigureFrameWxAgg(FigureFrameWx):
    def get_canvas(self, fig): ...

class FigureCanvasWxAgg(FigureCanvasAgg, _FigureCanvasWxBase):
    """
    The FigureCanvas contains the figure and does event handling.

    In the wxPython backend, it is derived from wxPanel, and (usually)
    lives inside a frame instantiated by a FigureManagerWx. The parent
    window probably implements a wxSizer to control the displayed
    control size - but we give a hint as to our preferred minimum
    size.
    """
    bitmap: Incomplete
    def draw(self, drawDC: Incomplete | None = None) -> None:
        """
        Render the figure using agg.
        """
    def blit(self, bbox: Incomplete | None = None) -> None: ...

class _BackendWxAgg(_BackendWx):
    FigureCanvas = FigureCanvasWxAgg
