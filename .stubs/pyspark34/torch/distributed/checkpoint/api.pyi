import traceback as tb
from typing import Dict, Tuple

__all__ = ['CheckpointException']

WRAPPED_EXCEPTION = Tuple[BaseException, tb.StackSummary]

class CheckpointException(BaseException):
    """
    Exception raised if failure was detected as part of a checkpoint load or save.
    """
    def __init__(self, msg: str, failures: Dict[int, WRAPPED_EXCEPTION]) -> None: ...
    @property
    def failures(self) -> Dict[int, WRAPPED_EXCEPTION]:
        """
        Returns:
            Dict of failed nodes and their associated exception.
              Keys are node ranks and values are exceptions
        """
