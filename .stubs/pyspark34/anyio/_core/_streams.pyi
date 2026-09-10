from ..streams.memory import MemoryObjectReceiveStream as MemoryObjectReceiveStream, MemoryObjectSendStream as MemoryObjectSendStream, MemoryObjectStreamState as MemoryObjectStreamState
from typing import Any, TypeVar, overload

T_Item = TypeVar('T_Item')

@overload
def create_memory_object_stream(max_buffer_size: float = ...) -> tuple[MemoryObjectSendStream[Any], MemoryObjectReceiveStream[Any]]: ...
@overload
def create_memory_object_stream(max_buffer_size: float = ..., item_type: type[T_Item] = ...) -> tuple[MemoryObjectSendStream[T_Item], MemoryObjectReceiveStream[T_Item]]: ...
