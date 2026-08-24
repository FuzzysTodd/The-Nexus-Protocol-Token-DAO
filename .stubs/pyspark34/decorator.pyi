from _typeshed import Incomplete
from contextlib import _GeneratorContextManager

__version__: str
DEF: Incomplete
POS: Incomplete
EMPTY: Incomplete

class FunctionMaker:
    """
    An object with the ability to create functions with a given signature.
    It has attributes name, doc, module, signature, defaults, dict and
    methods update and make.
    """
    args: Incomplete
    varargs: Incomplete
    varkw: Incomplete
    defaults: Incomplete
    kwonlyargs: Incomplete
    kwonlydefaults: Incomplete
    shortsignature: Incomplete
    name: Incomplete
    doc: Incomplete
    module: Incomplete
    annotations: Incomplete
    signature: Incomplete
    dict: Incomplete
    def __init__(self, func: Incomplete | None = None, name: Incomplete | None = None, signature: Incomplete | None = None, defaults: Incomplete | None = None, doc: Incomplete | None = None, module: Incomplete | None = None, funcdict: Incomplete | None = None) -> None: ...
    def update(self, func, **kw) -> None:
        """
        Update the signature of func with the data in self
        """
    def make(self, src_templ, evaldict: Incomplete | None = None, addsource: bool = False, **attrs):
        """
        Make a new function from a given template and update the signature
        """
    @classmethod
    def create(cls, obj, body, evaldict, defaults: Incomplete | None = None, doc: Incomplete | None = None, module: Incomplete | None = None, addsource: bool = True, **attrs):
        """
        Create a function from the strings name, signature and body.
        evaldict is the evaluation dictionary. If addsource is true an
        attribute __source__ is added to the result. The attributes attrs
        are added, if any.
        """

def fix(args, kwargs, sig):
    """
    Fix args and kwargs to be consistent with the signature
    """
def decorate(func, caller, extras=(), kwsyntax: bool = False):
    """
    Decorates a function/generator/coroutine using a caller.
    If kwsyntax is True calling the decorated functions with keyword
    syntax will pass the named arguments inside the ``kw`` dictionary,
    even if such argument are positional, similarly to what functools.wraps
    does. By default kwsyntax is False and the the arguments are untouched.
    """
def decoratorx(caller):
    '''
    A version of "decorator" implemented via "exec" and not via the
    Signature object. Use this if you are want to preserve the `.__code__`
    object properties (https://github.com/micheles/decorator/issues/129).
    '''
def decorator(caller, _func: Incomplete | None = None, kwsyntax: bool = False):
    """
    decorator(caller) converts a caller function into a decorator
    """

class ContextManager(_GeneratorContextManager):
    def __init__(self, g, *a, **k) -> None: ...
    def __call__(self, func): ...

def contextmanager(func): ...
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
