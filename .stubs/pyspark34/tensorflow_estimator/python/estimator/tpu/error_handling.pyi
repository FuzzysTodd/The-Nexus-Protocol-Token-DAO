from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow_estimator.python.estimator.tools import analytics as analytics

class ErrorRendezvous:
    '''Resolve errors from multiple threads during TPU execution.

  TPU errors can occur on the infeed or outfeed threads as well as the main
  training thread.

  Depending on which thread "wins" and receives the session error first, we may
  end up showing users a confusing and non-actionable error message (session
  cancelled) instead of a root cause (e.g. a bad filename).

  The rendezvous object provides a location to capture these errors until all
  threads terminate.  At that point we can choose the most informative error
  to report.
  '''
    def __init__(self, num_sources) -> None: ...
    def record_error(self, source, exc_info, session: Incomplete | None = None) -> None:
        """Report an exception from the given source.

    If a session is passed, a timer will be registered to close it after a few
    seconds.  This is necessary to ensure the main training loop does not hang
    if an infeed/oufeed error occurs.  We sleep a few seconds to allow a more
    interesting error from another thread to propagate.

    Args:
      source: string, source of the error
      exc_info: Output from `sys.exc_info` (type, value, traceback)
      session: Session to close after delay.
    """
    def record_done(self, source) -> None:
        """Mark execution source `source` as done.

    If an error was originally reported from `source` it is left intact.

    Args:
      source: `str`, source being recorded
    """
    def catch_errors(self, source, session: Incomplete | None = None) -> Generator[None, None, None]:
        """Context manager to report any errors within a block."""
    def raise_errors(self, timeout_sec: int = 0) -> None:
        '''Wait for up to `timeout` seconds for all error sources to finish.

    Preferentially raise "interesting" errors (errors not in the
    _UNINTERESTING_ERRORS) set.

    Args:
      timeout_sec: Seconds to wait for other error sources.
    '''
