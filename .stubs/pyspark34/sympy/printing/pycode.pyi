from .codeprinter import CodePrinter as CodePrinter
from .precedence import precedence as precedence
from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.mod import Mod as Mod

class AbstractPythonCodePrinter(CodePrinter):
    printmethod: str
    language: str
    reserved_words: Incomplete
    modules: Incomplete
    tab: str
    standard: Incomplete
    module_imports: Incomplete
    known_functions: Incomplete
    known_constants: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class ArrayPrinter: ...
class PythonCodePrinter(AbstractPythonCodePrinter): ...

def pycode(expr, **settings):
    """ Converts an expr to a string of Python code

    Parameters
    ==========

    expr : Expr
        A SymPy expression.
    fully_qualified_modules : bool
        Whether or not to write out full module names of functions
        (``math.sin`` vs. ``sin``). default: ``True``.
    standard : str or None, optional
        Only 'python3' (default) is supported.
        This parameter may be removed in the future.

    Examples
    ========

    >>> from sympy import pycode, tan, Symbol
    >>> pycode(tan(Symbol('x')) + 1)
    'math.tan(x) + 1'

    """

class MpmathPrinter(PythonCodePrinter):
    """
    Lambda printer for mpmath which maintains precision for floats
    """
    printmethod: str
    language: str

class SymPyPrinter(AbstractPythonCodePrinter):
    language: str
