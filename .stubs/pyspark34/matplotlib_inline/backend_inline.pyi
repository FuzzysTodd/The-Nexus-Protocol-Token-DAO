from .config import InlineBackend as InlineBackend
from _typeshed import Incomplete
from matplotlib.backends.backend_agg import FigureCanvasAgg

def new_figure_manager(num, *args, FigureClass=..., **kwargs):
    """
    Return a new figure manager for a new figure instance.

    This function is part of the API expected by Matplotlib backends.
    """
def new_figure_manager_given_figure(num, figure):
    """
    Return a new figure manager for a given figure instance.

    This function is part of the API expected by Matplotlib backends.
    """
def show(close: Incomplete | None = None, block: Incomplete | None = None) -> None:
    """Show all figures as SVG/PNG payloads sent to the IPython clients.

    Parameters
    ----------
    close : bool, optional
        If true, a ``plt.close('all')`` call is automatically issued after
        sending all the figures. If this is set, the figures will entirely
        removed from the internal list of figures.
    block : Not used.
        The `block` parameter is a Matplotlib experimental parameter.
        We accept it in the function signature for compatibility with other
        backends.
    """
def flush_figures():
    """Send all figures that changed

    This is meant to be called automatically and will call show() if, during
    prior code execution, there had been any calls to draw_if_interactive.

    This function is meant to be used as a post_execute callback in IPython,
    so user-caused errors are handled with showtraceback() instead of being
    allowed to raise.  If this function is not called from within IPython,
    then these exceptions will raise.
    """
FigureCanvas = FigureCanvasAgg

def configure_inline_support(shell, backend) -> None:
    """Configure an IPython shell object for matplotlib use.

    Parameters
    ----------
    shell : InteractiveShell instance

    backend : matplotlib backend
    """
def set_matplotlib_formats(*formats, **kwargs) -> None:
    """Select figure formats for the inline backend. Optionally pass quality for JPEG.

    For example, this enables PNG and JPEG output with a JPEG quality of 90%::

        In [1]: set_matplotlib_formats('png', 'jpeg', quality=90)

    To set this in your config files use the following::

        c.InlineBackend.figure_formats = {'png', 'jpeg'}
        c.InlineBackend.print_figure_kwargs.update({'quality' : 90})

    Parameters
    ----------
    *formats : strs
        One or more figure formats to enable: 'png', 'retina', 'jpeg', 'svg', 'pdf'.
    **kwargs
        Keyword args will be relayed to ``figure.canvas.print_figure``.
    """
def set_matplotlib_close(close: bool = True) -> None:
    """Set whether the inline backend closes all figures automatically or not.

    By default, the inline backend used in the IPython Notebook will close all
    matplotlib figures automatically after each cell is run. This means that
    plots in different cells won't interfere. Sometimes, you may want to make
    a plot in one cell and then refine it in later cells. This can be accomplished
    by::

        In [1]: set_matplotlib_close(False)

    To set this in your config files use the following::

        c.InlineBackend.close_figures = False

    Parameters
    ----------
    close : bool
        Should all matplotlib figures be automatically closed after each cell is
        run?
    """
