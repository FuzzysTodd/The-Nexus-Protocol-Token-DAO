import dataclasses
from ... import types as sqltypes
from ...sql import operators as operators
from ...sql.elements import ColumnElement as ColumnElement
from ...sql.type_api import TypeEngine as TypeEngine, TypeEngineMixin as TypeEngineMixin, _TE
from ...util import py310 as py310
from ...util.typing import Literal as Literal
from .operators import ADJACENT_TO as ADJACENT_TO, CONTAINED_BY as CONTAINED_BY, CONTAINS as CONTAINS, NOT_EXTEND_LEFT_OF as NOT_EXTEND_LEFT_OF, NOT_EXTEND_RIGHT_OF as NOT_EXTEND_RIGHT_OF, OVERLAP as OVERLAP, STRICTLY_LEFT_OF as STRICTLY_LEFT_OF, STRICTLY_RIGHT_OF as STRICTLY_RIGHT_OF
from _typeshed import Incomplete
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Generic, Type, overload

dc_slots: Incomplete
dc_kwonly: Incomplete

@dataclasses.dataclass(frozen=True, **dc_slots)
class Range(Generic[_T]):
    '''Represent a PostgreSQL range.

    E.g.::

        r = Range(10, 50, bounds="()")

    The calling style is similar to that of psycopg and psycopg2, in part
    to allow easier migration from previous SQLAlchemy versions that used
    these objects directly.

    :param lower: Lower bound value, or None
    :param upper: Upper bound value, or None
    :param bounds: keyword-only, optional string value that is one of
     ``"()"``, ``"[)"``, ``"(]"``, ``"[]"``.  Defaults to ``"[)"``.
    :param empty: keyword-only, optional bool indicating this is an "empty"
     range

    .. versionadded:: 2.0

    '''
    lower: _T | None = ...
    upper: _T | None = ...
    bounds: _BoundsType = ...
    empty: bool = ...
    def __init__(self, lower: _T | None = None, upper: _T | None = None, *, bounds: _BoundsType = '[)', empty: bool = False) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def isempty(self) -> bool:
        """A synonym for the 'empty' attribute."""
    @property
    def is_empty(self) -> bool:
        """A synonym for the 'empty' attribute."""
    @property
    def lower_inc(self) -> bool:
        """Return True if the lower bound is inclusive."""
    @property
    def lower_inf(self) -> bool:
        """Return True if this range is non-empty and lower bound is
        infinite."""
    @property
    def upper_inc(self) -> bool:
        """Return True if the upper bound is inclusive."""
    @property
    def upper_inf(self) -> bool:
        """Return True if this range is non-empty and the upper bound is
        infinite."""
    @property
    def __sa_type_engine__(self) -> AbstractRange[Range[_T]]: ...
    def __eq__(self, other: Any) -> bool:
        """Compare this range to the `other` taking into account
        bounds inclusivity, returning ``True`` if they are equal.
        """
    def contained_by(self, other: Range[_T]) -> bool:
        """Determine whether this range is a contained by `other`."""
    def contains(self, value: _T | Range[_T]) -> bool:
        """Determine whether this range contains `value`."""
    def overlaps(self, other: Range[_T]) -> bool:
        """Determine whether this range overlaps with `other`."""
    def strictly_left_of(self, other: Range[_T]) -> bool:
        """Determine whether this range is completely to the left of `other`."""
    __lshift__ = strictly_left_of
    def strictly_right_of(self, other: Range[_T]) -> bool:
        """Determine whether this range is completely to the right of `other`."""
    __rshift__ = strictly_right_of
    def not_extend_left_of(self, other: Range[_T]) -> bool:
        """Determine whether this does not extend to the left of `other`."""
    def not_extend_right_of(self, other: Range[_T]) -> bool:
        """Determine whether this does not extend to the right of `other`."""
    def adjacent_to(self, other: Range[_T]) -> bool:
        """Determine whether this range is adjacent to the `other`."""
    def union(self, other: Range[_T]) -> Range[_T]:
        '''Compute the union of this range with the `other`.

        This raises a ``ValueError`` exception if the two ranges are
        "disjunct", that is neither adjacent nor overlapping.
        '''
    def __add__(self, other: Range[_T]) -> Range[_T]: ...
    def difference(self, other: Range[_T]) -> Range[_T]:
        '''Compute the difference between this range and the `other`.

        This raises a ``ValueError`` exception if the two ranges are
        "disjunct", that is neither adjacent nor overlapping.
        '''
    def __sub__(self, other: Range[_T]) -> Range[_T]: ...
    def intersection(self, other: Range[_T]) -> Range[_T]:
        """Compute the intersection of this range with the `other`.

        .. versionadded:: 2.0.10

        """
    def __mul__(self, other: Range[_T]) -> Range[_T]: ...

class AbstractRange(sqltypes.TypeEngine[Range[_T]]):
    """
    Base for PostgreSQL RANGE types.

    .. seealso::

        `PostgreSQL range functions <https://www.postgresql.org/docs/current/static/functions-range.html>`_

    """
    render_bind_cast: bool
    __abstract__: bool
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    class comparator_factory(TypeEngine.Comparator[Range[Any]]):
        """Define comparison operations for range types."""
        def contains(self, other: Any, **kw: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the right hand operand,
            which can be an element or a range, is contained within the
            column.

            kwargs may be ignored by this operator but are required for API
            conformance.
            """
        def contained_by(self, other: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the column is contained
            within the right hand operand.
            """
        def overlaps(self, other: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the column overlaps
            (has points in common with) the right hand operand.
            """
        def strictly_left_of(self, other: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the column is strictly
            left of the right hand operand.
            """
        __lshift__ = strictly_left_of
        def strictly_right_of(self, other: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the column is strictly
            right of the right hand operand.
            """
        __rshift__ = strictly_right_of
        def not_extend_right_of(self, other: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the range in the column
            does not extend right of the range in the operand.
            """
        def not_extend_left_of(self, other: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the range in the column
            does not extend left of the range in the operand.
            """
        def adjacent_to(self, other: Any) -> ColumnElement[bool]:
            """Boolean expression. Returns true if the range in the column
            is adjacent to the range in the operand.
            """
        def union(self, other: Any) -> ColumnElement[bool]:
            """Range expression. Returns the union of the two ranges.
            Will raise an exception if the resulting range is not
            contiguous.
            """
        def difference(self, other: Any) -> ColumnElement[bool]:
            """Range expression. Returns the union of the two ranges.
            Will raise an exception if the resulting range is not
            contiguous.
            """
        def intersection(self, other: Any) -> ColumnElement[Range[_T]]:
            """Range expression. Returns the intersection of the two ranges.
            Will raise an exception if the resulting range is not
            contiguous.
            """

class AbstractRangeImpl(AbstractRange[Range[_T]]):
    """Marker for AbstractRange that will apply a subclass-specific
    adaptation"""

class AbstractMultiRange(AbstractRange[Range[_T]]):
    """base for PostgreSQL MULTIRANGE types"""
    __abstract__: bool

class AbstractMultiRangeImpl(AbstractRangeImpl[Range[_T]], AbstractMultiRange[Range[_T]]):
    """Marker for AbstractRange that will apply a subclass-specific
    adaptation"""

class INT4RANGE(AbstractRange[Range[int]]):
    """Represent the PostgreSQL INT4RANGE type."""
    __visit_name__: str

class INT8RANGE(AbstractRange[Range[int]]):
    """Represent the PostgreSQL INT8RANGE type."""
    __visit_name__: str

class NUMRANGE(AbstractRange[Range[Decimal]]):
    """Represent the PostgreSQL NUMRANGE type."""
    __visit_name__: str

class DATERANGE(AbstractRange[Range[date]]):
    """Represent the PostgreSQL DATERANGE type."""
    __visit_name__: str

class TSRANGE(AbstractRange[Range[datetime]]):
    """Represent the PostgreSQL TSRANGE type."""
    __visit_name__: str

class TSTZRANGE(AbstractRange[Range[datetime]]):
    """Represent the PostgreSQL TSTZRANGE type."""
    __visit_name__: str

class INT4MULTIRANGE(AbstractMultiRange[Range[int]]):
    """Represent the PostgreSQL INT4MULTIRANGE type."""
    __visit_name__: str

class INT8MULTIRANGE(AbstractMultiRange[Range[int]]):
    """Represent the PostgreSQL INT8MULTIRANGE type."""
    __visit_name__: str

class NUMMULTIRANGE(AbstractMultiRange[Range[Decimal]]):
    """Represent the PostgreSQL NUMMULTIRANGE type."""
    __visit_name__: str

class DATEMULTIRANGE(AbstractMultiRange[Range[date]]):
    """Represent the PostgreSQL DATEMULTIRANGE type."""
    __visit_name__: str

class TSMULTIRANGE(AbstractMultiRange[Range[datetime]]):
    """Represent the PostgreSQL TSRANGE type."""
    __visit_name__: str

class TSTZMULTIRANGE(AbstractMultiRange[Range[datetime]]):
    """Represent the PostgreSQL TSTZRANGE type."""
    __visit_name__: str
