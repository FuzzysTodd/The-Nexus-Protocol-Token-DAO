from py4j.java_gateway import JavaObject as JavaObject
from pyspark import since as since
from pyspark._globals import _NoValueType

class RuntimeConfig:
    """User-facing configuration API, accessible through `SparkSession.conf`.

    Options set here are automatically propagated to the Hadoop configuration during I/O.

    .. versionchanged:: 3.4.0
        Supports Spark Connect.
    """
    def __init__(self, jconf: JavaObject) -> None:
        """Create a new RuntimeConfig that wraps the underlying JVM object."""
    def set(self, key: str, value: str | int | bool) -> None:
        """Sets the given Spark runtime configuration property.

        .. versionchanged:: 3.4.0
            Supports Spark Connect.
        """
    def get(self, key: str, default: str | None | _NoValueType = ...) -> str | None:
        """Returns the value of Spark runtime configuration property for the given key,
        assuming it is set.

        .. versionchanged:: 3.4.0
            Supports Spark Connect.
        """
    def unset(self, key: str) -> None:
        """Resets the configuration property for the given key.

        .. versionchanged:: 3.4.0
            Supports Spark Connect.
        """
    def isModifiable(self, key: str) -> bool:
        """Indicates whether the configuration property with the given key
        is modifiable in the current session.

        .. versionchanged:: 3.4.0
            Supports Spark Connect.
        """
