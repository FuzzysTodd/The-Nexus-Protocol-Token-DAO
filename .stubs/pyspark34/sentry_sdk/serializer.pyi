from _typeshed import Incomplete
from sentry_sdk._compat import PY2 as PY2, binary_sequence_types as binary_sequence_types, iteritems as iteritems, number_types as number_types, string_types as string_types, text_type as text_type
from sentry_sdk._types import Event as Event, NotImplementedType as NotImplementedType, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.utils import AnnotatedValue as AnnotatedValue, capture_internal_exception as capture_internal_exception, disable_capture_event as disable_capture_event, format_timestamp as format_timestamp, safe_repr as safe_repr, strip_string as strip_string
from types import TracebackType
from typing import Any, Callable, ContextManager, Dict, List, Type

Span = Dict[str, Any]
ReprProcessor = Callable[[Any, Dict[str, Any]], NotImplementedType | str]
Segment = str | int
serializable_str_types: Incomplete
MAX_EVENT_BYTES: Incomplete
MAX_DATABAG_DEPTH: int
MAX_DATABAG_BREADTH: int
CYCLE_MARKER: str
global_repr_processors: List[ReprProcessor]

def add_global_repr_processor(processor: ReprProcessor) -> None: ...

class Memo:
    def __init__(self) -> None: ...
    def memoize(self, obj: Any) -> ContextManager[bool]: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, ty: Type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> None: ...

def serialize(event: Event, **kwargs: Any) -> Event: ...
