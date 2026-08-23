from _typeshed import Incomplete
from tensorboard import errors as errors, plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.metrics import metadata as metadata

class MetricsPlugin(base_plugin.TBPlugin):
    """Metrics Plugin for TensorBoard."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates MetricsPlugin.

        Args:
            context: A base_plugin.TBContext instance. MetricsLoader checks that
                it contains a valid `data_provider`.
        """
    def frontend_metadata(self): ...
    def get_plugin_apps(self): ...
    def data_plugin_names(self): ...
    def is_active(self): ...
