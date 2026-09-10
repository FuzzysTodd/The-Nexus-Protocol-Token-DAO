class Handler:
    """Handles a GetExperiment request."""
    def __init__(self, request_context, backend_context, experiment_id) -> None:
        """Constructor.

        Args:
          request_context: A tensorboard.context.RequestContext.
          backend_context: A backend_context.Context instance.
          experiment_id: A string, as from `plugin_util.experiment_id`.
        """
    def run(self):
        """Handles the request specified on construction.

        Returns:
          An Experiment object.
        """
