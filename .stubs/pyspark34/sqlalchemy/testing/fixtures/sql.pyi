from .. import config as config, mock as mock
from ... import event as event, util as util
from ...schema import sort_tables_and_constraints as sort_tables_and_constraints
from ...sql import visitors as visitors
from ...sql.elements import ClauseElement as ClauseElement
from ..assertions import eq_ as eq_, ne_ as ne_
from ..util import adict as adict, drop_all_tables_from_metadata as drop_all_tables_from_metadata
from .base import TestBase as TestBase
from _typeshed import Incomplete

class TablesTest(TestBase):
    run_setup_bind: str
    run_define_tables: str
    run_create_tables: str
    run_inserts: str
    run_deletes: str
    run_dispose_bind: Incomplete
    bind: Incomplete
    tables: Incomplete
    other: Incomplete
    sequences: Incomplete
    @property
    def tables_test_metadata(self): ...
    @classmethod
    def setup_bind(cls): ...
    @classmethod
    def dispose_bind(cls, bind) -> None: ...
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    @classmethod
    def fixtures(cls): ...
    @classmethod
    def insert_data(cls, connection) -> None: ...
    def sql_count_(self, count, fn) -> None: ...
    def sql_eq_(self, callable_, statements) -> None: ...

class NoCache: ...

class RemovesEvents:
    def event_listen(self, target, name, fn, **kw) -> None: ...

class ComputedReflectionFixtureTest(TablesTest):
    run_inserts: Incomplete
    run_deletes: Incomplete
    __backend__: bool
    __requires__: Incomplete
    regexp: Incomplete
    def normalize(self, text): ...
    @classmethod
    def define_tables(cls, metadata) -> None: ...

class CacheKeyFixture: ...

def insertmanyvalues_fixture(connection, randomize_rows: bool = False, warn_on_downgraded: bool = False): ...
