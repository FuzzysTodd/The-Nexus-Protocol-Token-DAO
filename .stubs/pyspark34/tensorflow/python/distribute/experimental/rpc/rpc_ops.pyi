from _typeshed import Incomplete
from tensorflow.python.data.util import structure as structure
from tensorflow.python.eager import context as context, def_function as def_function, function as tf_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors, type_spec as type_spec
from tensorflow.python.ops import math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.types import core as core_tf_types
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Optional, Sequence, Union

def get_output_specs_from_function(func: tf_function.ConcreteFunction): ...
def get_input_specs_from_function(func: tf_function.ConcreteFunction): ...

class Server:
    """A Server base class for accepting RPCs for registered tf.functions.

    Functions can be registered on the server and are exposed via RPCs.
  """
    @staticmethod
    def create(rpc_layer, address):
        '''Create TF RPC server at given address.

    Args:
      rpc_layer: Communication layer between client and server. Only "grpc" rpc
        layer is supported at the moment.
      address: Address where RPC server is hosted.

    Returns:
      An instance of `tf.distribute.experimental.rpc.Server` class.

    Raises:
        A ValueError if rpc_layer other than "grpc" is used. Only GRPC
        is supported at the moment.

    Example usage:

      >>> import portpicker
      >>> @tf.function(input_signature=[
      ...      tf.TensorSpec([], tf.int32),
      ...      tf.TensorSpec([], tf.int32)])
      ... def remote_fn(a, b):
      ...   return tf.add(a, b)

      >>> port = portpicker.pick_unused_port()
      >>> address = "localhost:{}".format(port)
      >>> server = tf.distribute.experimental.rpc.Server.create("grpc", address)
      >>> server.register("addition", remote_fn)
      >>> server.start()

    '''
    def register(self, method_name: str, func: Union[def_function.Function, tf_function.ConcreteFunction]):
        """Method for registering tf.function on server.

    Registered methods can be invoked remotely from clients.

    Args:
      method_name: Name of the tf.function. Clients use this method_name to make
        RPCs.
      func: A `tf.function` or ConcreteFunction to register.
    """
    def start(self) -> None:
        """Starts the RPC server on provided address.

     Server listens for new requests from client, once it is started.
    """

class Client:
    """Client class for invoking RPCs to the server."""
    @staticmethod
    def create(rpc_layer, address, name: str = '', timeout_in_ms: int = 0):
        '''Create TF RPC client to connect to the given address.

    Args:
      rpc_layer: Communication layer between client and server. Only "grpc" rpc
        layer is supported at the moment.
      address: Address of the server to connect the RPC client to.
      name: Name of the RPC Client. You can create multiple clients connecting
        to same server and distinguish them using different names.
      timeout_in_ms: The default timeout to use for outgoing RPCs from client. 0
        indicates no timeout. Exceeding timeout during RPC will raise
        DeadlineExceeded error.

    Returns:
      An instance of `tf.distribute.experimental.rpc.Client` with the following
      dynamically added methods for eagerly created clients:
        * `Registered methods` e.g. multiply(**args):
            If Client is created when executing eagerly, client will request the
            list of registered methods from server during client creation.
            The convenience methods for RPCs will be dynamically added to the
            created Client instance.

            For example, when a server has method "multiply" registered, the
            client object created in eager mode will have \'multiply\' method
            available. Users can use client.multiply(..) to make RPC, instead of
            client.call("multiply", ...)

            Both "call" and "multiply" methods are non-blocking i.e. they return
            a StatusOrResult object which should be used to wait for getting
            value or error.

            Along with the above, blocking versions of the registered
            methods are also dynamically added to client instance.
            e.g. multiply_blocking(**args). These methods block till the RPC is
            finished and return response for successful RPC. Otherwise raise
            exception.

            These methods are not available when Client is created inside a
            tf.function.

    Raises:
        A ValueError if rpc_layer other than "grpc" is used. Only GRPC
          is supported at the moment.
        A DeadlineExceeded exception in eager mode if timeout exceeds while
          creating and listing client methods.

    Example usage:
      >>> # Have server already started.
      >>> import portpicker
      >>> @tf.function(input_signature=[
      ...      tf.TensorSpec([], tf.int32),
      ...      tf.TensorSpec([], tf.int32)])
      ... def remote_fn(a, b):
      ...   return tf.add(a, b)

      >>> port = portpicker.pick_unused_port()
      >>> address = "localhost:{}".format(port)
      >>> server = tf.distribute.experimental.rpc.Server.create("grpc", address)
      >>> server.register("addition", remote_fn)
      >>> server.start()

      >>> # Start client
      >>> client = tf.distribute.experimental.rpc.Client.create("grpc",
      ...      address=address, name="test_client")

      >>> a = tf.constant(2, dtype=tf.int32)
      >>> b = tf.constant(3, dtype=tf.int32)

      >>> result = client.call(
      ...    args=[a, b],
      ...    method_name="addition",
      ...    output_specs=tf.TensorSpec((), tf.int32))

      >>> if result.is_ok():
      ...   result.get_value()

      >>> result = client.addition(a, b)

      >>> if result.is_ok():
      ...   result.get_value()

      >>> value = client.addition_blocking(a, b)
    '''
    def call(self, method_name: str, args: Optional[Sequence[core_tf_types.Tensor]] = None, output_specs: Incomplete | None = None, timeout_in_ms: int = 0):
        """Method for making RPC calls to remote server.

    This invokes RPC to the server, executing the registered method_name
    remotely.
    Args:
      method_name: Remote registered method to invoke
      args: List of arguments for the registered method.
      output_specs: Output specs for the output from method.
         For example, if tf.function is: @tf.function(input_signature=[
           tf.TensorSpec([], tf.int32), tf.TensorSpec([], tf.int32) ])
          def multiply_fn(a, b): return tf.math.multiply(a, b)
        output_spec is: tf.TensorSpec((), tf.int32)  If you have access to TF
          Function, the output specs can be generated
       from tf.function by calling: output_specs =
         tf.nest.map_structure(tf.type_spec_from_value,
         tf_function.get_concrete_function().structured_outputs  If output_specs
         are not provided, flattened list of tensors will be returned in
         response.
      timeout_in_ms: Timeout for this call. If 0, default client timeout will be
        used.

    Returns:
      An instance of `StatusOrResult` class with the following available
      methods.
        * `is_ok()`:
            Returns True of RPC was successful.
        * `get_error()`:
            Returns TF error_code and error message for the RPC.
        * `get_value()`:
            Returns the returned value from remote TF function execution
            when RPC is successful.

      Calling any of the above methods will block till RPC is completed and
      result is available.
    """

class GrpcServer(Server):
    '''GrpcServer object encapsulates a resource with GRPC server.

    Functions can be registered locally and are exposed via RPCs.
    Example:
    ```
    server = rpc_ops.GrpcServer("host:port")
    @tf.function
    def add(a, b):
      return a + b

    server.register("add", add)
    server.start()
    ```
  '''
    def __init__(self, address: str) -> None: ...
    def register(self, method_name: str, func: Union[def_function.Function, tf_function.ConcreteFunction]):
        """Method for registering functions."""
    def start(self) -> None:
        """Starts GRPC server."""

class GrpcClient(Client):
    """Client wrapper to connect to remote RPC server using GRPC.

  If Client is created with (list_registered_methods=True):
  1. Input and output specs for the methods till this point will be fetched from
  Server.
  2. convenience methods are added to invoke registered methods directly from
  client.
  For example:
    For call a server method `add`
    client.add(a, b) or client.add_async(a, b) can be used instead of
    client.call(args=[a,b], output_specs=[..])

  Prerequiste for using list_registered_methods=True:
   1. Server should be already started with the registered methods.
   2. Client must be created in Eager mode.
  """
    def __init__(self, address: str, name: str = '', list_registered_methods: bool = False, timeout_in_ms: int = 0) -> None: ...
    def call(self, method_name: str, args: Optional[Sequence[core_tf_types.Tensor]] = None, output_specs: Incomplete | None = None, timeout_in_ms: int = 0):
        """Method to invoke remote registered functions on the connected server.

    Server should be started before making an RPC Call.

    Args:
      method_name: Registered method to invoke on Server.
      args: Input arguments for the method.
      output_specs: Output specs for the output from method.
      timeout_in_ms: Timeout for this call. If 0, default client timeout will be
       used.

    Returns:
      StatusOrResult object. This function issues the RPC call to server, it
      does not block for the duration of RPC. Please call is_ok, get_error or
      get_value methods on the returned object to blocked till RPC finishes.
    """

class StatusOrResult:
    """Class representing result and status from RPC Call."""
    def __init__(self, status_or, deleter, output_specs: Incomplete | None = None) -> None: ...
    def __del__(self) -> None: ...
    def is_ok(self):
        """Returns True if RPC is successful, otherwise returns False.

    This call will block for RPC result.
    """
    def get_error(self):
        """Returns (TF Error Code, Error Message) from RPC Response.

    This call will block for RPC result.
    """
    def get_value(self):
        """Returns the returned response value from RPC Call when RPC is successful.

      The returned value is tensors in the output_specs format as returned from
      the RPC call


    This call will block for RPC result.
    """
