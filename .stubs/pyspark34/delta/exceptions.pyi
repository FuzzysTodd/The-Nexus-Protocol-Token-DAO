from py4j.java_gateway import JVMView as JVMView, JavaObject as JavaObject, is_instance_of as is_instance_of
from pyspark.errors.exceptions.captured import CapturedException
from pyspark.sql.utils import AnalysisException as AnalysisException, IllegalArgumentException as IllegalArgumentException, ParseException as ParseException

class DeltaConcurrentModificationException(CapturedException):
    """
    The basic class for all Delta commit conflict exceptions.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
class ConcurrentWriteException(CapturedException):
    """
    Thrown when a concurrent transaction has written data after the current transaction read the
    table.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
class MetadataChangedException(CapturedException):
    """
    Thrown when the metadata of the Delta table has changed between the time of read
    and the time of commit.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
class ProtocolChangedException(CapturedException):
    """
    Thrown when the protocol version has changed between the time of read
    and the time of commit.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
class ConcurrentAppendException(CapturedException):
    """
    Thrown when files are added that would have been read by the current transaction.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
class ConcurrentDeleteReadException(CapturedException):
    """
    Thrown when the current transaction reads data that was deleted by a concurrent transaction.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
class ConcurrentDeleteDeleteException(CapturedException):
    """
    Thrown when the current transaction deletes data that was deleted by a concurrent transaction.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
class ConcurrentTransactionException(CapturedException):
    """
    Thrown when concurrent transaction both attempt to update the same idempotent transaction.

    .. versionadded:: 1.0

    .. note:: Evolving
    """
