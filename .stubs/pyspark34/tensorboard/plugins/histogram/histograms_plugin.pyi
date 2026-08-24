from _typeshed import Incomplete
from tensorboard import errors as errors, plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.histogram import metadata as metadata

class HistogramsPlugin(base_plugin.TBPlugin):
    """Histograms Plugin for TensorBoard.

    This supports both old-style summaries (created with TensorFlow ops
    that output directly to the `histo` field of the proto) and new-
    style summaries (as created by the
    `tensorboard.plugins.histogram.summary` module).
    """
    plugin_name: Incomplete
    SAMPLE_SIZE: int
    def __init__(self, context) -> None:
        """Instantiates HistogramsPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self): ...
    def index_impl(self, ctx, experiment):
        """Return {runName: {tagName: {displayName: ..., description:
        ...}}}."""
    def frontend_metadata(self): ...
    def histograms_impl(self, ctx, tag, run, experiment, downsample_to: Incomplete | None = None):
        """Result of the form `(body, mime_type)`.

        At most `downsample_to` events will be returned. If this value is
        `None`, then default downsampling will be performed.

        Raises:
          tensorboard.errors.PublicError: On invalid request.
        """
    def tags_route(self, request): ...
    def histograms_route(self, request):
        """Given a tag and single run, return array of histogram values."""
