from _typeshed import Incomplete

class TensorBoardExporterServiceStub:
    """Service for exporting data from TensorBoard.dev.
    """
    StreamExperiments: Incomplete
    StreamExperimentData: Incomplete
    StreamBlobData: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class TensorBoardExporterServiceServicer:
    """Service for exporting data from TensorBoard.dev.
    """
    def StreamExperiments(self, request, context) -> None:
        """Stream the experiment_id of all the experiments owned by the caller.
        """
    def StreamExperimentData(self, request, context) -> None:
        """Stream scalars for all the runs and tags in an experiment.
        """
    def StreamBlobData(self, request, context) -> None:
        """Stream blob as chunks for a given blob_id.
        """

def add_TensorBoardExporterServiceServicer_to_server(servicer, server) -> None: ...

class TensorBoardExporterService:
    """Service for exporting data from TensorBoard.dev.
    """
    @staticmethod
    def StreamExperiments(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def StreamExperimentData(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def StreamBlobData(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
