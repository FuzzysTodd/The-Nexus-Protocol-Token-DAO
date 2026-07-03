import enum
import types
import typing
from autopage import command
from typing import TextIO, Type

__all__ = ['AutoPager', 'line_buffer_from_input']

class ErrorStrategy(enum.Enum):
    """
    The strategy for dealing with unicode errors when convering text to bytes.
    """
    STRICT: str
    IGNORE: str
    REPLACE: str
    BACKSLASH_REPLACE: str
    XML_CHARREF_REPLACE: str
    NAME_REPLACE: str

class AutoPager:
    """
    A context manager that launches a pager for the output if appropriate.

    If the output stream is not to the console (i.e. it is piped or
    redirected), no pager will be launched.
    """
    def __init__(self, output_stream: TextIO | None = None, *, pager_command: command.CommandType = ..., allow_color: bool = True, line_buffering: bool | None = None, reset_on_exit: bool = False, errors: ErrorStrategy | None = None) -> None: ...
    def to_terminal(self) -> bool:
        """Return whether the output stream is a terminal."""
    def __enter__(self) -> TextIO: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None, traceback: types.TracebackType | None) -> bool: ...
    def exit_code(self) -> int:
        """
        Return an appropriate exit code for the process based on any errors.

        If the user exits the program prematurely by closing the pager, we may
        want to return a different exit code for the process. This method
        returns an appropriate exit code on the basis of the existence and type
        of any uncaught exceptions.
        """

def line_buffer_from_input(input_stream: typing.IO | None = None) -> bool:
    """
    Return whether line buffering should be enabled for a given input stream.

    When data is being read from an input stream, processed somehow, and then
    written to an autopaged output stream, it may be desirable to enable line
    buffering on the output. This means that each line of data written to the
    output will be visible immediately, as opposed to waiting for the output
    buffer to fill up. This is, however, slower.

    If the input stream is a file, line buffering is unnecessary. This function
    determines whether an input stream might require line buffering on output.

    If no input stream is specified, sys.stdin is assumed.

        >>> with AutoPager(line_buffering=line_buffer_from_input()) as out:
        >>>     for l in sys.stdin:
        >>>         out.write(l)
    """
