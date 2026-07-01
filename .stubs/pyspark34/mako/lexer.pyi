from _typeshed import Incomplete
from mako import exceptions as exceptions, parsetree as parsetree
from mako.pygen import adjust_whitespace as adjust_whitespace

class Lexer:
    text: Incomplete
    filename: Incomplete
    template: Incomplete
    matched_lineno: int
    matched_charpos: int
    lineno: int
    match_position: int
    tag: Incomplete
    control_line: Incomplete
    ternary_stack: Incomplete
    encoding: Incomplete
    preprocessor: Incomplete
    def __init__(self, text, filename: Incomplete | None = None, input_encoding: Incomplete | None = None, preprocessor: Incomplete | None = None) -> None: ...
    @property
    def exception_kwargs(self): ...
    def match(self, regexp, flags: Incomplete | None = None):
        """compile the given regexp, cache the reg, and call match_reg()."""
    def match_reg(self, reg):
        """match the given regular expression object to the current text
        position.

        if a match occurs, update the current text and line position.

        """
    def parse_until_text(self, watch_nesting, *text): ...
    def append_node(self, nodecls, *args, **kwargs) -> None: ...
    def decode_raw_stream(self, text, decode_raw, known_encoding, filename):
        """given string/unicode or bytes/string, determine encoding
        from magic encoding comment, return body as unicode
        or raw if decode_raw=False

        """
    textlength: Incomplete
    def parse(self): ...
    keyword: Incomplete
    def match_tag_start(self): ...
    def match_tag_end(self): ...
    def match_end(self): ...
    def match_text(self): ...
    def match_python_block(self): ...
    def match_expression(self): ...
    def match_control_line(self): ...
    def match_comment(self):
        """matches the multiline version of a comment"""
