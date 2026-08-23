from _typeshed import Incomplete
from tensorboard import plugin_util as plugin_util, version as version
from tensorboard.backend import http_util as http_util
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.util import grpc_util as grpc_util, tb_logging as tb_logging

logger: Incomplete
DEFAULT_PORT: int
JS_MIMETYPES: Incomplete
JS_CACHE_EXPIRATION_IN_SECS: int

class CorePlugin(base_plugin.TBPlugin):
    """Core plugin for TensorBoard.

    This plugin serves runs, configuration data, and static assets. This
    plugin should always be present in a TensorBoard WSGI application.
    """
    plugin_name: str
    def __init__(self, context, include_debug_info: Incomplete | None = None) -> None:
        """Instantiates CorePlugin.

        Args:
          context: A base_plugin.TBContext instance.
          include_debug_info: If true, `/data/environment` will include some
            basic information like the TensorBoard server version. Disabled by
            default to prevent surprising information leaks in custom builds of
            TensorBoard.
        """
    def is_active(self): ...
    def get_plugin_apps(self): ...
    def get_resource_apps(self): ...
    def list_experiments_impl(self): ...

class CorePluginLoader(base_plugin.TBLoader):
    """CorePlugin factory."""
    def __init__(self, include_debug_info: Incomplete | None = None) -> None: ...
    def define_flags(self, parser):
        """Adds standard TensorBoard CLI flags to parser."""
    def fix_flags(self, flags) -> None:
        """Fixes standard TensorBoard CLI flags to parser."""
    def load(self, context):
        """Creates CorePlugin instance."""
