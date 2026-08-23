from _typeshed import Incomplete
from typing import Any, ClassVar

__all__ = ['StorageLevel']

class StorageLevel:
    """
    Flags for controlling the storage of an RDD. Each StorageLevel records whether to use memory,
    whether to drop the RDD to disk if it falls out of memory, whether to keep the data in memory
    in a JAVA-specific serialized format, and whether to replicate the RDD partitions on multiple
    nodes. Also contains static constants for some commonly used storage levels, MEMORY_ONLY.
    Since the data is always serialized on the Python side, all the constants use the serialized
    formats.
    """
    NONE: ClassVar['StorageLevel']
    DISK_ONLY: ClassVar['StorageLevel']
    DISK_ONLY_2: ClassVar['StorageLevel']
    DISK_ONLY_3: ClassVar['StorageLevel']
    MEMORY_ONLY: ClassVar['StorageLevel']
    MEMORY_ONLY_2: ClassVar['StorageLevel']
    MEMORY_AND_DISK: ClassVar['StorageLevel']
    MEMORY_AND_DISK_2: ClassVar['StorageLevel']
    OFF_HEAP: ClassVar['StorageLevel']
    MEMORY_AND_DISK_DESER: ClassVar['StorageLevel']
    useDisk: Incomplete
    useMemory: Incomplete
    useOffHeap: Incomplete
    deserialized: Incomplete
    replication: Incomplete
    def __init__(self, useDisk: bool, useMemory: bool, useOffHeap: bool, deserialized: bool, replication: int = 1) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
