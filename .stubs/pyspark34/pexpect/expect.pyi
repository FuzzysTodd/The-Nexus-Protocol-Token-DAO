from .exceptions import EOF as EOF, TIMEOUT as TIMEOUT
from _typeshed import Incomplete

class Expecter:
    spawn: Incomplete
    searcher: Incomplete
    searchwindowsize: Incomplete
    lookback: Incomplete
    def __init__(self, spawn, searcher, searchwindowsize: int = -1) -> None: ...
    def do_search(self, window, freshlen): ...
    def existing_data(self): ...
    def new_data(self, data): ...
    def eof(self, err: Incomplete | None = None): ...
    def timeout(self, err: Incomplete | None = None): ...
    def errored(self) -> None: ...
    def expect_loop(self, timeout: int = -1):
        """Blocking expect"""

class searcher_string:
    """This is a plain string search helper for the spawn.expect_any() method.
    This helper class is for speed. For more powerful regex patterns
    see the helper class, searcher_re.

    Attributes:

        eof_index     - index of EOF, or -1
        timeout_index - index of TIMEOUT, or -1

    After a successful match by the search() method the following attributes
    are available:

        start - index into the buffer, first byte of match
        end   - index into the buffer, first byte after match
        match - the matching string itself

    """
    eof_index: int
    timeout_index: int
    longest_string: int
    def __init__(self, strings) -> None:
        """This creates an instance of searcher_string. This argument 'strings'
        may be a list; a sequence of strings; or the EOF or TIMEOUT types. """
    match: Incomplete
    start: Incomplete
    end: Incomplete
    def search(self, buffer, freshlen, searchwindowsize: Incomplete | None = None):
        """This searches 'buffer' for the first occurrence of one of the search
        strings.  'freshlen' must indicate the number of bytes at the end of
        'buffer' which have not been searched before. It helps to avoid
        searching the same, possibly big, buffer over and over again.

        See class spawn for the 'searchwindowsize' argument.

        If there is a match this returns the index of that string, and sets
        'start', 'end' and 'match'. Otherwise, this returns -1. """

class searcher_re:
    """This is regular expression string search helper for the
    spawn.expect_any() method. This helper class is for powerful
    pattern matching. For speed, see the helper class, searcher_string.

    Attributes:

        eof_index     - index of EOF, or -1
        timeout_index - index of TIMEOUT, or -1

    After a successful match by the search() method the following attributes
    are available:

        start - index into the buffer, first byte of match
        end   - index into the buffer, first byte after match
        match - the re.match object returned by a successful re.search

    """
    eof_index: int
    timeout_index: int
    def __init__(self, patterns) -> None:
        """This creates an instance that searches for 'patterns' Where
        'patterns' may be a list or other sequence of compiled regular
        expressions, or the EOF or TIMEOUT types."""
    start: Incomplete
    match: Incomplete
    end: Incomplete
    def search(self, buffer, freshlen, searchwindowsize: Incomplete | None = None):
        """This searches 'buffer' for the first occurrence of one of the regular
        expressions. 'freshlen' must indicate the number of bytes at the end of
        'buffer' which have not been searched before.

        See class spawn for the 'searchwindowsize' argument.

        If there is a match this returns the index of that string, and sets
        'start', 'end' and 'match'. Otherwise, returns -1."""
