from _typeshed import Incomplete
from tensorboard import errors as errors, plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.audio import metadata as metadata

class AudioPlugin(base_plugin.TBPlugin):
    """Audio Plugin for TensorBoard."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates AudioPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self): ...
    def frontend_metadata(self): ...
