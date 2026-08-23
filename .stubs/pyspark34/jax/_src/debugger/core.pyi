import dataclasses
from _typeshed import Incomplete
from collections.abc import Hashable
from jax import tree_util as tree_util
from jax._src import core as core, debugging as debugging, traceback_util as traceback_util, util as util
from typing import Any, Protocol

class _DictWrapper:
    keys: list[Hashable]
    values: list[Any]
    def __init__(self, keys, values) -> None: ...
    def to_dict(self): ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, keys, values): ...

class _CantFlatten: ...

cant_flatten: Incomplete

@dataclasses.dataclass(frozen=True)
class DebuggerFrame:
    """Encapsulates Python frame information."""
    filename: str
    locals: dict[str, Any]
    globals: dict[str, Any]
    code_context: str
    source: list[str]
    lineno: int
    offset: int | None
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, info, valid_vars): ...
    @classmethod
    def from_frameinfo(cls, frame_info) -> DebuggerFrame: ...
    def __init__(self, filename, locals, globals, code_context, source, lineno, offset) -> None: ...

class Debugger(Protocol):
    def __call__(self, frames: list[DebuggerFrame], thread_id: int | None, **kwargs: Any) -> None: ...

def get_debugger(backend: str | None = None) -> Debugger: ...
def register_debugger(name: str, debugger: Debugger, priority: int) -> None: ...

debug_lock: Incomplete

def breakpoint(*, backend: str | None = None, filter_frames: bool = True, num_frames: int | None = None, ordered: bool = False, token: Incomplete | None = None, **kwargs):
    """Enters a breakpoint at a point in a program.

  Args:
    backend: The debugger backend to use. By default, picks the highest priority
      debugger and in the absence of other registered debuggers, falls back to
      the CLI debugger.
    filter_frames: Whether or not to filter out JAX-internal stack frames from
      the traceback. Since some libraries, like Flax, also make user of JAX's
      stack frame filtering system, this option can also affect whether stack
      frames from libraries are filtered.
    num_frames: The number of frames above the current stack frame to make
      available for inspection in the interactive debugger.
    ordered: A keyword only argument used to indicate whether or not the
      staged out computation will enforce ordering of this ``jax.debug.breakpoint``
      with respect to other ordered ``jax.debug.breakpoint`` and ``jax.debug.print``
      calls.
    token: A keyword only argument; an alternative to ``ordered``. If used then a JAX
      array (or pytree of JAX arrays) should be passed, and the breakpoint will be run
      once its value is computed.
      This is returned unchanged, and should be passed back to the computation.
      If the return value is unused in the later computation, then the whole computation
      will be pruned and this breakpoint will not be run.

  Returns:
    If `token` is passed, then its value is returned unchanged. Otherwise, returns
    `None`.
  """
