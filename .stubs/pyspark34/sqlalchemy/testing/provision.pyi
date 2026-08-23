from . import config as config, engines as engines, util as util
from .. import exc as exc, inspect as inspect
from ..sql import ddl as ddl, schema as schema
from _typeshed import Incomplete
from collections.abc import Generator

log: Incomplete
FOLLOWER_IDENT: Incomplete

class register:
    fns: Incomplete
    decorator: Incomplete
    def __init__(self, decorator: Incomplete | None = None) -> None: ...
    @classmethod
    def init(cls, fn): ...
    @classmethod
    def init_decorator(cls, decorator): ...
    def for_db(self, *dbnames): ...
    def __call__(self, cfg, *arg, **kw): ...

def create_follower_db(follower_ident) -> None: ...
def setup_config(db_url, options, file_config, follower_ident): ...
def drop_follower_db(follower_ident) -> None: ...
def generate_db_urls(db_urls, extra_drivers) -> Generator[Incomplete, None, None]:
    """Generate a set of URLs to test given configured URLs plus additional
    driver names.

    Given::

        --dburi postgresql://db1          --dburi postgresql://db2          --dburi postgresql://db2          --dbdriver=psycopg2 --dbdriver=asyncpg?async_fallback=true

    Noting that the default postgresql driver is psycopg2,  the output
    would be::

        postgresql+psycopg2://db1
        postgresql+asyncpg://db1
        postgresql+psycopg2://db2
        postgresql+psycopg2://db3

    That is, for the driver in a --dburi, we want to keep that and use that
    driver for each URL it's part of .   For a driver that is only
    in --dbdrivers, we want to use it just once for one of the URLs.
    for a driver that is both coming from --dburi as well as --dbdrivers,
    we want to keep it in that dburi.

    Driver specific query options can be specified by added them to the
    driver name. For example, to enable the async fallback option for
    asyncpg::

        --dburi postgresql://db1          --dbdriver=asyncpg?async_fallback=true

    """
def generate_driver_url(url, driver, query_str): ...
def drop_all_schema_objects_pre_tables(cfg, eng) -> None: ...
def drop_all_schema_objects_post_tables(cfg, eng) -> None: ...
def drop_all_schema_objects(cfg, eng) -> None: ...
def drop_views(cfg, eng) -> None: ...
def drop_materialized_views(cfg, eng) -> None: ...
def create_db(cfg, eng, ident) -> None:
    """Dynamically create a database for testing.

    Used when a test run will employ multiple processes, e.g., when run
    via `tox` or `pytest -n4`.
    """
def drop_db(cfg, eng, ident) -> None:
    """Drop a database that we dynamically created for testing."""
def update_db_opts(db_url, db_opts, options) -> None:
    """Set database options (db_opts) for a test database that we created."""
def post_configure_engine(url, engine, follower_ident) -> None:
    """Perform extra steps after configuring an engine for testing.

    (For the internal dialects, currently only used by sqlite, oracle)
    """
def follower_url_from_main(url, ident):
    '''Create a connection URL for a dynamically-created test database.

    :param url: the connection URL specified when the test run was invoked
    :param ident: the pytest-xdist "worker identifier" to be used as the
                  database name
    '''
def configure_follower(cfg, ident) -> None:
    """Create dialect-specific config settings for a follower database."""
def run_reap_dbs(url, ident) -> None:
    """Remove databases that were created during the test process, after the
    process has ended.

    This is an optional step that is invoked for certain backends that do not
    reliably release locks on the database as long as a process is still in
    use. For the internal dialects, this is currently only necessary for
    mssql and oracle.
    """
def reap_dbs(idents_file) -> None: ...
def temp_table_keyword_args(cfg, eng) -> None:
    """Specify keyword arguments for creating a temporary Table.

    Dialect-specific implementations of this method will return the
    kwargs that are passed to the Table method when creating a temporary
    table for testing, e.g., in the define_temp_tables method of the
    ComponentReflectionTest class in suite/test_reflection.py
    """
def prepare_for_drop_tables(config, connection) -> None: ...
def stop_test_class_outside_fixtures(config, db, testcls) -> None: ...
def get_temp_table_name(cfg, eng, base_name):
    '''Specify table name for creating a temporary Table.

    Dialect-specific implementations of this method will return the
    name to use when creating a temporary table for testing,
    e.g., in the define_temp_tables method of the
    ComponentReflectionTest class in suite/test_reflection.py

    Default to just the base name since that\'s what most dialects will
    use. The mssql dialect\'s implementation will need a "#" prepended.
    '''
def set_default_schema_on_connection(cfg, dbapi_connection, schema_name) -> None: ...
def upsert(cfg, table, returning, *, set_lambda: Incomplete | None = None, sort_by_parameter_order: bool = False) -> None:
    """return the backends insert..on conflict / on dupe etc. construct.

    while we should add a backend-neutral upsert construct as well, such as
    insert().upsert(), it's important that we continue to test the
    backend-specific insert() constructs since if we do implement
    insert().upsert(), that would be using a different codepath for the things
    we need to test like insertmanyvalues, etc.

    """
def normalize_sequence(cfg, sequence):
    """Normalize sequence parameters for dialect that don't start with 1
    by default.

    The default implementation does nothing
    """
