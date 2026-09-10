from _typeshed import Incomplete
from pypika.enums import Dialects as Dialects, JoinType as JoinType, ReferenceOption as ReferenceOption, SetOperation as SetOperation
from pypika.terms import ArithmeticExpression as ArithmeticExpression, Criterion as Criterion, EmptyCriterion as EmptyCriterion, Field as Field, Function as Function, Index as Index, Node as Node, PeriodCriterion as PeriodCriterion, Rollup as Rollup, Star as Star, Term as Term, Tuple as Tuple, ValueWrapper as ValueWrapper
from pypika.utils import JoinException as JoinException, QueryException as QueryException, RollupException as RollupException, SetOperationException as SetOperationException, builder as builder, format_alias_sql as format_alias_sql, format_quotes as format_quotes, ignore_copy as ignore_copy
from typing import Any, List, Sequence, Tuple as TypedTuple, Type

class Selectable(Node):
    alias: Incomplete
    def __init__(self, alias: str) -> None: ...
    def as_(self, alias: str) -> Selectable: ...
    def field(self, name: str) -> Field: ...
    @property
    def star(self) -> Star: ...
    def __getattr__(self, name: str) -> Field: ...
    def __getitem__(self, name: str) -> Field: ...
    def get_table_name(self) -> str: ...

class AliasedQuery(Selectable):
    name: Incomplete
    query: Incomplete
    def __init__(self, name: str, query: Selectable | None = None) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def __eq__(self, other: AliasedQuery) -> bool: ...
    def __hash__(self) -> int: ...

class Schema:
    def __init__(self, name: str, parent: Schema | None = None) -> None: ...
    def __eq__(self, other: Schema) -> bool: ...
    def __ne__(self, other: Schema) -> bool: ...
    def __getattr__(self, item: str) -> Table: ...
    def get_sql(self, quote_char: str | None = None, **kwargs: Any) -> str: ...

class Database(Schema):
    def __getattr__(self, item: str) -> Schema: ...

class Table(Selectable):
    def __init__(self, name: str, schema: Schema | str | None = None, alias: str | None = None, query_cls: Type['Query'] | None = None) -> None: ...
    def get_table_name(self) -> str: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def for_(self, temporal_criterion: Criterion) -> Table: ...
    def for_portion(self, period_criterion: PeriodCriterion) -> Table: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def select(self, *terms: Sequence[int | float | str | bool | Term | Field]) -> QueryBuilder:
        """
        Perform a SELECT operation on the current table

        :param terms:
            Type:  list[expression]

            A list of terms to select. These can be any type of int, float, str, bool or Term or a Field.

        :return:  QueryBuilder
        """
    def update(self) -> QueryBuilder:
        """
        Perform an UPDATE operation on the current table

        :return: QueryBuilder
        """
    def insert(self, *terms: int | float | str | bool | Term | Field) -> QueryBuilder:
        """
        Perform an INSERT operation on the current table

        :param terms:
            Type: list[expression]

            A list of terms to select. These can be any type of int, float, str, bool or  any other valid data

        :return: QueryBuilder
        """

def make_tables(*names: TypedTuple[str, str] | str, **kwargs: Any) -> List[Table]:
    """
    Shortcut to create many tables. If `names` param is a tuple, the first
    position will refer to the `_table_name` while the second will be its `alias`.
    Any other data structure will be treated as a whole as the `_table_name`.
    """

class Column:
    """Represents a column."""
    name: Incomplete
    type: Incomplete
    nullable: Incomplete
    default: Incomplete
    def __init__(self, column_name: str, column_type: str | None = None, nullable: bool | None = None, default: Any | Term | None = None) -> None: ...
    def get_name_sql(self, **kwargs: Any) -> str: ...
    def get_sql(self, **kwargs: Any) -> str: ...

def make_columns(*names: TypedTuple[str, str] | str) -> List[Column]:
    """
    Shortcut to create many columns. If `names` param is a tuple, the first
    position will refer to the `name` while the second will be its `type`.
    Any other data structure will be treated as a whole as the `name`.
    """

class PeriodFor:
    name: Incomplete
    start_column: Incomplete
    end_column: Incomplete
    def __init__(self, name: str, start_column: str | Column, end_column: str | Column) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class Query:
    """
    Query is the primary class and entry point in pypika. It is used to build queries iteratively using the builder
    design
    pattern.

    This class is immutable.
    """
    @classmethod
    def from_(cls, table: Selectable | str, **kwargs: Any) -> QueryBuilder:
        """
        Query builder entry point.  Initializes query building and sets the table to select from.  When using this
        function, the query becomes a SELECT query.

        :param table:
            Type: Table or str

            An instance of a Table object or a string table name.

        :returns QueryBuilder
        """
    @classmethod
    def create_table(cls, table: str | Table) -> CreateQueryBuilder:
        """
        Query builder entry point. Initializes query building and sets the table name to be created. When using this
        function, the query becomes a CREATE statement.

        :param table: An instance of a Table object or a string table name.

        :return: CreateQueryBuilder
        """
    @classmethod
    def drop_database(cls, database: Database | Table) -> DropQueryBuilder:
        """
        Query builder entry point. Initializes query building and sets the table name to be dropped. When using this
        function, the query becomes a DROP statement.

        :param database: An instance of a Database object or a string database name.

        :return: DropQueryBuilder
        """
    @classmethod
    def drop_table(cls, table: str | Table) -> DropQueryBuilder:
        """
        Query builder entry point. Initializes query building and sets the table name to be dropped. When using this
        function, the query becomes a DROP statement.

        :param table: An instance of a Table object or a string table name.

        :return: DropQueryBuilder
        """
    @classmethod
    def drop_user(cls, user: str) -> DropQueryBuilder:
        """
        Query builder entry point. Initializes query building and sets the table name to be dropped. When using this
        function, the query becomes a DROP statement.

        :param user: String user name.

        :return: DropQueryBuilder
        """
    @classmethod
    def drop_view(cls, view: str) -> DropQueryBuilder:
        """
        Query builder entry point. Initializes query building and sets the table name to be dropped. When using this
        function, the query becomes a DROP statement.

        :param view: String view name.

        :return: DropQueryBuilder
        """
    @classmethod
    def into(cls, table: Table | str, **kwargs: Any) -> QueryBuilder:
        """
        Query builder entry point.  Initializes query building and sets the table to insert into.  When using this
        function, the query becomes an INSERT query.

        :param table:
            Type: Table or str

            An instance of a Table object or a string table name.

        :returns QueryBuilder
        """
    @classmethod
    def with_(cls, table: str | Selectable, name: str, **kwargs: Any) -> QueryBuilder: ...
    @classmethod
    def select(cls, *terms: int | float | str | bool | Term, **kwargs: Any) -> QueryBuilder:
        """
        Query builder entry point.  Initializes query building without a table and selects fields.  Useful when testing
        SQL functions.

        :param terms:
            Type: list[expression]

            A list of terms to select.  These can be any type of int, float, str, bool, or Term.  They cannot be a Field
            unless the function ``Query.from_`` is called first.

        :returns QueryBuilder
        """
    @classmethod
    def update(cls, table: str | Table, **kwargs) -> QueryBuilder:
        """
        Query builder entry point.  Initializes query building and sets the table to update.  When using this
        function, the query becomes an UPDATE query.

        :param table:
            Type: Table or str

            An instance of a Table object or a string table name.

        :returns QueryBuilder
        """
    @classmethod
    def Table(cls, table_name: str, **kwargs) -> _TableClass:
        """
        Convenience method for creating a Table that uses this Query class.

        :param table_name:
            Type: str

            A string table name.

        :returns Table
        """
    @classmethod
    def Tables(cls, *names: TypedTuple[str, str] | str, **kwargs: Any) -> List[_TableClass]:
        """
        Convenience method for creating many tables that uses this Query class.
        See ``Query.make_tables`` for details.

        :param names:
            Type: list[str or tuple]

            A list of string table names, or name and alias tuples.

        :returns Table
        """

class _SetOperation(Selectable, Term):
    """
    A Query class wrapper for a all set operations, Union DISTINCT or ALL, Intersect, Except or Minus

    Created via the functions `Query.union`,`Query.union_all`,`Query.intersect`, `Query.except_of`,`Query.minus`.

    This class should not be instantiated directly.
    """
    base_query: Incomplete
    def __init__(self, base_query: QueryBuilder, set_operation_query: QueryBuilder, set_operation: SetOperation, alias: str | None = None, wrapper_cls: Type[ValueWrapper] = ...) -> None: ...
    def orderby(self, *fields: Field, **kwargs: Any) -> _SetOperation: ...
    def limit(self, limit: int) -> _SetOperation: ...
    def offset(self, offset: int) -> _SetOperation: ...
    def union(self, other: Selectable) -> _SetOperation: ...
    def union_all(self, other: Selectable) -> _SetOperation: ...
    def intersect(self, other: Selectable) -> _SetOperation: ...
    def except_of(self, other: Selectable) -> _SetOperation: ...
    def minus(self, other: Selectable) -> _SetOperation: ...
    def __add__(self, other: Selectable) -> _SetOperation: ...
    def __mul__(self, other: Selectable) -> _SetOperation: ...
    def __sub__(self, other: QueryBuilder) -> _SetOperation: ...
    def get_sql(self, with_alias: bool = False, subquery: bool = False, **kwargs: Any) -> str: ...

class QueryBuilder(Selectable, Term):
    """
    Query Builder is the main class in pypika which stores the state of a query and offers functions which allow the
    state to be branched immutably.
    """
    QUOTE_CHAR: str
    SECONDARY_QUOTE_CHAR: str
    ALIAS_QUOTE_CHAR: Incomplete
    QUERY_ALIAS_QUOTE_CHAR: Incomplete
    QUERY_CLS = Query
    dialect: Incomplete
    as_keyword: Incomplete
    wrap_set_operation_queries: Incomplete
    immutable: Incomplete
    def __init__(self, dialect: Dialects | None = None, wrap_set_operation_queries: bool = True, wrapper_cls: Type[ValueWrapper] = ..., immutable: bool = True, as_keyword: bool = False) -> None: ...
    def __copy__(self) -> QueryBuilder: ...
    def from_(self, selectable: Selectable | Query | str) -> QueryBuilder:
        """
        Adds a table to the query. This function can only be called once and will raise an AttributeError if called a
        second time.

        :param selectable:
            Type: ``Table``, ``Query``, or ``str``

            When a ``str`` is passed, a table with the name matching the ``str`` value is used.

        :returns
            A copy of the query with the table added.
        """
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> QueryBuilder:
        """
        Replaces all occurrences of the specified table with the new table. Useful when reusing fields across
        queries.

        :param current_table:
            The table instance to be replaces.
        :param new_table:
            The table instance to replace with.
        :return:
            A copy of the query with the tables replaced.
        """
    def with_(self, selectable: Selectable, name: str) -> QueryBuilder: ...
    def into(self, table: str | Table) -> QueryBuilder: ...
    def select(self, *terms: Any) -> QueryBuilder: ...
    def delete(self) -> QueryBuilder: ...
    def update(self, table: str | Table) -> QueryBuilder: ...
    def columns(self, *terms: Any) -> QueryBuilder: ...
    def insert(self, *terms: Any) -> QueryBuilder: ...
    def replace(self, *terms: Any) -> QueryBuilder: ...
    def force_index(self, term: str | Index, *terms: str | Index) -> QueryBuilder: ...
    def use_index(self, term: str | Index, *terms: str | Index) -> QueryBuilder: ...
    def distinct(self) -> QueryBuilder: ...
    def for_update(self) -> QueryBuilder: ...
    def ignore(self) -> QueryBuilder: ...
    def prewhere(self, criterion: Criterion) -> QueryBuilder: ...
    def where(self, criterion: Term | EmptyCriterion) -> QueryBuilder: ...
    def having(self, criterion: Term | EmptyCriterion) -> QueryBuilder: ...
    def groupby(self, *terms: str | int | Term) -> QueryBuilder: ...
    def with_totals(self) -> QueryBuilder: ...
    def rollup(self, *terms: list | tuple | set | Term, **kwargs: Any) -> QueryBuilder: ...
    def orderby(self, *fields: Any, **kwargs: Any) -> QueryBuilder: ...
    def join(self, item: Table | QueryBuilder | AliasedQuery | Selectable, how: JoinType = ...) -> Joiner: ...
    def inner_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def left_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def left_outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def right_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def right_outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def full_outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def cross_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def hash_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def limit(self, limit: int) -> QueryBuilder: ...
    def offset(self, offset: int) -> QueryBuilder: ...
    def union(self, other: QueryBuilder) -> _SetOperation: ...
    def union_all(self, other: QueryBuilder) -> _SetOperation: ...
    def intersect(self, other: QueryBuilder) -> _SetOperation: ...
    def except_of(self, other: QueryBuilder) -> _SetOperation: ...
    def minus(self, other: QueryBuilder) -> _SetOperation: ...
    def set(self, field: Field | str, value: Any) -> QueryBuilder: ...
    def __add__(self, other: QueryBuilder) -> _SetOperation: ...
    def __mul__(self, other: QueryBuilder) -> _SetOperation: ...
    def __sub__(self, other: QueryBuilder) -> _SetOperation: ...
    def slice(self, slice: slice) -> QueryBuilder: ...
    def __getitem__(self, item: Any) -> QueryBuilder | Field: ...
    def fields_(self) -> List[Field]: ...
    def do_join(self, join: Join) -> None: ...
    def is_joined(self, table: Table) -> bool: ...
    def __eq__(self, other: QueryBuilder) -> bool: ...
    def __ne__(self, other: QueryBuilder) -> bool: ...
    def __hash__(self) -> int: ...
    def get_sql(self, with_alias: bool = False, subquery: bool = False, **kwargs: Any) -> str: ...

class Joiner:
    query: Incomplete
    item: Incomplete
    how: Incomplete
    type_label: Incomplete
    def __init__(self, query: QueryBuilder, item: Table | QueryBuilder | AliasedQuery, how: JoinType, type_label: str) -> None: ...
    def on(self, criterion: Criterion | None, collate: str | None = None) -> QueryBuilder: ...
    def on_field(self, *fields: Any) -> QueryBuilder: ...
    def using(self, *fields: Any) -> QueryBuilder: ...
    def cross(self) -> QueryBuilder:
        """Return cross join"""

class Join:
    item: Incomplete
    how: Incomplete
    def __init__(self, item: Term, how: JoinType) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def validate(self, _from: Sequence[Table], _joins: Sequence[Table]) -> None: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Join:
        """
        Replaces all occurrences of the specified table with the new table. Useful when reusing
        fields across queries.

        :param current_table:
            The table to be replaced.
        :param new_table:
            The table to replace with.
        :return:
            A copy of the join with the tables replaced.
        """

class JoinOn(Join):
    criterion: Incomplete
    collate: Incomplete
    def __init__(self, item: Term, how: JoinType, criteria: QueryBuilder, collate: str | None = None) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def validate(self, _from: Sequence[Table], _joins: Sequence[Table]) -> None: ...
    item: Incomplete
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> JoinOn:
        """
        Replaces all occurrences of the specified table with the new table. Useful when reusing
        fields across queries.

        :param current_table:
            The table to be replaced.
        :param new_table:
            The table to replace with.
        :return:
            A copy of the join with the tables replaced.
        """

class JoinUsing(Join):
    fields: Incomplete
    def __init__(self, item: Term, how: JoinType, fields: Sequence[Field]) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def validate(self, _from: Sequence[Table], _joins: Sequence[Table]) -> None: ...
    item: Incomplete
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> JoinUsing:
        """
        Replaces all occurrences of the specified table with the new table. Useful when reusing
        fields across queries.

        :param current_table:
            The table to be replaced.
        :param new_table:
            The table to replace with.
        :return:
            A copy of the join with the tables replaced.
        """

class CreateQueryBuilder:
    """
    Query builder used to build CREATE queries.
    """
    QUOTE_CHAR: str
    SECONDARY_QUOTE_CHAR: str
    ALIAS_QUOTE_CHAR: Incomplete
    QUERY_CLS = Query
    dialect: Incomplete
    def __init__(self, dialect: Dialects | None = None) -> None: ...
    def create_table(self, table: Table | str) -> CreateQueryBuilder:
        """
        Creates the table.

        :param table:
            An instance of a Table object or a string table name.

        :raises AttributeError:
            If the table is already created.

        :return:
            CreateQueryBuilder.
        """
    def temporary(self) -> CreateQueryBuilder:
        """
        Makes the table temporary.

        :return:
            CreateQueryBuilder.
        """
    def unlogged(self) -> CreateQueryBuilder:
        """
        Makes the table unlogged.

        :return:
            CreateQueryBuilder.
        """
    def with_system_versioning(self) -> CreateQueryBuilder:
        """
        Adds system versioning.

        :return:
            CreateQueryBuilder.
        """
    def columns(self, *columns: str | TypedTuple[str, str] | Column) -> CreateQueryBuilder:
        """
        Adds the columns.

        :param columns:
            Type:  Union[str, TypedTuple[str, str], Column]

            A list of columns.

        :raises AttributeError:
            If the table is an as_select table.

        :return:
            CreateQueryBuilder.
        """
    def period_for(self, name, start_column: str | Column, end_column: str | Column) -> CreateQueryBuilder:
        """
        Adds a PERIOD FOR clause.

        :param name:
            The period name.

        :param start_column:
            The column that starts the period.

        :param end_column:
            The column that ends the period.

        :return:
            CreateQueryBuilder.
        """
    def unique(self, *columns: str | Column) -> CreateQueryBuilder:
        """
        Adds a UNIQUE constraint.

        :param columns:
            Type:  Union[str, Column]

            A list of columns.

        :return:
            CreateQueryBuilder.
        """
    def primary_key(self, *columns: str | Column) -> CreateQueryBuilder:
        """
        Adds a primary key constraint.

        :param columns:
            Type:  Union[str, Column]

            A list of columns.

        :raises AttributeError:
            If the primary key is already defined.

        :return:
            CreateQueryBuilder.
        """
    def foreign_key(self, columns: List[str | Column], reference_table: str | Table, reference_columns: List[str | Column], on_delete: ReferenceOption = None, on_update: ReferenceOption = None) -> CreateQueryBuilder:
        """
        Adds a foreign key constraint.

        :param columns:
            Type:  List[Union[str, Column]]

            A list of foreign key columns.

        :param reference_table:
            Type: Union[str, Table]

            The parent table name.

        :param reference_columns:
            Type: List[Union[str, Column]]

            Parent key columns.

        :param on_delete:
            Type: ReferenceOption

            Delete action.

        :param on_update:
            Type: ReferenceOption

            Update option.

        :raises AttributeError:
            If the foreign key is already defined.

        :return:
            CreateQueryBuilder.
        """
    def as_select(self, query_builder: QueryBuilder) -> CreateQueryBuilder:
        """
        Creates the table from a select statement.

        :param query_builder:
            The query.

        :raises AttributeError:
            If columns have been defined for the table.

        :return:
            CreateQueryBuilder.
        """
    def if_not_exists(self) -> CreateQueryBuilder: ...
    def get_sql(self, **kwargs: Any) -> str:
        """
        Gets the sql statement string.

        :return: The create table statement.
        :rtype: str
        """

class DropQueryBuilder:
    """
    Query builder used to build DROP queries.
    """
    QUOTE_CHAR: str
    SECONDARY_QUOTE_CHAR: str
    ALIAS_QUOTE_CHAR: Incomplete
    QUERY_CLS = Query
    dialect: Incomplete
    def __init__(self, dialect: Dialects | None = None) -> None: ...
    def drop_database(self, database: Database | str) -> DropQueryBuilder: ...
    def drop_table(self, table: Table | str) -> DropQueryBuilder: ...
    def drop_user(self, user: str) -> DropQueryBuilder: ...
    def drop_view(self, view: str) -> DropQueryBuilder: ...
    def if_exists(self) -> DropQueryBuilder: ...
    def get_sql(self, **kwargs: Any) -> str: ...
