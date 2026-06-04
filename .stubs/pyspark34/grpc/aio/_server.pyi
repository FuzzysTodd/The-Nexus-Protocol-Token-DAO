import grpc
from . import _base_server
from ._interceptor import ServerInterceptor as ServerInterceptor
from ._typing import ChannelArgumentType as ChannelArgumentType
from concurrent.futures import Executor
from grpc._cython import cygrpc as cygrpc
from typing import Any, Sequence

class Server(_base_server.Server):
    """Serves RPCs."""
    def __init__(self, thread_pool: Executor | None, generic_handlers: Sequence[grpc.GenericRpcHandler] | None, interceptors: Sequence[Any] | None, options: ChannelArgumentType, maximum_concurrent_rpcs: int | None, compression: grpc.Compression | None) -> None: ...
    def add_generic_rpc_handlers(self, generic_rpc_handlers: Sequence[grpc.GenericRpcHandler]) -> None:
        """Registers GenericRpcHandlers with this Server.

        This method is only safe to call before the server is started.

        Args:
          generic_rpc_handlers: A sequence of GenericRpcHandlers that will be
          used to service RPCs.
        """
    def add_insecure_port(self, address: str) -> int:
        """Opens an insecure port for accepting RPCs.

        This method may only be called before starting the server.

        Args:
          address: The address for which to open a port. If the port is 0,
            or not specified in the address, then the gRPC runtime will choose a port.

        Returns:
          An integer port on which the server will accept RPC requests.
        """
    def add_secure_port(self, address: str, server_credentials: grpc.ServerCredentials) -> int:
        """Opens a secure port for accepting RPCs.

        This method may only be called before starting the server.

        Args:
          address: The address for which to open a port.
            if the port is 0, or not specified in the address, then the gRPC
            runtime will choose a port.
          server_credentials: A ServerCredentials object.

        Returns:
          An integer port on which the server will accept RPC requests.
        """
    async def start(self) -> None:
        """Starts this Server.

        This method may only be called once. (i.e. it is not idempotent).
        """
    async def stop(self, grace: float | None) -> None:
        """Stops this Server.

        This method immediately stops the server from servicing new RPCs in
        all cases.

        If a grace period is specified, this method returns immediately and all
        RPCs active at the end of the grace period are aborted. If a grace
        period is not specified (by passing None for grace), all existing RPCs
        are aborted immediately and this method blocks until the last RPC
        handler terminates.

        This method is idempotent and may be called at any time. Passing a
        smaller grace value in a subsequent call will have the effect of
        stopping the Server sooner (passing None will have the effect of
        stopping the server immediately). Passing a larger grace value in a
        subsequent call will not have the effect of stopping the server later
        (i.e. the most restrictive grace value is used).

        Args:
          grace: A duration of time in seconds or None.
        """
    async def wait_for_termination(self, timeout: float | None = None) -> bool:
        """Block current coroutine until the server stops.

        This is an EXPERIMENTAL API.

        The wait will not consume computational resources during blocking, and
        it will block until one of the two following conditions are met:

        1) The server is stopped or terminated;
        2) A timeout occurs if timeout is not `None`.

        The timeout argument works in the same way as `threading.Event.wait()`.
        https://docs.python.org/3/library/threading.html#threading.Event.wait

        Args:
          timeout: A floating point number specifying a timeout for the
            operation in seconds.

        Returns:
          A bool indicates if the operation times out.
        """
    def __del__(self) -> None:
        """Schedules a graceful shutdown in current event loop.

        The Cython AioServer doesn't hold a ref-count to this class. It should
        be safe to slightly extend the underlying Cython object's life span.
        """

def server(migration_thread_pool: Executor | None = None, handlers: Sequence[grpc.GenericRpcHandler] | None = None, interceptors: Sequence[Any] | None = None, options: ChannelArgumentType | None = None, maximum_concurrent_rpcs: int | None = None, compression: grpc.Compression | None = None):
    """Creates a Server with which RPCs can be serviced.

    Args:
      migration_thread_pool: A futures.ThreadPoolExecutor to be used by the
        Server to execute non-AsyncIO RPC handlers for migration purpose.
      handlers: An optional list of GenericRpcHandlers used for executing RPCs.
        More handlers may be added by calling add_generic_rpc_handlers any time
        before the server is started.
      interceptors: An optional list of ServerInterceptor objects that observe
        and optionally manipulate the incoming RPCs before handing them over to
        handlers. The interceptors are given control in the order they are
        specified. This is an EXPERIMENTAL API.
      options: An optional list of key-value pairs (:term:`channel_arguments` in gRPC runtime)
        to configure the channel.
      maximum_concurrent_rpcs: The maximum number of concurrent RPCs this server
        will service before returning RESOURCE_EXHAUSTED status, or None to
        indicate no limit.
      compression: An element of grpc.compression, e.g.
        grpc.compression.Gzip. This compression algorithm will be used for the
        lifetime of the server unless overridden by set_compression.

    Returns:
      A Server object.
    """
