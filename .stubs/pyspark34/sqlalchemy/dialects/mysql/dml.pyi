from ...sql._typing import _DMLTableArgument
from ...sql.base import ReadOnlyColumnCollection
from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement, KeyedColumnElement
from ...sql.selectable import NamedFromClause
from ...util.typing import Self
from _typeshed import Incomplete
from typing import Any

__all__ = ['Insert', 'insert']

def insert(table: _DMLTableArgument) -> Insert:
    """Construct a MySQL/MariaDB-specific variant :class:`_mysql.Insert`
    construct.

    .. container:: inherited_member

        The :func:`sqlalchemy.dialects.mysql.insert` function creates
        a :class:`sqlalchemy.dialects.mysql.Insert`.  This class is based
        on the dialect-agnostic :class:`_sql.Insert` construct which may
        be constructed using the :func:`_sql.insert` function in
        SQLAlchemy Core.

    The :class:`_mysql.Insert` construct includes additional methods
    :meth:`_mysql.Insert.on_duplicate_key_update`.

    """

class Insert(StandardInsert):
    """MySQL-specific implementation of INSERT.

    Adds methods for MySQL-specific syntaxes such as ON DUPLICATE KEY UPDATE.

    The :class:`~.mysql.Insert` object is created using the
    :func:`sqlalchemy.dialects.mysql.insert` function.

    .. versionadded:: 1.2

    """
    stringify_dialect: str
    inherit_cache: bool
    @property
    def inserted(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]:
        '''Provide the "inserted" namespace for an ON DUPLICATE KEY UPDATE
        statement

        MySQL\'s ON DUPLICATE KEY UPDATE clause allows reference to the row
        that would be inserted, via a special function called ``VALUES()``.
        This attribute provides all columns in this row to be referenceable
        such that they will render within a ``VALUES()`` function inside the
        ON DUPLICATE KEY UPDATE clause.    The attribute is named ``.inserted``
        so as not to conflict with the existing
        :meth:`_expression.Insert.values` method.

        .. tip::  The :attr:`_mysql.Insert.inserted` attribute is an instance
            of :class:`_expression.ColumnCollection`, which provides an
            interface the same as that of the :attr:`_schema.Table.c`
            collection described at :ref:`metadata_tables_and_columns`.
            With this collection, ordinary names are accessible like attributes
            (e.g. ``stmt.inserted.some_column``), but special names and
            dictionary method names should be accessed using indexed access,
            such as ``stmt.inserted["column name"]`` or
            ``stmt.inserted["values"]``.  See the docstring for
            :class:`_expression.ColumnCollection` for further examples.

        .. seealso::

            :ref:`mysql_insert_on_duplicate_key_update` - example of how
            to use :attr:`_expression.Insert.inserted`

        '''
    def inserted_alias(self) -> NamedFromClause: ...
    def on_duplicate_key_update(self, *args: _UpdateArg, **kw: Any) -> Self:
        '''
        Specifies the ON DUPLICATE KEY UPDATE clause.

        :param \\**kw:  Column keys linked to UPDATE values.  The
         values may be any SQL expression or supported literal Python
         values.

        .. warning:: This dictionary does **not** take into account
           Python-specified default UPDATE values or generation functions,
           e.g. those specified using :paramref:`_schema.Column.onupdate`.
           These values will not be exercised for an ON DUPLICATE KEY UPDATE
           style of UPDATE, unless values are manually specified here.

        :param \\*args: As an alternative to passing key/value parameters,
         a dictionary or list of 2-tuples can be passed as a single positional
         argument.

         Passing a single dictionary is equivalent to the keyword argument
         form::

            insert().on_duplicate_key_update({"name": "some name"})

         Passing a list of 2-tuples indicates that the parameter assignments
         in the UPDATE clause should be ordered as sent, in a manner similar
         to that described for the :class:`_expression.Update`
         construct overall
         in :ref:`tutorial_parameter_ordered_updates`::

            insert().on_duplicate_key_update(
                [("name", "some name"), ("value", "some value")])

         .. versionchanged:: 1.3 parameters can be specified as a dictionary
            or list of 2-tuples; the latter form provides for parameter
            ordering.


        .. versionadded:: 1.2

        .. seealso::

            :ref:`mysql_insert_on_duplicate_key_update`

        '''

class OnDuplicateClause(ClauseElement):
    __visit_name__: str
    stringify_dialect: str
    inserted_alias: Incomplete
    update: Incomplete
    def __init__(self, inserted_alias: NamedFromClause, update: _UpdateArg) -> None: ...
