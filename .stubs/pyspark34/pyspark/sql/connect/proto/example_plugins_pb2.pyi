import builtins
import google.protobuf.descriptor
import google.protobuf.message
import pyspark.sql.connect.proto.expressions_pb2
import pyspark.sql.connect.proto.relations_pb2
import typing as typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ExamplePluginRelation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INPUT_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> pyspark.sql.connect.proto.relations_pb2.Relation: ...
    custom_field: builtins.str
    def __init__(self, *, input: pyspark.sql.connect.proto.relations_pb2.Relation | None = ..., custom_field: builtins.str = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['input', 'input']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['custom_field', 'custom_field', 'input', 'input']) -> None: ...
global___ExamplePluginRelation = ExamplePluginRelation

class ExamplePluginExpression(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHILD_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_FIELD_NUMBER: builtins.int
    @property
    def child(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression: ...
    custom_field: builtins.str
    def __init__(self, *, child: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ..., custom_field: builtins.str = ...) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal['child', 'child']) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal['child', 'child', 'custom_field', 'custom_field']) -> None: ...
global___ExamplePluginExpression = ExamplePluginExpression

class ExamplePluginCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CUSTOM_FIELD_FIELD_NUMBER: builtins.int
    custom_field: builtins.str
    def __init__(self, *, custom_field: builtins.str = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['custom_field', 'custom_field']) -> None: ...
global___ExamplePluginCommand = ExamplePluginCommand
