from _typeshed import Incomplete
from xgboost import collective as collective
from xgboost.tracker import RabitTracker as RabitTracker

def get_class_name(cls):
    """
    Return the class name.
    """

class CommunicatorContext:
    """
    A context controlling collective communicator initialization and finalization.
    This isn't specificially necessary (note Part 3), but it is more understandable coding-wise.
    """
    args: Incomplete
    def __init__(self, context, **args) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

def get_logger(name, level: str = 'INFO'):
    """Gets a logger by name, or creates and configures it for the first time."""
