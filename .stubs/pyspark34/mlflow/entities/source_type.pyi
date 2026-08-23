from _typeshed import Incomplete

class SourceType:
    """Enum for originating source of a :py:class:`mlflow.entities.Run`."""
    NOTEBOOK: Incomplete
    JOB: Incomplete
    PROJECT: Incomplete
    LOCAL: Incomplete
    UNKNOWN: Incomplete
    RECIPE: Incomplete
    SOURCETYPE_TO_STRING: Incomplete
    @staticmethod
    def from_string(status_str): ...
    @staticmethod
    def to_string(status): ...
