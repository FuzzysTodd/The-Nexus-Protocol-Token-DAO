from _typeshed import Incomplete
from py4j.java_gateway import CallbackServer as CallbackServer, CallbackServerParameters as CallbackServerParameters, DEFAULT_ACCEPT_TIMEOUT_PLACEHOLDER as DEFAULT_ACCEPT_TIMEOUT_PLACEHOLDER, DEFAULT_ADDRESS as DEFAULT_ADDRESS, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_PYTHON_PROXY_PORT as DEFAULT_PYTHON_PROXY_PORT, GatewayClient as GatewayClient, GatewayConnectionGuard as GatewayConnectionGuard, GatewayParameters as GatewayParameters, JavaGateway as JavaGateway, do_client_auth as do_client_auth, quiet_close as quiet_close, quiet_shutdown as quiet_shutdown, server_connection_stopped as server_connection_stopped, set_linger as set_linger
from py4j.protocol import Py4JAuthenticationError as Py4JAuthenticationError, Py4JError as Py4JError, Py4JNetworkError as Py4JNetworkError, get_command_part as get_command_part, get_return_value as get_return_value, smart_decode as smart_decode
from threading import Thread

logger: Incomplete
SHUTDOWN_FINALIZER_WORKER: str
DEFAULT_WORKER_SLEEP_TIME: int

class FinalizerWorker(Thread):
    deque: Incomplete
    def __init__(self, deque) -> None: ...
    def run(self) -> None: ...

class JavaParameters(GatewayParameters):
    """Wrapper class that contains all parameters that can be passed to
    configure a `ClientServer`.`
    """
    auto_gc: Incomplete
    daemonize_memory_management: Incomplete
    def __init__(self, address=..., port=..., auto_field: bool = False, auto_close: bool = True, auto_convert: bool = False, eager_load: bool = False, ssl_context: Incomplete | None = None, enable_memory_management: bool = True, auto_gc: bool = False, read_timeout: Incomplete | None = None, daemonize_memory_management: bool = True, auth_token: Incomplete | None = None) -> None:
        '''

        :param address: the address to which the client will request a
            connection. If you\'re assing a `SSLContext` with
            `check_hostname=True` then this address must match
            (one of) the hostname(s) in the certificate the gateway
            server presents.

        :param port: the port to which the client will request a connection.
            Default is 25333.

        :param auto_field: if `False`, each object accessed through this
            gateway won"t try to lookup fields (they will be accessible only by
            calling get_field). If `True`, fields will be automatically looked
            up, possibly hiding methods of the same name and making method
            calls less efficient.

        :param auto_close: if `True`, the connections created by the client
            close the socket when they are garbage collected.

        :param auto_convert: if `True`, try to automatically convert Python
            objects like sequences and maps to Java Objects. Default value is
            `False` to improve performance and because it is still possible to
            explicitly perform this conversion.

        :param eager_load: if `True`, the gateway tries to connect to the JVM
            by calling System.currentTimeMillis. If the gateway cannot connect
            to the JVM, it shuts down itself and raises an exception.

        :param ssl_context: if not None, SSL connections will be made using
            this SSLContext

        :param enable_memory_management: if True, tells the Java side when a
            JavaObject (reference to an object on the Java side) is garbage
            collected on the Python side.

        :param auto_gc: if True, call gc.collect() before sending a command to
            the Java side. This should prevent the gc from running between
            sending the command and waiting for an anwser. False by default
            because this case is extremely unlikely. Legacy option no longer
            used.

        :param read_timeout: if > 0, sets a timeout in seconds after
            which the socket stops waiting for a response from the Java side.

        :param daemonize_memory_management: if True, the worker Thread making
            the garbage collection requests will be daemonized. This means that
            the Python side might not send all garbage collection requests if
            it exits. If False, memory management will block the Python program
            exit until all requests are sent.

        :param auth_token: if provided, an authentication that token clients
            must provide to the server when connecting.
        '''

class PythonParameters(CallbackServerParameters):
    """Wrapper class that contains all parameters that can be passed to
    configure a `ClientServer`
    """
    auto_gc: Incomplete
    def __init__(self, address=..., port=..., daemonize: bool = False, daemonize_connections: bool = False, eager_load: bool = True, ssl_context: Incomplete | None = None, auto_gc: bool = False, accept_timeout=..., read_timeout: Incomplete | None = None, propagate_java_exceptions: bool = False, auth_token: Incomplete | None = None) -> None:
        """
        :param address: the address to which the client will request a
            connection

        :param port: the port to which the client will request a connection.
            Default is 25334.

        :param daemonize: If `True`, will set the daemon property of the server
            thread to True. The callback server will exit automatically if all
            the other threads exit.

        :param daemonize_connections: If `True`, callback server connections
            are executed in daemonized threads and will not block the exit of a
            program if non daemonized threads are finished.

        :param eager_load: If `True`, the callback server is automatically
            started when the JavaGateway is created.

        :param ssl_context: if not None, the SSLContext's certificate will be
            presented to callback connections.

        :param auto_gc: if True, call gc.collect() before returning a response
            to the Java side. This should prevent the gc from running between
            sending the response and waiting for a new command. False by
            default because this case is extremely unlikely but could break
            communication. Legacy option no longer used.

        :param accept_timeout: if > 0, sets a timeout in seconds after which
            the callbackserver stops waiting for a connection, sees if the
            callback server should shut down, and if not, wait again for a
            connection. The default is 5 seconds: this roughly means that
            if can take up to 5 seconds to shut down the callback server.

        :param read_timeout: if > 0, sets a timeout in seconds after
            which the socket stops waiting for a call or command from the
            Java side.

        :param propagate_java_exceptions: if `True`, any `Py4JJavaError` raised
            by a Python callback will cause the nested `java_exception` to be
            thrown on the Java side. If `False`, the `Py4JJavaError` will
            manifest as a `Py4JException` on the Java side, just as with any
            other kind of Python exception. Setting this option is useful if
            you need to implement a Java interface where the user of the
            interface has special handling for specific Java exception types.

        :param auth_token: if provided, an authentication token that clients
            must provide to the server when connecting.
        """

class JavaClient(GatewayClient):
    """Responsible for managing requests from Python to Java.

    This implementation is thread-safe because it always use only one
    ClientServerConnection per thread.
    """
    java_parameters: Incomplete
    python_parameters: Incomplete
    thread_connection: Incomplete
    finalizer_deque: Incomplete
    def __init__(self, java_parameters, python_parameters, gateway_property: Incomplete | None = None, finalizer_deque: Incomplete | None = None) -> None:
        """
        :param java_parameters: collection of parameters and flags used to
            configure the JavaGateway (Java client)

        :param python_parameters: collection of parameters and flags used to
            configure the CallbackServer (Python server)

        :param gateway_property: used to keep gateway preferences without a
            cycle with the JavaGateway

        :param finalizer_deque: deque used to manage garbage collection
            requests.
        """
    def garbage_collect_object(self, target_id, enqueue: bool = True) -> None:
        """Tells the Java side that there is no longer a reference to this
        JavaObject on the Python side. If enqueue is True, sends the request
        to the FinalizerWorker deque. Otherwise, sends the request to the Java
        side.
        """
    def set_thread_connection(self, connection) -> None:
        """Associates a ClientServerConnection with the current thread.

        :param connection: The ClientServerConnection to associate with the
            current thread.
        """
    def shutdown_gateway(self) -> None: ...
    def get_thread_connection(self):
        """Returns the ClientServerConnection associated with this thread. Can
        be None.
        """

class ThreadLocalConnectionFinalizer:
    """Cleans :class:`ClientServerConnection` held by a thread local by
    closing it properly and removing it from the :class:`JavaClient`
    deque. Right before the Python thread is terminated, this
    instance will be garbage-collected, which triggers a call
    to __del__  that contains the cleanup logic.
    """
    connection: Incomplete
    deque: Incomplete
    def __init__(self, connection, dequeue) -> None: ...
    def __del__(self) -> None:
        """Removes the connection associated with the current thread
        from the deque.

        Expected to be called when the thread that started the
        connection is garbage-collected.
        """

class ClientServerConnectionGuard(GatewayConnectionGuard):
    """Connection guard that does nothing on exit because there is no need to
    close or give back a connection.
    """
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class PythonServer(CallbackServer):
    """Responsible for managing requests from Java to Python.
    """
    java_parameters: Incomplete
    python_parameters: Incomplete
    gateway_property: Incomplete
    def __init__(self, java_client, java_parameters, python_parameters, gateway_property) -> None:
        """
        :param java_client: the gateway client used to call Java objects.

        :param java_parameters: collection of parameters and flags used to
            configure the JavaGateway (Java client)

        :param python_parameters: collection of parameters and flags used to
            configure the CallbackServer (Python server)

        :param gateway_property: used to keep gateway preferences.
        """

class ClientServerConnection:
    """Default connection for a ClientServer instance
    (socket-based, one per thread) responsible for communicating
    with the Java Virtual Machine.
    """
    java_parameters: Incomplete
    python_parameters: Incomplete
    address: Incomplete
    port: Incomplete
    java_address: Incomplete
    java_port: Incomplete
    python_address: Incomplete
    python_port: Incomplete
    ssl_context: Incomplete
    socket: Incomplete
    stream: Incomplete
    gateway_property: Incomplete
    pool: Incomplete
    is_connected: bool
    java_client: Incomplete
    python_server: Incomplete
    initiated_from_client: bool
    def __init__(self, java_parameters, python_parameters, gateway_property, java_client, python_server: Incomplete | None = None) -> None:
        """
        :param java_parameters: collection of parameters and flags used to
            configure the JavaGateway (Java client)

        :param python_parameters: collection of parameters and flags used to
            configure the CallbackServer (Python server)

        :param gateway_property: used to keep gateway preferences.

        :param java_client: the gateway client used to call Java objects.

        :param python_server: the Python server used to receive commands from
            Java. Only provided if created from Python server.
        """
    def connect_to_java_server(self) -> None: ...
    def init_socket_from_python_server(self, socket, stream) -> None: ...
    def shutdown_gateway(self) -> None:
        """Sends a shutdown command to the Java side.

        This will close the ClientServer on the Java side: all active
        connections will be closed. This may be useful if the lifecycle
        of the Java program must be tied to the Python program.
        """
    def start(self) -> None: ...
    def run(self) -> None: ...
    def send_command(self, command): ...
    def close(self, reset: bool = False) -> None: ...
    def wait_for_commands(self) -> None: ...
    def __del__(self) -> None: ...

class ClientServer(JavaGateway):
    """Subclass of JavaGateway that implements a different threading model: a
    thread always use the same connection to the other side so callbacks are
    executed in the calling thread.

    For example, if Python thread 1 calls Java, and Java calls Python, the
    callback (from Java to Python) will be executed in Python thread 1.

    Note about authentication: to enable authentication
    """
    java_parameters: Incomplete
    python_parameters: Incomplete
    def __init__(self, java_parameters: Incomplete | None = None, python_parameters: Incomplete | None = None, python_server_entry_point: Incomplete | None = None) -> None:
        """
        :param java_parameters: collection of parameters and flags used to
            configure the JavaGateway (Java client)

        :param python_parameters: collection of parameters and flags used to
            configure the CallbackServer (Python server)

        :param python_server_entry_point: can be requested by the Java side if
            Java is driving the communication.
        """
