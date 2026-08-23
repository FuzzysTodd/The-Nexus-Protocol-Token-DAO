import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.utils.uri import get_uri_scheme as get_uri_scheme

class UnsupportedModelRegistryStoreURIException(MlflowException):
    """Exception thrown when building a model registry store with an unsupported URI"""
    supported_uri_schemes: Incomplete
    def __init__(self, unsupported_uri, supported_uri_schemes) -> None: ...

class StoreRegistry(metaclass=abc.ABCMeta):
    """
    Abstract class defining a scheme-based registry for store implementations.

    This class allows the registration of a function or class to provide an
    implementation for a given scheme of `store_uri` through the `register`
    methods. Implementations declared though the entrypoints can be automatically
    registered through the `register_entrypoints` method.

    When instantiating a store through the `get_store` method, the scheme of
    the store URI provided (or inferred from environment) will be used to
    select which implementation to instantiate, which will be called with same
    arguments passed to the `get_store` method.
    """
    __metaclass__ = ABCMeta
    group_name: Incomplete
    @abstractmethod
    def __init__(self, group_name): ...
    def register(self, scheme, store_builder) -> None: ...
    def register_entrypoints(self) -> None:
        """Register tracking stores provided by other packages"""
    def get_store_builder(self, store_uri):
        """Get a store from the registry based on the scheme of store_uri

        :param store_uri: The store URI. If None, it will be inferred from the environment. This
                          URI is used to select which tracking store implementation to instantiate
                          and is passed to the constructor of the implementation.
        :return: A function that returns an instance of
                 ``mlflow.store.{tracking|model_registry}.AbstractStore`` that fulfills the store
                  URI requirements.
        """
