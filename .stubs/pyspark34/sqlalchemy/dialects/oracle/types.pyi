from ... import exc as exc
from ...sql import sqltypes as sqltypes
from ...types import NVARCHAR as NVARCHAR, VARCHAR as VARCHAR
from _typeshed import Incomplete

class RAW(sqltypes._Binary):
    __visit_name__: str
OracleRaw = RAW

class NCLOB(sqltypes.Text):
    __visit_name__: str

class VARCHAR2(VARCHAR):
    __visit_name__: str
NVARCHAR2 = NVARCHAR

class NUMBER(sqltypes.Numeric, sqltypes.Integer):
    __visit_name__: str
    def __init__(self, precision: Incomplete | None = None, scale: Incomplete | None = None, asdecimal: Incomplete | None = None) -> None: ...
    def adapt(self, impltype): ...

class FLOAT(sqltypes.FLOAT):
    '''Oracle FLOAT.

    This is the same as :class:`_sqltypes.FLOAT` except that
    an Oracle-specific :paramref:`_oracle.FLOAT.binary_precision`
    parameter is accepted, and
    the :paramref:`_sqltypes.Float.precision` parameter is not accepted.

    Oracle FLOAT types indicate precision in terms of "binary precision", which
    defaults to 126. For a REAL type, the value is 63. This parameter does not
    cleanly map to a specific number of decimal places but is roughly
    equivalent to the desired number of decimal places divided by 0.3103.

    .. versionadded:: 2.0

    '''
    __visit_name__: str
    binary_precision: Incomplete
    def __init__(self, binary_precision: Incomplete | None = None, asdecimal: bool = False, decimal_return_scale: Incomplete | None = None) -> None:
        '''
        Construct a FLOAT

        :param binary_precision: Oracle binary precision value to be rendered
         in DDL. This may be approximated to the number of decimal characters
         using the formula "decimal precision = 0.30103 * binary precision".
         The default value used by Oracle for FLOAT / DOUBLE PRECISION is 126.

        :param asdecimal: See :paramref:`_sqltypes.Float.asdecimal`

        :param decimal_return_scale: See
         :paramref:`_sqltypes.Float.decimal_return_scale`

        '''

class BINARY_DOUBLE(sqltypes.Double):
    __visit_name__: str

class BINARY_FLOAT(sqltypes.Float):
    __visit_name__: str

class BFILE(sqltypes.LargeBinary):
    __visit_name__: str

class LONG(sqltypes.Text):
    __visit_name__: str

class _OracleDateLiteralRender: ...

class DATE(_OracleDateLiteralRender, sqltypes.DateTime):
    """Provide the oracle DATE type.

    This type has no special Python behavior, except that it subclasses
    :class:`_types.DateTime`; this is to suit the fact that the Oracle
    ``DATE`` type supports a time value.

    """
    __visit_name__: str
    def literal_processor(self, dialect): ...

class _OracleDate(_OracleDateLiteralRender, sqltypes.Date):
    def literal_processor(self, dialect): ...

class INTERVAL(sqltypes.NativeForEmulated, sqltypes._AbstractInterval):
    __visit_name__: str
    day_precision: Incomplete
    second_precision: Incomplete
    def __init__(self, day_precision: Incomplete | None = None, second_precision: Incomplete | None = None) -> None:
        '''Construct an INTERVAL.

        Note that only DAY TO SECOND intervals are currently supported.
        This is due to a lack of support for YEAR TO MONTH intervals
        within available DBAPIs.

        :param day_precision: the day precision value.  this is the number of
          digits to store for the day field.  Defaults to "2"
        :param second_precision: the second precision value.  this is the
          number of digits to store for the fractional seconds field.
          Defaults to "6".

        '''
    def as_generic(self, allow_nulltype: bool = False): ...

class TIMESTAMP(sqltypes.TIMESTAMP):
    """Oracle implementation of ``TIMESTAMP``, which supports additional
    Oracle-specific modes

    .. versionadded:: 2.0

    """
    local_timezone: Incomplete
    def __init__(self, timezone: bool = False, local_timezone: bool = False) -> None:
        """Construct a new :class:`_oracle.TIMESTAMP`.

        :param timezone: boolean.  Indicates that the TIMESTAMP type should
         use Oracle's ``TIMESTAMP WITH TIME ZONE`` datatype.

        :param local_timezone: boolean.  Indicates that the TIMESTAMP type
         should use Oracle's ``TIMESTAMP WITH LOCAL TIME ZONE`` datatype.


        """

class ROWID(sqltypes.TypeEngine):
    """Oracle ROWID type.

    When used in a cast() or similar, generates ROWID.

    """
    __visit_name__: str

class _OracleBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi): ...
