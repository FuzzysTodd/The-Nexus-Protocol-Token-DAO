import builtins
import collections.abc
import google
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import pyspark.sql.connect.proto.catalog_pb2
import pyspark.sql.connect.proto.expressions_pb2
import pyspark.sql.connect.proto.types_pb2
import typing
import typing as typing_extensions
from _typeshed import Incomplete

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Relation(google.protobuf.message.Message):
    """The main [[Relation]] type. Fundamentally, a relation is a typed container
    that has exactly one explicit relation type set.

    When adding new relation types, they have to be registered here.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COMMON_FIELD_NUMBER: builtins.int
    READ_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    JOIN_FIELD_NUMBER: builtins.int
    SET_OP_FIELD_NUMBER: builtins.int
    SORT_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    AGGREGATE_FIELD_NUMBER: builtins.int
    SQL_FIELD_NUMBER: builtins.int
    LOCAL_RELATION_FIELD_NUMBER: builtins.int
    SAMPLE_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    DEDUPLICATE_FIELD_NUMBER: builtins.int
    RANGE_FIELD_NUMBER: builtins.int
    SUBQUERY_ALIAS_FIELD_NUMBER: builtins.int
    REPARTITION_FIELD_NUMBER: builtins.int
    TO_DF_FIELD_NUMBER: builtins.int
    WITH_COLUMNS_RENAMED_FIELD_NUMBER: builtins.int
    SHOW_STRING_FIELD_NUMBER: builtins.int
    DROP_FIELD_NUMBER: builtins.int
    TAIL_FIELD_NUMBER: builtins.int
    WITH_COLUMNS_FIELD_NUMBER: builtins.int
    HINT_FIELD_NUMBER: builtins.int
    UNPIVOT_FIELD_NUMBER: builtins.int
    TO_SCHEMA_FIELD_NUMBER: builtins.int
    REPARTITION_BY_EXPRESSION_FIELD_NUMBER: builtins.int
    MAP_PARTITIONS_FIELD_NUMBER: builtins.int
    COLLECT_METRICS_FIELD_NUMBER: builtins.int
    PARSE_FIELD_NUMBER: builtins.int
    GROUP_MAP_FIELD_NUMBER: builtins.int
    CO_GROUP_MAP_FIELD_NUMBER: builtins.int
    FILL_NA_FIELD_NUMBER: builtins.int
    DROP_NA_FIELD_NUMBER: builtins.int
    REPLACE_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    CROSSTAB_FIELD_NUMBER: builtins.int
    DESCRIBE_FIELD_NUMBER: builtins.int
    COV_FIELD_NUMBER: builtins.int
    CORR_FIELD_NUMBER: builtins.int
    APPROX_QUANTILE_FIELD_NUMBER: builtins.int
    FREQ_ITEMS_FIELD_NUMBER: builtins.int
    SAMPLE_BY_FIELD_NUMBER: builtins.int
    CATALOG_FIELD_NUMBER: builtins.int
    EXTENSION_FIELD_NUMBER: builtins.int
    UNKNOWN_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___RelationCommon: ...
    @property
    def read(self) -> global___Read: ...
    @property
    def project(self) -> global___Project: ...
    @property
    def filter(self) -> global___Filter: ...
    @property
    def join(self) -> global___Join: ...
    @property
    def set_op(self) -> global___SetOperation: ...
    @property
    def sort(self) -> global___Sort: ...
    @property
    def limit(self) -> global___Limit: ...
    @property
    def aggregate(self) -> global___Aggregate: ...
    @property
    def sql(self) -> global___SQL: ...
    @property
    def local_relation(self) -> global___LocalRelation: ...
    @property
    def sample(self) -> global___Sample: ...
    @property
    def offset(self) -> global___Offset: ...
    @property
    def deduplicate(self) -> global___Deduplicate: ...
    @property
    def range(self) -> global___Range: ...
    @property
    def subquery_alias(self) -> global___SubqueryAlias: ...
    @property
    def repartition(self) -> global___Repartition: ...
    @property
    def to_df(self) -> global___ToDF: ...
    @property
    def with_columns_renamed(self) -> global___WithColumnsRenamed: ...
    @property
    def show_string(self) -> global___ShowString: ...
    @property
    def drop(self) -> global___Drop: ...
    @property
    def tail(self) -> global___Tail: ...
    @property
    def with_columns(self) -> global___WithColumns: ...
    @property
    def hint(self) -> global___Hint: ...
    @property
    def unpivot(self) -> global___Unpivot: ...
    @property
    def to_schema(self) -> global___ToSchema: ...
    @property
    def repartition_by_expression(self) -> global___RepartitionByExpression: ...
    @property
    def map_partitions(self) -> global___MapPartitions: ...
    @property
    def collect_metrics(self) -> global___CollectMetrics: ...
    @property
    def parse(self) -> global___Parse: ...
    @property
    def group_map(self) -> global___GroupMap: ...
    @property
    def co_group_map(self) -> global___CoGroupMap: ...
    @property
    def fill_na(self) -> global___NAFill:
        """NA functions"""
    @property
    def drop_na(self) -> global___NADrop: ...
    @property
    def replace(self) -> global___NAReplace: ...
    @property
    def summary(self) -> global___StatSummary:
        """stat functions"""
    @property
    def crosstab(self) -> global___StatCrosstab: ...
    @property
    def describe(self) -> global___StatDescribe: ...
    @property
    def cov(self) -> global___StatCov: ...
    @property
    def corr(self) -> global___StatCorr: ...
    @property
    def approx_quantile(self) -> global___StatApproxQuantile: ...
    @property
    def freq_items(self) -> global___StatFreqItems: ...
    @property
    def sample_by(self) -> global___StatSampleBy: ...
    @property
    def catalog(self) -> pyspark.sql.connect.proto.catalog_pb2.Catalog:
        """Catalog API (experimental / unstable)"""
    @property
    def extension(self) -> google.protobuf.any_pb2.Any:
        """This field is used to mark extensions to the protocol. When plugins generate arbitrary
        relations they can add them here. During the planning the correct resolution is done.
        """
    @property
    def unknown(self) -> global___Unknown: ...
    def __init__(self, *, common: global___RelationCommon | None = ..., read: global___Read | None = ..., project: global___Project | None = ..., filter: global___Filter | None = ..., join: global___Join | None = ..., set_op: global___SetOperation | None = ..., sort: global___Sort | None = ..., limit: global___Limit | None = ..., aggregate: global___Aggregate | None = ..., sql: global___SQL | None = ..., local_relation: global___LocalRelation | None = ..., sample: global___Sample | None = ..., offset: global___Offset | None = ..., deduplicate: global___Deduplicate | None = ..., range: global___Range | None = ..., subquery_alias: global___SubqueryAlias | None = ..., repartition: global___Repartition | None = ..., to_df: global___ToDF | None = ..., with_columns_renamed: global___WithColumnsRenamed | None = ..., show_string: global___ShowString | None = ..., drop: global___Drop | None = ..., tail: global___Tail | None = ..., with_columns: global___WithColumns | None = ..., hint: global___Hint | None = ..., unpivot: global___Unpivot | None = ..., to_schema: global___ToSchema | None = ..., repartition_by_expression: global___RepartitionByExpression | None = ..., map_partitions: global___MapPartitions | None = ..., collect_metrics: global___CollectMetrics | None = ..., parse: global___Parse | None = ..., group_map: global___GroupMap | None = ..., co_group_map: global___CoGroupMap | None = ..., fill_na: global___NAFill | None = ..., drop_na: global___NADrop | None = ..., replace: global___NAReplace | None = ..., summary: global___StatSummary | None = ..., crosstab: global___StatCrosstab | None = ..., describe: global___StatDescribe | None = ..., cov: global___StatCov | None = ..., corr: global___StatCorr | None = ..., approx_quantile: global___StatApproxQuantile | None = ..., freq_items: global___StatFreqItems | None = ..., sample_by: global___StatSampleBy | None = ..., catalog: pyspark.sql.connect.proto.catalog_pb2.Catalog | None = ..., extension: google.protobuf.any_pb2.Any | None = ..., unknown: global___Unknown | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['aggregate', 'aggregate', 'approx_quantile', 'approx_quantile', 'catalog', 'catalog', 'co_group_map', 'co_group_map', 'collect_metrics', 'collect_metrics', 'common', 'common', 'corr', 'corr', 'cov', 'cov', 'crosstab', 'crosstab', 'deduplicate', 'deduplicate', 'describe', 'describe', 'drop', 'drop', 'drop_na', 'drop_na', 'extension', 'extension', 'fill_na', 'fill_na', 'filter', 'filter', 'freq_items', 'freq_items', 'group_map', 'group_map', 'hint', 'hint', 'join', 'join', 'limit', 'limit', 'local_relation', 'local_relation', 'map_partitions', 'map_partitions', 'offset', 'offset', 'parse', 'parse', 'project', 'project', 'range', 'range', 'read', 'read', 'rel_type', 'rel_type', 'repartition', 'repartition', 'repartition_by_expression', 'repartition_by_expression', 'replace', 'replace', 'sample', 'sample', 'sample_by', 'sample_by', 'set_op', 'set_op', 'show_string', 'show_string', 'sort', 'sort', 'sql', 'sql', 'subquery_alias', 'subquery_alias', 'summary', 'summary', 'tail', 'tail', 'to_df', 'to_df', 'to_schema', 'to_schema', 'unknown', 'unknown', 'unpivot', 'unpivot', 'with_columns', 'with_columns', 'with_columns_renamed', 'with_columns_renamed']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['aggregate', 'aggregate', 'approx_quantile', 'approx_quantile', 'catalog', 'catalog', 'co_group_map', 'co_group_map', 'collect_metrics', 'collect_metrics', 'common', 'common', 'corr', 'corr', 'cov', 'cov', 'crosstab', 'crosstab', 'deduplicate', 'deduplicate', 'describe', 'describe', 'drop', 'drop', 'drop_na', 'drop_na', 'extension', 'extension', 'fill_na', 'fill_na', 'filter', 'filter', 'freq_items', 'freq_items', 'group_map', 'group_map', 'hint', 'hint', 'join', 'join', 'limit', 'limit', 'local_relation', 'local_relation', 'map_partitions', 'map_partitions', 'offset', 'offset', 'parse', 'parse', 'project', 'project', 'range', 'range', 'read', 'read', 'rel_type', 'rel_type', 'repartition', 'repartition', 'repartition_by_expression', 'repartition_by_expression', 'replace', 'replace', 'sample', 'sample', 'sample_by', 'sample_by', 'set_op', 'set_op', 'show_string', 'show_string', 'sort', 'sort', 'sql', 'sql', 'subquery_alias', 'subquery_alias', 'summary', 'summary', 'tail', 'tail', 'to_df', 'to_df', 'to_schema', 'to_schema', 'unknown', 'unknown', 'unpivot', 'unpivot', 'with_columns', 'with_columns', 'with_columns_renamed', 'with_columns_renamed']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['rel_type', 'rel_type']) -> typing_extensions.Literal['read', 'project', 'filter', 'join', 'set_op', 'sort', 'limit', 'aggregate', 'sql', 'local_relation', 'sample', 'offset', 'deduplicate', 'range', 'subquery_alias', 'repartition', 'to_df', 'with_columns_renamed', 'show_string', 'drop', 'tail', 'with_columns', 'hint', 'unpivot', 'to_schema', 'repartition_by_expression', 'map_partitions', 'collect_metrics', 'parse', 'group_map', 'co_group_map', 'fill_na', 'drop_na', 'replace', 'summary', 'crosstab', 'describe', 'cov', 'corr', 'approx_quantile', 'freq_items', 'sample_by', 'catalog', 'extension', 'unknown'] | None: ...
global___Relation = Relation

class Unknown(google.protobuf.message.Message):
    """Used for testing purposes only."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...
global___Unknown = Unknown

class RelationCommon(google.protobuf.message.Message):
    """Common metadata of all relations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SOURCE_INFO_FIELD_NUMBER: builtins.int
    PLAN_ID_FIELD_NUMBER: builtins.int
    source_info: builtins.str
    plan_id: builtins.int
    def __init__(self, *, source_info: builtins.str = ..., plan_id: builtins.int | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_plan_id', '_plan_id', 'plan_id', 'plan_id']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_plan_id', '_plan_id', 'plan_id', 'plan_id', 'source_info', 'source_info']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_plan_id', '_plan_id']) -> typing_extensions.Literal['plan_id'] | None: ...
global___RelationCommon = RelationCommon

class SQL(google.protobuf.message.Message):
    """Relation that uses a SQL query to generate the output."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ArgsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression.Literal: ...
        def __init__(self, *, key: builtins.str = ..., value: pyspark.sql.connect.proto.expressions_pb2.Expression.Literal | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['value', 'value']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
    QUERY_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    query: builtins.str
    @property
    def args(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, pyspark.sql.connect.proto.expressions_pb2.Expression.Literal]:
        """(Optional) A map of parameter names to literal expressions."""
    def __init__(self, *, query: builtins.str = ..., args: collections.abc.Mapping[builtins.str, pyspark.sql.connect.proto.expressions_pb2.Expression.Literal] | None = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['args', 'args', 'query', 'query']) -> None: ...
global___SQL = SQL

class Read(google.protobuf.message.Message):
    """Relation that reads from a file / table or other data source. Does not have additional
    inputs.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class NamedTable(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class OptionsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            value: builtins.str
            def __init__(self, *, key: builtins.str = ..., value: builtins.str = ...) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
        UNPARSED_IDENTIFIER_FIELD_NUMBER: builtins.int
        OPTIONS_FIELD_NUMBER: builtins.int
        unparsed_identifier: builtins.str
        @property
        def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
            """Options for the named table. The map key is case insensitive."""
        def __init__(self, *, unparsed_identifier: builtins.str = ..., options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['options', 'options', 'unparsed_identifier', 'unparsed_identifier']) -> None: ...
    class DataSource(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class OptionsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            value: builtins.str
            def __init__(self, *, key: builtins.str = ..., value: builtins.str = ...) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
        FORMAT_FIELD_NUMBER: builtins.int
        SCHEMA_FIELD_NUMBER: builtins.int
        OPTIONS_FIELD_NUMBER: builtins.int
        PATHS_FIELD_NUMBER: builtins.int
        PREDICATES_FIELD_NUMBER: builtins.int
        format: builtins.str
        schema: builtins.str
        @property
        def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
            """Options for the data source. The context of this map varies based on the
            data source format. This options could be empty for valid data source format.
            The map key is case insensitive.
            """
        @property
        def paths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Optional) A list of path for file-system backed data sources."""
        @property
        def predicates(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Optional) Condition in the where clause for each partition.

            This is only supported by the JDBC data source.
            """
        def __init__(self, *, format: builtins.str | None = ..., schema: builtins.str | None = ..., options: collections.abc.Mapping[builtins.str, builtins.str] | None = ..., paths: collections.abc.Iterable[builtins.str] | None = ..., predicates: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_format', '_format', '_schema', '_schema', 'format', 'format', 'schema', 'schema']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_format', '_format', '_schema', '_schema', 'format', 'format', 'options', 'options', 'paths', 'paths', 'predicates', 'predicates', 'schema', 'schema']) -> None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_format', '_format']) -> typing_extensions.Literal['format'] | None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_schema', '_schema']) -> typing_extensions.Literal['schema'] | None: ...
    NAMED_TABLE_FIELD_NUMBER: builtins.int
    DATA_SOURCE_FIELD_NUMBER: builtins.int
    @property
    def named_table(self) -> global___Read.NamedTable: ...
    @property
    def data_source(self) -> global___Read.DataSource: ...
    def __init__(self, *, named_table: global___Read.NamedTable | None = ..., data_source: global___Read.DataSource | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['data_source', 'data_source', 'named_table', 'named_table', 'read_type', 'read_type']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['data_source', 'data_source', 'named_table', 'named_table', 'read_type', 'read_type']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['read_type', 'read_type']) -> typing_extensions.Literal['named_table', 'data_source'] | None: ...
global___Read = Read

class Project(google.protobuf.message.Message):
    """Projection of a bag of expressions for a given input relation.

    The input relation must be specified.
    The projected expression can be an arbitrary expression.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    EXPRESSIONS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Optional) Input relation is optional for Project.

        For example, `SELECT ABS(-1)` is valid plan without an input plan.
        """
    @property
    def expressions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Required) A Project requires at least one expression."""
    def __init__(self, *, input: global___Relation | None = ..., expressions: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['expressions', 'expressions', 'input', 'input']) -> None: ...
global___Project = Project

class Filter(google.protobuf.message.Message):
    """Relation that applies a boolean expression `condition` on each row of `input` to produce
    the output result.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for a Filter."""
    @property
    def condition(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression:
        """(Required) A Filter must have a condition expression."""
    def __init__(self, *, input: global___Relation | None = ..., condition: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['condition', 'condition', 'input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['condition', 'condition', 'input', 'input']) -> None: ...
global___Filter = Filter

class Join(google.protobuf.message.Message):
    """Relation of type [[Join]].

    `left` and `right` must be present.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _JoinType:
        ValueType: Incomplete
        V: typing_extensions.TypeAlias
    class _JoinTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Join._JoinType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        JOIN_TYPE_UNSPECIFIED: Join._JoinType.ValueType
        JOIN_TYPE_INNER: Join._JoinType.ValueType
        JOIN_TYPE_FULL_OUTER: Join._JoinType.ValueType
        JOIN_TYPE_LEFT_OUTER: Join._JoinType.ValueType
        JOIN_TYPE_RIGHT_OUTER: Join._JoinType.ValueType
        JOIN_TYPE_LEFT_ANTI: Join._JoinType.ValueType
        JOIN_TYPE_LEFT_SEMI: Join._JoinType.ValueType
        JOIN_TYPE_CROSS: Join._JoinType.ValueType
    class JoinType(_JoinType, metaclass=_JoinTypeEnumTypeWrapper): ...
    JOIN_TYPE_UNSPECIFIED: Join.JoinType.ValueType
    JOIN_TYPE_INNER: Join.JoinType.ValueType
    JOIN_TYPE_FULL_OUTER: Join.JoinType.ValueType
    JOIN_TYPE_LEFT_OUTER: Join.JoinType.ValueType
    JOIN_TYPE_RIGHT_OUTER: Join.JoinType.ValueType
    JOIN_TYPE_LEFT_ANTI: Join.JoinType.ValueType
    JOIN_TYPE_LEFT_SEMI: Join.JoinType.ValueType
    JOIN_TYPE_CROSS: Join.JoinType.ValueType
    LEFT_FIELD_NUMBER: builtins.int
    RIGHT_FIELD_NUMBER: builtins.int
    JOIN_CONDITION_FIELD_NUMBER: builtins.int
    JOIN_TYPE_FIELD_NUMBER: builtins.int
    USING_COLUMNS_FIELD_NUMBER: builtins.int
    @property
    def left(self) -> global___Relation:
        """(Required) Left input relation for a Join."""
    @property
    def right(self) -> global___Relation:
        """(Required) Right input relation for a Join."""
    @property
    def join_condition(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression:
        """(Optional) The join condition. Could be unset when `using_columns` is utilized.

        This field does not co-exist with using_columns.
        """
    join_type: global___Join.JoinType.ValueType
    @property
    def using_columns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Optional. using_columns provides a list of columns that should present on both sides of
        the join inputs that this Join will join on. For example A JOIN B USING col_name is
        equivalent to A JOIN B on A.col_name = B.col_name.

        This field does not co-exist with join_condition.
        """
    def __init__(self, *, left: global___Relation | None = ..., right: global___Relation | None = ..., join_condition: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ..., join_type: global___Join.JoinType.ValueType = ..., using_columns: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['join_condition', 'join_condition', 'left', 'left', 'right', 'right']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['join_condition', 'join_condition', 'join_type', 'join_type', 'left', 'left', 'right', 'right', 'using_columns', 'using_columns']) -> None: ...
global___Join = Join

class SetOperation(google.protobuf.message.Message):
    """Relation of type [[SetOperation]]"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _SetOpType:
        ValueType: Incomplete
        V: typing_extensions.TypeAlias
    class _SetOpTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SetOperation._SetOpType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SET_OP_TYPE_UNSPECIFIED: SetOperation._SetOpType.ValueType
        SET_OP_TYPE_INTERSECT: SetOperation._SetOpType.ValueType
        SET_OP_TYPE_UNION: SetOperation._SetOpType.ValueType
        SET_OP_TYPE_EXCEPT: SetOperation._SetOpType.ValueType
    class SetOpType(_SetOpType, metaclass=_SetOpTypeEnumTypeWrapper): ...
    SET_OP_TYPE_UNSPECIFIED: SetOperation.SetOpType.ValueType
    SET_OP_TYPE_INTERSECT: SetOperation.SetOpType.ValueType
    SET_OP_TYPE_UNION: SetOperation.SetOpType.ValueType
    SET_OP_TYPE_EXCEPT: SetOperation.SetOpType.ValueType
    LEFT_INPUT_FIELD_NUMBER: builtins.int
    RIGHT_INPUT_FIELD_NUMBER: builtins.int
    SET_OP_TYPE_FIELD_NUMBER: builtins.int
    IS_ALL_FIELD_NUMBER: builtins.int
    BY_NAME_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_COLUMNS_FIELD_NUMBER: builtins.int
    @property
    def left_input(self) -> global___Relation:
        """(Required) Left input relation for a Set operation."""
    @property
    def right_input(self) -> global___Relation:
        """(Required) Right input relation for a Set operation."""
    set_op_type: global___SetOperation.SetOpType.ValueType
    is_all: builtins.bool
    by_name: builtins.bool
    allow_missing_columns: builtins.bool
    def __init__(self, *, left_input: global___Relation | None = ..., right_input: global___Relation | None = ..., set_op_type: global___SetOperation.SetOpType.ValueType = ..., is_all: builtins.bool | None = ..., by_name: builtins.bool | None = ..., allow_missing_columns: builtins.bool | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_allow_missing_columns', '_allow_missing_columns', '_by_name', '_by_name', '_is_all', '_is_all', 'allow_missing_columns', 'allow_missing_columns', 'by_name', 'by_name', 'is_all', 'is_all', 'left_input', 'left_input', 'right_input', 'right_input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_allow_missing_columns', '_allow_missing_columns', '_by_name', '_by_name', '_is_all', '_is_all', 'allow_missing_columns', 'allow_missing_columns', 'by_name', 'by_name', 'is_all', 'is_all', 'left_input', 'left_input', 'right_input', 'right_input', 'set_op_type', 'set_op_type']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_allow_missing_columns', '_allow_missing_columns']) -> typing_extensions.Literal['allow_missing_columns'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_by_name', '_by_name']) -> typing_extensions.Literal['by_name'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_is_all', '_is_all']) -> typing_extensions.Literal['is_all'] | None: ...
global___SetOperation = SetOperation

class Limit(google.protobuf.message.Message):
    """Relation of type [[Limit]] that is used to `limit` rows from the input relation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for a Limit."""
    limit: builtins.int
    def __init__(self, *, input: global___Relation | None = ..., limit: builtins.int = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'limit', 'limit']) -> None: ...
global___Limit = Limit

class Offset(google.protobuf.message.Message):
    """Relation of type [[Offset]] that is used to read rows staring from the `offset` on
    the input relation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for an Offset."""
    offset: builtins.int
    def __init__(self, *, input: global___Relation | None = ..., offset: builtins.int = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'offset', 'offset']) -> None: ...
global___Offset = Offset

class Tail(google.protobuf.message.Message):
    """Relation of type [[Tail]] that is used to fetch `limit` rows from the last of the input relation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for an Tail."""
    limit: builtins.int
    def __init__(self, *, input: global___Relation | None = ..., limit: builtins.int = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'limit', 'limit']) -> None: ...
global___Tail = Tail

class Aggregate(google.protobuf.message.Message):
    """Relation of type [[Aggregate]]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _GroupType:
        ValueType: Incomplete
        V: typing_extensions.TypeAlias
    class _GroupTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Aggregate._GroupType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        GROUP_TYPE_UNSPECIFIED: Aggregate._GroupType.ValueType
        GROUP_TYPE_GROUPBY: Aggregate._GroupType.ValueType
        GROUP_TYPE_ROLLUP: Aggregate._GroupType.ValueType
        GROUP_TYPE_CUBE: Aggregate._GroupType.ValueType
        GROUP_TYPE_PIVOT: Aggregate._GroupType.ValueType
    class GroupType(_GroupType, metaclass=_GroupTypeEnumTypeWrapper): ...
    GROUP_TYPE_UNSPECIFIED: Aggregate.GroupType.ValueType
    GROUP_TYPE_GROUPBY: Aggregate.GroupType.ValueType
    GROUP_TYPE_ROLLUP: Aggregate.GroupType.ValueType
    GROUP_TYPE_CUBE: Aggregate.GroupType.ValueType
    GROUP_TYPE_PIVOT: Aggregate.GroupType.ValueType
    class Pivot(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        COL_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        @property
        def col(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression:
            """(Required) The column to pivot"""
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression.Literal]:
            """(Optional) List of values that will be translated to columns in the output DataFrame.

            Note that if it is empty, the server side will immediately trigger a job to collect
            the distinct values of the column.
            """
        def __init__(self, *, col: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ..., values: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression.Literal] | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['col', 'col']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['col', 'col', 'values', 'values']) -> None: ...
    INPUT_FIELD_NUMBER: builtins.int
    GROUP_TYPE_FIELD_NUMBER: builtins.int
    GROUPING_EXPRESSIONS_FIELD_NUMBER: builtins.int
    AGGREGATE_EXPRESSIONS_FIELD_NUMBER: builtins.int
    PIVOT_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for a RelationalGroupedDataset."""
    group_type: global___Aggregate.GroupType.ValueType
    @property
    def grouping_expressions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Required) Expressions for grouping keys"""
    @property
    def aggregate_expressions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Required) List of values that will be translated to columns in the output DataFrame."""
    @property
    def pivot(self) -> global___Aggregate.Pivot:
        """(Optional) Pivots a column of the current `DataFrame` and performs the specified aggregation."""
    def __init__(self, *, input: global___Relation | None = ..., group_type: global___Aggregate.GroupType.ValueType = ..., grouping_expressions: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., aggregate_expressions: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., pivot: global___Aggregate.Pivot | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input', 'pivot', 'pivot']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['aggregate_expressions', 'aggregate_expressions', 'group_type', 'group_type', 'grouping_expressions', 'grouping_expressions', 'input', 'input', 'pivot', 'pivot']) -> None: ...
global___Aggregate = Aggregate

class Sort(google.protobuf.message.Message):
    """Relation of type [[Sort]]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    ORDER_FIELD_NUMBER: builtins.int
    IS_GLOBAL_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for a Sort."""
    @property
    def order(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression.SortOrder]:
        """(Required) The ordering expressions"""
    is_global: builtins.bool
    def __init__(self, *, input: global___Relation | None = ..., order: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression.SortOrder] | None = ..., is_global: builtins.bool | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_is_global', '_is_global', 'input', 'input', 'is_global', 'is_global']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_is_global', '_is_global', 'input', 'input', 'is_global', 'is_global', 'order', 'order']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_is_global', '_is_global']) -> typing_extensions.Literal['is_global'] | None: ...
global___Sort = Sort

class Drop(google.protobuf.message.Message):
    """Drop specified columns."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    COLUMN_NAMES_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def columns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Optional) columns to drop."""
    @property
    def column_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) names of columns to drop."""
    def __init__(self, *, input: global___Relation | None = ..., columns: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., column_names: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['column_names', 'column_names', 'columns', 'columns', 'input', 'input']) -> None: ...
global___Drop = Drop

class Deduplicate(google.protobuf.message.Message):
    """Relation of type [[Deduplicate]] which have duplicate rows removed, could consider either only
    the subset of columns or all the columns.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLUMN_NAMES_FIELD_NUMBER: builtins.int
    ALL_COLUMNS_AS_KEYS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for a Deduplicate."""
    @property
    def column_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) Deduplicate based on a list of column names.

        This field does not co-use with `all_columns_as_keys`.
        """
    all_columns_as_keys: builtins.bool
    def __init__(self, *, input: global___Relation | None = ..., column_names: collections.abc.Iterable[builtins.str] | None = ..., all_columns_as_keys: builtins.bool | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_all_columns_as_keys', '_all_columns_as_keys', 'all_columns_as_keys', 'all_columns_as_keys', 'input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_all_columns_as_keys', '_all_columns_as_keys', 'all_columns_as_keys', 'all_columns_as_keys', 'column_names', 'column_names', 'input', 'input']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_all_columns_as_keys', '_all_columns_as_keys']) -> typing_extensions.Literal['all_columns_as_keys'] | None: ...
global___Deduplicate = Deduplicate

class LocalRelation(google.protobuf.message.Message):
    """A relation that does not need to be qualified by name."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    schema: builtins.str
    def __init__(self, *, data: builtins.bytes | None = ..., schema: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_data', '_data', '_schema', '_schema', 'data', 'data', 'schema', 'schema']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_data', '_data', '_schema', '_schema', 'data', 'data', 'schema', 'schema']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_data', '_data']) -> typing_extensions.Literal['data'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_schema', '_schema']) -> typing_extensions.Literal['schema'] | None: ...
global___LocalRelation = LocalRelation

class Sample(google.protobuf.message.Message):
    """Relation of type [[Sample]] that samples a fraction of the dataset."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    LOWER_BOUND_FIELD_NUMBER: builtins.int
    UPPER_BOUND_FIELD_NUMBER: builtins.int
    WITH_REPLACEMENT_FIELD_NUMBER: builtins.int
    SEED_FIELD_NUMBER: builtins.int
    DETERMINISTIC_ORDER_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for a Sample."""
    lower_bound: builtins.float
    upper_bound: builtins.float
    with_replacement: builtins.bool
    seed: builtins.int
    deterministic_order: builtins.bool
    def __init__(self, *, input: global___Relation | None = ..., lower_bound: builtins.float = ..., upper_bound: builtins.float = ..., with_replacement: builtins.bool | None = ..., seed: builtins.int | None = ..., deterministic_order: builtins.bool = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_seed', '_seed', '_with_replacement', '_with_replacement', 'input', 'input', 'seed', 'seed', 'with_replacement', 'with_replacement']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_seed', '_seed', '_with_replacement', '_with_replacement', 'deterministic_order', 'deterministic_order', 'input', 'input', 'lower_bound', 'lower_bound', 'seed', 'seed', 'upper_bound', 'upper_bound', 'with_replacement', 'with_replacement']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_seed', '_seed']) -> typing_extensions.Literal['seed'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_with_replacement', '_with_replacement']) -> typing_extensions.Literal['with_replacement'] | None: ...
global___Sample = Sample

class Range(google.protobuf.message.Message):
    """Relation of type [[Range]] that generates a sequence of integers."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    NUM_PARTITIONS_FIELD_NUMBER: builtins.int
    start: builtins.int
    end: builtins.int
    step: builtins.int
    num_partitions: builtins.int
    def __init__(self, *, start: builtins.int | None = ..., end: builtins.int = ..., step: builtins.int = ..., num_partitions: builtins.int | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_num_partitions', '_num_partitions', '_start', '_start', 'num_partitions', 'num_partitions', 'start', 'start']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_num_partitions', '_num_partitions', '_start', '_start', 'end', 'end', 'num_partitions', 'num_partitions', 'start', 'start', 'step', 'step']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_num_partitions', '_num_partitions']) -> typing_extensions.Literal['num_partitions'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_start', '_start']) -> typing_extensions.Literal['start'] | None: ...
global___Range = Range

class SubqueryAlias(google.protobuf.message.Message):
    """Relation alias."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    ALIAS_FIELD_NUMBER: builtins.int
    QUALIFIER_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation of SubqueryAlias."""
    alias: builtins.str
    @property
    def qualifier(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) Qualifier of the alias."""
    def __init__(self, *, input: global___Relation | None = ..., alias: builtins.str = ..., qualifier: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['alias', 'alias', 'input', 'input', 'qualifier', 'qualifier']) -> None: ...
global___SubqueryAlias = SubqueryAlias

class Repartition(google.protobuf.message.Message):
    """Relation repartition."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    NUM_PARTITIONS_FIELD_NUMBER: builtins.int
    SHUFFLE_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation of Repartition."""
    num_partitions: builtins.int
    shuffle: builtins.bool
    def __init__(self, *, input: global___Relation | None = ..., num_partitions: builtins.int = ..., shuffle: builtins.bool | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_shuffle', '_shuffle', 'input', 'input', 'shuffle', 'shuffle']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_shuffle', '_shuffle', 'input', 'input', 'num_partitions', 'num_partitions', 'shuffle', 'shuffle']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_shuffle', '_shuffle']) -> typing_extensions.Literal['shuffle'] | None: ...
global___Repartition = Repartition

class ShowString(google.protobuf.message.Message):
    """Compose the string representing rows for output.
    It will invoke 'Dataset.showString' to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    NUM_ROWS_FIELD_NUMBER: builtins.int
    TRUNCATE_FIELD_NUMBER: builtins.int
    VERTICAL_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    num_rows: builtins.int
    truncate: builtins.int
    vertical: builtins.bool
    def __init__(self, *, input: global___Relation | None = ..., num_rows: builtins.int = ..., truncate: builtins.int = ..., vertical: builtins.bool = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'num_rows', 'num_rows', 'truncate', 'truncate', 'vertical', 'vertical']) -> None: ...
global___ShowString = ShowString

class StatSummary(google.protobuf.message.Message):
    """Computes specified statistics for numeric and string columns.
    It will invoke 'Dataset.summary' (same as 'StatFunctions.summary')
    to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    STATISTICS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def statistics(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) Statistics from to be computed.

        Available statistics are:
         count
         mean
         stddev
         min
         max
         arbitrary approximate percentiles specified as a percentage (e.g. 75%)
         count_distinct
         approx_count_distinct

        If no statistics are given, this function computes 'count', 'mean', 'stddev', 'min',
        'approximate quartiles' (percentiles at 25%, 50%, and 75%), and 'max'.
        """
    def __init__(self, *, input: global___Relation | None = ..., statistics: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'statistics', 'statistics']) -> None: ...
global___StatSummary = StatSummary

class StatDescribe(google.protobuf.message.Message):
    """Computes basic statistics for numeric and string columns, including count, mean, stddev, min,
    and max. If no columns are given, this function computes statistics for all numerical or
    string columns.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def cols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) Columns to compute statistics on."""
    def __init__(self, *, input: global___Relation | None = ..., cols: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['cols', 'cols', 'input', 'input']) -> None: ...
global___StatDescribe = StatDescribe

class StatCrosstab(google.protobuf.message.Message):
    """Computes a pair-wise frequency table of the given columns. Also known as a contingency table.
    It will invoke 'Dataset.stat.crosstab' (same as 'StatFunctions.crossTabulate')
    to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COL1_FIELD_NUMBER: builtins.int
    COL2_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    col1: builtins.str
    col2: builtins.str
    def __init__(self, *, input: global___Relation | None = ..., col1: builtins.str = ..., col2: builtins.str = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['col1', 'col1', 'col2', 'col2', 'input', 'input']) -> None: ...
global___StatCrosstab = StatCrosstab

class StatCov(google.protobuf.message.Message):
    """Calculate the sample covariance of two numerical columns of a DataFrame.
    It will invoke 'Dataset.stat.cov' (same as 'StatFunctions.calculateCov') to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COL1_FIELD_NUMBER: builtins.int
    COL2_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    col1: builtins.str
    col2: builtins.str
    def __init__(self, *, input: global___Relation | None = ..., col1: builtins.str = ..., col2: builtins.str = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['col1', 'col1', 'col2', 'col2', 'input', 'input']) -> None: ...
global___StatCov = StatCov

class StatCorr(google.protobuf.message.Message):
    """Calculates the correlation of two columns of a DataFrame. Currently only supports the Pearson
    Correlation Coefficient. It will invoke 'Dataset.stat.corr' (same as
    'StatFunctions.pearsonCorrelation') to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COL1_FIELD_NUMBER: builtins.int
    COL2_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    col1: builtins.str
    col2: builtins.str
    method: builtins.str
    def __init__(self, *, input: global___Relation | None = ..., col1: builtins.str = ..., col2: builtins.str = ..., method: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_method', '_method', 'input', 'input', 'method', 'method']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_method', '_method', 'col1', 'col1', 'col2', 'col2', 'input', 'input', 'method', 'method']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_method', '_method']) -> typing_extensions.Literal['method'] | None: ...
global___StatCorr = StatCorr

class StatApproxQuantile(google.protobuf.message.Message):
    """Calculates the approximate quantiles of numerical columns of a DataFrame.
    It will invoke 'Dataset.stat.approxQuantile' (same as 'StatFunctions.approxQuantile')
    to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLS_FIELD_NUMBER: builtins.int
    PROBABILITIES_FIELD_NUMBER: builtins.int
    RELATIVE_ERROR_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def cols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Required) The names of the numerical columns."""
    @property
    def probabilities(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """(Required) A list of quantile probabilities.

        Each number must belong to [0, 1].
        For example 0 is the minimum, 0.5 is the median, 1 is the maximum.
        """
    relative_error: builtins.float
    def __init__(self, *, input: global___Relation | None = ..., cols: collections.abc.Iterable[builtins.str] | None = ..., probabilities: collections.abc.Iterable[builtins.float] | None = ..., relative_error: builtins.float = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['cols', 'cols', 'input', 'input', 'probabilities', 'probabilities', 'relative_error', 'relative_error']) -> None: ...
global___StatApproxQuantile = StatApproxQuantile

class StatFreqItems(google.protobuf.message.Message):
    """Finding frequent items for columns, possibly with false positives.
    It will invoke 'Dataset.stat.freqItems' (same as 'StatFunctions.freqItems')
    to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLS_FIELD_NUMBER: builtins.int
    SUPPORT_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def cols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Required) The names of the columns to search frequent items in."""
    support: builtins.float
    def __init__(self, *, input: global___Relation | None = ..., cols: collections.abc.Iterable[builtins.str] | None = ..., support: builtins.float | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_support', '_support', 'input', 'input', 'support', 'support']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_support', '_support', 'cols', 'cols', 'input', 'input', 'support', 'support']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_support', '_support']) -> typing_extensions.Literal['support'] | None: ...
global___StatFreqItems = StatFreqItems

class StatSampleBy(google.protobuf.message.Message):
    """Returns a stratified sample without replacement based on the fraction
    given on each stratum.
    It will invoke 'Dataset.stat.freqItems' (same as 'StatFunctions.freqItems')
    to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Fraction(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        STRATUM_FIELD_NUMBER: builtins.int
        FRACTION_FIELD_NUMBER: builtins.int
        @property
        def stratum(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression.Literal:
            """(Required) The stratum."""
        fraction: builtins.float
        def __init__(self, *, stratum: pyspark.sql.connect.proto.expressions_pb2.Expression.Literal | None = ..., fraction: builtins.float = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['stratum', 'stratum']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['fraction', 'fraction', 'stratum', 'stratum']) -> None: ...
    INPUT_FIELD_NUMBER: builtins.int
    COL_FIELD_NUMBER: builtins.int
    FRACTIONS_FIELD_NUMBER: builtins.int
    SEED_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def col(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression:
        """(Required) The column that defines strata."""
    @property
    def fractions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StatSampleBy.Fraction]:
        """(Required) Sampling fraction for each stratum.

        If a stratum is not specified, we treat its fraction as zero.
        """
    seed: builtins.int
    def __init__(self, *, input: global___Relation | None = ..., col: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ..., fractions: collections.abc.Iterable[global___StatSampleBy.Fraction] | None = ..., seed: builtins.int | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_seed', '_seed', 'col', 'col', 'input', 'input', 'seed', 'seed']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_seed', '_seed', 'col', 'col', 'fractions', 'fractions', 'input', 'input', 'seed', 'seed']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_seed', '_seed']) -> typing_extensions.Literal['seed'] | None: ...
global___StatSampleBy = StatSampleBy

class NAFill(google.protobuf.message.Message):
    """Replaces null values.
    It will invoke 'Dataset.na.fill' (same as 'DataFrameNaFunctions.fill') to compute the results.
    Following 3 parameter combinations are supported:
     1, 'values' only contains 1 item, 'cols' is empty:
       replaces null values in all type-compatible columns.
     2, 'values' only contains 1 item, 'cols' is not empty:
       replaces null values in specified columns.
     3, 'values' contains more than 1 items, then 'cols' is required to have the same length:
       replaces each specified column with corresponding value.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLS_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def cols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) Optional list of column names to consider."""
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression.Literal]:
        """(Required) Values to replace null values with.

        Should contain at least 1 item.
        Only 4 data types are supported now: bool, long, double, string
        """
    def __init__(self, *, input: global___Relation | None = ..., cols: collections.abc.Iterable[builtins.str] | None = ..., values: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression.Literal] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['cols', 'cols', 'input', 'input', 'values', 'values']) -> None: ...
global___NAFill = NAFill

class NADrop(google.protobuf.message.Message):
    """Drop rows containing null values.
    It will invoke 'Dataset.na.drop' (same as 'DataFrameNaFunctions.drop') to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLS_FIELD_NUMBER: builtins.int
    MIN_NON_NULLS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def cols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) Optional list of column names to consider.

        When it is empty, all the columns in the input relation will be considered.
        """
    min_non_nulls: builtins.int
    def __init__(self, *, input: global___Relation | None = ..., cols: collections.abc.Iterable[builtins.str] | None = ..., min_non_nulls: builtins.int | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_min_non_nulls', '_min_non_nulls', 'input', 'input', 'min_non_nulls', 'min_non_nulls']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_min_non_nulls', '_min_non_nulls', 'cols', 'cols', 'input', 'input', 'min_non_nulls', 'min_non_nulls']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_min_non_nulls', '_min_non_nulls']) -> typing_extensions.Literal['min_non_nulls'] | None: ...
global___NADrop = NADrop

class NAReplace(google.protobuf.message.Message):
    """Replaces old values with the corresponding values.
    It will invoke 'Dataset.na.replace' (same as 'DataFrameNaFunctions.replace')
    to compute the results.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Replacement(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        OLD_VALUE_FIELD_NUMBER: builtins.int
        NEW_VALUE_FIELD_NUMBER: builtins.int
        @property
        def old_value(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression.Literal:
            """(Required) The old value.

            Only 4 data types are supported now: null, bool, double, string.
            """
        @property
        def new_value(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression.Literal:
            """(Required) The new value.

            Should be of the same data type with the old value.
            """
        def __init__(self, *, old_value: pyspark.sql.connect.proto.expressions_pb2.Expression.Literal | None = ..., new_value: pyspark.sql.connect.proto.expressions_pb2.Expression.Literal | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['new_value', 'new_value', 'old_value', 'old_value']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['new_value', 'new_value', 'old_value', 'old_value']) -> None: ...
    INPUT_FIELD_NUMBER: builtins.int
    COLS_FIELD_NUMBER: builtins.int
    REPLACEMENTS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def cols(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional) List of column names to consider.

        When it is empty, all the type-compatible columns in the input relation will be considered.
        """
    @property
    def replacements(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NAReplace.Replacement]:
        """(Optional) The value replacement mapping."""
    def __init__(self, *, input: global___Relation | None = ..., cols: collections.abc.Iterable[builtins.str] | None = ..., replacements: collections.abc.Iterable[global___NAReplace.Replacement] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['cols', 'cols', 'input', 'input', 'replacements', 'replacements']) -> None: ...
global___NAReplace = NAReplace

class ToDF(google.protobuf.message.Message):
    """Rename columns on the input relation by the same length of names."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    COLUMN_NAMES_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation of RenameColumnsBySameLengthNames."""
    @property
    def column_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Required)

        The number of columns of the input relation must be equal to the length
        of this field. If this is not true, an exception will be returned.
        """
    def __init__(self, *, input: global___Relation | None = ..., column_names: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['column_names', 'column_names', 'input', 'input']) -> None: ...
global___ToDF = ToDF

class WithColumnsRenamed(google.protobuf.message.Message):
    """Rename columns on the input relation by a map with name to name mapping."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class RenameColumnsMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(self, *, key: builtins.str = ..., value: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
    INPUT_FIELD_NUMBER: builtins.int
    RENAME_COLUMNS_MAP_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def rename_columns_map(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """(Required)

        Renaming column names of input relation from A to B where A is the map key
        and B is the map value. This is a no-op if schema doesn't contain any A. It
        does not require that all input relation column names to present as keys.
        duplicated B are not allowed.
        """
    def __init__(self, *, input: global___Relation | None = ..., rename_columns_map: collections.abc.Mapping[builtins.str, builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'rename_columns_map', 'rename_columns_map']) -> None: ...
global___WithColumnsRenamed = WithColumnsRenamed

class WithColumns(google.protobuf.message.Message):
    """Adding columns or replacing the existing columns that have the same names."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    ALIASES_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def aliases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression.Alias]:
        """(Required)

        Given a column name, apply the corresponding expression on the column. If column
        name exists in the input relation, then replace the column. If the column name
        does not exist in the input relation, then adds it as a new column.

        Only one name part is expected from each Expression.Alias.

        An exception is thrown when duplicated names are present in the mapping.
        """
    def __init__(self, *, input: global___Relation | None = ..., aliases: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression.Alias] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['aliases', 'aliases', 'input', 'input']) -> None: ...
global___WithColumns = WithColumns

class Hint(google.protobuf.message.Message):
    """Specify a hint over a relation. Hint should have a name and optional parameters."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    name: builtins.str
    @property
    def parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Optional) Hint parameters."""
    def __init__(self, *, input: global___Relation | None = ..., name: builtins.str = ..., parameters: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'name', 'name', 'parameters', 'parameters']) -> None: ...
global___Hint = Hint

class Unpivot(google.protobuf.message.Message):
    """Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Values(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        VALUES_FIELD_NUMBER: builtins.int
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]: ...
        def __init__(self, *, values: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['values', 'values']) -> None: ...
    INPUT_FIELD_NUMBER: builtins.int
    IDS_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    VARIABLE_COLUMN_NAME_FIELD_NUMBER: builtins.int
    VALUE_COLUMN_NAME_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Required) Id columns."""
    @property
    def values(self) -> global___Unpivot.Values:
        """(Optional) Value columns to unpivot."""
    variable_column_name: builtins.str
    value_column_name: builtins.str
    def __init__(self, *, input: global___Relation | None = ..., ids: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., values: global___Unpivot.Values | None = ..., variable_column_name: builtins.str = ..., value_column_name: builtins.str = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_values', '_values', 'input', 'input', 'values', 'values']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_values', '_values', 'ids', 'ids', 'input', 'input', 'value_column_name', 'value_column_name', 'values', 'values', 'variable_column_name', 'variable_column_name']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_values', '_values']) -> typing_extensions.Literal['values'] | None: ...
global___Unpivot = Unpivot

class ToSchema(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Required) The user provided schema.

        The Sever side will update the dataframe with this schema.
        """
    def __init__(self, *, input: global___Relation | None = ..., schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input', 'schema', 'schema']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'schema', 'schema']) -> None: ...
global___ToSchema = ToSchema

class RepartitionByExpression(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    PARTITION_EXPRS_FIELD_NUMBER: builtins.int
    NUM_PARTITIONS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    @property
    def partition_exprs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Required) The partitioning expressions."""
    num_partitions: builtins.int
    def __init__(self, *, input: global___Relation | None = ..., partition_exprs: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., num_partitions: builtins.int | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_num_partitions', '_num_partitions', 'input', 'input', 'num_partitions', 'num_partitions']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_num_partitions', '_num_partitions', 'input', 'input', 'num_partitions', 'num_partitions', 'partition_exprs', 'partition_exprs']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_num_partitions', '_num_partitions']) -> typing_extensions.Literal['num_partitions'] | None: ...
global___RepartitionByExpression = RepartitionByExpression

class MapPartitions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    FUNC_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for a mapPartitions-equivalent API: mapInPandas, mapInArrow."""
    @property
    def func(self) -> pyspark.sql.connect.proto.expressions_pb2.CommonInlineUserDefinedFunction:
        """(Required) Input user-defined function."""
    def __init__(self, *, input: global___Relation | None = ..., func: pyspark.sql.connect.proto.expressions_pb2.CommonInlineUserDefinedFunction | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['func', 'func', 'input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['func', 'func', 'input', 'input']) -> None: ...
global___MapPartitions = MapPartitions

class GroupMap(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    GROUPING_EXPRESSIONS_FIELD_NUMBER: builtins.int
    FUNC_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation for Group Map API: apply, applyInPandas."""
    @property
    def grouping_expressions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Required) Expressions for grouping keys."""
    @property
    def func(self) -> pyspark.sql.connect.proto.expressions_pb2.CommonInlineUserDefinedFunction:
        """(Required) Input user-defined function."""
    def __init__(self, *, input: global___Relation | None = ..., grouping_expressions: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., func: pyspark.sql.connect.proto.expressions_pb2.CommonInlineUserDefinedFunction | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['func', 'func', 'input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['func', 'func', 'grouping_expressions', 'grouping_expressions', 'input', 'input']) -> None: ...
global___GroupMap = GroupMap

class CoGroupMap(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    INPUT_GROUPING_EXPRESSIONS_FIELD_NUMBER: builtins.int
    OTHER_FIELD_NUMBER: builtins.int
    OTHER_GROUPING_EXPRESSIONS_FIELD_NUMBER: builtins.int
    FUNC_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) One input relation for CoGroup Map API - applyInPandas."""
    @property
    def input_grouping_expressions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """Expressions for grouping keys of the first input relation."""
    @property
    def other(self) -> global___Relation:
        """(Required) The other input relation."""
    @property
    def other_grouping_expressions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """Expressions for grouping keys of the other input relation."""
    @property
    def func(self) -> pyspark.sql.connect.proto.expressions_pb2.CommonInlineUserDefinedFunction:
        """(Required) Input user-defined function."""
    def __init__(self, *, input: global___Relation | None = ..., input_grouping_expressions: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., other: global___Relation | None = ..., other_grouping_expressions: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ..., func: pyspark.sql.connect.proto.expressions_pb2.CommonInlineUserDefinedFunction | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['func', 'func', 'input', 'input', 'other', 'other']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['func', 'func', 'input', 'input', 'input_grouping_expressions', 'input_grouping_expressions', 'other', 'other', 'other_grouping_expressions', 'other_grouping_expressions']) -> None: ...
global___CoGroupMap = CoGroupMap

class CollectMetrics(google.protobuf.message.Message):
    """Collect arbitrary (named) metrics from a dataset."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    METRICS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) The input relation."""
    name: builtins.str
    @property
    def metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression]:
        """(Required) The metric sequence."""
    def __init__(self, *, input: global___Relation | None = ..., name: builtins.str = ..., metrics: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['input', 'input', 'metrics', 'metrics', 'name', 'name']) -> None: ...
global___CollectMetrics = CollectMetrics

class Parse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _ParseFormat:
        ValueType: Incomplete
        V: typing_extensions.TypeAlias
    class _ParseFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Parse._ParseFormat.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PARSE_FORMAT_UNSPECIFIED: Parse._ParseFormat.ValueType
        PARSE_FORMAT_CSV: Parse._ParseFormat.ValueType
        PARSE_FORMAT_JSON: Parse._ParseFormat.ValueType
    class ParseFormat(_ParseFormat, metaclass=_ParseFormatEnumTypeWrapper): ...
    PARSE_FORMAT_UNSPECIFIED: Parse.ParseFormat.ValueType
    PARSE_FORMAT_CSV: Parse.ParseFormat.ValueType
    PARSE_FORMAT_JSON: Parse.ParseFormat.ValueType
    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(self, *, key: builtins.str = ..., value: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
    INPUT_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation:
        """(Required) Input relation to Parse. The input is expected to have single text column."""
    format: global___Parse.ParseFormat.ValueType
    @property
    def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Optional) DataType representing the schema. If not set, Spark will infer the schema."""
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Options for the csv/json parser. The map key is case insensitive."""
    def __init__(self, *, input: global___Relation | None = ..., format: global___Parse.ParseFormat.ValueType = ..., schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ..., options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_schema', '_schema', 'input', 'input', 'schema', 'schema']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_schema', '_schema', 'format', 'format', 'input', 'input', 'options', 'options', 'schema', 'schema']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_schema', '_schema']) -> typing_extensions.Literal['schema'] | None: ...
global___Parse = Parse
