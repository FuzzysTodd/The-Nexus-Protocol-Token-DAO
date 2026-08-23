from _typeshed import Incomplete
from mako import exceptions as exceptions, pyparser as pyparser

class PythonCode:
    """represents information about a string containing Python code"""
    code: Incomplete
    declared_identifiers: Incomplete
    undeclared_identifiers: Incomplete
    def __init__(self, code, **exception_kwargs) -> None: ...

class ArgumentList:
    """parses a fragment of code as a comma-separated list of expressions"""
    codeargs: Incomplete
    args: Incomplete
    declared_identifiers: Incomplete
    undeclared_identifiers: Incomplete
    def __init__(self, code, **exception_kwargs) -> None: ...

class PythonFragment(PythonCode):
    """extends PythonCode to provide identifier lookups in partial control
    statements

    e.g.::

        for x in 5:
        elif y==9:
        except (MyException, e):

    """
    def __init__(self, code, **exception_kwargs) -> None: ...

class FunctionDecl:
    """function declaration"""
    code: Incomplete
    def __init__(self, code, allow_kwargs: bool = True, **exception_kwargs) -> None: ...
    def get_argument_expressions(self, as_call: bool = False):
        """Return the argument declarations of this FunctionDecl as a printable
        list.

        By default the return value is appropriate for writing in a ``def``;
        set `as_call` to true to build arguments to be passed to the function
        instead (assuming locals with the same names as the arguments exist).
        """
    @property
    def allargnames(self): ...

class FunctionArgs(FunctionDecl):
    """the argument portion of a function declaration"""
    def __init__(self, code, **kwargs) -> None: ...
