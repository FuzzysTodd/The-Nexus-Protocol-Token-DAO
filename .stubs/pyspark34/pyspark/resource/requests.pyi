from py4j.java_gateway import JVMView as JVMView, JavaObject as JavaObject
from typing import Dict, overload

class ExecutorResourceRequest:
    """
    An Executor resource request. This is used in conjunction with the ResourceProfile to
    programmatically specify the resources needed for an RDD that will be applied at the
    stage level.

    This is used to specify what the resource requirements are for an Executor and how
    Spark can find out specific details about those resources. Not all the parameters are
    required for every resource type. Resources like GPUs are supported and have same limitations
    as using the global spark configs spark.executor.resource.gpu.*. The amount, discoveryScript,
    and vendor parameters for resources are all the same parameters a user would specify through the
    configs: spark.executor.resource.{resourceName}.{amount, discoveryScript, vendor}.

    For instance, a user wants to allocate an Executor with GPU resources on YARN. The user has
    to specify the resource name (gpu), the amount or number of GPUs per Executor,
    the discovery script would be specified so that when the Executor starts up it can
    discovery what GPU addresses are available for it to use because YARN doesn't tell
    Spark that, then vendor would not be used because its specific for Kubernetes.

    See the configuration and cluster specific docs for more details.

    Use :class:`pyspark.ExecutorResourceRequests` class as a convenience API.

    .. versionadded:: 3.1.0

    Parameters
    ----------
    resourceName : str
        Name of the resource
    amount : str
        Amount requesting
    discoveryScript : str, optional
        Optional script used to discover the resources. This is required on some
        cluster managers that don't tell Spark the addresses of the resources
        allocated. The script runs on Executors startup to discover the addresses
        of the resources available.
    vendor : str, optional
        Vendor, required for some cluster managers

    See Also
    --------
    :class:`pyspark.resource.ResourceProfile`

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, resourceName: str, amount: int, discoveryScript: str = '', vendor: str = '') -> None: ...
    @property
    def resourceName(self) -> str:
        """
        Returns
        -------
        str
            Name of the resource
        """
    @property
    def amount(self) -> int:
        """
        Returns
        -------
        str
            Amount requesting
        """
    @property
    def discoveryScript(self) -> str:
        """
        Returns
        -------
        str
            Amount requesting
        """
    @property
    def vendor(self) -> str:
        """
        Returns
        -------
        str
            Vendor, required for some cluster managers
        """

class ExecutorResourceRequests:
    """
    A set of Executor resource requests. This is used in conjunction with the
    :class:`pyspark.resource.ResourceProfileBuilder` to programmatically specify the
    resources needed for an RDD that will be applied at the stage level.

    .. versionadded:: 3.1.0

    See Also
    --------
    :class:`pyspark.resource.ResourceProfile`

    Notes
    -----
    This API is evolving.
    """
    @overload
    def __init__(self, _jvm: JVMView) -> None: ...
    @overload
    def __init__(self, _jvm: None = ..., _requests: Dict[str, ExecutorResourceRequest] | None = ...) -> None: ...
    def memory(self, amount: str) -> ExecutorResourceRequests:
        '''
        Specify heap memory. The value specified will be converted to MiB.
        This is a convenient API to add :class:`ExecutorResourceRequest` for "memory" resource.

        Parameters
        ----------
        amount : str
            Amount of memory. In the same format as JVM memory strings (e.g. 512m, 2g).
            Default unit is MiB if not specified.

        Returns
        -------
        :class:`ExecutorResourceRequests`
        '''
    def memoryOverhead(self, amount: str) -> ExecutorResourceRequests:
        '''
        Specify overhead memory. The value specified will be converted to MiB.
        This is a convenient API to add :class:`ExecutorResourceRequest` for "memoryOverhead"
        resource.

        Parameters
        ----------
        amount : str
            Amount of memory. In the same format as JVM memory strings (e.g. 512m, 2g).
            Default unit is MiB if not specified.

        Returns
        -------
        :class:`ExecutorResourceRequests`
        '''
    def pysparkMemory(self, amount: str) -> ExecutorResourceRequests:
        '''
        Specify pyspark memory. The value specified will be converted to MiB.
        This is a convenient API to add :class:`ExecutorResourceRequest` for "pyspark.memory"
        resource.

        Parameters
        ----------
        amount : str
            Amount of memory. In the same format as JVM memory strings (e.g. 512m, 2g).
            Default unit is MiB if not specified.

        Returns
        -------
        :class:`ExecutorResourceRequests`
        '''
    def offheapMemory(self, amount: str) -> ExecutorResourceRequests:
        '''
        Specify off heap memory. The value specified will be converted to MiB.
        This value only take effect when MEMORY_OFFHEAP_ENABLED is true.
        This is a convenient API to add :class:`ExecutorResourceRequest` for "offHeap"
        resource.

        Parameters
        ----------
        amount : str
            Amount of memory. In the same format as JVM memory strings (e.g. 512m, 2g).
            Default unit is MiB if not specified.

        Returns
        -------
        :class:`ExecutorResourceRequests`
        '''
    def cores(self, amount: int) -> ExecutorResourceRequests:
        '''
        Specify number of cores per Executor.
        This is a convenient API to add :class:`ExecutorResourceRequest` for "cores" resource.

        Parameters
        ----------
        amount : int
            Number of cores to allocate per Executor.

        Returns
        -------
        :class:`ExecutorResourceRequests`
        '''
    def resource(self, resourceName: str, amount: int, discoveryScript: str = '', vendor: str = '') -> ExecutorResourceRequests:
        """
        Amount of a particular custom resource(GPU, FPGA, etc) to use. The resource names supported
        correspond to the regular Spark configs with the prefix removed. For instance, resources
        like GPUs are gpu (spark configs `spark.executor.resource.gpu.*`). If you pass in a resource
        that the cluster manager doesn't support the result is undefined, it may error or may just
        be ignored.
        This is a convenient API to add :class:`ExecutorResourceRequest` for custom resources.

        Parameters
        ----------
        resourceName : str
            Name of the resource.
        amount : str
            amount of that resource per executor to use.
        discoveryScript : str, optional
            Optional script used to discover the resources. This is required on
            some cluster managers that don't tell Spark the addresses of
            the resources allocated. The script runs on Executors startup to
            of the resources available.
        vendor : str
            Optional vendor, required for some cluster managers

        Returns
        -------
        :class:`ExecutorResourceRequests`
        """
    @property
    def requests(self) -> Dict[str, ExecutorResourceRequest]:
        """
        Returns
        -------
        dict
            Returns all the resource requests for the executor.
        """

class TaskResourceRequest:
    """
    A task resource request. This is used in conjunction with the
    :class:`pyspark.resource.ResourceProfile` to programmatically specify the resources
    needed for an RDD that will be applied at the stage level. The amount is specified
    as a float to allow for saying you want more than 1 task per resource. Valid values
    are less than or equal to 0.5 or whole numbers.
    Use :class:`pyspark.resource.TaskResourceRequests` class as a convenience API.

    Parameters
    ----------
    resourceName : str
        Name of the resource
    amount : float
        Amount requesting as a float to support fractional resource requests.
        Valid values are less than or equal to 0.5 or whole numbers. This essentially
        lets you configure X number of tasks to run on a single resource,
        ie amount equals 0.5 translates into 2 tasks per resource address.

    .. versionadded:: 3.1.0

    See Also
    --------
    :class:`pyspark.resource.ResourceProfile`

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, resourceName: str, amount: float) -> None: ...
    @property
    def resourceName(self) -> str:
        """
        Returns
        -------
        str
            Name of the resource.
        """
    @property
    def amount(self) -> float:
        """
        Returns
        -------
        str
            Amount requesting as a float to support fractional resource requests.
        """

class TaskResourceRequests:
    """
    A set of task resource requests. This is used in conjunction with the
    :class:`pyspark.resource.ResourceProfileBuilder` to programmatically specify the resources
    needed for an RDD that will be applied at the stage level.

    .. versionadded:: 3.1.0

    See Also
    --------
    :class:`pyspark.resource.ResourceProfile`

    Notes
    -----
    This API is evolving.
    """
    @overload
    def __init__(self, _jvm: JVMView) -> None: ...
    @overload
    def __init__(self, _jvm: None = ..., _requests: Dict[str, TaskResourceRequest] | None = ...) -> None: ...
    def cpus(self, amount: int) -> TaskResourceRequests:
        """
        Specify number of cpus per Task.
        This is a convenient API to add :class:`TaskResourceRequest` for cpus.

        Parameters
        ----------
        amount : int
            Number of cpus to allocate per Task.

        Returns
        -------
        :class:`TaskResourceRequests`
        """
    def resource(self, resourceName: str, amount: float) -> TaskResourceRequests:
        """
        Amount of a particular custom resource(GPU, FPGA, etc) to use.
        This is a convenient API to add :class:`TaskResourceRequest` for custom resources.

        Parameters
        ----------
        resourceName : str
            Name of the resource.
        amount : float
            Amount requesting as a float to support fractional resource requests.
            Valid values are less than or equal to 0.5 or whole numbers. This essentially
            lets you configure X number of tasks to run on a single resource,
            ie amount equals 0.5 translates into 2 tasks per resource address.

        Returns
        -------
        :class:`TaskResourceRequests`
        """
    @property
    def requests(self) -> Dict[str, TaskResourceRequest]:
        """
        Returns
        -------
        dict
            Returns all the resource requests for the task.
        """
