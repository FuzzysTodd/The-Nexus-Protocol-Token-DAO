from _typeshed import Incomplete

__all__ = ['Traceback', 'TracebackParseError', 'Frame', 'Code']

class _AttrDict(dict):
    def __getattr__(self, name): ...

class __traceback_maker(Exception): ...
class TracebackParseError(Exception): ...

class Code:
    """
    Class that replicates just enough of the builtin Code object to enable serialization and traceback rendering.
    """
    co_code: Incomplete
    co_filename: Incomplete
    co_name: Incomplete
    co_argcount: int
    co_kwonlyargcount: int
    co_varnames: Incomplete
    co_nlocals: int
    co_stacksize: int
    co_flags: int
    co_firstlineno: int
    def __init__(self, code) -> None: ...

class Frame:
    """
    Class that replicates just enough of the builtin Frame object to enable serialization and traceback rendering.
    """
    f_locals: Incomplete
    f_globals: Incomplete
    f_code: Incomplete
    f_lineno: Incomplete
    def __init__(self, frame) -> None: ...
    def clear(self) -> None:
        """
        For compatibility with PyPy 3.5;
        clear() was added to frame in Python 3.4
        and is called by traceback.clear_frames(), which
        in turn is called by unittest.TestCase.assertRaises
        """

class Traceback:
    """
    Class that wraps builtin Traceback objects.
    """
    tb_next: Incomplete
    tb_frame: Incomplete
    tb_lineno: Incomplete
    def __init__(self, tb) -> None: ...
    def as_traceback(self):
        """
        Convert to a builtin Traceback object that is usable for raising or rendering a stacktrace.
        """
    to_traceback = as_traceback
    def as_dict(self):
        """
        Converts to a dictionary representation. You can serialize the result to JSON as it only has
        builtin objects like dicts, lists, ints or strings.
        """
    to_dict = as_dict
    @classmethod
    def from_dict(cls, dct):
        """
        Creates an instance from a dictionary with the same structure as ``.as_dict()`` returns.
        """
    @classmethod
    def from_string(cls, string, strict: bool = True):
        """
        Creates an instance by parsing a stacktrace. Strict means that parsing stops when lines are not indented by at least two spaces
        anymore.
        """
