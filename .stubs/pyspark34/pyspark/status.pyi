from py4j.java_collections import JavaArray
from py4j.java_gateway import JavaObject
from typing import List, NamedTuple

__all__ = ['SparkJobInfo', 'SparkStageInfo', 'StatusTracker']

class SparkJobInfo(NamedTuple):
    """
    Exposes information about Spark Jobs.
    """
    jobId: int
    stageIds: JavaArray
    status: str

class SparkStageInfo(NamedTuple):
    """
    Exposes information about Spark Stages.
    """
    stageId: int
    currentAttemptId: int
    name: str
    numTasks: int
    numActiveTasks: int
    numCompletedTasks: int
    numFailedTasks: int

class StatusTracker:
    """
    Low-level status reporting APIs for monitoring job and stage progress.

    These APIs intentionally provide very weak consistency semantics;
    consumers of these APIs should be prepared to handle empty / missing
    information. For example, a job's stage ids may be known but the status
    API may not have any information about the details of those stages, so
    `getStageInfo` could potentially return `None` for a valid stage id.

    To limit memory usage, these APIs only provide information on recent
    jobs / stages.  These APIs will provide information for the last
    `spark.ui.retainedStages` stages and `spark.ui.retainedJobs` jobs.
    """
    def __init__(self, jtracker: JavaObject) -> None: ...
    def getJobIdsForGroup(self, jobGroup: str | None = None) -> List[int]:
        """
        Return a list of all known jobs in a particular job group.  If
        `jobGroup` is None, then returns all known jobs that are not
        associated with a job group.

        The returned list may contain running, failed, and completed jobs,
        and may vary across invocations of this method. This method does
        not guarantee the order of the elements in its result.
        """
    def getActiveStageIds(self) -> List[int]:
        """
        Returns an array containing the ids of all active stages.
        """
    def getActiveJobsIds(self) -> List[int]:
        """
        Returns an array containing the ids of all active jobs.
        """
    def getJobInfo(self, jobId: int) -> SparkJobInfo | None:
        """
        Returns a :class:`SparkJobInfo` object, or None if the job info
        could not be found or was garbage collected.
        """
    def getStageInfo(self, stageId: int) -> SparkStageInfo | None:
        """
        Returns a :class:`SparkStageInfo` object, or None if the stage
        info could not be found or was garbage collected.
        """
