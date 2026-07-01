from _typeshed import Incomplete

class TensorBoardDataProviderStub:
    """Missing associated documentation comment in .proto file."""
    GetExperiment: Incomplete
    ListPlugins: Incomplete
    ListRuns: Incomplete
    ListScalars: Incomplete
    ReadScalars: Incomplete
    ListTensors: Incomplete
    ReadTensors: Incomplete
    ListBlobSequences: Incomplete
    ReadBlobSequences: Incomplete
    ReadBlob: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class TensorBoardDataProviderServicer:
    """Missing associated documentation comment in .proto file."""
    def GetExperiment(self, request, context) -> None:
        """Get metadata about an experiment.
        """
    def ListPlugins(self, request, context) -> None:
        """List plugins that have data for an experiment.
        """
    def ListRuns(self, request, context) -> None:
        """List runs within an experiment.
        """
    def ListScalars(self, request, context) -> None:
        """List metadata about scalar time series.
        """
    def ReadScalars(self, request, context) -> None:
        """Read data from scalar time series.
        """
    def ListTensors(self, request, context) -> None:
        """List metadata about tensor time series.
        """
    def ReadTensors(self, request, context) -> None:
        """Read data from tensor time series.
        """
    def ListBlobSequences(self, request, context) -> None:
        """List metadata about blob sequence time series.
        """
    def ReadBlobSequences(self, request, context) -> None:
        """Read blob references from blob sequence time series. See `ReadBlob` to read
        the actual blob data.
        """
    def ReadBlob(self, request, context) -> None:
        """Read data for a specific blob.
        """

def add_TensorBoardDataProviderServicer_to_server(servicer, server) -> None: ...

class TensorBoardDataProvider:
    """Missing associated documentation comment in .proto file."""
    @staticmethod
    def GetExperiment(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ListPlugins(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ListRuns(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ListScalars(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ReadScalars(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ListTensors(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ReadTensors(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ListBlobSequences(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ReadBlobSequences(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def ReadBlob(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
