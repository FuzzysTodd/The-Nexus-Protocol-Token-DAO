from _typeshed import Incomplete
from collections import defaultdict

class BoundDictionary(defaultdict):
    """
    A default dictionary where elements are tightly coupled.

    The factory method is responsible for binding the parent object to the child.

    If a reference attribute is assigned then child objects will have the key assigned to this.

    Otherwise it's just a defaultdict.
    """
    reference: Incomplete
    def __init__(self, reference: Incomplete | None = None, *args, **kw) -> None: ...
    def __getitem__(self, key): ...
