import abc
from _typeshed import Incomplete
from abc import ABCMeta
from mlflow.store.model_registry.abstract_store import AbstractStore as AbstractStore
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.rest_utils import call_endpoint as call_endpoint, call_endpoints as call_endpoints

class BaseRestStore(AbstractStore, metaclass=abc.ABCMeta):
    """
    Base class client for a remote model registry server accessed via REST API calls
    """
    __metaclass__ = ABCMeta
    get_host_creds: Incomplete
    def __init__(self, get_host_creds) -> None: ...
