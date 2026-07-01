from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.audio import plugin_data_pb2 as plugin_data_pb2

PLUGIN_NAME: str
PROTO_VERSION: int
Encoding: Incomplete

def create_summary_metadata(display_name, description, encoding, *, converted_to_tensor: Incomplete | None = None):
    """Create a `SummaryMetadata` proto for audio plugin data.

    Returns:
      A `SummaryMetadata` protobuf object.
    """
def parse_plugin_metadata(content):
    """Parse summary metadata to a Python object.

    Arguments:
      content: The `content` field of a `SummaryMetadata` proto
        corresponding to the audio plugin.

    Returns:
      An `AudioPluginData` protobuf object.
    """
