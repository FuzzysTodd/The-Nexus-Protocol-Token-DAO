from debugpy.common import log as log

def dump() -> None:
    """Dump stacks of all threads in this process, except for the current thread."""
def dump_after(secs) -> None:
    """Invokes dump() on a background thread after waiting for the specified time."""
