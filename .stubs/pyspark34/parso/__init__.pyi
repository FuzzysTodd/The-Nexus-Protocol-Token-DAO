from _typeshed import Incomplete
from parso.grammar import Grammar as Grammar, load_grammar as load_grammar
from parso.parser import ParserSyntaxError as ParserSyntaxError
from parso.utils import python_bytes_to_unicode as python_bytes_to_unicode, split_lines as split_lines

__version__: str

def parse(code: Incomplete | None = None, **kwargs):
    """
    A utility function to avoid loading grammars.
    Params are documented in :py:meth:`parso.Grammar.parse`.

    :param str version: The version used by :py:func:`parso.load_grammar`.
    """
