from _typeshed import Incomplete
from tensorboard import context as context
from tensorboard.backend.event_processing import plugin_asset_util as plugin_asset_util
from tensorboard.backend.http_util import Respond as Respond
from tensorboard.compat import tf as tf
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.projector import metadata as metadata
from tensorboard.plugins.projector.projector_config_pb2 import ProjectorConfig as ProjectorConfig
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete
CONFIG_ROUTE: str
TENSOR_ROUTE: str
METADATA_ROUTE: str
RUNS_ROUTE: str
BOOKMARKS_ROUTE: str
SPRITE_IMAGE_ROUTE: str

class LRUCache:
    """LRU cache.

    Used for storing the last used tensor.
    """
    def __init__(self, size) -> None: ...
    def get(self, key): ...
    def set(self, key, value) -> None: ...

class EmbeddingMetadata:
    '''Metadata container for an embedding.

    The metadata holds different columns with values used for
    visualization (color by, label by) in the "Embeddings" tab in
    TensorBoard.
    '''
    num_points: Incomplete
    column_names: Incomplete
    name_to_values: Incomplete
    def __init__(self, num_points) -> None:
        """Constructs a metadata for an embedding of the specified size.

        Args:
          num_points: Number of points in the embedding.
        """
    def add_column(self, column_name, column_values) -> None:
        """Adds a named column of metadata values.

        Args:
          column_name: Name of the column.
          column_values: 1D array/list/iterable holding the column values. Must be
              of length `num_points`. The i-th value corresponds to the i-th point.

        Raises:
          ValueError: If `column_values` is not 1D array, or of length `num_points`,
              or the `name` is already used.
        """

class ProjectorPlugin(base_plugin.TBPlugin):
    """Embedding projector."""
    plugin_name: Incomplete
    data_provider: Incomplete
    logdir: Incomplete
    readers: Incomplete
    config_fpaths: Incomplete
    tensor_cache: Incomplete
    def __init__(self, context) -> None:
        """Instantiates ProjectorPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self):
        """Determines whether this plugin is active.

        This plugin is only active if any run has an embedding, and only
        when running against a local log directory.

        Returns:
          Whether any run has embedding data to show in the projector.
        """
    def frontend_metadata(self): ...
