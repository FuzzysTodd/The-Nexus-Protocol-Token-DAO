from tensorboard.plugins.hparams import metrics as metrics
from tensorboard.plugins.scalar import scalars_plugin as scalars_plugin

class Handler:
    """Handles a ListMetricEvals request."""
    def __init__(self, request_context, request, scalars_plugin_instance, experiment) -> None:
        """Constructor.

        Args:
            request_context: A tensorboard.context.RequestContext.
            request: A ListSessionGroupsRequest protobuf.
            scalars_plugin_instance: A scalars_plugin.ScalarsPlugin.
            experiment: A experiment ID, as a possibly-empty `str`.
        """
    def run(self):
        """Executes the request.

        Returns:
            An array of tuples representing the metric evaluations--each of the
            form (<wall time in secs>, <training step>, <metric value>).
        """
