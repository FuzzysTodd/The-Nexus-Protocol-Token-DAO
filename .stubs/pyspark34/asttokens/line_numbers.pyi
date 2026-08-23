from typing import Tuple

class LineNumbers:
    """
  Class to convert between character offsets in a text string, and pairs (line, column) of 1-based
  line and 0-based column numbers, as used by tokens and AST nodes.

  This class expects unicode for input and stores positions in unicode. But it supports
  translating to and from utf8 offsets, which are used by ast parsing.
  """
    def __init__(self, text: str) -> None: ...
    def from_utf8_col(self, line: int, utf8_column: int) -> int:
        """
    Given a 1-based line number and 0-based utf8 column, returns a 0-based unicode column.
    """
    def line_to_offset(self, line: int, column: int) -> int:
        """
    Converts 1-based line number and 0-based column to 0-based character offset into text.
    """
    def offset_to_line(self, offset: int) -> Tuple[int, int]:
        """
    Converts 0-based character offset to pair (line, col) of 1-based line and 0-based column
    numbers.
    """
