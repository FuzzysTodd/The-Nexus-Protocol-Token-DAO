from _typeshed import Incomplete
from collections.abc import Generator
from gevent._compat import iteritems as iteritems
from gevent.resolver._addresses import is_ipv4_addr as is_ipv4_addr, is_ipv6_addr as is_ipv6_addr

class HostsFile:
    """
    A class to read the contents of a hosts file (/etc/hosts).
    """
    LINES_RE: Incomplete
    v4: Incomplete
    v6: Incomplete
    aliases: Incomplete
    reverse: Incomplete
    fname: Incomplete
    def __init__(self, fname: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def iter_all_host_addr_pairs(self) -> Generator[Incomplete, None, None]: ...
