import abc
from _typeshed import Incomplete
from mlflow.deployments.base import BaseDeploymentClient as BaseDeploymentClient
from mlflow.deployments.utils import parse_target_uri as parse_target_uri
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.utils.annotations import developer_stable as developer_stable

class PluginManager(abc.ABC, metaclass=abc.ABCMeta):
    """
    Abstract class defining a entrypoint based plugin registration.

    This class allows the registration of a function or class to provide an implementation
    for a given key/name. Implementations declared though the entrypoints can be automatically
    registered through the `register_entrypoints` method.
    """
    group_name: Incomplete
    @abc.abstractmethod
    def __init__(self, group_name): ...
    @abc.abstractmethod
    def __getitem__(self, item): ...
    @property
    def registry(self):
        """
        Registry stores the registered plugin as a key value pair where key is the
        name of the plugin and value is the plugin object
        """
    @property
    def has_registered(self):
        '''
        Returns bool representing whether the "register_entrypoints" has run or not. This
        doesn\'t return True if `register` method is called outside of `register_entrypoints`
        to register plugins
        '''
    def register(self, target_name, plugin_module) -> None:
        """
        Register a deployment client given its target name and module

        :param target_name: The name of the deployment target. This name will be used by
                            `get_deploy_client()` to retrieve a deployment client from
                            the plugin store
        :param plugin_module: The module that implements the deployment plugin interface
        """
    def register_entrypoints(self) -> None:
        """
        Runs through all the packages that has the `group_name` defined as the entrypoint
        and register that into the registry
        """

class DeploymentPlugins(PluginManager):
    def __init__(self) -> None: ...
    def __getitem__(self, item):
        """Override __getitem__ so that we can directly look up plugins via dict-like syntax"""
