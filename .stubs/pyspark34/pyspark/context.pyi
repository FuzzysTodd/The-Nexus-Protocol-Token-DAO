from py4j.java_gateway import JavaGateway, JavaObject
from pyspark.accumulators import Accumulator, AccumulatorParam
from pyspark.broadcast import Broadcast
from pyspark.conf import SparkConf
from pyspark.profiler import BasicProfiler, MemoryProfiler, ProfilerCollector, UDFBasicProfiler
from pyspark.rdd import RDD
from pyspark.resource.information import ResourceInformation
from pyspark.serializers import Serializer
from pyspark.status import StatusTracker
from types import TracebackType
from typing import Any, Callable, Dict, Iterable, List, NoReturn, Sequence, Tuple, Type, TypeVar

__all__ = ['SparkContext']

T = TypeVar('T')
U = TypeVar('U')

class SparkContext:
    """
    Main entry point for Spark functionality. A SparkContext represents the
    connection to a Spark cluster, and can be used to create :class:`RDD` and
    broadcast variables on that cluster.

    When you create a new SparkContext, at least the master and app name should
    be set, either through the named parameters here or through `conf`.

    Parameters
    ----------
    master : str, optional
        Cluster URL to connect to (e.g. mesos://host:port, spark://host:port, local[4]).
    appName : str, optional
        A name for your job, to display on the cluster web UI.
    sparkHome : str, optional
        Location where Spark is installed on cluster nodes.
    pyFiles : list, optional
        Collection of .zip or .py files to send to the cluster
        and add to PYTHONPATH.  These can be paths on the local file
        system or HDFS, HTTP, HTTPS, or FTP URLs.
    environment : dict, optional
        A dictionary of environment variables to set on
        worker nodes.
    batchSize : int, optional, default 0
        The number of Python objects represented as a single
        Java object. Set 1 to disable batching, 0 to automatically choose
        the batch size based on object sizes, or -1 to use an unlimited
        batch size
    serializer : :class:`Serializer`, optional, default :class:`CPickleSerializer`
        The serializer for RDDs.
    conf : :class:`SparkConf`, optional
        An object setting Spark properties.
    gateway : class:`py4j.java_gateway.JavaGateway`,  optional
        Use an existing gateway and JVM, otherwise a new JVM
        will be instantiated. This is only used internally.
    jsc : class:`py4j.java_gateway.JavaObject`, optional
        The JavaSparkContext instance. This is only used internally.
    profiler_cls : type, optional, default :class:`BasicProfiler`
        A class of custom Profiler used to do profiling
    udf_profiler_cls : type, optional, default :class:`UDFBasicProfiler`
        A class of custom Profiler used to do udf profiling

    Notes
    -----
    Only one :class:`SparkContext` should be active per JVM. You must `stop()`
    the active :class:`SparkContext` before creating a new one.

    :class:`SparkContext` instance is not supported to share across multiple
    processes out of the box, and PySpark does not guarantee multi-processing execution.
    Use threads instead for concurrent processing purpose.

    Examples
    --------
    >>> from pyspark.context import SparkContext
    >>> sc = SparkContext('local', 'test')
    >>> sc2 = SparkContext('local', 'test2') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: ...
    """
    serializer: Serializer
    profiler_collector: ProfilerCollector
    PACKAGE_EXTENSIONS: Iterable[str]
    def __init__(self, master: str | None = None, appName: str | None = None, sparkHome: str | None = None, pyFiles: List[str] | None = None, environment: Dict[str, Any] | None = None, batchSize: int = 0, serializer: Serializer = ..., conf: SparkConf | None = None, gateway: JavaGateway | None = None, jsc: JavaObject | None = None, profiler_cls: Type[BasicProfiler] = ..., udf_profiler_cls: Type[UDFBasicProfiler] = ..., memory_profiler_cls: Type[MemoryProfiler] = ...) -> None: ...
    def __getnewargs__(self) -> NoReturn: ...
    def __enter__(self) -> SparkContext:
        """
        Enable 'with SparkContext(...) as sc: app(sc)' syntax.
        """
    def __exit__(self, type: Type[BaseException] | None, value: BaseException | None, trace: TracebackType | None) -> None:
        """
        Enable 'with SparkContext(...) as sc: app' syntax.

        Specifically stop the context on exit of the with block.
        """
    @classmethod
    def getOrCreate(cls, conf: SparkConf | None = None) -> SparkContext:
        """
        Get or instantiate a :class:`SparkContext` and register it as a singleton object.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        conf : :class:`SparkConf`, optional
            :class:`SparkConf` that will be used for initialization of the :class:`SparkContext`.

        Returns
        -------
        :class:`SparkContext`
            current :class:`SparkContext`, or a new one if it wasn't created before the function
            call.

        Examples
        --------
        >>> SparkContext.getOrCreate()
        <SparkContext ...>
        """
    def setLogLevel(self, logLevel: str) -> None:
        '''
        Control our logLevel. This overrides any user-defined log settings.
        Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN

        .. versionadded:: 1.4.0

        Parameters
        ----------
        logLevel : str
            The desired log level as a string.

        Examples
        --------
        >>> sc.setLogLevel("WARN")  # doctest :+SKIP
        '''
    @classmethod
    def setSystemProperty(cls, key: str, value: str) -> None:
        """
        Set a Java system property, such as `spark.executor.memory`. This must
        be invoked before instantiating :class:`SparkContext`.

        .. versionadded:: 0.9.0

        Parameters
        ----------
        key : str
            The key of a new Java system property.
        value : str
            The value of a new Java system property.
        """
    @property
    def version(self) -> str:
        """
        The version of Spark on which this application is running.

        .. versionadded:: 1.1.0

        Examples
        --------
        >>> _ = sc.version
        """
    @property
    def applicationId(self) -> str:
        """
        A unique identifier for the Spark application.
        Its format depends on the scheduler implementation.

        * in case of local spark app something like 'local-1433865536131'
        * in case of YARN something like 'application_1433865536131_34483'

        .. versionadded:: 1.5.0

        Examples
        --------
        >>> sc.applicationId  # doctest: +ELLIPSIS
        'local-...'
        """
    @property
    def uiWebUrl(self) -> str | None:
        """Return the URL of the SparkUI instance started by this :class:`SparkContext`

        .. versionadded:: 2.1.0

        Notes
        -----
        When the web ui is disabled, e.g., by ``spark.ui.enabled`` set to ``False``,
        it returns ``None``.

        Examples
        --------
        >>> sc.uiWebUrl
        'http://...'
        """
    @property
    def startTime(self) -> int:
        """Return the epoch time when the :class:`SparkContext` was started.

        .. versionadded:: 1.5.0

        Examples
        --------
        >>> _ = sc.startTime
        """
    @property
    def defaultParallelism(self) -> int:
        """
        Default level of parallelism to use when not given by user (e.g. for reduce tasks)

        .. versionadded:: 0.7.0

        Examples
        --------
        >>> sc.defaultParallelism > 0
        True
        """
    @property
    def defaultMinPartitions(self) -> int:
        """
        Default min number of partitions for Hadoop RDDs when not given by user

        .. versionadded:: 1.1.0

        Examples
        --------
        >>> sc.defaultMinPartitions > 0
        True
        """
    def stop(self) -> None:
        """
        Shut down the :class:`SparkContext`.

        .. versionadded:: 0.7.0
        """
    def emptyRDD(self) -> RDD[Any]:
        """
        Create an :class:`RDD` that has no partitions or elements.

        .. versionadded:: 1.5.0

        Returns
        -------
        :class:`RDD`
            An empty RDD

        Examples
        --------
        >>> sc.emptyRDD()
        EmptyRDD...
        >>> sc.emptyRDD().count()
        0
        """
    def range(self, start: int, end: int | None = None, step: int = 1, numSlices: int | None = None) -> RDD[int]:
        """
        Create a new RDD of int containing elements from `start` to `end`
        (exclusive), increased by `step` every element. Can be called the same
        way as python's built-in range() function. If called with a single argument,
        the argument is interpreted as `end`, and `start` is set to 0.

        .. versionadded:: 1.5.0

        Parameters
        ----------
        start : int
            the start value
        end : int, optional
            the end value (exclusive)
        step : int, optional, default 1
            the incremental step
        numSlices : int, optional
            the number of partitions of the new RDD

        Returns
        -------
        :class:`RDD`
            An RDD of int

        See Also
        --------
        :meth:`pyspark.sql.SparkSession.range`

        Examples
        --------
        >>> sc.range(5).collect()
        [0, 1, 2, 3, 4]
        >>> sc.range(2, 4).collect()
        [2, 3]
        >>> sc.range(1, 7, 2).collect()
        [1, 3, 5]

        Generate RDD with a negative step

        >>> sc.range(5, 0, -1).collect()
        [5, 4, 3, 2, 1]
        >>> sc.range(0, 5, -1).collect()
        []

        Control the number of partitions

        >>> sc.range(5, numSlices=1).getNumPartitions()
        1
        >>> sc.range(5, numSlices=10).getNumPartitions()
        10
        """
    def parallelize(self, c: Iterable[T], numSlices: int | None = None) -> RDD[T]:
        '''
        Distribute a local Python collection to form an RDD. Using range
        is recommended if the input represents a range for performance.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        c : :class:`collections.abc.Iterable`
            iterable collection to distribute
        numSlices : int, optional
            the number of partitions of the new RDD

        Returns
        -------
        :class:`RDD`
            RDD representing distributed collection.

        Examples
        --------
        >>> sc.parallelize([0, 2, 3, 4, 6], 5).glom().collect()
        [[0], [2], [3], [4], [6]]
        >>> sc.parallelize(range(0, 6, 2), 5).glom().collect()
        [[], [0], [], [2], [4]]

        Deal with a list of strings.

        >>> strings = ["a", "b", "c"]
        >>> sc.parallelize(strings, 2).glom().collect()
        [[\'a\'], [\'b\', \'c\']]
        '''
    def pickleFile(self, name: str, minPartitions: int | None = None) -> RDD[Any]:
        '''
        Load an RDD previously saved using :meth:`RDD.saveAsPickleFile` method.

        .. versionadded:: 1.1.0

        Parameters
        ----------
        name : str
            directory to the input data files, the path can be comma separated
            paths as a list of inputs
        minPartitions : int, optional
            suggested minimum number of partitions for the resulting RDD

        Returns
        -------
        :class:`RDD`
            RDD representing unpickled data from the file(s).

        See Also
        --------
        :meth:`RDD.saveAsPickleFile`

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary pickled file
        ...     path1 = os.path.join(d, "pickled1")
        ...     sc.parallelize(range(10)).saveAsPickleFile(path1, 3)
        ...
        ...     # Write another temporary pickled file
        ...     path2 = os.path.join(d, "pickled2")
        ...     sc.parallelize(range(-10, -5)).saveAsPickleFile(path2, 3)
        ...
        ...     # Load picked file
        ...     collected1 = sorted(sc.pickleFile(path1, 3).collect())
        ...     collected2 = sorted(sc.pickleFile(path2, 4).collect())
        ...
        ...     # Load two picked files together
        ...     collected3 = sorted(sc.pickleFile(\'{},{}\'.format(path1, path2), 5).collect())

        >>> collected1
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> collected2
        [-10, -9, -8, -7, -6]
        >>> collected3
        [-10, -9, -8, -7, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        '''
    def textFile(self, name: str, minPartitions: int | None = None, use_unicode: bool = True) -> RDD[str]:
        '''
        Read a text file from HDFS, a local file system (available on all
        nodes), or any Hadoop-supported file system URI, and return it as an
        RDD of Strings. The text files must be encoded as UTF-8.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        name : str
            directory to the input data files, the path can be comma separated
            paths as a list of inputs
        minPartitions : int, optional
            suggested minimum number of partitions for the resulting RDD
        use_unicode : bool, default True
            If `use_unicode` is False, the strings will be kept as `str` (encoding
            as `utf-8`), which is faster and smaller than unicode.

            .. versionadded:: 1.2.0

        Returns
        -------
        :class:`RDD`
            RDD representing text data from the file(s).

        See Also
        --------
        :meth:`RDD.saveAsTextFile`
        :meth:`SparkContext.wholeTextFiles`

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     path1 = os.path.join(d, "text1")
        ...     path2 = os.path.join(d, "text2")
        ...
        ...     # Write a temporary text file
        ...     sc.parallelize(["x", "y", "z"]).saveAsTextFile(path1)
        ...
        ...     # Write another temporary text file
        ...     sc.parallelize(["aa", "bb", "cc"]).saveAsTextFile(path2)
        ...
        ...     # Load text file
        ...     collected1 = sorted(sc.textFile(path1, 3).collect())
        ...     collected2 = sorted(sc.textFile(path2, 4).collect())
        ...
        ...     # Load two text files together
        ...     collected3 = sorted(sc.textFile(\'{},{}\'.format(path1, path2), 5).collect())

        >>> collected1
        [\'x\', \'y\', \'z\']
        >>> collected2
        [\'aa\', \'bb\', \'cc\']
        >>> collected3
        [\'aa\', \'bb\', \'cc\', \'x\', \'y\', \'z\']
        '''
    def wholeTextFiles(self, path: str, minPartitions: int | None = None, use_unicode: bool = True) -> RDD[Tuple[str, str]]:
        '''
        Read a directory of text files from HDFS, a local file system
        (available on all nodes), or any  Hadoop-supported file system
        URI. Each file is read as a single record and returned in a
        key-value pair, where the key is the path of each file, the
        value is the content of each file.
        The text files must be encoded as UTF-8.

        .. versionadded:: 1.0.0

        For example, if you have the following files:

        .. code-block:: text

            hdfs://a-hdfs-path/part-00000
            hdfs://a-hdfs-path/part-00001
            ...
            hdfs://a-hdfs-path/part-nnnnn

        Do ``rdd = sparkContext.wholeTextFiles("hdfs://a-hdfs-path")``,
        then ``rdd`` contains:

        .. code-block:: text

            (a-hdfs-path/part-00000, its content)
            (a-hdfs-path/part-00001, its content)
            ...
            (a-hdfs-path/part-nnnnn, its content)

        Parameters
        ----------
        path : str
            directory to the input data files, the path can be comma separated
            paths as a list of inputs
        minPartitions : int, optional
            suggested minimum number of partitions for the resulting RDD
        use_unicode : bool, default True
            If `use_unicode` is False, the strings will be kept as `str` (encoding
            as `utf-8`), which is faster and smaller than unicode.

            .. versionadded:: 1.2.0

        Returns
        -------
        :class:`RDD`
            RDD representing path-content pairs from the file(s).

        Notes
        -----
        Small files are preferred, as each file will be loaded fully in memory.

        See Also
        --------
        :meth:`RDD.saveAsTextFile`
        :meth:`SparkContext.textFile`

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary text file
        ...     with open(os.path.join(d, "1.txt"), "w") as f:
        ...         _ = f.write("123")
        ...
        ...     # Write another temporary text file
        ...     with open(os.path.join(d, "2.txt"), "w") as f:
        ...         _ = f.write("xyz")
        ...
        ...     collected = sorted(sc.wholeTextFiles(d).collect())
        >>> collected
        [(\'.../1.txt\', \'123\'), (\'.../2.txt\', \'xyz\')]
        '''
    def binaryFiles(self, path: str, minPartitions: int | None = None) -> RDD[Tuple[str, bytes]]:
        '''
        Read a directory of binary files from HDFS, a local file system
        (available on all nodes), or any Hadoop-supported file system URI
        as a byte array. Each file is read as a single record and returned
        in a key-value pair, where the key is the path of each file, the
        value is the content of each file.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        path : str
            directory to the input data files, the path can be comma separated
            paths as a list of inputs
        minPartitions : int, optional
            suggested minimum number of partitions for the resulting RDD

        Returns
        -------
        :class:`RDD`
            RDD representing path-content pairs from the file(s).

        Notes
        -----
        Small files are preferred, large file is also allowable, but may cause bad performance.

        See Also
        --------
        :meth:`SparkContext.binaryRecords`

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary binary file
        ...     with open(os.path.join(d, "1.bin"), "wb") as f1:
        ...         _ = f1.write(b"binary data I")
        ...
        ...     # Write another temporary binary file
        ...     with open(os.path.join(d, "2.bin"), "wb") as f2:
        ...         _ = f2.write(b"binary data II")
        ...
        ...     collected = sorted(sc.binaryFiles(d).collect())

        >>> collected
        [(\'.../1.bin\', b\'binary data I\'), (\'.../2.bin\', b\'binary data II\')]
        '''
    def binaryRecords(self, path: str, recordLength: int) -> RDD[bytes]:
        '''
        Load data from a flat binary file, assuming each record is a set of numbers
        with the specified numerical format (see ByteBuffer), and the number of
        bytes per record is constant.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        path : str
            Directory to the input data files
        recordLength : int
            The length at which to split the records

        Returns
        -------
        :class:`RDD`
            RDD of data with values, represented as byte arrays

        See Also
        --------
        :meth:`SparkContext.binaryFiles`

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # Write a temporary file
        ...     with open(os.path.join(d, "1.bin"), "w") as f:
        ...         for i in range(3):
        ...             _ = f.write("%04d" % i)
        ...
        ...     # Write another file
        ...     with open(os.path.join(d, "2.bin"), "w") as f:
        ...         for i in [-1, -2, -10]:
        ...             _ = f.write("%04d" % i)
        ...
        ...     collected = sorted(sc.binaryRecords(d, 4).collect())

        >>> collected
        [b\'-001\', b\'-002\', b\'-010\', b\'0000\', b\'0001\', b\'0002\']
        '''
    def sequenceFile(self, path: str, keyClass: str | None = None, valueClass: str | None = None, keyConverter: str | None = None, valueConverter: str | None = None, minSplits: int | None = None, batchSize: int = 0) -> RDD[Tuple[T, U]]:
        '''
        Read a Hadoop SequenceFile with arbitrary key and value Writable class from HDFS,
        a local file system (available on all nodes), or any Hadoop-supported file system URI.
        The mechanism is as follows:

            1. A Java RDD is created from the SequenceFile or other InputFormat, and the key
               and value Writable classes
            2. Serialization is attempted via Pickle pickling
            3. If this fails, the fallback is to call \'toString\' on each key and value
            4. :class:`CPickleSerializer` is used to deserialize pickled objects on the Python side

        .. versionadded:: 1.3.0

        Parameters
        ----------
        path : str
            path to sequencefile
        keyClass: str, optional
            fully qualified classname of key Writable class (e.g. "org.apache.hadoop.io.Text")
        valueClass : str, optional
            fully qualified classname of value Writable class
            (e.g. "org.apache.hadoop.io.LongWritable")
        keyConverter : str, optional
            fully qualified name of a function returning key WritableConverter
        valueConverter : str, optional
            fully qualifiedname of a function returning value WritableConverter
        minSplits : int, optional
            minimum splits in dataset (default min(2, sc.defaultParallelism))
        batchSize : int, optional, default 0
            The number of Python objects represented as a single
            Java object. (default 0, choose batchSize automatically)

        Returns
        -------
        :class:`RDD`
            RDD of tuples of key and corresponding value

        See Also
        --------
        :meth:`RDD.saveAsSequenceFile`
        :meth:`RDD.saveAsNewAPIHadoopFile`
        :meth:`RDD.saveAsHadoopFile`
        :meth:`SparkContext.newAPIHadoopFile`
        :meth:`SparkContext.hadoopFile`

        Examples
        --------
        >>> import os
        >>> import tempfile

        Set the class of output format

        >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "hadoop_file")
        ...
        ...     # Write a temporary Hadoop file
        ...     rdd = sc.parallelize([(1, {3.0: "bb"}), (2, {1.0: "aa"}), (3, {2.0: "dd"})])
        ...     rdd.saveAsNewAPIHadoopFile(path, output_format_class)
        ...
        ...     collected = sorted(sc.sequenceFile(path).collect())

        >>> collected
        [(1, {3.0: \'bb\'}), (2, {1.0: \'aa\'}), (3, {2.0: \'dd\'})]
        '''
    def newAPIHadoopFile(self, path: str, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: str | None = None, valueConverter: str | None = None, conf: Dict[str, str] | None = None, batchSize: int = 0) -> RDD[Tuple[T, U]]:
        '''
        Read a \'new API\' Hadoop InputFormat with arbitrary key and value class from HDFS,
        a local file system (available on all nodes), or any Hadoop-supported file system URI.
        The mechanism is the same as for meth:`SparkContext.sequenceFile`.

        A Hadoop configuration can be passed in as a Python dict. This will be converted into a
        Configuration in Java

        .. versionadded:: 1.1.0

        Parameters
        ----------
        path : str
            path to Hadoop file
        inputFormatClass : str
            fully qualified classname of Hadoop InputFormat
            (e.g. "org.apache.hadoop.mapreduce.lib.input.TextInputFormat")
        keyClass : str
            fully qualified classname of key Writable class
            (e.g. "org.apache.hadoop.io.Text")
        valueClass : str
            fully qualified classname of value Writable class
            (e.g. "org.apache.hadoop.io.LongWritable")
        keyConverter : str, optional
            fully qualified name of a function returning key WritableConverter
            None by default
        valueConverter : str, optional
            fully qualified name of a function returning value WritableConverter
            None by default
        conf : dict, optional
            Hadoop configuration, passed in as a dict
            None by default
        batchSize : int, optional, default 0
            The number of Python objects represented as a single
            Java object. (default 0, choose batchSize automatically)

        Returns
        -------
        :class:`RDD`
            RDD of tuples of key and corresponding value

        See Also
        --------
        :meth:`RDD.saveAsSequenceFile`
        :meth:`RDD.saveAsNewAPIHadoopFile`
        :meth:`RDD.saveAsHadoopFile`
        :meth:`SparkContext.sequenceFile`
        :meth:`SparkContext.hadoopFile`

        Examples
        --------
        >>> import os
        >>> import tempfile

        Set the related classes

        >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
        >>> input_format_class = "org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat"
        >>> key_class = "org.apache.hadoop.io.IntWritable"
        >>> value_class = "org.apache.hadoop.io.Text"

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "new_hadoop_file")
        ...
        ...     # Write a temporary Hadoop file
        ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
        ...     rdd.saveAsNewAPIHadoopFile(path, output_format_class, key_class, value_class)
        ...
        ...     loaded = sc.newAPIHadoopFile(path, input_format_class, key_class, value_class)
        ...     collected = sorted(loaded.collect())

        >>> collected
        [(1, \'\'), (1, \'a\'), (3, \'x\')]
        '''
    def newAPIHadoopRDD(self, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: str | None = None, valueConverter: str | None = None, conf: Dict[str, str] | None = None, batchSize: int = 0) -> RDD[Tuple[T, U]]:
        '''
        Read a \'new API\' Hadoop InputFormat with arbitrary key and value class, from an arbitrary
        Hadoop configuration, which is passed in as a Python dict.
        This will be converted into a Configuration in Java.
        The mechanism is the same as for meth:`SparkContext.sequenceFile`.

        .. versionadded:: 1.1.0

        Parameters
        ----------
        inputFormatClass : str
            fully qualified classname of Hadoop InputFormat
            (e.g. "org.apache.hadoop.mapreduce.lib.input.TextInputFormat")
        keyClass : str
            fully qualified classname of key Writable class (e.g. "org.apache.hadoop.io.Text")
        valueClass : str
            fully qualified classname of value Writable class
            (e.g. "org.apache.hadoop.io.LongWritable")
        keyConverter : str, optional
            fully qualified name of a function returning key WritableConverter
            (None by default)
        valueConverter : str, optional
            fully qualified name of a function returning value WritableConverter
            (None by default)
        conf : dict, optional
            Hadoop configuration, passed in as a dict (None by default)
        batchSize : int, optional, default 0
            The number of Python objects represented as a single
            Java object. (default 0, choose batchSize automatically)

        Returns
        -------
        :class:`RDD`
            RDD of tuples of key and corresponding value

        See Also
        --------
        :meth:`RDD.saveAsNewAPIHadoopDataset`
        :meth:`RDD.saveAsHadoopDataset`
        :meth:`SparkContext.hadoopRDD`
        :meth:`SparkContext.hadoopFile`

        Examples
        --------
        >>> import os
        >>> import tempfile

        Set the related classes

        >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
        >>> input_format_class = "org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat"
        >>> key_class = "org.apache.hadoop.io.IntWritable"
        >>> value_class = "org.apache.hadoop.io.Text"

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "new_hadoop_file")
        ...
        ...     # Create the conf for writing
        ...     write_conf = {
        ...         "mapreduce.job.outputformat.class": (output_format_class),
        ...         "mapreduce.job.output.key.class": key_class,
        ...         "mapreduce.job.output.value.class": value_class,
        ...         "mapreduce.output.fileoutputformat.outputdir": path,
        ...     }
        ...
        ...     # Write a temporary Hadoop file
        ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
        ...     rdd.saveAsNewAPIHadoopDataset(conf=write_conf)
        ...
        ...     # Create the conf for reading
        ...     read_conf = {"mapreduce.input.fileinputformat.inputdir": path}
        ...
        ...     loaded = sc.newAPIHadoopRDD(input_format_class,
        ...         key_class, value_class, conf=read_conf)
        ...     collected = sorted(loaded.collect())

        >>> collected
        [(1, \'\'), (1, \'a\'), (3, \'x\')]
        '''
    def hadoopFile(self, path: str, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: str | None = None, valueConverter: str | None = None, conf: Dict[str, str] | None = None, batchSize: int = 0) -> RDD[Tuple[T, U]]:
        '''
        Read an \'old\' Hadoop InputFormat with arbitrary key and value class from HDFS,
        a local file system (available on all nodes), or any Hadoop-supported file system URI.
        The mechanism is the same as for meth:`SparkContext.sequenceFile`.

        .. versionadded:: 1.1.0

        A Hadoop configuration can be passed in as a Python dict. This will be converted into a
        Configuration in Java.

        Parameters
        ----------
        path : str
            path to Hadoop file
        inputFormatClass : str
            fully qualified classname of Hadoop InputFormat
            (e.g. "org.apache.hadoop.mapreduce.lib.input.TextInputFormat")
        keyClass : str
            fully qualified classname of key Writable class (e.g. "org.apache.hadoop.io.Text")
        valueClass : str
            fully qualified classname of value Writable class
            (e.g. "org.apache.hadoop.io.LongWritable")
        keyConverter : str, optional
            fully qualified name of a function returning key WritableConverter
        valueConverter : str, optional
            fully qualified name of a function returning value WritableConverter
        conf : dict, optional
            Hadoop configuration, passed in as a dict
        batchSize : int, optional, default 0
            The number of Python objects represented as a single
            Java object. (default 0, choose batchSize automatically)

        Returns
        -------
        :class:`RDD`
            RDD of tuples of key and corresponding value

        See Also
        --------
        :meth:`RDD.saveAsSequenceFile`
        :meth:`RDD.saveAsNewAPIHadoopFile`
        :meth:`RDD.saveAsHadoopFile`
        :meth:`SparkContext.newAPIHadoopFile`
        :meth:`SparkContext.hadoopRDD`

        Examples
        --------
        >>> import os
        >>> import tempfile

        Set the related classes

        >>> output_format_class = "org.apache.hadoop.mapred.TextOutputFormat"
        >>> input_format_class = "org.apache.hadoop.mapred.TextInputFormat"
        >>> key_class = "org.apache.hadoop.io.IntWritable"
        >>> value_class = "org.apache.hadoop.io.Text"

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "old_hadoop_file")
        ...
        ...     # Write a temporary Hadoop file
        ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
        ...     rdd.saveAsHadoopFile(path, output_format_class, key_class, value_class)
        ...
        ...     loaded = sc.hadoopFile(path, input_format_class, key_class, value_class)
        ...     collected = sorted(loaded.collect())

        >>> collected
        [(0, \'1\\t\'), (0, \'1\\ta\'), (0, \'3\\tx\')]
        '''
    def hadoopRDD(self, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: str | None = None, valueConverter: str | None = None, conf: Dict[str, str] | None = None, batchSize: int = 0) -> RDD[Tuple[T, U]]:
        '''
        Read an \'old\' Hadoop InputFormat with arbitrary key and value class, from an arbitrary
        Hadoop configuration, which is passed in as a Python dict.
        This will be converted into a Configuration in Java.
        The mechanism is the same as for meth:`SparkContext.sequenceFile`.

        .. versionadded:: 1.1.0

        Parameters
        ----------
        inputFormatClass : str
            fully qualified classname of Hadoop InputFormat
            (e.g. "org.apache.hadoop.mapreduce.lib.input.TextInputFormat")
        keyClass : str
            fully qualified classname of key Writable class (e.g. "org.apache.hadoop.io.Text")
        valueClass : str
            fully qualified classname of value Writable class
            (e.g. "org.apache.hadoop.io.LongWritable")
        keyConverter : str, optional
            fully qualified name of a function returning key WritableConverter
        valueConverter : str, optional
            fully qualified name of a function returning value WritableConverter
        conf : dict, optional
            Hadoop configuration, passed in as a dict
        batchSize : int, optional, default 0
            The number of Python objects represented as a single
            Java object. (default 0, choose batchSize automatically)

        Returns
        -------
        :class:`RDD`
            RDD of tuples of key and corresponding value

        See Also
        --------
        :meth:`RDD.saveAsNewAPIHadoopDataset`
        :meth:`RDD.saveAsHadoopDataset`
        :meth:`SparkContext.newAPIHadoopRDD`
        :meth:`SparkContext.hadoopFile`

        Examples
        --------
        >>> import os
        >>> import tempfile

        Set the related classes

        >>> output_format_class = "org.apache.hadoop.mapred.TextOutputFormat"
        >>> input_format_class = "org.apache.hadoop.mapred.TextInputFormat"
        >>> key_class = "org.apache.hadoop.io.IntWritable"
        >>> value_class = "org.apache.hadoop.io.Text"

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "old_hadoop_file")
        ...
        ...     # Create the conf for writing
        ...     write_conf = {
        ...         "mapred.output.format.class": output_format_class,
        ...         "mapreduce.job.output.key.class": key_class,
        ...         "mapreduce.job.output.value.class": value_class,
        ...         "mapreduce.output.fileoutputformat.outputdir": path,
        ...     }
        ...
        ...     # Write a temporary Hadoop file
        ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
        ...     rdd.saveAsHadoopDataset(conf=write_conf)
        ...
        ...     # Create the conf for reading
        ...     read_conf = {"mapreduce.input.fileinputformat.inputdir": path}
        ...
        ...     loaded = sc.hadoopRDD(input_format_class, key_class, value_class, conf=read_conf)
        ...     collected = sorted(loaded.collect())

        >>> collected
        [(0, \'1\\t\'), (0, \'1\\ta\'), (0, \'3\\tx\')]
        '''
    def union(self, rdds: List[RDD[T]]) -> RDD[T]:
        '''
        Build the union of a list of RDDs.

        This supports unions() of RDDs with different serialized formats,
        although this forces them to be reserialized using the default
        serializer:

        .. versionadded:: 0.7.0

        See Also
        --------
        :meth:`RDD.union`

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     # generate a text RDD
        ...     with open(os.path.join(d, "union-text.txt"), "w") as f:
        ...         _ = f.write("Hello")
        ...     text_rdd = sc.textFile(d)
        ...
        ...     # generate another RDD
        ...     parallelized = sc.parallelize(["World!"])
        ...
        ...     unioned = sorted(sc.union([text_rdd, parallelized]).collect())

        >>> unioned
        [\'Hello\', \'World!\']
        '''
    def broadcast(self, value: T) -> Broadcast[T]:
        """
        Broadcast a read-only variable to the cluster, returning a :class:`Broadcast`
        object for reading it in distributed functions. The variable will
        be sent to each cluster only once.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        value : T
            value to broadcast to the Spark nodes

        Returns
        -------
        :class:`Broadcast`
            :class:`Broadcast` object, a read-only variable cached on each machine

        Examples
        --------
        >>> mapping = {1: 10001, 2: 10002}
        >>> bc = sc.broadcast(mapping)

        >>> rdd = sc.range(5)
        >>> rdd2 = rdd.map(lambda i: bc.value[i] if i in bc.value else -1)
        >>> rdd2.collect()
        [-1, 10001, 10002, -1, -1]

        >>> bc.destroy()
        """
    def accumulator(self, value: T, accum_param: AccumulatorParam[T] | None = None) -> Accumulator[T]:
        """
        Create an :class:`Accumulator` with the given initial value, using a given
        :class:`AccumulatorParam` helper object to define how to add values of the
        data type if provided. Default AccumulatorParams are used for integers
        and floating-point numbers if you do not provide one. For other types,
        a custom AccumulatorParam can be used.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        value : T
            initialized value
        accum_param : :class:`pyspark.AccumulatorParam`, optional
            helper object to define how to add values

        Returns
        -------
        :class:`Accumulator`
            `Accumulator` object, a shared variable that can be accumulated

        Examples
        --------
        >>> acc = sc.accumulator(9)
        >>> acc.value
        9
        >>> acc += 1
        >>> acc.value
        10

        Accumulator object can be accumulated in RDD operations:

        >>> rdd = sc.range(5)
        >>> def f(x):
        ...     global acc
        ...     acc += 1
        >>> rdd.foreach(f)
        >>> acc.value
        15
        """
    def addFile(self, path: str, recursive: bool = False) -> None:
        '''
        Add a file to be downloaded with this Spark job on every node.
        The `path` passed can be either a local file, a file in HDFS
        (or other Hadoop-supported filesystems), or an HTTP, HTTPS or
        FTP URI.

        To access the file in Spark jobs, use :meth:`SparkFiles.get` with the
        filename to find its download location.

        A directory can be given if the recursive option is set to True.
        Currently directories are only supported for Hadoop-supported filesystems.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        path : str
            can be either a local file, a file in HDFS (or other Hadoop-supported
            filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs,
            use :meth:`SparkFiles.get` to find its download location.
        recursive : bool, default False
            whether to recursively add files in the input directory

        See Also
        --------
        :meth:`SparkContext.listFiles`
        :meth:`SparkContext.addPyFile`
        :meth:`SparkFiles.get`

        Notes
        -----
        A path can be added only once. Subsequent additions of the same path are ignored.

        Examples
        --------
        >>> import os
        >>> import tempfile
        >>> from pyspark import SparkFiles

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path1 = os.path.join(d, "test1.txt")
        ...     with open(path1, "w") as f:
        ...         _ = f.write("100")
        ...
        ...     path2 = os.path.join(d, "test2.txt")
        ...     with open(path2, "w") as f:
        ...         _ = f.write("200")
        ...
        ...     sc.addFile(path1)
        ...     file_list1 = sorted(sc.listFiles)
        ...
        ...     sc.addFile(path2)
        ...     file_list2 = sorted(sc.listFiles)
        ...
        ...     # add path2 twice, this addition will be ignored
        ...     sc.addFile(path2)
        ...     file_list3 = sorted(sc.listFiles)
        ...
        ...     def func(iterator):
        ...         with open(SparkFiles.get("test1.txt")) as f:
        ...             mul = int(f.readline())
        ...             return [x * mul for x in iterator]
        ...
        ...     collected = sc.parallelize([1, 2, 3, 4]).mapPartitions(func).collect()

        >>> file_list1
        [\'file:/.../test1.txt\']
        >>> file_list2
        [\'file:/.../test1.txt\', \'file:/.../test2.txt\']
        >>> file_list3
        [\'file:/.../test1.txt\', \'file:/.../test2.txt\']
        >>> collected
        [100, 200, 300, 400]
        '''
    @property
    def listFiles(self) -> List[str]:
        """Returns a list of file paths that are added to resources.

        .. versionadded:: 3.4.0

        See Also
        --------
        :meth:`SparkContext.addFile`
        """
    def addPyFile(self, path: str) -> None:
        """
        Add a .py or .zip dependency for all tasks to be executed on this
        SparkContext in the future.  The `path` passed can be either a local
        file, a file in HDFS (or other Hadoop-supported filesystems), or an
        HTTP, HTTPS or FTP URI.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        path : str
            can be either a .py file or .zip dependency.

        See Also
        --------
        :meth:`SparkContext.addFile`

        Notes
        -----
        A path can be added only once. Subsequent additions of the same path are ignored.
        """
    def addArchive(self, path: str) -> None:
        '''
        Add an archive to be downloaded with this Spark job on every node.
        The `path` passed can be either a local file, a file in HDFS
        (or other Hadoop-supported filesystems), or an HTTP, HTTPS or
        FTP URI.

        To access the file in Spark jobs, use :meth:`SparkFiles.get` with the
        filename to find its download/unpacked location. The given path should
        be one of .zip, .tar, .tar.gz, .tgz and .jar.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        path : str
            can be either a local file, a file in HDFS (or other Hadoop-supported
            filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs,
            use :meth:`SparkFiles.get` to find its download location.

        See Also
        --------
        :meth:`SparkContext.listArchives`
        :meth:`SparkFiles.get`

        Notes
        -----
        A path can be added only once. Subsequent additions of the same path are ignored.
        This API is experimental.

        Examples
        --------
        Creates a zipped file that contains a text file written \'100\'.

        >>> import os
        >>> import tempfile
        >>> import zipfile
        >>> from pyspark import SparkFiles

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "test.txt")
        ...     with open(path, "w") as f:
        ...         _ = f.write("100")
        ...
        ...     zip_path1 = os.path.join(d, "test1.zip")
        ...     with zipfile.ZipFile(zip_path1, "w", zipfile.ZIP_DEFLATED) as z:
        ...         z.write(path, os.path.basename(path))
        ...
        ...     zip_path2 = os.path.join(d, "test2.zip")
        ...     with zipfile.ZipFile(zip_path2, "w", zipfile.ZIP_DEFLATED) as z:
        ...         z.write(path, os.path.basename(path))
        ...
        ...     sc.addArchive(zip_path1)
        ...     arch_list1 = sorted(sc.listArchives)
        ...
        ...     sc.addArchive(zip_path2)
        ...     arch_list2 = sorted(sc.listArchives)
        ...
        ...     # add zip_path2 twice, this addition will be ignored
        ...     sc.addArchive(zip_path2)
        ...     arch_list3 = sorted(sc.listArchives)
        ...
        ...     def func(iterator):
        ...         with open("%s/test.txt" % SparkFiles.get("test1.zip")) as f:
        ...             mul = int(f.readline())
        ...             return [x * mul for x in iterator]
        ...
        ...     collected = sc.parallelize([1, 2, 3, 4]).mapPartitions(func).collect()

        >>> arch_list1
        [\'file:/.../test1.zip\']
        >>> arch_list2
        [\'file:/.../test1.zip\', \'file:/.../test2.zip\']
        >>> arch_list3
        [\'file:/.../test1.zip\', \'file:/.../test2.zip\']
        >>> collected
        [100, 200, 300, 400]
        '''
    @property
    def listArchives(self) -> List[str]:
        """Returns a list of archive paths that are added to resources.

        .. versionadded:: 3.4.0

        See Also
        --------
        :meth:`SparkContext.addArchive`
        """
    def setCheckpointDir(self, dirName: str) -> None:
        """
        Set the directory under which RDDs are going to be checkpointed. The
        directory must be an HDFS path if running on a cluster.

        .. versionadded:: 0.7.0

        Parameters
        ----------
        dirName : str
            path to the directory where checkpoint files will be stored
            (must be HDFS path if running in cluster)

        See Also
        --------
        :meth:`SparkContext.getCheckpointDir`
        :meth:`RDD.checkpoint`
        :meth:`RDD.getCheckpointFile`
        """
    def getCheckpointDir(self) -> str | None:
        """
        Return the directory where RDDs are checkpointed. Returns None if no
        checkpoint directory has been set.

        .. versionadded:: 3.1.0

        See Also
        --------
        :meth:`SparkContext.setCheckpointDir`
        :meth:`RDD.checkpoint`
        :meth:`RDD.getCheckpointFile`
        """
    def setJobGroup(self, groupId: str, description: str, interruptOnCancel: bool = False) -> None:
        '''
        Assigns a group ID to all the jobs started by this thread until the group ID is set to a
        different value or cleared.

        Often, a unit of execution in an application consists of multiple Spark actions or jobs.
        Application programmers can use this method to group all those jobs together and give a
        group description. Once set, the Spark web UI will associate such jobs with this group.

        The application can use :meth:`SparkContext.cancelJobGroup` to cancel all
        running jobs in this group.

        .. versionadded:: 1.0.0

        Parameters
        ----------
        groupId : str
            The group ID to assign.
        description : str
            The description to set for the job group.
        interruptOnCancel : bool, optional, default False
            whether to interrupt jobs on job cancellation.

        Notes
        -----
        If interruptOnCancel is set to true for the job group, then job cancellation will result
        in Thread.interrupt() being called on the job\'s executor threads. This is useful to help
        ensure that the tasks are actually stopped in a timely manner, but is off by default due
        to HDFS-1208, where HDFS may respond to Thread.interrupt() by marking nodes as dead.

        If you run jobs in parallel, use :class:`pyspark.InheritableThread` for thread
        local inheritance.

        See Also
        --------
        :meth:`SparkContext.cancelJobGroup`

        Examples
        --------
        >>> import threading
        >>> from time import sleep
        >>> from pyspark import InheritableThread
        >>> result = "Not Set"
        >>> lock = threading.Lock()
        >>> def map_func(x):
        ...     sleep(100)
        ...     raise RuntimeError("Task should have been cancelled")
        >>> def start_job(x):
        ...     global result
        ...     try:
        ...         sc.setJobGroup("job_to_cancel", "some description")
        ...         result = sc.parallelize(range(x)).map(map_func).collect()
        ...     except Exception as e:
        ...         result = "Cancelled"
        ...     lock.release()
        >>> def stop_job():
        ...     sleep(5)
        ...     sc.cancelJobGroup("job_to_cancel")
        >>> suppress = lock.acquire()
        >>> suppress = InheritableThread(target=start_job, args=(10,)).start()
        >>> suppress = InheritableThread(target=stop_job).start()
        >>> suppress = lock.acquire()
        >>> print(result)
        Cancelled
        '''
    def setLocalProperty(self, key: str, value: str) -> None:
        """
        Set a local property that affects jobs submitted from this thread, such as the
        Spark fair scheduler pool.

        .. versionadded:: 1.0.0

        Parameters
        ----------
        key : str
            The key of the local property to set.
        value : str
            The value of the local property to set.

        See Also
        --------
        :meth:`SparkContext.getLocalProperty`

        Notes
        -----
        If you run jobs in parallel, use :class:`pyspark.InheritableThread` for thread
        local inheritance.
        """
    def getLocalProperty(self, key: str) -> str | None:
        """
        Get a local property set in this thread, or null if it is missing. See
        :meth:`setLocalProperty`.

        .. versionadded:: 1.0.0

        See Also
        --------
        :meth:`SparkContext.setLocalProperty`
        """
    def setJobDescription(self, value: str) -> None:
        """
        Set a human readable description of the current job.

        .. versionadded:: 2.3.0

        Parameters
        ----------
        value : str
            The job description to set.

        Notes
        -----
        If you run jobs in parallel, use :class:`pyspark.InheritableThread` for thread
        local inheritance.
        """
    def sparkUser(self) -> str:
        """
        Get SPARK_USER for user who is running SparkContext.

        .. versionadded:: 1.0.0
        """
    def cancelJobGroup(self, groupId: str) -> None:
        """
        Cancel active jobs for the specified group. See :meth:`SparkContext.setJobGroup`.
        for more information.

        .. versionadded:: 1.1.0

        Parameters
        ----------
        groupId : str
            The group ID to cancel the job.

        See Also
        --------
        :meth:`SparkContext.setJobGroup`
        :meth:`SparkContext.cancelJobGroup`
        """
    def cancelAllJobs(self) -> None:
        """
        Cancel all jobs that have been scheduled or are running.

        .. versionadded:: 1.1.0

        See Also
        --------
        :meth:`SparkContext.cancelJobGroup`
        :meth:`SparkContext.runJob`
        """
    def statusTracker(self) -> StatusTracker:
        """
        Return :class:`StatusTracker` object

        .. versionadded:: 1.4.0
        """
    def runJob(self, rdd: RDD[T], partitionFunc: Callable[[Iterable[T]], Iterable[U]], partitions: Sequence[int] | None = None, allowLocal: bool = False) -> List[U]:
        """
        Executes the given partitionFunc on the specified set of partitions,
        returning the result as an array of elements.

        If 'partitions' is not specified, this will run over all partitions.

        .. versionadded:: 1.1.0

        Parameters
        ----------
        rdd : :class:`RDD`
            target RDD to run tasks on
        partitionFunc : function
            a function to run on each partition of the RDD
        partitions : list, optional
            set of partitions to run on; some jobs may not want to compute on all
            partitions of the target RDD, e.g. for operations like `first`
        allowLocal : bool, default False
            this parameter takes no effect

        Returns
        -------
        list
            results of specified partitions

        See Also
        --------
        :meth:`SparkContext.cancelAllJobs`

        Examples
        --------
        >>> myRDD = sc.parallelize(range(6), 3)
        >>> sc.runJob(myRDD, lambda part: [x * x for x in part])
        [0, 1, 4, 9, 16, 25]

        >>> myRDD = sc.parallelize(range(6), 3)
        >>> sc.runJob(myRDD, lambda part: [x * x for x in part], [0, 2], True)
        [0, 1, 16, 25]
        """
    def show_profiles(self) -> None:
        """Print the profile stats to stdout

        .. versionadded:: 1.2.0

        See Also
        --------
        :meth:`SparkContext.dump_profiles`
        """
    def dump_profiles(self, path: str) -> None:
        """Dump the profile stats into directory `path`

        .. versionadded:: 1.2.0

        See Also
        --------
        :meth:`SparkContext.show_profiles`
        """
    def getConf(self) -> SparkConf:
        """Return a copy of this SparkContext's configuration :class:`SparkConf`.

        .. versionadded:: 2.1.0
        """
    @property
    def resources(self) -> Dict[str, ResourceInformation]:
        """
        Return the resource information of this :class:`SparkContext`.
        A resource could be a GPU, FPGA, etc.

        .. versionadded:: 3.0.0
        """
