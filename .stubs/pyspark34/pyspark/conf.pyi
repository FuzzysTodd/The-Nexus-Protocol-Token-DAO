from py4j.java_gateway import JVMView, JavaObject
from typing import List, Tuple, overload

__all__ = ['SparkConf']

class SparkConf:
    '''
    Configuration for a Spark application. Used to set various Spark
    parameters as key-value pairs.

    Most of the time, you would create a SparkConf object with
    ``SparkConf()``, which will load values from `spark.*` Java system
    properties as well. In this case, any parameters you set directly on
    the :class:`SparkConf` object take priority over system properties.

    For unit tests, you can also call ``SparkConf(false)`` to skip
    loading external settings and get the same configuration no matter
    what the system properties are.

    All setter methods in this class support chaining. For example,
    you can write ``conf.setMaster("local").setAppName("My app")``.

    Parameters
    ----------
    loadDefaults : bool
        whether to load values from Java system properties (True by default)
    _jvm : class:`py4j.java_gateway.JVMView`
        internal parameter used to pass a handle to the
        Java VM; does not need to be set by users
    _jconf : class:`py4j.java_gateway.JavaObject`
        Optionally pass in an existing SparkConf handle
        to use its parameters

    Notes
    -----
    Once a SparkConf object is passed to Spark, it is cloned
    and can no longer be modified by the user.

    Examples
    --------
    >>> from pyspark.conf import SparkConf
    >>> from pyspark.context import SparkContext
    >>> conf = SparkConf()
    >>> conf.setMaster("local").setAppName("My app")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.master")
    \'local\'
    >>> conf.get("spark.app.name")
    \'My app\'
    >>> sc = SparkContext(conf=conf)
    >>> sc.master
    \'local\'
    >>> sc.appName
    \'My app\'
    >>> sc.sparkHome is None
    True

    >>> conf = SparkConf(loadDefaults=False)
    >>> conf.setSparkHome("/path")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.home")
    \'/path\'
    >>> conf.setExecutorEnv("VAR1", "value1")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.setExecutorEnv(pairs = [("VAR3", "value3"), ("VAR4", "value4")])
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.executorEnv.VAR1")
    \'value1\'
    >>> print(conf.toDebugString())
    spark.executorEnv.VAR1=value1
    spark.executorEnv.VAR3=value3
    spark.executorEnv.VAR4=value4
    spark.home=/path
    >>> for p in sorted(conf.getAll(), key=lambda p: p[0]):
    ...     print(p)
    (\'spark.executorEnv.VAR1\', \'value1\')
    (\'spark.executorEnv.VAR3\', \'value3\')
    (\'spark.executorEnv.VAR4\', \'value4\')
    (\'spark.home\', \'/path\')
    >>> conf._jconf.setExecutorEnv("VAR5", "value5")
    JavaObject id...
    >>> print(conf.toDebugString())
    spark.executorEnv.VAR1=value1
    spark.executorEnv.VAR3=value3
    spark.executorEnv.VAR4=value4
    spark.executorEnv.VAR5=value5
    spark.home=/path
    '''
    def __init__(self, loadDefaults: bool = True, _jvm: JVMView | None = None, _jconf: JavaObject | None = None) -> None:
        """
        Create a new Spark configuration.
        """
    def set(self, key: str, value: str) -> SparkConf:
        """Set a configuration property."""
    def setIfMissing(self, key: str, value: str) -> SparkConf:
        """Set a configuration property, if not already set."""
    def setMaster(self, value: str) -> SparkConf:
        """Set master URL to connect to."""
    def setAppName(self, value: str) -> SparkConf:
        """Set application name."""
    def setSparkHome(self, value: str) -> SparkConf:
        """Set path where Spark is installed on worker nodes."""
    @overload
    def setExecutorEnv(self, key: str, value: str) -> SparkConf: ...
    @overload
    def setExecutorEnv(self, *, pairs: List[Tuple[str, str]]) -> SparkConf: ...
    def setAll(self, pairs: List[Tuple[str, str]]) -> SparkConf:
        """
        Set multiple parameters, passed as a list of key-value pairs.

        Parameters
        ----------
        pairs : iterable of tuples
            list of key-value pairs to set
        """
    @overload
    def get(self, key: str) -> str | None: ...
    @overload
    def get(self, key: str, defaultValue: None) -> str | None: ...
    @overload
    def get(self, key: str, defaultValue: str) -> str: ...
    def getAll(self) -> List[Tuple[str, str]]:
        """Get all values as a list of key-value pairs."""
    def contains(self, key: str) -> bool:
        """Does this configuration contain a given key?"""
    def toDebugString(self) -> str:
        """
        Returns a printable version of the configuration, as a list of
        key=value pairs, one per line.
        """
