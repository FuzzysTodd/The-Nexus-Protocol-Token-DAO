from _typeshed import Incomplete
from tensorboard.backend.event_processing import data_provider as data_provider, plugin_event_multiplexer as plugin_event_multiplexer, tag_types as tag_types
from tensorboard.compat import tf as tf
from tensorboard.data import ingester as ingester
from tensorboard.util import tb_logging as tb_logging

DEFAULT_SIZE_GUIDANCE: Incomplete
DEFAULT_TENSOR_SIZE_GUIDANCE: Incomplete
logger: Incomplete

class LocalDataIngester(ingester.DataIngester):
    """Data ingestion implementation to use when running locally."""
    def __init__(self, flags) -> None:
        """Initializes a `LocalDataIngester` from `flags`.

        Args:
          flags: An argparse.Namespace containing TensorBoard CLI flags.

        Returns:
          The new `LocalDataIngester`.
        """
    @property
    def data_provider(self): ...
    @property
    def deprecated_multiplexer(self): ...
    def start(self) -> None:
        """Starts ingesting data based on the ingester flag configuration."""
