from _typeshed import Incomplete
from tornado import gen as gen
from tornado.concurrent import Future as Future
from tornado.ioloop import IOLoop as IOLoop
from tornado.netutil import Resolver as Resolver, is_valid_ip as is_valid_ip
from typing import Any, Generator, List, Tuple

class CaresResolver(Resolver):
    """Name resolver based on the c-ares library.

    This is a non-blocking and non-threaded resolver.  It may not produce the
    same results as the system resolver, but can be used for non-blocking
    resolution when threads cannot be used.

    ``pycares`` will not return a mix of ``AF_INET`` and ``AF_INET6`` when
    ``family`` is ``AF_UNSPEC``, so it is only recommended for use in
    ``AF_INET`` (i.e. IPv4).  This is the default for
    ``tornado.simple_httpclient``, but other libraries may default to
    ``AF_UNSPEC``.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.

    .. deprecated:: 6.2
       This class is deprecated and will be removed in Tornado 7.0. Use the default
       thread-based resolver instead.
    """
    io_loop: Incomplete
    channel: Incomplete
    fds: Incomplete
    def initialize(self) -> None: ...
    def resolve(self, host: str, port: int, family: int = 0) -> Generator[Any, Any, List[Tuple[int, Any]]]: ...
