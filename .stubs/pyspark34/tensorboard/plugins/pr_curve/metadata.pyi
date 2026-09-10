from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.pr_curve import plugin_data_pb2 as plugin_data_pb2

PLUGIN_NAME: str
TRUE_POSITIVES_INDEX: int
FALSE_POSITIVES_INDEX: int
TRUE_NEGATIVES_INDEX: int
FALSE_NEGATIVES_INDEX: int
PRECISION_INDEX: int
RECALL_INDEX: int
PROTO_VERSION: int

def create_summary_metadata(display_name, description, num_thresholds):
    """Create a `summary_pb2.SummaryMetadata` proto for pr_curves plugin data.

    Arguments:
      display_name: The display name used in TensorBoard.
      description: The description to show in TensorBoard.
      num_thresholds: The number of thresholds to use for PR curves.

    Returns:
      A `summary_pb2.SummaryMetadata` protobuf object.
    """
def parse_plugin_metadata(content):
    """Parse summary metadata to a Python object.

    Arguments:
      content: The `content` field of a `SummaryMetadata` proto
        corresponding to the pr_curves plugin.

    Returns:
      A `PrCurvesPlugin` protobuf object.
    """
