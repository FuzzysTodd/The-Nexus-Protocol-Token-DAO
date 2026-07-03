from ..abc import ByteReceiveStream as ByteReceiveStream, ByteSendStream as ByteSendStream, ByteStream as ByteStream, Listener as Listener, ObjectReceiveStream as ObjectReceiveStream, ObjectSendStream as ObjectSendStream, ObjectStream as ObjectStream, TaskGroup as TaskGroup
from dataclasses import dataclass
from typing import Any, Callable, Generic, Mapping, Sequence, TypeVar

T_Item = TypeVar('T_Item')
T_Stream = TypeVar('T_Stream')

@dataclass(eq=False)
class StapledByteStream(ByteStream):
    """
    Combines two byte streams into a single, bidirectional byte stream.

    Extra attributes will be provided from both streams, with the receive stream providing the
    values in case of a conflict.

    :param ByteSendStream send_stream: the sending byte stream
    :param ByteReceiveStream receive_stream: the receiving byte stream
    """
    send_stream: ByteSendStream
    receive_stream: ByteReceiveStream
    async def receive(self, max_bytes: int = 65536) -> bytes: ...
    async def send(self, item: bytes) -> None: ...
    async def send_eof(self) -> None: ...
    async def aclose(self) -> None: ...
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...
    def __init__(self, send_stream, receive_stream) -> None: ...

@dataclass(eq=False)
class StapledObjectStream(ObjectStream[T_Item], Generic[T_Item]):
    """
    Combines two object streams into a single, bidirectional object stream.

    Extra attributes will be provided from both streams, with the receive stream providing the
    values in case of a conflict.

    :param ObjectSendStream send_stream: the sending object stream
    :param ObjectReceiveStream receive_stream: the receiving object stream
    """
    send_stream: ObjectSendStream[T_Item]
    receive_stream: ObjectReceiveStream[T_Item]
    async def receive(self) -> T_Item: ...
    async def send(self, item: T_Item) -> None: ...
    async def send_eof(self) -> None: ...
    async def aclose(self) -> None: ...
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...
    def __init__(self, send_stream, receive_stream) -> None: ...

@dataclass(eq=False)
class MultiListener(Listener[T_Stream], Generic[T_Stream]):
    """
    Combines multiple listeners into one, serving connections from all of them at once.

    Any MultiListeners in the given collection of listeners will have their listeners moved into
    this one.

    Extra attributes are provided from each listener, with each successive listener overriding any
    conflicting attributes from the previous one.

    :param listeners: listeners to serve
    :type listeners: Sequence[Listener[T_Stream]]
    """
    listeners: Sequence[Listener[T_Stream]]
    def __post_init__(self) -> None: ...
    async def serve(self, handler: Callable[[T_Stream], Any], task_group: TaskGroup | None = None) -> None: ...
    async def aclose(self) -> None: ...
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...
    def __init__(self, listeners) -> None: ...
