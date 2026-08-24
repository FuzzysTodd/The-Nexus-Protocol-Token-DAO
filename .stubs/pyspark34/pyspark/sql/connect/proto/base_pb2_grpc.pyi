from _typeshed import Incomplete

class SparkConnectServiceStub:
    """Main interface for the SparkConnect service."""
    ExecutePlan: Incomplete
    AnalyzePlan: Incomplete
    Config: Incomplete
    AddArtifacts: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class SparkConnectServiceServicer:
    """Main interface for the SparkConnect service."""
    def ExecutePlan(self, request, context) -> None:
        """Executes a request that contains the query and returns a stream of [[Response]].

        It is guaranteed that there is at least one ARROW batch returned even if the result set is empty.
        """
    def AnalyzePlan(self, request, context) -> None:
        """Analyzes a query and returns a [[AnalyzeResponse]] containing metadata about the query."""
    def Config(self, request, context) -> None:
        """Update or fetch the configurations and returns a [[ConfigResponse]] containing the result."""
    def AddArtifacts(self, request_iterator, context) -> None:
        """Add artifacts to the session and returns a [[AddArtifactsResponse]] containing metadata about
        the added artifacts.
        """

def add_SparkConnectServiceServicer_to_server(servicer, server) -> None: ...

class SparkConnectService:
    """Main interface for the SparkConnect service."""
    @staticmethod
    def ExecutePlan(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def AnalyzePlan(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def Config(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def AddArtifacts(request_iterator, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
