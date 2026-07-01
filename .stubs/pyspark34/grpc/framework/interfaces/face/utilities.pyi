from _typeshed import Incomplete
from grpc.framework.common import cardinality as cardinality, style as style
from grpc.framework.foundation import stream as stream
from grpc.framework.interfaces.face import face as face
from typing import NamedTuple

class _MethodImplementation(face.MethodImplementation, NamedTuple('_MethodImplementation', [('cardinality', Incomplete), ('style', Incomplete), ('unary_unary_inline', Incomplete), ('unary_stream_inline', Incomplete), ('stream_unary_inline', Incomplete), ('stream_stream_inline', Incomplete), ('unary_unary_event', Incomplete), ('unary_stream_event', Incomplete), ('stream_unary_event', Incomplete), ('stream_stream_event', Incomplete)])): ...

def unary_unary_inline(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a unary-unary RPC method as a callable value
      that takes a request value and an face.ServicerContext object and
      returns a response value.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
def unary_stream_inline(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a unary-stream RPC method as a callable
      value that takes a request value and an face.ServicerContext object and
      returns an iterator of response values.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
def stream_unary_inline(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a stream-unary RPC method as a callable
      value that takes an iterator of request values and an
      face.ServicerContext object and returns a response value.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
def stream_stream_inline(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a stream-stream RPC method as a callable
      value that takes an iterator of request values and an
      face.ServicerContext object and returns an iterator of response values.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
def unary_unary_event(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a unary-unary RPC method as a callable
      value that takes a request value, a response callback to which to pass
      the response value of the RPC, and an face.ServicerContext.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
def unary_stream_event(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a unary-stream RPC method as a callable
      value that takes a request value, a stream.Consumer to which to pass the
      the response values of the RPC, and an face.ServicerContext.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
def stream_unary_event(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a stream-unary RPC method as a callable
      value that takes a response callback to which to pass the response value
      of the RPC and an face.ServicerContext and returns a stream.Consumer to
      which the request values of the RPC should be passed.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
def stream_stream_event(behavior):
    """Creates an face.MethodImplementation for the given behavior.

  Args:
    behavior: The implementation of a stream-stream RPC method as a callable
      value that takes a stream.Consumer to which to pass the response values
      of the RPC and an face.ServicerContext and returns a stream.Consumer to
      which the request values of the RPC should be passed.

  Returns:
    An face.MethodImplementation derived from the given behavior.
  """
