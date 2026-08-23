from _typeshed import Incomplete
from tensorboard import plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.data import provider as provider
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.pr_curve import metadata as metadata

class PrCurvesPlugin(base_plugin.TBPlugin):
    """A plugin that serves PR curves for individual classes."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates a PrCurvesPlugin.

        Args:
          context: A base_plugin.TBContext instance. A magic container that
            TensorBoard uses to make objects available to the plugin.
        """
    def pr_curves_route(self, request):
        """A route that returns a JSON mapping between runs and PR curve data.

        Returns:
          Given a tag and a comma-separated list of runs (both stored within GET
          parameters), fetches a JSON object that maps between run name and objects
          containing data required for PR curves for that run. Runs that either
          cannot be found or that lack tags will be excluded from the response.
        """
    def pr_curves_impl(self, ctx, experiment, runs, tag):
        """Creates the JSON object for the PR curves response for a run-tag
        combo.

        Arguments:
          runs: A list of runs to fetch the curves for.
          tag: The tag to fetch the curves for.

        Raises:
          ValueError: If no PR curves could be fetched for a run and tag.

        Returns:
          The JSON object for the PR curves route response.
        """
    def tags_route(self, request):
        """A route (HTTP handler) that returns a response with tags.

        Returns:
          A response that contains a JSON object. The keys of the object
          are all the runs. Each run is mapped to a (potentially empty) dictionary
          whose keys are tags associated with run and whose values are metadata
          (dictionaries).

          The metadata dictionaries contain 2 keys:
            - displayName: For the display name used atop visualizations in
                TensorBoard.
            - description: The description that appears near visualizations upon the
                user hovering over a certain icon.
        """
    def tags_impl(self, ctx, experiment):
        """Creates the JSON object for the tags route response.

        Returns:
          The JSON object for the tags route response.
        """
    def get_plugin_apps(self):
        """Gets all routes offered by the plugin.

        Returns:
          A dictionary mapping URL path to route that handles it.
        """
    def is_active(self): ...
    def frontend_metadata(self): ...
