import inspect
from _typeshed import Incomplete

def fullargspec_to_signature(fullargspec: inspect.FullArgSpec) -> inspect.Signature:
    """Repackages fullargspec information into an equivalent inspect.Signature."""
def make_decorator(target, decorator_func, decorator_name: Incomplete | None = None, decorator_doc: str = '', decorator_argspec: Incomplete | None = None):
    """Make a decorator from a wrapper and a target.

  Args:
    target: The final callable to be wrapped.
    decorator_func: The wrapper function.
    decorator_name: The name of the decorator. If `None`, the name of the
      function calling make_decorator.
    decorator_doc: Documentation specific to this application of
      `decorator_func` to `target`.
    decorator_argspec: Override the signature using FullArgSpec.

  Returns:
    The `decorator_func` argument with new metadata attached.
  """
def rewrap(decorator_func, previous_target, new_target):
    """Injects a new target into a function built by make_decorator.

  This function allows replacing a function wrapped by `decorator_func`,
  assuming the decorator that wraps the function is written as described below.

  The decorator function must use `<decorator name>.__wrapped__` instead of the
  wrapped function that is normally used:

  Example:

      # Instead of this:
      def simple_parametrized_wrapper(*args, **kwds):
        return wrapped_fn(*args, **kwds)

      tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)

      # Write this:
      def simple_parametrized_wrapper(*args, **kwds):
        return simple_parametrized_wrapper.__wrapped__(*args, **kwds)

      tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)

  Note that this process modifies decorator_func.

  Args:
    decorator_func: Callable returned by `wrap`.
    previous_target: Callable that needs to be replaced.
    new_target: Callable to replace previous_target with.

  Returns:
    The updated decorator. If decorator_func is not a tf_decorator, new_target
    is returned.
  """
def unwrap(maybe_tf_decorator):
    """Unwraps an object into a list of TFDecorators and a final target.

  Args:
    maybe_tf_decorator: Any callable object.

  Returns:
    A tuple whose first element is an list of TFDecorator-derived objects that
    were applied to the final callable target, and whose second element is the
    final undecorated callable target. If the `maybe_tf_decorator` parameter is
    not decorated by any TFDecorators, the first tuple element will be an empty
    list. The `TFDecorator` list is ordered from outermost to innermost
    decorators.
  """

class TFDecorator:
    """Base class for all TensorFlow decorators.

  TFDecorator captures and exposes the wrapped target, and provides details
  about the current decorator.
  """
    __qualname__: Incomplete
    __doc__: Incomplete
    __signature__: Incomplete
    def __init__(self, decorator_name, target, decorator_doc: str = '', decorator_argspec: Incomplete | None = None) -> None: ...
    def __get__(self, instance, owner): ...
    def __call__(self, *args, **kwargs): ...
    @property
    def decorated_target(self): ...
    @decorated_target.setter
    def decorated_target(self, decorated_target) -> None: ...
    @property
    def decorator_name(self): ...
    @property
    def decorator_doc(self): ...
    @property
    def decorator_argspec(self): ...
