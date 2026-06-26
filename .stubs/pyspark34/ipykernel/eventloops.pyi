from _typeshed import Incomplete

loop_map: Incomplete

def register_integration(*toolkitnames):
    """Decorator to register an event loop to integrate with the IPython kernel

    The decorator takes names to register the event loop as for the %gui magic.
    You can provide alternative names for the same toolkit.

    The decorated function should take a single argument, the IPython kernel
    instance, arrange for the event loop to call ``kernel.do_one_iteration()``
    at least every ``kernel._poll_interval`` seconds, and start the event loop.

    :mod:`ipykernel.eventloops` provides and registers such functions
    for a few common event loops.
    """
def loop_qt(kernel) -> None:
    """Event loop for all supported versions of Qt."""
loop_qt5 = loop_qt

def loop_qt_exit(kernel) -> None: ...
def loop_wx(kernel):
    """Start a kernel with wx event loop support."""
def loop_wx_exit(kernel) -> None:
    """Exit the wx loop."""
def loop_tk(kernel) -> None:
    """Start a kernel with the Tk event loop."""
def loop_tk_exit(kernel) -> None:
    """Exit the tk loop."""
def loop_gtk(kernel) -> None:
    """Start the kernel, coordinating with the GTK event loop"""
def loop_gtk_exit(kernel) -> None:
    """Exit the gtk loop."""
def loop_gtk3(kernel) -> None:
    """Start the kernel, coordinating with the GTK event loop"""
def loop_gtk3_exit(kernel) -> None:
    """Exit the gtk3 loop."""
def loop_cocoa(kernel) -> None:
    """Start the kernel, coordinating with the Cocoa CFRunLoop event loop
    via the matplotlib MacOSX backend.
    """
def loop_cocoa_exit(kernel) -> None:
    """Exit the cocoa loop."""
def loop_asyncio(kernel) -> None:
    """Start a kernel with asyncio event loop support."""
def loop_asyncio_exit(kernel) -> None:
    """Exit hook for asyncio"""
def set_qt_api_env_from_gui(gui) -> None:
    """
    Sets the QT_API environment variable by trying to import PyQtx or PySidex.

    The user can generically request `qt` or a specific Qt version, e.g. `qt6`.
    For a generic Qt request, we let the mechanism in IPython choose the best
    available version by leaving the `QT_API` environment variable blank.

    For specific versions, we check to see whether the PyQt or PySide
    implementations are present and set `QT_API` accordingly to indicate to
    IPython which version we want. If neither implementation is present, we
    leave the environment variable set so IPython will generate a helpful error
    message.

    Notes
    -----
    - If the environment variable is already set, it will be used unchanged,
      regardless of what the user requested.
    """
def make_qt_app_for_kernel(gui, kernel) -> None:
    """Sets the `QT_API` environment variable if it isn't already set."""
def enable_gui(gui, kernel: Incomplete | None = None) -> None:
    """Enable integration with a given GUI"""
