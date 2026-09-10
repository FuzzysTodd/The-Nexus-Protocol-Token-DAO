from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import Function as Function
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Number as Number, Rational as Rational
from sympy.core.power import Pow as Pow
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import SympifyError as SympifyError
from sympy.printing.conventions import requires_partial as requires_partial
from sympy.printing.precedence import PRECEDENCE as PRECEDENCE, precedence as precedence, precedence_traditional as precedence_traditional
from sympy.printing.pretty.pretty_symbology import U as U, annotated as annotated, greek_unicode as greek_unicode, hobj as hobj, pretty_atom as pretty_atom, pretty_symbol as pretty_symbol, pretty_try_use_unicode as pretty_try_use_unicode, pretty_use_unicode as pretty_use_unicode, vobj as vobj, xobj as xobj, xsym as xsym
from sympy.printing.pretty.stringpict import prettyForm as prettyForm, stringPict as stringPict
from sympy.printing.printer import Printer as Printer, print_function as print_function
from sympy.printing.str import sstr as sstr
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import has_variety as has_variety

pprint_use_unicode = pretty_use_unicode
pprint_try_use_unicode = pretty_try_use_unicode

class PrettyPrinter(Printer):
    """Printer, which converts an expression into 2D ASCII-art figure."""
    printmethod: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    def emptyPrinter(self, expr): ...
    def doprint(self, expr): ...
    def join(self, delimiter, args): ...

def pretty(expr, **settings):
    """Returns a string containing the prettified form of expr.

    For information on keyword arguments see pretty_print function.

    """
def pretty_print(expr, **kwargs) -> None:
    '''Prints expr in pretty form.

    pprint is just a shortcut for this function.

    Parameters
    ==========

    expr : expression
        The expression to print.

    wrap_line : bool, optional (default=True)
        Line wrapping enabled/disabled.

    num_columns : int or None, optional (default=None)
        Number of columns before line breaking (default to None which reads
        the terminal width), useful when using SymPy without terminal.

    use_unicode : bool or None, optional (default=None)
        Use unicode characters, such as the Greek letter pi instead of
        the string pi.

    full_prec : bool or string, optional (default="auto")
        Use full precision.

    order : bool or string, optional (default=None)
        Set to \'none\' for long expressions if slow; default is None.

    use_unicode_sqrt_char : bool, optional (default=True)
        Use compact single-character square root symbol (when unambiguous).

    root_notation : bool, optional (default=True)
        Set to \'False\' for printing exponents of the form 1/n in fractional form.
        By default exponent is printed in root form.

    mat_symbol_style : string, optional (default="plain")
        Set to "bold" for printing MatrixSymbols using a bold mathematical symbol face.
        By default the standard face is used.

    imaginary_unit : string, optional (default="i")
        Letter to use for imaginary unit when use_unicode is True.
        Can be "i" (default) or "j".
    '''
pprint = pretty_print

def pager_print(expr, **settings) -> None:
    """Prints expr using the pager, in pretty form.

    This invokes a pager command using pydoc. Lines are not wrapped
    automatically. This routine is meant to be used with a pager that allows
    sideways scrolling, like ``less -S``.

    Parameters are the same as for ``pretty_print``. If you wish to wrap lines,
    pass ``num_columns=None`` to auto-detect the width of the terminal.

    """
