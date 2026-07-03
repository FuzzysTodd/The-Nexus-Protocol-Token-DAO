from tensorboard.compat.proto import summary_pb2 as summary_pb2

CONFIG_SUMMARY_TAG: str
PLUGIN_NAME: str

def create_summary_metadata():
    """Create a `SummaryMetadata` proto for custom scalar plugin data.

    Returns:
      A `summary_pb2.SummaryMetadata` protobuf object.
    """
