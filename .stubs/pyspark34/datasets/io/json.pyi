from .. import Dataset as Dataset, Features as Features, NamedSplit as NamedSplit, config as config
from ..formatting import query_table as query_table
from ..packaged_modules.json.json import Json as Json
from ..utils import logging as logging
from ..utils.typing import NestedDataStructureLike as NestedDataStructureLike, PathLike as PathLike
from .abc import AbstractDatasetReader as AbstractDatasetReader
from _typeshed import Incomplete
from typing import BinaryIO

class JsonDatasetReader(AbstractDatasetReader):
    field: Incomplete
    builder: Incomplete
    def __init__(self, path_or_paths: NestedDataStructureLike[PathLike], split: NamedSplit | None = None, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, streaming: bool = False, field: str | None = None, num_proc: int | None = None, **kwargs) -> None: ...
    def read(self): ...

class JsonDatasetWriter:
    dataset: Incomplete
    path_or_buf: Incomplete
    batch_size: Incomplete
    num_proc: Incomplete
    encoding: str
    to_json_kwargs: Incomplete
    def __init__(self, dataset: Dataset, path_or_buf: PathLike | BinaryIO, batch_size: int | None = None, num_proc: int | None = None, **to_json_kwargs) -> None: ...
    def write(self) -> int: ...
