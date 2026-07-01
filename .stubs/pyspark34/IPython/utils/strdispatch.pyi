from IPython.core.hooks import CommandChainDispatcher as CommandChainDispatcher
from _typeshed import Incomplete
from collections.abc import Generator

class StrDispatch:
    """Dispatch (lookup) a set of strings / regexps for match.

    Example:

    >>> dis = StrDispatch()
    >>> dis.add_s('hei',34, priority = 4)
    >>> dis.add_s('hei',123, priority = 2)
    >>> dis.add_re('h.i', 686)
    >>> print(list(dis.flat_matches('hei')))
    [123, 34, 686]
    """
    strs: Incomplete
    regexs: Incomplete
    def __init__(self) -> None: ...
    def add_s(self, s, obj, priority: int = 0) -> None:
        """ Adds a target 'string' for dispatching """
    def add_re(self, regex, obj, priority: int = 0) -> None:
        """ Adds a target regexp for dispatching """
    def dispatch(self, key) -> Generator[Incomplete, None, None]:
        """ Get a seq of Commandchain objects that match key """
    def s_matches(self, key) -> Generator[Incomplete, None, None]: ...
    def flat_matches(self, key) -> Generator[Incomplete, None, None]:
        """ Yield all 'value' targets, without priority """
