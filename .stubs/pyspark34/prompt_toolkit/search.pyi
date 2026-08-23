from .filters import FilterOrBool
from _typeshed import Incomplete
from enum import Enum
from prompt_toolkit.layout.controls import BufferControl

__all__ = ['SearchDirection', 'start_search', 'stop_search']

class SearchDirection(Enum):
    FORWARD: str
    BACKWARD: str

class SearchState:
    """
    A search 'query', associated with a search field (like a SearchToolbar).

    Every searchable `BufferControl` points to a `search_buffer_control`
    (another `BufferControls`) which represents the search field. The
    `SearchState` attached to that search field is used for storing the current
    search query.

    It is possible to have one searchfield for multiple `BufferControls`. In
    that case, they'll share the same `SearchState`.
    If there are multiple `BufferControls` that display the same `Buffer`, then
    they can have a different `SearchState` each (if they have a different
    search control).
    """
    text: Incomplete
    direction: Incomplete
    ignore_case: Incomplete
    def __init__(self, text: str = '', direction: SearchDirection = ..., ignore_case: FilterOrBool = False) -> None: ...
    def __invert__(self) -> SearchState:
        """
        Create a new SearchState where backwards becomes forwards and the other
        way around.
        """

def start_search(buffer_control: BufferControl | None = None, direction: SearchDirection = ...) -> None:
    """
    Start search through the given `buffer_control` using the
    `search_buffer_control`.

    :param buffer_control: Start search for this `BufferControl`. If not given,
        search through the current control.
    """
def stop_search(buffer_control: BufferControl | None = None) -> None:
    """
    Stop search through the given `buffer_control`.
    """
