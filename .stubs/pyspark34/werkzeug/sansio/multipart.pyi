from ..datastructures import Headers as Headers
from ..exceptions import RequestEntityTooLarge as RequestEntityTooLarge
from ..http import parse_options_header as parse_options_header
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum

class Event: ...

@dataclass(frozen=True)
class Preamble(Event):
    data: bytes
    def __init__(self, data) -> None: ...

@dataclass(frozen=True)
class Field(Event):
    name: str
    headers: Headers
    def __init__(self, name, headers) -> None: ...

@dataclass(frozen=True)
class File(Event):
    name: str
    filename: str
    headers: Headers
    def __init__(self, name, filename, headers) -> None: ...

@dataclass(frozen=True)
class Data(Event):
    data: bytes
    more_data: bool
    def __init__(self, data, more_data) -> None: ...

@dataclass(frozen=True)
class Epilogue(Event):
    data: bytes
    def __init__(self, data) -> None: ...

class NeedData(Event): ...

NEED_DATA: Incomplete

class State(Enum):
    PREAMBLE: Incomplete
    PART: Incomplete
    DATA: Incomplete
    DATA_START: Incomplete
    EPILOGUE: Incomplete
    COMPLETE: Incomplete

LINE_BREAK: bytes
BLANK_LINE_RE: Incomplete
LINE_BREAK_RE: Incomplete
HEADER_CONTINUATION_RE: Incomplete
SEARCH_EXTRA_LENGTH: int

class MultipartDecoder:
    """Decodes a multipart message as bytes into Python events.

    The part data is returned as available to allow the caller to save
    the data from memory to disk, if desired.
    """
    buffer: Incomplete
    complete: bool
    max_form_memory_size: Incomplete
    max_parts: Incomplete
    state: Incomplete
    boundary: Incomplete
    preamble_re: Incomplete
    boundary_re: Incomplete
    def __init__(self, boundary: bytes, max_form_memory_size: int | None = None, *, max_parts: int | None = None) -> None: ...
    def last_newline(self, data: bytes) -> int: ...
    def receive_data(self, data: bytes | None) -> None: ...
    def next_event(self) -> Event: ...

class MultipartEncoder:
    boundary: Incomplete
    state: Incomplete
    def __init__(self, boundary: bytes) -> None: ...
    def send_event(self, event: Event) -> bytes: ...
