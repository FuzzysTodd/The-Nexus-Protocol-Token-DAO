from mlflow.entities.model_registry._model_registry_entity import _ModelRegistryEntity

class RegisteredModelAlias(_ModelRegistryEntity):
    """Alias object associated with a registered model."""
    def __init__(self, alias, version) -> None: ...
    def __eq__(self, other): ...
    @property
    def alias(self):
        """String name of the alias."""
    @property
    def version(self):
        """String model version number that the alias points to."""
    @classmethod
    def from_proto(cls, proto): ...
    def to_proto(self): ...
