from _typeshed import Incomplete

class ModelVersionStatus:
    """Enum for status of an :py:class:`mlflow.entities.model_registry.ModelVersion`."""
    PENDING_REGISTRATION: Incomplete
    FAILED_REGISTRATION: Incomplete
    READY: Incomplete
    @staticmethod
    def from_string(status_str): ...
    @staticmethod
    def to_string(status): ...
    @staticmethod
    def all_status(): ...
