import types
from jax._src import util as util
from jax._src.config import config as config
from jax._src.lib import xla_extension as xla_extension
from typing import Any, Callable, TypeVar

C = TypeVar('C', bound=Callable[..., Any])

def register_exclusion(path: str): ...
def include_frame(f: types.FrameType) -> bool: ...
def filter_traceback(tb: types.TracebackType) -> types.TracebackType | None: ...
def format_exception_only(e: BaseException) -> str: ...

class UnfilteredStackTrace(Exception): ...
class SimplifiedTraceback(Exception): ...

def api_boundary(fun: C) -> C:
    """Wraps ``fun`` to form a boundary for filtering exception tracebacks.

  When an exception occurs below ``fun``, this appends to it a custom
  ``__cause__`` that carries a filtered traceback. The traceback imitates the
  stack trace of the original exception, but with JAX-internal frames removed.

  This boundary annotation works in composition with itself. The topmost frame
  corresponding to an :func:`~api_boundary` is the one below which stack traces
  are filtered. In other words, if ``api_boundary(f)`` calls
  ``api_boundary(g)``, directly or indirectly, the filtered stack trace provided
  is the same as if ``api_boundary(f)`` were to simply call ``g`` instead.

  This annotation is primarily useful in wrapping functions output by JAX's
  transformations. For example, consider ``g = jax.jit(f)``. When ``g`` is
  called, JAX's JIT compilation machinery is invoked, which in turn calls ``f``
  in order to trace and translate it. If the function ``f`` raises an exception,
  the stack unwinds through JAX's JIT internals up to the original call site of
  ``g``. Because the function returned by :func:`~jax.jit` is annotated as an
  :func:`~api_boundary`, such an exception is accompanied by an additional
  traceback that excludes the frames specific to JAX's implementation.
  """
