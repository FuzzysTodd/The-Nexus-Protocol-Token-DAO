from _typeshed import Incomplete
from mdurl._url import URL as URL

PROTOCOL_PATTERN: Incomplete
PORT_PATTERN: Incomplete
SIMPLE_PATH_PATTERN: Incomplete
DELIMS: Incomplete
UNWISE: Incomplete
AUTO_ESCAPE: Incomplete
NON_HOST_CHARS: Incomplete
HOST_ENDING_CHARS: Incomplete
HOSTNAME_MAX_LEN: int
HOSTNAME_PART_PATTERN: Incomplete
HOSTNAME_PART_START: Incomplete
HOSTLESS_PROTOCOL: Incomplete
SLASHED_PROTOCOL: Incomplete

class MutableURL:
    protocol: Incomplete
    slashes: bool
    auth: Incomplete
    port: Incomplete
    hostname: Incomplete
    hash: Incomplete
    search: Incomplete
    pathname: Incomplete
    def __init__(self) -> None: ...
    def parse(self, url: str, slashes_denote_host: bool) -> MutableURL: ...
    def parse_host(self, host: str) -> None: ...

def url_parse(url: URL | str, *, slashes_denote_host: bool = False) -> URL: ...
