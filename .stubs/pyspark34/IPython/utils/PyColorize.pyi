import tokenize
from .colorable import Colorable
from IPython.utils.coloransi import TermColors
from _typeshed import Incomplete

__all__ = ['ANSICodeColors', 'Parser']

generate_tokens = tokenize.generate_tokens
Colors = TermColors
ANSICodeColors: Incomplete

class Parser(Colorable):
    """ Format colored Python source.
    """
    color_table: Incomplete
    out: Incomplete
    pos: Incomplete
    lines: Incomplete
    raw: Incomplete
    style: Incomplete
    def __init__(self, color_table: Incomplete | None = None, out=..., parent: Incomplete | None = None, style: Incomplete | None = None) -> None:
        """ Create a parser with a specified color table and output channel.

        Call format() to process code.
        """
    def format(self, raw, out: Incomplete | None = None, scheme=...): ...
    colors: Incomplete
    def format2(self, raw, out: Incomplete | None = None):
        """ Parse and send the colored source.

        If out and scheme are not specified, the defaults (given to
        constructor) are used.

        out should be a file-type object. Optionally, out can be given as the
        string 'str' and the parser will automatically return the output in a
        string."""
    def __call__(self, toktype, toktext, start_pos, end_pos, line) -> None:
        """ Token handler, with syntax highlighting."""
