from _typeshed import Incomplete
from collections.abc import Generator
from setuptools.extern.more_itertools import consume as consume

def ensure_unique(iterable, key=...) -> Generator[Incomplete, None, Incomplete]:
    """
    Wrap an iterable to raise a ValueError if non-unique values are encountered.

    >>> list(ensure_unique('abc'))
    ['a', 'b', 'c']
    >>> consume(ensure_unique('abca'))
    Traceback (most recent call last):
    ...
    ValueError: Duplicate element 'a' encountered.
    """
