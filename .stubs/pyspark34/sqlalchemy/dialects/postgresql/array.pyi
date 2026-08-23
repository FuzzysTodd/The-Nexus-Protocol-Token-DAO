from ... import types as sqltypes, util as util
from ...sql import expression as expression, operators as operators
from ...sql._typing import _TypeEngineArgument
from .operators import CONTAINED_BY as CONTAINED_BY, CONTAINS as CONTAINS, OVERLAP as OVERLAP
from _typeshed import Incomplete
from typing import Any

def All(other, arrexpr, operator=...):
    """A synonym for the ARRAY-level :meth:`.ARRAY.Comparator.all` method.
    See that method for details.

    """

class array(expression.ExpressionClauseList[_T]):
    '''A PostgreSQL ARRAY literal.

    This is used to produce ARRAY literals in SQL expressions, e.g.::

        from sqlalchemy.dialects.postgresql import array
        from sqlalchemy.dialects import postgresql
        from sqlalchemy import select, func

        stmt = select(array([1,2]) + array([3,4,5]))

        print(stmt.compile(dialect=postgresql.dialect()))

    Produces the SQL::

        SELECT ARRAY[%(param_1)s, %(param_2)s] ||
            ARRAY[%(param_3)s, %(param_4)s, %(param_5)s]) AS anon_1

    An instance of :class:`.array` will always have the datatype
    :class:`_types.ARRAY`.  The "inner" type of the array is inferred from
    the values present, unless the ``type_`` keyword argument is passed::

        array([\'foo\', \'bar\'], type_=CHAR)

    Multidimensional arrays are produced by nesting :class:`.array` constructs.
    The dimensionality of the final :class:`_types.ARRAY`
    type is calculated by
    recursively adding the dimensions of the inner :class:`_types.ARRAY`
    type::

        stmt = select(
            array([
                array([1, 2]), array([3, 4]), array([column(\'q\'), column(\'x\')])
            ])
        )
        print(stmt.compile(dialect=postgresql.dialect()))

    Produces::

        SELECT ARRAY[ARRAY[%(param_1)s, %(param_2)s],
        ARRAY[%(param_3)s, %(param_4)s], ARRAY[q, x]] AS anon_1

    .. versionadded:: 1.3.6 added support for multidimensional array literals

    .. seealso::

        :class:`_postgresql.ARRAY`

    '''
    __visit_name__: str
    stringify_dialect: str
    inherit_cache: bool
    type: Incomplete
    def __init__(self, clauses, **kw) -> None: ...
    def self_group(self, against: Incomplete | None = None): ...

class ARRAY(sqltypes.ARRAY):
    '''PostgreSQL ARRAY type.

    The :class:`_postgresql.ARRAY` type is constructed in the same way
    as the core :class:`_types.ARRAY` type; a member type is required, and a
    number of dimensions is recommended if the type is to be used for more
    than one dimension::

        from sqlalchemy.dialects import postgresql

        mytable = Table("mytable", metadata,
                Column("data", postgresql.ARRAY(Integer, dimensions=2))
            )

    The :class:`_postgresql.ARRAY` type provides all operations defined on the
    core :class:`_types.ARRAY` type, including support for "dimensions",
    indexed access, and simple matching such as
    :meth:`.types.ARRAY.Comparator.any` and
    :meth:`.types.ARRAY.Comparator.all`.  :class:`_postgresql.ARRAY`
    class also
    provides PostgreSQL-specific methods for containment operations, including
    :meth:`.postgresql.ARRAY.Comparator.contains`
    :meth:`.postgresql.ARRAY.Comparator.contained_by`, and
    :meth:`.postgresql.ARRAY.Comparator.overlap`, e.g.::

        mytable.c.data.contains([1, 2])

    The :class:`_postgresql.ARRAY` type may not be supported on all
    PostgreSQL DBAPIs; it is currently known to work on psycopg2 only.

    Additionally, the :class:`_postgresql.ARRAY`
    type does not work directly in
    conjunction with the :class:`.ENUM` type.  For a workaround, see the
    special type at :ref:`postgresql_array_of_enum`.

    .. container:: topic

        **Detecting Changes in ARRAY columns when using the ORM**

        The :class:`_postgresql.ARRAY` type, when used with the SQLAlchemy ORM,
        does not detect in-place mutations to the array. In order to detect
        these, the :mod:`sqlalchemy.ext.mutable` extension must be used, using
        the :class:`.MutableList` class::

            from sqlalchemy.dialects.postgresql import ARRAY
            from sqlalchemy.ext.mutable import MutableList

            class SomeOrmClass(Base):
                # ...

                data = Column(MutableList.as_mutable(ARRAY(Integer)))

        This extension will allow "in-place" changes such to the array
        such as ``.append()`` to produce events which will be detected by the
        unit of work.  Note that changes to elements **inside** the array,
        including subarrays that are mutated in place, are **not** detected.

        Alternatively, assigning a new array value to an ORM element that
        replaces the old one will always trigger a change event.

    .. seealso::

        :class:`_types.ARRAY` - base array type

        :class:`_postgresql.array` - produces a literal array value.

    '''
    class Comparator(sqltypes.ARRAY.Comparator):
        """Define comparison operations for :class:`_types.ARRAY`.

        Note that these operations are in addition to those provided
        by the base :class:`.types.ARRAY.Comparator` class, including
        :meth:`.types.ARRAY.Comparator.any` and
        :meth:`.types.ARRAY.Comparator.all`.

        """
        def contains(self, other, **kwargs):
            """Boolean expression.  Test if elements are a superset of the
            elements of the argument array expression.

            kwargs may be ignored by this operator but are required for API
            conformance.
            """
        def contained_by(self, other):
            """Boolean expression.  Test if elements are a proper subset of the
            elements of the argument array expression.
            """
        def overlap(self, other):
            """Boolean expression.  Test if array has elements in common with
            an argument array expression.
            """
    comparator_factory = Comparator
    item_type: Incomplete
    as_tuple: Incomplete
    dimensions: Incomplete
    zero_indexes: Incomplete
    def __init__(self, item_type: _TypeEngineArgument[Any], as_tuple: bool = False, dimensions: int | None = None, zero_indexes: bool = False) -> None:
        '''Construct an ARRAY.

        E.g.::

          Column(\'myarray\', ARRAY(Integer))

        Arguments are:

        :param item_type: The data type of items of this array. Note that
          dimensionality is irrelevant here, so multi-dimensional arrays like
          ``INTEGER[][]``, are constructed as ``ARRAY(Integer)``, not as
          ``ARRAY(ARRAY(Integer))`` or such.

        :param as_tuple=False: Specify whether return results
          should be converted to tuples from lists. DBAPIs such
          as psycopg2 return lists by default. When tuples are
          returned, the results are hashable.

        :param dimensions: if non-None, the ARRAY will assume a fixed
         number of dimensions.  This will cause the DDL emitted for this
         ARRAY to include the exact number of bracket clauses ``[]``,
         and will also optimize the performance of the type overall.
         Note that PG arrays are always implicitly "non-dimensioned",
         meaning they can store any number of dimensions no matter how
         they were declared.

        :param zero_indexes=False: when True, index values will be converted
         between Python zero-based and PostgreSQL one-based indexes, e.g.
         a value of one will be added to all index values before passing
         to the database.

        '''
    @property
    def hashable(self): ...
    @property
    def python_type(self): ...
    def compare_values(self, x, y): ...
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
