from _typeshed import Incomplete
from tensorboard.plugins.mesh import metadata as metadata, plugin_data_pb2 as plugin_data_pb2, summary_v2 as summary_v2

mesh: Incomplete
mesh_pb: Incomplete

def op(name, vertices, faces: Incomplete | None = None, colors: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None, collections: Incomplete | None = None, config_dict: Incomplete | None = None):
    """Creates a TensorFlow summary op for mesh rendering.

    DEPRECATED: see `summary_v2.py` instead.

    Args:
      name: A name for this summary operation.
      vertices: Tensor of shape `[dim_1, ..., dim_n, 3]` representing the 3D
        coordinates of vertices.
      faces: Tensor of shape `[dim_1, ..., dim_n, 3]` containing indices of
        vertices within each triangle.
      colors: Tensor of shape `[dim_1, ..., dim_n, 3]` containing colors for each
        vertex.
      display_name: If set, will be used as the display name in TensorBoard.
        Defaults to `name`.
      description: A longform readable description of the summary data. Markdown
        is supported.
      collections: Which TensorFlow graph collections to add the summary op to.
        Defaults to `['summaries']`. Can usually be ignored.
      config_dict: Dictionary with ThreeJS classes names and configuration.

    Returns:
      Merged summary for mesh/point cloud representation.
    """
def pb(name, vertices, faces: Incomplete | None = None, colors: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None, config_dict: Incomplete | None = None):
    """Create a mesh summary to save in pb format.

    DEPRECATED: see `summary_v2.py` instead.

    Args:
      name: A name for this summary operation.
      vertices: numpy array of shape `[dim_1, ..., dim_n, 3]` representing the 3D
        coordinates of vertices.
      faces: numpy array of shape `[dim_1, ..., dim_n, 3]` containing indices of
        vertices within each triangle.
      colors: numpy array of shape `[dim_1, ..., dim_n, 3]` containing colors for
        each vertex.
      display_name: If set, will be used as the display name in TensorBoard.
        Defaults to `name`.
      description: A longform readable description of the summary data. Markdown
        is supported.
      config_dict: Dictionary with ThreeJS classes names and configuration.

    Returns:
      Instance of tf.Summary class.
    """
