from _typeshed import Incomplete
from grpc import ServicerContext as ServicerContext
from grpc._cython import cygrpc as cygrpc
from typing import Any, Callable, Iterable, Sequence, Tuple, TypeVar

RequestType = TypeVar('RequestType')
ResponseType = TypeVar('ResponseType')
SerializingFunction = Callable[[Any], bytes]
DeserializingFunction = Callable[[bytes], Any]
MetadataType = Sequence[Tuple[str, str | bytes]]
ChannelArgumentType = Tuple[str, Any]
DoneCallbackType = Callable[[Any], None]
NullaryCallbackType = Callable[[], None]
RequestIterableType = Iterable[Any]
ResponseIterableType = Iterable[Any]
UserTag: Incomplete
IntegratedCallFactory: Incomplete
ServerTagCallbackType: Incomplete
ServerCallbackTag: Incomplete
ArityAgnosticMethodHandler: Incomplete
