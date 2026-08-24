from ... import exc as exc, util as util
from ...sql import coercions as coercions, elements as elements, operators as operators, roles as roles
from ...sql.base import Generative as Generative
from ...util.typing import Self as Self
from _typeshed import Incomplete

class match(Generative, elements.BinaryExpression):
    '''Produce a ``MATCH (X, Y) AGAINST (\'TEXT\')`` clause.

    E.g.::

        from sqlalchemy import desc
        from sqlalchemy.dialects.mysql import match

        match_expr = match(
            users_table.c.firstname,
            users_table.c.lastname,
            against="Firstname Lastname",
        )

        stmt = (
            select(users_table)
            .where(match_expr.in_boolean_mode())
            .order_by(desc(match_expr))
        )

    Would produce SQL resembling::

        SELECT id, firstname, lastname
        FROM user
        WHERE MATCH(firstname, lastname) AGAINST (:param_1 IN BOOLEAN MODE)
        ORDER BY MATCH(firstname, lastname) AGAINST (:param_2) DESC

    The :func:`_mysql.match` function is a standalone version of the
    :meth:`_sql.ColumnElement.match` method available on all
    SQL expressions, as when :meth:`_expression.ColumnElement.match` is
    used, but allows to pass multiple columns

    :param cols: column expressions to match against

    :param against: expression to be compared towards

    :param in_boolean_mode: boolean, set "boolean mode" to true

    :param in_natural_language_mode: boolean , set "natural language" to true

    :param with_query_expansion: boolean, set "query expansion" to true

    .. versionadded:: 1.4.19

    .. seealso::

        :meth:`_expression.ColumnElement.match`

    '''
    __visit_name__: str
    inherit_cache: bool
    def __init__(self, *cols, **kw) -> None: ...
    modifiers: Incomplete
    def in_boolean_mode(self) -> Self:
        '''Apply the "IN BOOLEAN MODE" modifier to the MATCH expression.

        :return: a new :class:`_mysql.match` instance with modifications
         applied.
        '''
    def in_natural_language_mode(self) -> Self:
        '''Apply the "IN NATURAL LANGUAGE MODE" modifier to the MATCH
        expression.

        :return: a new :class:`_mysql.match` instance with modifications
         applied.
        '''
    def with_query_expansion(self) -> Self:
        '''Apply the "WITH QUERY EXPANSION" modifier to the MATCH expression.

        :return: a new :class:`_mysql.match` instance with modifications
         applied.
        '''
