from _typeshed import Incomplete

aliases: Incomplete
backends: Incomplete
registered: Incomplete

def register(name, inputhook) -> None:
    """Register the function *inputhook* as an event loop integration."""

class UnknownBackend(KeyError):
    name: Incomplete
    def __init__(self, name) -> None: ...

def set_qt_api(gui):
    """Sets the `QT_API` environment variable if it isn't already set."""
def get_inputhook_name_and_func(gui): ...
