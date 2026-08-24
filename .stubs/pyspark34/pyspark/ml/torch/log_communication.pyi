import socketserver
from _typeshed import Incomplete
from pyspark.context import SparkContext as SparkContext

def get_driver_host(sc: SparkContext) -> str | None: ...

class WriteLogToStdout(socketserver.StreamRequestHandler):
    def handle(self) -> None: ...

class LogStreamingServer:
    server: Incomplete
    serve_thread: Incomplete
    port: Incomplete
    def __init__(self) -> None: ...
    def start(self, spark_host_address: str = '') -> None: ...
    def shutdown(self) -> None: ...

class LogStreamingClientBase:
    def send(self, message: str) -> None: ...
    def close(self) -> None: ...

class LogStreamingClient(LogStreamingClientBase):
    """
    A client that streams log messages to :class:`LogStreamingServer`.
    In case of failures, the client will skip messages instead of raising an error.
    """
    address: Incomplete
    port: Incomplete
    timeout: Incomplete
    sock: Incomplete
    failed: bool
    def __init__(self, address: str, port: int, timeout: int = 10) -> None:
        """
        Creates a connection to the logging server and authenticates.This client is best effort,
        if authentication or sending a message  fails, the client will be marked as not alive and
        stop trying to send message.

        :param address: Address where the service is running.
        :param port: Port where the service is listening for new connections.
        """
    def send(self, message: str) -> None:
        """
        Sends a message.
        """
    def close(self) -> None:
        """
        Closes the connection.
        """
