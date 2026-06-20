from _typeshed import Incomplete

class Coord:
    """ Coordinates of a syntactic element. Consists of:
            - File name
            - Line number
            - (optional) column number, for the Lexer
    """
    file: Incomplete
    line: Incomplete
    column: Incomplete
    def __init__(self, file, line, column: Incomplete | None = None) -> None: ...

class ParseError(Exception): ...
class PLYParser: ...

def parameterized(*params):
    """ Decorator to create parameterized rules.

    Parameterized rule methods must be named starting with 'p_' and contain
    'xxx', and their docstrings may contain 'xxx' and 'yyy'. These will be
    replaced by the given parameter tuples. For example, ``p_xxx_rule()`` with
    docstring 'xxx_rule  : yyy' when decorated with
    ``@parameterized(('id', 'ID'))`` produces ``p_id_rule()`` with the docstring
    'id_rule  : ID'. Using multiple tuples produces multiple rules.
    """
def template(cls):
    """ Class decorator to generate rules from parameterized rule templates.

    See `parameterized` for more information on parameterized rules.
    """
