from .precedence import PRECEDENCE as PRECEDENCE, precedence as precedence
from .printer import Printer as Printer, print_function as print_function
from sympy.core import Basic as Basic, Mul as Mul, Number as Number, Pow as Pow, Rational as Rational, S as S
from sympy.core.relational import Relational as Relational
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.sympify import SympifyError as SympifyError
from sympy.utilities.iterables import sift as sift

class StrPrinter(Printer):
    printmethod: str
    def parenthesize(self, item, level, strict: bool = False): ...
    def stringify(self, args, sep, level: int = 0): ...
    def emptyPrinter(self, expr): ...

def sstr(expr, **settings):
    """Returns the expression as a string.

    For large expressions where speed is a concern, use the setting
    order='none'. If abbrev=True setting is used then units are printed in
    abbreviated form.

    Examples
    ========

    >>> from sympy import symbols, Eq, sstr
    >>> a, b = symbols('a b')
    >>> sstr(Eq(a + b, 0))
    'Eq(a + b, 0)'
    """

class StrReprPrinter(StrPrinter):
    """(internal) -- see sstrrepr"""

def sstrrepr(expr, **settings):
    """return expr in mixed str/repr form

       i.e. strings are returned in repr form with quotes, and everything else
       is returned in str form.

       This function could be useful for hooking into sys.displayhook
    """
