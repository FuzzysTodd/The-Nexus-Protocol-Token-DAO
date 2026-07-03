from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.scalar import plugin_data_pb2 as plugin_data_pb2

PLUGIN_NAME: str
PROTO_VERSION: int

def create_summary_metadata(display_name, description):
    """Create a `summary_pb2.SummaryMetadata` proto for scalar plugin data.

    Returns:
      A `summary_pb2.SummaryMetadata` protobuf object.
    """
def parse_plugin_metadata(content):
    """Parse summary metadata to a Python object.

    Arguments:
      content: The `content` field of a `SummaryMetadata` proto
        corresponding to the scalar plugin.

    Returns:
      A `ScalarPluginData` protobuf object.
    """
