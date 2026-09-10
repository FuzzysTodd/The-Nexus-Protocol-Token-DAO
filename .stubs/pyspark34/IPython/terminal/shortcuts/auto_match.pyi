from _typeshed import Incomplete
from prompt_toolkit.key_binding import KeyPressEvent as KeyPressEvent

def parenthesis(event: KeyPressEvent):
    """Auto-close parenthesis"""
def brackets(event: KeyPressEvent):
    """Auto-close brackets"""
def braces(event: KeyPressEvent):
    """Auto-close braces"""
def double_quote(event: KeyPressEvent):
    """Auto-close double quotes"""
def single_quote(event: KeyPressEvent):
    """Auto-close single quotes"""
def docstring_double_quotes(event: KeyPressEvent):
    """Auto-close docstring (double quotes)"""
def docstring_single_quotes(event: KeyPressEvent):
    """Auto-close docstring (single quotes)"""
def raw_string_parenthesis(event: KeyPressEvent):
    """Auto-close parenthesis in raw strings"""
def raw_string_bracket(event: KeyPressEvent):
    """Auto-close bracker in raw strings"""
def raw_string_braces(event: KeyPressEvent):
    """Auto-close braces in raw strings"""
def skip_over(event: KeyPressEvent):
    """Skip over automatically added parenthesis/quote.

    (rather than adding another parenthesis/quote)"""
def delete_pair(event: KeyPressEvent):
    """Delete auto-closed parenthesis"""

auto_match_parens: Incomplete
auto_match_parens_raw_string: Incomplete
