from _typeshed import Incomplete
from pyspark import RDD as RDD, SparkContext as SparkContext

class TransformFunction:
    """
    This class wraps a function RDD[X] -> RDD[Y] that was passed to
    DStream.transform(), allowing it to be called from Java via Py4J's
    callback server.

    Java calls this function with a sequence of JavaRDDs and this function
    returns a single JavaRDD pointer back to Java.
    """
    ctx: Incomplete
    func: Incomplete
    deserializers: Incomplete
    rdd_wrap_func: Incomplete
    failure: Incomplete
    def __init__(self, ctx, func, *deserializers) -> None: ...
    def rdd_wrapper(self, func): ...
    def call(self, milliseconds, jrdds): ...
    def getLastFailure(self): ...
    class Java:
        implements: Incomplete

class TransformFunctionSerializer:
    """
    This class implements a serializer for PythonTransformFunction Java
    objects.

    This is necessary because the Java PythonTransformFunction objects are
    actually Py4J references to Python objects and thus are not directly
    serializable. When Java needs to serialize a PythonTransformFunction,
    it uses this class to invoke Python, which returns the serialized function
    as a byte array.
    """
    ctx: Incomplete
    serializer: Incomplete
    gateway: Incomplete
    failure: Incomplete
    def __init__(self, ctx, serializer, gateway: Incomplete | None = None) -> None: ...
    def dumps(self, id): ...
    def loads(self, data): ...
    def getLastFailure(self): ...
    class Java:
        implements: Incomplete

def rddToFileName(prefix, suffix, timestamp):
    '''
    Return string prefix-time(.suffix)

    Examples
    --------
    >>> rddToFileName("spark", None, 12345678910)
    \'spark-12345678910\'
    >>> rddToFileName("spark", "tmp", 12345678910)
    \'spark-12345678910.tmp\'
    '''
