from _typeshed import Incomplete
from mako import exceptions as exceptions

class PythonPrinter:
    indent: int
    indent_detail: Incomplete
    indentstring: str
    stream: Incomplete
    lineno: int
    line_buffer: Incomplete
    in_indent_lines: bool
    source_map: Incomplete
    def __init__(self, stream) -> None: ...
    def start_source(self, lineno) -> None: ...
    def write_blanks(self, num) -> None: ...
    def write_indented_block(self, block, starting_lineno: Incomplete | None = None) -> None:
        """print a line or lines of python which already contain indentation.

        The indentation of the total block of lines will be adjusted to that of
        the current indent level."""
    def writelines(self, *lines) -> None:
        """print a series of lines of python."""
    def writeline(self, line) -> None:
        """print a line of python, indenting it according to the current
        indent level.

        this also adjusts the indentation counter according to the
        content of the line.

        """
    def close(self) -> None:
        """close this printer, flushing any remaining lines."""

def adjust_whitespace(text):
    """remove the left-whitespace margin of a block of Python code."""
