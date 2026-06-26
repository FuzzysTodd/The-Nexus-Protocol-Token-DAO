from .._project_spec import EntryPoint as EntryPoint, LaunchProject as LaunchProject
from ..builder.build import get_env_vars_dict as get_env_vars_dict
from ..errors import LaunchError as LaunchError
from ..utils import LOG_PREFIX as LOG_PREFIX, MAX_ENV_LENGTHS as MAX_ENV_LENGTHS, PROJECT_SYNCHRONOUS as PROJECT_SYNCHRONOUS, get_kube_context_and_api_client as get_kube_context_and_api_client, make_name_dns_safe as make_name_dns_safe
from .abstract import AbstractRun as AbstractRun, AbstractRunner as AbstractRunner
from .kubernetes_monitor import KubernetesRunMonitor as KubernetesRunMonitor
from _typeshed import Incomplete
from kubernetes.client.api.batch_v1_api import BatchV1Api as BatchV1Api
from kubernetes.client.api.core_v1_api import CoreV1Api as CoreV1Api
from kubernetes.client.api.custom_objects_api import CustomObjectsApi as CustomObjectsApi
from kubernetes.client.models.v1_job import V1Job as V1Job
from kubernetes.client.models.v1_secret import V1Secret as V1Secret
from typing import Any, Dict, List
from wandb.apis.internal import Api as Api
from wandb.sdk.launch.environment.abstract import AbstractEnvironment as AbstractEnvironment
from wandb.sdk.launch.registry.abstract import AbstractRegistry as AbstractRegistry
from wandb.sdk.launch.registry.azure_container_registry import AzureContainerRegistry as AzureContainerRegistry
from wandb.sdk.launch.registry.local_registry import LocalRegistry as LocalRegistry
from wandb.sdk.launch.runner.abstract import Status as Status
from wandb.util import get_module as get_module

TIMEOUT: int

class KubernetesSubmittedRun(AbstractRun):
    """Wrapper for a launched run on Kubernetes."""
    monitor: Incomplete
    batch_api: Incomplete
    core_api: Incomplete
    name: Incomplete
    namespace: Incomplete
    secret: Incomplete
    def __init__(self, monitor: KubernetesRunMonitor, batch_api: BatchV1Api, core_api: CoreV1Api, name: str, namespace: str | None = 'default', secret: V1Secret | None = None) -> None:
        """Initialize a KubernetesSubmittedRun.

        Other implementations of the AbstractRun interface poll on the run
        when `get_status` is called, but KubernetesSubmittedRun uses
        Kubernetes watch streams to update the run status. One thread handles
        events from the job object and another thread handles events from the
        rank 0 pod. These threads updated the `_status` attributed of the
        KubernetesSubmittedRun object. When `get_status` is called, the
        `_status` attribute is returned.

        Arguments:
            batch_api: Kubernetes BatchV1Api object.
            core_api: Kubernetes CoreV1Api object.
            name: Name of the job.
            namespace: Kubernetes namespace.
            secret: Kubernetes secret.

        Returns:
            None.
        """
    @property
    def id(self) -> str:
        """Return the run id."""
    def get_logs(self) -> str | None: ...
    def get_job(self) -> V1Job:
        """Return the job object."""
    def wait(self) -> bool:
        """Wait for the run to finish.

        Returns:
            True if the run finished successfully, False otherwise.
        """
    def get_status(self) -> Status: ...
    def cancel(self) -> None:
        """Cancel the run."""

class CrdSubmittedRun(AbstractRun):
    """Run submitted to a CRD backend, e.g. Volcano."""
    group: Incomplete
    version: Incomplete
    plural: Incomplete
    name: Incomplete
    namespace: Incomplete
    core_api: Incomplete
    custom_api: Incomplete
    monitor: Incomplete
    def __init__(self, group: str, version: str, plural: str, name: str, namespace: str, core_api: CoreV1Api, custom_api: CustomObjectsApi, monitor: KubernetesRunMonitor) -> None:
        """Create a run object for tracking the progress of a CRD.

        Arguments:
            group: The API group of the CRD.
            version: The API version of the CRD.
            plural: The plural name of the CRD.
            name: The name of the CRD instance.
            namespace: The namespace of the CRD instance.
            core_api: The Kubernetes core API client.
            custom_api: The Kubernetes custom object API client.
            monitor: The run monitor.

        Raises:
            LaunchError: If the CRD instance does not exist.
        """
    @property
    def id(self) -> str:
        """Get the name of the custom object."""
    def get_logs(self) -> str | None:
        """Get logs for custom object."""
    def get_status(self) -> Status:
        """Get status of custom object."""
    def cancel(self) -> None:
        """Cancel the custom object."""
    def wait(self) -> bool:
        """Wait for this custom object to finish running."""

class KubernetesRunner(AbstractRunner):
    """Launches runs onto kubernetes."""
    environment: Incomplete
    registry: Incomplete
    def __init__(self, api: Api, backend_config: Dict[str, Any], environment: AbstractEnvironment, registry: AbstractRegistry) -> None:
        """Create a Kubernetes runner.

        Arguments:
            api: The API client object.
            backend_config: The backend configuration.
            environment: The environment to launch runs into.

        Raises:
            LaunchError: If the Kubernetes configuration is invalid.
        """
    def get_namespace(self, resource_args: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Get the namespace to launch into.

        Arguments:
            resource_args: The resource args to launch.
            context: The k8s config context.

        Returns:
            The namespace to launch into.
        """
    def run(self, launch_project: LaunchProject, image_uri: str) -> AbstractRun | None:
        """Execute a launch project on Kubernetes.

        Arguments:
            launch_project: The launch project to execute.
            builder: The builder to use to build the image.

        Returns:
            The run object if the run was successful, otherwise None.
        """

def inject_entrypoint_and_args(containers: List[dict], entry_point: EntryPoint | None, override_args: List[str], should_override_entrypoint: bool) -> None:
    """Inject the entrypoint and args into the containers.

    Arguments:
        containers: The containers to inject the entrypoint and args into.
        entry_point: The entrypoint to inject.
        override_args: The args to inject.
        should_override_entrypoint: Whether to override the entrypoint.

    Returns:
        None
    """
def maybe_create_imagepull_secret(core_api: CoreV1Api, registry: AbstractRegistry, run_id: str, namespace: str) -> V1Secret | None:
    """Create a secret for pulling images from a private registry.

    Arguments:
        core_api: The Kubernetes CoreV1Api object.
        registry: The registry to pull from.
        run_id: The run id.
        namespace: The namespace to create the secret in.

    Returns:
        A secret if one was created, otherwise None.
    """
def add_wandb_env(root: dict | list, env_vars: Dict[str, str]) -> None:
    '''Injects wandb environment variables into specs.

    Recursively walks the spec and injects the environment variables into
    every container spec. Containers are identified by the "containers" key.

    This function treats the WANDB_RUN_ID and WANDB_GROUP_ID environment variables
    specially. If they are present in the spec, they will be overwritten. If a setting
    for WANDB_RUN_ID is provided in env_vars, then that environment variable will only be
    set in the first container modified by this function.

    Arguments:
        root: The spec to modify.
        env_vars: The environment variables to inject.

    Returns: None.
    '''
def add_label_to_pods(manifest: dict | list, label_key: str, label_value: str) -> None:
    '''Add a label to all pod specs in a manifest.

    Recursively traverses the manifest and adds the label to all pod specs.
    Pod specs are identified by the presence of a "spec" key with a "containers"
    key in the value.

    Arguments:
        manifest: The manifest to modify.
        label_key: The label key to add.
        label_value: The label value to add.

    Returns: None.
    '''
def add_entrypoint_args_overrides(manifest: dict | list, overrides: dict) -> None:
    '''Add entrypoint and args overrides to all containers in a manifest.

    Recursively traverses the manifest and adds the entrypoint and args overrides
    to all containers. Containers are identified by the presence of a "spec" key
    with a "containers" key in the value.

    Arguments:
        manifest: The manifest to modify.
        overrides: Dictionary with args and entrypoint keys.

    Returns: None.
    '''
