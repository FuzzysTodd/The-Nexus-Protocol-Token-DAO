from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.image import plugin_data_pb2 as plugin_data_pb2

PLUGIN_NAME: str
PROTO_VERSION: int

def create_summary_metadata(display_name, description, *, converted_to_tensor: Incomplete | None = None):
    """Create a `summary_pb2.SummaryMetadata` proto for image plugin data.

    Returns:
      A `summary_pb2.SummaryMetadata` protobuf object.
    """
def parse_plugin_metadata(content):
    """Parse summary metadata to a Python object.

    Arguments:
      content: The `content` field of a `SummaryMetadata` proto
        corresponding to the image plugin.

    Returns:
      An `ImagePluginData` protobuf object.
    """
