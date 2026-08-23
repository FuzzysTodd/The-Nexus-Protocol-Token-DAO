from py4j.java_gateway import JavaObject as JavaObject
from pyspark.resource.requests import ExecutorResourceRequest as ExecutorResourceRequest, ExecutorResourceRequests as ExecutorResourceRequests, TaskResourceRequest as TaskResourceRequest, TaskResourceRequests as TaskResourceRequests
from typing import Dict, overload

class ResourceProfile:
    '''
    Resource profile to associate with an RDD. A :class:`pyspark.resource.ResourceProfile`
    allows the user to specify executor and task requirements for an RDD that will get
    applied during a stage. This allows the user to change the resource requirements between
    stages. This is meant to be immutable so user cannot change it after building.

    .. versionadded:: 3.1.0

    Notes
    -----
    This API is evolving.

    Examples
    --------
    Create Executor resource requests.

    >>> executor_requests = (
    ...     ExecutorResourceRequests()
    ...     .cores(2)
    ...     .memory("6g")
    ...     .memoryOverhead("1g")
    ...     .pysparkMemory("2g")
    ...     .offheapMemory("3g")
    ...     .resource("gpu", 2, "testGpus", "nvidia.com")
    ... )

    Create task resource requasts.

    >>> task_requests = TaskResourceRequests().cpus(2).resource("gpu", 2)

    Create a resource profile.

    >>> builder = ResourceProfileBuilder()
    >>> resource_profile = builder.require(executor_requests).require(task_requests).build

    Create an RDD with the resource profile.

    >>> rdd = sc.parallelize(range(10)).withResources(resource_profile)
    >>> rdd.getResourceProfile()
    <pyspark.resource.profile.ResourceProfile object ...>
    >>> rdd.getResourceProfile().taskResources
    {\'cpus\': <...TaskResourceRequest...>, \'gpu\': <...TaskResourceRequest...>}
    >>> rdd.getResourceProfile().executorResources
    {\'gpu\': <...ExecutorResourceRequest...>,
     \'cores\': <...ExecutorResourceRequest...>,
     \'offHeap\': <...ExecutorResourceRequest...>,
     \'memoryOverhead\': <...ExecutorResourceRequest...>,
     \'pyspark.memory\': <...ExecutorResourceRequest...>,
     \'memory\': <...ExecutorResourceRequest...>}
    '''
    @overload
    def __init__(self, _java_resource_profile: JavaObject) -> None: ...
    @overload
    def __init__(self, _java_resource_profile: None = ..., _exec_req: Dict[str, ExecutorResourceRequest] | None = ..., _task_req: Dict[str, TaskResourceRequest] | None = ...) -> None: ...
    @property
    def id(self) -> int:
        """
        Returns
        -------
        int
            A unique id of this :class:`ResourceProfile`
        """
    @property
    def taskResources(self) -> Dict[str, TaskResourceRequest]:
        """
        Returns
        -------
        dict
            a dictionary of resources to :class:`TaskResourceRequest`
        """
    @property
    def executorResources(self) -> Dict[str, ExecutorResourceRequest]:
        """
        Returns
        -------
        dict
            a dictionary of resources to :class:`ExecutorResourceRequest`
        """

class ResourceProfileBuilder:
    """
    Resource profile Builder to build a resource profile to associate with an RDD.
    A ResourceProfile allows the user to specify executor and task requirements for
    an RDD that will get applied during a stage. This allows the user to change the
    resource requirements between stages.

    .. versionadded:: 3.1.0

    See Also
    --------
    :class:`pyspark.resource.ResourceProfile`

    Notes
    -----
    This API is evolving.
    """
    def __init__(self) -> None: ...
    def require(self, resourceRequest: ExecutorResourceRequests | TaskResourceRequests) -> ResourceProfileBuilder:
        """
        Add executor resource requests

        Parameters
        ----------
        resourceRequest : :class:`ExecutorResourceRequests` or :class:`TaskResourceRequests`
            The detailed executor resource requests, see :class:`ExecutorResourceRequests`

        Returns
        -------
        dict
            a dictionary of resources to :class:`ExecutorResourceRequest`
        """
    def clearExecutorResourceRequests(self) -> None: ...
    def clearTaskResourceRequests(self) -> None: ...
    @property
    def taskResources(self) -> Dict[str, TaskResourceRequest]:
        """
        Returns
        -------
        dict
            a dictionary of resources to :class:`TaskResourceRequest`
        """
    @property
    def executorResources(self) -> Dict[str, ExecutorResourceRequest]:
        """
        Returns
        -------
        dict
            a dictionary of resources to :class:`ExecutorResourceRequest`
        """
    @property
    def build(self) -> ResourceProfile: ...
