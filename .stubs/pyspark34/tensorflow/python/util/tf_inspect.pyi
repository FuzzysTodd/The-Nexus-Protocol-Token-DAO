import inspect as _inspect
from _typeshed import Incomplete
from tensorflow.python.util import tf_decorator as tf_decorator
from typing import NamedTuple

def signature(obj, *, follow_wrapped: bool = True):
    """TFDecorator-aware replacement for inspect.signature."""
Parameter = _inspect.Parameter
Signature = _inspect.Signature
ArgSpec: Incomplete

class ArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    keywords: Incomplete
    defaults: Incomplete
FullArgSpec = _inspect.FullArgSpec

class FullArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    varkw: Incomplete
    defaults: Incomplete
    kwonlyargs: Incomplete
    kwonlydefaults: Incomplete
    annotations: Incomplete

def currentframe():
    """TFDecorator-aware replacement for inspect.currentframe."""
def getargspec(obj):
    """TFDecorator-aware replacement for `inspect.getargspec`.

  Note: `getfullargspec` is recommended as the python 2/3 compatible
  replacement for this function.

  Args:
    obj: A function, partial function, or callable object, possibly decorated.

  Returns:
    The `ArgSpec` that describes the signature of the outermost decorator that
    changes the callable's signature, or the `ArgSpec` that describes
    the object if not decorated.

  Raises:
    ValueError: When callable's signature can not be expressed with
      ArgSpec.
    TypeError: For objects of unsupported types.
  """
def getfullargspec(obj):
    """TFDecorator-aware replacement for `inspect.getfullargspec`.

  This wrapper emulates `inspect.getfullargspec` in[^)]* Python2.

  Args:
    obj: A callable, possibly decorated.

  Returns:
    The `FullArgSpec` that describes the signature of
    the outermost decorator that changes the callable's signature. If the
    callable is not decorated, `inspect.getfullargspec()` will be called
    directly on the callable.
  """
def getcallargs(*func_and_positional, **named):
    """TFDecorator-aware replacement for inspect.getcallargs.

  Args:
    *func_and_positional: A callable, possibly decorated, followed by any
      positional arguments that would be passed to `func`.
    **named: The named argument dictionary that would be passed to `func`.

  Returns:
    A dictionary mapping `func`'s named arguments to the values they would
    receive if `func(*positional, **named)` were called.

  `getcallargs` will use the argspec from the outermost decorator that provides
  it. If no attached decorators modify argspec, the final unwrapped target's
  argspec will be used.
  """
def getframeinfo(*args, **kwargs): ...
def getdoc(object):
    """TFDecorator-aware replacement for inspect.getdoc.

  Args:
    object: An object, possibly decorated.

  Returns:
    The docstring associated with the object.

  The outermost-decorated object is intended to have the most complete
  documentation, so the decorated parameter is not unwrapped.
  """
def getfile(object):
    """TFDecorator-aware replacement for inspect.getfile."""
def getmembers(object, predicate: Incomplete | None = None):
    """TFDecorator-aware replacement for inspect.getmembers."""
def getmodule(object):
    """TFDecorator-aware replacement for inspect.getmodule."""
def getmro(cls):
    """TFDecorator-aware replacement for inspect.getmro."""
def getsource(object):
    """TFDecorator-aware replacement for inspect.getsource."""
def getsourcefile(object):
    """TFDecorator-aware replacement for inspect.getsourcefile."""
def getsourcelines(object):
    """TFDecorator-aware replacement for inspect.getsourcelines."""
def isbuiltin(object):
    """TFDecorator-aware replacement for inspect.isbuiltin."""
def isclass(object):
    """TFDecorator-aware replacement for inspect.isclass."""
def isfunction(object):
    """TFDecorator-aware replacement for inspect.isfunction."""
def isframe(object):
    """TFDecorator-aware replacement for inspect.ismodule."""
def isgenerator(object):
    """TFDecorator-aware replacement for inspect.isgenerator."""
def isgeneratorfunction(object):
    """TFDecorator-aware replacement for inspect.isgeneratorfunction."""
def ismethod(object):
    """TFDecorator-aware replacement for inspect.ismethod."""
def isanytargetmethod(object):
    """Checks if `object` or a TF Decorator wrapped target contains self or cls.

  This function could be used along with `tf_inspect.getfullargspec` to
  determine if the first argument of `object` argspec is self or cls. If the
  first argument is self or cls, it needs to be excluded from argspec when we
  compare the argspec to the input arguments and, if provided, the tf.function
  input_signature.

  Like `tf_inspect.getfullargspec` and python `inspect.getfullargspec`, it
  does not unwrap python decorators.

  Args:
    obj: An method, function, or functool.partial, possibly decorated by
    TFDecorator.

  Returns:
    A bool indicates if `object` or any target along the chain of TF decorators
    is a method.
  """
def ismodule(object):
    """TFDecorator-aware replacement for inspect.ismodule."""
def isroutine(object):
    """TFDecorator-aware replacement for inspect.isroutine."""
def stack(context: int = 1):
    """TFDecorator-aware replacement for inspect.stack."""
