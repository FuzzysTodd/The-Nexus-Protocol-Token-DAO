import logging
from optuna._experimental import experimental as experimental
from typing import Any

class _TqdmLoggingHandler(logging.StreamHandler):
    def emit(self, record: Any) -> None: ...

class _ProgressBar:
    """Progress Bar implementation for `Study.optimize` on the top of `tqdm`.

    Args:
        is_valid:
            Whether to show progress bars in `Study.optimize`.
        n_trials:
            The number of trials.
        timeout:
            Stop study after the given number of second(s).
    """
    def __init__(self, is_valid: bool, n_trials: int | None = None, timeout: float | None = None) -> None: ...
    def update(self, elapsed_seconds: float | None) -> None:
        """Update the progress bars if ``is_valid`` is ``True``.

        Args:
            elapsed_seconds:
                The time past since `Study.optimize` started.
        """
    def close(self) -> None:
        """Close progress bars."""
