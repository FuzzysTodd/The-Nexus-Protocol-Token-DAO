from .buffer import Buffer
from .document import Document
from .filters import Filter
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import Callable

__all__ = ['Suggestion', 'AutoSuggest', 'ThreadedAutoSuggest', 'DummyAutoSuggest', 'AutoSuggestFromHistory', 'ConditionalAutoSuggest', 'DynamicAutoSuggest']

class Suggestion:
    """
    Suggestion returned by an auto-suggest algorithm.

    :param text: The suggestion text.
    """
    text: Incomplete
    def __init__(self, text: str) -> None: ...

class AutoSuggest(metaclass=ABCMeta):
    """
    Base class for auto suggestion implementations.
    """
    @abstractmethod
    def get_suggestion(self, buffer: Buffer, document: Document) -> Suggestion | None:
        """
        Return `None` or a :class:`.Suggestion` instance.

        We receive both :class:`~prompt_toolkit.buffer.Buffer` and
        :class:`~prompt_toolkit.document.Document`. The reason is that auto
        suggestions are retrieved asynchronously. (Like completions.) The
        buffer text could be changed in the meantime, but ``document`` contains
        the buffer document like it was at the start of the auto suggestion
        call. So, from here, don't access ``buffer.text``, but use
        ``document.text`` instead.

        :param buffer: The :class:`~prompt_toolkit.buffer.Buffer` instance.
        :param document: The :class:`~prompt_toolkit.document.Document` instance.
        """
    async def get_suggestion_async(self, buff: Buffer, document: Document) -> Suggestion | None:
        """
        Return a :class:`.Future` which is set when the suggestions are ready.
        This function can be overloaded in order to provide an asynchronous
        implementation.
        """

class ThreadedAutoSuggest(AutoSuggest):
    """
    Wrapper that runs auto suggestions in a thread.
    (Use this to prevent the user interface from becoming unresponsive if the
    generation of suggestions takes too much time.)
    """
    auto_suggest: Incomplete
    def __init__(self, auto_suggest: AutoSuggest) -> None: ...
    def get_suggestion(self, buff: Buffer, document: Document) -> Suggestion | None: ...
    async def get_suggestion_async(self, buff: Buffer, document: Document) -> Suggestion | None:
        """
        Run the `get_suggestion` function in a thread.
        """

class DummyAutoSuggest(AutoSuggest):
    """
    AutoSuggest class that doesn't return any suggestion.
    """
    def get_suggestion(self, buffer: Buffer, document: Document) -> Suggestion | None: ...

class AutoSuggestFromHistory(AutoSuggest):
    """
    Give suggestions based on the lines in the history.
    """
    def get_suggestion(self, buffer: Buffer, document: Document) -> Suggestion | None: ...

class ConditionalAutoSuggest(AutoSuggest):
    """
    Auto suggest that can be turned on and of according to a certain condition.
    """
    auto_suggest: Incomplete
    filter: Incomplete
    def __init__(self, auto_suggest: AutoSuggest, filter: bool | Filter) -> None: ...
    def get_suggestion(self, buffer: Buffer, document: Document) -> Suggestion | None: ...

class DynamicAutoSuggest(AutoSuggest):
    """
    Validator class that can dynamically returns any Validator.

    :param get_validator: Callable that returns a :class:`.Validator` instance.
    """
    get_auto_suggest: Incomplete
    def __init__(self, get_auto_suggest: Callable[[], AutoSuggest | None]) -> None: ...
    def get_suggestion(self, buff: Buffer, document: Document) -> Suggestion | None: ...
    async def get_suggestion_async(self, buff: Buffer, document: Document) -> Suggestion | None: ...
