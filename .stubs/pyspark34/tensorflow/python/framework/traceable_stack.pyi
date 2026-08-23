from _typeshed import Incomplete

class TraceableObject:
    """Wrap an object together with its the code definition location."""
    SUCCESS: Incomplete
    HEURISTIC_USED: Incomplete
    FAILURE: Incomplete
    obj: Incomplete
    filename: Incomplete
    lineno: Incomplete
    def __init__(self, obj, filename: Incomplete | None = None, lineno: Incomplete | None = None) -> None: ...
    def set_filename_and_line_from_caller(self, offset: int = 0):
        """Set filename and line using the caller's stack frame.

    If the requested stack information is not available, a heuristic may
    be applied and self.HEURISTIC USED will be returned.  If the heuristic
    fails then no change will be made to the filename and lineno members
    (None by default) and self.FAILURE will be returned.

    Args:
      offset: Integer.  If 0, the caller's stack frame is used.  If 1,
          the caller's caller's stack frame is used.  Larger values are
          permissible but if out-of-range (larger than the number of stack
          frames available) the outermost stack frame will be used.

    Returns:
      TraceableObject.SUCCESS if appropriate stack information was found,
      TraceableObject.HEURISTIC_USED if the offset was larger than the stack,
      and TraceableObject.FAILURE if the stack was empty.
    """
    def copy_metadata(self):
        """Return a TraceableObject like this one, but without the object."""

class TraceableStack:
    """A stack of TraceableObjects."""
    def __init__(self, existing_stack: Incomplete | None = None) -> None:
        """Constructor.

    Args:
      existing_stack: [TraceableObject, ...] If provided, this object will
        set its new stack to a SHALLOW COPY of existing_stack.
    """
    def push_obj(self, obj, offset: int = 0):
        """Add object to the stack and record its filename and line information.

    Args:
      obj: An object to store on the stack.
      offset: Integer.  If 0, the caller's stack frame is used.  If 1,
          the caller's caller's stack frame is used.

    Returns:
      TraceableObject.SUCCESS if appropriate stack information was found,
      TraceableObject.HEURISTIC_USED if the stack was smaller than expected,
      and TraceableObject.FAILURE if the stack was empty.
    """
    def pop_obj(self):
        """Remove last-inserted object and return it, without filename/line info."""
    def peek_top_obj(self):
        """Return the most recent stored object."""
    def peek_objs(self):
        """Return iterator over stored objects ordered newest to oldest."""
    def peek_traceable_objs(self):
        """Return iterator over stored TraceableObjects ordered newest to oldest."""
    def __len__(self) -> int:
        """Return number of items on the stack, and used for truth-value testing."""
    def copy(self):
        """Return a copy of self referencing the same objects but in a new list.

    This method is implemented to support thread-local stacks.

    Returns:
      TraceableStack with a new list that holds existing objects.
    """
