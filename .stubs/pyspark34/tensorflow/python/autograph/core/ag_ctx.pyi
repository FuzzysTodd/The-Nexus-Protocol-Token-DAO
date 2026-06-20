import enum
from _typeshed import Incomplete
from tensorflow.python.autograph.utils import ag_logging as ag_logging
from tensorflow.python.util.tf_export import tf_export as tf_export

stacks: Incomplete

def control_status_ctx():
    """Returns the current control context for autograph.

  This method is useful when calling `tf.__internal__.autograph.tf_convert`,
  The context will be used by tf_convert to determine whether it should convert
  the input function. See the sample usage like below:

  ```
  def foo(func):
    return tf.__internal__.autograph.tf_convert(
       input_fn, ctx=tf.__internal__.autograph.control_status_ctx())()
  ```

  Returns:
    The current control context of autograph.
  """

class Status(enum.Enum):
    UNSPECIFIED: int
    ENABLED: int
    DISABLED: int

class ControlStatusCtx:
    """A context that tracks whether autograph is enabled by the user."""
    status: Incomplete
    options: Incomplete
    def __init__(self, status, options: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, unused_type: type[BaseException] | None, unused_value: BaseException | None, unused_traceback: types.TracebackType | None) -> None: ...

class NullCtx:
    """Helper substitute for contextlib.nullcontext."""
    def __enter__(self) -> None: ...
    def __exit__(self, unused_type: type[BaseException] | None, unused_value: BaseException | None, unused_traceback: types.TracebackType | None) -> None: ...

INSPECT_SOURCE_SUPPORTED: bool
