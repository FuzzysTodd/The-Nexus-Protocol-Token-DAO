import traceback
from ._exceptions import BaseExceptionGroup as BaseExceptionGroup
from _typeshed import Incomplete
from collections.abc import Generator
from types import TracebackType
from typing import Any, List

max_group_width: int
max_group_depth: int

class _ExceptionPrintContext:
    seen: Incomplete
    exception_group_depth: int
    need_close: bool
    def __init__(self) -> None: ...
    def indent(self): ...
    def emit(self, text_gen, margin_char: Incomplete | None = None) -> Generator[Incomplete, None, Incomplete]: ...

def exceptiongroup_excepthook(etype: type[BaseException], value: BaseException, tb: TracebackType | None) -> None: ...

class PatchedTracebackException(traceback.TracebackException):
    stack: Incomplete
    exc_type: Incomplete
    __notes__: Incomplete
    filename: Incomplete
    lineno: Incomplete
    text: Incomplete
    offset: Incomplete
    msg: Incomplete
    end_lineno: Incomplete
    end_offset: Incomplete
    __suppress_context__: Incomplete
    def __init__(self, exc_type: type[BaseException], exc_value: BaseException, exc_traceback: TracebackType | None, *, limit: int | None = None, lookup_lines: bool = True, capture_locals: bool = False, compact: bool = False, _seen: set[int] | None = None) -> None: ...
    def format(self, *, chain: bool = True, _ctx: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
    def format_exception_only(self) -> Generator[Incomplete, Incomplete, None]:
        """Format the exception part of the traceback.
        The return value is a generator of strings, each ending in a newline.
        Normally, the generator emits a single string; however, for
        SyntaxError exceptions, it emits several lines that (when
        printed) display detailed information about where the syntax
        error occurred.
        The message indicating which exception occurred is always the last
        string in the output.
        """

traceback_exception_original_format: Incomplete
traceback_exception_original_format_exception_only: Incomplete
traceback_exception_format_syntax_error: Incomplete

def format_exception_only(__exc: BaseException) -> List[str]: ...
def _(__exc: type, value: BaseException) -> List[str]: ...
def format_exception(__exc: BaseException, limit: int | None = None, chain: bool = True) -> List[str]: ...
def print_exception(__exc: BaseException, limit: int | None = None, file: Any = None, chain: bool = True) -> None: ...
def print_exc(limit: int | None = None, file: Any | None = None, chain: bool = True) -> None: ...
