from _typeshed import Incomplete

op_data: str
precedence_data: Incomplete
symbol_data: Incomplete

def get_op_symbol(obj, fmt: str = '%s', symbol_data=..., type=...):
    """Given an AST node object, returns a string containing the symbol.
    """
def get_op_precedence(obj, precedence_data=..., type=...):
    """Given an AST node object, returns the precedence.
    """

class Precedence:
    highest: Incomplete
