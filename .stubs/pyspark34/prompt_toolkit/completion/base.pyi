from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from prompt_toolkit.document import Document
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText, StyleAndTextTuples
from typing import AsyncGenerator, Callable, Iterable, Sequence

__all__ = ['Completion', 'Completer', 'ThreadedCompleter', 'DummyCompleter', 'DynamicCompleter', 'CompleteEvent', 'ConditionalCompleter', 'merge_completers', 'get_common_complete_suffix']

class Completion:
    """
    :param text: The new string that will be inserted into the document.
    :param start_position: Position relative to the cursor_position where the
        new text will start. The text will be inserted between the
        start_position and the original cursor position.
    :param display: (optional string or formatted text) If the completion has
        to be displayed differently in the completion menu.
    :param display_meta: (Optional string or formatted text) Meta information
        about the completion, e.g. the path or source where it's coming from.
        This can also be a callable that returns a string.
    :param style: Style string.
    :param selected_style: Style string, used for a selected completion.
        This can override the `style` parameter.
    """
    text: Incomplete
    start_position: Incomplete
    display: Incomplete
    style: Incomplete
    selected_style: Incomplete
    def __init__(self, text: str, start_position: int = 0, display: AnyFormattedText | None = None, display_meta: AnyFormattedText | None = None, style: str = '', selected_style: str = '') -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def display_text(self) -> str:
        """The 'display' field as plain text."""
    @property
    def display_meta(self) -> StyleAndTextTuples:
        """Return meta-text. (This is lazy when using a callable)."""
    @property
    def display_meta_text(self) -> str:
        """The 'meta' field as plain text."""
    def new_completion_from_position(self, position: int) -> Completion:
        """
        (Only for internal use!)
        Get a new completion by splitting this one. Used by `Application` when
        it needs to have a list of new completions after inserting the common
        prefix.
        """

class CompleteEvent:
    """
    Event that called the completer.

    :param text_inserted: When True, it means that completions are requested
        because of a text insert. (`Buffer.complete_while_typing`.)
    :param completion_requested: When True, it means that the user explicitly
        pressed the `Tab` key in order to view the completions.

    These two flags can be used for instance to implement a completer that
    shows some completions when ``Tab`` has been pressed, but not
    automatically when the user presses a space. (Because of
    `complete_while_typing`.)
    """
    text_inserted: Incomplete
    completion_requested: Incomplete
    def __init__(self, text_inserted: bool = False, completion_requested: bool = False) -> None: ...

class Completer(metaclass=ABCMeta):
    """
    Base class for completer implementations.
    """
    @abstractmethod
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]:
        """
        This should be a generator that yields :class:`.Completion` instances.

        If the generation of completions is something expensive (that takes a
        lot of time), consider wrapping this `Completer` class in a
        `ThreadedCompleter`. In that case, the completer algorithm runs in a
        background thread and completions will be displayed as soon as they
        arrive.

        :param document: :class:`~prompt_toolkit.document.Document` instance.
        :param complete_event: :class:`.CompleteEvent` instance.
        """
    async def get_completions_async(self, document: Document, complete_event: CompleteEvent) -> AsyncGenerator[Completion, None]:
        """
        Asynchronous generator for completions. (Probably, you won't have to
        override this.)

        Asynchronous generator of :class:`.Completion` objects.
        """

class ThreadedCompleter(Completer):
    """
    Wrapper that runs the `get_completions` generator in a thread.

    (Use this to prevent the user interface from becoming unresponsive if the
    generation of completions takes too much time.)

    The completions will be displayed as soon as they are produced. The user
    can already select a completion, even if not all completions are displayed.
    """
    completer: Incomplete
    def __init__(self, completer: Completer) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...
    async def get_completions_async(self, document: Document, complete_event: CompleteEvent) -> AsyncGenerator[Completion, None]:
        """
        Asynchronous generator of completions.
        """

class DummyCompleter(Completer):
    """
    A completer that doesn't return any completion.
    """
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...

class DynamicCompleter(Completer):
    """
    Completer class that can dynamically returns any Completer.

    :param get_completer: Callable that returns a :class:`.Completer` instance.
    """
    get_completer: Incomplete
    def __init__(self, get_completer: Callable[[], Completer | None]) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...
    async def get_completions_async(self, document: Document, complete_event: CompleteEvent) -> AsyncGenerator[Completion, None]: ...

class ConditionalCompleter(Completer):
    """
    Wrapper around any other completer that will enable/disable the completions
    depending on whether the received condition is satisfied.

    :param completer: :class:`.Completer` instance.
    :param filter: :class:`.Filter` instance.
    """
    completer: Incomplete
    filter: Incomplete
    def __init__(self, completer: Completer, filter: FilterOrBool) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...
    async def get_completions_async(self, document: Document, complete_event: CompleteEvent) -> AsyncGenerator[Completion, None]: ...

class _MergedCompleter(Completer):
    """
    Combine several completers into one.
    """
    completers: Incomplete
    def __init__(self, completers: Sequence[Completer]) -> None: ...
    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]: ...
    async def get_completions_async(self, document: Document, complete_event: CompleteEvent) -> AsyncGenerator[Completion, None]: ...

def merge_completers(completers: Sequence[Completer], deduplicate: bool = False) -> Completer:
    """
    Combine several completers into one.

    :param deduplicate: If `True`, wrap the result in a `DeduplicateCompleter`
        so that completions that would result in the same text will be
        deduplicated.
    """
def get_common_complete_suffix(document: Document, completions: Sequence[Completion]) -> str:
    """
    Return the common prefix for all completions.
    """
