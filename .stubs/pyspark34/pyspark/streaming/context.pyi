from py4j.java_gateway import JavaObject
from pyspark import RDD
from pyspark.context import SparkContext
from pyspark.storagelevel import StorageLevel
from pyspark.streaming.dstream import DStream
from pyspark.streaming.listener import StreamingListener
from typing import Any, Callable, List, TypeVar

__all__ = ['StreamingContext']

T = TypeVar('T')

class StreamingContext:
    """
    Main entry point for Spark Streaming functionality. A StreamingContext
    represents the connection to a Spark cluster, and can be used to create
    :class:`DStream` various input sources. It can be from an existing :class:`SparkContext`.
    After creating and transforming DStreams, the streaming computation can
    be started and stopped using `context.start()` and `context.stop()`,
    respectively. `context.awaitTermination()` allows the current thread
    to wait for the termination of the context by `stop()` or by an exception.

    .. deprecated:: Spark 3.4.0
       This is deprecated as of Spark 3.4.0.
       There are no longer updates to DStream and it's a legacy project.
       There is a newer and easier to use streaming engine in Spark called Structured Streaming.
       You should use Spark Structured Streaming for your streaming applications.

    Parameters
    ----------
    sparkContext : :class:`SparkContext`
        SparkContext object.
    batchDuration : int, optional
        the time interval (in seconds) at which streaming
        data will be divided into batches
    """
    def __init__(self, sparkContext: SparkContext, batchDuration: int | None = None, jssc: JavaObject | None = None) -> None: ...
    @classmethod
    def getOrCreate(cls, checkpointPath: str, setupFunc: Callable[[], 'StreamingContext']) -> StreamingContext:
        """
        Either recreate a StreamingContext from checkpoint data or create a new StreamingContext.
        If checkpoint data exists in the provided `checkpointPath`, then StreamingContext will be
        recreated from the checkpoint data. If the data does not exist, then the provided setupFunc
        will be used to create a new context.

        Parameters
        ----------
        checkpointPath : str
            Checkpoint directory used in an earlier streaming program
        setupFunc : function
            Function to create a new context and setup DStreams
        """
    @classmethod
    def getActive(cls) -> StreamingContext | None:
        """
        Return either the currently active StreamingContext (i.e., if there is a context started
        but not stopped) or None.
        """
    @classmethod
    def getActiveOrCreate(cls, checkpointPath: str, setupFunc: Callable[[], 'StreamingContext']) -> StreamingContext:
        """
        Either return the active StreamingContext (i.e. currently started but not stopped),
        or recreate a StreamingContext from checkpoint data or create a new StreamingContext
        using the provided setupFunc function. If the checkpointPath is None or does not contain
        valid checkpoint data, then setupFunc will be called to create a new context and setup
        DStreams.

        Parameters
        ----------
        checkpointPath : str
            Checkpoint directory used in an earlier streaming program. Can be
            None if the intention is to always create a new context when there
            is no active context.
        setupFunc : function
            Function to create a new JavaStreamingContext and setup DStreams
        """
    @property
    def sparkContext(self) -> SparkContext:
        """
        Return SparkContext which is associated with this StreamingContext.
        """
    def start(self) -> None:
        """
        Start the execution of the streams.
        """
    def awaitTermination(self, timeout: int | None = None) -> None:
        """
        Wait for the execution to stop.

        Parameters
        ----------
        timeout : int, optional
            time to wait in seconds
        """
    def awaitTerminationOrTimeout(self, timeout: int) -> None:
        """
        Wait for the execution to stop. Return `true` if it's stopped; or
        throw the reported error during the execution; or `false` if the
        waiting time elapsed before returning from the method.

        Parameters
        ----------
        timeout : int
            time to wait in seconds
        """
    def stop(self, stopSparkContext: bool = True, stopGraceFully: bool = False) -> None:
        """
        Stop the execution of the streams, with option of ensuring all
        received data has been processed.

        Parameters
        ----------
        stopSparkContext : bool, optional
            Stop the associated SparkContext or not
        stopGracefully : bool, optional
            Stop gracefully by waiting for the processing of all received
            data to be completed
        """
    def remember(self, duration: int) -> None:
        """
        Set each DStreams in this context to remember RDDs it generated
        in the last given duration. DStreams remember RDDs only for a
        limited duration of time and releases them for garbage collection.
        This method allows the developer to specify how long to remember
        the RDDs (if the developer wishes to query old data outside the
        DStream computation).

        Parameters
        ----------
        duration : int
            Minimum duration (in seconds) that each DStream should remember its RDDs
        """
    def checkpoint(self, directory: str) -> None:
        """
        Sets the context to periodically checkpoint the DStream operations for master
        fault-tolerance. The graph will be checkpointed every batch interval.

        Parameters
        ----------
        directory : str
            HDFS-compatible directory where the checkpoint data will be reliably stored
        """
    def socketTextStream(self, hostname: str, port: int, storageLevel: StorageLevel = ...) -> DStream[str]:
        """
        Create an input from TCP source hostname:port. Data is received using
        a TCP socket and receive byte is interpreted as UTF8 encoded ``\\n`` delimited
        lines.

        Parameters
        ----------
        hostname : str
            Hostname to connect to for receiving data
        port : int
            Port to connect to for receiving data
        storageLevel : :class:`pyspark.StorageLevel`, optional
            Storage level to use for storing the received objects
        """
    def textFileStream(self, directory: str) -> DStream[str]:
        '''
        Create an input stream that monitors a Hadoop-compatible file system
        for new files and reads them as text files. Files must be written to the
        monitored directory by "moving" them from another location within the same
        file system. File names starting with . are ignored.
        The text files must be encoded as UTF-8.
        '''
    def binaryRecordsStream(self, directory: str, recordLength: int) -> DStream[bytes]:
        '''
        Create an input stream that monitors a Hadoop-compatible file system
        for new files and reads them as flat binary files with records of
        fixed length. Files must be written to the monitored directory by "moving"
        them from another location within the same file system.
        File names starting with . are ignored.

        Parameters
        ----------
        directory : str
            Directory to load data from
        recordLength : int
            Length of each record in bytes
        '''
    def queueStream(self, rdds: List[RDD[T]], oneAtATime: bool = True, default: RDD[T] | None = None) -> DStream[T]:
        """
        Create an input stream from a queue of RDDs or list. In each batch,
        it will process either one or all of the RDDs returned by the queue.

        Parameters
        ----------
        rdds : list
            Queue of RDDs
        oneAtATime : bool, optional
            pick one rdd each time or pick all of them once.
        default : :class:`pyspark.RDD`, optional
            The default rdd if no more in rdds

        Notes
        -----
        Changes to the queue after the stream is created will not be recognized.
        """
    def transform(self, dstreams: List['DStream[Any]'], transformFunc: Callable[..., RDD[T]]) -> DStream[T]:
        """
        Create a new DStream in which each RDD is generated by applying
        a function on RDDs of the DStreams. The order of the JavaRDDs in
        the transform function parameter will be the same as the order
        of corresponding DStreams in the list.
        """
    def union(self, *dstreams: DStream[T]) -> DStream[T]:
        """
        Create a unified DStream from multiple DStreams of the same
        type and same slide duration.
        """
    def addStreamingListener(self, streamingListener: StreamingListener) -> None:
        """
        Add a [[org.apache.spark.streaming.scheduler.StreamingListener]] object for
        receiving system events related to streaming.
        """
