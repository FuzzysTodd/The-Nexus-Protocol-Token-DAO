from mlflow.entities.model_registry._model_registry_entity import _ModelRegistryEntity

class ModelVersionTag(_ModelRegistryEntity):
    """Tag object associated with a model version."""
    def __init__(self, key, value) -> None: ...
    def __eq__(self, other): ...
    @property
    def key(self):
        """String name of the tag."""
    @property
    def value(self):
        """String value of the tag."""
    @classmethod
    def from_proto(cls, proto): ...
    def to_proto(self): ...
