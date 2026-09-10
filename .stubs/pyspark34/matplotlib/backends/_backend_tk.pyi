import tkinter as tk
from _typeshed import Incomplete
from matplotlib import backend_tools as backend_tools, cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import CloseEvent as CloseEvent, FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, KeyEvent as KeyEvent, LocationEvent as LocationEvent, MouseEvent as MouseEvent, NavigationToolbar2 as NavigationToolbar2, ResizeEvent as ResizeEvent, TimerBase as TimerBase, ToolContainerBase as ToolContainerBase, _Backend, cursors as cursors

cursord: Incomplete
TK_PHOTO_COMPOSITE_OVERLAY: int
TK_PHOTO_COMPOSITE_SET: int

def blit(photoimage, aggimage, offsets, bbox: Incomplete | None = None) -> None:
    """
    Blit *aggimage* to *photoimage*.

    *offsets* is a tuple describing how to fill the ``offset`` field of the
    ``Tk_PhotoImageBlock`` struct: it should be (0, 1, 2, 3) for RGBA8888 data,
    (2, 1, 0, 3) for little-endian ARBG32 (i.e. GBRA8888) data and (1, 2, 3, 0)
    for big-endian ARGB32 (i.e. ARGB8888) data.

    If *bbox* is passed, it defines the region that gets blitted. That region
    will be composed with the previous data according to the alpha channel.
    Blitting will be clipped to pixels inside the canvas, including silently
    doing nothing if the *bbox* region is entirely outside the canvas.

    Tcl events must be dispatched to trigger a blit from a non-Tcl thread.
    """

class TimerTk(TimerBase):
    """Subclass of `backend_bases.TimerBase` using Tk timer events."""
    parent: Incomplete
    def __init__(self, parent, *args, **kwargs) -> None: ...

class FigureCanvasTk(FigureCanvasBase):
    required_interactive_framework: str
    manager_class: Incomplete
    def __init__(self, figure: Incomplete | None = None, master: Incomplete | None = None) -> None: ...
    def resize(self, event) -> None: ...
    def draw_idle(self) -> None: ...
    def get_tk_widget(self):
        """
        Return the Tk widget used to implement FigureCanvasTkAgg.

        Although the initial implementation uses a Tk canvas,  this routine
        is intended to hide that fact.
        """
    def motion_notify_event(self, event) -> None: ...
    def enter_notify_event(self, event) -> None: ...
    def leave_notify_event(self, event) -> None: ...
    def button_press_event(self, event, dblclick: bool = False) -> None: ...
    def button_dblclick_event(self, event) -> None: ...
    def button_release_event(self, event) -> None: ...
    def scroll_event(self, event) -> None: ...
    def scroll_event_windows(self, event) -> None:
        """MouseWheel event processor"""
    def key_press(self, event) -> None: ...
    def key_release(self, event) -> None: ...
    def new_timer(self, *args, **kwargs): ...
    def flush_events(self) -> None: ...
    def start_event_loop(self, timeout: int = 0) -> None: ...
    def stop_event_loop(self) -> None: ...
    def set_cursor(self, cursor) -> None: ...

class FigureManagerTk(FigureManagerBase):
    """
    Attributes
    ----------
    canvas : `FigureCanvas`
        The FigureCanvas instance
    num : int or str
        The Figure number
    toolbar : tk.Toolbar
        The tk.Toolbar
    window : tk.Window
        The tk.Window
    """
    window: Incomplete
    def __init__(self, canvas, num, window) -> None: ...
    @classmethod
    def create_with_canvas(cls, canvas_class, figure, num): ...
    @classmethod
    def start_main_loop(cls) -> None: ...
    def resize(self, width, height) -> None: ...
    def show(self) -> None: ...
    def destroy(self, *args) -> None: ...
    def get_window_title(self): ...
    def set_window_title(self, title) -> None: ...
    def full_screen_toggle(self) -> None: ...

class NavigationToolbar2Tk(NavigationToolbar2, tk.Frame):
    window: Incomplete
    message: Incomplete
    def __init__(self, canvas, window: Incomplete | None = None, *, pack_toolbar: bool = True) -> None:
        '''
        Parameters
        ----------
        canvas : `FigureCanvas`
            The figure canvas on which to operate.
        window : tk.Window
            The tk.Window which owns this toolbar.
        pack_toolbar : bool, default: True
            If True, add the toolbar to the parent\'s pack manager\'s packing
            list during initialization with ``side="bottom"`` and ``fill="x"``.
            If you want to use the toolbar with a different layout manager, use
            ``pack_toolbar=False``.
        '''
    def pan(self, *args) -> None: ...
    def zoom(self, *args) -> None: ...
    def set_message(self, s) -> None: ...
    def draw_rubberband(self, event, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...
    lastrect: Incomplete
    def save_figure(self, *args) -> None: ...
    def set_history_buttons(self) -> None: ...

class ToolTip:
    """
    Tooltip recipe from
    http://www.voidspace.org.uk/python/weblog/arch_d7_2006_07_01.shtml#e387
    """
    @staticmethod
    def createToolTip(widget, text) -> None: ...
    widget: Incomplete
    tipwindow: Incomplete
    id: Incomplete
    x: int
    def __init__(self, widget) -> None: ...
    text: Incomplete
    def showtip(self, text) -> None:
        """Display text in tooltip window."""
    def hidetip(self) -> None: ...

class RubberbandTk(backend_tools.RubberbandBase):
    def draw_rubberband(self, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...
    lastrect: Incomplete

class ToolbarTk(ToolContainerBase, tk.Frame):
    def __init__(self, toolmanager, window: Incomplete | None = None) -> None: ...
    def add_toolitem(self, name, group, position, image_file, description, toggle): ...
    def toggle_toolitem(self, name, toggled) -> None: ...
    def remove_toolitem(self, name) -> None: ...
    def set_message(self, s) -> None: ...

class SaveFigureTk(backend_tools.SaveFigureBase):
    def trigger(self, *args) -> None: ...

class ConfigureSubplotsTk(backend_tools.ConfigureSubplotsBase):
    def trigger(self, *args) -> None: ...

class HelpTk(backend_tools.ToolHelpBase):
    def trigger(self, *args): ...
Toolbar = ToolbarTk

class _BackendTk(_Backend):
    backend_version: Incomplete
    FigureCanvas = FigureCanvasTk
    FigureManager = FigureManagerTk
    mainloop: Incomplete
