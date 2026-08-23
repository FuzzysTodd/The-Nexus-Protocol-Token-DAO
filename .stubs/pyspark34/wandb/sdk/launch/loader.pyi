from .builder.abstract import AbstractBuilder as AbstractBuilder
from .environment.abstract import AbstractEnvironment as AbstractEnvironment
from .registry.abstract import AbstractRegistry as AbstractRegistry
from .registry.local_registry import LocalRegistry as LocalRegistry
from .runner.abstract import AbstractRunner as AbstractRunner
from _typeshed import Incomplete
from typing import Any, Dict
from wandb.apis.internal import Api as Api
from wandb.docker import is_docker_installed as is_docker_installed
from wandb.sdk.launch.errors import LaunchError as LaunchError

WANDB_RUNNERS: Incomplete

def environment_from_config(config: Dict[str, Any] | None) -> AbstractEnvironment:
    '''Create an environment from a config.

    This helper function is used to create an environment from a config. The
    config should have a "type" key that specifies the type of environment to
    create. The remaining keys are passed to the environment\'s from_config
    method. If the config is None or empty, a LocalEnvironment is returned.

    Arguments:
        config (Dict[str, Any]): The config.

    Returns:
        Environment: The environment constructed.
    '''
def registry_from_config(config: Dict[str, Any] | None, environment: AbstractEnvironment) -> AbstractRegistry:
    '''Create a registry from a config.

    This helper function is used to create a registry from a config. The
    config should have a "type" key that specifies the type of registry to
    create. The remaining keys are passed to the registry\'s from_config
    method. If the config is None or empty, a LocalRegistry is returned.

    Arguments:
        config (Dict[str, Any]): The registry config.
        environment (Environment): The environment of the registry.

    Returns:
        The registry if config is not None, otherwise None.

    Raises:
        LaunchError: If the registry is not configured correctly.
    '''
def builder_from_config(config: Dict[str, Any] | None, environment: AbstractEnvironment, registry: AbstractRegistry) -> AbstractBuilder:
    '''Create a builder from a config.

    This helper function is used to create a builder from a config. The
    config should have a "type" key that specifies the type of builder to import
    and create. The remaining keys are passed to the builder\'s from_config
    method. If the config is None or empty, a default builder is returned.

    The default builder will be a DockerBuilder if we find a working docker cli
    on the system, otherwise it will be a NoOpBuilder.

    Arguments:
        config (Dict[str, Any]): The builder config.
        registry (Registry): The registry of the builder.

    Returns:
        The builder.

    Raises:
        LaunchError: If the builder is not configured correctly.
    '''
def runner_from_config(runner_name: str, api: Api, runner_config: Dict[str, Any], environment: AbstractEnvironment, registry: AbstractRegistry) -> AbstractRunner:
    '''Create a runner from a config.

    This helper function is used to create a runner from a config. The
    config should have a "type" key that specifies the type of runner to import
    and create. The remaining keys are passed to the runner\'s from_config
    method. If the config is None or empty, a LocalContainerRunner is returned.

    Arguments:
        runner_name (str): The name of the backend.
        api (Api): The API.
        runner_config (Dict[str, Any]): The backend config.

    Returns:
        The runner.

    Raises:
        LaunchError: If the runner is not configured correctly.
    '''
