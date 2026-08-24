import gc
from . import config as config, mock as mock
from .. import inspect as inspect
from ..engine import Connection as Connection
from ..schema import Column as Column, DropConstraint as DropConstraint, DropTable as DropTable, ForeignKeyConstraint as ForeignKeyConstraint, MetaData as MetaData, Table as Table
from ..sql import schema as schema
from ..sql.sqltypes import Integer as Integer
from ..util import decorator as decorator, defaultdict as defaultdict, has_refcount_gc as has_refcount_gc, inspect_getfullargspec as inspect_getfullargspec
from _typeshed import Incomplete
from collections.abc import Generator

def non_refcount_gc_collect(*args) -> None: ...
gc_collect = non_refcount_gc_collect
lazy_gc = non_refcount_gc_collect
gc_collect = gc.collect

def picklers() -> Generator[Incomplete, None, Incomplete]: ...
def random_choices(population, k: int = 1): ...
def round_decimal(value, prec): ...

class RandomSet(set):
    def __iter__(self): ...
    def pop(self): ...
    def union(self, other): ...
    def difference(self, other): ...
    def intersection(self, other): ...
    def copy(self): ...

def conforms_partial_ordering(tuples, sorted_elements):
    """True if the given sorting conforms to the given partial ordering."""
def all_partial_orderings(tuples, elements): ...
def function_named(fn, name):
    '''Return a function with a given __name__.

    Will assign to __name__ and return the original function if possible on
    the Python implementation, otherwise a new function will be constructed.

    This function should be phased out as much as possible
    in favor of @decorator.   Tests that "generate" many named tests
    should be modernized.

    '''
def run_as_contextmanager(ctx, fn, *arg, **kw):
    """Run the given function under the given contextmanager,
    simulating the behavior of 'with' to support older
    Python versions.

    This is not necessary anymore as we have placed 2.6
    as minimum Python version, however some tests are still using
    this structure.

    """
def rowset(results):
    """Converts the results of sql execution into a plain set of column tuples.

    Useful for asserting the results of an unordered query.
    """
def fail(msg) -> None: ...
def provide_metadata(fn, *args, **kw):
    '''Provide bound MetaData for a single test, dropping afterwards.

    Legacy; use the "metadata" pytest fixture.

    '''
def flag_combinations(*combinations):
    """A facade around @testing.combinations() oriented towards boolean
    keyword-based arguments.

    Basically generates a nice looking identifier based on the keywords
    and also sets up the argument names.

    E.g.::

        @testing.flag_combinations(
            dict(lazy=False, passive=False),
            dict(lazy=True, passive=False),
            dict(lazy=False, passive=True),
            dict(lazy=False, passive=True, raiseload=True),
        )


    would result in::

        @testing.combinations(
            ('', False, False, False),
            ('lazy', True, False, False),
            ('lazy_passive', True, True, False),
            ('lazy_passive', True, True, True),
            id_='iaaa',
            argnames='lazy,passive,raiseload'
        )

    """
def lambda_combinations(lambda_arg_sets, **kw): ...
def resolve_lambda(__fn, **kw):
    """Given a no-arg lambda and a namespace, return a new lambda that
    has all the values filled in.

    This is used so that we can have module-level fixtures that
    refer to instance-level variables using lambdas.

    """
def metadata_fixture(ddl: str = 'function'):
    """Provide MetaData for a pytest fixture."""
def force_drop_names(*names):
    """Force the given table names to be dropped after test complete,
    isolating for foreign key cycles

    """

class adict(dict):
    """Dict keys available as attributes.  Shadows."""
    def __getattribute__(self, key): ...
    def __call__(self, *keys): ...
    get_all = __call__

def drop_all_tables_from_metadata(metadata, engine_or_connection) -> None: ...
def drop_all_tables(engine, inspector, schema: Incomplete | None = None, consider_schemas=(None,), include_names: Incomplete | None = None) -> None: ...
def teardown_events(event_cls): ...
def total_size(o):
    """Returns the approximate memory footprint an object and all of its
    contents.

    source: https://code.activestate.com/recipes/577504/


    """
def count_cache_key_tuples(tup):
    """given a cache key tuple, counts how many instances of actual
    tuples are found.

    used to alert large jumps in cache key complexity.

    """
