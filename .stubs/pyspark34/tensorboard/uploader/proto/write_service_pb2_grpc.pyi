from _typeshed import Incomplete

class TensorBoardWriterServiceStub:
    """Service for writing data to TensorBoard.dev.
    """
    CreateExperiment: Incomplete
    UpdateExperiment: Incomplete
    DeleteExperiment: Incomplete
    PurgeData: Incomplete
    WriteScalar: Incomplete
    WriteTensor: Incomplete
    GetOrCreateBlobSequence: Incomplete
    GetBlobMetadata: Incomplete
    WriteBlob: Incomplete
    DeleteOwnUser: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class TensorBoardWriterServiceServicer:
    """Service for writing data to TensorBoard.dev.
    """
    def CreateExperiment(self, request, context) -> None:
        """Request for a new location to write TensorBoard readable events.
        """
    def UpdateExperiment(self, request, context) -> None:
        """Request to mutate metadata associated with an experiment.
        """
    def DeleteExperiment(self, request, context) -> None:
        """Request that an experiment be deleted, along with all tags and scalars
        that it contains. This call may only be made by the original owner of the
        experiment.
        """
    def PurgeData(self, request, context) -> None:
        """Request that unreachable data be purged. Used only for testing;
        disabled in production.
        """
    def WriteScalar(self, request, context) -> None:
        """Request additional scalar data be stored in TensorBoard.dev.
        """
    def WriteTensor(self, request, context) -> None:
        """Request additional tensor data be stored in TensorBoard.dev.
        """
    def GetOrCreateBlobSequence(self, request, context) -> None:
        """Request to obtain a specific BlobSequence entry, creating it if needed,
        to be subsequently populated with blobs.
        """
    def GetBlobMetadata(self, request, context) -> None:
        """Request the current status of blob data being stored in TensorBoard.dev,
        to support resumable uploads.
        """
    def WriteBlob(self, request_iterator, context) -> None:
        """Request additional blob data be stored in TensorBoard.dev.
        """
    def DeleteOwnUser(self, request, context) -> None:
        """Request that the calling user and all their data be permanently deleted.
        Used for testing purposes.
        """

def add_TensorBoardWriterServiceServicer_to_server(servicer, server) -> None: ...

class TensorBoardWriterService:
    """Service for writing data to TensorBoard.dev.
    """
    @staticmethod
    def CreateExperiment(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def UpdateExperiment(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def DeleteExperiment(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def PurgeData(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def WriteScalar(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def WriteTensor(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def GetOrCreateBlobSequence(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def GetBlobMetadata(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def WriteBlob(request_iterator, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def DeleteOwnUser(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
