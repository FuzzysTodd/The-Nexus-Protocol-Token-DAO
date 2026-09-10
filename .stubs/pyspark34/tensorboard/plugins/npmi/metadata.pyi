from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.npmi import plugin_data_pb2 as plugin_data_pb2

PLUGIN_NAME: str
PROTO_VERSION: int
ANNOTATIONS_TAG: str
METRICS_TAG: str
VALUES_TAG: str
EMBEDDINGS_TAG: str

def create_summary_metadata(description): ...
def parse_plugin_metadata(content):
    """Parse summary metadata to a Python object.
    Arguments:
      content: The `content` field of a `SummaryMetadata` proto
        corresponding to the scalar plugin.
    Returns:
      A `ScalarPluginData` protobuf object.
    """
