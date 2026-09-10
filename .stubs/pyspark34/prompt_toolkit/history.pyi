from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import AsyncGenerator, Iterable, Sequence

__all__ = ['History', 'ThreadedHistory', 'DummyHistory', 'FileHistory', 'InMemoryHistory']

class History(metaclass=ABCMeta):
    """
    Base ``History`` class.

    This also includes abstract methods for loading/storing history.
    """
    def __init__(self) -> None: ...
    async def load(self) -> AsyncGenerator[str, None]:
        """
        Load the history and yield all the entries in reverse order (latest,
        most recent history entry first).

        This method can be called multiple times from the `Buffer` to
        repopulate the history when prompting for a new input. So we are
        responsible here for both caching, and making sure that strings that
        were were appended to the history will be incorporated next time this
        method is called.
        """
    def get_strings(self) -> list[str]:
        """
        Get the strings from the history that are loaded so far.
        (In order. Oldest item first.)
        """
    def append_string(self, string: str) -> None:
        """Add string to the history."""
    @abstractmethod
    def load_history_strings(self) -> Iterable[str]:
        """
        This should be a generator that yields `str` instances.

        It should yield the most recent items first, because they are the most
        important. (The history can already be used, even when it's only
        partially loaded.)
        """
    @abstractmethod
    def store_string(self, string: str) -> None:
        """
        Store the string in persistent storage.
        """

class ThreadedHistory(History):
    """
    Wrapper around `History` implementations that run the `load()` generator in
    a thread.

    Use this to increase the start-up time of prompt_toolkit applications.
    History entries are available as soon as they are loaded. We don't have to
    wait for everything to be loaded.
    """
    history: Incomplete
    def __init__(self, history: History) -> None: ...
    async def load(self) -> AsyncGenerator[str, None]:
        """
        Like `History.load(), but call `self.load_history_strings()` in a
        background thread.
        """
    def append_string(self, string: str) -> None: ...
    def load_history_strings(self) -> Iterable[str]: ...
    def store_string(self, string: str) -> None: ...

class InMemoryHistory(History):
    """
    :class:`.History` class that keeps a list of all strings in memory.

    In order to prepopulate the history, it's possible to call either
    `append_string` for all items or pass a list of strings to `__init__` here.
    """
    def __init__(self, history_strings: Sequence[str] | None = None) -> None: ...
    def load_history_strings(self) -> Iterable[str]: ...
    def store_string(self, string: str) -> None: ...

class DummyHistory(History):
    """
    :class:`.History` object that doesn't remember anything.
    """
    def load_history_strings(self) -> Iterable[str]: ...
    def store_string(self, string: str) -> None: ...
    def append_string(self, string: str) -> None: ...

class FileHistory(History):
    """
    :class:`.History` class that stores all strings in a file.
    """
    filename: Incomplete
    def __init__(self, filename: str) -> None: ...
    def load_history_strings(self) -> Iterable[str]: ...
    def store_string(self, string: str) -> None: ...
