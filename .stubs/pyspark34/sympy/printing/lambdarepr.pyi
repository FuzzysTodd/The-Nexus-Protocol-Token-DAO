from .numpy import NumPyPrinter as NumPyPrinter
from .pycode import MpmathPrinter as MpmathPrinter, PythonCodePrinter as PythonCodePrinter

__all__ = ['PythonCodePrinter', 'MpmathPrinter', 'NumPyPrinter', 'LambdaPrinter', 'NumPyPrinter', 'IntervalPrinter', 'lambdarepr']

class LambdaPrinter(PythonCodePrinter):
    """
    This printer converts expressions into strings that can be used by
    lambdify.
    """
    printmethod: str

class NumExprPrinter(LambdaPrinter):
    printmethod: str
    module: str
    def blacklisted(self, expr) -> None: ...
    def doprint(self, expr): ...

class IntervalPrinter(MpmathPrinter, LambdaPrinter):
    """Use ``lambda`` printer but print numbers as ``mpi`` intervals. """

def lambdarepr(expr, **settings):
    """
    Returns a string usable for lambdifying.
    """
