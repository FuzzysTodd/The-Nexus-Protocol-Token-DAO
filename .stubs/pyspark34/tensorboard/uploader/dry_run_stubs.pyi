from _typeshed import Incomplete
from collections.abc import Generator
from tensorboard.uploader.proto import write_service_pb2 as write_service_pb2

class DryRunTensorBoardWriterStub:
    """A dry-run TensorBoardWriter gRPC Server.

    Only the methods used by the `tensorboard dev upload` are
    mocked out in this class.

    When additional methods start to be used by the command,
    their mocks should be added to this class.
    """
    def CreateExperiment(self, request, **kwargs):
        """Create a new experiment and remember it has been created."""
    def WriteScalar(self, request, **kwargs): ...
    def WriteTensor(self, request, **kwargs): ...
    def GetOrCreateBlobSequence(self, request, **kwargs): ...
    def WriteBlob(self, request, **kwargs) -> Generator[Incomplete, None, None]: ...
