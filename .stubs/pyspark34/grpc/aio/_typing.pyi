from ._metadata import Metadata as Metadata, MetadataKey as MetadataKey, MetadataValue as MetadataValue
from _typeshed import Incomplete
from grpc._cython.cygrpc import EOF as EOF
from typing import Any, AsyncIterable, Callable, Iterable, Sequence, Tuple, TypeVar

RequestType = TypeVar('RequestType')
ResponseType = TypeVar('ResponseType')
SerializingFunction = Callable[[Any], bytes]
DeserializingFunction = Callable[[bytes], Any]
MetadatumType = Tuple[MetadataKey, MetadataValue]
MetadataType = Metadata | Sequence[MetadatumType]
ChannelArgumentType = Sequence[Tuple[str, Any]]
EOFType: Incomplete
DoneCallbackType = Callable[[Any], None]
RequestIterableType = Iterable[Any] | AsyncIterable[Any]
ResponseIterableType = AsyncIterable[Any]
