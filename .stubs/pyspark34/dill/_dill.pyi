import typing
from .logger import adapter as logger
from _typeshed import Incomplete
from pickle import DEFAULT_PROTOCOL as DEFAULT_PROTOCOL, HIGHEST_PROTOCOL as HIGHEST_PROTOCOL, PickleError as PickleError, PicklingError as PicklingError, Unpickler as StockUnpickler, UnpicklingError as UnpicklingError, _Pickler as StockPickler

__all__ = ['dump', 'dumps', 'load', 'loads', 'copy', 'Pickler', 'Unpickler', 'register', 'pickle', 'pickles', 'check', 'DEFAULT_PROTOCOL', 'HIGHEST_PROTOCOL', 'HANDLE_FMODE', 'CONTENTS_FMODE', 'FILE_FMODE', 'PickleError', 'PickleWarning', 'PicklingError', 'PicklingWarning', 'UnpicklingError', 'UnpicklingWarning']

log = logger
BufferType = memoryview
ClassType = type
SliceType = slice
TypeType = type
XRangeType = range
IS_IPYTHON = __IPYTHON__

class Sentinel:
    """
    Create a unique sentinel object that is pickled as a constant.
    """
    name: Incomplete
    __module__: Incomplete
    def __init__(self, name, module_name: Incomplete | None = None) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __reduce__(self): ...
    def __reduce_ex__(self, protocol): ...

HANDLE_FMODE: int
CONTENTS_FMODE: int
FILE_FMODE: int

def copy(obj, *args, **kwds):
    """
    Use pickling to 'copy' an object (i.e. `loads(dumps(obj))`).

    See :func:`dumps` and :func:`loads` for keyword arguments.
    """
def dump(obj, file, protocol: Incomplete | None = None, byref: Incomplete | None = None, fmode: Incomplete | None = None, recurse: Incomplete | None = None, **kwds) -> None:
    """
    Pickle an object to a file.

    See :func:`dumps` for keyword arguments.
    """
def dumps(obj, protocol: Incomplete | None = None, byref: Incomplete | None = None, fmode: Incomplete | None = None, recurse: Incomplete | None = None, **kwds):
    """
    Pickle an object to a string.

    *protocol* is the pickler protocol, as defined for Python *pickle*.

    If *byref=True*, then dill behaves a lot more like pickle as certain
    objects (like modules) are pickled by reference as opposed to attempting
    to pickle the object itself.

    If *recurse=True*, then objects referred to in the global dictionary
    are recursively traced and pickled, instead of the default behavior
    of attempting to store the entire global dictionary. This is needed for
    functions defined via *exec()*.

    *fmode* (:const:`HANDLE_FMODE`, :const:`CONTENTS_FMODE`,
    or :const:`FILE_FMODE`) indicates how file handles will be pickled.
    For example, when pickling a data file handle for transfer to a remote
    compute service, *FILE_FMODE* will include the file contents in the
    pickle and cursor position so that a remote method can operate
    transparently on an object with an open file handle.

    Default values for keyword arguments can be set in :mod:`dill.settings`.
    """
def load(file, ignore: Incomplete | None = None, **kwds):
    """
    Unpickle an object from a file.

    See :func:`loads` for keyword arguments.
    """
def loads(str, ignore: Incomplete | None = None, **kwds):
    """
    Unpickle an object from a string.

    If *ignore=False* then objects whose class is defined in the module
    *__main__* are updated to reference the existing class in *__main__*,
    otherwise they are left to refer to the reconstructed type, which may
    be different.

    Default values for keyword arguments can be set in :mod:`dill.settings`.
    """

class MetaCatchingDict(dict):
    def get(self, key, default: Incomplete | None = None): ...
    def __missing__(self, key): ...

class PickleWarning(Warning, PickleError): ...
class PicklingWarning(PickleWarning, PicklingError): ...
class UnpicklingWarning(PickleWarning, UnpicklingError): ...

class Pickler(StockPickler):
    """python's Pickler extended to interpreter sessions"""
    dispatch: typing.Dict[type, typing.Callable[[Pickler, typing.Any], None]]
    def __init__(self, file, *args, **kwds) -> None: ...
    def save(self, obj, save_persistent_id: bool = True) -> None: ...
    def dump(self, obj) -> None: ...

class Unpickler(StockUnpickler):
    """python's Unpickler extended to interpreter sessions and more types"""
    def find_class(self, module, name): ...
    def __init__(self, *args, **kwds) -> None: ...
    def load(self): ...

def pickle(t, func) -> None:
    """expose :attr:`~Pickler.dispatch` table for user-created extensions"""
def register(t):
    """decorator to register types to Pickler's :attr:`~Pickler.dispatch` table"""

class match:
    """
    Make avaialable a limited structural pattern matching-like syntax for Python < 3.10

    Patterns can be only tuples (without types) currently.
    Inspired by the package pattern-matching-PEP634.

    Usage:
    >>> with match(args) as m:
    >>>     if   m.case(('x', 'y')):
    >>>         # use m.x and m.y
    >>>     elif m.case(('x', 'y', 'z')):
    >>>         # use m.x, m.y and m.z

    Equivalent native code for Python >= 3.10:
    >>> match args:
    >>>     case (x, y):
    >>>         # use x and y
    >>>     case (x, y, z):
    >>>         # use x, y and z
    """
    value: Incomplete
    def __init__(self, value) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info): ...
    args: Incomplete
    def case(self, args):
        """just handles tuple patterns"""
    @property
    def fields(self): ...
    def __getattr__(self, item): ...
CODE_VERSION = version

class _itemgetter_helper:
    items: Incomplete
    def __init__(self) -> None: ...
    def __getitem__(self, item) -> None: ...

class _attrgetter_helper:
    attrs: Incomplete
    index: Incomplete
    def __init__(self, attrs, index: Incomplete | None = None) -> None: ...
    def __getattribute__(self, attr): ...

class _dictproxy_helper(dict):
    def __ror__(self, a): ...

def pickles(obj, exact: bool = False, safe: bool = False, **kwds):
    """
    Quick check if object pickles with dill.

    If *exact=True* then an equality test is done to check if the reconstructed
    object matches the original object.

    If *safe=True* then any exception will raised in copy signal that the
    object is not picklable, otherwise only pickling errors will be trapped.

    Additional keyword arguments are as :func:`dumps` and :func:`loads`.
    """
def check(obj, *args, **kwds) -> None:
    """
    Check pickling of an object across another process.

    *python* is the path to the python interpreter (defaults to sys.executable)

    Set *verbose=True* to print the unpickled object in the other process.

    Additional keyword arguments are as :func:`dumps` and :func:`loads`.
    """
