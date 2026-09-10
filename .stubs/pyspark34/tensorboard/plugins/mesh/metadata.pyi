import dataclasses
from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.mesh import plugin_data_pb2 as plugin_data_pb2
from typing import Any

PLUGIN_NAME: str

@dataclasses.dataclass(frozen=True)
class MeshTensor:
    """A mesh tensor.

    Attributes:
      data: Tensor of shape `[dim_1, ..., dim_n, 3]` representing the mesh data
        of one of the following:
          - 3D coordinates of vertices
          - Indices of vertices within each triangle
          - Colors for each vertex
      content_type: Type of the mesh plugin data content.
      data_type: Data type of the elements in the tensor.
    """
    data: Any
    content_type: plugin_data_pb2.MeshPluginData.ContentType
    data_type: Any
    def __init__(self, data, content_type, data_type) -> None: ...

def get_components_bitmask(content_types):
    """Creates bitmask for all existing components of the summary.

    Args:
      content_type: list of plugin_data_pb2.MeshPluginData.ContentType,
        representing all components related to the summary.
    Returns: bitmask based on passed tensors.
    """
def get_current_version():
    """Returns current verions of the proto."""
def get_instance_name(name, content_type):
    """Returns a unique instance name for a given summary related to the
    mesh."""
def create_summary_metadata(name, display_name, content_type, components, shape, description: Incomplete | None = None, json_config: Incomplete | None = None):
    """Creates summary metadata which defined at MeshPluginData proto.

    Arguments:
      name: Original merged (summaries of different types) summary name.
      display_name: The display name used in TensorBoard.
      content_type: Value from MeshPluginData.ContentType enum describing data.
      components: Bitmask representing present parts (vertices, colors, etc.) that
        belong to the summary.
      shape: list of dimensions sizes of the tensor.
      description: The description to show in TensorBoard.
      json_config: A string, JSON-serialized dictionary of ThreeJS classes
        configuration.

    Returns:
      A `summary_pb2.SummaryMetadata` protobuf object.
    """
def parse_plugin_metadata(content):
    """Parse summary metadata to a Python object.

    Arguments:
      content: The `content` field of a `SummaryMetadata` proto
        corresponding to the mesh plugin.

    Returns:
      A `MeshPluginData` protobuf object.
    Raises: Error if the version of the plugin is not supported.
    """
