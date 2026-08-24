import inspect
from _typeshed import Incomplete
from collections.abc import Generator
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic
from sympy.core.function import AppliedUndef as AppliedUndef, Function as Function, UndefinedFunction as UndefinedFunction
from typing import Type

def printer_context(printer, **kwargs) -> Generator[None, None, None]: ...

class Printer:
    """ Generic printer

    Its job is to provide infrastructure for implementing new printers easily.

    If you want to define your custom Printer or your custom printing method
    for your custom class then see the example above: printer_example_ .
    """
    printmethod: str
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    @classmethod
    def set_global_settings(cls, **settings) -> None:
        """Set system-wide printing settings. """
    @property
    def order(self): ...
    def doprint(self, expr):
        """Returns printer's representation for expr (as a string)"""
    def emptyPrinter(self, expr): ...

class _PrintFunction:
    """
    Function wrapper to replace ``**settings`` in the signature with printer defaults
    """
    def __init__(self, f, print_cls: Type[Printer]) -> None: ...
    def __reduce__(self): ...
    def __call__(self, *args, **kwargs): ...
    @property
    def __signature__(self) -> inspect.Signature: ...

def print_function(print_cls):
    """ A decorator to replace kwargs with the printer settings in __signature__ """
