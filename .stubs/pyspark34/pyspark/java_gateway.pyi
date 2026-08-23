from _typeshed import Incomplete
from pyspark.serializers import UTF8Deserializer as UTF8Deserializer, read_int as read_int, write_with_length as write_with_length

def launch_gateway(conf: Incomplete | None = None, popen_kwargs: Incomplete | None = None):
    """
    launch jvm gateway

    Parameters
    ----------
    conf : :py:class:`pyspark.SparkConf`
        spark configuration passed to spark-submit
    popen_kwargs : dict
        Dictionary of kwargs to pass to Popen when spawning
        the py4j JVM. This is a developer feature intended for use in
        customizing how pyspark interacts with the py4j JVM (e.g., capturing
        stdout/stderr).

    Returns
    -------
    ClientServer or JavaGateway
    """
def local_connect_and_auth(port, auth_secret):
    """
    Connect to local host, authenticate with it, and return a (sockfile,sock) for that connection.
    Handles IPV4 & IPV6, does some error handling.

    Parameters
    ----------
    port : str or int or None
    auth_secret : str

    Returns
    -------
    tuple
        with (sockfile, sock)
    """
def ensure_callback_server_started(gw) -> None:
    """
    Start callback server if not already started. The callback server is needed if the Java
    driver process needs to callback into the Python driver process to execute Python code.
    """
