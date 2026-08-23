from _typeshed import Incomplete
from tensorboard import errors as errors, plugin_util as plugin_util
from tensorboard.backend import http_util as http_util, process_graph as process_graph
from tensorboard.compat.proto import config_pb2 as config_pb2, graph_pb2 as graph_pb2
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.graph import graph_util as graph_util, keras_util as keras_util, metadata as metadata
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class GraphsPlugin(base_plugin.TBPlugin):
    """Graphs Plugin for TensorBoard."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates GraphsPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self):
        """The graphs plugin is active iff any run has a graph or metadata."""
    def data_plugin_names(self): ...
    def frontend_metadata(self): ...
    def info_impl(self, ctx, experiment: Incomplete | None = None):
        """Returns a dict of all runs and their data availabilities."""
    def graph_impl(self, ctx, run, tag, is_conceptual, experiment: Incomplete | None = None, limit_attr_size: Incomplete | None = None, large_attrs_key: Incomplete | None = None):
        """Result of the form `(body, mime_type)`; may raise `NotFound`."""
    def run_metadata_impl(self, ctx, experiment, run, tag):
        """Result of the form `(body, mime_type)`; may raise `NotFound`."""
    def info_route(self, request): ...
    def graph_route(self, request):
        """Given a single run, return the graph definition in protobuf
        format."""
    def run_metadata_route(self, request):
        """Given a tag and a run, return the session.run() metadata."""
