from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def delete_rpc_future_resource(handle, deleter, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    handle: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DeleteRpcFutureResource: Incomplete

def delete_rpc_future_resource_eager_fallback(handle, deleter, name, ctx): ...

class _RpcCallOutput(NamedTuple):
    future: Incomplete
    deleter: Incomplete

def rpc_call(client, method_name, args, timeout_in_ms, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    client: A `Tensor` of type `resource`.
    method_name: A `Tensor` of type `string`.
    args: A list of `Tensor` objects.
    timeout_in_ms: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (future, deleter).

    future: A `Tensor` of type `resource`.
    deleter: A `Tensor` of type `variant`.
  """

RpcCall: Incomplete

def rpc_call_eager_fallback(client, method_name, args, timeout_in_ms, name, ctx): ...

class _RpcCheckStatusOutput(NamedTuple):
    error_code: Incomplete
    error: Incomplete

def rpc_check_status(status_or, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    status_or: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (error_code, error).

    error_code: A `Tensor` of type `int64`.
    error: A `Tensor` of type `string`.
  """

RpcCheckStatus: Incomplete

def rpc_check_status_eager_fallback(status_or, name, ctx): ...

class _RpcClientOutput(NamedTuple):
    client: Incomplete
    method_specs: Incomplete

def rpc_client(server_address, timeout_in_ms, shared_name: str = '', list_registered_methods: bool = False, name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    server_address: A `Tensor` of type `string`.
    timeout_in_ms: A `Tensor` of type `int64`.
    shared_name: An optional `string`. Defaults to `""`.
    list_registered_methods: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (client, method_specs).

    client: A `Tensor` of type `resource`.
    method_specs: A `Tensor` of type `string`.
  '''

RpcClient: Incomplete

def rpc_client_eager_fallback(server_address, timeout_in_ms, shared_name, list_registered_methods, name, ctx): ...
def rpc_get_value(status_or, Tout, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    status_or: A `Tensor` of type `resource`.
    Tout: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  """

RpcGetValue: Incomplete

def rpc_get_value_eager_fallback(status_or, Tout, name, ctx): ...
def rpc_server(server_address, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    server_address: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

RpcServer: Incomplete

def rpc_server_eager_fallback(server_address, name, ctx): ...
def rpc_server_register(server, method_name, captured_inputs, f, output_specs, input_specs: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    server: A `Tensor` of type `resource`.
    method_name: A `Tensor` of type `string`.
    captured_inputs: A list of `Tensor` objects.
    f: A function decorated with @Defun.
    output_specs: A `string`.
    input_specs: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

RpcServerRegister: Incomplete

def rpc_server_register_eager_fallback(server, method_name, captured_inputs, f, output_specs, input_specs, name, ctx): ...
def rpc_server_start(server, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    server: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

RpcServerStart: Incomplete

def rpc_server_start_eager_fallback(server, name, ctx): ...
