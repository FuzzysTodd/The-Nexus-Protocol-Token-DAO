from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.numbers import Integer as Integer, IntegerConstant as IntegerConstant, equal_valued as equal_valued
from sympy.printing.codeprinter import CodePrinter as CodePrinter
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence

known_functions: Incomplete
number_symbols: Incomplete
spec_relational_ops: Incomplete
not_supported_symbol: Incomplete

class MapleCodePrinter(CodePrinter):
    """
    Printer which converts a SymPy expression into a maple code.
    """
    printmethod: str
    language: str
    known_functions: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...

def maple_code(expr, assign_to: Incomplete | None = None, **settings):
    """Converts ``expr`` to a string of Maple code.

    Parameters
    ==========

    expr : Expr
        A SymPy expression to be converted.
    assign_to : optional
        When given, the argument is used as the name of the variable to which
        the expression is assigned.  Can be a string, ``Symbol``,
        ``MatrixSymbol``, or ``Indexed`` type.  This can be helpful for
        expressions that generate multi-line statements.
    precision : integer, optional
        The precision for numbers such as pi  [default=16].
    user_functions : dict, optional
        A dictionary where keys are ``FunctionClass`` instances and values are
        their string representations.  Alternatively, the dictionary value can
        be a list of tuples i.e. [(argument_test, cfunction_string)].  See
        below for examples.
    human : bool, optional
        If True, the result is a single string that may contain some constant
        declarations for the number symbols.  If False, the same information is
        returned in a tuple of (symbols_to_declare, not_supported_functions,
        code_text).  [default=True].
    contract: bool, optional
        If True, ``Indexed`` instances are assumed to obey tensor contraction
        rules and the corresponding nested loops over indices are generated.
        Setting contract=False will not generate loops, instead the user is
        responsible to provide values for the indices in the code.
        [default=True].
    inline: bool, optional
        If True, we try to create single-statement code instead of multiple
        statements.  [default=True].

    """
def print_maple_code(expr, **settings) -> None:
    """Prints the Maple representation of the given expression.

    See :func:`maple_code` for the meaning of the optional arguments.

    Examples
    ========

    >>> from sympy import print_maple_code, symbols
    >>> x, y = symbols('x y')
    >>> print_maple_code(x, assign_to=y)
    y := x
    """
