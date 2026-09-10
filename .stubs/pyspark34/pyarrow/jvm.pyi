from _typeshed import Incomplete

class _JvmBufferNanny:
    """
    An object that keeps a org.apache.arrow.memory.ArrowBuf's underlying
    memory alive.
    """
    ref_manager: Incomplete
    def __init__(self, jvm_buf) -> None: ...
    def __del__(self) -> None: ...

def jvm_buffer(jvm_buf):
    """
    Construct an Arrow buffer from org.apache.arrow.memory.ArrowBuf

    Parameters
    ----------

    jvm_buf: org.apache.arrow.memory.ArrowBuf
        Arrow Buffer representation on the JVM.

    Returns
    -------
    pyarrow.Buffer
        Python Buffer that references the JVM memory.
    """
def field(jvm_field):
    """
    Construct a Field from a org.apache.arrow.vector.types.pojo.Field
    instance.

    Parameters
    ----------
    jvm_field: org.apache.arrow.vector.types.pojo.Field

    Returns
    -------
    pyarrow.Field
    """
def schema(jvm_schema):
    """
    Construct a Schema from a org.apache.arrow.vector.types.pojo.Schema
    instance.

    Parameters
    ----------
    jvm_schema: org.apache.arrow.vector.types.pojo.Schema

    Returns
    -------
    pyarrow.Schema
    """
def array(jvm_array):
    """
    Construct an (Python) Array from its JVM equivalent.

    Parameters
    ----------
    jvm_array : org.apache.arrow.vector.ValueVector

    Returns
    -------
    array : Array
    """
def record_batch(jvm_vector_schema_root):
    """
    Construct a (Python) RecordBatch from a JVM VectorSchemaRoot

    Parameters
    ----------
    jvm_vector_schema_root : org.apache.arrow.vector.VectorSchemaRoot

    Returns
    -------
    record_batch: pyarrow.RecordBatch
    """
