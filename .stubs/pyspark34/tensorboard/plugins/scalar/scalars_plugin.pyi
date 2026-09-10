from _typeshed import Incomplete
from tensorboard import errors as errors, plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.scalar import metadata as metadata

class OutputFormat:
    """An enum used to list the valid output formats for API calls."""
    JSON: str
    CSV: str

class ScalarsPlugin(base_plugin.TBPlugin):
    """Scalars Plugin for TensorBoard."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates ScalarsPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self): ...
    def frontend_metadata(self): ...
    def index_impl(self, ctx, experiment: Incomplete | None = None):
        """Return {runName: {tagName: {displayName: ..., description:
        ...}}}."""
    def scalars_impl(self, ctx, tag, run, experiment, output_format):
        """Result of the form `(body, mime_type)`."""
    def scalars_multirun_impl(self, ctx, tag, runs, experiment):
        """Result of the form `(body, mime_type)`."""
    def tags_route(self, request): ...
    def scalars_route(self, request):
        """Given a tag and single run, return array of ScalarEvents."""
    def scalars_multirun_route(self, request):
        """Given a tag and list of runs, return dict of ScalarEvent arrays."""
