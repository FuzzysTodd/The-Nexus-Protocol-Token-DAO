import socket
import ssl
from _typeshed import Incomplete
from tornado import gen as gen, process as process
from tornado.ioloop import IOLoop as IOLoop
from tornado.iostream import IOStream as IOStream, SSLIOStream as SSLIOStream
from tornado.log import app_log as app_log
from tornado.netutil import add_accept_handler as add_accept_handler, bind_sockets as bind_sockets, ssl_wrap_socket as ssl_wrap_socket
from tornado.util import errno_from_exception as errno_from_exception
from typing import Any, Awaitable, Dict, Iterable

class TCPServer:
    '''A non-blocking, single-threaded TCP server.

    To use `TCPServer`, define a subclass which overrides the `handle_stream`
    method. For example, a simple echo server could be defined like this::

      from tornado.tcpserver import TCPServer
      from tornado.iostream import StreamClosedError

      class EchoServer(TCPServer):
          async def handle_stream(self, stream, address):
              while True:
                  try:
                      data = await stream.read_until(b"\\n") await
                      stream.write(data)
                  except StreamClosedError:
                      break

    To make this server serve SSL traffic, send the ``ssl_options`` keyword
    argument with an `ssl.SSLContext` object. For compatibility with older
    versions of Python ``ssl_options`` may also be a dictionary of keyword
    arguments for the `ssl.wrap_socket` method.::

       ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
       ssl_ctx.load_cert_chain(os.path.join(data_dir, "mydomain.crt"),
                               os.path.join(data_dir, "mydomain.key"))
       TCPServer(ssl_options=ssl_ctx)

    `TCPServer` initialization follows one of three patterns:

    1. `listen`: single-process::

            async def main():
                server = TCPServer()
                server.listen(8888)
                await asyncio.Event.wait()

            asyncio.run(main())

       While this example does not create multiple processes on its own, when
       the ``reuse_port=True`` argument is passed to ``listen()`` you can run
       the program multiple times to create a multi-process service.

    2. `add_sockets`: multi-process::

            sockets = bind_sockets(8888)
            tornado.process.fork_processes(0)
            async def post_fork_main():
                server = TCPServer()
                server.add_sockets(sockets)
                await asyncio.Event().wait()
            asyncio.run(post_fork_main())

       The `add_sockets` interface is more complicated, but it can be used with
       `tornado.process.fork_processes` to run a multi-process service with all
       worker processes forked from a single parent.  `add_sockets` can also be
       used in single-process servers if you want to create your listening
       sockets in some way other than `~tornado.netutil.bind_sockets`.

       Note that when using this pattern, nothing that touches the event loop
       can be run before ``fork_processes``.

    3. `bind`/`start`: simple **deprecated** multi-process::

            server = TCPServer()
            server.bind(8888)
            server.start(0)  # Forks multiple sub-processes
            IOLoop.current().start()

       This pattern is deprecated because it requires interfaces in the
       `asyncio` module that have been deprecated since Python 3.10. Support for
       creating multiple processes in the ``start`` method will be removed in a
       future version of Tornado.

    .. versionadded:: 3.1
       The ``max_buffer_size`` argument.

    .. versionchanged:: 5.0
       The ``io_loop`` argument has been removed.
    '''
    ssl_options: Incomplete
    max_buffer_size: Incomplete
    read_chunk_size: Incomplete
    def __init__(self, ssl_options: Dict[str, Any] | ssl.SSLContext | None = None, max_buffer_size: int | None = None, read_chunk_size: int | None = None) -> None: ...
    def listen(self, port: int, address: str | None = None, family: socket.AddressFamily = ..., backlog: int = ..., flags: int | None = None, reuse_port: bool = False) -> None:
        """Starts accepting connections on the given port.

        This method may be called more than once to listen on multiple ports.
        `listen` takes effect immediately; it is not necessary to call
        `TCPServer.start` afterwards.  It is, however, necessary to start the
        event loop if it is not already running.

        All arguments have the same meaning as in
        `tornado.netutil.bind_sockets`.

        .. versionchanged:: 6.2

           Added ``family``, ``backlog``, ``flags``, and ``reuse_port``
           arguments to match `tornado.netutil.bind_sockets`.
        """
    def add_sockets(self, sockets: Iterable[socket.socket]) -> None:
        """Makes this server start accepting connections on the given sockets.

        The ``sockets`` parameter is a list of socket objects such as
        those returned by `~tornado.netutil.bind_sockets`.
        `add_sockets` is typically used in combination with that
        method and `tornado.process.fork_processes` to provide greater
        control over the initialization of a multi-process server.
        """
    def add_socket(self, socket: socket.socket) -> None:
        """Singular version of `add_sockets`.  Takes a single socket object."""
    def bind(self, port: int, address: str | None = None, family: socket.AddressFamily = ..., backlog: int = ..., flags: int | None = None, reuse_port: bool = False) -> None:
        """Binds this server to the given port on the given address.

        To start the server, call `start`. If you want to run this server in a
        single process, you can call `listen` as a shortcut to the sequence of
        `bind` and `start` calls.

        Address may be either an IP address or hostname.  If it's a hostname,
        the server will listen on all IP addresses associated with the name.
        Address may be an empty string or None to listen on all available
        interfaces.  Family may be set to either `socket.AF_INET` or
        `socket.AF_INET6` to restrict to IPv4 or IPv6 addresses, otherwise both
        will be used if available.

        The ``backlog`` argument has the same meaning as for `socket.listen
        <socket.socket.listen>`. The ``reuse_port`` argument has the same
        meaning as for `.bind_sockets`.

        This method may be called multiple times prior to `start` to listen on
        multiple ports or interfaces.

        .. versionchanged:: 4.4
           Added the ``reuse_port`` argument.

        .. versionchanged:: 6.2
           Added the ``flags`` argument to match `.bind_sockets`.

        .. deprecated:: 6.2
           Use either ``listen()`` or ``add_sockets()`` instead of ``bind()``
           and ``start()``.
        """
    def start(self, num_processes: int | None = 1, max_restarts: int | None = None) -> None:
        """Starts this server in the `.IOLoop`.

        By default, we run the server in this process and do not fork any
        additional child process.

        If num_processes is ``None`` or <= 0, we detect the number of cores
        available on this machine and fork that number of child
        processes. If num_processes is given and > 1, we fork that
        specific number of sub-processes.

        Since we use processes and not threads, there is no shared memory
        between any server code.

        Note that multiple processes are not compatible with the autoreload
        module (or the ``autoreload=True`` option to `tornado.web.Application`
        which defaults to True when ``debug=True``).
        When using multiple processes, no IOLoops can be created or
        referenced until after the call to ``TCPServer.start(n)``.

        Values of ``num_processes`` other than 1 are not supported on Windows.

        The ``max_restarts`` argument is passed to `.fork_processes`.

        .. versionchanged:: 6.0

           Added ``max_restarts`` argument.

        .. deprecated:: 6.2
           Use either ``listen()`` or ``add_sockets()`` instead of ``bind()``
           and ``start()``.
        """
    def stop(self) -> None:
        """Stops listening for new connections.

        Requests currently in progress may still continue after the
        server is stopped.
        """
    def handle_stream(self, stream: IOStream, address: tuple) -> Awaitable[None] | None:
        """Override to handle a new `.IOStream` from an incoming connection.

        This method may be a coroutine; if so any exceptions it raises
        asynchronously will be logged. Accepting of incoming connections
        will not be blocked by this coroutine.

        If this `TCPServer` is configured for SSL, ``handle_stream``
        may be called before the SSL handshake has completed. Use
        `.SSLIOStream.wait_for_handshake` if you need to verify the client's
        certificate or use NPN/ALPN.

        .. versionchanged:: 4.2
           Added the option for this method to be a coroutine.
        """
