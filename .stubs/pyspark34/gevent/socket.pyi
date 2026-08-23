from _typeshed import Incomplete
from gevent._compat import PY311 as PY311, exc_clear as exc_clear
from gevent._util import copy_globals as copy_globals

__implements__: Incomplete
__dns__: Incomplete
__extensions__: Incomplete
__imports__: Incomplete
class error(Exception):
    errno: Incomplete

def getfqdn(*args) -> None: ...
def create_connection(address, timeout=..., source_address: Incomplete | None = None, *, all_errors: bool = False):
    """
    create_connection(address, timeout=None, source_address=None, *, all_errors=False) -> socket

    Connect to *address* and return the :class:`gevent.socket.socket`
    object.

    Convenience function. Connect to *address* (a 2-tuple ``(host,
    port)``) and return the socket object. Passing the optional
    *timeout* parameter will set the timeout on the socket instance
    before attempting to connect. If no *timeout* is supplied, the
    global default timeout setting returned by
    :func:`getdefaulttimeout` is used. If *source_address* is set it
    must be a tuple of (host, port) for the socket to bind as a source
    address before making the connection. A host of '' or port 0 tells
    the OS to use the default.

    .. versionchanged:: 20.6.0
        If the host part of the address includes an IPv6 scope ID,
        it will be used instead of ignored, if the platform supplies
        :func:`socket.inet_pton`.
    .. versionchanged:: 22.08.0
        Add the *all_errors* argument. This only has meaning on Python 3.11+;
        it is a programming error to pass it on earlier versions.
    .. versionchanged:: 23.7.0
        You can pass a value for ``all_errors`` on any version of Python.
        It is forced to false for any version before 3.11 inside the function.
    """
