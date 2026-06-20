from _typeshed import Incomplete
from gevent._compat import MAC as MAC, PYPY as PYPY, hostname_types as hostname_types, integer_types as integer_types, string_types as string_types, text_type as text_type
from gevent.resolver._addresses import is_ipv6_addr as is_ipv6_addr

class AbstractResolver:
    HOSTNAME_ENCODING: str
    EAI_NONAME_MSG: Incomplete
    EAI_FAMILY_MSG: str
    def close(self) -> None:
        """
        Release resources held by this object.

        Subclasses that define resources should override.

        .. versionadded:: 22.10.1
        """
    @staticmethod
    def fixup_gaierror(func): ...
    def gethostbyname(self, hostname, family=...): ...
    def gethostbyname_ex(self, hostname, family=...): ...
    def getaddrinfo(self, host, port, family: int = 0, socktype: int = 0, proto: int = 0, flags: int = 0): ...
    def gethostbyaddr(self, ip_address): ...
    def getnameinfo(self, sockaddr, flags): ...
