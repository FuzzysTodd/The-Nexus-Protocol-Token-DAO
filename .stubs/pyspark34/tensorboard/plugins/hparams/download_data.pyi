from tensorboard.plugins.hparams import error as error

class OutputFormat:
    """An enum used to list the valid output formats for API calls."""
    JSON: str
    CSV: str
    LATEX: str

class Handler:
    """Handles a DownloadData request."""
    def __init__(self, context, experiment, session_groups, response_format, columns_visibility) -> None:
        """Constructor.

        Args:
          context: A backend_context.Context instance.
          experiment: Experiment proto.
          session_groups: ListSessionGroupsResponse proto.
          response_format: A string in the OutputFormat enum.
          columns_visibility: A list of boolean values to filter columns.
        """
    def run(self):
        """Handles the request specified on construction.

        Returns:
          A response body.
          A mime type (string) for the response.
        """
