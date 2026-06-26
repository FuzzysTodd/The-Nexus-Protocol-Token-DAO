from . import testing as testing
from .. import assert_raises as assert_raises, config as config, engines as engines, eq_ as eq_, fixtures as fixtures, is_not_none as is_not_none, is_true as is_true, ne_ as ne_, provide_metadata as provide_metadata
from ... import Integer as Integer, String as String, bindparam as bindparam, dialects as dialects, event as event, exc as exc, literal_column as literal_column, select as select
from ...sql.compiler import Compiled as Compiled
from ...util import inspect_getfullargspec as inspect_getfullargspec
from ..assertions import expect_raises as expect_raises, expect_raises_message as expect_raises_message
from ..config import requirements as requirements
from ..provision import set_default_schema_on_connection as set_default_schema_on_connection
from ..schema import Column as Column, Table as Table
from _typeshed import Incomplete
from collections.abc import Generator

class PingTest(fixtures.TestBase):
    __backend__: bool
    def test_do_ping(self) -> None: ...

class ArgSignatureTest(fixtures.TestBase):
    '''test that all visit_XYZ() in :class:`_sql.Compiler` subclasses have
    ``**kw``, for #8988.

    This test uses runtime code inspection.   Does not need to be a
    ``__backend__`` test as it only needs to run once provided all target
    dialects have been imported.

    For third party dialects, the suite would be run with that third
    party as a "--dburi", which means its compiler classes will have been
    imported by the time this test runs.

    '''
    def all_subclasses(self, request) -> Generator[Incomplete, None, None]: ...
    def test_all_visit_methods_accept_kw(self, all_subclasses) -> None: ...

class ExceptionTest(fixtures.TablesTest):
    """Test basic exception wrapping.

    DBAPIs vary a lot in exception behavior so to actually anticipate
    specific exceptions from real round trips, we need to be conservative.

    """
    run_deletes: str
    __backend__: bool
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    def test_integrity_error(self) -> None: ...
    def test_exception_with_non_ascii(self) -> None: ...

class IsolationLevelTest(fixtures.TestBase):
    __backend__: bool
    __requires__: Incomplete
    def test_default_isolation_level(self) -> None: ...
    def test_non_default_isolation_level(self) -> None: ...
    def test_all_levels(self) -> None: ...
    def test_invalid_level_execution_option(self, connection_no_trans) -> None:
        """test for the new get_isolation_level_values() method"""
    def test_invalid_level_engine_param(self, testing_engine) -> None:
        """test for the new get_isolation_level_values() method
        and support for the dialect-level 'isolation_level' parameter.

        """
    def test_dialect_user_setting_is_restored(self, testing_engine) -> None: ...

class AutocommitIsolationTest(fixtures.TablesTest):
    run_deletes: str
    __requires__: Incomplete
    __backend__: bool
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    def test_autocommit_on(self, connection_no_trans) -> None: ...
    def test_autocommit_off(self, connection_no_trans) -> None: ...
    def test_turn_autocommit_off_via_default_iso_level(self, connection_no_trans) -> None: ...
    def test_dialect_autocommit_is_restored(self, testing_engine, use_dialect_setting) -> None:
        """test #10147"""

class EscapingTest(fixtures.TestBase):
    def test_percent_sign_round_trip(self) -> None:
        """test that the DBAPI accommodates for escaped / nonescaped
        percent signs in a way that matches the compiler

        """

class WeCanSetDefaultSchemaWEventsTest(fixtures.TestBase):
    __backend__: bool
    __requires__: Incomplete
    def test_control_case(self) -> None: ...
    def test_wont_work_wo_insert(self) -> None: ...
    def test_schema_change_on_connect(self) -> None: ...
    def test_schema_change_works_w_transactions(self) -> None: ...

class FutureWeCanSetDefaultSchemaWEventsTest(fixtures.FutureEngineMixin, WeCanSetDefaultSchemaWEventsTest): ...

class DifficultParametersTest(fixtures.TestBase):
    __backend__: bool
    tough_parameters: Incomplete
    def test_round_trip_same_named_column(self, paramname, connection, metadata) -> None: ...
    def multirow_fixture(self, metadata, connection) -> Generator[Incomplete, None, None]: ...
    def test_standalone_bindparam_escape(self, paramname, connection, multirow_fixture) -> None: ...
    def test_standalone_bindparam_escape_expanding(self, paramname, connection, multirow_fixture) -> None: ...

class ReturningGuardsTest(fixtures.TablesTest):
    """test that the various 'returning' flags are set appropriately"""
    __backend__: bool
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    def run_stmt(self, connection): ...
    def test_insert_single(self, connection, run_stmt) -> None: ...
    def test_insert_many(self, connection, run_stmt) -> None: ...
    def test_update_single(self, connection, run_stmt) -> None: ...
    def test_update_many(self, connection, run_stmt) -> None: ...
    def test_delete_single(self, connection, run_stmt) -> None: ...
    def test_delete_many(self, connection, run_stmt) -> None: ...
