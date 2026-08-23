from _typeshed import Incomplete
from typing import Callable, ContextManager, Dict, Generator, Generic

__all__ = ['Event', 'DummyContext', 'get_cwidth', 'suspend_to_background_supported', 'is_conemu_ansi', 'is_windows', 'in_main_thread', 'get_bell_environment_variable', 'get_term_environment_variable', 'take_using_weights', 'to_str', 'to_int', 'AnyFloat', 'to_float', 'is_dumb_terminal']

class Event(Generic[_Sender]):
    """
    Simple event to which event handlers can be attached. For instance::

        class Cls:
            def __init__(self):
                # Define event. The first parameter is the sender.
                self.event = Event(self)

        obj = Cls()

        def handler(sender):
            pass

        # Add event handler by using the += operator.
        obj.event += handler

        # Fire event.
        obj.event()
    """
    sender: Incomplete
    def __init__(self, sender: _Sender, handler: Callable[[_Sender], None] | None = None) -> None: ...
    def __call__(self) -> None:
        """Fire event."""
    def fire(self) -> None:
        """Alias for just calling the event."""
    def add_handler(self, handler: Callable[[_Sender], None]) -> None:
        """
        Add another handler to this callback.
        (Handler should be a callable that takes exactly one parameter: the
        sender object.)
        """
    def remove_handler(self, handler: Callable[[_Sender], None]) -> None:
        """
        Remove a handler from this callback.
        """
    def __iadd__(self, handler: Callable[[_Sender], None]) -> Event[_Sender]:
        """
        `event += handler` notation for adding a handler.
        """
    def __isub__(self, handler: Callable[[_Sender], None]) -> Event[_Sender]:
        """
        `event -= handler` notation for removing a handler.
        """

class DummyContext(ContextManager[None]):
    """
    (contextlib.nested is not available on Py3)
    """
    def __enter__(self) -> None: ...
    def __exit__(self, *a: object) -> None: ...

class _CharSizesCache(Dict[str, int]):
    """
    Cache for wcwidth sizes.
    """
    LONG_STRING_MIN_LEN: int
    MAX_LONG_STRINGS: int
    def __init__(self) -> None: ...
    def __missing__(self, string: str) -> int: ...

def get_cwidth(string: str) -> int:
    """
    Return width of a string. Wrapper around ``wcwidth``.
    """
def suspend_to_background_supported() -> bool:
    """
    Returns `True` when the Python implementation supports
    suspend-to-background. This is typically `False' on Windows systems.
    """
def is_windows() -> bool:
    """
    True when we are using Windows.
    """
def is_conemu_ansi() -> bool:
    """
    True when the ConEmu Windows console is used.
    """
def in_main_thread() -> bool:
    """
    True when the current thread is the main thread.
    """
def get_bell_environment_variable() -> bool:
    """
    True if env variable is set to true (true, TRUE, True, 1).
    """
def get_term_environment_variable() -> str:
    """Return the $TERM environment variable."""
def take_using_weights(items: list[_T], weights: list[int]) -> Generator[_T, None, None]:
    """
    Generator that keeps yielding items from the items list, in proportion to
    their weight. For instance::

        # Getting the first 70 items from this generator should have yielded 10
        # times A, 20 times B and 40 times C, all distributed equally..
        take_using_weights(['A', 'B', 'C'], [5, 10, 20])

    :param items: List of items to take from.
    :param weights: Integers representing the weight. (Numbers have to be
                    integers, not floats.)
    """
def to_str(value: Callable[[], str] | str) -> str:
    """Turn callable or string into string."""
def to_int(value: Callable[[], int] | int) -> int:
    """Turn callable or int into int."""
AnyFloat = Callable[[], float] | float

def to_float(value: AnyFloat) -> float:
    """Turn callable or float into float."""
def is_dumb_terminal(term: str | None = None) -> bool:
    '''
    True if this terminal type is considered "dumb".

    If so, we should fall back to the simplest possible form of line editing,
    without cursor positioning and color support.
    '''
