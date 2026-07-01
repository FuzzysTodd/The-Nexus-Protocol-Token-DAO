from _typeshed import Incomplete

class StringIOTree:
    """
    See module docs.
    """
    prepended_children: Incomplete
    stream: Incomplete
    write: Incomplete
    markers: Incomplete
    def __init__(self, stream: Incomplete | None = None) -> None: ...
    def empty(self): ...
    def getvalue(self): ...
    def copyto(self, target) -> None:
        """Potentially cheaper than getvalue as no string concatenation
        needs to happen."""
    def commit(self) -> None: ...
    def reset(self) -> None: ...
    def insert(self, iotree) -> None:
        """
        Insert a StringIOTree (and all of its contents) at this location.
        Further writing to self appears after what is inserted.
        """
    def insertion_point(self):
        """
        Returns a new StringIOTree, which is left behind at the current position
        (it what is written to the result will appear right before whatever is
        next written to self).

        Calling getvalue() or copyto() on the result will only return the
        contents written to it.
        """
    def allmarkers(self): ...
