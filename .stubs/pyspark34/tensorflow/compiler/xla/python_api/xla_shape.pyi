from _typeshed import Incomplete
from tensorflow.compiler.xla import xla_data_pb2 as xla_data_pb2
from tensorflow.compiler.xla.python_api import types as types

class Shape:
    """Wraps a xla_data_pb2.ShapeProto message with a convenient Python type.

  Provides direct access to the underlying xla_data_pb2.ShapeProto message in
  the
  message attribute, along with accessor wrappers to the message's fields.
  Avoid direct access to .message unless interacting directly with protobuf APIs
  like CopyFrom. In other words, prefer hauling the shape around in a Shape, and
  only access .message when strictly required by the protobuf API.
  """
    message: Incomplete
    def __init__(self, element_type, dimensions, layout: Incomplete | None = None) -> None:
        """Creates a new XLA Shape.

    Args:
      element_type: element type from xla_data_pb2.
      dimensions: sequence of dimensions sizes (integers), or sequence
        of Shapes in the case of a tuple, i.e. when element_type is
        TUPLE.
      layout: optional minor_to_major sequence for layout. If not given, the
        default major-to-minor layout is used.

    Raises:
      ValueError: if element_type is TUPLE but dimensions are not Shape objects.
    """
    def element_type(self): ...
    def is_tuple(self): ...
    def dimensions(self): ...
    def tuple_shapes(self):
        """If this is a tuple, returns its sequence of constituent Shape objects.

    Returns:
      Tuple sub-shapes.

    Raises:
      ValueError: if this is not a tuple.
    """
    def layout(self): ...
    @staticmethod
    def from_pyval(pyval): ...

def CreateShapeFromNumpy(value):
    """Create a Shape from a Numpy array or a nested tuple structure thereof.

  Args:
    value: Numpy array or (possibly nested) tuple structure that bottoms out in
      Numpy arrays.

  Returns:
    A Shape object.
  """
def CreateShapeFromDtypeAndTuple(dtype, shape_tuple):
    """Create a shape from a Numpy dtype and a sequence of nonnegative integers.

  Args:
    dtype: a numpy dtype, e.g. np.dtype('int32').
    shape_tuple: a sequence of nonnegative integers.

  Returns:
    A Shape object.
  """
