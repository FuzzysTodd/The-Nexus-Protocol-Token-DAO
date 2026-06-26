import datetime as dt
from ...sql import sqltypes as sqltypes, type_api as type_api
from ...sql.operators import OperatorType as OperatorType
from ...sql.type_api import TypeEngine as TypeEngine
from ...util.typing import Literal as Literal
from _typeshed import Incomplete
from typing import Any, Type, overload

class PGUuid(sqltypes.UUID[sqltypes._UUID_RETURN]):
    render_bind_cast: bool
    render_literal_cast: bool
    @overload
    def __init__(self, as_uuid: Literal[True] = ...) -> None: ...
    @overload
    def __init__(self, as_uuid: Literal[False] = ...) -> None: ...

class BYTEA(sqltypes.LargeBinary):
    __visit_name__: str

class INET(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGInet = INET

class CIDR(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGCidr = CIDR

class MACADDR(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGMacAddr = MACADDR

class MACADDR8(sqltypes.TypeEngine[str]):
    __visit_name__: str
PGMacAddr8 = MACADDR8

class MONEY(sqltypes.TypeEngine[str]):
    '''Provide the PostgreSQL MONEY type.

    Depending on driver, result rows using this type may return a
    string value which includes currency symbols.

    For this reason, it may be preferable to provide conversion to a
    numerically-based currency datatype using :class:`_types.TypeDecorator`::

        import re
        import decimal
        from sqlalchemy import Dialect
        from sqlalchemy import TypeDecorator

        class NumericMoney(TypeDecorator):
            impl = MONEY

            def process_result_value(
                self, value: Any, dialect: Dialect
            ) -> None:
                if value is not None:
                    # adjust this for the currency and numeric
                    m = re.match(r"\\$([\\d.]+)", value)
                    if m:
                        value = decimal.Decimal(m.group(1))
                return value

    Alternatively, the conversion may be applied as a CAST using
    the :meth:`_types.TypeDecorator.column_expression` method as follows::

        import decimal
        from sqlalchemy import cast
        from sqlalchemy import TypeDecorator

        class NumericMoney(TypeDecorator):
            impl = MONEY

            def column_expression(self, column: Any):
                return cast(column, Numeric())

    .. versionadded:: 1.2

    '''
    __visit_name__: str

class OID(sqltypes.TypeEngine[int]):
    """Provide the PostgreSQL OID type."""
    __visit_name__: str

class REGCONFIG(sqltypes.TypeEngine[str]):
    """Provide the PostgreSQL REGCONFIG type.

    .. versionadded:: 2.0.0rc1

    """
    __visit_name__: str

class TSQUERY(sqltypes.TypeEngine[str]):
    """Provide the PostgreSQL TSQUERY type.

    .. versionadded:: 2.0.0rc1

    """
    __visit_name__: str

class REGCLASS(sqltypes.TypeEngine[str]):
    """Provide the PostgreSQL REGCLASS type.

    .. versionadded:: 1.2.7

    """
    __visit_name__: str

class TIMESTAMP(sqltypes.TIMESTAMP):
    """Provide the PostgreSQL TIMESTAMP type."""
    __visit_name__: str
    precision: Incomplete
    def __init__(self, timezone: bool = False, precision: int | None = None) -> None:
        """Construct a TIMESTAMP.

        :param timezone: boolean value if timezone present, default False
        :param precision: optional integer precision value

         .. versionadded:: 1.4

        """

class TIME(sqltypes.TIME):
    """PostgreSQL TIME type."""
    __visit_name__: str
    precision: Incomplete
    def __init__(self, timezone: bool = False, precision: int | None = None) -> None:
        """Construct a TIME.

        :param timezone: boolean value if timezone present, default False
        :param precision: optional integer precision value

         .. versionadded:: 1.4

        """

class INTERVAL(type_api.NativeForEmulated, sqltypes._AbstractInterval):
    """PostgreSQL INTERVAL type."""
    __visit_name__: str
    native: bool
    precision: Incomplete
    fields: Incomplete
    def __init__(self, precision: int | None = None, fields: str | None = None) -> None:
        '''Construct an INTERVAL.

        :param precision: optional integer precision value
        :param fields: string fields specifier.  allows storage of fields
         to be limited, such as ``"YEAR"``, ``"MONTH"``, ``"DAY TO HOUR"``,
         etc.

         .. versionadded:: 1.2

        '''
    @classmethod
    def adapt_emulated_to_native(cls, interval: sqltypes.Interval, **kw: Any) -> INTERVAL: ...
    def as_generic(self, allow_nulltype: bool = False) -> sqltypes.Interval: ...
    @property
    def python_type(self) -> Type[dt.timedelta]: ...
PGInterval = INTERVAL

class BIT(sqltypes.TypeEngine[int]):
    __visit_name__: str
    length: Incomplete
    varying: Incomplete
    def __init__(self, length: int | None = None, varying: bool = False) -> None: ...
PGBit = BIT

class TSVECTOR(sqltypes.TypeEngine[str]):
    """The :class:`_postgresql.TSVECTOR` type implements the PostgreSQL
    text search type TSVECTOR.

    It can be used to do full text queries on natural language
    documents.

    .. seealso::

        :ref:`postgresql_match`

    """
    __visit_name__: str

class CITEXT(sqltypes.TEXT):
    """Provide the PostgreSQL CITEXT type.

    .. versionadded:: 2.0.7

    """
    __visit_name__: str
    def coerce_compared_value(self, op: OperatorType | None, value: Any) -> TypeEngine[Any]: ...
