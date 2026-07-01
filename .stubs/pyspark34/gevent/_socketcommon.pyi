from _typeshed import Incomplete
from errno import EWOULDBLOCK
from gevent._compat import PY39 as PY39, exc_clear as exc_clear, integer_types as integer_types, string_types as string_types
from gevent._util import copy_globals as copy_globals
from gevent.timeout import Timeout as Timeout

__dns__: Incomplete
__extensions__: Incomplete
__imports__: Incomplete
EAGAIN = EWOULDBLOCK
GSENDAGAIN: Incomplete
wait: Incomplete
wait_read: Incomplete
wait_write: Incomplete
wait_readwrite: Incomplete

class cancel_wait_ex(error):
    def __init__(self) -> None: ...

def cancel_wait(watcher, error=...) -> None:
    """See :meth:`gevent.hub.Hub.cancel_wait`"""
def gethostbyname(hostname):
    """
    gethostbyname(host) -> address

    Return the IP address (a string of the form '255.255.255.255') for a host.

    .. seealso:: :doc:`/dns`
    """
def gethostbyname_ex(hostname):
    """
    gethostbyname_ex(host) -> (name, aliaslist, addresslist)

    Return the true host name, a list of aliases, and a list of IP addresses,
    for a host.  The host argument is a string giving a host name or IP number.
    Resolve host and port into list of address info entries.

    .. seealso:: :doc:`/dns`
    """
def getaddrinfo(host, port, family: int = 0, type: int = 0, proto: int = 0, flags: int = 0):
    """
    Resolve host and port into list of address info entries.

    Translate the host/port argument into a sequence of 5-tuples that contain
    all the necessary arguments for creating a socket connected to that service.
    host is a domain name, a string representation of an IPv4/v6 address or
    None. port is a string service name such as 'http', a numeric port number or
    None. By passing None as the value of host and port, you can pass NULL to
    the underlying C API.

    The family, type and proto arguments can be optionally specified in order to
    narrow the list of addresses returned. Passing zero as a value for each of
    these arguments selects the full range of results.

    .. seealso:: :doc:`/dns`
    """
def gethostbyaddr(ip_address):
    """
    gethostbyaddr(ip_address) -> (name, aliaslist, addresslist)

    Return the true host name, a list of aliases, and a list of IP addresses,
    for a host.  The host argument is a string giving a host name or IP number.

    .. seealso:: :doc:`/dns`
    """
def getnameinfo(sockaddr, flags):
    """
    getnameinfo(sockaddr, flags) -> (host, port)

    Get host and port for a sockaddr.

    .. seealso:: :doc:`/dns`
    """
def getfqdn(name: str = ''):
    """Get fully qualified domain name from name.

    An empty argument is interpreted as meaning the local host.

    First the hostname returned by gethostbyaddr() is checked, then
    possibly existing aliases. In case no FQDN is available, hostname
    from gethostname() is returned.

    .. versionchanged:: 23.7.0
       The IPv6 generic address '::' now returns the result of
       ``gethostname``, like the IPv4 address '0.0.0.0'.
    """

timeout_default: Incomplete

class SocketMixin:
    hub: Incomplete
    timeout: Incomplete
    def __init__(self) -> None: ...
    ref: Incomplete
    def settimeout(self, howlong) -> None: ...
    def gettimeout(self): ...
    def setblocking(self, flag) -> None: ...
    def shutdown(self, how) -> None: ...
    family: Incomplete
    type: Incomplete
    proto: Incomplete
    def fileno(self): ...
    def getsockname(self): ...
    def getpeername(self): ...
    def bind(self, address): ...
    def listen(self, *args): ...
    def getsockopt(self, *args): ...
    def setsockopt(self, *args): ...
    def ioctl(self, *args): ...
    def sleeptaskw(self, *args): ...
    def getblocking(self):
        """
        Returns whether the socket will approximate blocking
        behaviour.

        .. versionadded:: 1.3a2
            Added in Python 3.7.
        """
    def connect(self, address) -> None:
        """
        Connect to *address*.

        .. versionchanged:: 20.6.0
            If the host part of the address includes an IPv6 scope ID,
            it will be used instead of ignored, if the platform supplies
            :func:`socket.inet_pton`.
        """
    def connect_ex(self, address):
        """
        Connect to *address*, returning a result code.

        .. versionchanged:: 23.7.0
           No longer uses an overridden ``connect`` method on
           this object. Instead, like the standard library, this method always
           uses a non-replacable internal connection function.
        """
    def recv(self, *args): ...
    def recvfrom(self, *args): ...
    def recvfrom_into(self, *args): ...
    def recv_into(self, *args): ...
    def sendall(self, data, flags: int = 0): ...
    def sendto(self, *args): ...
    def send(self, data, flags: int = 0, timeout=...): ...
