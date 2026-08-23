import enum
from _typeshed import Incomplete
from matplotlib import cbook as cbook
from matplotlib._pylab_helpers import Gcf as Gcf

class Cursors(enum.IntEnum):
    """Backend-independent cursor types."""
    POINTER: Incomplete
    HAND: Incomplete
    SELECT_REGION: Incomplete
    MOVE: Incomplete
    WAIT: Incomplete
    RESIZE_HORIZONTAL: Incomplete
    RESIZE_VERTICAL: Incomplete
cursors = Cursors

class ToolBase:
    """
    Base tool class.

    A base tool, only implements `trigger` method or no method at all.
    The tool is instantiated by `matplotlib.backend_managers.ToolManager`.
    """
    default_keymap: Incomplete
    description: Incomplete
    image: Incomplete
    def __init__(self, toolmanager, name) -> None: ...
    name: Incomplete
    toolmanager: Incomplete
    canvas: Incomplete
    @property
    def figure(self):
        """The Figure affected by this tool, or None."""
    @figure.setter
    def figure(self, figure) -> None: ...
    set_figure: Incomplete
    def trigger(self, sender, event, data: Incomplete | None = None) -> None:
        """
        Called when this tool gets used.

        This method is called by `.ToolManager.trigger_tool`.

        Parameters
        ----------
        event : `.Event`
            The canvas event that caused this tool to be called.
        sender : object
            Object that requested the tool to be triggered.
        data : object
            Extra data.
        """
    def destroy(self) -> None:
        """
        Destroy the tool.

        This method is called by `.ToolManager.remove_tool`.
        """

class ToolToggleBase(ToolBase):
    """
    Toggleable tool.

    Every time it is triggered, it switches between enable and disable.

    Parameters
    ----------
    ``*args``
        Variable length argument to be used by the Tool.
    ``**kwargs``
        `toggled` if present and True, sets the initial state of the Tool
        Arbitrary keyword arguments to be consumed by the Tool
    """
    radio_group: Incomplete
    cursor: Incomplete
    default_toggled: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def trigger(self, sender, event, data: Incomplete | None = None) -> None:
        """Calls `enable` or `disable` based on `toggled` value."""
    def enable(self, event: Incomplete | None = None) -> None:
        """
        Enable the toggle tool.

        `trigger` calls this method when `toggled` is False.
        """
    def disable(self, event: Incomplete | None = None) -> None:
        """
        Disable the toggle tool.

        `trigger` call this method when `toggled` is True.

        This can happen in different circumstances.

        * Click on the toolbar tool button.
        * Call to `matplotlib.backend_managers.ToolManager.trigger_tool`.
        * Another `ToolToggleBase` derived tool is triggered
          (from the same `.ToolManager`).
        """
    @property
    def toggled(self):
        """State of the toggled tool."""
    def set_figure(self, figure) -> None: ...

class ToolSetCursor(ToolBase):
    """
    Change to the current cursor while inaxes.

    This tool, keeps track of all `ToolToggleBase` derived tools, and updates
    the cursor when a tool gets triggered.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, figure) -> None: ...

class ToolCursorPosition(ToolBase):
    """
    Send message with the current pointer position.

    This tool runs in the background reporting the position of the cursor.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def set_figure(self, figure) -> None: ...
    def send_message(self, event) -> None:
        """Call `matplotlib.backend_managers.ToolManager.message_event`."""

class RubberbandBase(ToolBase):
    """Draw and remove a rubberband."""
    def trigger(self, sender, event, data: Incomplete | None = None) -> None:
        """Call `draw_rubberband` or `remove_rubberband` based on data."""
    def draw_rubberband(self, *data) -> None:
        """
        Draw rubberband.

        This method must get implemented per backend.
        """
    def remove_rubberband(self) -> None:
        """
        Remove rubberband.

        This method should get implemented per backend.
        """

class ToolQuit(ToolBase):
    """Tool to call the figure manager destroy method."""
    description: str
    default_keymap: Incomplete
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...

class ToolQuitAll(ToolBase):
    """Tool to call the figure manager destroy method."""
    description: str
    default_keymap: Incomplete
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...

class ToolGrid(ToolBase):
    """Tool to toggle the major grids of the figure."""
    description: str
    default_keymap: Incomplete
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...

class ToolMinorGrid(ToolBase):
    """Tool to toggle the major and minor grids of the figure."""
    description: str
    default_keymap: Incomplete
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...

class ToolFullScreen(ToolBase):
    """Tool to toggle full screen."""
    description: str
    default_keymap: Incomplete
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...

class AxisScaleBase(ToolToggleBase):
    """Base Tool to toggle between linear and logarithmic."""
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...
    def enable(self, event: Incomplete | None = None) -> None: ...
    def disable(self, event: Incomplete | None = None) -> None: ...

class ToolYScale(AxisScaleBase):
    """Tool to toggle between linear and logarithmic scales on the Y axis."""
    description: str
    default_keymap: Incomplete
    def set_scale(self, ax, scale) -> None: ...

class ToolXScale(AxisScaleBase):
    """Tool to toggle between linear and logarithmic scales on the X axis."""
    description: str
    default_keymap: Incomplete
    def set_scale(self, ax, scale) -> None: ...

class ToolViewsPositions(ToolBase):
    """
    Auxiliary Tool to handle changes in views and positions.

    Runs in the background and should get used by all the tools that
    need to access the figure's history of views and positions, e.g.

    * `ToolZoom`
    * `ToolPan`
    * `ToolHome`
    * `ToolBack`
    * `ToolForward`
    """
    views: Incomplete
    positions: Incomplete
    home_views: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def add_figure(self, figure):
        """Add the current figure to the stack of views and positions."""
    def clear(self, figure) -> None:
        """Reset the axes stack."""
    def update_view(self) -> None:
        """
        Update the view limits and position for each axes from the current
        stack position. If any axes are present in the figure that aren't in
        the current stack position, use the home view limits for those axes and
        don't update *any* positions.
        """
    def push_current(self, figure: Incomplete | None = None) -> None:
        """
        Push the current view limits and position onto their respective stacks.
        """
    def update_home_views(self, figure: Incomplete | None = None) -> None:
        """
        Make sure that ``self.home_views`` has an entry for all axes present
        in the figure.
        """
    def home(self) -> None:
        """Recall the first view and position from the stack."""
    def back(self) -> None:
        """Back one step in the stack of views and positions."""
    def forward(self) -> None:
        """Forward one step in the stack of views and positions."""

class ViewsPositionsBase(ToolBase):
    """Base class for `ToolHome`, `ToolBack` and `ToolForward`."""
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...

class ToolHome(ViewsPositionsBase):
    """Restore the original view limits."""
    description: str
    image: str
    default_keymap: Incomplete

class ToolBack(ViewsPositionsBase):
    """Move back up the view limits stack."""
    description: str
    image: str
    default_keymap: Incomplete

class ToolForward(ViewsPositionsBase):
    """Move forward in the view lim stack."""
    description: str
    image: str
    default_keymap: Incomplete

class ConfigureSubplotsBase(ToolBase):
    """Base tool for the configuration of subplots."""
    description: str
    image: str

class SaveFigureBase(ToolBase):
    """Base tool for figure saving."""
    description: str
    image: str
    default_keymap: Incomplete

class ZoomPanBase(ToolToggleBase):
    """Base class for `ToolZoom` and `ToolPan`."""
    base_scale: float
    scrollthresh: float
    lastscroll: Incomplete
    def __init__(self, *args) -> None: ...
    def enable(self, event: Incomplete | None = None) -> None:
        """Connect press/release events and lock the canvas."""
    def disable(self, event: Incomplete | None = None) -> None:
        """Release the canvas and disconnect press/release events."""
    def trigger(self, sender, event, data: Incomplete | None = None) -> None: ...
    def scroll_zoom(self, event) -> None: ...

class ToolZoom(ZoomPanBase):
    """A Tool for zooming using a rectangle selector."""
    description: str
    image: str
    default_keymap: Incomplete
    cursor: Incomplete
    radio_group: str
    def __init__(self, *args) -> None: ...

class ToolPan(ZoomPanBase):
    """Pan axes with left mouse, zoom with right."""
    default_keymap: Incomplete
    description: str
    image: str
    cursor: Incomplete
    radio_group: str
    def __init__(self, *args) -> None: ...

class ToolHelpBase(ToolBase):
    description: str
    default_keymap: Incomplete
    image: str
    @staticmethod
    def format_shortcut(key_sequence):
        """
        Convert a shortcut string from the notation used in rc config to the
        standard notation for displaying shortcuts, e.g. 'ctrl+a' -> 'Ctrl+A'.
        """

class ToolCopyToClipboardBase(ToolBase):
    """Tool to copy the figure to the clipboard."""
    description: str
    default_keymap: Incomplete
    def trigger(self, *args, **kwargs) -> None: ...

default_tools: Incomplete
default_toolbar_tools: Incomplete

def add_tools_to_manager(toolmanager, tools=...) -> None:
    """
    Add multiple tools to a `.ToolManager`.

    Parameters
    ----------
    toolmanager : `.backend_managers.ToolManager`
        Manager to which the tools are added.
    tools : {str: class_like}, optional
        The tools to add in a {name: tool} dict, see
        `.backend_managers.ToolManager.add_tool` for more info.
    """
def add_tools_to_container(container, tools=...) -> None:
    """
    Add multiple tools to the container.

    Parameters
    ----------
    container : Container
        `.backend_bases.ToolContainerBase` object that will get the tools
        added.
    tools : list, optional
        List in the form ``[[group1, [tool1, tool2 ...]], [group2, [...]]]``
        where the tools ``[tool1, tool2, ...]`` will display in group1.
        See `.backend_bases.ToolContainerBase.add_tool` for details.
    """
