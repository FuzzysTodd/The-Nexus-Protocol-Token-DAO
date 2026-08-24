from .capture import CapturedIO as CapturedIO, capture_output as capture_output
from IPython.utils.decorators import undoc as undoc
from _typeshed import Incomplete

class Tee:
    """A class to duplicate an output stream to stdout/err.

    This works in a manner very similar to the Unix 'tee' command.

    When the object is closed or deleted, it closes the original file given to
    it for duplication.
    """
    file: Incomplete
    channel: Incomplete
    ostream: Incomplete
    def __init__(self, file_or_name, mode: str = 'w', channel: str = 'stdout') -> None:
        """Construct a new Tee object.

        Parameters
        ----------
        file_or_name : filename or open filehandle (writable)
            File that will be duplicated
        mode : optional, valid mode for open().
            If a filename was give, open with this mode.
        channel : str, one of ['stdout', 'stderr']
        """
    def close(self) -> None:
        """Close the file and restore the channel."""
    def write(self, data) -> None:
        """Write data to both channels."""
    def flush(self) -> None:
        """Flush both channels."""
    def __del__(self) -> None: ...

def ask_yes_no(prompt, default: Incomplete | None = None, interrupt: Incomplete | None = None):
    """Asks a question and returns a boolean (y/n) answer.

    If default is given (one of 'y','n'), it is used if the user input is
    empty. If interrupt is given (one of 'y','n'), it is used if the user
    presses Ctrl-C. Otherwise the question is repeated until an answer is
    given.

    An EOF is treated as the default answer.  If there is no default, an
    exception is raised to prevent infinite loops.

    Valid answers are: y/yes/n/no (match is not case sensitive)."""
def temp_pyfile(src, ext: str = '.py'):
    """Make a temporary python file, return filename and filehandle.

    Parameters
    ----------
    src : string or list of strings (no need for ending newlines if list)
        Source code to be written to the file.
    ext : optional, string
        Extension for the generated file.

    Returns
    -------
    (filename, open filehandle)
        It is the caller's responsibility to close the open file and unlink it.
    """
def raw_print(*args, **kw) -> None:
    """DEPRECATED: Raw print to sys.__stdout__, otherwise identical interface to print()."""
def raw_print_err(*args, **kw) -> None:
    """DEPRECATED: Raw print to sys.__stderr__, otherwise identical interface to print()."""
