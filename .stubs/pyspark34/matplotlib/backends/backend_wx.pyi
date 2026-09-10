import wx
from _typeshed import Incomplete
from matplotlib import backend_tools as backend_tools, cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import CloseEvent as CloseEvent, FigureCanvasBase as FigureCanvasBase, FigureManagerBase as FigureManagerBase, GraphicsContextBase as GraphicsContextBase, KeyEvent as KeyEvent, LocationEvent as LocationEvent, MouseButton as MouseButton, MouseEvent as MouseEvent, NavigationToolbar2 as NavigationToolbar2, RendererBase as RendererBase, ResizeEvent as ResizeEvent, TimerBase as TimerBase, ToolContainerBase as ToolContainerBase, _Backend, cursors as cursors
from matplotlib.path import Path as Path
from matplotlib.transforms import Affine2D as Affine2D

PIXELS_PER_INCH: int

def error_msg_wx(msg, parent: Incomplete | None = None) -> None:
    """Signal an error condition with a popup error dialog."""

class TimerWx(TimerBase):
    """Subclass of `.TimerBase` using wx.Timer events."""
    def __init__(self, *args, **kwargs) -> None: ...

class RendererWx(RendererBase):
    """
    The renderer handles all the drawing primitives using a graphics
    context instance that controls the colors/styles. It acts as the
    'renderer' instance used by many classes in the hierarchy.
    """
    fontweights: Incomplete
    fontangles: Incomplete
    fontnames: Incomplete
    width: Incomplete
    height: Incomplete
    bitmap: Incomplete
    fontd: Incomplete
    dpi: Incomplete
    gc: Incomplete
    def __init__(self, bitmap, dpi) -> None:
        """Initialise a wxWindows renderer instance."""
    def flipy(self): ...
    def offset_text_height(self): ...
    def get_text_width_height_descent(self, s, prop, ismath): ...
    def get_canvas_width_height(self): ...
    def handle_clip_rectangle(self, gc) -> None: ...
    @staticmethod
    def convert_path(gfx_ctx, path, transform): ...
    def draw_path(self, gc, path, transform, rgbFace: Incomplete | None = None) -> None: ...
    def draw_image(self, gc, x, y, im) -> None: ...
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = False, mtext: Incomplete | None = None) -> None: ...
    def new_gc(self): ...
    def get_wx_font(self, s, prop):
        """Return a wx font.  Cache font instances for efficiency."""
    def points_to_pixels(self, points): ...

class GraphicsContextWx(GraphicsContextBase):
    """
    The graphics context provides the color, line styles, etc.

    This class stores a reference to a wxMemoryDC, and a
    wxGraphicsContext that draws to it.  Creating a wxGraphicsContext
    seems to be fairly heavy, so these objects are cached based on the
    bitmap object that is passed in.

    The base GraphicsContext stores colors as an RGB tuple on the unit
    interval, e.g., (0.5, 0.0, 1.0).  wxPython uses an int interval, but
    since wxPython colour management is rather simple, I have not chosen
    to implement a separate colour manager class.
    """
    bitmap: Incomplete
    dc: Incomplete
    gfx_ctx: Incomplete
    renderer: Incomplete
    def __init__(self, bitmap, renderer) -> None: ...
    IsSelected: bool
    def select(self) -> None:
        """Select the current bitmap into this wxDC instance."""
    def unselect(self) -> None:
        """Select a Null bitmap into this wxDC instance."""
    def set_foreground(self, fg, isRGBA: Incomplete | None = None) -> None: ...
    def set_linewidth(self, w) -> None: ...
    def set_capstyle(self, cs) -> None: ...
    def set_joinstyle(self, js) -> None: ...
    def get_wxcolour(self, color):
        """Convert an RGB(A) color to a wx.Colour."""

class _FigureCanvasWxBase(FigureCanvasBase, wx.Panel):
    """
    The FigureCanvas contains the figure and does event handling.

    In the wxPython backend, it is derived from wxPanel, and (usually) lives
    inside a frame instantiated by a FigureManagerWx. The parent window
    probably implements a wx.Sizer to control the displayed control size - but
    we give a hint as to our preferred minimum size.
    """
    required_interactive_framework: str
    manager_class: Incomplete
    keyvald: Incomplete
    bitmap: Incomplete
    def __init__(self, parent, id, figure: Incomplete | None = None) -> None:
        """
        Initialize a FigureWx instance.

        - Initialize the FigureCanvasBase and wxPanel parents.
        - Set event handlers for resize, paint, and keyboard and mouse
          interaction.
        """
    def Copy_to_Clipboard(self, event: Incomplete | None = None) -> None:
        """Copy bitmap of canvas to system clipboard."""
    def draw_idle(self) -> None: ...
    def flush_events(self) -> None: ...
    def start_event_loop(self, timeout: int = 0) -> None: ...
    def stop_event_loop(self, event: Incomplete | None = None) -> None: ...
    def gui_repaint(self, drawDC: Incomplete | None = None) -> None:
        """
        Update the displayed image on the GUI canvas, using the supplied
        wx.PaintDC device context.

        The 'WXAgg' backend sets origin accordingly.
        """
    filetypes: Incomplete
    def print_figure(self, filename, *args, **kwargs) -> None: ...
    def set_cursor(self, cursor) -> None: ...

class FigureCanvasWx(_FigureCanvasWxBase):
    renderer: Incomplete
    def draw(self, drawDC: Incomplete | None = None) -> None:
        """
        Render the figure using RendererWx instance renderer, or using a
        previously defined renderer if none is specified.
        """
    print_bmp: Incomplete
    print_jpeg: Incomplete
    print_jpg: Incomplete
    print_pcx: Incomplete
    print_png: Incomplete
    print_tiff: Incomplete
    print_tif: Incomplete
    print_xpm: Incomplete

class FigureFrameWx(wx.Frame):
    canvas: Incomplete
    def __init__(self, num, fig, *, canvas_class: Incomplete | None = None) -> None: ...
    sizer: Incomplete
    figmgr: Incomplete
    num: Incomplete
    toolbar: Incomplete
    toolmanager: Incomplete
    def get_canvas(self, fig): ...
    def get_figure_manager(self): ...

class FigureManagerWx(FigureManagerBase):
    """
    Container/controller for the FigureCanvas and GUI frame.

    It is instantiated by Gcf whenever a new figure is created.  Gcf is
    responsible for managing multiple instances of FigureManagerWx.

    Attributes
    ----------
    canvas : `FigureCanvas`
        a FigureCanvasWx(wx.Panel) instance
    window : wxFrame
        a wxFrame instance - wxpython.org/Phoenix/docs/html/Frame.html
    """
    frame: Incomplete
    def __init__(self, canvas, num, frame) -> None: ...
    @classmethod
    def create_with_canvas(cls, canvas_class, figure, num): ...
    @classmethod
    def start_main_loop(cls) -> None: ...
    def show(self) -> None: ...
    def destroy(self, *args) -> None: ...
    def full_screen_toggle(self) -> None: ...
    def get_window_title(self): ...
    def set_window_title(self, title) -> None: ...
    def resize(self, width, height) -> None: ...

class NavigationToolbar2Wx(NavigationToolbar2, wx.ToolBar):
    wx_ids: Incomplete
    def __init__(self, canvas, coordinates: bool = True, *, style=...) -> None: ...
    def zoom(self, *args) -> None: ...
    def pan(self, *args) -> None: ...
    def save_figure(self, *args) -> None: ...
    def draw_rubberband(self, event, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...
    def set_message(self, s) -> None: ...
    def set_history_buttons(self) -> None: ...

class ToolbarWx(ToolContainerBase, wx.ToolBar):
    def __init__(self, toolmanager, parent: Incomplete | None = None, style=...) -> None: ...
    def add_toolitem(self, name, group, position, image_file, description, toggle) -> None: ...
    def toggle_toolitem(self, name, toggled) -> None: ...
    def remove_toolitem(self, name) -> None: ...
    def set_message(self, s) -> None: ...

class ConfigureSubplotsWx(backend_tools.ConfigureSubplotsBase):
    def trigger(self, *args) -> None: ...

class SaveFigureWx(backend_tools.SaveFigureBase):
    def trigger(self, *args) -> None: ...

class RubberbandWx(backend_tools.RubberbandBase):
    def draw_rubberband(self, x0, y0, x1, y1) -> None: ...
    def remove_rubberband(self) -> None: ...

class _HelpDialog(wx.Dialog):
    headers: Incomplete
    widths: Incomplete
    def __init__(self, parent, help_entries) -> None: ...
    @classmethod
    def show(cls, parent, help_entries) -> None: ...

class HelpWx(backend_tools.ToolHelpBase):
    def trigger(self, *args) -> None: ...

class ToolCopyToClipboardWx(backend_tools.ToolCopyToClipboardBase):
    def trigger(self, *args, **kwargs) -> None: ...

class _BackendWx(_Backend):
    FigureCanvas = FigureCanvasWx
    FigureManager = FigureManagerWx
    mainloop: Incomplete
