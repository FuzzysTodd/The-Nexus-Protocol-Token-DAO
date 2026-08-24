from . import base as base
from ..constants import namespaces as namespaces, voidElements as voidElements
from _typeshed import Incomplete
from collections.abc import Generator

class TreeWalker(base.TreeWalker):
    def __iter__(self): ...
    def tokens(self, event, next) -> Generator[Incomplete, None, None]: ...
