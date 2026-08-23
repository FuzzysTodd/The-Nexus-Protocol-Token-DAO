from _typeshed import Incomplete
from tensorboard.compat.proto import tensor_pb2 as tensor_pb2
from tensorboard.compat.tensorflow_stub import compat as compat, dtypes as dtypes, tensor_shape as tensor_shape

def ExtractBitsFromFloat16(x): ...
def SlowAppendFloat16ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def ExtractBitsFromBFloat16(x): ...
def SlowAppendBFloat16ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendFloat32ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendFloat64ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendIntArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendInt64ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendQIntArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendUInt32ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendUInt64ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendComplex64ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendComplex128ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendObjectArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def SlowAppendBoolArrayToTensorProto(tensor_proto, proto_values) -> None: ...

BACKUP_DICT: Incomplete

def GetFromNumpyDTypeDict(dtype_dict, dtype): ...
def GetNumpyAppendFn(dtype): ...

class _Message:
    def __init__(self, message) -> None: ...

def make_tensor_proto(values, dtype: Incomplete | None = None, shape: Incomplete | None = None, verify_shape: bool = False):
    '''Create a TensorProto.

    Args:
      values:         Values to put in the TensorProto.
      dtype:          Optional tensor_pb2 DataType value.
      shape:          List of integers representing the dimensions of tensor.
      verify_shape:   Boolean that enables verification of a shape of values.

    Returns:
      A `TensorProto`. Depending on the type, it may contain data in the
      "tensor_content" attribute, which is not directly useful to Python programs.
      To access the values you should convert the proto back to a numpy ndarray
      with `tensor_util.MakeNdarray(proto)`.

      If `values` is a `TensorProto`, it is immediately returned; `dtype` and
      `shape` are ignored.

    Raises:
      TypeError:  if unsupported types are provided.
      ValueError: if arguments have inappropriate values or if verify_shape is
       True and shape of values is not equals to a shape from the argument.

    make_tensor_proto accepts "values" of a python scalar, a python list, a
    numpy ndarray, or a numpy scalar.

    If "values" is a python scalar or a python list, make_tensor_proto
    first convert it to numpy ndarray. If dtype is None, the
    conversion tries its best to infer the right numpy data
    type. Otherwise, the resulting numpy array has a convertible data
    type with the given dtype.

    In either case above, the numpy ndarray (either the caller provided
    or the auto converted) must have the convertible type with dtype.

    make_tensor_proto then converts the numpy array to a tensor proto.

    If "shape" is None, the resulting tensor proto represents the numpy
    array precisely.

    Otherwise, "shape" specifies the tensor\'s shape and the numpy array
    can not have more elements than what "shape" specifies.
    '''
def make_ndarray(tensor):
    """Create a numpy ndarray from a tensor.

    Create a numpy ndarray with the same shape and data as the tensor.

    Args:
      tensor: A TensorProto.

    Returns:
      A numpy array with the tensor contents.

    Raises:
      TypeError: if tensor has unsupported type.
    """
