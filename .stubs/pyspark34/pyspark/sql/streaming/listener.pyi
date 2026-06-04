import abc
import uuid
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from py4j.java_gateway import JavaObject
from pyspark.sql import Row
from typing import Dict, List

__all__ = ['StreamingQueryListener']

class StreamingQueryListener(ABC, metaclass=abc.ABCMeta):
    """
    Interface for listening to events related to :class:`~pyspark.sql.streaming.StreamingQuery`.

    .. versionadded:: 3.4.0

    Notes
    -----
    The methods are not thread-safe as they may be called from different threads.
    The events received are identical with Scala API. Refer to its documentation.

    This API is evolving.

    Examples
    --------
    >>> class MyListener(StreamingQueryListener):
    ...    def onQueryStarted(self, event: QueryStartedEvent) -> None:
    ...        # Do something with event.
    ...        pass
    ...
    ...    def onQueryProgress(self, event: QueryProgressEvent) -> None:
    ...        # Do something with event.
    ...        pass
    ...
    ...    def onQueryTerminated(self, event: QueryTerminatedEvent) -> None:
    ...        # Do something with event.
    ...        pass
    ...
    >>> spark.streams.addListener(MyListener())
    """
    @abstractmethod
    def onQueryStarted(self, event: QueryStartedEvent) -> None:
        """
        Called when a query is started.

        Notes
        -----
        This is called synchronously with :py:meth:`~pyspark.sql.streaming.DataStreamWriter.start`,
        that is, `onQueryStart` will be called on all listeners before `DataStreamWriter.start()`
        returns the corresponding :class:`~pyspark.sql.streaming.StreamingQuery`.
        Please don't block this method as it will block your query.
        """
    @abstractmethod
    def onQueryProgress(self, event: QueryProgressEvent) -> None:
        """
        Called when there is some status update (ingestion rate updated, etc.)

        Notes
        -----
        This method is asynchronous. The status in :class:`~pyspark.sql.streaming.StreamingQuery`
        will always be latest no matter when this method is called. Therefore, the status of
        :class:`~pyspark.sql.streaming.StreamingQuery`.
        may be changed before/when you process the event. E.g., you may find
        :class:`~pyspark.sql.streaming.StreamingQuery` is terminated when you are
        processing `QueryProgressEvent`.
        """
    @abstractmethod
    def onQueryTerminated(self, event: QueryTerminatedEvent) -> None:
        """
        Called when a query is stopped, with or without error.
        """

class JStreamingQueryListener:
    """
    Python class that implements Java interface by Py4J.
    """
    pylistener: Incomplete
    def __init__(self, pylistener: StreamingQueryListener) -> None: ...
    def onQueryStarted(self, jevent: JavaObject) -> None: ...
    def onQueryProgress(self, jevent: JavaObject) -> None: ...
    def onQueryTerminated(self, jevent: JavaObject) -> None: ...
    class Java:
        implements: Incomplete

class QueryStartedEvent:
    """
    Event representing the start of a query.

    .. versionadded:: 3.4.0

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, jevent: JavaObject) -> None: ...
    @property
    def id(self) -> uuid.UUID:
        """
        A unique query id that persists across restarts. See
        py:meth:`~pyspark.sql.streaming.StreamingQuery.id`.
        """
    @property
    def runId(self) -> uuid.UUID:
        """
        A query id that is unique for every start/restart. See
        py:meth:`~pyspark.sql.streaming.StreamingQuery.runId`.
        """
    @property
    def name(self) -> str | None:
        """
        User-specified name of the query, `None` if not specified.
        """
    @property
    def timestamp(self) -> str:
        """
        The timestamp to start a query.
        """

class QueryProgressEvent:
    """
    Event representing any progress updates in a query.

    .. versionadded:: 3.4.0

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, jevent: JavaObject) -> None: ...
    @property
    def progress(self) -> StreamingQueryProgress:
        """
        The query progress updates.
        """

class QueryTerminatedEvent:
    """
    Event representing that termination of a query.

    .. versionadded:: 3.4.0

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, jevent: JavaObject) -> None: ...
    @property
    def id(self) -> uuid.UUID:
        """
        A unique query id that persists across restarts. See
        py:meth:`~pyspark.sql.streaming.StreamingQuery.id`.
        """
    @property
    def runId(self) -> uuid.UUID:
        """
        A query id that is unique for every start/restart. See
        py:meth:`~pyspark.sql.streaming.StreamingQuery.runId`.
        """
    @property
    def exception(self) -> str | None:
        """
        The exception message of the query if the query was terminated
        with an exception. Otherwise, it will be `None`.
        """

class StreamingQueryProgress:
    """
    .. versionadded:: 3.4.0

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, jprogress: JavaObject) -> None: ...
    @property
    def id(self) -> uuid.UUID:
        """
        A unique query id that persists across restarts. See
        py:meth:`~pyspark.sql.streaming.StreamingQuery.id`.
        """
    @property
    def runId(self) -> uuid.UUID:
        """
        A query id that is unique for every start/restart. See
        py:meth:`~pyspark.sql.streaming.StreamingQuery.runId`.
        """
    @property
    def name(self) -> str | None:
        """
        User-specified name of the query, `None` if not specified.
        """
    @property
    def timestamp(self) -> str:
        """
        The timestamp to start a query.
        """
    @property
    def batchId(self) -> int:
        """
        A unique id for the current batch of data being processed.  Note that in the
        case of retries after a failure a given batchId my be executed more than once.
        Similarly, when there is no data to be processed, the batchId will not be
        incremented.
        """
    @property
    def batchDuration(self) -> int:
        """
        The process duration of each batch.
        """
    @property
    def durationMs(self) -> Dict[str, int]:
        """
        The amount of time taken to perform various operations in milliseconds.
        """
    @property
    def eventTime(self) -> Dict[str, str]:
        '''
        Statistics of event time seen in this batch. It may contain the following keys:

        .. code-block:: python

            {
                "max": "2016-12-05T20:54:20.827Z",  # maximum event time seen in this trigger
                "min": "2016-12-05T20:54:20.827Z",  # minimum event time seen in this trigger
                "avg": "2016-12-05T20:54:20.827Z",  # average event time seen in this trigger
                "watermark": "2016-12-05T20:54:20.827Z"  # watermark used in this trigger
            }

        All timestamps are in ISO8601 format, i.e. UTC timestamps.
        '''
    @property
    def stateOperators(self) -> List['StateOperatorProgress']:
        """
        Information about operators in the query that store state.
        """
    @property
    def sources(self) -> List['SourceProgress']:
        """
        detailed statistics on data being read from each of the streaming sources.
        """
    @property
    def sink(self) -> SinkProgress:
        """
        A unique query id that persists across restarts. See
        py:meth:`~pyspark.sql.streaming.StreamingQuery.id`.
        """
    @property
    def observedMetrics(self) -> Dict[str, Row]: ...
    @property
    def numInputRows(self) -> str | None:
        """
        The aggregate (across all sources) number of records processed in a trigger.
        """
    @property
    def inputRowsPerSecond(self) -> str:
        """
        The aggregate (across all sources) rate of data arriving.
        """
    @property
    def processedRowsPerSecond(self) -> str:
        """
        The aggregate (across all sources) rate at which Spark is processing data..
        """
    @property
    def json(self) -> str:
        """
        The compact JSON representation of this progress.
        """
    @property
    def prettyJson(self) -> str:
        """
        The pretty (i.e. indented) JSON representation of this progress.
        """

class StateOperatorProgress:
    """
    .. versionadded:: 3.4.0

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, jprogress: JavaObject) -> None: ...
    @property
    def operatorName(self) -> str: ...
    @property
    def numRowsTotal(self) -> int: ...
    @property
    def numRowsUpdated(self) -> int: ...
    @property
    def allUpdatesTimeMs(self) -> int: ...
    @property
    def numRowsRemoved(self) -> int: ...
    @property
    def allRemovalsTimeMs(self) -> int: ...
    @property
    def commitTimeMs(self) -> int: ...
    @property
    def memoryUsedBytes(self) -> int: ...
    @property
    def numRowsDroppedByWatermark(self) -> int: ...
    @property
    def numShufflePartitions(self) -> int: ...
    @property
    def numStateStoreInstances(self) -> int: ...
    @property
    def customMetrics(self) -> Dict[str, int]: ...
    @property
    def json(self) -> str:
        """
        The compact JSON representation of this progress.
        """
    @property
    def prettyJson(self) -> str:
        """
        The pretty (i.e. indented) JSON representation of this progress.
        """

class SourceProgress:
    """
    .. versionadded:: 3.4.0

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, jprogress: JavaObject) -> None: ...
    @property
    def description(self) -> str:
        """
        Description of the source.
        """
    @property
    def startOffset(self) -> str:
        """
        The starting offset for data being read.
        """
    @property
    def endOffset(self) -> str:
        """
        The ending offset for data being read.
        """
    @property
    def latestOffset(self) -> str:
        """
        The latest offset from this source.
        """
    @property
    def numInputRows(self) -> int:
        """
        The number of records read from this source.
        """
    @property
    def inputRowsPerSecond(self) -> float:
        """
        The rate at which data is arriving from this source.
        """
    @property
    def processedRowsPerSecond(self) -> float:
        """
        The rate at which data from this source is being processed by Spark.
        """
    @property
    def metrics(self) -> Dict[str, str]: ...
    @property
    def json(self) -> str:
        """
        The compact JSON representation of this progress.
        """
    @property
    def prettyJson(self) -> str:
        """
        The pretty (i.e. indented) JSON representation of this progress.
        """

class SinkProgress:
    """
    .. versionadded:: 3.4.0

    Notes
    -----
    This API is evolving.
    """
    def __init__(self, jprogress: JavaObject) -> None: ...
    @property
    def description(self) -> str:
        """
        Description of the source.
        """
    @property
    def numOutputRows(self) -> int:
        """
        Number of rows written to the sink or -1 for Continuous Mode (temporarily)
        or Sink V1 (until decommissioned).
        """
    @property
    def metrics(self) -> Dict[str, str]: ...
    @property
    def json(self) -> str:
        """
        The compact JSON representation of this progress.
        """
    @property
    def prettyJson(self) -> str:
        """
        The pretty (i.e. indented) JSON representation of this progress.
        """
