from .logger import trace as trace
from _typeshed import Incomplete

__all__ = ['baditems', 'badobjects', 'badtypes', 'code', 'errors', 'freevars', 'getmodule', 'globalvars', 'nestedcode', 'nestedglobals', 'outermost', 'referredglobals', 'referrednested', 'trace', 'varnames']

def getmodule(object, _filename: Incomplete | None = None, force: bool = False):
    """get the module of the object"""
def outermost(func):
    """get outermost enclosing object (i.e. the outer function in a closure)

    NOTE: this is the object-equivalent of getsource(func, enclosing=True)
    """
def nestedcode(func, recurse: bool = True):
    """get the code objects for any nested functions (e.g. in a closure)"""
def code(func):
    """get the code object for the given function or method

    NOTE: use dill.source.getsource(CODEOBJ) to get the source code
    """
def referrednested(func, recurse: bool = True):
    """get functions defined inside of func (e.g. inner functions in a closure)

    NOTE: results may differ if the function has been executed or not.
    If len(nestedcode(func)) > len(referrednested(func)), try calling func().
    If possible, python builds code objects, but delays building functions
    until func() is called.
    """
def freevars(func):
    """get objects defined in enclosing code that are referred to by func

    returns a dict of {name:object}"""
def nestedglobals(func, recurse: bool = True):
    """get the names of any globals found within func"""
def referredglobals(func, recurse: bool = True, builtin: bool = False):
    """get the names of objects in the global scope referred to by func"""
def globalvars(func, recurse: bool = True, builtin: bool = False):
    """get objects defined in global scope that are referred to by func

    return a dict of {name:object}"""
def varnames(func):
    """get names of variables defined by func

    returns a tuple (local vars, local vars referrenced by nested functions)"""
def baditems(obj, exact: bool = False, safe: bool = False):
    """get items in object that fail to pickle"""
def badobjects(obj, depth: int = 0, exact: bool = False, safe: bool = False):
    """get objects that fail to pickle"""
def badtypes(obj, depth: int = 0, exact: bool = False, safe: bool = False):
    """get types for objects that fail to pickle"""
def errors(obj, depth: int = 0, exact: bool = False, safe: bool = False):
    """get errors for objects that fail to pickle"""
