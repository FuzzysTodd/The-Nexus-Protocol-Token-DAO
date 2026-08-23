from .. import exc as exc, util as util
from ..util.typing import Literal as Literal, Protocol as Protocol
from ._typing import ColumnExpressionArgument as ColumnExpressionArgument
from .cache_key import CacheConst as CacheConst
from .elements import ColumnElement as ColumnElement
from .type_api import TypeEngine as TypeEngine
from _typeshed import Incomplete
from enum import IntEnum
from typing import Any, Callable, Generic, Type, overload

class OperatorType(Protocol):
    """describe an op() function."""
    @overload
    def __call__(self, left: ColumnExpressionArgument[Any], right: Any | None = None, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    @overload
    def __call__(self, left: Operators, right: Any | None = None, *other: Any, **kwargs: Any) -> Operators: ...

add: Incomplete
and_: Incomplete
contains: Incomplete
eq: Incomplete
floordiv: Incomplete
ge: Incomplete
getitem: Incomplete
gt: Incomplete
inv: Incomplete
le: Incomplete
lshift: Incomplete
lt: Incomplete
mod: Incomplete
mul: Incomplete
ne: Incomplete
neg: Incomplete
or_: Incomplete
rshift: Incomplete
sub: Incomplete
truediv: Incomplete

class Operators:
    """Base of comparison and logical operators.

    Implements base methods
    :meth:`~sqlalchemy.sql.operators.Operators.operate` and
    :meth:`~sqlalchemy.sql.operators.Operators.reverse_operate`, as well as
    :meth:`~sqlalchemy.sql.operators.Operators.__and__`,
    :meth:`~sqlalchemy.sql.operators.Operators.__or__`,
    :meth:`~sqlalchemy.sql.operators.Operators.__invert__`.

    Usually is used via its most common subclass
    :class:`.ColumnOperators`.

    """
    def __and__(self, other: Any) -> Operators:
        """Implement the ``&`` operator.

        When used with SQL expressions, results in an
        AND operation, equivalent to
        :func:`_expression.and_`, that is::

            a & b

        is equivalent to::

            from sqlalchemy import and_
            and_(a, b)

        Care should be taken when using ``&`` regarding
        operator precedence; the ``&`` operator has the highest precedence.
        The operands should be enclosed in parenthesis if they contain
        further sub expressions::

            (a == 2) & (b == 4)

        """
    def __or__(self, other: Any) -> Operators:
        """Implement the ``|`` operator.

        When used with SQL expressions, results in an
        OR operation, equivalent to
        :func:`_expression.or_`, that is::

            a | b

        is equivalent to::

            from sqlalchemy import or_
            or_(a, b)

        Care should be taken when using ``|`` regarding
        operator precedence; the ``|`` operator has the highest precedence.
        The operands should be enclosed in parenthesis if they contain
        further sub expressions::

            (a == 2) | (b == 4)

        """
    def __invert__(self) -> Operators:
        """Implement the ``~`` operator.

        When used with SQL expressions, results in a
        NOT operation, equivalent to
        :func:`_expression.not_`, that is::

            ~a

        is equivalent to::

            from sqlalchemy import not_
            not_(a)

        """
    def op(self, opstring: str, precedence: int = 0, is_comparison: bool = False, return_type: Type[TypeEngine[Any]] | TypeEngine[Any] | None = None, python_impl: Callable[..., Any] | None = None) -> Callable[[Any], Operators]:
        '''Produce a generic operator function.

        e.g.::

          somecolumn.op("*")(5)

        produces::

          somecolumn * 5

        This function can also be used to make bitwise operators explicit. For
        example::

          somecolumn.op(\'&\')(0xff)

        is a bitwise AND of the value in ``somecolumn``.

        :param opstring: a string which will be output as the infix operator
          between this element and the expression passed to the
          generated function.

        :param precedence: precedence which the database is expected to apply
         to the operator in SQL expressions. This integer value acts as a hint
         for the SQL compiler to know when explicit parenthesis should be
         rendered around a particular operation. A lower number will cause the
         expression to be parenthesized when applied against another operator
         with higher precedence. The default value of ``0`` is lower than all
         operators except for the comma (``,``) and ``AS`` operators. A value
         of 100 will be higher or equal to all operators, and -100 will be
         lower than or equal to all operators.

         .. seealso::

            :ref:`faq_sql_expression_op_parenthesis` - detailed description
            of how the SQLAlchemy SQL compiler renders parenthesis

        :param is_comparison: legacy; if True, the operator will be considered
         as a "comparison" operator, that is which evaluates to a boolean
         true/false value, like ``==``, ``>``, etc.  This flag is provided
         so that ORM relationships can establish that the operator is a
         comparison operator when used in a custom join condition.

         Using the ``is_comparison`` parameter is superseded by using the
         :meth:`.Operators.bool_op` method instead;  this more succinct
         operator sets this parameter automatically, but also provides
         correct :pep:`484` typing support as the returned object will
         express a "boolean" datatype, i.e. ``BinaryExpression[bool]``.

        :param return_type: a :class:`.TypeEngine` class or object that will
          force the return type of an expression produced by this operator
          to be of that type.   By default, operators that specify
          :paramref:`.Operators.op.is_comparison` will resolve to
          :class:`.Boolean`, and those that do not will be of the same
          type as the left-hand operand.

        :param python_impl: an optional Python function that can evaluate
         two Python values in the same way as this operator works when
         run on the database server.  Useful for in-Python SQL expression
         evaluation functions, such as for ORM hybrid attributes, and the
         ORM "evaluator" used to match objects in a session after a multi-row
         update or delete.

         e.g.::

            >>> expr = column(\'x\').op(\'+\', python_impl=lambda a, b: a + b)(\'y\')

         The operator for the above expression will also work for non-SQL
         left and right objects::

            >>> expr.operator(5, 10)
            15

         .. versionadded:: 2.0


        .. seealso::

            :meth:`.Operators.bool_op`

            :ref:`types_operators`

            :ref:`relationship_custom_operator`

        '''
    def bool_op(self, opstring: str, precedence: int = 0, python_impl: Callable[..., Any] | None = None) -> Callable[[Any], Operators]:
        '''Return a custom boolean operator.

        This method is shorthand for calling
        :meth:`.Operators.op` and passing the
        :paramref:`.Operators.op.is_comparison`
        flag with True.    A key advantage to using :meth:`.Operators.bool_op`
        is that when using column constructs, the "boolean" nature of the
        returned expression will be present for :pep:`484` purposes.

        .. seealso::

            :meth:`.Operators.op`

        '''
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> Operators:
        """Operate on an argument.

        This is the lowest level of operation, raises
        :class:`NotImplementedError` by default.

        Overriding this on a subclass can allow common
        behavior to be applied to all operations.
        For example, overriding :class:`.ColumnOperators`
        to apply ``func.lower()`` to the left and right
        side::

            class MyComparator(ColumnOperators):
                def operate(self, op, other, **kwargs):
                    return op(func.lower(self), func.lower(other), **kwargs)

        :param op:  Operator callable.
        :param \\*other: the 'other' side of the operation. Will
         be a single scalar for most operations.
        :param \\**kwargs: modifiers.  These may be passed by special
         operators such as :meth:`ColumnOperators.contains`.


        """
    __sa_operate__ = operate
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> Operators:
        """Reverse operate on an argument.

        Usage is the same as :meth:`operate`.

        """

class custom_op(OperatorType, Generic[_T]):
    '''Represent a \'custom\' operator.

    :class:`.custom_op` is normally instantiated when the
    :meth:`.Operators.op` or :meth:`.Operators.bool_op` methods
    are used to create a custom operator callable.  The class can also be
    used directly when programmatically constructing expressions.   E.g.
    to represent the "factorial" operation::

        from sqlalchemy.sql import UnaryExpression
        from sqlalchemy.sql import operators
        from sqlalchemy import Numeric

        unary = UnaryExpression(table.c.somecolumn,
                modifier=operators.custom_op("!"),
                type_=Numeric)


    .. seealso::

        :meth:`.Operators.op`

        :meth:`.Operators.bool_op`

    '''
    opstring: Incomplete
    precedence: Incomplete
    is_comparison: Incomplete
    natural_self_precedent: Incomplete
    eager_grouping: Incomplete
    return_type: Incomplete
    python_impl: Incomplete
    def __init__(self, opstring: str, precedence: int = 0, is_comparison: bool = False, return_type: Type[TypeEngine[_T]] | TypeEngine[_T] | None = None, natural_self_precedent: bool = False, eager_grouping: bool = False, python_impl: Callable[..., Any] | None = None) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @overload
    def __call__(self, left: ColumnExpressionArgument[Any], right: Any | None = None, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    @overload
    def __call__(self, left: Operators, right: Any | None = None, *other: Any, **kwargs: Any) -> Operators: ...

class ColumnOperators(Operators):
    """Defines boolean, comparison, and other operators for
    :class:`_expression.ColumnElement` expressions.

    By default, all methods call down to
    :meth:`.operate` or :meth:`.reverse_operate`,
    passing in the appropriate operator function from the
    Python builtin ``operator`` module or
    a SQLAlchemy-specific operator function from
    :mod:`sqlalchemy.expression.operators`.   For example
    the ``__eq__`` function::

        def __eq__(self, other):
            return self.operate(operators.eq, other)

    Where ``operators.eq`` is essentially::

        def eq(a, b):
            return a == b

    The core column expression unit :class:`_expression.ColumnElement`
    overrides :meth:`.Operators.operate` and others
    to return further :class:`_expression.ColumnElement` constructs,
    so that the ``==`` operation above is replaced by a clause
    construct.

    .. seealso::

        :ref:`types_operators`

        :attr:`.TypeEngine.comparator_factory`

        :class:`.ColumnOperators`

        :class:`.PropComparator`

    """
    timetuple: Literal[None]
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnOperators: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnOperators: ...
    def __lt__(self, other: Any) -> ColumnOperators:
        """Implement the ``<`` operator.

        In a column context, produces the clause ``a < b``.

        """
    def __le__(self, other: Any) -> ColumnOperators:
        """Implement the ``<=`` operator.

        In a column context, produces the clause ``a <= b``.

        """
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> ColumnOperators:
        """Implement the ``==`` operator.

        In a column context, produces the clause ``a = b``.
        If the target is ``None``, produces ``a IS NULL``.

        """
    def __ne__(self, other: Any) -> ColumnOperators:
        """Implement the ``!=`` operator.

        In a column context, produces the clause ``a != b``.
        If the target is ``None``, produces ``a IS NOT NULL``.

        """
    def is_distinct_from(self, other: Any) -> ColumnOperators:
        '''Implement the ``IS DISTINCT FROM`` operator.

        Renders "a IS DISTINCT FROM b" on most platforms;
        on some such as SQLite may render "a IS NOT b".

        '''
    def is_not_distinct_from(self, other: Any) -> ColumnOperators:
        '''Implement the ``IS NOT DISTINCT FROM`` operator.

        Renders "a IS NOT DISTINCT FROM b" on most platforms;
        on some such as SQLite may render "a IS b".

        .. versionchanged:: 1.4 The ``is_not_distinct_from()`` operator is
           renamed from ``isnot_distinct_from()`` in previous releases.
           The previous name remains available for backwards compatibility.

        '''
    def isnot_distinct_from(self, other: Any) -> ColumnOperators: ...
    def __gt__(self, other: Any) -> ColumnOperators:
        """Implement the ``>`` operator.

        In a column context, produces the clause ``a > b``.

        """
    def __ge__(self, other: Any) -> ColumnOperators:
        """Implement the ``>=`` operator.

        In a column context, produces the clause ``a >= b``.

        """
    def __neg__(self) -> ColumnOperators:
        """Implement the ``-`` operator.

        In a column context, produces the clause ``-a``.

        """
    def __contains__(self, other: Any) -> ColumnOperators: ...
    def __getitem__(self, index: Any) -> ColumnOperators:
        """Implement the [] operator.

        This can be used by some database-specific types
        such as PostgreSQL ARRAY and HSTORE.

        """
    def __lshift__(self, other: Any) -> ColumnOperators:
        """implement the << operator.

        Not used by SQLAlchemy core, this is provided
        for custom operator systems which want to use
        << as an extension point.
        """
    def __rshift__(self, other: Any) -> ColumnOperators:
        """implement the >> operator.

        Not used by SQLAlchemy core, this is provided
        for custom operator systems which want to use
        >> as an extension point.
        """
    def concat(self, other: Any) -> ColumnOperators:
        """Implement the 'concat' operator.

        In a column context, produces the clause ``a || b``,
        or uses the ``concat()`` operator on MySQL.

        """
    def like(self, other: Any, escape: str | None = None) -> ColumnOperators:
        '''Implement the ``like`` operator.

        In a column context, produces the expression::

            a LIKE other

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.like("%foobar%"))

        :param other: expression to be compared
        :param escape: optional escape character, renders the ``ESCAPE``
          keyword, e.g.::

            somecolumn.like("foo/%bar", escape="/")

        .. seealso::

            :meth:`.ColumnOperators.ilike`

        '''
    def ilike(self, other: Any, escape: str | None = None) -> ColumnOperators:
        '''Implement the ``ilike`` operator, e.g. case insensitive LIKE.

        In a column context, produces an expression either of the form::

            lower(a) LIKE lower(other)

        Or on backends that support the ILIKE operator::

            a ILIKE other

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.ilike("%foobar%"))

        :param other: expression to be compared
        :param escape: optional escape character, renders the ``ESCAPE``
          keyword, e.g.::

            somecolumn.ilike("foo/%bar", escape="/")

        .. seealso::

            :meth:`.ColumnOperators.like`

        '''
    def bitwise_xor(self, other: Any) -> ColumnOperators:
        """Produce a bitwise XOR operation, typically via the ``^``
        operator, or ``#`` for PostgreSQL.

        .. versionadded:: 2.0.2

        .. seealso::

            :ref:`operators_bitwise`

        """
    def bitwise_or(self, other: Any) -> ColumnOperators:
        """Produce a bitwise OR operation, typically via the ``|``
        operator.

        .. versionadded:: 2.0.2

        .. seealso::

            :ref:`operators_bitwise`

        """
    def bitwise_and(self, other: Any) -> ColumnOperators:
        """Produce a bitwise AND operation, typically via the ``&``
        operator.

        .. versionadded:: 2.0.2

        .. seealso::

            :ref:`operators_bitwise`

        """
    def bitwise_not(self) -> ColumnOperators:
        """Produce a bitwise NOT operation, typically via the ``~``
        operator.

        .. versionadded:: 2.0.2

        .. seealso::

            :ref:`operators_bitwise`

        """
    def bitwise_lshift(self, other: Any) -> ColumnOperators:
        """Produce a bitwise LSHIFT operation, typically via the ``<<``
        operator.

        .. versionadded:: 2.0.2

        .. seealso::

            :ref:`operators_bitwise`

        """
    def bitwise_rshift(self, other: Any) -> ColumnOperators:
        """Produce a bitwise RSHIFT operation, typically via the ``>>``
        operator.

        .. versionadded:: 2.0.2

        .. seealso::

            :ref:`operators_bitwise`

        """
    def in_(self, other: Any) -> ColumnOperators:
        '''Implement the ``in`` operator.

        In a column context, produces the clause ``column IN <other>``.

        The given parameter ``other`` may be:

        * A list of literal values, e.g.::

            stmt.where(column.in_([1, 2, 3]))

          In this calling form, the list of items is converted to a set of
          bound parameters the same length as the list given::

            WHERE COL IN (?, ?, ?)

        * A list of tuples may be provided if the comparison is against a
          :func:`.tuple_` containing multiple expressions::

            from sqlalchemy import tuple_
            stmt.where(tuple_(col1, col2).in_([(1, 10), (2, 20), (3, 30)]))

        * An empty list, e.g.::

            stmt.where(column.in_([]))

          In this calling form, the expression renders an "empty set"
          expression.  These expressions are tailored to individual backends
          and are generally trying to get an empty SELECT statement as a
          subquery.  Such as on SQLite, the expression is::

            WHERE col IN (SELECT 1 FROM (SELECT 1) WHERE 1!=1)

          .. versionchanged:: 1.4  empty IN expressions now use an
             execution-time generated SELECT subquery in all cases.

        * A bound parameter, e.g. :func:`.bindparam`, may be used if it
          includes the :paramref:`.bindparam.expanding` flag::

            stmt.where(column.in_(bindparam(\'value\', expanding=True)))

          In this calling form, the expression renders a special non-SQL
          placeholder expression that looks like::

            WHERE COL IN ([EXPANDING_value])

          This placeholder expression is intercepted at statement execution
          time to be converted into the variable number of bound parameter
          form illustrated earlier.   If the statement were executed as::

            connection.execute(stmt, {"value": [1, 2, 3]})

          The database would be passed a bound parameter for each value::

            WHERE COL IN (?, ?, ?)

          .. versionadded:: 1.2 added "expanding" bound parameters

          If an empty list is passed, a special "empty list" expression,
          which is specific to the database in use, is rendered.  On
          SQLite this would be::

            WHERE COL IN (SELECT 1 FROM (SELECT 1) WHERE 1!=1)

          .. versionadded:: 1.3 "expanding" bound parameters now support
             empty lists

        * a :func:`_expression.select` construct, which is usually a
          correlated scalar select::

            stmt.where(
                column.in_(
                    select(othertable.c.y).
                    where(table.c.x == othertable.c.x)
                )
            )

          In this calling form, :meth:`.ColumnOperators.in_` renders as given::

            WHERE COL IN (SELECT othertable.y
            FROM othertable WHERE othertable.x = table.x)

        :param other: a list of literals, a :func:`_expression.select`
         construct, or a :func:`.bindparam` construct that includes the
         :paramref:`.bindparam.expanding` flag set to True.

        '''
    def not_in(self, other: Any) -> ColumnOperators:
        '''implement the ``NOT IN`` operator.

        This is equivalent to using negation with
        :meth:`.ColumnOperators.in_`, i.e. ``~x.in_(y)``.

        In the case that ``other`` is an empty sequence, the compiler
        produces an "empty not in" expression.   This defaults to the
        expression "1 = 1" to produce true in all cases.  The
        :paramref:`_sa.create_engine.empty_in_strategy` may be used to
        alter this behavior.

        .. versionchanged:: 1.4 The ``not_in()`` operator is renamed from
           ``notin_()`` in previous releases.  The previous name remains
           available for backwards compatibility.

        .. versionchanged:: 1.2  The :meth:`.ColumnOperators.in_` and
           :meth:`.ColumnOperators.not_in` operators
           now produce a "static" expression for an empty IN sequence
           by default.

        .. seealso::

            :meth:`.ColumnOperators.in_`

        '''
    def notin_(self, other: Any) -> ColumnOperators: ...
    def not_like(self, other: Any, escape: str | None = None) -> ColumnOperators:
        """implement the ``NOT LIKE`` operator.

        This is equivalent to using negation with
        :meth:`.ColumnOperators.like`, i.e. ``~x.like(y)``.

        .. versionchanged:: 1.4 The ``not_like()`` operator is renamed from
           ``notlike()`` in previous releases.  The previous name remains
           available for backwards compatibility.

        .. seealso::

            :meth:`.ColumnOperators.like`

        """
    def notlike(self, other: Any, escape: str | None = None) -> ColumnOperators: ...
    def not_ilike(self, other: Any, escape: str | None = None) -> ColumnOperators:
        """implement the ``NOT ILIKE`` operator.

        This is equivalent to using negation with
        :meth:`.ColumnOperators.ilike`, i.e. ``~x.ilike(y)``.

        .. versionchanged:: 1.4 The ``not_ilike()`` operator is renamed from
           ``notilike()`` in previous releases.  The previous name remains
           available for backwards compatibility.

        .. seealso::

            :meth:`.ColumnOperators.ilike`

        """
    def notilike(self, other: Any, escape: str | None = None) -> ColumnOperators: ...
    def is_(self, other: Any) -> ColumnOperators:
        """Implement the ``IS`` operator.

        Normally, ``IS`` is generated automatically when comparing to a
        value of ``None``, which resolves to ``NULL``.  However, explicit
        usage of ``IS`` may be desirable if comparing to boolean values
        on certain platforms.

        .. seealso:: :meth:`.ColumnOperators.is_not`

        """
    def is_not(self, other: Any) -> ColumnOperators:
        """Implement the ``IS NOT`` operator.

        Normally, ``IS NOT`` is generated automatically when comparing to a
        value of ``None``, which resolves to ``NULL``.  However, explicit
        usage of ``IS NOT`` may be desirable if comparing to boolean values
        on certain platforms.

        .. versionchanged:: 1.4 The ``is_not()`` operator is renamed from
           ``isnot()`` in previous releases.  The previous name remains
           available for backwards compatibility.

        .. seealso:: :meth:`.ColumnOperators.is_`

        """
    def isnot(self, other: Any) -> ColumnOperators: ...
    def startswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnOperators:
        '''Implement the ``startswith`` operator.

        Produces a LIKE expression that tests against a match for the start
        of a string value::

            column LIKE <other> || \'%\'

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.startswith("foobar"))

        Since the operator uses ``LIKE``, wildcard characters
        ``"%"`` and ``"_"`` that are present inside the <other> expression
        will behave like wildcards as well.   For literal string
        values, the :paramref:`.ColumnOperators.startswith.autoescape` flag
        may be set to ``True`` to apply escaping to occurrences of these
        characters within the string value so that they match as themselves
        and not as wildcard characters.  Alternatively, the
        :paramref:`.ColumnOperators.startswith.escape` parameter will establish
        a given character as an escape character which can be of use when
        the target expression is not a literal string.

        :param other: expression to be compared.   This is usually a plain
          string value, but can also be an arbitrary SQL expression.  LIKE
          wildcard characters ``%`` and ``_`` are not escaped by default unless
          the :paramref:`.ColumnOperators.startswith.autoescape` flag is
          set to True.

        :param autoescape: boolean; when True, establishes an escape character
          within the LIKE expression, then applies it to all occurrences of
          ``"%"``, ``"_"`` and the escape character itself within the
          comparison value, which is assumed to be a literal string and not a
          SQL expression.

          An expression such as::

            somecolumn.startswith("foo%bar", autoescape=True)

          Will render as::

            somecolumn LIKE :param || \'%\' ESCAPE \'/\'

          With the value of ``:param`` as ``"foo/%bar"``.

        :param escape: a character which when given will render with the
          ``ESCAPE`` keyword to establish that character as the escape
          character.  This character can then be placed preceding occurrences
          of ``%`` and ``_`` to allow them to act as themselves and not
          wildcard characters.

          An expression such as::

            somecolumn.startswith("foo/%bar", escape="^")

          Will render as::

            somecolumn LIKE :param || \'%\' ESCAPE \'^\'

          The parameter may also be combined with
          :paramref:`.ColumnOperators.startswith.autoescape`::

            somecolumn.startswith("foo%bar^bat", escape="^", autoescape=True)

          Where above, the given literal parameter will be converted to
          ``"foo^%bar^^bat"`` before being passed to the database.

        .. seealso::

            :meth:`.ColumnOperators.endswith`

            :meth:`.ColumnOperators.contains`

            :meth:`.ColumnOperators.like`

        '''
    def istartswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnOperators:
        '''Implement the ``istartswith`` operator, e.g. case insensitive
        version of :meth:`.ColumnOperators.startswith`.

        Produces a LIKE expression that tests against an insensitive
        match for the start of a string value::

            lower(column) LIKE lower(<other>) || \'%\'

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.istartswith("foobar"))

        Since the operator uses ``LIKE``, wildcard characters
        ``"%"`` and ``"_"`` that are present inside the <other> expression
        will behave like wildcards as well.   For literal string
        values, the :paramref:`.ColumnOperators.istartswith.autoescape` flag
        may be set to ``True`` to apply escaping to occurrences of these
        characters within the string value so that they match as themselves
        and not as wildcard characters.  Alternatively, the
        :paramref:`.ColumnOperators.istartswith.escape` parameter will
        establish a given character as an escape character which can be of
        use when the target expression is not a literal string.

        :param other: expression to be compared.   This is usually a plain
          string value, but can also be an arbitrary SQL expression.  LIKE
          wildcard characters ``%`` and ``_`` are not escaped by default unless
          the :paramref:`.ColumnOperators.istartswith.autoescape` flag is
          set to True.

        :param autoescape: boolean; when True, establishes an escape character
          within the LIKE expression, then applies it to all occurrences of
          ``"%"``, ``"_"`` and the escape character itself within the
          comparison value, which is assumed to be a literal string and not a
          SQL expression.

          An expression such as::

            somecolumn.istartswith("foo%bar", autoescape=True)

          Will render as::

            lower(somecolumn) LIKE lower(:param) || \'%\' ESCAPE \'/\'

          With the value of ``:param`` as ``"foo/%bar"``.

        :param escape: a character which when given will render with the
          ``ESCAPE`` keyword to establish that character as the escape
          character.  This character can then be placed preceding occurrences
          of ``%`` and ``_`` to allow them to act as themselves and not
          wildcard characters.

          An expression such as::

            somecolumn.istartswith("foo/%bar", escape="^")

          Will render as::

            lower(somecolumn) LIKE lower(:param) || \'%\' ESCAPE \'^\'

          The parameter may also be combined with
          :paramref:`.ColumnOperators.istartswith.autoescape`::

            somecolumn.istartswith("foo%bar^bat", escape="^", autoescape=True)

          Where above, the given literal parameter will be converted to
          ``"foo^%bar^^bat"`` before being passed to the database.

        .. seealso::

            :meth:`.ColumnOperators.startswith`
        '''
    def endswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnOperators:
        '''Implement the \'endswith\' operator.

        Produces a LIKE expression that tests against a match for the end
        of a string value::

            column LIKE \'%\' || <other>

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.endswith("foobar"))

        Since the operator uses ``LIKE``, wildcard characters
        ``"%"`` and ``"_"`` that are present inside the <other> expression
        will behave like wildcards as well.   For literal string
        values, the :paramref:`.ColumnOperators.endswith.autoescape` flag
        may be set to ``True`` to apply escaping to occurrences of these
        characters within the string value so that they match as themselves
        and not as wildcard characters.  Alternatively, the
        :paramref:`.ColumnOperators.endswith.escape` parameter will establish
        a given character as an escape character which can be of use when
        the target expression is not a literal string.

        :param other: expression to be compared.   This is usually a plain
          string value, but can also be an arbitrary SQL expression.  LIKE
          wildcard characters ``%`` and ``_`` are not escaped by default unless
          the :paramref:`.ColumnOperators.endswith.autoescape` flag is
          set to True.

        :param autoescape: boolean; when True, establishes an escape character
          within the LIKE expression, then applies it to all occurrences of
          ``"%"``, ``"_"`` and the escape character itself within the
          comparison value, which is assumed to be a literal string and not a
          SQL expression.

          An expression such as::

            somecolumn.endswith("foo%bar", autoescape=True)

          Will render as::

            somecolumn LIKE \'%\' || :param ESCAPE \'/\'

          With the value of ``:param`` as ``"foo/%bar"``.

        :param escape: a character which when given will render with the
          ``ESCAPE`` keyword to establish that character as the escape
          character.  This character can then be placed preceding occurrences
          of ``%`` and ``_`` to allow them to act as themselves and not
          wildcard characters.

          An expression such as::

            somecolumn.endswith("foo/%bar", escape="^")

          Will render as::

            somecolumn LIKE \'%\' || :param ESCAPE \'^\'

          The parameter may also be combined with
          :paramref:`.ColumnOperators.endswith.autoescape`::

            somecolumn.endswith("foo%bar^bat", escape="^", autoescape=True)

          Where above, the given literal parameter will be converted to
          ``"foo^%bar^^bat"`` before being passed to the database.

        .. seealso::

            :meth:`.ColumnOperators.startswith`

            :meth:`.ColumnOperators.contains`

            :meth:`.ColumnOperators.like`

        '''
    def iendswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnOperators:
        '''Implement the ``iendswith`` operator, e.g. case insensitive
        version of :meth:`.ColumnOperators.endswith`.

        Produces a LIKE expression that tests against an insensitive match
        for the end of a string value::

            lower(column) LIKE \'%\' || lower(<other>)

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.iendswith("foobar"))

        Since the operator uses ``LIKE``, wildcard characters
        ``"%"`` and ``"_"`` that are present inside the <other> expression
        will behave like wildcards as well.   For literal string
        values, the :paramref:`.ColumnOperators.iendswith.autoescape` flag
        may be set to ``True`` to apply escaping to occurrences of these
        characters within the string value so that they match as themselves
        and not as wildcard characters.  Alternatively, the
        :paramref:`.ColumnOperators.iendswith.escape` parameter will establish
        a given character as an escape character which can be of use when
        the target expression is not a literal string.

        :param other: expression to be compared.   This is usually a plain
          string value, but can also be an arbitrary SQL expression.  LIKE
          wildcard characters ``%`` and ``_`` are not escaped by default unless
          the :paramref:`.ColumnOperators.iendswith.autoescape` flag is
          set to True.

        :param autoescape: boolean; when True, establishes an escape character
          within the LIKE expression, then applies it to all occurrences of
          ``"%"``, ``"_"`` and the escape character itself within the
          comparison value, which is assumed to be a literal string and not a
          SQL expression.

          An expression such as::

            somecolumn.iendswith("foo%bar", autoescape=True)

          Will render as::

            lower(somecolumn) LIKE \'%\' || lower(:param) ESCAPE \'/\'

          With the value of ``:param`` as ``"foo/%bar"``.

        :param escape: a character which when given will render with the
          ``ESCAPE`` keyword to establish that character as the escape
          character.  This character can then be placed preceding occurrences
          of ``%`` and ``_`` to allow them to act as themselves and not
          wildcard characters.

          An expression such as::

            somecolumn.iendswith("foo/%bar", escape="^")

          Will render as::

            lower(somecolumn) LIKE \'%\' || lower(:param) ESCAPE \'^\'

          The parameter may also be combined with
          :paramref:`.ColumnOperators.iendswith.autoescape`::

            somecolumn.endswith("foo%bar^bat", escape="^", autoescape=True)

          Where above, the given literal parameter will be converted to
          ``"foo^%bar^^bat"`` before being passed to the database.

        .. seealso::

            :meth:`.ColumnOperators.endswith`
        '''
    def contains(self, other: Any, **kw: Any) -> ColumnOperators:
        '''Implement the \'contains\' operator.

        Produces a LIKE expression that tests against a match for the middle
        of a string value::

            column LIKE \'%\' || <other> || \'%\'

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.contains("foobar"))

        Since the operator uses ``LIKE``, wildcard characters
        ``"%"`` and ``"_"`` that are present inside the <other> expression
        will behave like wildcards as well.   For literal string
        values, the :paramref:`.ColumnOperators.contains.autoescape` flag
        may be set to ``True`` to apply escaping to occurrences of these
        characters within the string value so that they match as themselves
        and not as wildcard characters.  Alternatively, the
        :paramref:`.ColumnOperators.contains.escape` parameter will establish
        a given character as an escape character which can be of use when
        the target expression is not a literal string.

        :param other: expression to be compared.   This is usually a plain
          string value, but can also be an arbitrary SQL expression.  LIKE
          wildcard characters ``%`` and ``_`` are not escaped by default unless
          the :paramref:`.ColumnOperators.contains.autoescape` flag is
          set to True.

        :param autoescape: boolean; when True, establishes an escape character
          within the LIKE expression, then applies it to all occurrences of
          ``"%"``, ``"_"`` and the escape character itself within the
          comparison value, which is assumed to be a literal string and not a
          SQL expression.

          An expression such as::

            somecolumn.contains("foo%bar", autoescape=True)

          Will render as::

            somecolumn LIKE \'%\' || :param || \'%\' ESCAPE \'/\'

          With the value of ``:param`` as ``"foo/%bar"``.

        :param escape: a character which when given will render with the
          ``ESCAPE`` keyword to establish that character as the escape
          character.  This character can then be placed preceding occurrences
          of ``%`` and ``_`` to allow them to act as themselves and not
          wildcard characters.

          An expression such as::

            somecolumn.contains("foo/%bar", escape="^")

          Will render as::

            somecolumn LIKE \'%\' || :param || \'%\' ESCAPE \'^\'

          The parameter may also be combined with
          :paramref:`.ColumnOperators.contains.autoescape`::

            somecolumn.contains("foo%bar^bat", escape="^", autoescape=True)

          Where above, the given literal parameter will be converted to
          ``"foo^%bar^^bat"`` before being passed to the database.

        .. seealso::

            :meth:`.ColumnOperators.startswith`

            :meth:`.ColumnOperators.endswith`

            :meth:`.ColumnOperators.like`


        '''
    def icontains(self, other: Any, **kw: Any) -> ColumnOperators:
        '''Implement the ``icontains`` operator, e.g. case insensitive
        version of :meth:`.ColumnOperators.contains`.

        Produces a LIKE expression that tests against an insensitive match
        for the middle of a string value::

            lower(column) LIKE \'%\' || lower(<other>) || \'%\'

        E.g.::

            stmt = select(sometable).\\\n                where(sometable.c.column.icontains("foobar"))

        Since the operator uses ``LIKE``, wildcard characters
        ``"%"`` and ``"_"`` that are present inside the <other> expression
        will behave like wildcards as well.   For literal string
        values, the :paramref:`.ColumnOperators.icontains.autoescape` flag
        may be set to ``True`` to apply escaping to occurrences of these
        characters within the string value so that they match as themselves
        and not as wildcard characters.  Alternatively, the
        :paramref:`.ColumnOperators.icontains.escape` parameter will establish
        a given character as an escape character which can be of use when
        the target expression is not a literal string.

        :param other: expression to be compared.   This is usually a plain
          string value, but can also be an arbitrary SQL expression.  LIKE
          wildcard characters ``%`` and ``_`` are not escaped by default unless
          the :paramref:`.ColumnOperators.icontains.autoescape` flag is
          set to True.

        :param autoescape: boolean; when True, establishes an escape character
          within the LIKE expression, then applies it to all occurrences of
          ``"%"``, ``"_"`` and the escape character itself within the
          comparison value, which is assumed to be a literal string and not a
          SQL expression.

          An expression such as::

            somecolumn.icontains("foo%bar", autoescape=True)

          Will render as::

            lower(somecolumn) LIKE \'%\' || lower(:param) || \'%\' ESCAPE \'/\'

          With the value of ``:param`` as ``"foo/%bar"``.

        :param escape: a character which when given will render with the
          ``ESCAPE`` keyword to establish that character as the escape
          character.  This character can then be placed preceding occurrences
          of ``%`` and ``_`` to allow them to act as themselves and not
          wildcard characters.

          An expression such as::

            somecolumn.icontains("foo/%bar", escape="^")

          Will render as::

            lower(somecolumn) LIKE \'%\' || lower(:param) || \'%\' ESCAPE \'^\'

          The parameter may also be combined with
          :paramref:`.ColumnOperators.contains.autoescape`::

            somecolumn.icontains("foo%bar^bat", escape="^", autoescape=True)

          Where above, the given literal parameter will be converted to
          ``"foo^%bar^^bat"`` before being passed to the database.

        .. seealso::

            :meth:`.ColumnOperators.contains`

        '''
    def match(self, other: Any, **kwargs: Any) -> ColumnOperators:
        '''Implements a database-specific \'match\' operator.

        :meth:`_sql.ColumnOperators.match` attempts to resolve to
        a MATCH-like function or operator provided by the backend.
        Examples include:

        * PostgreSQL - renders ``x @@ plainto_tsquery(y)``

            .. versionchanged:: 2.0  ``plainto_tsquery()`` is used instead
               of ``to_tsquery()`` for PostgreSQL now; for compatibility with
               other forms, see :ref:`postgresql_match`.


        * MySQL - renders ``MATCH (x) AGAINST (y IN BOOLEAN MODE)``

          .. seealso::

                :class:`_mysql.match` - MySQL specific construct with
                additional features.

        * Oracle - renders ``CONTAINS(x, y)``
        * other backends may provide special implementations.
        * Backends without any special implementation will emit
          the operator as "MATCH".  This is compatible with SQLite, for
          example.

        '''
    def regexp_match(self, pattern: Any, flags: str | None = None) -> ColumnOperators:
        '''Implements a database-specific \'regexp match\' operator.

        E.g.::

            stmt = select(table.c.some_column).where(
                table.c.some_column.regexp_match(\'^(b|c)\')
            )

        :meth:`_sql.ColumnOperators.regexp_match` attempts to resolve to
        a REGEXP-like function or operator provided by the backend, however
        the specific regular expression syntax and flags available are
        **not backend agnostic**.

        Examples include:

        * PostgreSQL - renders ``x ~ y`` or ``x !~ y`` when negated.
        * Oracle - renders ``REGEXP_LIKE(x, y)``
        * SQLite - uses SQLite\'s ``REGEXP`` placeholder operator and calls into
          the Python ``re.match()`` builtin.
        * other backends may provide special implementations.
        * Backends without any special implementation will emit
          the operator as "REGEXP" or "NOT REGEXP".  This is compatible with
          SQLite and MySQL, for example.

        Regular expression support is currently implemented for Oracle,
        PostgreSQL, MySQL and MariaDB.  Partial support is available for
        SQLite.  Support among third-party dialects may vary.

        :param pattern: The regular expression pattern string or column
          clause.
        :param flags: Any regular expression string flags to apply, passed as
          plain Python string only.  These flags are backend specific.
          Some backends, like PostgreSQL and MariaDB, may alternatively
          specify the flags as part of the pattern.
          When using the ignore case flag \'i\' in PostgreSQL, the ignore case
          regexp match operator ``~*`` or ``!~*`` will be used.

        .. versionadded:: 1.4

        .. versionchanged:: 1.4.48, 2.0.18  Note that due to an implementation
           error, the "flags" parameter previously accepted SQL expression
           objects such as column expressions in addition to plain Python
           strings.   This implementation did not work correctly with caching
           and was removed; strings only should be passed for the "flags"
           parameter, as these flags are rendered as literal inline values
           within SQL expressions.

        .. seealso::

            :meth:`_sql.ColumnOperators.regexp_replace`


        '''
    def regexp_replace(self, pattern: Any, replacement: Any, flags: str | None = None) -> ColumnOperators:
        '''Implements a database-specific \'regexp replace\' operator.

        E.g.::

            stmt = select(
                table.c.some_column.regexp_replace(
                    \'b(..)\',
                    \'X\x01Y\',
                    flags=\'g\'
                )
            )

        :meth:`_sql.ColumnOperators.regexp_replace` attempts to resolve to
        a REGEXP_REPLACE-like function provided by the backend, that
        usually emit the function ``REGEXP_REPLACE()``.  However,
        the specific regular expression syntax and flags available are
        **not backend agnostic**.

        Regular expression replacement support is currently implemented for
        Oracle, PostgreSQL, MySQL 8 or greater and MariaDB.  Support among
        third-party dialects may vary.

        :param pattern: The regular expression pattern string or column
          clause.
        :param pattern: The replacement string or column clause.
        :param flags: Any regular expression string flags to apply, passed as
          plain Python string only.  These flags are backend specific.
          Some backends, like PostgreSQL and MariaDB, may alternatively
          specify the flags as part of the pattern.

        .. versionadded:: 1.4

        .. versionchanged:: 1.4.48, 2.0.18  Note that due to an implementation
           error, the "flags" parameter previously accepted SQL expression
           objects such as column expressions in addition to plain Python
           strings.   This implementation did not work correctly with caching
           and was removed; strings only should be passed for the "flags"
           parameter, as these flags are rendered as literal inline values
           within SQL expressions.


        .. seealso::

            :meth:`_sql.ColumnOperators.regexp_match`

        '''
    def desc(self) -> ColumnOperators:
        """Produce a :func:`_expression.desc` clause against the
        parent object."""
    def asc(self) -> ColumnOperators:
        """Produce a :func:`_expression.asc` clause against the
        parent object."""
    def nulls_first(self) -> ColumnOperators:
        """Produce a :func:`_expression.nulls_first` clause against the
        parent object.

        .. versionchanged:: 1.4 The ``nulls_first()`` operator is
           renamed from ``nullsfirst()`` in previous releases.
           The previous name remains available for backwards compatibility.
        """
    def nullsfirst(self) -> ColumnOperators: ...
    def nulls_last(self) -> ColumnOperators:
        """Produce a :func:`_expression.nulls_last` clause against the
        parent object.

        .. versionchanged:: 1.4 The ``nulls_last()`` operator is
           renamed from ``nullslast()`` in previous releases.
           The previous name remains available for backwards compatibility.
        """
    def nullslast(self) -> ColumnOperators: ...
    def collate(self, collation: str) -> ColumnOperators:
        """Produce a :func:`_expression.collate` clause against
        the parent object, given the collation string.

        .. seealso::

            :func:`_expression.collate`

        """
    def __radd__(self, other: Any) -> ColumnOperators:
        """Implement the ``+`` operator in reverse.

        See :meth:`.ColumnOperators.__add__`.

        """
    def __rsub__(self, other: Any) -> ColumnOperators:
        """Implement the ``-`` operator in reverse.

        See :meth:`.ColumnOperators.__sub__`.

        """
    def __rmul__(self, other: Any) -> ColumnOperators:
        """Implement the ``*`` operator in reverse.

        See :meth:`.ColumnOperators.__mul__`.

        """
    def __rmod__(self, other: Any) -> ColumnOperators:
        """Implement the ``%`` operator in reverse.

        See :meth:`.ColumnOperators.__mod__`.

        """
    def between(self, cleft: Any, cright: Any, symmetric: bool = False) -> ColumnOperators:
        """Produce a :func:`_expression.between` clause against
        the parent object, given the lower and upper range.

        """
    def distinct(self) -> ColumnOperators:
        """Produce a :func:`_expression.distinct` clause against the
        parent object.

        """
    def any_(self) -> ColumnOperators:
        """Produce an :func:`_expression.any_` clause against the
        parent object.

        See the documentation for :func:`_sql.any_` for examples.

        .. note:: be sure to not confuse the newer
            :meth:`_sql.ColumnOperators.any_` method with its older
            :class:`_types.ARRAY`-specific counterpart, the
            :meth:`_types.ARRAY.Comparator.any` method, which a different
            calling syntax and usage pattern.

        """
    def all_(self) -> ColumnOperators:
        """Produce an :func:`_expression.all_` clause against the
        parent object.

        See the documentation for :func:`_sql.all_` for examples.

        .. note:: be sure to not confuse the newer
            :meth:`_sql.ColumnOperators.all_` method with its older
            :class:`_types.ARRAY`-specific counterpart, the
            :meth:`_types.ARRAY.Comparator.all` method, which a different
            calling syntax and usage pattern.

        """
    def __add__(self, other: Any) -> ColumnOperators:
        """Implement the ``+`` operator.

        In a column context, produces the clause ``a + b``
        if the parent object has non-string affinity.
        If the parent object has a string affinity,
        produces the concatenation operator, ``a || b`` -
        see :meth:`.ColumnOperators.concat`.

        """
    def __sub__(self, other: Any) -> ColumnOperators:
        """Implement the ``-`` operator.

        In a column context, produces the clause ``a - b``.

        """
    def __mul__(self, other: Any) -> ColumnOperators:
        """Implement the ``*`` operator.

        In a column context, produces the clause ``a * b``.

        """
    def __mod__(self, other: Any) -> ColumnOperators:
        """Implement the ``%`` operator.

        In a column context, produces the clause ``a % b``.

        """
    def __truediv__(self, other: Any) -> ColumnOperators:
        """Implement the ``/`` operator.

        In a column context, produces the clause ``a / b``, and
        considers the result type to be numeric.

        .. versionchanged:: 2.0  The truediv operator against two integers
           is now considered to return a numeric value.    Behavior on specific
           backends may vary.

        """
    def __rtruediv__(self, other: Any) -> ColumnOperators:
        """Implement the ``/`` operator in reverse.

        See :meth:`.ColumnOperators.__truediv__`.

        """
    def __floordiv__(self, other: Any) -> ColumnOperators:
        '''Implement the ``//`` operator.

        In a column context, produces the clause ``a / b``,
        which is the same as "truediv", but considers the result
        type to be integer.

        .. versionadded:: 2.0

        '''
    def __rfloordiv__(self, other: Any) -> ColumnOperators:
        """Implement the ``//`` operator in reverse.

        See :meth:`.ColumnOperators.__floordiv__`.

        """

def commutative_op(fn: _FN) -> _FN: ...
def comparison_op(fn: _FN) -> _FN: ...
def from_() -> Any: ...
def function_as_comparison_op() -> Any: ...
def as_() -> Any: ...
def exists() -> Any: ...
def is_true(a: Any) -> Any: ...
def istrue(a: Any) -> Any: ...
def is_false(a: Any) -> Any: ...
def isfalse(a: Any) -> Any: ...
def is_distinct_from(a: Any, b: Any) -> Any: ...
def is_not_distinct_from(a: Any, b: Any) -> Any: ...
def isnot_distinct_from(a: Any, b: Any) -> Any: ...
def is_(a: Any, b: Any) -> Any: ...
def is_not(a: Any, b: Any) -> Any: ...
def isnot(a: Any, b: Any) -> Any: ...
def collate(a: Any, b: Any) -> Any: ...
def op(a: Any, opstring: str, b: Any) -> Any: ...
def like_op(a: Any, b: Any, escape: str | None = None) -> Any: ...
def not_like_op(a: Any, b: Any, escape: str | None = None) -> Any: ...
def notlike_op(a: Any, b: Any, escape: str | None = None) -> Any: ...
def ilike_op(a: Any, b: Any, escape: str | None = None) -> Any: ...
def not_ilike_op(a: Any, b: Any, escape: str | None = None) -> Any: ...
def notilike_op(a: Any, b: Any, escape: str | None = None) -> Any: ...
def between_op(a: Any, b: Any, c: Any, symmetric: bool = False) -> Any: ...
def not_between_op(a: Any, b: Any, c: Any, symmetric: bool = False) -> Any: ...
def notbetween_op(a: Any, b: Any, c: Any, symmetric: bool = False) -> Any: ...
def in_op(a: Any, b: Any) -> Any: ...
def not_in_op(a: Any, b: Any) -> Any: ...
def notin_op(a: Any, b: Any) -> Any: ...
def distinct_op(a: Any) -> Any: ...
def any_op(a: Any) -> Any: ...
def all_op(a: Any) -> Any: ...
def startswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def not_startswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def notstartswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def istartswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def not_istartswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def endswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def not_endswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def notendswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def iendswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def not_iendswith_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def contains_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def not_contains_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def notcontains_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def icontains_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def not_icontains_op(a: Any, b: Any, escape: str | None = None, autoescape: bool = False) -> Any: ...
def match_op(a: Any, b: Any, **kw: Any) -> Any: ...
def regexp_match_op(a: Any, b: Any, flags: str | None = None) -> Any: ...
def not_regexp_match_op(a: Any, b: Any, flags: str | None = None) -> Any: ...
def regexp_replace_op(a: Any, b: Any, replacement: Any, flags: str | None = None) -> Any: ...
def not_match_op(a: Any, b: Any, **kw: Any) -> Any: ...
def notmatch_op(a: Any, b: Any, **kw: Any) -> Any: ...
def comma_op(a: Any, b: Any) -> Any: ...
def filter_op(a: Any, b: Any) -> Any: ...
def concat_op(a: Any, b: Any) -> Any: ...
def desc_op(a: Any) -> Any: ...
def asc_op(a: Any) -> Any: ...
def nulls_first_op(a: Any) -> Any: ...
def nullsfirst_op(a: Any) -> Any: ...
def nulls_last_op(a: Any) -> Any: ...
def nullslast_op(a: Any) -> Any: ...
def json_getitem_op(a: Any, b: Any) -> Any: ...
def json_path_getitem_op(a: Any, b: Any) -> Any: ...
def bitwise_xor_op(a: Any, b: Any) -> Any: ...
def bitwise_or_op(a: Any, b: Any) -> Any: ...
def bitwise_and_op(a: Any, b: Any) -> Any: ...
def bitwise_not_op(a: Any) -> Any: ...
def bitwise_lshift_op(a: Any, b: Any) -> Any: ...
def bitwise_rshift_op(a: Any, b: Any) -> Any: ...
def is_comparison(op: OperatorType) -> bool: ...
def is_commutative(op: OperatorType) -> bool: ...
def is_ordering_modifier(op: OperatorType) -> bool: ...
def is_natural_self_precedent(op: OperatorType) -> bool: ...
def is_boolean(op: OperatorType) -> bool: ...
def mirror(op: OperatorType) -> OperatorType:
    """rotate a comparison operator 180 degrees.

    Note this is not the same as negation.

    """
def is_associative(op: OperatorType) -> bool: ...

class _OpLimit(IntEnum): ...

def is_precedent(operator: OperatorType, against: OperatorType) -> bool: ...
