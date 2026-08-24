from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def recv(tensor_type, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated: bool = False, name: Incomplete | None = None):
    """Receives the named tensor from send_device on recv_device.

  Args:
    tensor_type: A `tf.DType`.
    tensor_name: A `string`. The name of the tensor to receive.
    send_device: A `string`. The name of the device sending the tensor.
    send_device_incarnation: An `int`. The current incarnation of send_device.
    recv_device: A `string`. The name of the device receiving the tensor.
    client_terminated: An optional `bool`. Defaults to `False`.
      If set to true, this indicates that the node was added
      to the graph as a result of a client-side feed or fetch of Tensor data,
      in which case the corresponding send or recv is expected to be managed
      locally by the caller.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `tensor_type`.
  """

Recv: Incomplete

def recv_eager_fallback(tensor_type, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated, name, ctx): ...
def send(tensor, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated: bool = False, name: Incomplete | None = None):
    """Sends the named tensor from send_device to recv_device.

  Args:
    tensor: A `Tensor`. The tensor to send.
    tensor_name: A `string`. The name of the tensor to send.
    send_device: A `string`. The name of the device sending the tensor.
    send_device_incarnation: An `int`. The current incarnation of send_device.
    recv_device: A `string`. The name of the device receiving the tensor.
    client_terminated: An optional `bool`. Defaults to `False`.
      If set to true, this indicates that the node was added
      to the graph as a result of a client-side feed or fetch of Tensor data,
      in which case the corresponding send or recv is expected to be managed
      locally by the caller.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

Send: Incomplete

def send_eager_fallback(tensor, tensor_name, send_device, send_device_incarnation, recv_device, client_terminated, name, ctx): ...
