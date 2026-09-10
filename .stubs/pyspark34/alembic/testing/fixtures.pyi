from ..environment import EnvironmentContext as EnvironmentContext
from ..migration import MigrationContext as MigrationContext
from ..operations import Operations as Operations
from ..util import sqla_compat as sqla_compat
from ..util.sqla_compat import create_mock_engine as create_mock_engine, sqla_14 as sqla_14, sqla_2 as sqla_2
from _typeshed import Incomplete
from collections.abc import Generator
from sqlalchemy.testing.fixtures import TablesTest as SQLAlchemyTablesTest, TestBase as SQLAlchemyTestBase

testing_config: Incomplete

class TestBase(SQLAlchemyTestBase):
    is_sqlalchemy_future = sqla_2
    def ops_context(self, migration_context) -> Generator[Incomplete, None, None]: ...
    def migration_context(self, connection): ...
    def connection(self) -> Generator[Incomplete, None, None]: ...

class TablesTest(TestBase, SQLAlchemyTablesTest): ...

class FutureEngineMixin:
    __requires__: Incomplete

def capture_db(dialect: str = 'postgresql://'): ...
def capture_context_buffer(**kw) -> Generator[Incomplete, None, Incomplete]: ...
def capture_engine_context_buffer(**kw) -> Generator[Incomplete, None, Incomplete]: ...
def op_fixture(dialect: str = 'default', as_sql: bool = False, naming_convention: Incomplete | None = None, literal_binds: bool = False, native_boolean: Incomplete | None = None): ...

class AlterColRoundTripFixture:
    __requires__: Incomplete
    conn: Incomplete
    ctx: Incomplete
    op: Incomplete
    metadata: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
