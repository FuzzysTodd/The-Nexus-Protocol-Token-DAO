from pandas.core.indexing import IndexingMixin as IndexingMixin
from typing import Generic

class NDFrameIndexerBase(Generic[_IndexingMixinT]):
    name: str
    obj: _IndexingMixinT
    def __init__(self, name: str, obj: _IndexingMixinT) -> None: ...
    @property
    def ndim(self) -> int: ...
