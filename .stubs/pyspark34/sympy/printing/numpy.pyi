from .codeprinter import CodePrinter as CodePrinter
from .pycode import ArrayPrinter as ArrayPrinter, PythonCodePrinter as PythonCodePrinter
from _typeshed import Incomplete
from sympy.core import S as S
from sympy.core.function import Lambda as Lambda
from sympy.core.power import Pow as Pow

class NumPyPrinter(ArrayPrinter, PythonCodePrinter):
    """
    Numpy printer which handles vectorized piecewise functions,
    logical operators, etc.
    """
    language: Incomplete
    printmethod: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None:
        """
        `settings` is passed to CodePrinter.__init__()
        `module` specifies the array module to use, currently 'NumPy', 'CuPy'
        or 'JAX'.
        """

class SciPyPrinter(NumPyPrinter):
    language: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class CuPyPrinter(NumPyPrinter):
    """
    CuPy printer which handles vectorized piecewise functions,
    logical operators, etc.
    """
    def __init__(self, settings: Incomplete | None = None) -> None: ...

class JaxPrinter(NumPyPrinter):
    """
    JAX printer which handles vectorized piecewise functions,
    logical operators, etc.
    """
    def __init__(self, settings: Incomplete | None = None) -> None: ...
