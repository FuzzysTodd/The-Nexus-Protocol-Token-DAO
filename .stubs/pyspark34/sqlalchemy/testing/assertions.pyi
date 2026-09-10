from . import assertsql as assertsql, config as config, engines as engines, mock as mock
from .. import schema as schema, sql as sql, util as util
from ..engine import default as default, url as url
from ..sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL as LABEL_STYLE_TABLENAME_PLUS_COL
from ..util import decorator as decorator
from .exclusions import db_spec as db_spec
from .util import fail as fail
from _typeshed import Incomplete
from collections.abc import Generator

def expect_warnings(*messages, **kw):
    """Context manager which expects one or more warnings.

    With no arguments, squelches all SAWarning emitted via
    sqlalchemy.util.warn and sqlalchemy.util.warn_limited.   Otherwise
    pass string expressions that will match selected warnings via regex;
    all non-matching warnings are sent through.

    The expect version **asserts** that the warnings were in fact seen.

    Note that the test suite sets SAWarning warnings to raise exceptions.

    """
def expect_warnings_on(db, *messages, **kw) -> Generator[None, None, None]:
    """Context manager which expects one or more warnings on specific
    dialects.

    The expect version **asserts** that the warnings were in fact seen.

    """
def emits_warning(*messages):
    """Decorator form of expect_warnings().

    Note that emits_warning does **not** assert that the warnings
    were in fact seen.

    """
def expect_deprecated(*messages, **kw): ...
def expect_deprecated_20(*messages, **kw): ...
def emits_warning_on(db, *messages):
    """Mark a test as emitting a warning on a specific dialect.

    With no arguments, squelches all SAWarning failures.  Or pass one or more
    strings; these will be matched to the root of the warning description by
    warnings.filterwarnings().

    Note that emits_warning_on does **not** assert that the warnings
    were in fact seen.

    """
def uses_deprecated(*messages):
    """Mark a test as immune from fatal deprecation warnings.

    With no arguments, squelches all SADeprecationWarning failures.
    Or pass one or more strings; these will be matched to the root
    of the warning description by warnings.filterwarnings().

    As a special case, you may pass a function name prefixed with //
    and it will be re-written as needed to match the standard warning
    verbiage emitted by the sqlalchemy.util.deprecated decorator.

    Note that uses_deprecated does **not** assert that the warnings
    were in fact seen.

    """
def global_cleanup_assertions() -> None:
    """Check things that have to be finalized at the end of a test suite.

    Hardcoded at the moment, a modular system can be built here
    to support things like PG prepared transactions, tables all
    dropped, etc.

    """
def int_within_variance(expected, received, variance) -> None: ...
def eq_regex(a, b, msg: Incomplete | None = None) -> None: ...
def eq_(a, b, msg: Incomplete | None = None) -> None:
    """Assert a == b, with repr messaging on failure."""
def ne_(a, b, msg: Incomplete | None = None) -> None:
    """Assert a != b, with repr messaging on failure."""
def le_(a, b, msg: Incomplete | None = None) -> None:
    """Assert a <= b, with repr messaging on failure."""
def is_instance_of(a, b, msg: Incomplete | None = None) -> None: ...
def is_none(a, msg: Incomplete | None = None) -> None: ...
def is_not_none(a, msg: Incomplete | None = None) -> None: ...
def is_true(a, msg: Incomplete | None = None) -> None: ...
def is_false(a, msg: Incomplete | None = None) -> None: ...
def is_(a, b, msg: Incomplete | None = None) -> None:
    """Assert a is b, with repr messaging on failure."""
def is_not(a, b, msg: Incomplete | None = None) -> None:
    """Assert a is not b, with repr messaging on failure."""
is_not_ = is_not

def in_(a, b, msg: Incomplete | None = None) -> None:
    """Assert a in b, with repr messaging on failure."""
def not_in(a, b, msg: Incomplete | None = None) -> None:
    """Assert a in not b, with repr messaging on failure."""
not_in_ = not_in

def startswith_(a, fragment, msg: Incomplete | None = None) -> None:
    """Assert a.startswith(fragment), with repr messaging on failure."""
def eq_ignore_whitespace(a, b, msg: Incomplete | None = None) -> None: ...
def assert_raises(except_cls, callable_, *args, **kw): ...
def assert_raises_context_ok(except_cls, callable_, *args, **kw): ...
def assert_raises_message(except_cls, msg, callable_, *args, **kwargs): ...
def assert_warns(except_cls, callable_, *args, **kwargs):
    """legacy adapter function for functions that were previously using
    assert_raises with SAWarning or similar.

    has some workarounds to accommodate the fact that the callable completes
    with this approach rather than stopping at the exception raise.


    """
def assert_warns_message(except_cls, msg, callable_, *args, **kwargs):
    """legacy adapter function for functions that were previously using
    assert_raises with SAWarning or similar.

    has some workarounds to accommodate the fact that the callable completes
    with this approach rather than stopping at the exception raise.

    Also uses regex.search() to match the given message to the error string
    rather than regex.match().

    """
def assert_raises_message_context_ok(except_cls, msg, callable_, *args, **kwargs): ...

class _ErrorContainer:
    error: Incomplete

def expect_raises(except_cls, check_context: bool = True): ...
def expect_raises_message(except_cls, msg, check_context: bool = True): ...

class AssertsCompiledSQL:
    test_statement: Incomplete
    supports_execution: Incomplete
    def assert_compile(self, clause, result, params: Incomplete | None = None, checkparams: Incomplete | None = None, for_executemany: bool = False, check_literal_execute: Incomplete | None = None, check_post_param: Incomplete | None = None, dialect: Incomplete | None = None, checkpositional: Incomplete | None = None, check_prefetch: Incomplete | None = None, use_default_dialect: bool = False, allow_dialect_select: bool = False, supports_default_values: bool = True, supports_default_metavalue: bool = True, literal_binds: bool = False, render_postcompile: bool = False, schema_translate_map: Incomplete | None = None, render_schema_translate: bool = False, default_schema_name: Incomplete | None = None, from_linting: bool = False, check_param_order: bool = True, use_literal_execute_for_simple_int: bool = False): ...

class ComparesTables:
    def assert_tables_equal(self, table, reflected_table, strict_types: bool = False, strict_constraints: bool = True) -> None: ...
    def assert_types_base(self, c1, c2) -> None: ...

class AssertsExecutionResults:
    def assert_result(self, result, class_, *objects) -> None: ...
    def assert_list(self, result, class_, list_) -> None: ...
    def assert_row(self, class_, rowobj, desc) -> None: ...
    def assert_unordered_result(self, result, cls, *expected):
        """As assert_result, but the order of objects is not considered.

        The algorithm is very expensive but not a big deal for the small
        numbers of rows that the test suite manipulates.
        """
    def sql_execution_asserter(self, db: Incomplete | None = None): ...
    def assert_sql_execution(self, db, callable_, *rules): ...
    def assert_sql(self, db, callable_, rules): ...
    def assert_sql_count(self, db, callable_, count): ...
    def assert_execution(self, db, *rules) -> Generator[None, None, None]: ...
    def assert_statement_count(self, db, count): ...
    def assert_statement_count_multi_db(self, dbs, counts) -> Generator[None, None, None]: ...

class ComparesIndexes:
    def compare_table_index_with_expected(self, table: schema.Table, expected: list, dialect_name: str): ...
