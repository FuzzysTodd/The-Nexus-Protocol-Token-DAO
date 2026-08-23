from typing import Any

__all__ = ['load_scheduler']

class SchedulerError(Exception):
    """Raised when a known error occurs with wandb sweep scheduler."""

def load_scheduler(scheduler_type: str) -> Any: ...
