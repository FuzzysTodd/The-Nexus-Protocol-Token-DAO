from .. import Features as Features, NamedSplit as NamedSplit
from ..packaged_modules.text.text import Text as Text
from ..utils.typing import NestedDataStructureLike as NestedDataStructureLike, PathLike as PathLike
from .abc import AbstractDatasetReader as AbstractDatasetReader
from _typeshed import Incomplete

class TextDatasetReader(AbstractDatasetReader):
    builder: Incomplete
    def __init__(self, path_or_paths: NestedDataStructureLike[PathLike], split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, streaming: bool = False, num_proc: int | None = None, **kwargs) -> None: ...
    def read(self): ...
