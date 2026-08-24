from _typeshed import Incomplete
from sympy.core import Basic as Basic, Expr as Expr, Float as Float
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import precedence as precedence

known_functions: Incomplete

class MCodePrinter(CodePrinter):
    """A printer to convert Python expressions to
    strings of the Wolfram's Mathematica code
    """
    printmethod: str
    language: str
    known_functions: Incomplete
    def __init__(self, settings={}) -> None:
        """Register function mappings supplied by user"""

def mathematica_code(expr, **settings):
    """Converts an expr to a string of the Wolfram Mathematica code

    Examples
    ========

    >>> from sympy import mathematica_code as mcode, symbols, sin
    >>> x = symbols('x')
    >>> mcode(sin(x).series(x).removeO())
    '(1/120)*x^5 - 1/6*x^3 + x'
    """
