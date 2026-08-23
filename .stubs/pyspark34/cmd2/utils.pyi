import argparse
from . import constants as constants
from .argparse_custom import ChoicesProviderFunc as ChoicesProviderFunc, CompleterFunc as CompleterFunc
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Callable, Dict, Iterable, List, TextIO, Type

PopenTextIO: Incomplete

def is_quoted(arg: str) -> bool:
    """
    Checks if a string is quoted

    :param arg: the string being checked for quotes
    :return: True if a string is quoted
    """
def quote_string(arg: str) -> str:
    """Quote a string"""
def quote_string_if_needed(arg: str) -> str:
    """Quote a string if it contains spaces and isn't already quoted"""
def strip_quotes(arg: str) -> str:
    """Strip outer quotes from a string.

     Applies to both single and double quotes.

    :param arg:  string to strip outer quotes from
    :return: same string with potentially outer quotes stripped
    """
def to_bool(val: Any) -> bool:
    '''Converts anything to a boolean based on its value.

    Strings like "True", "true", "False", and "false" return True, True, False, and False
    respectively. All other values are converted using bool()

    :param val: value being converted
    :return: boolean value expressed in the passed in value
    :raises: ValueError if the string does not contain a value corresponding to a boolean value
    '''

class Settable:
    """Used to configure an attribute to be settable via the set command in the CLI"""
    name: Incomplete
    val_type: Incomplete
    description: Incomplete
    settable_obj: Incomplete
    settable_attrib_name: Incomplete
    onchange_cb: Incomplete
    choices: Incomplete
    choices_provider: Incomplete
    completer: Incomplete
    def __init__(self, name: str, val_type: Type[Any] | Callable[[Any], Any], description: str, settable_object: object, *, settable_attrib_name: str | None = None, onchange_cb: Callable[[str, _T, _T], Any] | None = None, choices: Iterable[Any] | None = None, choices_provider: ChoicesProviderFunc | None = None, completer: CompleterFunc | None = None) -> None:
        """
        Settable Initializer

        :param name: name of the instance attribute being made settable
        :param val_type: callable used to cast the string value from the command line into its proper type and
                         even validate its value. Setting this to bool provides tab completion for true/false and
                         validation using to_bool(). The val_type function should raise an exception if it fails.
                         This exception will be caught and printed by Cmd.do_set().
        :param description: string describing this setting
        :param settable_object: object to which the instance attribute belongs (e.g. self)
        :param settable_attrib_name: name which displays to the user in the output of the set command.
                                     Defaults to `name` if not specified.
        :param onchange_cb: optional function or method to call when the value of this settable is altered
                            by the set command. (e.g. onchange_cb=self.debug_changed)

                            Cmd.do_set() passes the following 3 arguments to onchange_cb:
                                param_name: str - name of the changed parameter
                                old_value: Any - the value before being changed
                                new_value: Any - the value after being changed

        The following optional settings provide tab completion for a parameter's values. They correspond to the
        same settings in argparse-based tab completion. A maximum of one of these should be provided.

        :param choices: iterable of accepted values
        :param choices_provider: function that provides choices for this argument
        :param completer: tab completion function that provides choices for this argument
        """
    def get_value(self) -> Any:
        """
        Get the value of the settable attribute
        :return:
        """
    def set_value(self, value: Any) -> Any:
        """
        Set the settable attribute on the specified destination object
        :param value: New value to set
        :return: New value that the attribute was set to
        """

def is_text_file(file_path: str) -> bool:
    """Returns if a file contains only ASCII or UTF-8 encoded text and isn't empty.

    :param file_path: path to the file being checked
    :return: True if the file is a non-empty text file, otherwise False
    :raises OSError if file can't be read
    """
def remove_duplicates(list_to_prune: List[_T]) -> List[_T]:
    """Removes duplicates from a list while preserving order of the items.

    :param list_to_prune: the list being pruned of duplicates
    :return: The pruned list
    """
def norm_fold(astr: str) -> str:
    """Normalize and casefold Unicode strings for saner comparisons.

    :param astr: input unicode string
    :return: a normalized and case-folded version of the input string
    """
def alphabetical_sort(list_to_sort: Iterable[str]) -> List[str]:
    """Sorts a list of strings alphabetically.

    For example: ['a1', 'A11', 'A2', 'a22', 'a3']

    To sort a list in place, don't call this method, which makes a copy. Instead, do this:

    my_list.sort(key=norm_fold)

    :param list_to_sort: the list being sorted
    :return: the sorted list
    """
def try_int_or_force_to_lower_case(input_str: str) -> int | str:
    """
    Tries to convert the passed-in string to an integer. If that fails, it converts it to lower case using norm_fold.
    :param input_str: string to convert
    :return: the string as an integer or a lower case version of the string
    """
def natural_keys(input_str: str) -> List[int | str]:
    """
    Converts a string into a list of integers and strings to support natural sorting (see natural_sort).

    For example: natural_keys('abc123def') -> ['abc', '123', 'def']
    :param input_str: string to convert
    :return: list of strings and integers
    """
def natural_sort(list_to_sort: Iterable[str]) -> List[str]:
    """
    Sorts a list of strings case insensitively as well as numerically.

    For example: ['a1', 'A2', 'a3', 'A11', 'a22']

    To sort a list in place, don't call this method, which makes a copy. Instead, do this:

    my_list.sort(key=natural_keys)

    :param list_to_sort: the list being sorted
    :return: the list sorted naturally
    """
def quote_specific_tokens(tokens: List[str], tokens_to_quote: List[str]) -> None:
    """
    Quote specific tokens in a list

    :param tokens: token list being edited
    :param tokens_to_quote: the tokens, which if present in tokens, to quote
    """
def unquote_specific_tokens(tokens: List[str], tokens_to_unquote: List[str]) -> None:
    """
    Unquote specific tokens in a list

    :param tokens: token list being edited
    :param tokens_to_unquote: the tokens, which if present in tokens, to unquote
    """
def expand_user(token: str) -> str:
    """
    Wrap os.expanduser() to support expanding ~ in quoted strings
    :param token: the string to expand
    """
def expand_user_in_tokens(tokens: List[str]) -> None:
    """
    Call expand_user() on all tokens in a list of strings
    :param tokens: tokens to expand
    """
def find_editor() -> str | None:
    """
    Used to set cmd2.Cmd.DEFAULT_EDITOR. If EDITOR env variable is set, that will be used.
    Otherwise the function will look for a known editor in directories specified by PATH env variable.
    :return: Default editor or None
    """
def files_from_glob_pattern(pattern: str, access: int = ...) -> List[str]:
    """Return a list of file paths based on a glob pattern.

    Only files are returned, not directories, and optionally only files for which the user has a specified access to.

    :param pattern: file name or glob pattern
    :param access: file access type to verify (os.* where * is F_OK, R_OK, W_OK, or X_OK)
    :return: list of files matching the name or glob pattern
    """
def files_from_glob_patterns(patterns: List[str], access: int = ...) -> List[str]:
    """Return a list of file paths based on a list of glob patterns.

    Only files are returned, not directories, and optionally only files for which the user has a specified access to.

    :param patterns: list of file names and/or glob patterns
    :param access: file access type to verify (os.* where * is F_OK, R_OK, W_OK, or X_OK)
    :return: list of files matching the names and/or glob patterns
    """
def get_exes_in_path(starts_with: str) -> List[str]:
    """Returns names of executables in a user's path

    :param starts_with: what the exes should start with. leave blank for all exes in path.
    :return: a list of matching exe names
    """

class StdSim:
    """
    Class to simulate behavior of sys.stdout or sys.stderr.
    Stores contents in internal buffer and optionally echos to the inner stream it is simulating.
    """
    inner_stream: Incomplete
    echo: Incomplete
    encoding: Incomplete
    errors: Incomplete
    pause_storage: bool
    buffer: Incomplete
    def __init__(self, inner_stream: TextIO | StdSim, *, echo: bool = False, encoding: str = 'utf-8', errors: str = 'replace') -> None:
        """
        StdSim Initializer

        :param inner_stream: the wrapped stream. Should be a TextIO or StdSim instance.
        :param echo: if True, then all input will be echoed to inner_stream
        :param encoding: codec for encoding/decoding strings (defaults to utf-8)
        :param errors: how to handle encoding/decoding errors (defaults to replace)
        """
    def write(self, s: str) -> None:
        """
        Add str to internal bytes buffer and if echo is True, echo contents to inner stream

        :param s: String to write to the stream
        """
    def getvalue(self) -> str:
        """Get the internal contents as a str"""
    def getbytes(self) -> bytes:
        """Get the internal contents as bytes"""
    def read(self, size: int | None = -1) -> str:
        """
        Read from the internal contents as a str and then clear them out

        :param size: Number of bytes to read from the stream
        """
    def readbytes(self) -> bytes:
        """Read from the internal contents as bytes and then clear them out"""
    def clear(self) -> None:
        """Clear the internal contents"""
    def isatty(self) -> bool:
        """StdSim only considered an interactive stream if `echo` is True and `inner_stream` is a tty."""
    @property
    def line_buffering(self) -> bool:
        """
        Handle when the inner stream doesn't have a line_buffering attribute which is the case
        when running unit tests because pytest sets stdout to a pytest EncodedFile object.
        """
    def __getattr__(self, item: str) -> Any: ...

class ByteBuf:
    """
    Used by StdSim to write binary data and stores the actual bytes written
    """
    NEWLINES: Incomplete
    byte_buf: Incomplete
    std_sim_instance: Incomplete
    def __init__(self, std_sim_instance: StdSim) -> None: ...
    def write(self, b: bytes) -> None:
        """Add bytes to internal bytes buffer and if echo is True, echo contents to inner stream."""

class ProcReader:
    """
    Used to capture stdout and stderr from a Popen process if any of those were set to subprocess.PIPE.
    If neither are pipes, then the process will run normally and no output will be captured.
    """
    def __init__(self, proc: PopenTextIO, stdout: StdSim | TextIO, stderr: StdSim | TextIO) -> None:
        """
        ProcReader initializer
        :param proc: the Popen process being read from
        :param stdout: the stream to write captured stdout
        :param stderr: the stream to write captured stderr
        """
    def send_sigint(self) -> None:
        """Send a SIGINT to the process similar to if <Ctrl>+C were pressed"""
    def terminate(self) -> None:
        """Terminate the process"""
    def wait(self) -> None:
        """Wait for the process to finish"""

class ContextFlag:
    """A context manager which is also used as a boolean flag value within the default sigint handler.

    Its main use is as a flag to prevent the SIGINT handler in cmd2 from raising a KeyboardInterrupt
    while a critical code section has set the flag to True. Because signal handling is always done on the
    main thread, this class is not thread-safe since there is no need.
    """
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Any) -> None: ...

class RedirectionSavedState:
    """Created by each command to store information required to restore state after redirection"""
    redirecting: bool
    saved_self_stdout: Incomplete
    saved_sys_stdout: Incomplete
    saved_pipe_proc_reader: Incomplete
    saved_redirecting: Incomplete
    def __init__(self, self_stdout: StdSim | TextIO, sys_stdout: StdSim | TextIO, pipe_proc_reader: ProcReader | None, saved_redirecting: bool) -> None:
        """
        RedirectionSavedState initializer
        :param self_stdout: saved value of Cmd.stdout
        :param sys_stdout: saved value of sys.stdout
        :param pipe_proc_reader: saved value of Cmd._cur_pipe_proc_reader
        :param saved_redirecting: saved value of Cmd._redirecting
        """

class TextAlignment(Enum):
    """Horizontal text alignment"""
    LEFT: int
    CENTER: int
    RIGHT: int

def align_text(text: str, alignment: TextAlignment, *, fill_char: str = ' ', width: int | None = None, tab_width: int = 4, truncate: bool = False) -> str:
    """
    Align text for display within a given width. Supports characters with display widths greater than 1.
    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    There are convenience wrappers around this function: align_left(), align_center(), and align_right()

    :param text: text to align (can contain multiple lines)
    :param alignment: how to align the text
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then each line will be shortened to fit within the display width. The truncated
                     portions are replaced by a '…' character. Defaults to False.
    :return: aligned text
    :raises: TypeError if fill_char is more than one character (not including ANSI style sequences)
    :raises: ValueError if text or fill_char contains an unprintable character
    :raises: ValueError if width is less than 1
    """
def align_left(text: str, *, fill_char: str = ' ', width: int | None = None, tab_width: int = 4, truncate: bool = False) -> str:
    """
    Left align text for display within a given width. Supports characters with display widths greater than 1.
    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    :param text: text to left align (can contain multiple lines)
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then text will be shortened to fit within the display width. The truncated portion is
                     replaced by a '…' character. Defaults to False.
    :return: left-aligned text
    :raises: TypeError if fill_char is more than one character (not including ANSI style sequences)
    :raises: ValueError if text or fill_char contains an unprintable character
    :raises: ValueError if width is less than 1
    """
def align_center(text: str, *, fill_char: str = ' ', width: int | None = None, tab_width: int = 4, truncate: bool = False) -> str:
    """
    Center text for display within a given width. Supports characters with display widths greater than 1.
    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    :param text: text to center (can contain multiple lines)
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then text will be shortened to fit within the display width. The truncated portion is
                     replaced by a '…' character. Defaults to False.
    :return: centered text
    :raises: TypeError if fill_char is more than one character (not including ANSI style sequences)
    :raises: ValueError if text or fill_char contains an unprintable character
    :raises: ValueError if width is less than 1
    """
def align_right(text: str, *, fill_char: str = ' ', width: int | None = None, tab_width: int = 4, truncate: bool = False) -> str:
    """
    Right align text for display within a given width. Supports characters with display widths greater than 1.
    ANSI style sequences do not count toward the display width. If text has line breaks, then each line is aligned
    independently.

    :param text: text to right align (can contain multiple lines)
    :param fill_char: character that fills the alignment gap. Defaults to space. (Cannot be a line breaking character)
    :param width: display width of the aligned text. Defaults to width of the terminal.
    :param tab_width: any tabs in the text will be replaced with this many spaces. if fill_char is a tab, then it will
                      be converted to one space.
    :param truncate: if True, then text will be shortened to fit within the display width. The truncated portion is
                     replaced by a '…' character. Defaults to False.
    :return: right-aligned text
    :raises: TypeError if fill_char is more than one character (not including ANSI style sequences)
    :raises: ValueError if text or fill_char contains an unprintable character
    :raises: ValueError if width is less than 1
    """
def truncate_line(line: str, max_width: int, *, tab_width: int = 4) -> str:
    '''
    Truncate a single line to fit within a given display width. Any portion of the string that is truncated
    is replaced by a \'…\' character. Supports characters with display widths greater than 1. ANSI style sequences
    do not count toward the display width.

    If there are ANSI style sequences in the string after where truncation occurs, this function will append them
    to the returned string.

    This is done to prevent issues caused in cases like: truncate_line(Fg.BLUE + hello + Fg.RESET, 3)
    In this case, "hello" would be truncated before Fg.RESET resets the color from blue. Appending the remaining style
    sequences makes sure the style is in the same state had the entire string been printed. align_text() relies on this
    behavior when preserving style over multiple lines.

    :param line: text to truncate
    :param max_width: the maximum display width the resulting string is allowed to have
    :param tab_width: any tabs in the text will be replaced with this many spaces
    :return: line that has a display width less than or equal to width
    :raises: ValueError if text contains an unprintable character like a newline
    :raises: ValueError if max_width is less than 1
    '''
def get_styles_dict(text: str) -> Dict[int, str]:
    """
    Return an OrderedDict containing all ANSI style sequences found in a string

    The structure of the dictionary is:
        key: index where sequences begins
        value: ANSI style sequence found at index in text

    Keys are in ascending order

    :param text: text to search for style sequences
    """
def categorize(func: Callable[..., Any] | Iterable[Callable[..., Any]], category: str) -> None:
    '''Categorize a function.

    The help command output will group the passed function under the
    specified category heading

    :param func: function or list of functions to categorize
    :param category: category to put it in

    :Example:

    >>> import cmd2
    >>> class MyApp(cmd2.Cmd):
    >>>   def do_echo(self, arglist):
    >>>     self.poutput(\' \'.join(arglist)
    >>>
    >>>   cmd2.utils.categorize(do_echo, "Text Processing")

    For an alternative approach to categorizing commands using a decorator, see
    :func:`~cmd2.decorators.with_category`
    '''
def get_defining_class(meth: Callable[..., Any]) -> Type[Any] | None:
    """
    Attempts to resolve the class that defined a method.

    Inspired by implementation published here:
        https://stackoverflow.com/a/25959545/1956611

    :param meth: method to inspect
    :return: class type in which the supplied method was defined. None if it couldn't be resolved.
    """

class CompletionMode(Enum):
    """Enum for what type of tab completion to perform in cmd2.Cmd.read_input()"""
    NONE: int
    COMMANDS: int
    CUSTOM: int

class CustomCompletionSettings:
    """Used by cmd2.Cmd.complete() to tab complete strings other than command arguments"""
    parser: Incomplete
    preserve_quotes: Incomplete
    def __init__(self, parser: argparse.ArgumentParser, *, preserve_quotes: bool = False) -> None:
        """
        Initializer

        :param parser: arg parser defining format of string being tab completed
        :param preserve_quotes: if True, then quoted tokens will keep their quotes when processed by
                                ArgparseCompleter. This is helpful in cases when you're tab completing
                                flag-like tokens (e.g. -o, --option) and you don't want them to be
                                treated as argparse flags when quoted. Set this to True if you plan
                                on passing the string to argparse with the tokens still quoted.
        """

def strip_doc_annotations(doc: str) -> str:
    """
    Strip annotations from a docstring leaving only the text description

    :param doc: documentation string
    """
