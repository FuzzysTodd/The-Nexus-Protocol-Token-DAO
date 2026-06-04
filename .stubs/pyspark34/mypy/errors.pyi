from _typeshed import Incomplete
from mypy.errorcodes import ErrorCode as ErrorCode, IMPORT as IMPORT
from mypy.message_registry import ErrorMessage as ErrorMessage
from mypy.options import Options as Options
from mypy.scope import Scope as Scope
from mypy.util import DEFAULT_SOURCE_OFFSET as DEFAULT_SOURCE_OFFSET, is_typeshed_file as is_typeshed_file
from typing import Callable, Iterable, NoReturn, TextIO, TypeVar
from typing_extensions import Final, Literal, TypeAlias as _TypeAlias

T = TypeVar('T')
SHOW_NOTE_CODES: Final[Incomplete]
allowed_duplicates: Final[Incomplete]
original_error_codes: Final[Incomplete]

class ErrorInfo:
    """Representation of a single error message."""
    import_ctx: list[tuple[str, int]]
    file: str
    module: str | None
    type: str | None
    function_or_member: str | None
    line: int
    column: int
    end_line: int
    end_column: int
    severity: str
    message: str
    code: ErrorCode | None
    blocker: bool
    only_once: bool
    allow_dups: bool
    origin: tuple[str, Iterable[int]]
    target: str | None
    hidden: bool
    def __init__(self, import_ctx: list[tuple[str, int]], file: str, module: str | None, typ: str | None, function_or_member: str | None, line: int, column: int, end_line: int, end_column: int, severity: str, message: str, code: ErrorCode | None, blocker: bool, only_once: bool, allow_dups: bool, origin: tuple[str, Iterable[int]] | None = None, target: str | None = None) -> None: ...

ErrorTuple: _TypeAlias

class ErrorWatcher:
    """Context manager that can be used to keep track of new errors recorded
    around a given operation.

    Errors maintain a stack of such watchers. The handler is called starting
    at the top of the stack, and is propagated down the stack unless filtered
    out by one of the ErrorWatcher instances.
    """
    errors: Incomplete
    def __init__(self, errors: Errors, *, filter_errors: bool | Callable[[str, ErrorInfo], bool] = False, save_filtered_errors: bool = False) -> None: ...
    def __enter__(self) -> ErrorWatcher: ...
    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> Literal[False]: ...
    def on_error(self, file: str, info: ErrorInfo) -> bool:
        """Handler called when a new error is recorded.

        The default implementation just sets the has_new_errors flag

        Return True to filter out the error, preventing it from being seen by other
        ErrorWatcher further down the stack and from being recorded by Errors
        """
    def has_new_errors(self) -> bool: ...
    def filtered_errors(self) -> list[ErrorInfo]: ...

class Errors:
    """Container for compile errors.

    This class generates and keeps tracks of compile errors and the
    current error context (nested imports).
    """
    error_info_map: dict[str, list[ErrorInfo]]
    has_blockers: set[str]
    flushed_files: set[str]
    import_ctx: list[tuple[str, int]]
    ignore_prefix: str | None
    file: str
    ignored_lines: dict[str, dict[int, list[str]]]
    unreachable_lines: dict[str, set[int]]
    used_ignored_lines: dict[str, dict[int, list[str]]]
    ignored_files: set[str]
    only_once_messages: set[str]
    show_error_context: bool
    show_column_numbers: bool
    show_error_end: bool
    show_absolute_path: bool
    target_module: str | None
    scope: Scope | None
    seen_import_error: bool
    options: Incomplete
    hide_error_codes: Incomplete
    read_source: Incomplete
    def __init__(self, options: Options, *, read_source: Callable[[str], list[str] | None] | None = None, hide_error_codes: bool | None = None) -> None: ...
    function_or_member: Incomplete
    def initialize(self) -> None: ...
    def reset(self) -> None: ...
    def set_ignore_prefix(self, prefix: str) -> None:
        """Set path prefix that will be removed from all paths."""
    def simplify_path(self, file: str) -> str: ...
    def set_file(self, file: str, module: str | None, options: Options, scope: Scope | None = None) -> None:
        """Set the path and module id of the current file."""
    def set_file_ignored_lines(self, file: str, ignored_lines: dict[int, list[str]], ignore_all: bool = False) -> None: ...
    def set_unreachable_lines(self, file: str, unreachable_lines: set[int]) -> None: ...
    def current_target(self) -> str | None:
        """Retrieves the current target from the associated scope.

        If there is no associated scope, use the target module."""
    def current_module(self) -> str | None: ...
    def import_context(self) -> list[tuple[str, int]]:
        """Return a copy of the import context."""
    def set_import_context(self, ctx: list[tuple[str, int]]) -> None:
        """Replace the entire import context with a new value."""
    def report(self, line: int, column: int | None, message: str, code: ErrorCode | None = None, *, blocker: bool = False, severity: str = 'error', file: str | None = None, only_once: bool = False, allow_dups: bool = False, origin_span: Iterable[int] | None = None, offset: int = 0, end_line: int | None = None, end_column: int | None = None) -> None:
        """Report message at the given line using the current error context.

        Args:
            line: line number of error
            column: column number of error
            message: message to report
            code: error code (defaults to 'misc'; not shown for notes)
            blocker: if True, don't continue analysis after this error
            severity: 'error' or 'note'
            file: if non-None, override current file as context
            only_once: if True, only report this exact message once per build
            allow_dups: if True, allow duplicate copies of this message (ignored if only_once)
            origin_span: if non-None, override current context as origin
                         (type: ignores have effect here)
            end_line: if non-None, override current context as end
        """
    def add_error_info(self, info: ErrorInfo) -> None: ...
    def has_many_errors(self) -> bool: ...
    def report_hidden_errors(self, info: ErrorInfo) -> None: ...
    def is_ignored_error(self, line: int, info: ErrorInfo, ignores: dict[int, list[str]]) -> bool: ...
    def is_error_code_enabled(self, error_code: ErrorCode) -> bool: ...
    def clear_errors_in_targets(self, path: str, targets: set[str]) -> None:
        """Remove errors in specific fine-grained targets within a file."""
    def generate_unused_ignore_errors(self, file: str) -> None: ...
    def generate_ignore_without_code_errors(self, file: str, is_warning_unused_ignores: bool) -> None: ...
    def num_messages(self) -> int:
        """Return the number of generated messages."""
    def is_errors(self) -> bool:
        """Are there any generated messages?"""
    def is_blockers(self) -> bool:
        """Are the any errors that are blockers?"""
    def blocker_module(self) -> str | None:
        """Return the module with a blocking error, or None if not possible."""
    def is_errors_for_file(self, file: str) -> bool:
        """Are there any errors for the given file?"""
    def prefer_simple_messages(self) -> bool:
        """Should we generate simple/fast error messages?

        Return True if errors are not shown to user, i.e. errors are ignored
        or they are collected for internal use only.

        If True, we should prefer to generate a simple message quickly.
        All normal errors should still be reported.
        """
    def raise_error(self, use_stdout: bool = True) -> NoReturn:
        """Raise a CompileError with the generated messages.

        Render the messages suitable for displaying.
        """
    def format_messages(self, error_info: list[ErrorInfo], source_lines: list[str] | None) -> list[str]:
        """Return a string list that represents the error messages.

        Use a form suitable for displaying to the user. If self.pretty
        is True also append a relevant trimmed source code line (only for
        severity 'error').
        """
    def file_messages(self, path: str) -> list[str]:
        """Return a string list of new error messages from a given file.

        Use a form suitable for displaying to the user.
        """
    def new_messages(self) -> list[str]:
        """Return a string list of new error messages.

        Use a form suitable for displaying to the user.
        Errors from different files are ordered based on the order in which
        they first generated an error.
        """
    def targets(self) -> set[str]:
        """Return a set of all targets that contain errors."""
    def render_messages(self, errors: list[ErrorInfo]) -> list[ErrorTuple]:
        """Translate the messages into a sequence of tuples.

        Each tuple is of form (path, line, col, severity, message, allow_dups, code).
        The rendered sequence includes information about error contexts.
        The path item may be None. If the line item is negative, the
        line number is not defined for the tuple.
        """
    def sort_messages(self, errors: list[ErrorInfo]) -> list[ErrorInfo]:
        """Sort an array of error messages locally by line number.

        I.e., sort a run of consecutive messages with the same
        context by line number, but otherwise retain the general
        ordering of the messages.
        """
    def remove_duplicates(self, errors: list[ErrorTuple]) -> list[ErrorTuple]:
        """Remove duplicates from a sorted error list."""

class CompileError(Exception):
    """Exception raised when there is a compile error.

    It can be a parse, semantic analysis, type check or other
    compilation-related error.

    CompileErrors raised from an errors object carry all of the
    messages that have not been reported out by error streaming.
    This is patched up by build.build to contain either all error
    messages (if errors were streamed) or none (if they were not).

    """
    messages: list[str]
    use_stdout: bool
    module_with_blocker: str | None
    def __init__(self, messages: list[str], use_stdout: bool = False, module_with_blocker: str | None = None) -> None: ...

def remove_path_prefix(path: str, prefix: str | None) -> str:
    """If path starts with prefix, return copy of path with the prefix removed.
    Otherwise, return path. If path is None, return None.
    """
def report_internal_error(err: Exception, file: str | None, line: int, errors: Errors, options: Options, stdout: TextIO | None = None, stderr: TextIO | None = None) -> NoReturn:
    """Report internal error and exit.

    This optionally starts pdb or shows a traceback.
    """
