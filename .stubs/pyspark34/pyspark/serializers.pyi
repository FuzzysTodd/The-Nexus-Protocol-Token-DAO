from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['PickleSerializer', 'CPickleSerializer', 'CloudPickleSerializer', 'MarshalSerializer', 'UTF8Deserializer']

class SpecialLengths:
    END_OF_DATA_SECTION: int
    PYTHON_EXCEPTION_THROWN: int
    TIMING_DATA: int
    END_OF_STREAM: int
    NULL: int
    START_ARROW_STREAM: int

class Serializer:
    def dump_stream(self, iterator, stream) -> None:
        """
        Serialize an iterator of objects to the output stream.
        """
    def load_stream(self, stream) -> None:
        """
        Return an iterator of deserialized objects from the input stream.
        """
    def dumps(self, obj) -> None:
        """
        Serialize an object into a byte array.
        When batching is used, this will be called with an array of objects.
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class FramedSerializer(Serializer):
    """
    Serializer that writes objects as a stream of (length, data) pairs,
    where `length` is a 32-bit integer and data is `length` bytes.
    """
    def dump_stream(self, iterator, stream) -> None: ...
    def load_stream(self, stream) -> Generator[Incomplete, None, None]: ...
    def dumps(self, obj) -> None:
        """
        Serialize an object into a byte array.
        When batching is used, this will be called with an array of objects.
        """
    def loads(self, obj) -> None:
        """
        Deserialize an object from a byte array.
        """

class BatchedSerializer(Serializer):
    """
    Serializes a stream of objects in batches by calling its wrapped
    Serializer with streams of objects.
    """
    UNLIMITED_BATCH_SIZE: int
    UNKNOWN_BATCH_SIZE: int
    serializer: Incomplete
    batchSize: Incomplete
    def __init__(self, serializer, batchSize=...) -> None: ...
    def dump_stream(self, iterator, stream) -> None: ...
    def load_stream(self, stream): ...

class FlattenedValuesSerializer(BatchedSerializer):
    """
    Serializes a stream of list of pairs, split the list of values
    which contain more than a certain number of objects to make them
    have similar sizes.
    """
    def __init__(self, serializer, batchSize: int = 10) -> None: ...
    def load_stream(self, stream): ...

class AutoBatchedSerializer(BatchedSerializer):
    """
    Choose the size of batch automatically based on the size of object
    """
    bestSize: Incomplete
    def __init__(self, serializer, bestSize=...) -> None: ...
    def dump_stream(self, iterator, stream) -> None: ...

class CartesianDeserializer(Serializer):
    """
    Deserializes the JavaRDD cartesian() of two PythonRDDs.
    Due to pyspark batching we cannot simply use the result of the Java RDD cartesian,
    we additionally need to do the cartesian within each pair of batches.
    """
    key_ser: Incomplete
    val_ser: Incomplete
    def __init__(self, key_ser, val_ser) -> None: ...
    def load_stream(self, stream): ...

class PairDeserializer(Serializer):
    """
    Deserializes the JavaRDD zip() of two PythonRDDs.
    Due to pyspark batching we cannot simply use the result of the Java RDD zip,
    we additionally need to do the zip within each pair of batches.
    """
    key_ser: Incomplete
    val_ser: Incomplete
    def __init__(self, key_ser, val_ser) -> None: ...
    def load_stream(self, stream): ...

class NoOpSerializer(FramedSerializer):
    def loads(self, obj): ...
    def dumps(self, obj): ...

class PickleSerializer(FramedSerializer):
    """
    Serializes objects using Python's pickle serializer:

        http://docs.python.org/2/library/pickle.html

    This serializer supports nearly any Python object, but may
    not be as fast as more specialized serializers.
    """
    def dumps(self, obj): ...
    def loads(self, obj, encoding: str = 'bytes'): ...

class CloudPickleSerializer(FramedSerializer):
    def dumps(self, obj): ...
    def loads(self, obj, encoding: str = 'bytes'): ...
CPickleSerializer = PickleSerializer
CPickleSerializer = CloudPickleSerializer

class MarshalSerializer(FramedSerializer):
    """
    Serializes objects using Python's Marshal serializer:

        http://docs.python.org/2/library/marshal.html

    This serializer is faster than CloudPickleSerializer but supports fewer datatypes.
    """
    def dumps(self, obj): ...
    def loads(self, obj): ...

class AutoSerializer(FramedSerializer):
    """
    Choose marshal or pickle as serialization protocol automatically
    """
    def __init__(self) -> None: ...
    def dumps(self, obj): ...
    def loads(self, obj): ...

class CompressedSerializer(FramedSerializer):
    """
    Compress the serialized data
    """
    serializer: Incomplete
    def __init__(self, serializer) -> None: ...
    def dumps(self, obj): ...
    def loads(self, obj): ...

class UTF8Deserializer(Serializer):
    """
    Deserializes streams written by String.getBytes.
    """
    use_unicode: Incomplete
    def __init__(self, use_unicode: bool = True) -> None: ...
    def loads(self, stream): ...
    def load_stream(self, stream) -> Generator[Incomplete, None, None]: ...

class ChunkedStream:
    '''
    This is a file-like object takes a stream of data, of unknown length, and breaks it into fixed
    length frames.  The intended use case is serializing large data and sending it immediately over
    a socket -- we do not want to buffer the entire data before sending it, but the receiving end
    needs to know whether or not there is more data coming.

    It works by buffering the incoming data in some fixed-size chunks.  If the buffer is full, it
    first sends the buffer size, then the data.  This repeats as long as there is more data to send.
    When this is closed, it sends the length of whatever data is in the buffer, then that data, and
    finally a "length" of -1 to indicate the stream has completed.
    '''
    buffer_size: Incomplete
    buffer: Incomplete
    current_pos: int
    wrapped: Incomplete
    def __init__(self, wrapped, buffer_size) -> None: ...
    def write(self, bytes) -> None: ...
    def close(self) -> None: ...
    @property
    def closed(self):
        """
        Return True if the `wrapped` object has been closed.
        NOTE: this property is required by pyarrow to be used as a file-like object in
        pyarrow.RecordBatchStreamWriter from ArrowStreamSerializer
        """
