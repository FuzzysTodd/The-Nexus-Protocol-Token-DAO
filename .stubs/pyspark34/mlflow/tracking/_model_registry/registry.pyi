from _typeshed import Incomplete
from mlflow.tracking.registry import StoreRegistry as StoreRegistry

class ModelRegistryStoreRegistry(StoreRegistry):
    """Scheme-based registry for model registry store implementations

    This class allows the registration of a function or class to provide an
    implementation for a given scheme of `store_uri` through the `register`
    methods. Implementations declared though the entrypoints
    `mlflow.registry_store` group can be automatically registered through the
    `register_entrypoints` method.

    When instantiating a store through the `get_store` method, the scheme of
    the store URI provided (or inferred from environment) will be used to
    select which implementation to instantiate, which will be called with same
    arguments passed to the `get_store` method.
    """
    def __init__(self) -> None: ...
    def get_store(self, store_uri: Incomplete | None = None, tracking_uri: Incomplete | None = None):
        """Get a store from the registry based on the scheme of store_uri

        :param store_uri: The store URI. If None, it will be inferred from the environment. This URI
                          is used to select which tracking store implementation to instantiate and
                          is passed to the constructor of the implementation.
        :param tracking_uri: The optional string tracking URI to use for any MLflow tracking-related
                             operations in the registry client, e.g. downloading source run
                             artifacts in order to re-upload them to the model registry location.

        :return: An instance of `mlflow.store.model_registry.AbstractStore` that fulfills the
                 store URI requirements.
        """
