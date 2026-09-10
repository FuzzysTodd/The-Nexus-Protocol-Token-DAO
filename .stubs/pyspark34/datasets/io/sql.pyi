import sqlalchemy
import sqlite3
from .. import Dataset as Dataset, Features as Features, config as config
from ..formatting import query_table as query_table
from ..packaged_modules.sql.sql import Sql as Sql
from ..utils import logging as logging
from .abc import AbstractDatasetInputStream as AbstractDatasetInputStream
from _typeshed import Incomplete

class SqlDatasetReader(AbstractDatasetInputStream):
    builder: Incomplete
    def __init__(self, sql: str | sqlalchemy.sql.Selectable, con: str | sqlalchemy.engine.Connection | sqlalchemy.engine.Engine | sqlite3.Connection, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, **kwargs) -> None: ...
    def read(self): ...

class SqlDatasetWriter:
    dataset: Incomplete
    name: Incomplete
    con: Incomplete
    batch_size: Incomplete
    num_proc: Incomplete
    to_sql_kwargs: Incomplete
    def __init__(self, dataset: Dataset, name: str, con: str | sqlalchemy.engine.Connection | sqlalchemy.engine.Engine | sqlite3.Connection, batch_size: int | None = None, num_proc: int | None = None, **to_sql_kwargs) -> None: ...
    def write(self) -> int: ...
