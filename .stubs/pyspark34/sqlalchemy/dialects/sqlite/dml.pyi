from ...sql._typing import _DMLTableArgument
from ...sql.base import ReadOnlyColumnCollection
from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement, KeyedColumnElement
from ...util.typing import Self
from .._typing import _OnConflictIndexElementsT, _OnConflictIndexWhereT, _OnConflictSetT, _OnConflictWhereT
from _typeshed import Incomplete
from typing import Any

__all__ = ['Insert', 'insert']

def insert(table: _DMLTableArgument) -> Insert:
    """Construct a sqlite-specific variant :class:`_sqlite.Insert`
    construct.

    .. container:: inherited_member

        The :func:`sqlalchemy.dialects.sqlite.insert` function creates
        a :class:`sqlalchemy.dialects.sqlite.Insert`.  This class is based
        on the dialect-agnostic :class:`_sql.Insert` construct which may
        be constructed using the :func:`_sql.insert` function in
        SQLAlchemy Core.

    The :class:`_sqlite.Insert` construct includes additional methods
    :meth:`_sqlite.Insert.on_conflict_do_update`,
    :meth:`_sqlite.Insert.on_conflict_do_nothing`.

    """

class Insert(StandardInsert):
    """SQLite-specific implementation of INSERT.

    Adds methods for SQLite-specific syntaxes such as ON CONFLICT.

    The :class:`_sqlite.Insert` object is created using the
    :func:`sqlalchemy.dialects.sqlite.insert` function.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`sqlite_on_conflict_insert`

    """
    stringify_dialect: str
    inherit_cache: bool
    def excluded(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]:
        '''Provide the ``excluded`` namespace for an ON CONFLICT statement

        SQLite\'s ON CONFLICT clause allows reference to the row that would
        be inserted, known as ``excluded``.  This attribute provides
        all columns in this row to be referenceable.

        .. tip::  The :attr:`_sqlite.Insert.excluded` attribute is an instance
            of :class:`_expression.ColumnCollection`, which provides an
            interface the same as that of the :attr:`_schema.Table.c`
            collection described at :ref:`metadata_tables_and_columns`.
            With this collection, ordinary names are accessible like attributes
            (e.g. ``stmt.excluded.some_column``), but special names and
            dictionary method names should be accessed using indexed access,
            such as ``stmt.excluded["column name"]`` or
            ``stmt.excluded["values"]``.  See the docstring for
            :class:`_expression.ColumnCollection` for further examples.

        '''
    def on_conflict_do_update(self, index_elements: _OnConflictIndexElementsT = None, index_where: _OnConflictIndexWhereT = None, set_: _OnConflictSetT = None, where: _OnConflictWhereT = None) -> Self:
        """
        Specifies a DO UPDATE SET action for ON CONFLICT clause.

        :param index_elements:
         A sequence consisting of string column names, :class:`_schema.Column`
         objects, or other column expression objects that will be used
         to infer a target index or unique constraint.

        :param index_where:
         Additional WHERE criterion that can be used to infer a
         conditional target index.

        :param set\\_:
         A dictionary or other mapping object
         where the keys are either names of columns in the target table,
         or :class:`_schema.Column` objects or other ORM-mapped columns
         matching that of the target table, and expressions or literals
         as values, specifying the ``SET`` actions to take.

         .. versionadded:: 1.4 The
            :paramref:`_sqlite.Insert.on_conflict_do_update.set_`
            parameter supports :class:`_schema.Column` objects from the target
            :class:`_schema.Table` as keys.

         .. warning:: This dictionary does **not** take into account
            Python-specified default UPDATE values or generation functions,
            e.g. those specified using :paramref:`_schema.Column.onupdate`.
            These values will not be exercised for an ON CONFLICT style of
            UPDATE, unless they are manually specified in the
            :paramref:`.Insert.on_conflict_do_update.set_` dictionary.

        :param where:
         Optional argument. If present, can be a literal SQL
         string or an acceptable expression for a ``WHERE`` clause
         that restricts the rows affected by ``DO UPDATE SET``. Rows
         not meeting the ``WHERE`` condition will not be updated
         (effectively a ``DO NOTHING`` for those rows).

        """
    def on_conflict_do_nothing(self, index_elements: _OnConflictIndexElementsT = None, index_where: _OnConflictIndexWhereT = None) -> Self:
        """
        Specifies a DO NOTHING action for ON CONFLICT clause.

        :param index_elements:
         A sequence consisting of string column names, :class:`_schema.Column`
         objects, or other column expression objects that will be used
         to infer a target index or unique constraint.

        :param index_where:
         Additional WHERE criterion that can be used to infer a
         conditional target index.

        """

class OnConflictClause(ClauseElement):
    stringify_dialect: str
    constraint_target: None
    inferred_target_elements: _OnConflictIndexElementsT
    inferred_target_whereclause: _OnConflictIndexWhereT
    def __init__(self, index_elements: _OnConflictIndexElementsT = None, index_where: _OnConflictIndexWhereT = None) -> None: ...

class OnConflictDoNothing(OnConflictClause):
    __visit_name__: str

class OnConflictDoUpdate(OnConflictClause):
    __visit_name__: str
    update_values_to_set: Incomplete
    update_whereclause: Incomplete
    def __init__(self, index_elements: _OnConflictIndexElementsT = None, index_where: _OnConflictIndexWhereT = None, set_: _OnConflictSetT = None, where: _OnConflictWhereT = None) -> None: ...
