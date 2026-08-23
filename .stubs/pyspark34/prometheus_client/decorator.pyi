from _typeshed import Incomplete
from contextlib import GeneratorContextManager as _GeneratorContextManager
from typing import NamedTuple

__version__: str

def get_init(cls): ...

class ArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    varkw: Incomplete
    defaults: Incomplete

def getargspec(f):
    """A replacement for inspect.getargspec"""

DEF: Incomplete

class FunctionMaker:
    """
    An object with the ability to create functions with a given signature.
    It has attributes name, doc, module, signature, defaults, dict and
    methods update and make.
    """
    shortsignature: Incomplete
    name: Incomplete
    doc: Incomplete
    module: Incomplete
    annotations: Incomplete
    signature: Incomplete
    dict: Incomplete
    defaults: Incomplete
    def __init__(self, func: Incomplete | None = None, name: Incomplete | None = None, signature: Incomplete | None = None, defaults: Incomplete | None = None, doc: Incomplete | None = None, module: Incomplete | None = None, funcdict: Incomplete | None = None) -> None: ...
    def update(self, func, **kw) -> None:
        """Update the signature of func with the data in self"""
    def make(self, src_templ, evaldict: Incomplete | None = None, addsource: bool = False, **attrs):
        """Make a new function from a given template and update the signature"""
    @classmethod
    def create(cls, obj, body, evaldict, defaults: Incomplete | None = None, doc: Incomplete | None = None, module: Incomplete | None = None, addsource: bool = True, **attrs):
        """
        Create a function from the strings name, signature and body.
        evaldict is the evaluation dictionary. If addsource is true an
        attribute __source__ is added to the result. The attributes attrs
        are added, if any.
        """

def decorate(func, caller):
    """
    decorate(func, caller) decorates a function using a caller.
    """
def decorator(caller, _func: Incomplete | None = None):
    """decorator(caller) converts a caller function into a decorator"""

class ContextManager(_GeneratorContextManager):
    def __call__(self, func):
        """Context manager decorator"""

init: Incomplete
n_args: Incomplete

def __init__(self, g, *a, **k) -> None: ...

contextmanager: Incomplete

def append(a, vancestors) -> None:
    """
    Append ``a`` to the list of the virtual ancestors, unless it is already
    included.
    """
def dispatch_on(*dispatch_args):
    """
    Factory of decorators turning a function into a generic function
    dispatching on the given arguments.
    """
