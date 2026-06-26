import time
from _typeshed import Incomplete
from typing import Callable, Container, IO, Iterable, Sequence, Sized, TypeVar
from typing_extensions import Final, Literal

CURSES_ENABLED: bool
T = TypeVar('T')
TYPESHED_DIR: Final[Incomplete]
ENCODING_RE: Final[Incomplete]
DEFAULT_SOURCE_OFFSET: Final[int]
DEFAULT_COLUMNS: Final[int]
MINIMUM_WIDTH: Final[int]
MINIMUM_WINDOWS_MAJOR_VT100: Final[int]
MINIMUM_WINDOWS_BUILD_VT100: Final[int]
SPECIAL_DUNDERS: Final[Incomplete]

def is_dunder(name: str, exclude_special: bool = False) -> bool:
    """Returns whether name is a dunder name.

    Args:
        exclude_special: Whether to return False for a couple special dunder methods.

    """
def is_sunder(name: str) -> bool: ...
def split_module_names(mod_name: str) -> list[str]:
    """Return the module and all parent module names.

    So, if `mod_name` is 'a.b.c', this function will return
    ['a.b.c', 'a.b', and 'a'].
    """
def module_prefix(modules: Iterable[str], target: str) -> str | None: ...
def split_target(modules: Iterable[str], target: str) -> tuple[str, str] | None: ...
def short_type(obj: object) -> str:
    """Return the last component of the type name of an object.

    If obj is None, return 'nil'. For example, if obj is 1, return 'int'.
    """
def find_python_encoding(text: bytes) -> tuple[str, int]:
    """PEP-263 for detecting Python file encoding"""
def bytes_to_human_readable_repr(b: bytes) -> str:
    """Converts bytes into some human-readable representation. Unprintable
    bytes such as the nul byte are escaped. For example:

        >>> b = bytes([102, 111, 111, 10, 0])
        >>> s = bytes_to_human_readable_repr(b)
        >>> print(s)
        foo
\x00
        >>> print(repr(s))
        'foo\\n\\x00'
    """

class DecodeError(Exception):
    """Exception raised when a file cannot be decoded due to an unknown encoding type.

    Essentially a wrapper for the LookupError raised by `bytearray.decode`
    """

def decode_python_encoding(source: bytes) -> str:
    """Read the Python file with while obeying PEP-263 encoding detection.

    Returns the source as a string.
    """
def read_py_file(path: str, read: Callable[[str], bytes]) -> list[str] | None:
    """Try reading a Python file as list of source lines.

    Return None if something goes wrong.
    """
def trim_source_line(line: str, max_len: int, col: int, min_width: int) -> tuple[str, int]:
    """Trim a line of source code to fit into max_len.

    Show 'min_width' characters on each side of 'col' (an error location). If either
    start or end is trimmed, this is indicated by adding '...' there.
    A typical result looks like this:
        ...some_variable = function_to_call(one_arg, other_arg) or...

    Return the trimmed string and the column offset to to adjust error location.
    """
def get_mypy_comments(source: str) -> list[tuple[int, str]]: ...

PASS_TEMPLATE: Final[str]
FAIL_TEMPLATE: Final[str]
ERROR_TEMPLATE: Final[str]

def write_junit_xml(dt: float, serious: bool, messages: list[str], path: str, version: str, platform: str) -> None: ...

class IdMapper:
    """Generate integer ids for objects.

    Unlike id(), these start from 0 and increment by 1, and ids won't
    get reused across the life-time of IdMapper.

    Assume objects don't redefine __eq__ or __hash__.
    """
    id_map: Incomplete
    next_id: int
    def __init__(self) -> None: ...
    def id(self, o: object) -> int: ...

def get_prefix(fullname: str) -> str:
    """Drop the final component of a qualified name (e.g. ('x.y' -> 'x')."""
def get_top_two_prefixes(fullname: str) -> tuple[str, str]:
    """Return one and two component prefixes of a fully qualified name.

    Given 'a.b.c.d', return ('a', 'a.b').

    If fullname has only one component, return (fullname, fullname).
    """
def correct_relative_import(cur_mod_id: str, relative: int, target: str, is_cur_package_init_file: bool) -> tuple[str, bool]: ...

fields_cache: Final[dict[type[object], list[str]]]

def get_class_descriptors(cls) -> Sequence[str]: ...
def replace_object_state(new: object, old: object, copy_dict: bool = False, skip_slots: tuple[str, ...] = ()) -> None:
    """Copy state of old node to the new node.

    This handles cases where there is __dict__ and/or attribute descriptors
    (either from slots or because the type is defined in a C extension module).

    Assume that both objects have the same __class__.
    """
def is_sub_path(path1: str, path2: str) -> bool:
    """Given two paths, return if path1 is a sub-path of path2."""
def hard_exit(status: int = 0) -> None:
    """Kill the current process without fully cleaning up.

    This can be quite a bit faster than a normal exit() since objects are not freed.
    """
def unmangle(name: str) -> str:
    """Remove internal suffixes from a short name."""
def get_unique_redefinition_name(name: str, existing: Container[str]) -> str:
    """Get a simple redefinition name not present among existing.

    For example, for name 'foo' we try 'foo-redefinition', 'foo-redefinition2',
    'foo-redefinition3', etc. until we find one that is not in existing.
    """
def check_python_version(program: str) -> None:
    """Report issues with the Python used to run mypy, dmypy, or stubgen"""
def count_stats(messages: list[str]) -> tuple[int, int, int]:
    """Count total number of errors, notes and error_files in message list."""
def split_words(msg: str) -> list[str]:
    """Split line of text into words (but not within quoted groups)."""
def get_terminal_width() -> int:
    """Get current terminal width if possible, otherwise return the default one."""
def soft_wrap(msg: str, max_len: int, first_offset: int, num_indent: int = 0) -> str:
    '''Wrap a long error message into few lines.

    Breaks will only happen between words, and never inside a quoted group
    (to avoid breaking types such as "Union[int, str]"). The \'first_offset\' is
    the width before the start of first line.

    Pad every next line with \'num_indent\' spaces. Every line will be at most \'max_len\'
    characters, except if it is a single word or quoted group.

    For example:
               first_offset
        ------------------------
        path/to/file: error: 58: Some very long error message
            that needs to be split in separate lines.
            "Long[Type, Names]" are never split.
        ^^^^--------------------------------------------------
        num_indent           max_len
    '''
def hash_digest(data: bytes) -> str:
    """Compute a hash digest of some data.

    We use a cryptographic hash because we want a low probability of
    accidental collision, but we don't really care about any of the
    cryptographic properties.
    """
def parse_gray_color(cup: bytes) -> str:
    """Reproduce a gray color in ANSI escape sequence"""
def should_force_color() -> bool: ...

class FancyFormatter:
    """Apply color and bold font to terminal output.

    This currently only works on Linux and Mac.
    """
    hide_error_codes: Incomplete
    dummy_term: bool
    colors: Incomplete
    def __init__(self, f_out: IO[str], f_err: IO[str], hide_error_codes: bool) -> None: ...
    BOLD: str
    UNDER: str
    BLUE: str
    GREEN: str
    RED: str
    YELLOW: str
    NORMAL: str
    DIM: str
    def initialize_vt100_colors(self) -> bool:
        """Return True if initialization was successful and we can use colors, False otherwise"""
    def initialize_win_colors(self) -> bool:
        """Return True if initialization was successful and we can use colors, False otherwise"""
    def initialize_unix_colors(self) -> bool:
        """Return True if initialization was successful and we can use colors, False otherwise"""
    def style(self, text: str, color: Literal['red', 'green', 'blue', 'yellow', 'none'], bold: bool = False, underline: bool = False, dim: bool = False) -> str:
        """Apply simple color and style (underlined or bold)."""
    def fit_in_terminal(self, messages: list[str], fixed_terminal_width: int | None = None) -> list[str]:
        """Improve readability by wrapping error messages and trimming source code."""
    def colorize(self, error: str) -> str:
        """Colorize an output line by highlighting the status and error code."""
    def highlight_quote_groups(self, msg: str) -> str:
        """Make groups quoted with double quotes bold (including quotes).

        This is used to highlight types, attribute names etc.
        """
    def underline_link(self, note: str) -> str:
        """Underline a link in a note message (if any).

        This assumes there is at most one link in the message.
        """
    def format_success(self, n_sources: int, use_color: bool = True) -> str:
        """Format short summary in case of success.

        n_sources is total number of files passed directly on command line,
        i.e. excluding stubs and followed imports.
        """
    def format_error(self, n_errors: int, n_files: int, n_sources: int, *, blockers: bool = False, use_color: bool = True) -> str:
        """Format a short summary in case of errors."""

def is_typeshed_file(typeshed_dir: str | None, file: str) -> bool: ...
def is_stub_package_file(file: str) -> bool: ...
def unnamed_function(name: str | None) -> bool: ...
time_ref = time.perf_counter_ns

def time_spent_us(t0: int) -> int: ...
def plural_s(s: int | Sized) -> str: ...
