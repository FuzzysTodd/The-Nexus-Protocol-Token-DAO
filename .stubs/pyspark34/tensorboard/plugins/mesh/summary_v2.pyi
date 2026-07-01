from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.mesh import metadata as metadata, plugin_data_pb2 as plugin_data_pb2
from tensorboard.util import tensor_util as tensor_util

def mesh(name, vertices, faces: Incomplete | None = None, colors: Incomplete | None = None, config_dict: Incomplete | None = None, step: Incomplete | None = None, description: Incomplete | None = None):
    """Writes a TensorFlow mesh summary.

    Args:
      name: A name for this summary. The summary tag used for TensorBoard will
        be this name prefixed by any active name scopes.
      vertices: Tensor of shape `[dim_1, ..., dim_n, 3]` representing the 3D
        coordinates of vertices.
      faces: Tensor of shape `[dim_1, ..., dim_n, 3]` containing indices of
        vertices within each triangle.
      colors: Tensor of shape `[dim_1, ..., dim_n, 3]` containing colors for each
        vertex.
      config_dict: Dictionary with ThreeJS classes names and configuration.
      step: Explicit `int64`-castable monotonic step value for this summary. If
        omitted, this defaults to `tf.summary.experimental.get_step()`, which must
        not be None.
      description: Optional long-form description for this summary, as a
        constant `str`. Markdown is supported. Defaults to empty.

    Returns:
      True if all components of the mesh were saved successfully and False
        otherwise.
    """
def mesh_pb(tag, vertices, faces: Incomplete | None = None, colors: Incomplete | None = None, config_dict: Incomplete | None = None, description: Incomplete | None = None):
    """Create a mesh summary to save in pb format.

    Args:
      tag: String tag for the summary.
      vertices: numpy array of shape `[dim_1, ..., dim_n, 3]` representing the 3D
        coordinates of vertices.
      faces: numpy array of shape `[dim_1, ..., dim_n, 3]` containing indices of
        vertices within each triangle.
      colors: numpy array of shape `[dim_1, ..., dim_n, 3]` containing colors for
        each vertex.
      config_dict: Dictionary with ThreeJS classes names and configuration.
      description: Optional long-form description for this summary, as a
        constant `str`. Markdown is supported. Defaults to empty.

    Returns:
      Instance of tf.Summary class.
    """
