from .compat import pickle as pickle
from _typeshed import Incomplete
from types import CellType as CellType

DEFAULT_PROTOCOL: Incomplete
PYPY: Incomplete
builtin_code_type: Incomplete

def register_pickle_by_value(module) -> None:
    """Register a module to make it functions and classes picklable by value.

    By default, functions and classes that are attributes of an importable
    module are to be pickled by reference, that is relying on re-importing
    the attribute from the module at load time.

    If `register_pickle_by_value(module)` is called, all its functions and
    classes are subsequently to be pickled by value, meaning that they can
    be loaded in Python processes where the module is not importable.

    This is especially useful when developing a module in a distributed
    execution environment: restarting the client Python process with the new
    source code is enough: there is no need to re-install the new version
    of the module on all the worker nodes nor to restart the workers.

    Note: this feature is considered experimental. See the cloudpickle
    README.md file for more details and limitations.
    """
def unregister_pickle_by_value(module) -> None:
    """Unregister that the input module should be pickled by value."""
def list_registry_pickle_by_value(): ...
def cell_set(cell, value) -> None:
    """Set the value of a closure cell.

    The point of this function is to set the cell_contents attribute of a cell
    after its creation. This operation is necessary in case the cell contains a
    reference to the function the cell belongs to, as when calling the
    function's constructor
    ``f = types.FunctionType(code, globals, name, argdefs, closure)``,
    closure will not be able to contain the yet-to-be-created f.

    In Python3.7, cell_contents is writeable, so setting the contents of a cell
    can be done simply using
    >>> cell.cell_contents = value

    In earlier Python3 versions, the cell_contents attribute of a cell is read
    only, but this limitation can be worked around by leveraging the Python 3
    ``nonlocal`` keyword.

    In Python2 however, this attribute is read only, and there is no
    ``nonlocal`` keyword. For this reason, we need to come up with more
    complicated hacks to set this attribute.

    The chosen approach is to create a function with a STORE_DEREF opcode,
    which sets the content of a closure variable. Typically:

    >>> def inner(value):
    ...     lambda: cell  # the lambda makes cell a closure
    ...     cell = value  # cell is a closure, so this triggers a STORE_DEREF

    (Note that in Python2, A STORE_DEREF can never be triggered from an inner
    function. The function g for example here
    >>> def f(var):
    ...     def g():
    ...         var += 1
    ...     return g

    will not modify the closure variable ``var```inplace, but instead try to
    load a local variable var and increment it. As g does not assign the local
    variable ``var`` any initial value, calling f(1)() will fail at runtime.)

    Our objective is to set the value of a given cell ``cell``. So we need to
    somewhat reference our ``cell`` object into the ``inner`` function so that
    this object (and not the smoke cell of the lambda function) gets affected
    by the STORE_DEREF operation.

    In inner, ``cell`` is referenced as a cell variable (an enclosing variable
    that is referenced by the inner function). If we create a new function
    cell_set with the exact same code as ``inner``, but with ``cell`` marked as
    a free variable instead, the STORE_DEREF will be applied on its closure -
    ``cell``, which we can specify explicitly during construction! The new
    cell_set variable thus actually sets the contents of a specified cell!

    Note: we do not make use of the ``nonlocal`` keyword to set the contents of
    a cell in early python3 versions to limit possible syntax errors in case
    test and checker libraries decide to parse the whole file.
    """

STORE_GLOBAL: Incomplete
DELETE_GLOBAL: Incomplete
LOAD_GLOBAL: Incomplete
GLOBAL_OPS: Incomplete
HAVE_ARGUMENT: Incomplete
EXTENDED_ARG: Incomplete

def parametrized_type_hint_getinitargs(obj): ...
def is_tornado_coroutine(func):
    """
    Return whether *func* is a Tornado coroutine function.
    Running coroutines are not supported.
    """
load = pickle.load
loads = pickle.loads

def subimport(name): ...
def dynamic_subimport(name, vars): ...
def instance(cls):
    """Create a new instance of a class.

    Parameters
    ----------
    cls : type
        The class to create an instance of.

    Returns
    -------
    instance : cls
        A new instance of ``cls``.
    """

class _empty_cell_value:
    """sentinel for empty closures
    """
    @classmethod
    def __reduce__(cls): ...
