from _typeshed import Incomplete
from pyspark.java_gateway import local_connect_and_auth as local_connect_and_auth
from pyspark.resource import ResourceInformation as ResourceInformation
from pyspark.serializers import UTF8Deserializer as UTF8Deserializer, read_int as read_int, write_int as write_int, write_with_length as write_with_length
from typing import Dict, List

class TaskContext:
    '''
    Contextual information about a task which can be read or mutated during
    execution. To access the TaskContext for a running task, use:
    :meth:`TaskContext.get`.

    .. versionadded:: 2.2.0

    Examples
    --------
    >>> from pyspark import TaskContext

    Get a task context instance from :class:`RDD`.

    >>> spark.sparkContext.setLocalProperty("key1", "value")
    >>> taskcontext = spark.sparkContext.parallelize([1]).map(lambda _: TaskContext.get()).first()
    >>> isinstance(taskcontext.attemptNumber(), int)
    True
    >>> isinstance(taskcontext.partitionId(), int)
    True
    >>> isinstance(taskcontext.stageId(), int)
    True
    >>> isinstance(taskcontext.taskAttemptId(), int)
    True
    >>> taskcontext.getLocalProperty("key1")
    \'value\'
    >>> isinstance(taskcontext.cpus(), int)
    True

    Get a task context instance from a dataframe via Python UDF.

    >>> from pyspark.sql import Row
    >>> from pyspark.sql.functions import udf
    >>> @udf("STRUCT<anum: INT, partid: INT, stageid: INT, taskaid: INT, prop: STRING, cpus: INT>")
    ... def taskcontext_as_row():
    ...    taskcontext = TaskContext.get()
    ...    return Row(
    ...        anum=taskcontext.attemptNumber(),
    ...        partid=taskcontext.partitionId(),
    ...        stageid=taskcontext.stageId(),
    ...        taskaid=taskcontext.taskAttemptId(),
    ...        prop=taskcontext.getLocalProperty("key2"),
    ...        cpus=taskcontext.cpus())
    ...
    >>> spark.sparkContext.setLocalProperty("key2", "value")
    >>> [(anum, partid, stageid, taskaid, prop, cpus)] = (
    ...     spark.range(1).select(taskcontext_as_row()).first()
    ... )
    >>> isinstance(anum, int)
    True
    >>> isinstance(partid, int)
    True
    >>> isinstance(stageid, int)
    True
    >>> isinstance(taskaid, int)
    True
    >>> prop
    \'value\'
    >>> isinstance(cpus, int)
    True

    Get a task context instance from a dataframe via Pandas UDF.

    >>> import pandas as pd  # doctest: +SKIP
    >>> from pyspark.sql.functions import pandas_udf
    >>> @pandas_udf("STRUCT<"
    ...     "anum: INT, partid: INT, stageid: INT, taskaid: INT, prop: STRING, cpus: INT>")
    ... def taskcontext_as_row(_):
    ...    taskcontext = TaskContext.get()
    ...    return pd.DataFrame({
    ...        "anum": [taskcontext.attemptNumber()],
    ...        "partid": [taskcontext.partitionId()],
    ...        "stageid": [taskcontext.stageId()],
    ...        "taskaid": [taskcontext.taskAttemptId()],
    ...        "prop": [taskcontext.getLocalProperty("key3")],
    ...        "cpus": [taskcontext.cpus()]
    ...    })  # doctest: +SKIP
    ...
    >>> spark.sparkContext.setLocalProperty("key3", "value")  # doctest: +SKIP
    >>> [(anum, partid, stageid, taskaid, prop, cpus)] = (
    ...     spark.range(1).select(taskcontext_as_row("id")).first()
    ... )  # doctest: +SKIP
    >>> isinstance(anum, int)
    True
    >>> isinstance(partid, int)
    True
    >>> isinstance(stageid, int)
    True
    >>> isinstance(taskaid, int)
    True
    >>> prop
    \'value\'
    >>> isinstance(cpus, int)
    True
    '''
    def __new__(cls) -> TaskContext:
        """
        Even if users construct :class:`TaskContext` instead of using get, give them the singleton.
        """
    @classmethod
    def get(cls) -> TaskContext | None:
        """
        Return the currently active :class:`TaskContext`. This can be called inside of
        user functions to access contextual information about running tasks.

        Returns
        -------
        :class:`TaskContext`, optional

        Notes
        -----
        Must be called on the worker, not the driver. Returns ``None`` if not initialized.
        """
    def stageId(self) -> int:
        """
        The ID of the stage that this task belong to.

        Returns
        -------
        int
            current stage id.
        """
    def partitionId(self) -> int:
        """
        The ID of the RDD partition that is computed by this task.

        Returns
        -------
        int
            current partition id.
        """
    def attemptNumber(self) -> int:
        """
        How many times this task has been attempted.  The first task attempt will be assigned
        attemptNumber = 0, and subsequent attempts will have increasing attempt numbers.

        Returns
        -------
        int
            current attempt number.
        """
    def taskAttemptId(self) -> int:
        """
        An ID that is unique to this task attempt (within the same :class:`SparkContext`,
        no two task attempts will share the same attempt ID).  This is roughly equivalent
        to Hadoop's `TaskAttemptID`.

        Returns
        -------
        int
            current task attempt id.
        """
    def getLocalProperty(self, key: str) -> str | None:
        """
        Get a local property set upstream in the driver, or None if it is missing.

        Parameters
        ----------
        key : str
            the key of the local property to get.

        Returns
        -------
        int
            the value of the local property.
        """
    def cpus(self) -> int:
        """
        CPUs allocated to the task.

        Returns
        -------
        int
            the number of CPUs.
        """
    def resources(self) -> Dict[str, ResourceInformation]:
        """
        Resources allocated to the task. The key is the resource name and the value is information
        about the resource.

        Returns
        -------
        dict
            a dictionary of a string resource name, and :class:`ResourceInformation`.
        """

BARRIER_FUNCTION: int
ALL_GATHER_FUNCTION: int

class BarrierTaskContext(TaskContext):
    """
    A :class:`TaskContext` with extra contextual info and tooling for tasks in a barrier stage.
    Use :func:`BarrierTaskContext.get` to obtain the barrier context for a running barrier task.

    .. versionadded:: 2.4.0

    Notes
    -----
    This API is experimental

    Examples
    --------
    Set a barrier, and execute it with RDD.

    >>> from pyspark import BarrierTaskContext
    >>> def block_and_do_something(itr):
    ...     taskcontext = BarrierTaskContext.get()
    ...     # Do something.
    ...
    ...     # Wait until all tasks finished.
    ...     taskcontext.barrier()
    ...
    ...     return itr
    ...
    >>> rdd = spark.sparkContext.parallelize([1])
    >>> rdd.barrier().mapPartitions(block_and_do_something).collect()
    [1]
    """
    @classmethod
    def get(cls) -> BarrierTaskContext:
        """
        Return the currently active :class:`BarrierTaskContext`.
        This can be called inside of user functions to access contextual information about
        running tasks.

        Notes
        -----
        Must be called on the worker, not the driver. Returns ``None`` if not initialized.
        An Exception will raise if it is not in a barrier stage.

        This API is experimental
        """
    def barrier(self) -> None:
        """
        Sets a global barrier and waits until all tasks in this stage hit this barrier.
        Similar to `MPI_Barrier` function in MPI, this function blocks until all tasks
        in the same stage have reached this routine.

        .. versionadded:: 2.4.0

        Notes
        -----
        This API is experimental

        In a barrier stage, each task much have the same number of `barrier()`
        calls, in all possible code branches. Otherwise, you may get the job hanging
        or a `SparkException` after timeout.
        """
    def allGather(self, message: str = '') -> List[str]:
        """
        This function blocks until all tasks in the same stage have reached this routine.
        Each task passes in a message and returns with a list of all the messages passed in
        by each of those tasks.

        .. versionadded:: 3.0.0

        Notes
        -----
        This API is experimental

        In a barrier stage, each task much have the same number of `barrier()`
        calls, in all possible code branches. Otherwise, you may get the job hanging
        or a `SparkException` after timeout.
        """
    def getTaskInfos(self) -> List['BarrierTaskInfo']:
        """
        Returns :class:`BarrierTaskInfo` for all tasks in this barrier stage,
        ordered by partition ID.

        .. versionadded:: 2.4.0

        Notes
        -----
        This API is experimental

        Examples
        --------
        >>> from pyspark import BarrierTaskContext
        >>> rdd = spark.sparkContext.parallelize([1])
        >>> barrier_info = rdd.barrier().mapPartitions(
        ...     lambda _: [BarrierTaskContext.get().getTaskInfos()]).collect()[0][0]
        >>> barrier_info.address
        '...:...'
        """

class BarrierTaskInfo:
    """
    Carries all task infos of a barrier task.

    .. versionadded:: 2.4.0

    Attributes
    ----------
    address : str
        The IPv4 address (host:port) of the executor that the barrier task is running on

    Notes
    -----
    This API is experimental
    """
    address: Incomplete
    def __init__(self, address: str) -> None: ...
