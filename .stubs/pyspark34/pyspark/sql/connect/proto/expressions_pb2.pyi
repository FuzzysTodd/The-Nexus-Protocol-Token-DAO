import builtins
import collections.abc
import google
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import pyspark.sql.connect.proto.types_pb2
import typing
import typing as typing_extensions
from _typeshed import Incomplete

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Expression(google.protobuf.message.Message):
    """Expression used to refer to fields, functions and similar. This can be used everywhere
    expressions in SQL appear.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Window(google.protobuf.message.Message):
        """Expression for the OVER clause or WINDOW clause."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class WindowFrame(google.protobuf.message.Message):
            """The window frame"""
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            class _FrameType:
                ValueType: Incomplete
                V: typing_extensions.TypeAlias
            class _FrameTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Expression.Window.WindowFrame._FrameType.ValueType], builtins.type):
                DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
                FRAME_TYPE_UNDEFINED: Expression.Window.WindowFrame._FrameType.ValueType
                FRAME_TYPE_ROW: Expression.Window.WindowFrame._FrameType.ValueType
                FRAME_TYPE_RANGE: Expression.Window.WindowFrame._FrameType.ValueType
            class FrameType(_FrameType, metaclass=_FrameTypeEnumTypeWrapper): ...
            FRAME_TYPE_UNDEFINED: Expression.Window.WindowFrame.FrameType.ValueType
            FRAME_TYPE_ROW: Expression.Window.WindowFrame.FrameType.ValueType
            FRAME_TYPE_RANGE: Expression.Window.WindowFrame.FrameType.ValueType
            class FrameBoundary(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor
                CURRENT_ROW_FIELD_NUMBER: builtins.int
                UNBOUNDED_FIELD_NUMBER: builtins.int
                VALUE_FIELD_NUMBER: builtins.int
                current_row: builtins.bool
                unbounded: builtins.bool
                @property
                def value(self) -> global___Expression:
                    """This is an expression for future proofing. We are expecting literals on the server side."""
                def __init__(self, *, current_row: builtins.bool = ..., unbounded: builtins.bool = ..., value: global___Expression | None = ...) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal['boundary', 'boundary', 'current_row', 'current_row', 'unbounded', 'unbounded', 'value', 'value']) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal['boundary', 'boundary', 'current_row', 'current_row', 'unbounded', 'unbounded', 'value', 'value']) -> None: ...
                def WhichOneof(self, oneof_group: typing_extensions.Literal['boundary', 'boundary']) -> typing_extensions.Literal['current_row', 'unbounded', 'value'] | None: ...
            FRAME_TYPE_FIELD_NUMBER: builtins.int
            LOWER_FIELD_NUMBER: builtins.int
            UPPER_FIELD_NUMBER: builtins.int
            frame_type: global___Expression.Window.WindowFrame.FrameType.ValueType
            @property
            def lower(self) -> global___Expression.Window.WindowFrame.FrameBoundary:
                """(Required) The lower bound of the frame."""
            @property
            def upper(self) -> global___Expression.Window.WindowFrame.FrameBoundary:
                """(Required) The upper bound of the frame."""
            def __init__(self, *, frame_type: global___Expression.Window.WindowFrame.FrameType.ValueType = ..., lower: global___Expression.Window.WindowFrame.FrameBoundary | None = ..., upper: global___Expression.Window.WindowFrame.FrameBoundary | None = ...) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal['lower', 'lower', 'upper', 'upper']) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal['frame_type', 'frame_type', 'lower', 'lower', 'upper', 'upper']) -> None: ...
        WINDOW_FUNCTION_FIELD_NUMBER: builtins.int
        PARTITION_SPEC_FIELD_NUMBER: builtins.int
        ORDER_SPEC_FIELD_NUMBER: builtins.int
        FRAME_SPEC_FIELD_NUMBER: builtins.int
        @property
        def window_function(self) -> global___Expression:
            """(Required) The window function."""
        @property
        def partition_spec(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Expression]:
            """(Optional) The way that input rows are partitioned."""
        @property
        def order_spec(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Expression.SortOrder]:
            """(Optional) Ordering of rows in a partition."""
        @property
        def frame_spec(self) -> global___Expression.Window.WindowFrame:
            """(Optional) Window frame in a partition.

            If not set, it will be treated as 'UnspecifiedFrame'.
            """
        def __init__(self, *, window_function: global___Expression | None = ..., partition_spec: collections.abc.Iterable[global___Expression] | None = ..., order_spec: collections.abc.Iterable[global___Expression.SortOrder] | None = ..., frame_spec: global___Expression.Window.WindowFrame | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['frame_spec', 'frame_spec', 'window_function', 'window_function']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['frame_spec', 'frame_spec', 'order_spec', 'order_spec', 'partition_spec', 'partition_spec', 'window_function', 'window_function']) -> None: ...
    class SortOrder(google.protobuf.message.Message):
        """SortOrder is used to specify the  data ordering, it is normally used in Sort and Window.
        It is an unevaluable expression and cannot be evaluated, so can not be used in Projection.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _SortDirection:
            ValueType: Incomplete
            V: typing_extensions.TypeAlias
        class _SortDirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Expression.SortOrder._SortDirection.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            SORT_DIRECTION_UNSPECIFIED: Expression.SortOrder._SortDirection.ValueType
            SORT_DIRECTION_ASCENDING: Expression.SortOrder._SortDirection.ValueType
            SORT_DIRECTION_DESCENDING: Expression.SortOrder._SortDirection.ValueType
        class SortDirection(_SortDirection, metaclass=_SortDirectionEnumTypeWrapper): ...
        SORT_DIRECTION_UNSPECIFIED: Expression.SortOrder.SortDirection.ValueType
        SORT_DIRECTION_ASCENDING: Expression.SortOrder.SortDirection.ValueType
        SORT_DIRECTION_DESCENDING: Expression.SortOrder.SortDirection.ValueType
        class _NullOrdering:
            ValueType: Incomplete
            V: typing_extensions.TypeAlias
        class _NullOrderingEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Expression.SortOrder._NullOrdering.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            SORT_NULLS_UNSPECIFIED: Expression.SortOrder._NullOrdering.ValueType
            SORT_NULLS_FIRST: Expression.SortOrder._NullOrdering.ValueType
            SORT_NULLS_LAST: Expression.SortOrder._NullOrdering.ValueType
        class NullOrdering(_NullOrdering, metaclass=_NullOrderingEnumTypeWrapper): ...
        SORT_NULLS_UNSPECIFIED: Expression.SortOrder.NullOrdering.ValueType
        SORT_NULLS_FIRST: Expression.SortOrder.NullOrdering.ValueType
        SORT_NULLS_LAST: Expression.SortOrder.NullOrdering.ValueType
        CHILD_FIELD_NUMBER: builtins.int
        DIRECTION_FIELD_NUMBER: builtins.int
        NULL_ORDERING_FIELD_NUMBER: builtins.int
        @property
        def child(self) -> global___Expression:
            """(Required) The expression to be sorted."""
        direction: global___Expression.SortOrder.SortDirection.ValueType
        null_ordering: global___Expression.SortOrder.NullOrdering.ValueType
        def __init__(self, *, child: global___Expression | None = ..., direction: global___Expression.SortOrder.SortDirection.ValueType = ..., null_ordering: global___Expression.SortOrder.NullOrdering.ValueType = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['child', 'child']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['child', 'child', 'direction', 'direction', 'null_ordering', 'null_ordering']) -> None: ...
    class Cast(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        EXPR_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        TYPE_STR_FIELD_NUMBER: builtins.int
        @property
        def expr(self) -> global___Expression:
            """(Required) the expression to be casted."""
        @property
        def type(self) -> pyspark.sql.connect.proto.types_pb2.DataType: ...
        type_str: builtins.str
        def __init__(self, *, expr: global___Expression | None = ..., type: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., type_str: builtins.str = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['cast_to_type', 'cast_to_type', 'expr', 'expr', 'type', 'type', 'type_str', 'type_str']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['cast_to_type', 'cast_to_type', 'expr', 'expr', 'type', 'type', 'type_str', 'type_str']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['cast_to_type', 'cast_to_type']) -> typing_extensions.Literal['type', 'type_str'] | None: ...
    class Literal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class Decimal(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            VALUE_FIELD_NUMBER: builtins.int
            PRECISION_FIELD_NUMBER: builtins.int
            SCALE_FIELD_NUMBER: builtins.int
            value: builtins.str
            precision: builtins.int
            scale: builtins.int
            def __init__(self, *, value: builtins.str = ..., precision: builtins.int | None = ..., scale: builtins.int | None = ...) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal['_precision', '_precision', '_scale', '_scale', 'precision', 'precision', 'scale', 'scale']) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal['_precision', '_precision', '_scale', '_scale', 'precision', 'precision', 'scale', 'scale', 'value', 'value']) -> None: ...
            @typing.overload
            def WhichOneof(self, oneof_group: typing_extensions.Literal['_precision', '_precision']) -> typing_extensions.Literal['precision'] | None: ...
            @typing.overload
            def WhichOneof(self, oneof_group: typing_extensions.Literal['_scale', '_scale']) -> typing_extensions.Literal['scale'] | None: ...
        class CalendarInterval(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            MONTHS_FIELD_NUMBER: builtins.int
            DAYS_FIELD_NUMBER: builtins.int
            MICROSECONDS_FIELD_NUMBER: builtins.int
            months: builtins.int
            days: builtins.int
            microseconds: builtins.int
            def __init__(self, *, months: builtins.int = ..., days: builtins.int = ..., microseconds: builtins.int = ...) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal['days', 'days', 'microseconds', 'microseconds', 'months', 'months']) -> None: ...
        class Array(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            ELEMENT_TYPE_FIELD_NUMBER: builtins.int
            ELEMENTS_FIELD_NUMBER: builtins.int
            @property
            def element_type(self) -> pyspark.sql.connect.proto.types_pb2.DataType: ...
            @property
            def elements(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Expression.Literal]: ...
            def __init__(self, *, element_type: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., elements: collections.abc.Iterable[global___Expression.Literal] | None = ...) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal['element_type', 'element_type']) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal['element_type', 'element_type', 'elements', 'elements']) -> None: ...
        NULL_FIELD_NUMBER: builtins.int
        BINARY_FIELD_NUMBER: builtins.int
        BOOLEAN_FIELD_NUMBER: builtins.int
        BYTE_FIELD_NUMBER: builtins.int
        SHORT_FIELD_NUMBER: builtins.int
        INTEGER_FIELD_NUMBER: builtins.int
        LONG_FIELD_NUMBER: builtins.int
        FLOAT_FIELD_NUMBER: builtins.int
        DOUBLE_FIELD_NUMBER: builtins.int
        DECIMAL_FIELD_NUMBER: builtins.int
        STRING_FIELD_NUMBER: builtins.int
        DATE_FIELD_NUMBER: builtins.int
        TIMESTAMP_FIELD_NUMBER: builtins.int
        TIMESTAMP_NTZ_FIELD_NUMBER: builtins.int
        CALENDAR_INTERVAL_FIELD_NUMBER: builtins.int
        YEAR_MONTH_INTERVAL_FIELD_NUMBER: builtins.int
        DAY_TIME_INTERVAL_FIELD_NUMBER: builtins.int
        ARRAY_FIELD_NUMBER: builtins.int
        @property
        def null(self) -> pyspark.sql.connect.proto.types_pb2.DataType: ...
        binary: builtins.bytes
        boolean: builtins.bool
        byte: builtins.int
        short: builtins.int
        integer: builtins.int
        long: builtins.int
        float: builtins.float
        double: builtins.float
        @property
        def decimal(self) -> global___Expression.Literal.Decimal: ...
        string: builtins.str
        date: builtins.int
        timestamp: builtins.int
        timestamp_ntz: builtins.int
        @property
        def calendar_interval(self) -> global___Expression.Literal.CalendarInterval: ...
        year_month_interval: builtins.int
        day_time_interval: builtins.int
        @property
        def array(self) -> global___Expression.Literal.Array: ...
        def __init__(self, *, null: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., binary: builtins.bytes = ..., boolean: builtins.bool = ..., byte: builtins.int = ..., short: builtins.int = ..., integer: builtins.int = ..., long: builtins.int = ..., float: builtins.float = ..., double: builtins.float = ..., decimal: global___Expression.Literal.Decimal | None = ..., string: builtins.str = ..., date: builtins.int = ..., timestamp: builtins.int = ..., timestamp_ntz: builtins.int = ..., calendar_interval: global___Expression.Literal.CalendarInterval | None = ..., year_month_interval: builtins.int = ..., day_time_interval: builtins.int = ..., array: global___Expression.Literal.Array | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['array', 'array', 'binary', 'binary', 'boolean', 'boolean', 'byte', 'byte', 'calendar_interval', 'calendar_interval', 'date', 'date', 'day_time_interval', 'day_time_interval', 'decimal', 'decimal', 'double', 'double', 'float', 'float', 'integer', 'integer', 'literal_type', 'literal_type', 'long', 'long', 'null', 'null', 'short', 'short', 'string', 'string', 'timestamp', 'timestamp', 'timestamp_ntz', 'timestamp_ntz', 'year_month_interval', 'year_month_interval']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['array', 'array', 'binary', 'binary', 'boolean', 'boolean', 'byte', 'byte', 'calendar_interval', 'calendar_interval', 'date', 'date', 'day_time_interval', 'day_time_interval', 'decimal', 'decimal', 'double', 'double', 'float', 'float', 'integer', 'integer', 'literal_type', 'literal_type', 'long', 'long', 'null', 'null', 'short', 'short', 'string', 'string', 'timestamp', 'timestamp', 'timestamp_ntz', 'timestamp_ntz', 'year_month_interval', 'year_month_interval']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['literal_type', 'literal_type']) -> typing_extensions.Literal['null', 'binary', 'boolean', 'byte', 'short', 'integer', 'long', 'float', 'double', 'decimal', 'string', 'date', 'timestamp', 'timestamp_ntz', 'calendar_interval', 'year_month_interval', 'day_time_interval', 'array'] | None: ...
    class UnresolvedAttribute(google.protobuf.message.Message):
        """An unresolved attribute that is not explicitly bound to a specific column, but the column
        is resolved during analysis by name.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        UNPARSED_IDENTIFIER_FIELD_NUMBER: builtins.int
        PLAN_ID_FIELD_NUMBER: builtins.int
        unparsed_identifier: builtins.str
        plan_id: builtins.int
        def __init__(self, *, unparsed_identifier: builtins.str = ..., plan_id: builtins.int | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_plan_id', '_plan_id', 'plan_id', 'plan_id']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_plan_id', '_plan_id', 'plan_id', 'plan_id', 'unparsed_identifier', 'unparsed_identifier']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_plan_id', '_plan_id']) -> typing_extensions.Literal['plan_id'] | None: ...
    class UnresolvedFunction(google.protobuf.message.Message):
        """An unresolved function is not explicitly bound to one explicit function, but the function
        is resolved during analysis following Sparks name resolution rules.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        FUNCTION_NAME_FIELD_NUMBER: builtins.int
        ARGUMENTS_FIELD_NUMBER: builtins.int
        IS_DISTINCT_FIELD_NUMBER: builtins.int
        IS_USER_DEFINED_FUNCTION_FIELD_NUMBER: builtins.int
        function_name: builtins.str
        @property
        def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Expression]:
            """(Optional) Function arguments. Empty arguments are allowed."""
        is_distinct: builtins.bool
        is_user_defined_function: builtins.bool
        def __init__(self, *, function_name: builtins.str = ..., arguments: collections.abc.Iterable[global___Expression] | None = ..., is_distinct: builtins.bool = ..., is_user_defined_function: builtins.bool = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['arguments', 'arguments', 'function_name', 'function_name', 'is_distinct', 'is_distinct', 'is_user_defined_function', 'is_user_defined_function']) -> None: ...
    class ExpressionString(google.protobuf.message.Message):
        """Expression as string."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        EXPRESSION_FIELD_NUMBER: builtins.int
        expression: builtins.str
        def __init__(self, *, expression: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['expression', 'expression']) -> None: ...
    class UnresolvedStar(google.protobuf.message.Message):
        """UnresolvedStar is used to expand all the fields of a relation or struct."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        UNPARSED_TARGET_FIELD_NUMBER: builtins.int
        unparsed_target: builtins.str
        def __init__(self, *, unparsed_target: builtins.str | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_unparsed_target', '_unparsed_target', 'unparsed_target', 'unparsed_target']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_unparsed_target', '_unparsed_target', 'unparsed_target', 'unparsed_target']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_unparsed_target', '_unparsed_target']) -> typing_extensions.Literal['unparsed_target'] | None: ...
    class UnresolvedRegex(google.protobuf.message.Message):
        '''Represents all of the input attributes to a given relational operator, for example in
        "SELECT `(id)?+.+` FROM ...".
        '''
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        COL_NAME_FIELD_NUMBER: builtins.int
        PLAN_ID_FIELD_NUMBER: builtins.int
        col_name: builtins.str
        plan_id: builtins.int
        def __init__(self, *, col_name: builtins.str = ..., plan_id: builtins.int | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_plan_id', '_plan_id', 'plan_id', 'plan_id']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_plan_id', '_plan_id', 'col_name', 'col_name', 'plan_id', 'plan_id']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_plan_id', '_plan_id']) -> typing_extensions.Literal['plan_id'] | None: ...
    class UnresolvedExtractValue(google.protobuf.message.Message):
        """Extracts a value or values from an Expression"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        CHILD_FIELD_NUMBER: builtins.int
        EXTRACTION_FIELD_NUMBER: builtins.int
        @property
        def child(self) -> global___Expression:
            """(Required) The expression to extract value from, can be
            Map, Array, Struct or array of Structs.
            """
        @property
        def extraction(self) -> global___Expression:
            """(Required) The expression to describe the extraction, can be
            key of Map, index of Array, field name of Struct.
            """
        def __init__(self, *, child: global___Expression | None = ..., extraction: global___Expression | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['child', 'child', 'extraction', 'extraction']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['child', 'child', 'extraction', 'extraction']) -> None: ...
    class UpdateFields(google.protobuf.message.Message):
        """Add, replace or drop a field of `StructType` expression by name."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        STRUCT_EXPRESSION_FIELD_NUMBER: builtins.int
        FIELD_NAME_FIELD_NUMBER: builtins.int
        VALUE_EXPRESSION_FIELD_NUMBER: builtins.int
        @property
        def struct_expression(self) -> global___Expression:
            """(Required) The struct expression."""
        field_name: builtins.str
        @property
        def value_expression(self) -> global___Expression:
            """(Optional) The expression to add or replace.

            When not set, it means this field will be dropped.
            """
        def __init__(self, *, struct_expression: global___Expression | None = ..., field_name: builtins.str = ..., value_expression: global___Expression | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['struct_expression', 'struct_expression', 'value_expression', 'value_expression']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['field_name', 'field_name', 'struct_expression', 'struct_expression', 'value_expression', 'value_expression']) -> None: ...
    class Alias(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        EXPR_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        METADATA_FIELD_NUMBER: builtins.int
        @property
        def expr(self) -> global___Expression:
            """(Required) The expression that alias will be added on."""
        @property
        def name(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) a list of name parts for the alias.

            Scalar columns only has one name that presents.
            """
        metadata: builtins.str
        def __init__(self, *, expr: global___Expression | None = ..., name: collections.abc.Iterable[builtins.str] | None = ..., metadata: builtins.str | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_metadata', '_metadata', 'expr', 'expr', 'metadata', 'metadata']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_metadata', '_metadata', 'expr', 'expr', 'metadata', 'metadata', 'name', 'name']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_metadata', '_metadata']) -> typing_extensions.Literal['metadata'] | None: ...
    class LambdaFunction(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        FUNCTION_FIELD_NUMBER: builtins.int
        ARGUMENTS_FIELD_NUMBER: builtins.int
        @property
        def function(self) -> global___Expression:
            """(Required) The lambda function.

            The function body should use 'UnresolvedAttribute' as arguments, the sever side will
            replace 'UnresolvedAttribute' with 'UnresolvedNamedLambdaVariable'.
            """
        @property
        def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Expression.UnresolvedNamedLambdaVariable]:
            """(Required) Function variables. Must contains 1 ~ 3 variables."""
        def __init__(self, *, function: global___Expression | None = ..., arguments: collections.abc.Iterable[global___Expression.UnresolvedNamedLambdaVariable] | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['function', 'function']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['arguments', 'arguments', 'function', 'function']) -> None: ...
    class UnresolvedNamedLambdaVariable(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_PARTS_FIELD_NUMBER: builtins.int
        @property
        def name_parts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) a list of name parts for the variable. Must not be empty."""
        def __init__(self, *, name_parts: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['name_parts', 'name_parts']) -> None: ...
    LITERAL_FIELD_NUMBER: builtins.int
    UNRESOLVED_ATTRIBUTE_FIELD_NUMBER: builtins.int
    UNRESOLVED_FUNCTION_FIELD_NUMBER: builtins.int
    EXPRESSION_STRING_FIELD_NUMBER: builtins.int
    UNRESOLVED_STAR_FIELD_NUMBER: builtins.int
    ALIAS_FIELD_NUMBER: builtins.int
    CAST_FIELD_NUMBER: builtins.int
    UNRESOLVED_REGEX_FIELD_NUMBER: builtins.int
    SORT_ORDER_FIELD_NUMBER: builtins.int
    LAMBDA_FUNCTION_FIELD_NUMBER: builtins.int
    WINDOW_FIELD_NUMBER: builtins.int
    UNRESOLVED_EXTRACT_VALUE_FIELD_NUMBER: builtins.int
    UPDATE_FIELDS_FIELD_NUMBER: builtins.int
    UNRESOLVED_NAMED_LAMBDA_VARIABLE_FIELD_NUMBER: builtins.int
    COMMON_INLINE_USER_DEFINED_FUNCTION_FIELD_NUMBER: builtins.int
    EXTENSION_FIELD_NUMBER: builtins.int
    @property
    def literal(self) -> global___Expression.Literal: ...
    @property
    def unresolved_attribute(self) -> global___Expression.UnresolvedAttribute: ...
    @property
    def unresolved_function(self) -> global___Expression.UnresolvedFunction: ...
    @property
    def expression_string(self) -> global___Expression.ExpressionString: ...
    @property
    def unresolved_star(self) -> global___Expression.UnresolvedStar: ...
    @property
    def alias(self) -> global___Expression.Alias: ...
    @property
    def cast(self) -> global___Expression.Cast: ...
    @property
    def unresolved_regex(self) -> global___Expression.UnresolvedRegex: ...
    @property
    def sort_order(self) -> global___Expression.SortOrder: ...
    @property
    def lambda_function(self) -> global___Expression.LambdaFunction: ...
    @property
    def window(self) -> global___Expression.Window: ...
    @property
    def unresolved_extract_value(self) -> global___Expression.UnresolvedExtractValue: ...
    @property
    def update_fields(self) -> global___Expression.UpdateFields: ...
    @property
    def unresolved_named_lambda_variable(self) -> global___Expression.UnresolvedNamedLambdaVariable: ...
    @property
    def common_inline_user_defined_function(self) -> global___CommonInlineUserDefinedFunction: ...
    @property
    def extension(self) -> google.protobuf.any_pb2.Any:
        """This field is used to mark extensions to the protocol. When plugins generate arbitrary
        relations they can add them here. During the planning the correct resolution is done.
        """
    def __init__(self, *, literal: global___Expression.Literal | None = ..., unresolved_attribute: global___Expression.UnresolvedAttribute | None = ..., unresolved_function: global___Expression.UnresolvedFunction | None = ..., expression_string: global___Expression.ExpressionString | None = ..., unresolved_star: global___Expression.UnresolvedStar | None = ..., alias: global___Expression.Alias | None = ..., cast: global___Expression.Cast | None = ..., unresolved_regex: global___Expression.UnresolvedRegex | None = ..., sort_order: global___Expression.SortOrder | None = ..., lambda_function: global___Expression.LambdaFunction | None = ..., window: global___Expression.Window | None = ..., unresolved_extract_value: global___Expression.UnresolvedExtractValue | None = ..., update_fields: global___Expression.UpdateFields | None = ..., unresolved_named_lambda_variable: global___Expression.UnresolvedNamedLambdaVariable | None = ..., common_inline_user_defined_function: global___CommonInlineUserDefinedFunction | None = ..., extension: google.protobuf.any_pb2.Any | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['alias', 'alias', 'cast', 'cast', 'common_inline_user_defined_function', 'common_inline_user_defined_function', 'expr_type', 'expr_type', 'expression_string', 'expression_string', 'extension', 'extension', 'lambda_function', 'lambda_function', 'literal', 'literal', 'sort_order', 'sort_order', 'unresolved_attribute', 'unresolved_attribute', 'unresolved_extract_value', 'unresolved_extract_value', 'unresolved_function', 'unresolved_function', 'unresolved_named_lambda_variable', 'unresolved_named_lambda_variable', 'unresolved_regex', 'unresolved_regex', 'unresolved_star', 'unresolved_star', 'update_fields', 'update_fields', 'window', 'window']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['alias', 'alias', 'cast', 'cast', 'common_inline_user_defined_function', 'common_inline_user_defined_function', 'expr_type', 'expr_type', 'expression_string', 'expression_string', 'extension', 'extension', 'lambda_function', 'lambda_function', 'literal', 'literal', 'sort_order', 'sort_order', 'unresolved_attribute', 'unresolved_attribute', 'unresolved_extract_value', 'unresolved_extract_value', 'unresolved_function', 'unresolved_function', 'unresolved_named_lambda_variable', 'unresolved_named_lambda_variable', 'unresolved_regex', 'unresolved_regex', 'unresolved_star', 'unresolved_star', 'update_fields', 'update_fields', 'window', 'window']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['expr_type', 'expr_type']) -> typing_extensions.Literal['literal', 'unresolved_attribute', 'unresolved_function', 'expression_string', 'unresolved_star', 'alias', 'cast', 'unresolved_regex', 'sort_order', 'lambda_function', 'window', 'unresolved_extract_value', 'update_fields', 'unresolved_named_lambda_variable', 'common_inline_user_defined_function', 'extension'] | None: ...
global___Expression = Expression

class CommonInlineUserDefinedFunction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FUNCTION_NAME_FIELD_NUMBER: builtins.int
    DETERMINISTIC_FIELD_NUMBER: builtins.int
    ARGUMENTS_FIELD_NUMBER: builtins.int
    PYTHON_UDF_FIELD_NUMBER: builtins.int
    SCALAR_SCALA_UDF_FIELD_NUMBER: builtins.int
    JAVA_UDF_FIELD_NUMBER: builtins.int
    function_name: builtins.str
    deterministic: builtins.bool
    @property
    def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Expression]:
        """(Optional) Function arguments. Empty arguments are allowed."""
    @property
    def python_udf(self) -> global___PythonUDF: ...
    @property
    def scalar_scala_udf(self) -> global___ScalarScalaUDF: ...
    @property
    def java_udf(self) -> global___JavaUDF: ...
    def __init__(self, *, function_name: builtins.str = ..., deterministic: builtins.bool = ..., arguments: collections.abc.Iterable[global___Expression] | None = ..., python_udf: global___PythonUDF | None = ..., scalar_scala_udf: global___ScalarScalaUDF | None = ..., java_udf: global___JavaUDF | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['function', 'function', 'java_udf', 'java_udf', 'python_udf', 'python_udf', 'scalar_scala_udf', 'scalar_scala_udf']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['arguments', 'arguments', 'deterministic', 'deterministic', 'function', 'function', 'function_name', 'function_name', 'java_udf', 'java_udf', 'python_udf', 'python_udf', 'scalar_scala_udf', 'scalar_scala_udf']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['function', 'function']) -> typing_extensions.Literal['python_udf', 'scalar_scala_udf', 'java_udf'] | None: ...
global___CommonInlineUserDefinedFunction = CommonInlineUserDefinedFunction

class PythonUDF(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OUTPUT_TYPE_FIELD_NUMBER: builtins.int
    EVAL_TYPE_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    PYTHON_VER_FIELD_NUMBER: builtins.int
    @property
    def output_type(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Required) Output type of the Python UDF"""
    eval_type: builtins.int
    command: builtins.bytes
    python_ver: builtins.str
    def __init__(self, *, output_type: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., eval_type: builtins.int = ..., command: builtins.bytes = ..., python_ver: builtins.str = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['output_type', 'output_type']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['command', 'command', 'eval_type', 'eval_type', 'output_type', 'output_type', 'python_ver', 'python_ver']) -> None: ...
global___PythonUDF = PythonUDF

class ScalarScalaUDF(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAYLOAD_FIELD_NUMBER: builtins.int
    INPUTTYPES_FIELD_NUMBER: builtins.int
    OUTPUTTYPE_FIELD_NUMBER: builtins.int
    NULLABLE_FIELD_NUMBER: builtins.int
    payload: builtins.bytes
    @property
    def inputTypes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.types_pb2.DataType]:
        """(Optional) Input type(s) of the UDF"""
    @property
    def outputType(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Required) Output type of the UDF"""
    nullable: builtins.bool
    def __init__(self, *, payload: builtins.bytes = ..., inputTypes: collections.abc.Iterable[pyspark.sql.connect.proto.types_pb2.DataType] | None = ..., outputType: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., nullable: builtins.bool = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['outputType', 'outputType']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['inputTypes', 'inputTypes', 'nullable', 'nullable', 'outputType', 'outputType', 'payload', 'payload']) -> None: ...
global___ScalarScalaUDF = ScalarScalaUDF

class JavaUDF(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLASS_NAME_FIELD_NUMBER: builtins.int
    OUTPUT_TYPE_FIELD_NUMBER: builtins.int
    AGGREGATE_FIELD_NUMBER: builtins.int
    class_name: builtins.str
    @property
    def output_type(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Optional) Output type of the Java UDF"""
    aggregate: builtins.bool
    def __init__(self, *, class_name: builtins.str = ..., output_type: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., aggregate: builtins.bool = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_output_type', '_output_type', 'output_type', 'output_type']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_output_type', '_output_type', 'aggregate', 'aggregate', 'class_name', 'class_name', 'output_type', 'output_type']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_output_type', '_output_type']) -> typing_extensions.Literal['output_type'] | None: ...
global___JavaUDF = JavaUDF
