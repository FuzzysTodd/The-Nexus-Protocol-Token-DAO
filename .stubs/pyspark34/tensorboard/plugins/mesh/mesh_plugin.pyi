from _typeshed import Incomplete
from tensorboard import plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.mesh import metadata as metadata, plugin_data_pb2 as plugin_data_pb2

class MeshPlugin(base_plugin.TBPlugin):
    """A plugin that serves 3D visualization of meshes."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates a MeshPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance. A magic container that
            TensorBoard uses to make objects available to the plugin.
        """
    def get_plugin_apps(self):
        """Gets all routes offered by the plugin.

        This method is called by TensorBoard when retrieving all the
        routes offered by the plugin.

        Returns:
          A dictionary mapping URL path to route that handles it.
        """
    def is_active(self): ...
    def frontend_metadata(self): ...
