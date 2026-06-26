import os
import typing as t
import typing_extensions as te
from ._compat import WIN as WIN, auto_wrap_for_ansi as auto_wrap_for_ansi, binary_streams as binary_streams, open_stream as open_stream, should_strip_ansi as should_strip_ansi, strip_ansi as strip_ansi, text_streams as text_streams
from .globals import resolve_color_default as resolve_color_default
from _typeshed import Incomplete
from types import TracebackType

P = te.ParamSpec('P')
R = t.TypeVar('R')

def safecall(func: t.Callable[P, R]) -> t.Callable[P, R | None]:
    """Wraps a function so that it swallows exceptions."""
def make_str(value: t.Any) -> str:
    """Converts a value into a valid string."""
def make_default_short_help(help: str, max_length: int = 45) -> str:
    """Returns a condensed version of help string."""

class LazyFile:
    """A lazy file works like a regular file but it does not fully open
    the file but it does perform some basic checks early to see if the
    filename parameter does make sense.  This is useful for safely opening
    files for writing.
    """
    name: Incomplete
    mode: Incomplete
    encoding: Incomplete
    errors: Incomplete
    atomic: Incomplete
    should_close: Incomplete
    def __init__(self, filename: str | os.PathLike[str], mode: str = 'r', encoding: str | None = None, errors: str | None = 'strict', atomic: bool = False) -> None: ...
    def __getattr__(self, name: str) -> t.Any: ...
    def open(self) -> t.IO[t.Any]:
        """Opens the file if it's not yet open.  This call might fail with
        a :exc:`FileError`.  Not handling this error will produce an error
        that Click shows.
        """
    def close(self) -> None:
        """Closes the underlying file, no matter what."""
    def close_intelligently(self) -> None:
        """This function only closes the file if it was opened by the lazy
        file wrapper.  For instance this will never close stdin.
        """
    def __enter__(self) -> LazyFile: ...
    def __exit__(self, exc_type: t.Type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None: ...
    def __iter__(self) -> t.Iterator[t.AnyStr]: ...

class KeepOpenFile:
    def __init__(self, file: t.IO[t.Any]) -> None: ...
    def __getattr__(self, name: str) -> t.Any: ...
    def __enter__(self) -> KeepOpenFile: ...
    def __exit__(self, exc_type: t.Type[BaseException] | None, exc_value: BaseException | None, tb: TracebackType | None) -> None: ...
    def __iter__(self) -> t.Iterator[t.AnyStr]: ...

def echo(message: t.Any | None = None, file: t.IO[t.Any] | None = None, nl: bool = True, err: bool = False, color: bool | None = None) -> None:
    """Print a message and newline to stdout or a file. This should be
    used instead of :func:`print` because it provides better support
    for different data, files, and environments.

    Compared to :func:`print`, this does the following:

    -   Ensures that the output encoding is not misconfigured on Linux.
    -   Supports Unicode in the Windows console.
    -   Supports writing to binary outputs, and supports writing bytes
        to text outputs.
    -   Supports colors and styles on Windows.
    -   Removes ANSI color and style codes if the output does not look
        like an interactive terminal.
    -   Always flushes the output.

    :param message: The string or bytes to output. Other objects are
        converted to strings.
    :param file: The file to write to. Defaults to ``stdout``.
    :param err: Write to ``stderr`` instead of ``stdout``.
    :param nl: Print a newline after the message. Enabled by default.
    :param color: Force showing or hiding colors and other styles. By
        default Click will remove color if the output does not look like
        an interactive terminal.

    .. versionchanged:: 6.0
        Support Unicode output on the Windows console. Click does not
        modify ``sys.stdout``, so ``sys.stdout.write()`` and ``print()``
        will still not support Unicode.

    .. versionchanged:: 4.0
        Added the ``color`` parameter.

    .. versionadded:: 3.0
        Added the ``err`` parameter.

    .. versionchanged:: 2.0
        Support colors on Windows if colorama is installed.
    """
def get_binary_stream(name: te.Literal['stdin', 'stdout', 'stderr']) -> t.BinaryIO:
    """Returns a system stream for byte processing.

    :param name: the name of the stream to open.  Valid names are ``'stdin'``,
                 ``'stdout'`` and ``'stderr'``
    """
def get_text_stream(name: te.Literal['stdin', 'stdout', 'stderr'], encoding: str | None = None, errors: str | None = 'strict') -> t.TextIO:
    """Returns a system stream for text processing.  This usually returns
    a wrapped stream around a binary stream returned from
    :func:`get_binary_stream` but it also can take shortcuts for already
    correctly configured streams.

    :param name: the name of the stream to open.  Valid names are ``'stdin'``,
                 ``'stdout'`` and ``'stderr'``
    :param encoding: overrides the detected default encoding.
    :param errors: overrides the default error mode.
    """
def open_file(filename: str, mode: str = 'r', encoding: str | None = None, errors: str | None = 'strict', lazy: bool = False, atomic: bool = False) -> t.IO[t.Any]:
    """Open a file, with extra behavior to handle ``'-'`` to indicate
    a standard stream, lazy open on write, and atomic write. Similar to
    the behavior of the :class:`~click.File` param type.

    If ``'-'`` is given to open ``stdout`` or ``stdin``, the stream is
    wrapped so that using it in a context manager will not close it.
    This makes it possible to use the function without accidentally
    closing a standard stream:

    .. code-block:: python

        with open_file(filename) as f:
            ...

    :param filename: The name of the file to open, or ``'-'`` for
        ``stdin``/``stdout``.
    :param mode: The mode in which to open the file.
    :param encoding: The encoding to decode or encode a file opened in
        text mode.
    :param errors: The error handling mode.
    :param lazy: Wait to open the file until it is accessed. For read
        mode, the file is temporarily opened to raise access errors
        early, then closed until it is read again.
    :param atomic: Write to a temporary file and replace the given file
        on close.

    .. versionadded:: 3.0
    """
def format_filename(filename: str | bytes | os.PathLike[str] | os.PathLike[bytes], shorten: bool = False) -> str:
    '''Format a filename as a string for display. Ensures the filename can be
    displayed by replacing any invalid bytes or surrogate escapes in the name
    with the replacement character ``�``.

    Invalid bytes or surrogate escapes will raise an error when written to a
    stream with ``errors="strict". This will typically happen with ``stdout``
    when the locale is something like ``en_GB.UTF-8``.

    Many scenarios *are* safe to write surrogates though, due to PEP 538 and
    PEP 540, including:

    -   Writing to ``stderr``, which uses ``errors="backslashreplace"``.
    -   The system has ``LANG=C.UTF-8``, ``C``, or ``POSIX``. Python opens
        stdout and stderr with ``errors="surrogateescape"``.
    -   None of ``LANG/LC_*`` are set. Python assumes ``LANG=C.UTF-8``.
    -   Python is started in UTF-8 mode  with  ``PYTHONUTF8=1`` or ``-X utf8``.
        Python opens stdout and stderr with ``errors="surrogateescape"``.

    :param filename: formats a filename for UI display.  This will also convert
                     the filename into unicode without failing.
    :param shorten: this optionally shortens the filename to strip of the
                    path that leads up to it.
    '''
def get_app_dir(app_name: str, roaming: bool = True, force_posix: bool = False) -> str:
    '''Returns the config folder for the application.  The default behavior
    is to return whatever is most appropriate for the operating system.

    To give you an idea, for an app called ``"Foo Bar"``, something like
    the following folders could be returned:

    Mac OS X:
      ``~/Library/Application Support/Foo Bar``
    Mac OS X (POSIX):
      ``~/.foo-bar``
    Unix:
      ``~/.config/foo-bar``
    Unix (POSIX):
      ``~/.foo-bar``
    Windows (roaming):
      ``C:\\Users\\<user>\\AppData\\Roaming\\Foo Bar``
    Windows (not roaming):
      ``C:\\Users\\<user>\\AppData\\Local\\Foo Bar``

    .. versionadded:: 2.0

    :param app_name: the application name.  This should be properly capitalized
                     and can contain whitespace.
    :param roaming: controls if the folder should be roaming or not on Windows.
                    Has no effect otherwise.
    :param force_posix: if this is set to `True` then on any POSIX system the
                        folder will be stored in the home folder with a leading
                        dot instead of the XDG config home or darwin\'s
                        application support folder.
    '''

class PacifyFlushWrapper:
    """This wrapper is used to catch and suppress BrokenPipeErrors resulting
    from ``.flush()`` being called on broken pipe during the shutdown/final-GC
    of the Python interpreter. Notably ``.flush()`` is always called on
    ``sys.stdout`` and ``sys.stderr``. So as to have minimal impact on any
    other cleanup code, and the case where the underlying file is not a broken
    pipe, all calls and attributes are proxied.
    """
    wrapped: Incomplete
    def __init__(self, wrapped: t.IO[t.Any]) -> None: ...
    def flush(self) -> None: ...
    def __getattr__(self, attr: str) -> t.Any: ...
