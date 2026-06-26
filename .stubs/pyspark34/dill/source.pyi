from _typeshed import Incomplete

__all__ = ['findsource', 'getsourcelines', 'getsource', 'indent', 'outdent', '_wrap', 'dumpsource', 'getname', '_namespace', 'getimport', '_importable', 'importable', 'isdynamic', 'isfrommain']

def isfrommain(obj):
    """check if object was built in __main__"""
def isdynamic(obj):
    """check if object was built in the interpreter"""
def findsource(object):
    """Return the entire source file and starting line number for an object.
    For interactively-defined objects, the 'file' is the interpreter's history.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of all the lines
    in the file and the line number indexes a line in that list.  An IOError
    is raised if the source code cannot be retrieved, while a TypeError is
    raised for objects where the source code is unavailable (e.g. builtins)."""
def getsourcelines(object, lstrip: bool = False, enclosing: bool = False):
    """Return a list of source lines and starting line number for an object.
    Interactively-defined objects refer to lines in the interpreter's history.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a list of the lines
    corresponding to the object and the line number indicates where in the
    original source file the first line of code was found.  An IOError is
    raised if the source code cannot be retrieved, while a TypeError is
    raised for objects where the source code is unavailable (e.g. builtins).

    If lstrip=True, ensure there is no indentation in the first line of code.
    If enclosing=True, then also return any enclosing code."""
def getsource(object, alias: str = '', lstrip: bool = False, enclosing: bool = False, force: bool = False, builtin: bool = False):
    """Return the text of the source code for an object. The source code for
    interactively-defined objects are extracted from the interpreter's history.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a single string.  An
    IOError is raised if the source code cannot be retrieved, while a
    TypeError is raised for objects where the source code is unavailable
    (e.g. builtins).

    If alias is provided, then add a line of code that renames the object.
    If lstrip=True, ensure there is no indentation in the first line of code.
    If enclosing=True, then also return any enclosing code.
    If force=True, catch (TypeError,IOError) and try to use import hooks.
    If builtin=True, force an import for any builtins
    """
def indent(code, spaces: int = 4):
    """indent a block of code with whitespace (default is 4 spaces)"""
def outdent(code, spaces: Incomplete | None = None, all: bool = True):
    """outdent a block of code (default is to strip all leading whitespace)"""
def _wrap(f):
    """ encapsulate a function and it's __import__ """
def dumpsource(object, alias: str = '', new: bool = False, enclose: bool = True):
    """'dump to source', where the code includes a pickled object.

    If new=True and object is a class instance, then create a new
    instance using the unpacked class source code. If enclose, then
    create the object inside a function enclosure (thus minimizing
    any global namespace pollution).
    """
def getname(obj, force: bool = False, fqn: bool = False):
    """get the name of the object. for lambdas, get the name of the pointer """
def _namespace(obj):
    """_namespace(obj); return namespace hierarchy (as a list of names)
    for the given object.  For an instance, find the class hierarchy.

    For example:

    >>> from functools import partial
    >>> p = partial(int, base=2)
    >>> _namespace(p)
    ['functools', 'partial']
    """
def getimport(obj, alias: str = '', verify: bool = True, builtin: bool = False, enclosing: bool = False):
    """get the likely import string for the given object

    obj is the object to inspect
    If verify=True, then test the import string before returning it.
    If builtin=True, then force an import for builtins where possible.
    If enclosing=True, get the import for the outermost enclosing callable.
    If alias is provided, then rename the object on import.
    """
def _importable(obj, alias: str = '', source: Incomplete | None = None, enclosing: bool = False, force: bool = True, builtin: bool = True, lstrip: bool = True):
    """get an import string (or the source code) for the given object

    This function will attempt to discover the name of the object, or the repr
    of the object, or the source code for the object. To attempt to force
    discovery of the source code, use source=True, to attempt to force the
    use of an import, use source=False; otherwise an import will be sought
    for objects not defined in __main__. The intent is to build a string
    that can be imported from a python file. obj is the object to inspect.
    If alias is provided, then rename the object with the given alias.

    If source=True, use these options:
      If enclosing=True, then also return any enclosing code.
      If force=True, catch (TypeError,IOError) and try to use import hooks.
      If lstrip=True, ensure there is no indentation in the first line of code.

    If source=False, use these options:
      If enclosing=True, get the import for the outermost enclosing callable.
      If force=True, then don't test the import string before returning it.
      If builtin=True, then force an import for builtins where possible.
    """
def importable(obj, alias: str = '', source: Incomplete | None = None, builtin: bool = True):
    """get an importable string (i.e. source code or the import string)
    for the given object, including any required objects from the enclosing
    and global scope

    This function will attempt to discover the name of the object, or the repr
    of the object, or the source code for the object. To attempt to force
    discovery of the source code, use source=True, to attempt to force the
    use of an import, use source=False; otherwise an import will be sought
    for objects not defined in __main__. The intent is to build a string
    that can be imported from a python file.

    obj is the object to inspect. If alias is provided, then rename the
    object with the given alias. If builtin=True, then force an import for
    builtins where possible.
    """
getblocks_from_history = getblocks
