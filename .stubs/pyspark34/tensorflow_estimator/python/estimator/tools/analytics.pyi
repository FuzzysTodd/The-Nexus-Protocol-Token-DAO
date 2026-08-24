def track_usage(tool_id, tags) -> None:
    """No usage tracking for external library.

  Args:
    tool_id: A string identifier for tool to be tracked.
    tags: list of string tags that will be added to the tracking.
  """
def track_numerical_issues(exc_info) -> None:
    """No tracking for external library.

  Args:
    exc_info: Output from `sys.exc_info` (type, value, traceback)
  """
