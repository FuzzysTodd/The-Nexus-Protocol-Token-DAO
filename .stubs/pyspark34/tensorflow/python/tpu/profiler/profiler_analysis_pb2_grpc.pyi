from _typeshed import Incomplete

class ProfileAnalysisStub:
    """//////////////////////////////////////////////////////////////////////////////

  ProfileAnalysis service provide entry point for profiling TPU and for
  serving profiled data to Tensorboard through GRPC
  //////////////////////////////////////////////////////////////////////////////
  """
    NewSession: Incomplete
    EnumSessions: Incomplete
    GetSessionToolData: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """

class ProfileAnalysisServicer:
    """//////////////////////////////////////////////////////////////////////////////

  ProfileAnalysis service provide entry point for profiling TPU and for
  serving profiled data to Tensorboard through GRPC
  //////////////////////////////////////////////////////////////////////////////
  """
    def NewSession(self, request, context) -> None:
        """Starts a profiling session, blocks until it completes.

    TPUProfileAnalysis service delegate this to TPUProfiler service.
    Populate the profiled data in repository, then return status to caller.
    """
    def EnumSessions(self, request, context) -> None:
        """Enumerate existing sessions and return available profile tools."""
    def GetSessionToolData(self, request, context) -> None:
        """Retrieve specific tool's data for specific session."""

def add_ProfileAnalysisServicer_to_server(servicer, server) -> None: ...
