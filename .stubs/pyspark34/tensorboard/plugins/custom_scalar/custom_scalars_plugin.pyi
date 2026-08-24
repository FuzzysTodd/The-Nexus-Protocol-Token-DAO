from _typeshed import Incomplete
from tensorboard import plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.compat import tf as tf
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.custom_scalar import layout_pb2 as layout_pb2, metadata as metadata
from tensorboard.plugins.scalar import scalars_plugin as scalars_plugin

class CustomScalarsPlugin(base_plugin.TBPlugin):
    """CustomScalars Plugin for TensorBoard."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates ScalarsPlugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self):
        """Plugin is active if there is a custom layout for the dashboard."""
    def frontend_metadata(self): ...
    def download_data_route(self, request): ...
    def download_data_impl(self, ctx, run, tag, experiment, response_format):
        """Provides a response for downloading scalars data for a data series.

        Args:
          ctx: A tensorboard.context.RequestContext value.
          run: The run.
          tag: The specific tag.
          experiment: An experiment ID, as a possibly-empty `str`.
          response_format: A string. One of the values of the OutputFormat enum
            of the scalar plugin.

        Raises:
          ValueError: If the scalars plugin is not registered.

        Returns:
          2 entities:
            - A JSON object response body.
            - A mime type (string) for the response.
        """
    def scalars_route(self, request):
        """Given a tag regex and single run, return ScalarEvents.

        This route takes 2 GET params:
        run: A run string to find tags for.
        tag: A string that is a regex used to find matching tags.
        The response is a JSON object:
        {
          // Whether the regular expression is valid. Also false if empty.
          regexValid: boolean,

          // An object mapping tag name to a list of ScalarEvents.
          payload: Object<string, ScalarEvent[]>,
        }
        """
    def scalars_impl(self, ctx, run, tag_regex_string, experiment):
        """Given a tag regex and single run, return ScalarEvents.

        Args:
          ctx: A tensorboard.context.RequestContext value.
          run: A run string.
          tag_regex_string: A regular expression that captures portions of tags.

        Raises:
          ValueError: if the scalars plugin is not registered.

        Returns:
          A dictionary that is the JSON-able response.
        """
    def layout_route(self, request):
        """Fetches the custom layout specified by the config file in the logdir.

        If more than 1 run contains a layout, this method merges the layouts by
        merging charts within individual categories. If 2 categories with the same
        name are found, the charts within are merged. The merging is based on the
        order of the runs to which the layouts are written.

        The response is a JSON object mirroring properties of the Layout proto if a
        layout for any run is found.

        The response is an empty object if no layout could be found.
        """
    def layout_impl(self, ctx, experiment): ...
