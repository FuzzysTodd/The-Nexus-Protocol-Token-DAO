from _typeshed import Incomplete

__all__ = ['lex', 'format', 'highlight']

def lex(code, lexer):
    """
    Lex `code` with the `lexer` (must be a `Lexer` instance)
    and return an iterable of tokens. Currently, this only calls
    `lexer.get_tokens()`.
    """
def format(tokens, formatter, outfile: Incomplete | None = None):
    """
    Format ``tokens`` (an iterable of tokens) with the formatter ``formatter``
    (a `Formatter` instance).

    If ``outfile`` is given and a valid file object (an object with a
    ``write`` method), the result will be written to it, otherwise it
    is returned as a string.
    """
def highlight(code, lexer, formatter, outfile: Incomplete | None = None):
    """
    This is the most high-level highlighting function. It combines `lex` and
    `format` in one function.
    """
