from _typeshed import Incomplete
from tensorflow.python.util import tf_inspect as tf_inspect

def islambda(f): ...
def isnamedtuple(f):
    """Returns True if the argument is a namedtuple-like."""
def isbuiltin(f):
    """Returns True if the argument is a built-in function."""
def isconstructor(cls):
    """Returns True if the argument is an object constructor.

  In general, any object of type class is a constructor, with the exception
  of classes created using a callable metaclass.
  See below for why a callable metaclass is not a trivial combination:
  https://docs.python.org/2.7/reference/datamodel.html#customizing-class-creation

  Args:
    cls: Any

  Returns:
    Bool
  """
def getimmediatesource(obj):
    """A variant of inspect.getsource that ignores the __wrapped__ property."""
def getnamespace(f):
    """Returns the complete namespace of a function.

  Namespace is defined here as the mapping of all non-local variables to values.
  This includes the globals and the closure variables. Note that this captures
  the entire globals collection of the function, and may contain extra symbols
  that it does not actually use.

  Args:
    f: User defined function.

  Returns:
    A dict mapping symbol names to values.
  """
def getqualifiedname(namespace, object_, max_depth: int = 5, visited: Incomplete | None = None):
    """Returns the name by which a value can be referred to in a given namespace.

  If the object defines a parent module, the function attempts to use it to
  locate the object.

  This function will recurse inside modules, but it will not search objects for
  attributes. The recursion depth is controlled by max_depth.

  Args:
    namespace: Dict[str, Any], the namespace to search into.
    object_: Any, the value to search.
    max_depth: Optional[int], a limit to the recursion depth when searching
      inside modules.
    visited: Optional[Set[int]], ID of modules to avoid visiting.
  Returns: Union[str, None], the fully-qualified name that resolves to the value
    o, or None if it couldn't be found.
  """
def getdefiningclass(m, owner_class):
    """Resolves the class (e.g. one of the superclasses) that defined a method."""
def getmethodclass(m):
    """Resolves a function's owner, e.g.

  a method's class.

  Note that this returns the object that the function was retrieved from, not
  necessarily the class where it was defined.

  This function relies on Python stack frame support in the interpreter, and
  has the same limitations that inspect.currentframe.

  Limitations. This function will only work correctly if the owned class is
  visible in the caller's global or local variables.

  Args:
    m: A user defined function

  Returns:
    The class that this function was retrieved from, or None if the function
    is not an object or class method, or the class that owns the object or
    method is not visible to m.

  Raises:
    ValueError: if the class could not be resolved for any unexpected reason.
  """
def getfutureimports(entity):
    """Detects what future imports are necessary to safely execute entity source.

  Args:
    entity: Any object

  Returns:
    A tuple of future strings
  """
