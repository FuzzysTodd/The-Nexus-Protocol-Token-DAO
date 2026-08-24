from _typeshed import Incomplete
from tensorboard import plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.distribution import compressor as compressor, metadata as metadata
from tensorboard.plugins.histogram import histograms_plugin as histograms_plugin

class DistributionsPlugin(base_plugin.TBPlugin):
    """Distributions Plugin for TensorBoard.

    This supports both old-style summaries (created with TensorFlow ops
    that output directly to the `histo` field of the proto) and new-
    style summaries (as created by the
    `tensorboard.plugins.histogram.summary` module).
    """
    plugin_name: Incomplete
    SAMPLE_SIZE: int
    def __init__(self, context) -> None:
        """Instantiates DistributionsPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self):
        """This plugin is active iff any run has at least one histogram tag.

        (The distributions plugin uses the same data source as the
        histogram plugin.)
        """
    def data_plugin_names(self): ...
    def frontend_metadata(self): ...
    def distributions_impl(self, ctx, tag, run, experiment):
        """Result of the form `(body, mime_type)`.

        Raises:
          tensorboard.errors.PublicError: On invalid request.
        """
    def index_impl(self, ctx, experiment): ...
    def tags_route(self, request): ...
    def distributions_route(self, request):
        """Given a tag and single run, return an array of compressed
        histograms."""
