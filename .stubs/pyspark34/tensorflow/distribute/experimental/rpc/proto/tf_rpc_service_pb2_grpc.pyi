from _typeshed import Incomplete

class RpcServiceStub:
    """Missing associated documentation comment in .proto file."""
    Call: Incomplete
    List: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class RpcServiceServicer:
    """Missing associated documentation comment in .proto file."""
    def Call(self, request, context) -> None:
        """RPC for invoking a registered function on remote server.
        """
    def List(self, request, context) -> None:
        """RPC for listing available methods in a server.
        """

def add_RpcServiceServicer_to_server(servicer, server) -> None: ...

class RpcService:
    """Missing associated documentation comment in .proto file."""
    @staticmethod
    def Call(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def List(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
