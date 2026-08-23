from .._version import __control_protocol_version__ as __control_protocol_version__, __jupyter_widgets_base_version__ as __jupyter_widgets_base_version__, __protocol_version__ as __protocol_version__
from .utils import deprecation as deprecation
from _typeshed import Incomplete
from collections.abc import Generator
from traitlets import Bytes as Bytes, HasTraits

TRAITLETS_FILE: Incomplete

def envset(name, default):
    """Return True if the given environment variable is turned on, otherwise False
    If the environment variable is set, True will be returned if it is assigned to a value
    other than 'no', 'n', 'false', 'off', '0', or '0.0' (case insensitive).
    If the environment variable is not set, the default value is returned.
    """

PROTOCOL_VERSION_MAJOR: Incomplete
CONTROL_PROTOCOL_VERSION_MAJOR: Incomplete
JUPYTER_WIDGETS_ECHO: Incomplete
widget_serialization: Incomplete

class LoggingHasTraits(HasTraits):
    """A parent class for HasTraits that log.
    Subclasses have a log trait, and the default behavior
    is to get the logger from the currently running Application.
    """
    log: Incomplete

class CallbackDispatcher(LoggingHasTraits):
    """A structure for registering and running callbacks"""
    callbacks: Incomplete
    def __call__(self, *args, **kwargs):
        """Call all of the registered callbacks."""
    def register_callback(self, callback, remove: bool = False) -> None:
        """(Un)Register a callback

        Parameters
        ----------
        callback: method handle
            Method to be registered or unregistered.
        remove=False: bool
            Whether to unregister the callback."""

class WidgetRegistry:
    def __init__(self) -> None: ...
    def register(self, model_module, model_module_version_range, model_name, view_module, view_module_version_range, view_name, klass) -> None:
        """Register a value"""
    def get(self, model_module, model_module_version, model_name, view_module, view_module_version, view_name):
        """Get a value"""
    def items(self) -> Generator[Incomplete, None, None]: ...

def register(widget):
    """A decorator registering a widget class in the widget registry."""

class _staticproperty:
    fget: Incomplete
    def __init__(self, fget) -> None: ...
    def __get__(self, owner_self, owner_cls): ...

class Widget(LoggingHasTraits):
    def widgets(): ...
    def widget_types(): ...
    @classmethod
    def close_all(cls) -> None: ...
    @staticmethod
    def on_widget_constructed(callback) -> None:
        """Registers a callback to be called when a widget is constructed.

        The callback must have the following signature:
        callback(widget)"""
    @classmethod
    def handle_control_comm_opened(cls, comm, msg) -> None:
        '''
        Class method, called when the comm-open message on the
        "jupyter.widget.control" comm channel is received
        '''
    @staticmethod
    def handle_comm_opened(comm, msg) -> None:
        """Static method, called when a widget is constructed."""
    @staticmethod
    def get_manager_state(drop_defaults: bool = False, widgets: Incomplete | None = None):
        """Returns the full state for a widget manager for embedding

        :param drop_defaults: when True, it will not include default value
        :param widgets: list with widgets to include in the state (or all widgets when None)
        :return:
        """
    def get_view_spec(self): ...
    comm: Incomplete
    keys: Incomplete
    def __init__(self, **kwargs) -> None:
        """Public constructor"""
    def __del__(self) -> None:
        """Object disposal"""
    def open(self):
        """Open a comm to the frontend if one isn't already open."""
    @property
    def model_id(self):
        """Gets the model id of this widget.

        If a Comm doesn't exist yet, a Comm will be created automagically."""
    def close(self) -> None:
        """Close method.

        Closes the underlying comm.
        When the comm is closed, all of the widget views are automatically
        removed from the front-end."""
    def send_state(self, key: Incomplete | None = None) -> None:
        """Sends the widget state, or a piece of it, to the front-end, if it exists.

        Parameters
        ----------
        key : unicode, or iterable (optional)
            A single property's name or iterable of property names to sync with the front-end.
        """
    def get_state(self, key: Incomplete | None = None, drop_defaults: bool = False):
        """Gets the widget state, or a piece of it.

        Parameters
        ----------
        key : unicode or iterable (optional)
            A single property's name or iterable of property names to get.

        Returns
        -------
        state : dict of states
        metadata : dict
            metadata for each field: {key: metadata}
        """
    def set_state(self, sync_data) -> None:
        """Called when a state is received from the front-end."""
    def send(self, content, buffers: Incomplete | None = None) -> None:
        """Sends a custom msg to the widget model in the front-end.

        Parameters
        ----------
        content : dict
            Content of the message to send.
        buffers : list of binary buffers
            Binary buffers to send with message
        """
    def on_msg(self, callback, remove: bool = False) -> None:
        """(Un)Register a custom msg receive callback.

        Parameters
        ----------
        callback: callable
            callback will be passed three arguments when a message arrives::

                callback(widget, content, buffers)

        remove: bool
            True if the callback should be unregistered."""
    def add_traits(self, **traits) -> None:
        """Dynamically add trait attributes to the Widget."""
    def notify_change(self, change) -> None:
        """Called when a property has changed."""
    def hold_sync(self) -> Generator[None, None, None]:
        """Hold syncing any state until the outermost context manager exits"""
