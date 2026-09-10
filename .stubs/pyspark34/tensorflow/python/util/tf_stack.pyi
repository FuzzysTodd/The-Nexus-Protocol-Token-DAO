from _typeshed import Incomplete

class StackTraceTransform:
    """Base class for stack trace transformation functions."""
    parent: Incomplete
    def __enter__(self): ...
    def __exit__(self, unused_type: type[BaseException] | None, unused_value: BaseException | None, unused_traceback: types.TracebackType | None) -> None: ...
    def update(self) -> None: ...

class StackTraceMapper(StackTraceTransform):
    """Allows remapping traceback information to different source code."""
    internal_map: Incomplete
    def __init__(self) -> None: ...
    def update(self) -> None: ...
    def get_effective_source_map(self) -> None:
        """Returns a map (filename, lineno) -> (filename, lineno, function_name)."""

EMPTY_DICT: Incomplete

class SentinelMapper(StackTraceMapper):
    def get_effective_source_map(self): ...

class StackTraceFilter(StackTraceTransform):
    """Allows filtering traceback information by removing superfluous frames."""
    internal_set: Incomplete
    def __init__(self) -> None: ...
    def update(self) -> None: ...
    def get_filtered_filenames(self) -> None: ...

EMPTY_SET: Incomplete

class SentinelFilter(StackTraceFilter):
    def get_filtered_filenames(self): ...

class CurrentModuleFilter(StackTraceFilter):
    """Filters stack frames from the module where this is used (best effort)."""
    def __init__(self) -> None: ...
    def get_filtered_filenames(self): ...

def extract_stack():
    """An eager-friendly alternative to traceback.extract_stack.

  Returns:
    A list-like FrameSummary containing StackFrame-like objects, which are
    namedtuple-like objects with the following fields: filename, lineno, name,
    line, meant to masquerade as traceback.FrameSummary objects.
  """
def extract_stack_for_op(c_op, stacklevel: int = 1) -> None:
    """Attaches the current stack trace to `c_op`.

  Args:
    c_op: a TF_Operation object.
    stacklevel: An integer for ignoring Python wrapper stack frames.
      The default value of 1 ignores this function from the frame.
  """

StackSummary: Incomplete
FrameSummary: Incomplete
