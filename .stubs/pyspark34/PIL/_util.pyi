from _typeshed import Incomplete

def is_path(f): ...
def is_directory(f):
    """Checks if an object is a string, and that it points to a directory."""

class DeferredError:
    ex: Incomplete
    def __init__(self, ex) -> None: ...
    def __getattr__(self, elt) -> None: ...
