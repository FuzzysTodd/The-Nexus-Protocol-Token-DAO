import contextlib
from _typeshed import Incomplete
from datetime import datetime
from functools import wraps as wraps
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from typing import Any, Tuple, Type, TypeVar

T = TypeVar('T')
PY2: Incomplete
PY33: Incomplete
PY37: Incomplete
PY310: Incomplete
PY311: Incomplete
text_type = str
string_types: Tuple[type]
number_types: Tuple[type, type]
int_types: Incomplete
iteritems: Incomplete
binary_sequence_types: Incomplete

def datetime_utcnow() -> datetime: ...
def utc_from_timestamp(timestamp: float) -> datetime: ...
def implements_str(x: T) -> T: ...
def reraise(tp: Type[BaseException] | None, value: BaseException | None, tb: Any | None = None) -> None: ...
contextmanager = contextlib.contextmanager

def with_metaclass(meta: Any, *bases: Any) -> Any: ...
def check_thread_support() -> None: ...
