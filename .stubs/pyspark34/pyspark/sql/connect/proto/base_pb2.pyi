import builtins
import collections.abc
import google
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import pyspark.sql.connect.proto.commands_pb2
import pyspark.sql.connect.proto.common_pb2
import pyspark.sql.connect.proto.expressions_pb2
import pyspark.sql.connect.proto.relations_pb2
import pyspark.sql.connect.proto.types_pb2
import typing
import typing as typing_extensions
from _typeshed import Incomplete

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Plan(google.protobuf.message.Message):
    """A [[Plan]] is the structure that carries the runtime information for the execution from the
    client to the server. A [[Plan]] can either be of the type [[Relation]] which is a reference
    to the underlying logical plan or it can be of the [[Command]] type that is used to execute
    commands on the server.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROOT_FIELD_NUMBER: builtins.int
    COMMAND_FIELD_NUMBER: builtins.int
    @property
    def root(self) -> pyspark.sql.connect.proto.relations_pb2.Relation: ...
    @property
    def command(self) -> pyspark.sql.connect.proto.commands_pb2.Command: ...
    def __init__(self, *, root: pyspark.sql.connect.proto.relations_pb2.Relation | None = ..., command: pyspark.sql.connect.proto.commands_pb2.Command | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['command', 'command', 'op_type', 'op_type', 'root', 'root']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['command', 'command', 'op_type', 'op_type', 'root', 'root']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['op_type', 'op_type']) -> typing_extensions.Literal['root', 'command'] | None: ...
global___Plan = Plan

class UserContext(google.protobuf.message.Message):
    """User Context is used to refer to one particular user session that is executing
    queries in the backend.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    EXTENSIONS_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    user_name: builtins.str
    @property
    def extensions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """To extend the existing user context message that is used to identify incoming requests,
        Spark Connect leverages the Any protobuf type that can be used to inject arbitrary other
        messages into this message. Extensions are stored as a `repeated` type to be able to
        handle multiple active extensions.
        """
    def __init__(self, *, user_id: builtins.str = ..., user_name: builtins.str = ..., extensions: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['extensions', 'extensions', 'user_id', 'user_id', 'user_name', 'user_name']) -> None: ...
global___UserContext = UserContext

class AnalyzePlanRequest(google.protobuf.message.Message):
    """Request to perform plan analyze, optionally to explain the plan."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Schema(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PLAN_FIELD_NUMBER: builtins.int
        @property
        def plan(self) -> global___Plan:
            """(Required) The logical plan to be analyzed."""
        def __init__(self, *, plan: global___Plan | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> None: ...
    class Explain(google.protobuf.message.Message):
        """Explains the input plan based on a configurable mode."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class _ExplainMode:
            ValueType: Incomplete
            V: typing_extensions.TypeAlias
        class _ExplainModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AnalyzePlanRequest.Explain._ExplainMode.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            EXPLAIN_MODE_UNSPECIFIED: AnalyzePlanRequest.Explain._ExplainMode.ValueType
            EXPLAIN_MODE_SIMPLE: AnalyzePlanRequest.Explain._ExplainMode.ValueType
            EXPLAIN_MODE_EXTENDED: AnalyzePlanRequest.Explain._ExplainMode.ValueType
            EXPLAIN_MODE_CODEGEN: AnalyzePlanRequest.Explain._ExplainMode.ValueType
            EXPLAIN_MODE_COST: AnalyzePlanRequest.Explain._ExplainMode.ValueType
            EXPLAIN_MODE_FORMATTED: AnalyzePlanRequest.Explain._ExplainMode.ValueType
        class ExplainMode(_ExplainMode, metaclass=_ExplainModeEnumTypeWrapper):
            """Plan explanation mode."""
        EXPLAIN_MODE_UNSPECIFIED: AnalyzePlanRequest.Explain.ExplainMode.ValueType
        EXPLAIN_MODE_SIMPLE: AnalyzePlanRequest.Explain.ExplainMode.ValueType
        EXPLAIN_MODE_EXTENDED: AnalyzePlanRequest.Explain.ExplainMode.ValueType
        EXPLAIN_MODE_CODEGEN: AnalyzePlanRequest.Explain.ExplainMode.ValueType
        EXPLAIN_MODE_COST: AnalyzePlanRequest.Explain.ExplainMode.ValueType
        EXPLAIN_MODE_FORMATTED: AnalyzePlanRequest.Explain.ExplainMode.ValueType
        PLAN_FIELD_NUMBER: builtins.int
        EXPLAIN_MODE_FIELD_NUMBER: builtins.int
        @property
        def plan(self) -> global___Plan:
            """(Required) The logical plan to be analyzed."""
        explain_mode: global___AnalyzePlanRequest.Explain.ExplainMode.ValueType
        def __init__(self, *, plan: global___Plan | None = ..., explain_mode: global___AnalyzePlanRequest.Explain.ExplainMode.ValueType = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['explain_mode', 'explain_mode', 'plan', 'plan']) -> None: ...
    class TreeString(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PLAN_FIELD_NUMBER: builtins.int
        @property
        def plan(self) -> global___Plan:
            """(Required) The logical plan to be analyzed."""
        def __init__(self, *, plan: global___Plan | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> None: ...
    class IsLocal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PLAN_FIELD_NUMBER: builtins.int
        @property
        def plan(self) -> global___Plan:
            """(Required) The logical plan to be analyzed."""
        def __init__(self, *, plan: global___Plan | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> None: ...
    class IsStreaming(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PLAN_FIELD_NUMBER: builtins.int
        @property
        def plan(self) -> global___Plan:
            """(Required) The logical plan to be analyzed."""
        def __init__(self, *, plan: global___Plan | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> None: ...
    class InputFiles(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PLAN_FIELD_NUMBER: builtins.int
        @property
        def plan(self) -> global___Plan:
            """(Required) The logical plan to be analyzed."""
        def __init__(self, *, plan: global___Plan | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> None: ...
    class SparkVersion(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        def __init__(self) -> None: ...
    class DDLParse(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        DDL_STRING_FIELD_NUMBER: builtins.int
        ddl_string: builtins.str
        def __init__(self, *, ddl_string: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['ddl_string', 'ddl_string']) -> None: ...
    class SameSemantics(google.protobuf.message.Message):
        """Returns `true` when the logical query plans  are equal and therefore return same results."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TARGET_PLAN_FIELD_NUMBER: builtins.int
        OTHER_PLAN_FIELD_NUMBER: builtins.int
        @property
        def target_plan(self) -> global___Plan:
            """(Required) The plan to be compared."""
        @property
        def other_plan(self) -> global___Plan:
            """(Required) The other plan to be compared."""
        def __init__(self, *, target_plan: global___Plan | None = ..., other_plan: global___Plan | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['other_plan', 'other_plan', 'target_plan', 'target_plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['other_plan', 'other_plan', 'target_plan', 'target_plan']) -> None: ...
    class SemanticHash(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PLAN_FIELD_NUMBER: builtins.int
        @property
        def plan(self) -> global___Plan:
            """(Required) The logical plan to get a hashCode."""
        def __init__(self, *, plan: global___Plan | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['plan', 'plan']) -> None: ...
    class Persist(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RELATION_FIELD_NUMBER: builtins.int
        STORAGE_LEVEL_FIELD_NUMBER: builtins.int
        @property
        def relation(self) -> pyspark.sql.connect.proto.relations_pb2.Relation:
            """(Required) The logical plan to persist."""
        @property
        def storage_level(self) -> pyspark.sql.connect.proto.common_pb2.StorageLevel:
            """(Optional) The storage level."""
        def __init__(self, *, relation: pyspark.sql.connect.proto.relations_pb2.Relation | None = ..., storage_level: pyspark.sql.connect.proto.common_pb2.StorageLevel | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_storage_level', '_storage_level', 'relation', 'relation', 'storage_level', 'storage_level']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_storage_level', '_storage_level', 'relation', 'relation', 'storage_level', 'storage_level']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_storage_level', '_storage_level']) -> typing_extensions.Literal['storage_level'] | None: ...
    class Unpersist(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RELATION_FIELD_NUMBER: builtins.int
        BLOCKING_FIELD_NUMBER: builtins.int
        @property
        def relation(self) -> pyspark.sql.connect.proto.relations_pb2.Relation:
            """(Required) The logical plan to unpersist."""
        blocking: builtins.bool
        def __init__(self, *, relation: pyspark.sql.connect.proto.relations_pb2.Relation | None = ..., blocking: builtins.bool | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_blocking', '_blocking', 'blocking', 'blocking', 'relation', 'relation']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_blocking', '_blocking', 'blocking', 'blocking', 'relation', 'relation']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_blocking', '_blocking']) -> typing_extensions.Literal['blocking'] | None: ...
    class GetStorageLevel(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RELATION_FIELD_NUMBER: builtins.int
        @property
        def relation(self) -> pyspark.sql.connect.proto.relations_pb2.Relation:
            """(Required) The logical plan to get the storage level."""
        def __init__(self, *, relation: pyspark.sql.connect.proto.relations_pb2.Relation | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['relation', 'relation']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['relation', 'relation']) -> None: ...
    SESSION_ID_FIELD_NUMBER: builtins.int
    USER_CONTEXT_FIELD_NUMBER: builtins.int
    CLIENT_TYPE_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    EXPLAIN_FIELD_NUMBER: builtins.int
    TREE_STRING_FIELD_NUMBER: builtins.int
    IS_LOCAL_FIELD_NUMBER: builtins.int
    IS_STREAMING_FIELD_NUMBER: builtins.int
    INPUT_FILES_FIELD_NUMBER: builtins.int
    SPARK_VERSION_FIELD_NUMBER: builtins.int
    DDL_PARSE_FIELD_NUMBER: builtins.int
    SAME_SEMANTICS_FIELD_NUMBER: builtins.int
    SEMANTIC_HASH_FIELD_NUMBER: builtins.int
    PERSIST_FIELD_NUMBER: builtins.int
    UNPERSIST_FIELD_NUMBER: builtins.int
    GET_STORAGE_LEVEL_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    @property
    def user_context(self) -> global___UserContext:
        """(Required) User context"""
    client_type: builtins.str
    @property
    def schema(self) -> global___AnalyzePlanRequest.Schema: ...
    @property
    def explain(self) -> global___AnalyzePlanRequest.Explain: ...
    @property
    def tree_string(self) -> global___AnalyzePlanRequest.TreeString: ...
    @property
    def is_local(self) -> global___AnalyzePlanRequest.IsLocal: ...
    @property
    def is_streaming(self) -> global___AnalyzePlanRequest.IsStreaming: ...
    @property
    def input_files(self) -> global___AnalyzePlanRequest.InputFiles: ...
    @property
    def spark_version(self) -> global___AnalyzePlanRequest.SparkVersion: ...
    @property
    def ddl_parse(self) -> global___AnalyzePlanRequest.DDLParse: ...
    @property
    def same_semantics(self) -> global___AnalyzePlanRequest.SameSemantics: ...
    @property
    def semantic_hash(self) -> global___AnalyzePlanRequest.SemanticHash: ...
    @property
    def persist(self) -> global___AnalyzePlanRequest.Persist: ...
    @property
    def unpersist(self) -> global___AnalyzePlanRequest.Unpersist: ...
    @property
    def get_storage_level(self) -> global___AnalyzePlanRequest.GetStorageLevel: ...
    def __init__(self, *, session_id: builtins.str = ..., user_context: global___UserContext | None = ..., client_type: builtins.str | None = ..., schema: global___AnalyzePlanRequest.Schema | None = ..., explain: global___AnalyzePlanRequest.Explain | None = ..., tree_string: global___AnalyzePlanRequest.TreeString | None = ..., is_local: global___AnalyzePlanRequest.IsLocal | None = ..., is_streaming: global___AnalyzePlanRequest.IsStreaming | None = ..., input_files: global___AnalyzePlanRequest.InputFiles | None = ..., spark_version: global___AnalyzePlanRequest.SparkVersion | None = ..., ddl_parse: global___AnalyzePlanRequest.DDLParse | None = ..., same_semantics: global___AnalyzePlanRequest.SameSemantics | None = ..., semantic_hash: global___AnalyzePlanRequest.SemanticHash | None = ..., persist: global___AnalyzePlanRequest.Persist | None = ..., unpersist: global___AnalyzePlanRequest.Unpersist | None = ..., get_storage_level: global___AnalyzePlanRequest.GetStorageLevel | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'analyze', 'analyze', 'client_type', 'client_type', 'ddl_parse', 'ddl_parse', 'explain', 'explain', 'get_storage_level', 'get_storage_level', 'input_files', 'input_files', 'is_local', 'is_local', 'is_streaming', 'is_streaming', 'persist', 'persist', 'same_semantics', 'same_semantics', 'schema', 'schema', 'semantic_hash', 'semantic_hash', 'spark_version', 'spark_version', 'tree_string', 'tree_string', 'unpersist', 'unpersist', 'user_context', 'user_context']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'analyze', 'analyze', 'client_type', 'client_type', 'ddl_parse', 'ddl_parse', 'explain', 'explain', 'get_storage_level', 'get_storage_level', 'input_files', 'input_files', 'is_local', 'is_local', 'is_streaming', 'is_streaming', 'persist', 'persist', 'same_semantics', 'same_semantics', 'schema', 'schema', 'semantic_hash', 'semantic_hash', 'session_id', 'session_id', 'spark_version', 'spark_version', 'tree_string', 'tree_string', 'unpersist', 'unpersist', 'user_context', 'user_context']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_client_type', '_client_type']) -> typing_extensions.Literal['client_type'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['analyze', 'analyze']) -> typing_extensions.Literal['schema', 'explain', 'tree_string', 'is_local', 'is_streaming', 'input_files', 'spark_version', 'ddl_parse', 'same_semantics', 'semantic_hash', 'persist', 'unpersist', 'get_storage_level'] | None: ...
global___AnalyzePlanRequest = AnalyzePlanRequest

class AnalyzePlanResponse(google.protobuf.message.Message):
    """Response to performing analysis of the query. Contains relevant metadata to be able to
    reason about the performance.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Schema(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        SCHEMA_FIELD_NUMBER: builtins.int
        @property
        def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType: ...
        def __init__(self, *, schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['schema', 'schema']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['schema', 'schema']) -> None: ...
    class Explain(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        EXPLAIN_STRING_FIELD_NUMBER: builtins.int
        explain_string: builtins.str
        def __init__(self, *, explain_string: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['explain_string', 'explain_string']) -> None: ...
    class TreeString(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TREE_STRING_FIELD_NUMBER: builtins.int
        tree_string: builtins.str
        def __init__(self, *, tree_string: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['tree_string', 'tree_string']) -> None: ...
    class IsLocal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        IS_LOCAL_FIELD_NUMBER: builtins.int
        is_local: builtins.bool
        def __init__(self, *, is_local: builtins.bool = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['is_local', 'is_local']) -> None: ...
    class IsStreaming(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        IS_STREAMING_FIELD_NUMBER: builtins.int
        is_streaming: builtins.bool
        def __init__(self, *, is_streaming: builtins.bool = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['is_streaming', 'is_streaming']) -> None: ...
    class InputFiles(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        FILES_FIELD_NUMBER: builtins.int
        @property
        def files(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """A best-effort snapshot of the files that compose this Dataset"""
        def __init__(self, *, files: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['files', 'files']) -> None: ...
    class SparkVersion(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        VERSION_FIELD_NUMBER: builtins.int
        version: builtins.str
        def __init__(self, *, version: builtins.str = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['version', 'version']) -> None: ...
    class DDLParse(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PARSED_FIELD_NUMBER: builtins.int
        @property
        def parsed(self) -> pyspark.sql.connect.proto.types_pb2.DataType: ...
        def __init__(self, *, parsed: pyspark.sql.connect.proto.types_pb2.DataType | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['parsed', 'parsed']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['parsed', 'parsed']) -> None: ...
    class SameSemantics(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RESULT_FIELD_NUMBER: builtins.int
        result: builtins.bool
        def __init__(self, *, result: builtins.bool = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['result', 'result']) -> None: ...
    class SemanticHash(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RESULT_FIELD_NUMBER: builtins.int
        result: builtins.int
        def __init__(self, *, result: builtins.int = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['result', 'result']) -> None: ...
    class Persist(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        def __init__(self) -> None: ...
    class Unpersist(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        def __init__(self) -> None: ...
    class GetStorageLevel(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        STORAGE_LEVEL_FIELD_NUMBER: builtins.int
        @property
        def storage_level(self) -> pyspark.sql.connect.proto.common_pb2.StorageLevel:
            """(Required) The StorageLevel as a result of get_storage_level request."""
        def __init__(self, *, storage_level: pyspark.sql.connect.proto.common_pb2.StorageLevel | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['storage_level', 'storage_level']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['storage_level', 'storage_level']) -> None: ...
    SESSION_ID_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    EXPLAIN_FIELD_NUMBER: builtins.int
    TREE_STRING_FIELD_NUMBER: builtins.int
    IS_LOCAL_FIELD_NUMBER: builtins.int
    IS_STREAMING_FIELD_NUMBER: builtins.int
    INPUT_FILES_FIELD_NUMBER: builtins.int
    SPARK_VERSION_FIELD_NUMBER: builtins.int
    DDL_PARSE_FIELD_NUMBER: builtins.int
    SAME_SEMANTICS_FIELD_NUMBER: builtins.int
    SEMANTIC_HASH_FIELD_NUMBER: builtins.int
    PERSIST_FIELD_NUMBER: builtins.int
    UNPERSIST_FIELD_NUMBER: builtins.int
    GET_STORAGE_LEVEL_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    @property
    def schema(self) -> global___AnalyzePlanResponse.Schema: ...
    @property
    def explain(self) -> global___AnalyzePlanResponse.Explain: ...
    @property
    def tree_string(self) -> global___AnalyzePlanResponse.TreeString: ...
    @property
    def is_local(self) -> global___AnalyzePlanResponse.IsLocal: ...
    @property
    def is_streaming(self) -> global___AnalyzePlanResponse.IsStreaming: ...
    @property
    def input_files(self) -> global___AnalyzePlanResponse.InputFiles: ...
    @property
    def spark_version(self) -> global___AnalyzePlanResponse.SparkVersion: ...
    @property
    def ddl_parse(self) -> global___AnalyzePlanResponse.DDLParse: ...
    @property
    def same_semantics(self) -> global___AnalyzePlanResponse.SameSemantics: ...
    @property
    def semantic_hash(self) -> global___AnalyzePlanResponse.SemanticHash: ...
    @property
    def persist(self) -> global___AnalyzePlanResponse.Persist: ...
    @property
    def unpersist(self) -> global___AnalyzePlanResponse.Unpersist: ...
    @property
    def get_storage_level(self) -> global___AnalyzePlanResponse.GetStorageLevel: ...
    def __init__(self, *, session_id: builtins.str = ..., schema: global___AnalyzePlanResponse.Schema | None = ..., explain: global___AnalyzePlanResponse.Explain | None = ..., tree_string: global___AnalyzePlanResponse.TreeString | None = ..., is_local: global___AnalyzePlanResponse.IsLocal | None = ..., is_streaming: global___AnalyzePlanResponse.IsStreaming | None = ..., input_files: global___AnalyzePlanResponse.InputFiles | None = ..., spark_version: global___AnalyzePlanResponse.SparkVersion | None = ..., ddl_parse: global___AnalyzePlanResponse.DDLParse | None = ..., same_semantics: global___AnalyzePlanResponse.SameSemantics | None = ..., semantic_hash: global___AnalyzePlanResponse.SemanticHash | None = ..., persist: global___AnalyzePlanResponse.Persist | None = ..., unpersist: global___AnalyzePlanResponse.Unpersist | None = ..., get_storage_level: global___AnalyzePlanResponse.GetStorageLevel | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['ddl_parse', 'ddl_parse', 'explain', 'explain', 'get_storage_level', 'get_storage_level', 'input_files', 'input_files', 'is_local', 'is_local', 'is_streaming', 'is_streaming', 'persist', 'persist', 'result', 'result', 'same_semantics', 'same_semantics', 'schema', 'schema', 'semantic_hash', 'semantic_hash', 'spark_version', 'spark_version', 'tree_string', 'tree_string', 'unpersist', 'unpersist']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['ddl_parse', 'ddl_parse', 'explain', 'explain', 'get_storage_level', 'get_storage_level', 'input_files', 'input_files', 'is_local', 'is_local', 'is_streaming', 'is_streaming', 'persist', 'persist', 'result', 'result', 'same_semantics', 'same_semantics', 'schema', 'schema', 'semantic_hash', 'semantic_hash', 'session_id', 'session_id', 'spark_version', 'spark_version', 'tree_string', 'tree_string', 'unpersist', 'unpersist']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['result', 'result']) -> typing_extensions.Literal['schema', 'explain', 'tree_string', 'is_local', 'is_streaming', 'input_files', 'spark_version', 'ddl_parse', 'same_semantics', 'semantic_hash', 'persist', 'unpersist', 'get_storage_level'] | None: ...
global___AnalyzePlanResponse = AnalyzePlanResponse

class ExecutePlanRequest(google.protobuf.message.Message):
    """A request to be executed by the service."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SESSION_ID_FIELD_NUMBER: builtins.int
    USER_CONTEXT_FIELD_NUMBER: builtins.int
    PLAN_FIELD_NUMBER: builtins.int
    CLIENT_TYPE_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    @property
    def user_context(self) -> global___UserContext:
        """(Required) User context

        user_context.user_id and session+id both identify a unique remote spark session on the
        server side.
        """
    @property
    def plan(self) -> global___Plan:
        """(Required) The logical plan to be executed / analyzed."""
    client_type: builtins.str
    def __init__(self, *, session_id: builtins.str = ..., user_context: global___UserContext | None = ..., plan: global___Plan | None = ..., client_type: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'client_type', 'client_type', 'plan', 'plan', 'user_context', 'user_context']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'client_type', 'client_type', 'plan', 'plan', 'session_id', 'session_id', 'user_context', 'user_context']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_client_type', '_client_type']) -> typing_extensions.Literal['client_type'] | None: ...
global___ExecutePlanRequest = ExecutePlanRequest

class ExecutePlanResponse(google.protobuf.message.Message):
    """The response of a query, can be one or more for each request. Responses belonging to the
    same input query, carry the same `session_id`.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class SqlCommandResult(google.protobuf.message.Message):
        """A SQL command returns an opaque Relation that can be directly used as input for the next
        call.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        RELATION_FIELD_NUMBER: builtins.int
        @property
        def relation(self) -> pyspark.sql.connect.proto.relations_pb2.Relation: ...
        def __init__(self, *, relation: pyspark.sql.connect.proto.relations_pb2.Relation | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['relation', 'relation']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['relation', 'relation']) -> None: ...
    class ArrowBatch(google.protobuf.message.Message):
        """Batch results of metrics."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ROW_COUNT_FIELD_NUMBER: builtins.int
        DATA_FIELD_NUMBER: builtins.int
        row_count: builtins.int
        data: builtins.bytes
        def __init__(self, *, row_count: builtins.int = ..., data: builtins.bytes = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['data', 'data', 'row_count', 'row_count']) -> None: ...
    class Metrics(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class MetricObject(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            class ExecutionMetricsEntry(google.protobuf.message.Message):
                DESCRIPTOR: google.protobuf.descriptor.Descriptor
                KEY_FIELD_NUMBER: builtins.int
                VALUE_FIELD_NUMBER: builtins.int
                key: builtins.str
                @property
                def value(self) -> global___ExecutePlanResponse.Metrics.MetricValue: ...
                def __init__(self, *, key: builtins.str = ..., value: global___ExecutePlanResponse.Metrics.MetricValue | None = ...) -> None: ...
                def HasField(self, field_name: typing_extensions.Literal['value', 'value']) -> builtins.bool: ...
                def ClearField(self, field_name: typing_extensions.Literal['key', 'key', 'value', 'value']) -> None: ...
            NAME_FIELD_NUMBER: builtins.int
            PLAN_ID_FIELD_NUMBER: builtins.int
            PARENT_FIELD_NUMBER: builtins.int
            EXECUTION_METRICS_FIELD_NUMBER: builtins.int
            name: builtins.str
            plan_id: builtins.int
            parent: builtins.int
            @property
            def execution_metrics(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___ExecutePlanResponse.Metrics.MetricValue]: ...
            def __init__(self, *, name: builtins.str = ..., plan_id: builtins.int = ..., parent: builtins.int = ..., execution_metrics: collections.abc.Mapping[builtins.str, global___ExecutePlanResponse.Metrics.MetricValue] | None = ...) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal['execution_metrics', 'execution_metrics', 'name', 'name', 'parent', 'parent', 'plan_id', 'plan_id']) -> None: ...
        class MetricValue(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            NAME_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            METRIC_TYPE_FIELD_NUMBER: builtins.int
            name: builtins.str
            value: builtins.int
            metric_type: builtins.str
            def __init__(self, *, name: builtins.str = ..., value: builtins.int = ..., metric_type: builtins.str = ...) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal['metric_type', 'metric_type', 'name', 'name', 'value', 'value']) -> None: ...
        METRICS_FIELD_NUMBER: builtins.int
        @property
        def metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExecutePlanResponse.Metrics.MetricObject]: ...
        def __init__(self, *, metrics: collections.abc.Iterable[global___ExecutePlanResponse.Metrics.MetricObject] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['metrics', 'metrics']) -> None: ...
    class ObservedMetrics(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        name: builtins.str
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pyspark.sql.connect.proto.expressions_pb2.Expression.Literal]: ...
        def __init__(self, *, name: builtins.str = ..., values: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression.Literal] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['name', 'name', 'values', 'values']) -> None: ...
    SESSION_ID_FIELD_NUMBER: builtins.int
    ARROW_BATCH_FIELD_NUMBER: builtins.int
    SQL_COMMAND_RESULT_FIELD_NUMBER: builtins.int
    EXTENSION_FIELD_NUMBER: builtins.int
    METRICS_FIELD_NUMBER: builtins.int
    OBSERVED_METRICS_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    @property
    def arrow_batch(self) -> global___ExecutePlanResponse.ArrowBatch: ...
    @property
    def sql_command_result(self) -> global___ExecutePlanResponse.SqlCommandResult:
        """Special case for executing SQL commands."""
    @property
    def extension(self) -> google.protobuf.any_pb2.Any:
        """Support arbitrary result objects."""
    @property
    def metrics(self) -> global___ExecutePlanResponse.Metrics:
        """Metrics for the query execution. Typically, this field is only present in the last
        batch of results and then represent the overall state of the query execution.
        """
    @property
    def observed_metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ExecutePlanResponse.ObservedMetrics]:
        """The metrics observed during the execution of the query plan."""
    @property
    def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Optional) The Spark schema. This field is available when `collect` is called."""
    def __init__(self, *, session_id: builtins.str = ..., arrow_batch: global___ExecutePlanResponse.ArrowBatch | None = ..., sql_command_result: global___ExecutePlanResponse.SqlCommandResult | None = ..., extension: google.protobuf.any_pb2.Any | None = ..., metrics: global___ExecutePlanResponse.Metrics | None = ..., observed_metrics: collections.abc.Iterable[global___ExecutePlanResponse.ObservedMetrics] | None = ..., schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['arrow_batch', 'arrow_batch', 'extension', 'extension', 'metrics', 'metrics', 'response_type', 'response_type', 'schema', 'schema', 'sql_command_result', 'sql_command_result']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['arrow_batch', 'arrow_batch', 'extension', 'extension', 'metrics', 'metrics', 'observed_metrics', 'observed_metrics', 'response_type', 'response_type', 'schema', 'schema', 'session_id', 'session_id', 'sql_command_result', 'sql_command_result']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['response_type', 'response_type']) -> typing_extensions.Literal['arrow_batch', 'sql_command_result', 'extension'] | None: ...
global___ExecutePlanResponse = ExecutePlanResponse

class KeyValue(google.protobuf.message.Message):
    """The key-value pair for the config request and response."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    value: builtins.str
    def __init__(self, *, key: builtins.str = ..., value: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_value', '_value', 'value', 'value']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_value', '_value', 'key', 'key', 'value', 'value']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_value', '_value']) -> typing_extensions.Literal['value'] | None: ...
global___KeyValue = KeyValue

class ConfigRequest(google.protobuf.message.Message):
    """Request to update or fetch the configurations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Operation(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        SET_FIELD_NUMBER: builtins.int
        GET_FIELD_NUMBER: builtins.int
        GET_WITH_DEFAULT_FIELD_NUMBER: builtins.int
        GET_OPTION_FIELD_NUMBER: builtins.int
        GET_ALL_FIELD_NUMBER: builtins.int
        UNSET_FIELD_NUMBER: builtins.int
        IS_MODIFIABLE_FIELD_NUMBER: builtins.int
        @property
        def set(self) -> global___ConfigRequest.Set: ...
        @property
        def get(self) -> global___ConfigRequest.Get: ...
        @property
        def get_with_default(self) -> global___ConfigRequest.GetWithDefault: ...
        @property
        def get_option(self) -> global___ConfigRequest.GetOption: ...
        @property
        def get_all(self) -> global___ConfigRequest.GetAll: ...
        @property
        def unset(self) -> global___ConfigRequest.Unset: ...
        @property
        def is_modifiable(self) -> global___ConfigRequest.IsModifiable: ...
        def __init__(self, *, set: global___ConfigRequest.Set | None = ..., get: global___ConfigRequest.Get | None = ..., get_with_default: global___ConfigRequest.GetWithDefault | None = ..., get_option: global___ConfigRequest.GetOption | None = ..., get_all: global___ConfigRequest.GetAll | None = ..., unset: global___ConfigRequest.Unset | None = ..., is_modifiable: global___ConfigRequest.IsModifiable | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['get', 'get', 'get_all', 'get_all', 'get_option', 'get_option', 'get_with_default', 'get_with_default', 'is_modifiable', 'is_modifiable', 'op_type', 'op_type', 'set', 'set', 'unset', 'unset']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['get', 'get', 'get_all', 'get_all', 'get_option', 'get_option', 'get_with_default', 'get_with_default', 'is_modifiable', 'is_modifiable', 'op_type', 'op_type', 'set', 'set', 'unset', 'unset']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['op_type', 'op_type']) -> typing_extensions.Literal['set', 'get', 'get_with_default', 'get_option', 'get_all', 'unset', 'is_modifiable'] | None: ...
    class Set(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PAIRS_FIELD_NUMBER: builtins.int
        @property
        def pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeyValue]:
            """(Required) The config key-value pairs to set."""
        def __init__(self, *, pairs: collections.abc.Iterable[global___KeyValue] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['pairs', 'pairs']) -> None: ...
    class Get(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEYS_FIELD_NUMBER: builtins.int
        @property
        def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) The config keys to get."""
        def __init__(self, *, keys: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['keys', 'keys']) -> None: ...
    class GetWithDefault(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PAIRS_FIELD_NUMBER: builtins.int
        @property
        def pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeyValue]:
            """(Required) The config key-value paris to get. The value will be used as the default value."""
        def __init__(self, *, pairs: collections.abc.Iterable[global___KeyValue] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['pairs', 'pairs']) -> None: ...
    class GetOption(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEYS_FIELD_NUMBER: builtins.int
        @property
        def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) The config keys to get optionally."""
        def __init__(self, *, keys: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['keys', 'keys']) -> None: ...
    class GetAll(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PREFIX_FIELD_NUMBER: builtins.int
        prefix: builtins.str
        def __init__(self, *, prefix: builtins.str | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['_prefix', '_prefix', 'prefix', 'prefix']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['_prefix', '_prefix', 'prefix', 'prefix']) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal['_prefix', '_prefix']) -> typing_extensions.Literal['prefix'] | None: ...
    class Unset(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEYS_FIELD_NUMBER: builtins.int
        @property
        def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) The config keys to unset."""
        def __init__(self, *, keys: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['keys', 'keys']) -> None: ...
    class IsModifiable(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEYS_FIELD_NUMBER: builtins.int
        @property
        def keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """(Required) The config keys to check the config is modifiable."""
        def __init__(self, *, keys: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['keys', 'keys']) -> None: ...
    SESSION_ID_FIELD_NUMBER: builtins.int
    USER_CONTEXT_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    CLIENT_TYPE_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    @property
    def user_context(self) -> global___UserContext:
        """(Required) User context"""
    @property
    def operation(self) -> global___ConfigRequest.Operation:
        """(Required) The operation for the config."""
    client_type: builtins.str
    def __init__(self, *, session_id: builtins.str = ..., user_context: global___UserContext | None = ..., operation: global___ConfigRequest.Operation | None = ..., client_type: builtins.str | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'client_type', 'client_type', 'operation', 'operation', 'user_context', 'user_context']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'client_type', 'client_type', 'operation', 'operation', 'session_id', 'session_id', 'user_context', 'user_context']) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_client_type', '_client_type']) -> typing_extensions.Literal['client_type'] | None: ...
global___ConfigRequest = ConfigRequest

class ConfigResponse(google.protobuf.message.Message):
    """Response to the config request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SESSION_ID_FIELD_NUMBER: builtins.int
    PAIRS_FIELD_NUMBER: builtins.int
    WARNINGS_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    @property
    def pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeyValue]:
        '''(Optional) The result key-value pairs.

        Available when the operation is \'Get\', \'GetWithDefault\', \'GetOption\', \'GetAll\'.
        Also available for the operation \'IsModifiable\' with boolean string "true" and "false".
        '''
    @property
    def warnings(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional)

        Warning messages for deprecated or unsupported configurations.
        """
    def __init__(self, *, session_id: builtins.str = ..., pairs: collections.abc.Iterable[global___KeyValue] | None = ..., warnings: collections.abc.Iterable[builtins.str] | None = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['pairs', 'pairs', 'session_id', 'session_id', 'warnings', 'warnings']) -> None: ...
global___ConfigResponse = ConfigResponse

class AddArtifactsRequest(google.protobuf.message.Message):
    """Request to transfer client-local artifacts."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ArtifactChunk(google.protobuf.message.Message):
        """A chunk of an Artifact."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        DATA_FIELD_NUMBER: builtins.int
        CRC_FIELD_NUMBER: builtins.int
        data: builtins.bytes
        crc: builtins.int
        def __init__(self, *, data: builtins.bytes = ..., crc: builtins.int = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['crc', 'crc', 'data', 'data']) -> None: ...
    class SingleChunkArtifact(google.protobuf.message.Message):
        """An artifact that is contained in a single `ArtifactChunk`.
        Generally, this message represents tiny artifacts such as REPL-generated class files.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        DATA_FIELD_NUMBER: builtins.int
        name: builtins.str
        @property
        def data(self) -> global___AddArtifactsRequest.ArtifactChunk:
            """A single data chunk."""
        def __init__(self, *, name: builtins.str = ..., data: global___AddArtifactsRequest.ArtifactChunk | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['data', 'data']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['data', 'data', 'name', 'name']) -> None: ...
    class Batch(google.protobuf.message.Message):
        """A number of `SingleChunkArtifact` batched into a single RPC."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ARTIFACTS_FIELD_NUMBER: builtins.int
        @property
        def artifacts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AddArtifactsRequest.SingleChunkArtifact]: ...
        def __init__(self, *, artifacts: collections.abc.Iterable[global___AddArtifactsRequest.SingleChunkArtifact] | None = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['artifacts', 'artifacts']) -> None: ...
    class BeginChunkedArtifact(google.protobuf.message.Message):
        """Signals the beginning/start of a chunked artifact.
        A large artifact is transferred through a payload of `BeginChunkedArtifact` followed by a
        sequence of `ArtifactChunk`s.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        TOTAL_BYTES_FIELD_NUMBER: builtins.int
        NUM_CHUNKS_FIELD_NUMBER: builtins.int
        INITIAL_CHUNK_FIELD_NUMBER: builtins.int
        name: builtins.str
        total_bytes: builtins.int
        num_chunks: builtins.int
        @property
        def initial_chunk(self) -> global___AddArtifactsRequest.ArtifactChunk:
            """The first/initial chunk."""
        def __init__(self, *, name: builtins.str = ..., total_bytes: builtins.int = ..., num_chunks: builtins.int = ..., initial_chunk: global___AddArtifactsRequest.ArtifactChunk | None = ...) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal['initial_chunk', 'initial_chunk']) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal['initial_chunk', 'initial_chunk', 'name', 'name', 'num_chunks', 'num_chunks', 'total_bytes', 'total_bytes']) -> None: ...
    SESSION_ID_FIELD_NUMBER: builtins.int
    USER_CONTEXT_FIELD_NUMBER: builtins.int
    CLIENT_TYPE_FIELD_NUMBER: builtins.int
    BATCH_FIELD_NUMBER: builtins.int
    BEGIN_CHUNK_FIELD_NUMBER: builtins.int
    CHUNK_FIELD_NUMBER: builtins.int
    session_id: builtins.str
    @property
    def user_context(self) -> global___UserContext:
        """User context"""
    client_type: builtins.str
    @property
    def batch(self) -> global___AddArtifactsRequest.Batch: ...
    @property
    def begin_chunk(self) -> global___AddArtifactsRequest.BeginChunkedArtifact:
        """The metadata and the initial chunk of a large artifact chunked into multiple requests.
        The server side is notified about the total size of the large artifact as well as the
        number of chunks to expect.
        """
    @property
    def chunk(self) -> global___AddArtifactsRequest.ArtifactChunk:
        """A chunk of an artifact excluding metadata. This can be any chunk of a large artifact
        excluding the first chunk (which is included in `BeginChunkedArtifact`).
        """
    def __init__(self, *, session_id: builtins.str = ..., user_context: global___UserContext | None = ..., client_type: builtins.str | None = ..., batch: global___AddArtifactsRequest.Batch | None = ..., begin_chunk: global___AddArtifactsRequest.BeginChunkedArtifact | None = ..., chunk: global___AddArtifactsRequest.ArtifactChunk | None = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'batch', 'batch', 'begin_chunk', 'begin_chunk', 'chunk', 'chunk', 'client_type', 'client_type', 'payload', 'payload', 'user_context', 'user_context']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['_client_type', '_client_type', 'batch', 'batch', 'begin_chunk', 'begin_chunk', 'chunk', 'chunk', 'client_type', 'client_type', 'payload', 'payload', 'session_id', 'session_id', 'user_context', 'user_context']) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_client_type', '_client_type']) -> typing_extensions.Literal['client_type'] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['payload', 'payload']) -> typing_extensions.Literal['batch', 'begin_chunk', 'chunk'] | None: ...
global___AddArtifactsRequest = AddArtifactsRequest

class AddArtifactsResponse(google.protobuf.message.Message):
    """Response to adding an artifact. Contains relevant metadata to verify successful transfer of
    artifact(s).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ArtifactSummary(google.protobuf.message.Message):
        """Metadata of an artifact."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        NAME_FIELD_NUMBER: builtins.int
        IS_CRC_SUCCESSFUL_FIELD_NUMBER: builtins.int
        name: builtins.str
        is_crc_successful: builtins.bool
        def __init__(self, *, name: builtins.str = ..., is_crc_successful: builtins.bool = ...) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal['is_crc_successful', 'is_crc_successful', 'name', 'name']) -> None: ...
    ARTIFACTS_FIELD_NUMBER: builtins.int
    @property
    def artifacts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AddArtifactsResponse.ArtifactSummary]:
        """The list of artifact(s) seen by the server."""
    def __init__(self, *, artifacts: collections.abc.Iterable[global___AddArtifactsResponse.ArtifactSummary] | None = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['artifacts', 'artifacts']) -> None: ...
global___AddArtifactsResponse = AddArtifactsResponse
