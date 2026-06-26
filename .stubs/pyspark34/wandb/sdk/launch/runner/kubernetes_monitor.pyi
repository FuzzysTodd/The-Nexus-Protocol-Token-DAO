from .abstract import State as State, Status as Status
from _typeshed import Incomplete
from kubernetes import watch
from kubernetes.client import BatchV1Api as BatchV1Api, CoreV1Api as CoreV1Api, CustomObjectsApi as CustomObjectsApi, V1PodStatus as V1PodStatus
from typing import Any, Dict

CRD_STATE_DICT: Dict[str, State]

class SafeWatch:
    """Wrapper for the kubernetes watch class that can recover in more situations."""
    def __init__(self, watcher: watch.Watch) -> None:
        """Initialize the SafeWatch."""
    def stream(self, func: Any, *args: Any, **kwargs: Any) -> Any:
        """Stream the watcher."""
    def stop(self) -> None:
        """Stop the watcher."""

class KubernetesRunMonitor:
    pod_label_selector: Incomplete
    job_field_selector: Incomplete
    namespace: Incomplete
    batch_api: Incomplete
    core_api: Incomplete
    custom_api: Incomplete
    group: Incomplete
    version: Incomplete
    plural: Incomplete
    def __init__(self, job_field_selector: str, pod_label_selector: str, namespace: str, batch_api: BatchV1Api, core_api: CoreV1Api, custom_api: CustomObjectsApi = None, group: str | None = None, version: str | None = None, plural: str | None = None) -> None:
        '''Initialize KubernetesRunMonitor.

        If a custom api is provided, the group, version, and plural arguments must also
        be provided. These are used to query the custom api for a launched custom
        object (CRD). Group, version, and plural in this context refer to the
        Kubernetes API group, version, and plural for the CRD. For more information
        see: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

        The run monitor starts two threads to watch for pods and jobs/crds matching the
        provided selectors. The status is set to "starting" when the run monitor is
        initialized. The status is set to "running" when a pod matching the pod selector
        is found with a status of "Running" or has a container with a status of
        "ContainerCreating". The status is set to "finished" when a job matching the job
        selector is found with a status of "Succeeded". The status is set to "failed"
        when a job matching the job selector is found with a status of "Failed" or a pod
        matching the pod selector is found with a status of "Failed". The status is set
        to "preempted" when a pod matching the pod selector is found with a condition
        type of "DisruptionTarget" and a reason of "EvictionByEvictionAPI",
        "PreemptionByScheduler", or "TerminationByKubelet".

        The logic for the CRD is similar to the logic for the job, but we inspect
        both the phase of the CRD and the conditions since some CRDs do not have a
        phase field.

        Arguments:
            job_field_selector: The field selector for the job or crd.
            pod_label_selector: The label selector for the pods.
            namespace: The namespace to monitor.
            batch_api: The batch api client.
            core_api: The core api client.
            custom_api: The custom api client.
            group: The group of the CRD.
            version: The version of the CRD.
            plural: The plural of the CRD.

        Returns:
            None.
        '''
    def start(self) -> None:
        """Start the run monitor."""
    def stop(self) -> None:
        """Stop the run monitor."""
    def get_status(self) -> Status:
        """Get the run status."""
