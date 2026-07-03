import logging
from _typeshed import Incomplete
from py4j.compat import CompatThread as CompatThread, Queue as Queue, basestring as basestring, hasattr2 as hasattr2, range as range
from py4j.finalizer import ThreadSafeFinalizer as ThreadSafeFinalizer
from py4j.protocol import Py4JAuthenticationError as Py4JAuthenticationError, Py4JError as Py4JError, Py4JJavaError as Py4JJavaError, Py4JNetworkError as Py4JNetworkError, compute_exception_message as compute_exception_message, escape_new_line as escape_new_line, get_command_part as get_command_part, get_error_message as get_error_message, get_return_value as get_return_value, is_error as is_error, is_fatal_error as is_fatal_error, register_output_converter as register_output_converter, smart_decode as smart_decode, unescape_new_line as unescape_new_line
from py4j.signals import Signal as Signal
from py4j.version import __version__ as __version__
from threading import Thread

class NullHandler(logging.Handler):
    def emit(self, record) -> None: ...

null_handler: Incomplete
logger: Incomplete
BUFFER_SIZE: int
DEFAULT_ADDRESS: str
DEFAULT_PORT: int
DEFAULT_PYTHON_PROXY_PORT: int
DEFAULT_ACCEPT_TIMEOUT_PLACEHOLDER: str
DEFAULT_CALLBACK_SERVER_ACCEPT_TIMEOUT: int
PY4J_SKIP_COLLECTIONS: str
PY4J_TRUE: Incomplete
server_connection_stopped: Incomplete
server_connection_started: Incomplete
server_connection_error: Incomplete
server_started: Incomplete
server_stopped: Incomplete
pre_server_shutdown: Incomplete
post_server_shutdown: Incomplete

def get_create_new_process_group_kwargs():
    """Ensures that the child process is created in another process group.

    This prevents signals such as SIGINT from propagating to the JVM.
    """
def set_reuse_address(server_socket) -> None:
    """Sets reuse address option if not on windows.

    On windows, the SO_REUSEADDR option means that multiple server sockets can
    be bound to the same address (it has nothing to do with TIME_WAIT).
    """
def set_default_callback_accept_timeout(accept_timeout) -> None:
    """Sets default accept timeout of callback server.
    """
def deprecated(name, last_version, use_instead: str = '', level=..., raise_exc: bool = False) -> None: ...
def java_import(jvm_view, import_str):
    """Imports the package or class specified by `import_str` in the
    jvm view namespace.

    :param jvm_view: The jvm_view in which to import a class/package.
    :import_str: The class (e.g., java.util.List) or the package
                 (e.g., java.io.*) to import
    """
def find_jar_path():
    """Tries to find the path where the py4j jar is located.
    """
def launch_gateway(port: int = 0, jarpath: str = '', classpath: str = '', javaopts=[], die_on_exit: bool = False, redirect_stdout: Incomplete | None = None, redirect_stderr: Incomplete | None = None, daemonize_redirect: bool = True, java_path: str = 'java', create_new_process_group: bool = False, enable_auth: bool = False, cwd: Incomplete | None = None, return_proc: bool = False, use_shell: bool = False):
    '''Launch a `Gateway` in a new Java process.

    The redirect parameters accept file-like objects, Queue, or deque. When
    text lines are sent to the stdout or stderr of the child JVM, these lines
    are redirected to the file-like object (``write(line)``), the Queue
    (``put(line)``), or the deque (``appendleft(line)``).

    The text line will contain a newline character.

    Only text output is accepted on stdout and stderr. If you wish to
    communicate with the child JVM through bytes, you need to create your own
    helper function.

    :param port: the port to launch the Java Gateway on.  If no port is
        specified then an ephemeral port is used.
    :param jarpath: the path to the Py4J jar.  Only necessary if the jar
        was installed at a non-standard location or if Python is using
        a different `sys.prefix` than the one that Py4J was installed
        under.
    :param classpath: the classpath used to launch the Java Gateway.
    :param javaopts: an array of extra options to pass to Java (the classpath
        should be specified using the `classpath` parameter, not `javaopts`.)
    :param die_on_exit: if `True`, the Java gateway process will die when
        this Python process exits or is killed.
    :param redirect_stdout: where to redirect the JVM stdout. If None (default)
        stdout is redirected to os.devnull. Otherwise accepts a
        file descriptor, a queue, or a deque. Will send one line at a time
        to these objects.
    :param redirect_stderr: where to redirect the JVM stdout. If None (default)
        stderr is redirected to os.devnull. Otherwise accepts a
        file descriptor, a queue, or a deque. Will send one line at a time to
        these objects.
    :param daemonize_redirect: if True, the consumer threads will be daemonized
        and will not prevent the main Python process from exiting. This means
        the file descriptors (stderr, stdout, redirect_stderr, redirect_stdout)
        might not be properly closed. This is not usually a problem, but in
        case of errors related to file descriptors, set this flag to False.
    :param java_path: If None, Py4J will use $JAVA_HOME/bin/java if $JAVA_HOME
        is defined, otherwise it will use "java".
    :param create_new_process_group: If True, the JVM is started in a new
        process group. This ensures that signals sent to the parent Python
        process are not forwarded to the JVM. For example, sending
        Ctrl-C/SIGINT won\'t interrupt the JVM. If the python process dies, the
        Java process will stay alive, which may be a problem for some scenarios
        though.
    :param enable_auth: If True, the server will require clients to provide an
        authentication token when connecting.
    :param cwd: If not None, path that will be used as the current working
        directory of the Java process.
    :param return_proc: If True, returns the Popen object returned when the JVM
        process was created.
    :param use_shell: If True, Popen will be start the java process with
        shell=True

    :rtype: the port number of the `Gateway` server or, when auth enabled,
            a 2-tuple with the port number and the auth token.
    '''
def get_field(java_object, field_name):
    """Retrieves the field named `field_name` from the `java_object`.

    This function is useful when `auto_field=false` in a gateway or
    Java object.

    :param java_object: the instance containing the field
    :param field_name: the name of the field to retrieve
    """
def set_field(java_object, field_name, value):
    """Sets the field named `field_name` of `java_object` to `value`.

    This function is the only way to set a field because the assignment
    operator in Python cannot be overloaded.

    :param java_object: the instance containing the field
    :param field_name: the name of the field to set
    :param value: the value to assign to the field
    """
def get_method(java_object, method_name):
    """Retrieves a reference to the method of an object.

    This function is useful when `auto_field=true` and an instance field has
    the same name as a method. The full signature of the method is not
    required: it is determined when the method is called.

    :param java_object: the instance containing the method
    :param method_name: the name of the method to retrieve
    """
def is_instance_of(gateway, java_object, java_class):
    """Indicates whether a java object is an instance of the provided
    java_class.

    :param gateway: the JavaGateway instance
    :param java_object: the JavaObject instance
    :param java_class: can be a string (fully qualified name), a JavaClass
            instance, or a JavaObject instance)
    """
def get_java_class(java_class):
    """Returns the java.lang.Class of a JavaClass. This is equivalent to
    calling .class in Java.

    :param java_class: An instance of JavaClass
    :rtype: An instance of JavaObject that corresponds to a java.lang.Class
    """
def quiet_close(closable) -> None:
    """Quietly closes a closable object without throwing an exception.

    :param closable: Object with a ``close`` method.
    """
def quiet_shutdown(socket_instance) -> None:
    """Quietly shuts down a socket without throwing an exception.

    :param socket_instance: Socket with ``shutdown`` method.
    """
def set_linger(a_socket) -> None:
    """Sets SO_LINGER to true, 0 to send a RST packet. This forcibly closes the
    connection and the remote socket should fail on write and should not need
    to read to realize that the socket was closed.

    Only use on timeout and maybe shutdown because it does not terminate the
    TCP connection normally.
    """
def check_connection(a_socket, read_timeout) -> None:
    """Checks that a socket is ready to receive by reading from it.

    If the read times out, this is a good sign. If the read returns an
    empty string, this usually means that the socket was remotely closed.

    :param a_socket: The socket to read from.
    :param read_timeout: The read_timeout to restore the socket to.
    """
def gateway_help(gateway_client, var, pattern: Incomplete | None = None, short_name: bool = True, display: bool = True):
    '''Displays a help page about a class or an object.

    :param gateway_client: The gatway client

    :param var: JavaObject, JavaClass or JavaMember for which a help page
     will be generated.

    :param pattern: Star-pattern used to filter the members. For example
     "get*Foo" may return getMyFoo, getFoo, getFooBar, but not bargetFoo.
     The pattern is matched against the entire signature. To match only
     the name of a method, use "methodName(*".

    :param short_name: If True, only the simple name of the parameter
     types and return types will be displayed. If False, the fully
     qualified name of the types will be displayed.

    :param display: If True, the help page is displayed in an interactive
     page similar to the `help` command in Python. If False, the page is
     returned as a string.
    '''
def do_client_auth(command, input_stream, sock, auth_token):
    """Receives and decodes a auth token.

    - If the token does not match, an exception is raised.
    - If the command received is not an Auth command, an exception is raised.
    - If an exception occurs, it is wrapped in a Py4JAuthenticationError.
    - Otherwise, it returns True.
    """
def is_magic_member(name):
    """Returns True if the name starts and ends with __
    """

class OutputConsumer(CompatThread):
    """Thread that consumes output
    """
    redirect: Incomplete
    stream: Incomplete
    redirect_func: Incomplete
    def __init__(self, redirect, stream, *args, **kwargs) -> None: ...
    def run(self) -> None: ...

class ProcessConsumer(CompatThread):
    """Thread that ensures process stdout and stderr are properly closed.
    """
    proc: Incomplete
    closable_list: Incomplete
    def __init__(self, proc, closable_list, *args, **kwargs) -> None: ...
    def run(self) -> None: ...

class GatewayParameters:
    """Wrapper class that contains all parameters that can be passed to
    configure a `JavaGateway`
    """
    address: Incomplete
    port: Incomplete
    auto_field: Incomplete
    auto_close: Incomplete
    auto_convert: Incomplete
    eager_load: Incomplete
    ssl_context: Incomplete
    enable_memory_management: Incomplete
    read_timeout: Incomplete
    auth_token: Incomplete
    def __init__(self, address=..., port=..., auto_field: bool = False, auto_close: bool = True, auto_convert: bool = False, eager_load: bool = False, ssl_context: Incomplete | None = None, enable_memory_management: bool = True, read_timeout: Incomplete | None = None, auth_token: Incomplete | None = None) -> None:
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

        :param read_timeout: if > 0, sets a timeout in seconds after
            which the socket stops waiting for a response from the Java side.

        :param auth_token: if provided, an authentication that token clients
            must provide to the server when connecting.
        '''

class CallbackServerParameters:
    """Wrapper class that contains all parameters that can be passed to
    configure a `CallbackServer`
    """
    address: Incomplete
    port: Incomplete
    daemonize: Incomplete
    daemonize_connections: Incomplete
    eager_load: Incomplete
    ssl_context: Incomplete
    accept_timeout: Incomplete
    read_timeout: Incomplete
    propagate_java_exceptions: Incomplete
    auth_token: Incomplete
    def __init__(self, address=..., port=..., daemonize: bool = False, daemonize_connections: bool = False, eager_load: bool = True, ssl_context: Incomplete | None = None, accept_timeout=..., read_timeout: Incomplete | None = None, propagate_java_exceptions: bool = False, auth_token: Incomplete | None = None) -> None:
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

class DummyRLock:
    def __init__(self) -> None: ...
    def acquire(self, blocking: int = 1) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...

class GatewayConnectionGuard:
    def __init__(self, client, connection) -> None: ...
    def __enter__(self): ...
    def read(self, hint: int = -1): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class GatewayClient:
    """Responsible for managing connections to the JavaGateway.

    This implementation is thread-safe and connections are created on-demand.
    This means that Py4J-Python can be accessed by multiple threads and
    messages are sent to and processed concurrently by the Java Gateway.

    When creating a custom :class:`JavaGateway`, it is recommended to pass an
    instance of :class:`GatewayClient` instead of a :class:`GatewayConnection`:
    both have the same interface, but the client supports multiple threads and
    connections, which is essential when using callbacks.  """
    gateway_parameters: Incomplete
    address: Incomplete
    port: Incomplete
    is_connected: bool
    auto_close: Incomplete
    gateway_property: Incomplete
    ssl_context: Incomplete
    deque: Incomplete
    def __init__(self, address=..., port=..., auto_close: bool = True, gateway_property: Incomplete | None = None, ssl_context: Incomplete | None = None, gateway_parameters: Incomplete | None = None) -> None:
        """
        :param gateway_parameters: the set of parameters used to configure the
            GatewayClient.

        :param gateway_property: used to keep gateway preferences without a
            cycle with the gateway
        """
    def garbage_collect_object(self, target_id) -> None:
        """Tells the Java side that there is no longer a reference to this
        JavaObject on the Python side.
        """
    def shutdown_gateway(self) -> None:
        """Sends a shutdown command to the gateway. This will close the
           gateway server: all active connections will be closed. This may
           be useful if the lifecycle of the Java program must be tied to
           the Python program.
        """
    def send_command(self, command, retry: bool = True, binary: bool = False):
        """Sends a command to the JVM. This method is not intended to be
           called directly by Py4J users. It is usually called by
           :class:`JavaMember` instances.

        :param command: the `string` command to send to the JVM. The command
         must follow the Py4J protocol.

        :param retry: if `True`, the GatewayClient tries to resend a message
         if it fails.

        :param binary: if `True`, we won't wait for a Py4J-protocol response
         from the other end; we'll just return the raw connection to the
         caller. The caller becomes the owner of the connection, and is
         responsible for closing the connection (or returning it this
         `GatewayClient` pool using `_give_back_connection`).

        :rtype: the `string` answer received from the JVM (The answer follows
         the Py4J protocol). The guarded `GatewayConnection` is also returned
         if `binary` is `True`.
        """
    def close(self) -> None:
        """Closes all currently opened connections.

        This operation is not thread safe and is only a best effort strategy
        to close active connections.

        All connections are guaranteed to be closed only if no other thread
        is accessing the client and no call is pending.
        """

class GatewayConnection:
    """Default gateway connection (socket based) responsible for communicating
       with the Java Virtual Machine."""
    gateway_parameters: Incomplete
    address: Incomplete
    port: Incomplete
    socket: Incomplete
    is_connected: bool
    auto_close: Incomplete
    gateway_property: Incomplete
    wr: Incomplete
    def __init__(self, gateway_parameters, gateway_property: Incomplete | None = None) -> None:
        """
        :param gateway_parameters: the set of parameters used to configure the
            GatewayClient.

        :param gateway_property: contains gateway preferences to avoid a cycle
         with gateway
        """
    stream: Incomplete
    def start(self) -> None:
        """Starts the connection by connecting to the `address` and the `port`
        """
    def close(self, reset: bool = False) -> None:
        """Closes the connection by closing the socket.

        If reset is True, sends a RST packet with SO_LINGER
        """
    def shutdown_gateway(self) -> None:
        """Sends a shutdown command to the gateway. This will close the gateway
           server: all active connections will be closed. This may be useful
           if the lifecycle of the Java program must be tied to the Python
           program.
        """
    def send_command(self, command):
        """Sends a command to the JVM. This method is not intended to be
           called directly by Py4J users: it is usually called by JavaMember
           instances.

        :param command: the `string` command to send to the JVM. The command
         must follow the Py4J protocol.

        :rtype: the `string` answer received from the JVM (The answer follows
         the Py4J protocol).
        """

class JavaMember:
    """Represents a member (i.e., method) of a :class:`JavaObject`. For now,
       only methods are supported. Fields are retrieved directly and are not
       contained in a JavaMember.
    """
    name: Incomplete
    container: Incomplete
    target_id: Incomplete
    gateway_client: Incomplete
    command_header: Incomplete
    pool: Incomplete
    converters: Incomplete
    def __init__(self, name, container, target_id, gateway_client) -> None: ...
    @property
    def __doc__(self): ...
    def stream(self, *args):
        """
        Call the method using the 'binary' protocol.

        :rtype: The `GatewayConnection` that the call command was sent to.
        """
    def __call__(self, *args): ...

class JavaObject:
    """Represents a Java object from which you can call methods or access
       fields."""
    def __init__(self, target_id, gateway_client) -> None:
        """
        :param target_id: the identifier of the object on the JVM side. Given
         by the JVM.

        :param gateway_client: the gateway client used to communicate with
         the JVM.
        """
    @property
    def __doc__(self): ...
    def __getattr__(self, name): ...
    def __dir__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class JavaClass:
    """A `JavaClass` represents a Java Class from which static members can be
       retrieved. `JavaClass` instances are also needed to initialize an array.

       Usually, `JavaClass` are not initialized using their constructor, but
       they are created while accessing the `jvm` property of a gateway, e.g.,
       `gateway.jvm.java.lang.String`.
    """
    def __init__(self, fqn, gateway_client) -> None: ...
    @property
    def __doc__(self): ...
    def __dir__(self): ...
    def __getattr__(self, name): ...
    def __call__(self, *args): ...

class UserHelpAutoCompletion:
    '''
    Type a package name or a class name.

    For example with a JVMView called view:
    >>> o = view.Object() # create a java.lang.Object
    >>> random = view.jvm.java.util.Random() # create a java.util.Random

    The default JVMView is in the gateway and is called:
    >>> gateway.jvm

    By default, java.lang.* is available in the view. To
    add additional Classes/Packages, do:
    >>> from py4j.java_gateway import java_import
    >>> java_import(gateway.jvm, "com.example.Class1")
    >>> instance = gateway.jvm.Class1()

    Package and class completions are only available for
    explicitly imported Java classes. For example, if you
    java_import(gateway.jvm, "com.example.Class1")
    then Class1 will appear in the completions.
    '''
    KEY: str

class JavaPackage:
    """A `JavaPackage` represents part of a Java package from which Java
       classes can be accessed.

       Usually, `JavaPackage` are not initialized using their constructor, but
       they are created while accessing the `jvm` property of a gateway, e.g.,
       `gateway.jvm.java.lang`.
    """
    def __init__(self, fqn, gateway_client, jvm_id: Incomplete | None = None) -> None: ...
    def __dir__(self): ...
    def __getattr__(self, name): ...

class JVMView:
    """A `JVMView` allows access to the Java Virtual Machine of a
       `JavaGateway`.

       This can be used to reference static members (fields and methods) and
       to call constructors.
    """
    def __init__(self, gateway_client, jvm_name, id: Incomplete | None = None, jvm_object: Incomplete | None = None) -> None: ...
    def __dir__(self): ...
    def __getattr__(self, name): ...

class GatewayProperty:
    """Object shared by callbackserver, gateway, and connections.
    """
    auto_field: Incomplete
    pool: Incomplete
    enable_memory_management: Incomplete
    def __init__(self, auto_field, pool, enable_memory_management: bool = True) -> None: ...

class JavaGateway:
    """A `JavaGateway` is the main interaction point between a Python VM and
       a JVM.

    * A `JavaGateway` instance is connected to a `Gateway` instance on the
      Java side.

    * The `entry_point` field of a `JavaGateway` instance is connected to
      the `Gateway.entryPoint` instance on the Java side.

    * The `java_gateway_server` field of a `JavaGateway` instance is connected
      to the `GatewayServer` instance on the Java side.

    * The `jvm` field of `JavaGateway` enables user to access classes, static
      members (fields and methods) and call constructors.

    * The `java_process` field of a `JavaGateway` instance is a
      subprocess.Popen object for the Java process that the `JavaGateway`
      is connected to, or None if the `JavaGateway` connected to a preexisting
      Java process (in which case we cannot directly access that process from
      Python).

    Methods that are not defined by `JavaGateway` are always redirected to
    `entry_point`. For example, ``gateway.doThat()`` is equivalent to
    ``gateway.entry_point.doThat()``. This is a trade-off between convenience
    and potential confusion.
    """
    gateway_parameters: Incomplete
    callback_server_parameters: Incomplete
    python_server_entry_point: Incomplete
    gateway_property: Incomplete
    java_process: Incomplete
    def __init__(self, gateway_client: Incomplete | None = None, auto_field: bool = False, python_proxy_port=..., start_callback_server: bool = False, auto_convert: bool = False, eager_load: bool = False, gateway_parameters: Incomplete | None = None, callback_server_parameters: Incomplete | None = None, python_server_entry_point: Incomplete | None = None, java_process: Incomplete | None = None) -> None:
        '''
        :param gateway_parameters: An instance of `GatewayParameters` used to
            configure the various options of the gateway.

        :param callback_server_parameters: An instance of
            `CallbackServerParameters` used to configure various options of the
            gateway server. Must be provided to start a gateway server.
            Otherwise, callbacks won"t be available.

        :param python_server_entry_point: can be requested by the Java side if
            Java is driving the communication.

        :param java_process: the subprocess.Popen object for the Java process
            that the `JavaGateway` shall connect to, if available.
        '''
    entry_point: Incomplete
    java_gateway_server: Incomplete
    jvm: Incomplete
    def set_gateway_client(self, gateway_client) -> None:
        """Sets the gateway client for this JavaGateway. This sets the
        appropriate gateway_property and resets the main jvm view (self.jvm).

        This is for advanced usage only. And should only be set before the
        gateway is loaded.
        """
    def __getattr__(self, name): ...
    def get_callback_server(self): ...
    def start_callback_server(self, callback_server_parameters: Incomplete | None = None):
        """Starts the callback server.

        :param callback_server_parameters: parameters to use to start the
            server. If not provided, it will use the gateway callback server
            parameters.

        :rtype: Returns True if the server was started by this call or False if
            it was already started (you cannot have more than one started
            callback server).
        """
    def new_jvm_view(self, name: str = 'custom jvm'):
        """Creates a new JVM view with its own imports. A JVM view ensures
        that the import made in one view does not conflict with the import
        of another view.

        Generally, each Python module should have its own view (to replicate
        Java behavior).

        :param name: Optional name of the jvm view. Does not need to be
            unique, i.e., two distinct views can have the same name
            (internally, they will have a distinct id).

        :rtype: A JVMView instance (same class as the gateway.jvm instance).
        """
    def new_array(self, java_class, *dimensions):
        """Creates a Java array of type `java_class` of `dimensions`

        :param java_class: The :class:`JavaClass` instance representing the
            type of the array.

        :param dimensions: A list of dimensions of the array. For example
            `[1,2]` would produce an `array[1][2]`.

        :rtype: A :class:`JavaArray <py4j.java_collections.JavaArray>`
            instance.
        """
    def shutdown(self, raise_exception: bool = False) -> None:
        """Shuts down the :class:`GatewayClient` and the
           :class:`CallbackServer <py4j.java_callback.CallbackServer>`.

        :param raise_exception: If `True`, raise an exception if an error
            occurs while shutting down (very likely with sockets).
        """
    def shutdown_callback_server(self, raise_exception: bool = False) -> None:
        """Shuts down the
           :class:`CallbackServer <py4j.java_callback.CallbackServer>`.

        :param raise_exception: If `True`, raise an exception if an error
            occurs while shutting down (very likely with sockets).
        """
    def close_callback_server(self, raise_exception: bool = False) -> None:
        """Closes the
           :class:`CallbackServer <py4j.java_callback.CallbackServer>`
           connections.

        :param raise_exception: If `True`, raise an exception if an error
            occurs while closing the callback server connections
            (very likely with sockets).
        """
    def restart_callback_server(self) -> None:
        """Shuts down the callback server (if started) and restarts a new one.
        """
    def close(self, keep_callback_server: bool = False, close_callback_server_connections: bool = False) -> None:
        """Closes all gateway connections. A connection will be reopened if
           necessary (e.g., if a :class:`JavaMethod` is called).

        :param keep_callback_server: if `True`, the callback server is not
            shut down. Mutually exclusive with
            close_callback_server_connections.
        :param close_callback_server_connections: if `True`, close all
            callback server connections.
        """
    def detach(self, java_object) -> None:
        """Makes the Java Gateway dereference this object.

        The equivalent of this method is called when a JavaObject instance
        is garbage collected on the Python side. This method, or gc.collect()
        should still be invoked when memory is limited or when too many objects
        are created on the Java side.

        :param java_object: The JavaObject instance to dereference (free) on
            the Java side.
        """
    def help(self, var, pattern: Incomplete | None = None, short_name: bool = True, display: bool = True):
        '''Displays a help page about a class or an object.

        :param var: JavaObject, JavaClass or JavaMember for which a help page
            will be generated.

        :param pattern: Star-pattern used to filter the members. For example
            "get\\*Foo" may return getMyFoo, getFoo, getFooBar, but not
            bargetFoo. The pattern is matched against the entire signature.
            To match only the name of a method, use "methodName(\\*".

        :param short_name: If True, only the simple name of the parameter
            types and return types will be displayed. If False, the fully
            qualified name of the types will be displayed.

        :param display: If True, the help page is displayed in an interactive
            page similar to the `help` command in Python. If False, the page is
            returned as a string.
        '''
    @classmethod
    def launch_gateway(cls, port: int = 0, jarpath: str = '', classpath: str = '', javaopts=[], die_on_exit: bool = False, redirect_stdout: Incomplete | None = None, redirect_stderr: Incomplete | None = None, daemonize_redirect: bool = True, java_path: str = 'java', create_new_process_group: bool = False, enable_auth: bool = False, cwd: Incomplete | None = None, use_shell: bool = False):
        '''Launch a `Gateway` in a new Java process and create a default
        :class:`JavaGateway <py4j.java_gateway.JavaGateway>` to connect to
        it.

        See :func:`launch_gateway <py4j.java_gateway.launch_gateway>` for more
        information about this function.

        :param port: the port to launch the Java Gateway on.  If no port is
            specified then an ephemeral port is used.
        :param jarpath: the path to the Py4J jar.  Only necessary if the jar
            was installed at a non-standard location or if Python is using
            a different `sys.prefix` than the one that Py4J was installed
            under.
        :param classpath: the classpath used to launch the Java Gateway.
        :param javaopts: an array of extra options to pass to Java (the
            classpath should be specified using the `classpath` parameter,
            not `javaopts`.)
        :param die_on_exit: if `True`, the Java gateway process will die when
            this Python process exits or is killed.
        :param redirect_stdout: where to redirect the JVM stdout.
            If None (default)
            stdout is redirected to os.devnull. Otherwise accepts a
            file descriptor, a queue, or a deque. Will send one line at a time
            to these objects.
        :param redirect_stderr: where to redirect the JVM stdout.
            If None (default)
            stderr is redirected to os.devnull. Otherwise accepts a
            file descriptor, a queue, or a deque. Will send one line at a time
            to these objects.
        :param daemonize_redirect: if True, the consumer threads will be
            daemonized and will not prevent the main Python process from
            exiting. This means the file descriptors (stderr, stdout,
            redirect_stderr, redirect_stdout) might not be properly closed.
            This is not usually a problem, but in case of errors related
            to file descriptors, set this flag to False.
        :param java_path: If None, Py4J will use $JAVA_HOME/bin/java if
            $JAVA_HOME is defined, otherwise it will use "java".
        :param create_new_process_group: If True, the JVM is started in a new
            process group. This ensures that signals sent to the parent Python
            process are not forwarded to the JVM. For example, sending
            Ctrl-C/SIGINT won\'t interrupt the JVM. If the python process dies,
            the Java process will stay alive, which may be a problem for some
            scenarios though.
        :param enable_auth: If True, the server will require clients to provide
            an authentication token when connecting.
        :param cwd: If not None, path that will be used as the current working
            directory of the Java process.
        :param use_shell: If True, Popen will be start the java process with
            shell=True

        :rtype: a :class:`JavaGateway <py4j.java_gateway.JavaGateway>`
            connected to the `Gateway` server.
        '''

class CallbackServer:
    """The CallbackServer is responsible for receiving call back connection
       requests from the JVM. Usually connections are reused on the Java side,
       but there is at least one connection per concurrent thread.
    """
    gateway_client: Incomplete
    callback_server_parameters: Incomplete
    port: Incomplete
    address: Incomplete
    ssl_context: Incomplete
    pool: Incomplete
    connections: Incomplete
    lock: Incomplete
    is_shutdown: bool
    is_shutting_down: bool
    def __init__(self, pool, gateway_client, port=..., address=..., callback_server_parameters: Incomplete | None = None) -> None:
        """
        :param pool: the pool responsible of tracking Python objects passed to
            the Java side.

        :param gateway_client: the gateway client used to call Java objects.

        :param callback_server_parameters: An instance of
            `CallbackServerParameters` used to configure various options of the
            callback server.

        """
    server_socket: Incomplete
    thread: Incomplete
    def start(self) -> None:
        """Starts the CallbackServer. This method should be called by the
        client instead of run()."""
    def get_listening_port(self):
        """Returns the port on which the callback server is listening to.
        Different than `port` when port is 0.
        """
    def get_listening_address(self):
        """Returns the address on which the callback server is listening to.
        May be different than `address` if `address` was an alias (e.g.,
        localhost).
        """
    def run(self) -> None:
        """Starts listening and accepting connection requests.

           This method is called when invoking `CallbackServer.start()`. A
           CallbackServer instance is created and started automatically when
           a :class:`JavaGateway <py4j.java_gateway.JavaGateway>` instance is
           created.
        """
    def close(self) -> None:
        """Closes all active callback connections
        """
    def shutdown(self) -> None:
        """Stops listening and accepting connection requests. All live
           connections are closed.

           This method can safely be called by another thread.
        """

class CallbackConnection(Thread):
    """A `CallbackConnection` receives callbacks and garbage collection
       requests from the Java side.
    """
    pool: Incomplete
    input: Incomplete
    socket: Incomplete
    gateway_client: Incomplete
    callback_server_parameters: Incomplete
    callback_server: Incomplete
    daemon: Incomplete
    def __init__(self, pool, input, socket_instance, gateway_client, callback_server_parameters, callback_server) -> None: ...
    def run(self) -> None: ...
    def close(self, reset: bool = False) -> None: ...

class PythonProxyPool:
    """A `PythonProxyPool` manages proxies that are passed to the Java side.
       A proxy is a Python class that implements a Java interface.

       A proxy has an internal class named `Java` with a member named
       `implements` which is a list of fully qualified names (string) of the
       implemented interfaces.

       The `PythonProxyPool` implements a subset of the dict interface:
       `pool[id]`, `del(pool[id])`, `pool.put(proxy)`, `pool.clear()`,
       `id in pool`, `len(pool)`.

       The `PythonProxyPool` is thread-safe.
    """
    lock: Incomplete
    dict: Incomplete
    next_id: int
    def __init__(self) -> None: ...
    def put(self, object, force_id: Incomplete | None = None):
        """Adds a proxy to the pool.

        :param object: The proxy to add to the pool.
        :rtype: A unique identifier associated with the object.
        """
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def clear(self) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __len__(self) -> int: ...
