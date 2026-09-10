from .backend_webagg_core import FigureCanvasWebAggCore as FigureCanvasWebAggCore, FigureManagerWebAgg as FigureManagerWebAgg, NavigationToolbar2WebAgg as NavigationToolbar2WebAgg, TimerAsyncio as TimerAsyncio, TimerTornado as TimerTornado
from _typeshed import Incomplete
from matplotlib import is_interactive as is_interactive
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import CloseEvent as CloseEvent, NavigationToolbar2 as NavigationToolbar2, _Backend

def connection_info():
    """
    Return a string showing the figure and connection status for the backend.

    This is intended as a diagnostic tool, and not for general use.
    """

class NavigationIPy(NavigationToolbar2WebAgg):
    toolitems: Incomplete

class FigureManagerNbAgg(FigureManagerWebAgg):
    ToolbarCls = NavigationIPy
    def __init__(self, canvas, num) -> None: ...
    @classmethod
    def create_with_canvas(cls, canvas_class, figure, num): ...
    def display_js(self) -> None: ...
    def show(self) -> None: ...
    def reshow(self) -> None:
        """
        A special method to re-show the figure in the notebook.

        """
    @property
    def connected(self): ...
    @classmethod
    def get_javascript(cls, stream: Incomplete | None = None): ...
    def destroy(self) -> None: ...
    web_sockets: Incomplete
    def clearup_closed(self) -> None:
        """Clear up any closed Comms."""
    def remove_comm(self, comm_id) -> None: ...

class FigureCanvasNbAgg(FigureCanvasWebAggCore):
    manager_class = FigureManagerNbAgg

class CommSocket:
    """
    Manages the Comm connection between IPython and the browser (client).

    Comms are 2 way, with the CommSocket being able to publish a message
    via the send_json method, and handle a message with on_message. On the
    JS side figure.send_message and figure.ws.onmessage do the sending and
    receiving respectively.

    """
    supports_binary: Incomplete
    manager: Incomplete
    uuid: Incomplete
    comm: Incomplete
    def __init__(self, manager) -> None: ...
    def is_open(self): ...
    def on_close(self) -> None: ...
    def send_json(self, content) -> None: ...
    def send_binary(self, blob) -> None: ...
    def on_message(self, message) -> None: ...

class _BackendNbAgg(_Backend):
    FigureCanvas = FigureCanvasNbAgg
    FigureManager = FigureManagerNbAgg
