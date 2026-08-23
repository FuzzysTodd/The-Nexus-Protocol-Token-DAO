from _typeshed import Incomplete

class ProfilerServiceStub:
    """The ProfilerService service retrieves performance information about
    the programs running on connected devices over a period of time.
    """
    Profile: Incomplete
    Terminate: Incomplete
    Monitor: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class ProfilerServiceServicer:
    """The ProfilerService service retrieves performance information about
    the programs running on connected devices over a period of time.
    """
    def Profile(self, request, context) -> None:
        """Starts a profiling session, blocks until it completes, and returns data.
        """
    def Terminate(self, request, context) -> None:
        """Signal to terminate the Profile rpc for a on-going profiling session,
        The Profile rpc will return successfully and prematurely without timeout.
        This is used by programmatic mode to end the session in workers.
        """
    def Monitor(self, request, context) -> None:
        """Collects profiling data and returns user-friendly metrics.
        """

def add_ProfilerServiceServicer_to_server(servicer, server) -> None: ...

class ProfilerService:
    """The ProfilerService service retrieves performance information about
    the programs running on connected devices over a period of time.
    """
    @staticmethod
    def Profile(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def Terminate(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def Monitor(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
