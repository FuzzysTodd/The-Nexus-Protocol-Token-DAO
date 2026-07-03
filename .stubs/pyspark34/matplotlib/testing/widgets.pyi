from _typeshed import Incomplete

def get_ax():
    """Create a plot and return its axes."""
def noop(*args, **kwargs) -> None: ...
def mock_event(ax, button: int = 1, xdata: int = 0, ydata: int = 0, key: Incomplete | None = None, step: int = 1):
    """
    Create a mock event that can stand in for `.Event` and its subclasses.

    This event is intended to be used in tests where it can be passed into
    event handling functions.

    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        The axes the event will be in.
    xdata : int
        x coord of mouse in data coords.
    ydata : int
        y coord of mouse in data coords.
    button : None or `MouseButton` or {'up', 'down'}
        The mouse button pressed in this event (see also `.MouseEvent`).
    key : None or str
        The key pressed when the mouse event triggered (see also `.KeyEvent`).
    step : int
        Number of scroll steps (positive for 'up', negative for 'down').

    Returns
    -------
    event
        A `.Event`\\-like Mock instance.
    """
def do_event(tool, etype, button: int = 1, xdata: int = 0, ydata: int = 0, key: Incomplete | None = None, step: int = 1) -> None:
    """
    Trigger an event on the given tool.

    Parameters
    ----------
    tool : matplotlib.widgets.RectangleSelector
    etype : str
        The event to trigger.
    xdata : int
        x coord of mouse in data coords.
    ydata : int
        y coord of mouse in data coords.
    button : None or `MouseButton` or {'up', 'down'}
        The mouse button pressed in this event (see also `.MouseEvent`).
    key : None or str
        The key pressed when the mouse event triggered (see also `.KeyEvent`).
    step : int
        Number of scroll steps (positive for 'up', negative for 'down').
    """
def click_and_drag(tool, start, end, key: Incomplete | None = None) -> None:
    """
    Helper to simulate a mouse drag operation.

    Parameters
    ----------
    tool : `~matplotlib.widgets.Widget`
    start : [float, float]
        Starting point in data coordinates.
    end : [float, float]
        End point in data coordinates.
    key : None or str
         An optional key that is pressed during the whole operation
         (see also `.KeyEvent`).
    """
