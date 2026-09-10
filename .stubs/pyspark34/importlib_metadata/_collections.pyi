import collections
from _typeshed import Incomplete
from typing import NamedTuple

class FreezableDefaultDict(collections.defaultdict):
    """
    Often it is desirable to prevent the mutation of
    a default dict after its initial construction, such
    as to prevent mutation during iteration.

    >>> dd = FreezableDefaultDict(list)
    >>> dd[0].append('1')
    >>> dd.freeze()
    >>> dd[1]
    []
    >>> len(dd)
    1
    """
    def __missing__(self, key): ...
    def freeze(self): ...

class Pair(NamedTuple('Pair', [('name', Incomplete), ('value', Incomplete)])):
    @classmethod
    def parse(cls, text): ...
