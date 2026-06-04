import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing as typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class StorageLevel(google.protobuf.message.Message):
    """StorageLevel for persisting Datasets/Tables."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USE_DISK_FIELD_NUMBER: builtins.int
    USE_MEMORY_FIELD_NUMBER: builtins.int
    USE_OFF_HEAP_FIELD_NUMBER: builtins.int
    DESERIALIZED_FIELD_NUMBER: builtins.int
    REPLICATION_FIELD_NUMBER: builtins.int
    use_disk: builtins.bool
    use_memory: builtins.bool
    use_off_heap: builtins.bool
    deserialized: builtins.bool
    replication: builtins.int
    def __init__(self, *, use_disk: builtins.bool = ..., use_memory: builtins.bool = ..., use_off_heap: builtins.bool = ..., deserialized: builtins.bool = ..., replication: builtins.int = ...) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal['deserialized', 'deserialized', 'replication', 'replication', 'use_disk', 'use_disk', 'use_memory', 'use_memory', 'use_off_heap', 'use_off_heap']) -> None: ...
global___StorageLevel = StorageLevel
