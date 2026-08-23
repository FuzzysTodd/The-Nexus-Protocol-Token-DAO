from _typeshed import Incomplete
from tensorflow.core.framework import tensor_pb2 as tensor_pb2, tensor_shape_pb2 as tensor_shape_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, errors_impl as errors_impl, fast_tensor_util as fast_tensor_util, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.types import core as core, internal as internal
from tensorflow.python.util import compat as compat, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

def ExtractBitsFromFloat16(x): ...
def SlowAppendFloat16ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def ExtractBitsFromBFloat16(x): ...
def SlowAppendBFloat16ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def FastAppendBFloat16ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def ExtractBitsFromFloat8e5m2(x): ...
def SlowAppendFloat8e5m2ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def FastAppendFloat8e5m2ArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def ExtractBitsFromFloat8e4m3fn(x): ...
def SlowAppendFloat8e4m3fnArrayToTensorProto(tensor_proto, proto_values) -> None: ...
def FastAppendFloat8e4m3fnArrayToTensorProto(tensor_proto, proto_values) -> None: ...
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
def GetFromNumpyDTypeDict(dtype_dict, dtype): ...
def GetNumpyAppendFn(dtype): ...
def TensorShapeProtoToList(shape):
    """Convert a TensorShape to a list.

  Args:
    shape: A TensorShapeProto.

  Returns:
    List of integers representing the dimensions of the tensor.
  """
def make_tensor_proto(values, dtype: Incomplete | None = None, shape: Incomplete | None = None, verify_shape: bool = False, allow_broadcast: bool = False):
    '''Create a TensorProto.

  In TensorFlow 2.0, representing tensors as protos should no longer be a
  common workflow. That said, this utility function is still useful for
  generating TF Serving request protos:

  ```python
    request = tensorflow_serving.apis.predict_pb2.PredictRequest()
    request.model_spec.name = "my_model"
    request.model_spec.signature_name = "serving_default"
    request.inputs["images"].CopyFrom(tf.make_tensor_proto(X_new))
  ```

  `make_tensor_proto` accepts "values" of a python scalar, a python list, a
  numpy ndarray, or a numpy scalar.

  If "values" is a python scalar or a python list, make_tensor_proto
  first convert it to numpy ndarray. If dtype is None, the
  conversion tries its best to infer the right numpy data
  type. Otherwise, the resulting numpy array has a compatible data
  type with the given dtype.

  In either case above, the numpy ndarray (either the caller provided
  or the auto-converted) must have the compatible type with dtype.

  `make_tensor_proto` then converts the numpy array to a tensor proto.

  If "shape" is None, the resulting tensor proto represents the numpy
  array precisely.

  Otherwise, "shape" specifies the tensor\'s shape and the numpy array
  can not have more elements than what "shape" specifies.

  Args:
    values:         Values to put in the TensorProto.
    dtype:          Optional tensor_pb2 DataType value.
    shape:          List of integers representing the dimensions of tensor.
    verify_shape:   Boolean that enables verification of a shape of values.
    allow_broadcast:  Boolean that enables allowing scalars and 1 length vector
        broadcasting. Cannot be true when verify_shape is true.

  Returns:
    A `TensorProto`. Depending on the type, it may contain data in the
    "tensor_content" attribute, which is not directly useful to Python programs.
    To access the values you should convert the proto back to a numpy ndarray
    with `tf.make_ndarray(proto)`.

    If `values` is a `TensorProto`, it is immediately returned; `dtype` and
    `shape` are ignored.

  Raises:
    TypeError:  if unsupported types are provided.
    ValueError: if arguments have inappropriate values or if verify_shape is
     True and shape of values is not equals to a shape from the argument.

  '''
def MakeNdarray(tensor):
    """Create a numpy ndarray from a tensor.

  Create a numpy ndarray with the same shape and data as the tensor.

  For example:

  ```python
  # Tensor a has shape (2,3)
  a = tf.constant([[1,2,3],[4,5,6]])
  proto_tensor = tf.make_tensor_proto(a)  # convert `tensor a` to a proto tensor
  tf.make_ndarray(proto_tensor) # output: array([[1, 2, 3],
  #                                              [4, 5, 6]], dtype=int32)
  # output has shape (2,3)
  ```

  Args:
    tensor: A TensorProto.

  Returns:
    A numpy array with the tensor contents.

  Raises:
    TypeError: if tensor has unsupported type.

  """
def ShapeEquals(tensor_proto, shape):
    '''Returns True if "tensor_proto" has the given "shape".

  Args:
    tensor_proto: A TensorProto.
    shape: A tensor shape, expressed as a TensorShape, list, or tuple.

  Returns:
    True if "tensor_proto" has the given "shape", otherwise False.

  Raises:
    TypeError: If "tensor_proto" is not a TensorProto, or shape is not a
      TensorShape, list, or tuple.
  '''
def constant_value(tensor, partial: bool = False):
    """Returns the constant value of the given tensor, if efficiently calculable.

  This function attempts to partially evaluate the given tensor, and
  returns its value as a numpy ndarray if this succeeds.

  Example usage:

  >>> a = tf.constant(10)
  >>> tf.get_static_value(a)
  10
  >>> b = tf.constant(20)
  >>> tf.get_static_value(tf.add(a, b))
  30

  >>> # `tf.Variable` is not supported.
  >>> c = tf.Variable(30)
  >>> print(tf.get_static_value(c))
  None

  Using `partial` option is most relevant when calling `get_static_value` inside
  a `tf.function`. Setting it to `True` will return the results but for the
  values that cannot be evaluated will be `None`. For example:

  ```python
  class Foo:
    def __init__(self):
      self.a = tf.Variable(1)
      self.b = tf.constant(2)

    @tf.function
    def bar(self, partial):
      packed = tf.raw_ops.Pack(values=[self.a, self.b])
      static_val = tf.get_static_value(packed, partial=partial)
      tf.print(static_val)

  f = Foo()
  f.bar(partial=True)  # `array([None, array(2, dtype=int32)], dtype=object)`
  f.bar(partial=False)  # `None`
  ```

  Compatibility(V1): If `constant_value(tensor)` returns a non-`None` result, it
  will no longer be possible to feed a different value for `tensor`. This allows
  the result of this function to influence the graph that is constructed, and
  permits static shape optimizations.

  Args:
    tensor: The Tensor to be evaluated.
    partial: If True, the returned numpy array is allowed to have partially
      evaluated values. Values that can't be evaluated will be None.

  Returns:
    A numpy ndarray containing the constant value of the given `tensor`,
    or None if it cannot be calculated.

  Raises:
    TypeError: if tensor is not an ops.Tensor.
  """
def constant_value_as_shape(tensor):
    """A version of `constant_value()` that returns a `TensorShape`.

  This version should be used when a constant tensor value is
  interpreted as a (possibly partial) shape, e.g. in the shape
  function for `tf.reshape()`. By explicitly requesting a
  `TensorShape` as the return value, it is possible to represent
  unknown dimensions; by contrast, `constant_value()` is
  all-or-nothing.

  Args:
    tensor: The rank-0 or rank-1 Tensor to be evaluated.

  Returns:
    A `TensorShape` based on the constant value of the given `tensor`.

  Raises:
    ValueError: If the shape is rank-0 and is not statically known to be -1.
  """
def is_tf_type(x):
    """Checks whether `x` is a TF-native type that can be passed to many TF ops.

  Use `is_tensor` to differentiate types that can ingested by TensorFlow ops
  without any conversion (e.g., `tf.Tensor`, `tf.SparseTensor`, and
  `tf.RaggedTensor`) from types that need to be converted into tensors before
  they are ingested (e.g., numpy `ndarray` and Python scalars).

  For example, in the following code block:

  ```python
  if not tf.is_tensor(t):
    t = tf.convert_to_tensor(t)
  return t.shape, t.dtype
  ```

  we check to make sure that `t` is a tensor (and convert it if not) before
  accessing its `shape` and `dtype`.  (But note that not all TensorFlow native
  types have shapes or dtypes; `tf.data.Dataset` is an example of a TensorFlow
  native type that has neither shape nor dtype.)

  Args:
    x: A python object to check.

  Returns:
    `True` if `x` is a TensorFlow-native type.
  """
is_tensor = is_tf_type

def shape_tensor(shape):
    """Convert to an int32 or int64 tensor, defaulting to int32 if empty."""
def maybe_set_static_shape(tensor, shape) -> None:
    """Sets the shape of `tensor` to the `shape`'s constant value, if inferrable.

  This is a temporary workaround to fix shape inference across functional op
  boundaries. E.g.

  ```python
  shape = tf.constant([3])
  @tf.function
  def f():
    u = tf.random_uniform(shape)
    return u
  ```

  If we were to rely solely on C++ shape inference, the shape of `u` inside
  `f` would be unknown because C++ shape inference is not aware of the outer
  graph and all it sees is a Placeholder node when backtracing the captured
  tensor for `shape`. `maybe_set_static_shape` computes the static shape value
  of `shape` by traversing the `FuncGraph` boundaries and sets the correct
  shape.

  A longer term solution would be to fix C++ shape inference.

  Args:
    tensor: A tensor.
    shape: A shape tensor.
  """
def try_evaluate_constant(tensor):
    """Evaluates a symbolic tensor as a constant.

  Args:
    tensor: a symbolic Tensor.

  Returns:
    ndarray if the evaluation succeeds, or None if it fails.
  """
