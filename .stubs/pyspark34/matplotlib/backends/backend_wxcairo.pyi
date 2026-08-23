from .backend_cairo import FigureCanvasCairo as FigureCanvasCairo, cairo as cairo
from .backend_wx import FigureFrameWx as FigureFrameWx, _BackendWx, _FigureCanvasWxBase
from _typeshed import Incomplete

class FigureFrameWxCairo(FigureFrameWx):
    def get_canvas(self, fig): ...

class FigureCanvasWxCairo(FigureCanvasCairo, _FigureCanvasWxBase):
    """
    The FigureCanvas contains the figure and does event handling.

    In the wxPython backend, it is derived from wxPanel, and (usually) lives
    inside a frame instantiated by a FigureManagerWx. The parent window
    probably implements a wxSizer to control the displayed control size - but
    we give a hint as to our preferred minimum size.
    """
    bitmap: Incomplete
    def draw(self, drawDC: Incomplete | None = None) -> None: ...

class _BackendWxCairo(_BackendWx):
    FigureCanvas = FigureCanvasWxCairo
