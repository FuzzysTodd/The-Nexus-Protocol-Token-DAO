from _typeshed import Incomplete
from tensorboard.compat.proto import event_pb2 as event_pb2
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

def ParseFileVersion(file_version: str) -> float:
    """Convert the string file_version in event.proto into a float.

    Args:
      file_version: String file_version from event.proto

    Returns:
      Version number as a float.
    """
def GetSourceWriter(source_metadata: event_pb2.SourceMetadata) -> str | None:
    """Gets the source writer name from the source metadata proto."""
