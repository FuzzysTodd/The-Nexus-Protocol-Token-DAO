from _typeshed import Incomplete
from tensorboard.plugins.custom_scalar import layout_pb2 as layout_pb2, metadata as metadata

def op(scalars_layout, collections: Incomplete | None = None):
    """Creates a summary that contains a layout.

    When users navigate to the custom scalars dashboard, they will see a layout
    based on the proto provided to this function.

    Args:
      scalars_layout: The scalars_layout_pb2.Layout proto that specifies the
          layout.
      collections: Optional list of graph collections keys. The new
          summary op is added to these collections. Defaults to
          `[Graph Keys.SUMMARIES]`.

    Returns:
      A tensor summary op that writes the layout to disk.
    """
def pb(scalars_layout):
    """Creates a summary that contains a layout.

    When users navigate to the custom scalars dashboard, they will see a layout
    based on the proto provided to this function.

    Args:
      scalars_layout: The scalars_layout_pb2.Layout proto that specifies the
          layout.

    Returns:
      A summary proto containing the layout.
    """
