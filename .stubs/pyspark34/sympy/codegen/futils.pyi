from _typeshed import Incomplete
from sympy.codegen.fnodes import Module as Module
from sympy.core.symbol import Dummy as Dummy
from sympy.printing.fortran import FCodePrinter as FCodePrinter

def render_as_module(definitions, name, declarations=(), printer_settings: Incomplete | None = None):
    """ Creates a ``Module`` instance and renders it as a string.

    This generates Fortran source code for a module with the correct ``use`` statements.

    Parameters
    ==========

    definitions : iterable
        Passed to :class:`sympy.codegen.fnodes.Module`.
    name : str
        Passed to :class:`sympy.codegen.fnodes.Module`.
    declarations : iterable
        Passed to :class:`sympy.codegen.fnodes.Module`. It will be extended with
        use statements, 'implicit none' and public list generated from ``definitions``.
    printer_settings : dict
        Passed to ``FCodePrinter`` (default: ``{'standard': 2003, 'source_format': 'free'}``).

    """
