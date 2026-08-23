from . import types as types
from ...sql import coercions as coercions, elements as elements, expression as expression, functions as functions, roles as roles, schema as schema
from ...sql.schema import ColumnCollectionConstraint as ColumnCollectionConstraint
from ...sql.sqltypes import TEXT as TEXT
from ...sql.visitors import InternalTraversal as InternalTraversal
from .array import ARRAY as ARRAY
from _typeshed import Incomplete

class aggregate_order_by(expression.ColumnElement):
    '''Represent a PostgreSQL aggregate order by expression.

    E.g.::

        from sqlalchemy.dialects.postgresql import aggregate_order_by
        expr = func.array_agg(aggregate_order_by(table.c.a, table.c.b.desc()))
        stmt = select(expr)

    would represent the expression::

        SELECT array_agg(a ORDER BY b DESC) FROM table;

    Similarly::

        expr = func.string_agg(
            table.c.a,
            aggregate_order_by(literal_column("\',\'"), table.c.a)
        )
        stmt = select(expr)

    Would represent::

        SELECT string_agg(a, \',\' ORDER BY a) FROM table;

    .. versionchanged:: 1.2.13 - the ORDER BY argument may be multiple terms

    .. seealso::

        :class:`_functions.array_agg`

    '''
    __visit_name__: str
    stringify_dialect: str
    target: Incomplete
    type: Incomplete
    order_by: Incomplete
    def __init__(self, target, *order_by) -> None: ...
    def self_group(self, against: Incomplete | None = None): ...
    def get_children(self, **kwargs): ...

class ExcludeConstraint(ColumnCollectionConstraint):
    """A table-level EXCLUDE constraint.

    Defines an EXCLUDE constraint as described in the `PostgreSQL
    documentation`__.

    __ https://www.postgresql.org/docs/current/static/sql-createtable.html#SQL-CREATETABLE-EXCLUDE

    """
    __visit_name__: str
    where: Incomplete
    inherit_cache: bool
    create_drop_stringify_dialect: str
    operators: Incomplete
    using: Incomplete
    ops: Incomplete
    def __init__(self, *elements, **kw) -> None:
        '''
        Create an :class:`.ExcludeConstraint` object.

        E.g.::

            const = ExcludeConstraint(
                (Column(\'period\'), \'&&\'),
                (Column(\'group\'), \'=\'),
                where=(Column(\'group\') != \'some group\'),
                ops={\'group\': \'my_operator_class\'}
            )

        The constraint is normally embedded into the :class:`_schema.Table`
        construct
        directly, or added later using :meth:`.append_constraint`::

            some_table = Table(
                \'some_table\', metadata,
                Column(\'id\', Integer, primary_key=True),
                Column(\'period\', TSRANGE()),
                Column(\'group\', String)
            )

            some_table.append_constraint(
                ExcludeConstraint(
                    (some_table.c.period, \'&&\'),
                    (some_table.c.group, \'=\'),
                    where=some_table.c.group != \'some group\',
                    name=\'some_table_excl_const\',
                    ops={\'group\': \'my_operator_class\'}
                )
            )

        The exclude constraint defined in this example requires the
        ``btree_gist`` extension, that can be created using the
        command ``CREATE EXTENSION btree_gist;``.

        :param \\*elements:

          A sequence of two tuples of the form ``(column, operator)`` where
          "column" is either a :class:`_schema.Column` object, or a SQL
          expression element (e.g. ``func.int8range(table.from, table.to)``)
          or the name of a column as string, and "operator" is a string
          containing the operator to use (e.g. `"&&"` or `"="`).

          In order to specify a column name when a :class:`_schema.Column`
          object is not available, while ensuring
          that any necessary quoting rules take effect, an ad-hoc
          :class:`_schema.Column` or :func:`_expression.column`
          object should be used.
          The ``column`` may also be a string SQL expression when
          passed as :func:`_expression.literal_column` or
          :func:`_expression.text`

        :param name:
          Optional, the in-database name of this constraint.

        :param deferrable:
          Optional bool.  If set, emit DEFERRABLE or NOT DEFERRABLE when
          issuing DDL for this constraint.

        :param initially:
          Optional string.  If set, emit INITIALLY <value> when issuing DDL
          for this constraint.

        :param using:
          Optional string.  If set, emit USING <index_method> when issuing DDL
          for this constraint. Defaults to \'gist\'.

        :param where:
          Optional SQL expression construct or literal SQL string.
          If set, emit WHERE <predicate> when issuing DDL
          for this constraint.

        :param ops:
          Optional dictionary.  Used to define operator classes for the
          elements; works the same way as that of the
          :ref:`postgresql_ops <postgresql_operator_classes>`
          parameter specified to the :class:`_schema.Index` construct.

          .. versionadded:: 1.3.21

          .. seealso::

            :ref:`postgresql_operator_classes` - general description of how
            PostgreSQL operator classes are specified.

        '''

def array_agg(*arg, **kw):
    """PostgreSQL-specific form of :class:`_functions.array_agg`, ensures
    return type is :class:`_postgresql.ARRAY` and not
    the plain :class:`_types.ARRAY`, unless an explicit ``type_``
    is passed.

    """

class _regconfig_fn(functions.GenericFunction[_T]):
    inherit_cache: bool
    def __init__(self, *args, **kwargs) -> None: ...

class to_tsvector(_regconfig_fn):
    '''The PostgreSQL ``to_tsvector`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSVECTOR`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.to_tsvector` will be used automatically when invoking
    ``sqlalchemy.func.to_tsvector()``, ensuring the correct argument and return
    type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache: bool
    type = types.TSVECTOR

class to_tsquery(_regconfig_fn):
    '''The PostgreSQL ``to_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.to_tsquery` will be used automatically when invoking
    ``sqlalchemy.func.to_tsquery()``, ensuring the correct argument and return
    type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache: bool
    type = types.TSQUERY

class plainto_tsquery(_regconfig_fn):
    '''The PostgreSQL ``plainto_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.plainto_tsquery` will be used automatically when
    invoking ``sqlalchemy.func.plainto_tsquery()``, ensuring the correct
    argument and return type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache: bool
    type = types.TSQUERY

class phraseto_tsquery(_regconfig_fn):
    '''The PostgreSQL ``phraseto_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.phraseto_tsquery` will be used automatically when
    invoking ``sqlalchemy.func.phraseto_tsquery()``, ensuring the correct
    argument and return type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache: bool
    type = types.TSQUERY

class websearch_to_tsquery(_regconfig_fn):
    '''The PostgreSQL ``websearch_to_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.websearch_to_tsquery` will be used automatically when
    invoking ``sqlalchemy.func.websearch_to_tsquery()``, ensuring the correct
    argument and return type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache: bool
    type = types.TSQUERY

class ts_headline(_regconfig_fn):
    '''The PostgreSQL ``ts_headline`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_types.TEXT`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.ts_headline` will be used automatically when invoking
    ``sqlalchemy.func.ts_headline()``, ensuring the correct argument and return
    type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache: bool
    type = TEXT
    def __init__(self, *args, **kwargs) -> None: ...
