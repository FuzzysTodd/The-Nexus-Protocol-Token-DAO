from _typeshed import Incomplete

__all__ = ['looper']

class looper:
    """
    Helper for looping (particularly in templates)

    Use this like::

        for loop, item in looper(seq):
            if loop.first:
                ...
    """
    seq: Incomplete
    def __init__(self, seq) -> None: ...
    def __iter__(self): ...

class looper_iter:
    seq: Incomplete
    pos: int
    def __init__(self, seq) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class loop_pos:
    seq: Incomplete
    pos: Incomplete
    def __init__(self, seq, pos) -> None: ...
    def index(self): ...
    index: Incomplete
    def number(self): ...
    number: Incomplete
    def item(self): ...
    item: Incomplete
    def __next__(self): ...
    __next__: Incomplete
    next = __next__
    def previous(self): ...
    previous: Incomplete
    def odd(self): ...
    odd: Incomplete
    def even(self): ...
    even: Incomplete
    def first(self): ...
    first: Incomplete
    def last(self): ...
    last: Incomplete
    def length(self): ...
    length: Incomplete
    def first_group(self, getter: Incomplete | None = None):
        """
        Returns true if this item is the start of a new group,
        where groups mean that some attribute has changed.  The getter
        can be None (the item itself changes), an attribute name like
        ``'.attr'``, a function, or a dict key or list index.
        """
    def last_group(self, getter: Incomplete | None = None):
        """
        Returns true if this item is the end of a new group,
        where groups mean that some attribute has changed.  The getter
        can be None (the item itself changes), an attribute name like
        ``'.attr'``, a function, or a dict key or list index.
        """
