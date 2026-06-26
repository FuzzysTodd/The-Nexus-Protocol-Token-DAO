from ._abnf import field_name as field_name, field_value as field_value
from ._events import Request as Request
from ._util import LocalProtocolError as LocalProtocolError, bytesify as bytesify, validate as validate
from typing import List, Sequence, Tuple, overload
from typing_extensions import Literal

class Headers(Sequence[Tuple[bytes, bytes]]):
    '''
    A list-like interface that allows iterating over headers as byte-pairs
    of (lowercased-name, value).

    Internally we actually store the representation as three-tuples,
    including both the raw original casing, in order to preserve casing
    over-the-wire, and the lowercased name, for case-insensitive comparisions.

    r = Request(
        method="GET",
        target="/",
        headers=[("Host", "example.org"), ("Connection", "keep-alive")],
        http_version="1.1",
    )
    assert r.headers == [
        (b"host", b"example.org"),
        (b"connection", b"keep-alive")
    ]
    assert r.headers.raw_items() == [
        (b"Host", b"example.org"),
        (b"Connection", b"keep-alive")
    ]
    '''
    def __init__(self, full_items: List[Tuple[bytes, bytes, bytes]]) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx: int) -> Tuple[bytes, bytes]: ...
    def raw_items(self) -> List[Tuple[bytes, bytes]]: ...
HeaderTypes = List[Tuple[bytes, bytes]] | List[Tuple[bytes, str]] | List[Tuple[str, bytes]] | List[Tuple[str, str]]

@overload
def normalize_and_validate(headers: Headers, _parsed: Literal[True]) -> Headers: ...
@overload
def normalize_and_validate(headers: HeaderTypes, _parsed: Literal[False]) -> Headers: ...
@overload
def normalize_and_validate(headers: Headers | HeaderTypes, _parsed: bool = False) -> Headers: ...
def get_comma_header(headers: Headers, name: bytes) -> List[bytes]: ...
def set_comma_header(headers: Headers, name: bytes, new_values: List[bytes]) -> Headers: ...
def has_expect_100_continue(request: Request) -> bool: ...
