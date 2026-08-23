from _typeshed import Incomplete
from tensorflow.core.framework import resource_handle_pb2 as resource_handle_pb2
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_data_flow_ops as gen_data_flow_ops
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export

def encode_resource_handle(resource_handle):
    """Encode a ResourceHandle proto as custom numpy struct type."""

class TensorHandle:
    """Represents a handle for a live tensor in a session."""
    def __init__(self, handle, dtype, session) -> None:
        '''Constructs a new tensor handle.

    A tensor handle for a persistent tensor is a python string
    that has the form of "tensor_name;unique_id;device_name".

    Args:
      handle: A tensor handle.
      dtype: The data type of the tensor represented by `handle`.
      session: The session in which the tensor is produced.
    '''
    def __del__(self) -> None: ...
    def to_numpy_array(self):
        """Convert a TensorHandle object to a feedable numpy value.

    Returns:
      A numpy array of a custom struct type that can be used as a feed value
      to run().
    """
    @property
    def handle(self):
        """The string representation of this handle."""
    def eval(self):
        """Return the value of the tensor represented by this handle."""
    def delete(self) -> None:
        """Force the deletion of this persistent tensor."""
    def get_raw_handle(self):
        """Return the raw handle of the tensor.

    Note that the method disables the automatic garbage collection of this
    persistent tensor. The caller is now responsible for managing the life
    time of the tensor.
    """

def get_session_handle(data, name: Incomplete | None = None):
    '''Return the handle of `data`.

  This is EXPERIMENTAL and subject to change.

  Keep `data` "in-place" in the runtime and create a handle that can be
  used to retrieve `data` in a subsequent run().

  Combined with `get_session_tensor`, we can keep a tensor produced in
  one run call in place, and use it as the input in a future run call.

  Args:
    data: A tensor to be stored in the session.
    name: Optional name prefix for the return tensor.

  Returns:
    A scalar string tensor representing a unique handle for `data`.

  Raises:
    TypeError: if `data` is not a Tensor.

  Example:

  ```python
  c = tf.multiply(a, b)
  h = tf.compat.v1.get_session_handle(c)
  h = sess.run(h)

  p, a = tf.compat.v1.get_session_tensor(h.handle, tf.float32)
  b = tf.multiply(a, 10)
  c = sess.run(b, feed_dict={p: h.handle})
  ```

  '''
def get_session_tensor(handle, dtype, name: Incomplete | None = None):
    """Get the tensor of type `dtype` by feeding a tensor handle.

  This is EXPERIMENTAL and subject to change.

  Get the value of the tensor from a tensor handle. The tensor
  is produced in a previous run() and stored in the state of the
  session.

  Args:
    handle: The string representation of a persistent tensor handle.
    dtype: The type of the output tensor.
    name: Optional name prefix for the return tensor.

  Returns:
    A pair of tensors. The first is a placeholder for feeding a
    tensor handle and the second is the tensor in the session state
    keyed by the tensor handle.

  Example:

  ```python
  c = tf.multiply(a, b)
  h = tf.compat.v1.get_session_handle(c)
  h = sess.run(h)

  p, a = tf.compat.v1.get_session_tensor(h.handle, tf.float32)
  b = tf.multiply(a, 10)
  c = sess.run(b, feed_dict={p: h.handle})
  ```

  """
def delete_session_tensor(handle, name: Incomplete | None = None):
    """Delete the tensor for the given tensor handle.

  This is EXPERIMENTAL and subject to change.

  Delete the tensor of a given tensor handle. The tensor is produced
  in a previous run() and stored in the state of the session.

  Args:
    handle: The string representation of a persistent tensor handle.
    name: Optional name prefix for the return tensor.

  Returns:
    A pair of graph elements. The first is a placeholder for feeding a
    tensor handle and the second is a deletion operation.
  """
