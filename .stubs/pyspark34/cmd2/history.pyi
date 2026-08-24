from . import utils as utils
from .parsing import Statement as Statement
from _typeshed import Incomplete
from collections import OrderedDict
from typing import Any, Dict, Iterable, List, overload

class HistoryItem:
    """Class used to represent one command in the history list"""
    statement: Statement
    @property
    def raw(self) -> str:
        """The raw input from the user for this item.

        Proxy property for ``self.statement.raw``
        """
    @property
    def expanded(self) -> str:
        """Return the command as run which includes shortcuts and aliases resolved
        plus any changes made in hooks

        Proxy property for ``self.statement.expanded_command_line``
        """
    def pr(self, idx: int, script: bool = False, expanded: bool = False, verbose: bool = False) -> str:
        """Represent this item in a pretty fashion suitable for printing.

        If you pass verbose=True, script and expanded will be ignored

        :param idx: The 1-based index of this item in the history list
        :param script: True if formatting for a script (No item numbers)
        :param expanded: True if expanded command line should be printed
        :param verbose: True if expanded and raw should both appear when they are different
        :return: pretty print string version of a HistoryItem
        """
    def to_dict(self) -> Dict[str, Any]:
        """Utility method to convert this HistoryItem into a dictionary for use in persistent JSON history files"""
    @staticmethod
    def from_dict(source_dict: Dict[str, Any]) -> HistoryItem:
        """
        Utility method to restore a HistoryItem from a dictionary

        :param source_dict: source data dictionary (generated using to_dict())
        :return: HistoryItem object
        :raises KeyError: if source_dict is missing required elements
        """
    def __init__(self, statement) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class History(List[HistoryItem]):
    """A list of :class:`~cmd2.history.HistoryItem` objects with additional methods
    for searching and managing the list.

    :class:`~cmd2.Cmd` instantiates this class into the :data:`~cmd2.Cmd.history`
    attribute, and adds commands to it as a user enters them.

    See :ref:`features/history:History` for information about the built-in command
    which allows users to view, search, run, and save previously entered commands.

    Developers interested in accessing previously entered commands can use this
    class to gain access to the historical record.
    """
    session_start_index: int
    def __init__(self, seq: Iterable[HistoryItem] = ()) -> None: ...
    def start_session(self) -> None:
        """Start a new session, thereby setting the next index as the first index in the new session."""
    @overload
    def append(self, new: HistoryItem) -> None: ...
    @overload
    def append(self, new: Statement) -> None: ...
    def clear(self) -> None:
        """Remove all items from the History list."""
    def get(self, index: int) -> HistoryItem:
        """Get item from the History list using 1-based indexing.

        :param index: optional item to get
        :return: a single :class:`~cmd2.history.HistoryItem`
        """
    spanpattern: Incomplete
    def span(self, span: str, include_persisted: bool = False) -> OrderedDict[int, HistoryItem]:
        """Return a slice of the History list

        :param span: string containing an index or a slice
        :param include_persisted: if True, then retrieve full results including from persisted history
        :return: a dictionary of history items keyed by their 1-based index in ascending order,
                 or an empty dictionary if no results were found

        This method can accommodate input in any of these forms:

            a..b or a:b
            a.. or a:
            ..a or :a
            -a.. or -a:
            ..-a or :-a

        Different from native python indexing and slicing of arrays, this method
        uses 1-based array numbering. Users who are not programmers can't grok
        zero based numbering. Programmers can sometimes grok zero based numbering.
        Which reminds me, there are only two hard problems in programming:

        - naming
        - cache invalidation
        - off by one errors

        """
    def str_search(self, search: str, include_persisted: bool = False) -> OrderedDict[int, HistoryItem]:
        """Find history items which contain a given string

        :param search: the string to search for
        :param include_persisted: if True, then search full history including persisted history
        :return: a dictionary of history items keyed by their 1-based index in ascending order,
                 or an empty dictionary if the string was not found
        """
    def regex_search(self, regex: str, include_persisted: bool = False) -> OrderedDict[int, HistoryItem]:
        """Find history items which match a given regular expression

        :param regex: the regular expression to search for.
        :param include_persisted: if True, then search full history including persisted history
        :return: a dictionary of history items keyed by their 1-based index in ascending order,
                 or an empty dictionary if the regex was not matched
        """
    def truncate(self, max_length: int) -> None:
        """Truncate the length of the history, dropping the oldest items if necessary

        :param max_length: the maximum length of the history, if negative, all history
                           items will be deleted
        :return: nothing
        """
    def to_json(self) -> str:
        """Utility method to convert this History into a JSON string for use in persistent history files"""
    @staticmethod
    def from_json(history_json: str) -> History:
        """
        Utility method to restore History from a JSON string

        :param history_json: history data as JSON string (generated using to_json())
        :return: History object
        :raises json.JSONDecodeError: if passed invalid JSON string
        :raises KeyError: if JSON is missing required elements
        :raises ValueError: if history version in JSON isn't supported
        """
