from . import coercions as coercions, operators as operators, roles as roles, visitors as visitors
from .. import exc as exc, util as util
from ..engine.interfaces import _AnyExecuteParams
from ..engine.row import Row as Row
from ..util.typing import Literal as Literal, Protocol as Protocol
from ._typing import _EquivalentColumnMap, is_text_clause as is_text_clause
from .elements import BinaryExpression as BinaryExpression, BindParameter as BindParameter, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement, Grouping as Grouping, KeyedColumnElement as KeyedColumnElement, Label as Label, NamedColumn as NamedColumn, Null as Null, TextClause as TextClause, UnaryExpression as UnaryExpression
from .schema import Column as Column
from .selectable import Alias as Alias, FromClause as FromClause, FromGrouping as FromGrouping, Join as Join, ScalarSelect as ScalarSelect, SelectBase as SelectBase, Selectable as Selectable, TableClause as TableClause, _JoinTargetElement, _SelectIterable
from .visitors import ExternalTraversal as ExternalTraversal, ExternallyTraversible as ExternallyTraversible, _ET
from _typeshed import Incomplete
from collections.abc import Generator
from typing import AbstractSet, Any, Callable, Collection, Iterable, Iterator, List, Sequence, overload

def join_condition(a: FromClause, b: FromClause, a_subset: FromClause | None = None, consider_as_foreign_keys: AbstractSet[ColumnClause[Any]] | None = None) -> ColumnElement[bool]:
    '''Create a join condition between two tables or selectables.

    e.g.::

        join_condition(tablea, tableb)

    would produce an expression along the lines of::

        tablea.c.id==tableb.c.tablea_id

    The join is determined based on the foreign key relationships
    between the two selectables.   If there are multiple ways
    to join, or no way to join, an error is raised.

    :param a_subset: An optional expression that is a sub-component
        of ``a``.  An attempt will be made to join to just this sub-component
        first before looking at the full ``a`` construct, and if found
        will be successful even if there are other ways to join to ``a``.
        This allows the "right side" of a join to be passed thereby
        providing a "natural join".

    '''
def find_join_source(clauses: List[FromClause], join_to: FromClause) -> List[int]:
    """Given a list of FROM clauses and a selectable,
    return the first index and element from the list of
    clauses which can be joined against the selectable.  returns
    None, None if no match is found.

    e.g.::

        clause1 = table1.join(table2)
        clause2 = table4.join(table5)

        join_to = table2.join(table3)

        find_join_source([clause1, clause2], join_to) == clause1

    """
def find_left_clause_that_matches_given(clauses: Sequence[FromClause], join_from: FromClause) -> List[int]:
    """Given a list of FROM clauses and a selectable,
    return the indexes from the list of
    clauses which is derived from the selectable.

    """
def find_left_clause_to_join_from(clauses: Sequence[FromClause], join_to: _JoinTargetElement, onclause: ColumnElement[Any] | None) -> List[int]:
    '''Given a list of FROM clauses, a selectable,
    and optional ON clause, return a list of integer indexes from the
    clauses list indicating the clauses that can be joined from.

    The presence of an "onclause" indicates that at least one clause can
    definitely be joined from; if the list of clauses is of length one
    and the onclause is given, returns that index.   If the list of clauses
    is more than length one, and the onclause is given, attempts to locate
    which clauses contain the same columns.

    '''
def visit_binary_product(fn: Callable[[BinaryExpression[Any], ColumnElement[Any], ColumnElement[Any]], None], expr: ColumnElement[Any]) -> None:
    '''Produce a traversal of the given expression, delivering
    column comparisons to the given function.

    The function is of the form::

        def my_fn(binary, left, right)

    For each binary expression located which has a
    comparison operator, the product of "left" and
    "right" will be delivered to that function,
    in terms of that binary.

    Hence an expression like::

        and_(
            (a + b) == q + func.sum(e + f),
            j == r
        )

    would have the traversal::

        a <eq> q
        a <eq> e
        a <eq> f
        b <eq> q
        b <eq> e
        b <eq> f
        j <eq> r

    That is, every combination of "left" and
    "right" that doesn\'t further contain
    a binary comparison is passed as pairs.

    '''
def find_tables(clause: ClauseElement, *, check_columns: bool = False, include_aliases: bool = False, include_joins: bool = False, include_selects: bool = False, include_crud: bool = False) -> List[TableClause]:
    """locate Table objects within the given expression."""
def unwrap_order_by(clause):
    """Break up an 'order by' expression into individual column-expressions,
    without DESC/ASC/NULLS FIRST/NULLS LAST"""
def unwrap_label_reference(element): ...
def expand_column_list_from_order_by(collist, order_by):
    """Given the columns clause and ORDER BY of a selectable,
    return a list of column expressions that can be added to the collist
    corresponding to the ORDER BY, without repeating those already
    in the collist.

    """
def clause_is_present(clause, search):
    """Given a target clause and a second to search within, return True
    if the target is plainly present in the search without any
    subqueries or aliases involved.

    Basically descends through Joins.

    """
def tables_from_leftmost(clause: FromClause) -> Iterator[FromClause]: ...
def surface_selectables(clause) -> Generator[Incomplete, None, None]: ...
def surface_selectables_only(clause) -> Generator[Incomplete, None, None]: ...
def extract_first_column_annotation(column, annotation_name): ...
def selectables_overlap(left: FromClause, right: FromClause) -> bool:
    """Return True if left/right have some overlapping selectable"""
def bind_values(clause):
    '''Return an ordered list of "bound" values in the given clause.

    E.g.::

        >>> expr = and_(
        ...    table.c.foo==5, table.c.foo==7
        ... )
        >>> bind_values(expr)
        [5, 7]
    '''

class _repr_base:
    max_chars: int
    def trunc(self, value: Any) -> str: ...

class _repr_row(_repr_base):
    """Provide a string view of a row."""
    row: Incomplete
    max_chars: Incomplete
    def __init__(self, row: Row[Any], max_chars: int = 300) -> None: ...

class _long_statement(str): ...

class _repr_params(_repr_base):
    """Provide a string view of bound parameters.

    Truncates display to a given number of 'multi' parameter sets,
    as well as long values to a given number of characters.

    """
    params: Incomplete
    ismulti: Incomplete
    batches: Incomplete
    max_chars: Incomplete
    max_params: Incomplete
    def __init__(self, params: _AnyExecuteParams | None, batches: int, max_params: int = 100, max_chars: int = 300, ismulti: bool | None = None) -> None: ...

def adapt_criterion_to_null(crit: _CE, nulls: Collection[Any]) -> _CE:
    """given criterion containing bind params, convert selected elements
    to IS NULL.

    """
def splice_joins(left: FromClause | None, right: FromClause | None, stop_on: FromClause | None = None) -> FromClause | None: ...
@overload
def reduce_columns(columns: Iterable[ColumnElement[Any]], *clauses: ClauseElement | None, **kw: bool) -> Sequence[ColumnElement[Any]]: ...
@overload
def reduce_columns(columns: _SelectIterable, *clauses: ClauseElement | None, **kw: bool) -> Sequence[ColumnElement[Any] | TextClause]: ...
def criterion_as_pairs(expression, consider_as_foreign_keys: Incomplete | None = None, consider_as_referenced_keys: Incomplete | None = None, any_operator: bool = False):
    """traverse an expression and locate binary criterion pairs."""

class ClauseAdapter(visitors.ReplacingExternalTraversal):
    """Clones and modifies clauses based on column correspondence.

    E.g.::

      table1 = Table('sometable', metadata,
          Column('col1', Integer),
          Column('col2', Integer)
          )
      table2 = Table('someothertable', metadata,
          Column('col1', Integer),
          Column('col2', Integer)
          )

      condition = table1.c.col1 == table2.c.col1

    make an alias of table1::

      s = table1.alias('foo')

    calling ``ClauseAdapter(s).traverse(condition)`` converts
    condition to read::

      s.c.col1 == table2.c.col1

    """
    __traverse_options__: Incomplete
    selectable: Incomplete
    include_fn: Incomplete
    exclude_fn: Incomplete
    equivalents: Incomplete
    adapt_on_names: Incomplete
    adapt_from_selectables: Incomplete
    def __init__(self, selectable: Selectable, equivalents: _EquivalentColumnMap | None = None, include_fn: Callable[[ClauseElement], bool] | None = None, exclude_fn: Callable[[ClauseElement], bool] | None = None, adapt_on_names: bool = False, anonymize_labels: bool = False, adapt_from_selectables: AbstractSet[FromClause] | None = None) -> None: ...
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: _ET) -> _ET: ...
    def replace(self, col: _ET, _include_singleton_constants: bool = False) -> _ET | None: ...

class _ColumnLookup(Protocol):
    @overload
    def __getitem__(self, key: None) -> None: ...
    @overload
    def __getitem__(self, key: ColumnClause[Any]) -> ColumnClause[Any]: ...
    @overload
    def __getitem__(self, key: ColumnElement[Any]) -> ColumnElement[Any]: ...
    @overload
    def __getitem__(self, key: _ET) -> _ET: ...

class ColumnAdapter(ClauseAdapter):
    '''Extends ClauseAdapter with extra utility functions.

    Key aspects of ColumnAdapter include:

    * Expressions that are adapted are stored in a persistent
      .columns collection; so that an expression E adapted into
      an expression E1, will return the same object E1 when adapted
      a second time.   This is important in particular for things like
      Label objects that are anonymized, so that the ColumnAdapter can
      be used to present a consistent "adapted" view of things.

    * Exclusion of items from the persistent collection based on
      include/exclude rules, but also independent of hash identity.
      This because "annotated" items all have the same hash identity as their
      parent.

    * "wrapping" capability is added, so that the replacement of an expression
      E can proceed through a series of adapters.  This differs from the
      visitor\'s "chaining" feature in that the resulting object is passed
      through all replacing functions unconditionally, rather than stopping
      at the first one that returns non-None.

    * An adapt_required option, used by eager loading to indicate that
      We don\'t trust a result row column that is not translated.
      This is to prevent a column from being interpreted as that
      of the child row in a self-referential scenario, see
      inheritance/test_basic.py->EagerTargetingTest.test_adapt_stringency

    '''
    columns: _ColumnLookup
    adapt_required: Incomplete
    allow_label_resolve: Incomplete
    def __init__(self, selectable: Selectable, equivalents: _EquivalentColumnMap | None = None, adapt_required: bool = False, include_fn: Callable[[ClauseElement], bool] | None = None, exclude_fn: Callable[[ClauseElement], bool] | None = None, adapt_on_names: bool = False, allow_label_resolve: bool = True, anonymize_labels: bool = False, adapt_from_selectables: AbstractSet[FromClause] | None = None) -> None: ...
    class _IncludeExcludeMapping:
        parent: Incomplete
        columns: Incomplete
        def __init__(self, parent, columns) -> None: ...
        def __getitem__(self, key): ...
    def wrap(self, adapter): ...
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: _ET) -> _ET: ...
    def chain(self, visitor: ExternalTraversal) -> ColumnAdapter: ...
    @property
    def visitor_iterator(self) -> Iterator[ColumnAdapter]: ...
    adapt_clause = traverse
    adapt_list: Incomplete
    def adapt_check_present(self, col: ColumnElement[Any]) -> ColumnElement[Any] | None: ...
