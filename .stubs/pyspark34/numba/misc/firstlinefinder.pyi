import ast
from _typeshed import Incomplete

class FindDefFirstLine(ast.NodeVisitor):
    """
    Attributes
    ----------
    first_stmt_line : int or None
        This stores the first statement line number if the definition is found.
        Or, ``None`` if the definition is not found.
    """
    first_stmt_line: Incomplete
    def __init__(self, code) -> None:
        """
        Parameters
        ----------
        code :
            The function's code object.
        """
    def visit_FunctionDef(self, node: ast.FunctionDef): ...

def get_func_body_first_lineno(pyfunc):
    """
    Look up the first line of function body using the file in
    ``pyfunc.__code__.co_filename``.

    Returns
    -------
    lineno : int; or None
        The first line number of the function body; or ``None`` if the first
        line cannot be determined.
    """
