from _typeshed import Incomplete
from traitlets.config.configurable import Configurable

class DisplayTrap(Configurable):
    """Object to manage sys.displayhook.

    This came from IPython.core.kernel.display_hook, but is simplified
    (no callbacks or formatters) until more of the core is refactored.
    """
    hook: Incomplete
    old_hook: Incomplete
    def __init__(self, hook: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None): ...
    def set(self) -> None:
        """Set the hook."""
    def unset(self) -> None:
        """Unset the hook."""
