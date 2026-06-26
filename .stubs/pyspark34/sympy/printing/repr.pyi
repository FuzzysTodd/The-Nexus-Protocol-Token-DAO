from .printer import Printer as Printer, print_function as print_function
from sympy.core.function import AppliedUndef as AppliedUndef
from sympy.core.mul import Mul as Mul

class ReprPrinter(Printer):
    printmethod: str
    def reprify(self, args, sep):
        """
        Prints each item in `args` and joins them with `sep`.
        """
    def emptyPrinter(self, expr):
        """
        The fallback printer.
        """

def srepr(expr, **settings):
    """return expr in repr form"""
