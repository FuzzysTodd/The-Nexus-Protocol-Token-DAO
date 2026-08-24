from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def a(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

A: Incomplete

def a_eager_fallback(name, ctx): ...
def attr(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: An `int`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

Attr: Incomplete

def attr_eager_fallback(a, name, ctx): ...
def attr_bool(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrBool: Incomplete

def attr_bool_eager_fallback(a, name, ctx): ...
def attr_bool_list(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `bools`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrBoolList: Incomplete

def attr_bool_list_eager_fallback(a, name, ctx): ...
def attr_default(a: str = 'banana', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    a: An optional `string`. Defaults to `"banana"`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

AttrDefault: Incomplete

def attr_default_eager_fallback(a, name, ctx): ...
def attr_empty_list_default(a=[], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: An optional list of `floats`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrEmptyListDefault: Incomplete

def attr_empty_list_default_eager_fallback(a, name, ctx): ...
def attr_enum(a, name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    a: A `string` from: `"apples", "oranges"`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

AttrEnum: Incomplete

def attr_enum_eager_fallback(a, name, ctx): ...
def attr_enum_list(a, name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    a: A list of `strings` from: `"apples", "oranges"`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

AttrEnumList: Incomplete

def attr_enum_list_eager_fallback(a, name, ctx): ...
def attr_float(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `float`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrFloat: Incomplete

def attr_float_eager_fallback(a, name, ctx): ...
def attr_list_default(a=[5, 15], name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: An optional list of `ints`. Defaults to `[5, 15]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrListDefault: Incomplete

def attr_list_default_eager_fallback(a, name, ctx): ...
def attr_list_min(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `ints` that has length `>= 2`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrListMin: Incomplete

def attr_list_min_eager_fallback(a, name, ctx): ...
def attr_list_type_default(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of at least 1 `Tensor` objects with the same type.
    b: A list with the same length as `a` of `Tensor` objects with the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrListTypeDefault: Incomplete

def attr_list_type_default_eager_fallback(a, b, name, ctx): ...
def attr_min(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: An `int` that is `>= 5`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrMin: Incomplete

def attr_min_eager_fallback(a, name, ctx): ...
def attr_partial_shape(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `tf.TensorShape` or list of `ints`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrPartialShape: Incomplete

def attr_partial_shape_eager_fallback(a, name, ctx): ...
def attr_partial_shape_list(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of shapes (each a `tf.TensorShape` or list of `ints`).
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrPartialShapeList: Incomplete

def attr_partial_shape_list_eager_fallback(a, name, ctx): ...
def attr_shape(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `tf.TensorShape` or list of `ints`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrShape: Incomplete

def attr_shape_eager_fallback(a, name, ctx): ...
def attr_shape_list(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of shapes (each a `tf.TensorShape` or list of `ints`).
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrShapeList: Incomplete

def attr_shape_list_eager_fallback(a, name, ctx): ...
def attr_type_default(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AttrTypeDefault: Incomplete

def attr_type_default_eager_fallback(a, name, ctx): ...
def b(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

B: Incomplete

def b_eager_fallback(name, ctx): ...
def binary(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor`.
    b: A `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Binary: Incomplete

def binary_eager_fallback(a, b, name, ctx): ...

class _ComplexStructOutput(NamedTuple):
    a: Incomplete
    b: Incomplete
    c: Incomplete

def complex_struct(n_a, n_b, t_c, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    n_a: An `int` that is `>= 0`.
    n_b: An `int` that is `>= 0`.
    t_c: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b, c).

    a: A list of `n_a` `Tensor` objects with type `int32`.
    b: A list of `n_b` `Tensor` objects with type `int64`.
    c: A list of `Tensor` objects of type `t_c`.
  """

ComplexStruct: Incomplete

def complex_struct_eager_fallback(n_a, n_b, t_c, name, ctx): ...
def copy_op(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

CopyOp: Incomplete

def copy_op_eager_fallback(a, name, ctx): ...
def default_attrs(string_val: str = 'abc', string_list_val=['abc', ''], int_val: int = 123, int_list_val=[1, 2, 3], float_val: int = 10, float_list_val=[10], bool_val: bool = True, bool_list_val=[True, False], type_val=..., type_list_val=..., shape_val=[2, 1], shape_list_val=[[], [1]], tensor_val=..., tensor_list_val=..., name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    string_val: An optional `string`. Defaults to `"abc"`.
    string_list_val: An optional list of `strings`. Defaults to `["abc", ""]`.
    int_val: An optional `int`. Defaults to `123`.
    int_list_val: An optional list of `ints`. Defaults to `[1, 2, 3]`.
    float_val: An optional `float`. Defaults to `10`.
    float_list_val: An optional list of `floats`. Defaults to `[10]`.
    bool_val: An optional `bool`. Defaults to `True`.
    bool_list_val: An optional list of `bools`. Defaults to `[True, False]`.
    type_val: An optional `tf.DType`. Defaults to `tf.int32`.
    type_list_val: An optional list of `tf.DTypes`. Defaults to `[tf.int32, tf.float32]`.
    shape_val: An optional `tf.TensorShape` or list of `ints`. Defaults to `[2, 1]`.
    shape_list_val: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[[], [1]]`.
    tensor_val: An optional `tf.TensorProto`. Defaults to `dtype: DT_INT32 tensor_shape { } int_val: 1`.
    tensor_list_val: An optional list of `tf.TensorProto` objects. Defaults to `[dtype: DT_INT32 tensor_shape { } int_val: 1]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

DefaultAttrs: Incomplete

def default_attrs_eager_fallback(string_val, string_list_val, int_val, int_list_val, float_val, float_list_val, bool_val, bool_list_val, type_val, type_list_val, shape_val, shape_list_val, tensor_val, tensor_list_val, name, ctx): ...
def device_placement_op(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

DevicePlacementOp: Incomplete

def device_placement_op_eager_fallback(name, ctx): ...
def dtype_with_default_op(in_, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    in_: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

DtypeWithDefaultOp: Incomplete

def dtype_with_default_op_eager_fallback(in_, name, ctx): ...

class _FiveFloatOutputsOutput(NamedTuple):
    a: Incomplete
    b: Incomplete
    c: Incomplete
    d: Incomplete
    e: Incomplete

def five_float_outputs(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b, c, d, e).

    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    c: A `Tensor` of type `float32`.
    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `float32`.
  """

FiveFloatOutputs: Incomplete

def five_float_outputs_eager_fallback(name, ctx): ...
def float_input(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

FloatInput: Incomplete

def float_input_eager_fallback(a, name, ctx): ...
def float_output(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

FloatOutput: Incomplete

def float_output_eager_fallback(name, ctx): ...

class _FloatOutputStringOutputOutput(NamedTuple):
    a: Incomplete
    b: Incomplete

def float_output_string_output(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `string`.
  """

FloatOutputStringOutput: Incomplete

def float_output_string_output_eager_fallback(name, ctx): ...

class _Foo1Output(NamedTuple):
    d: Incomplete
    e: Incomplete

def foo1(a, b, c, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `int32`.
    c: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (d, e).

    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `int32`.
  """

Foo1: Incomplete

def foo1_eager_fallback(a, b, c, name, ctx): ...

class _Foo2Output(NamedTuple):
    d: Incomplete
    e: Incomplete

def foo2(a, b, c, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `string`.
    c: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (d, e).

    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `int32`.
  """

Foo2: Incomplete

def foo2_eager_fallback(a, b, c, name, ctx): ...

class _Foo3Output(NamedTuple):
    d: Incomplete
    e: Incomplete

def foo3(a, b, c, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `string`.
    c: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (d, e).

    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `int32`.
  """

Foo3: Incomplete

def foo3_eager_fallback(a, b, c, name, ctx): ...
def func_attr(f, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    f: A function decorated with @Defun.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

FuncAttr: Incomplete

def func_attr_eager_fallback(f, name, ctx): ...
def func_list_attr(f, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    f: A list of functions decorated with @Defun.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

FuncListAttr: Incomplete

def func_list_attr_eager_fallback(f, name, ctx): ...
def get_deadline(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

GetDeadline: Incomplete

def get_deadline_eager_fallback(name, ctx): ...
def graph_def_version(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

GraphDefVersion: Incomplete

def graph_def_version_eager_fallback(name, ctx): ...
def in_polymorphic_twice(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `Tensor` objects with the same type.
    b: A list of `Tensor` objects with the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

InPolymorphicTwice: Incomplete

def in_polymorphic_twice_eager_fallback(a, b, name, ctx): ...
def int64_output(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

Int64Output: Incomplete

def int64_output_eager_fallback(name, ctx): ...
def int_attr(foo: int = 1, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    foo: An optional `int`. Defaults to `1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

IntAttr: Incomplete

def int_attr_eager_fallback(foo, name, ctx): ...
def int_input(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

IntInput: Incomplete

def int_input_eager_fallback(a, name, ctx): ...
def int_input_float_input(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

IntInputFloatInput: Incomplete

def int_input_float_input_eager_fallback(a, b, name, ctx): ...
def int_input_int_output(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

IntInputIntOutput: Incomplete

def int_input_int_output_eager_fallback(a, name, ctx): ...
def int_output(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

IntOutput: Incomplete

def int_output_eager_fallback(name, ctx): ...

class _IntOutputFloatOutputOutput(NamedTuple):
    a: Incomplete
    b: Incomplete

def int_output_float_output(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `float32`.
  """

IntOutputFloatOutput: Incomplete

def int_output_float_output_eager_fallback(name, ctx): ...
def is_resource_handle_ref_counting(handle, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    handle: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

IsResourceHandleRefCounting: Incomplete

def is_resource_handle_ref_counting_eager_fallback(handle, name, ctx): ...
def is_tensor_float32_enabled(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

IsTensorFloat32Enabled: Incomplete

def is_tensor_float32_enabled_eager_fallback(name, ctx): ...
def kernel_label(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

KernelLabel: Incomplete

def kernel_label_eager_fallback(name, ctx): ...
def kernel_label_required(input, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

KernelLabelRequired: Incomplete

def kernel_label_required_eager_fallback(input, name, ctx): ...
def list_input(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of at least 1 `Tensor` objects with the same type.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ListInput: Incomplete

def list_input_eager_fallback(a, name, ctx): ...
def list_output(T, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A list of `tf.DTypes` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `T`.
  """

ListOutput: Incomplete

def list_output_eager_fallback(T, name, ctx): ...
def make_weak_resource_handle(handle, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    handle: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """

MakeWeakResourceHandle: Incomplete

def make_weak_resource_handle_eager_fallback(handle, name, ctx): ...

class _MixedStructOutput(NamedTuple):
    a: Incomplete
    b: Incomplete

def mixed_struct(n_a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    n_a: An `int` that is `>= 0`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A list of `n_a` `Tensor` objects with type `int32`.
    b: A `Tensor` of type `float32`.
  """

MixedStruct: Incomplete

def mixed_struct_eager_fallback(n_a, name, ctx): ...
def n_in_polymorphic_twice(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `Tensor` objects with the same type.
    b: A list with the same length as `a` of `Tensor` objects with the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

NInPolymorphicTwice: Incomplete

def n_in_polymorphic_twice_eager_fallback(a, b, name, ctx): ...
def n_in_twice(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `Tensor` objects with type `int32`.
    b: A list with the same length as `a` of `Tensor` objects with type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

NInTwice: Incomplete

def n_in_twice_eager_fallback(a, b, name, ctx): ...
def n_in_two_type_variables(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `Tensor` objects with the same type.
    b: A list with the same length as `a` of `Tensor` objects with the same type.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

NInTwoTypeVariables: Incomplete

def n_in_two_type_variables_eager_fallback(a, b, name, ctx): ...
def n_ints_in(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of at least 2 `Tensor` objects with type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

NIntsIn: Incomplete

def n_ints_in_eager_fallback(a, name, ctx): ...
def n_ints_out(N, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    N: An `int` that is `>= 2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `int32`.
  """

NIntsOut: Incomplete

def n_ints_out_eager_fallback(N, name, ctx): ...
def n_ints_out_default(N: int = 3, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    N: An optional `int` that is `>= 2`. Defaults to `3`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `int32`.
  """

NIntsOutDefault: Incomplete

def n_ints_out_default_eager_fallback(N, name, ctx): ...
def n_polymorphic_in(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of at least 2 `Tensor` objects with the same type.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

NPolymorphicIn: Incomplete

def n_polymorphic_in_eager_fallback(a, name, ctx): ...
def n_polymorphic_out(T, N, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A `tf.DType`.
    N: An `int` that is `>= 2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `T`.
  """

NPolymorphicOut: Incomplete

def n_polymorphic_out_eager_fallback(T, N, name, ctx): ...
def n_polymorphic_out_default(T=..., N: int = 2, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: An optional `tf.DType`. Defaults to `tf.bool`.
    N: An optional `int` that is `>= 2`. Defaults to `2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `T`.
  """

NPolymorphicOutDefault: Incomplete

def n_polymorphic_out_default_eager_fallback(T, N, name, ctx): ...
def n_polymorphic_restrict_in(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of at least 2 `Tensor` objects with the same type in: `string`, `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

NPolymorphicRestrictIn: Incomplete

def n_polymorphic_restrict_in_eager_fallback(a, name, ctx): ...
def n_polymorphic_restrict_out(T, N, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A `tf.DType` from: `tf.string, tf.bool`.
    N: An `int` that is `>= 2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `T`.
  """

NPolymorphicRestrictOut: Incomplete

def n_polymorphic_restrict_out_eager_fallback(T, N, name, ctx): ...

class _Namespace_TestStringOutputOutput(NamedTuple):
    output1: Incomplete
    output2: Incomplete

def namespace_test_string_output(input, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output1, output2).

    output1: A `Tensor` of type `float32`.
    output2: A `Tensor` of type `string`.
  """

Namespace_TestStringOutput: Incomplete

def namespace_test_string_output_eager_fallback(input, name, ctx): ...
def none(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

None_: Incomplete

def none_eager_fallback(name, ctx): ...
def old(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

Old: Incomplete

def old_eager_fallback(name, ctx): ...
def op_with_default_attr(default_float: int = 123, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    default_float: An optional `float`. Defaults to `123`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

OpWithDefaultAttr: Incomplete

def op_with_default_attr_eager_fallback(default_float, name, ctx): ...
def op_with_future_default_attr(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

OpWithFutureDefaultAttr: Incomplete

def op_with_future_default_attr_eager_fallback(name, ctx): ...
def out_t(T, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  """

OutT: Incomplete

def out_t_eager_fallback(T, name, ctx): ...
def out_type_list(T, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `T`.
  """

OutTypeList: Incomplete

def out_type_list_eager_fallback(T, name, ctx): ...
def out_type_list_restrict(t, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    t: A list of `tf.DTypes` from: `tf.string, tf.bool` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `t`.
  """

OutTypeListRestrict: Incomplete

def out_type_list_restrict_eager_fallback(t, name, ctx): ...
def polymorphic(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Polymorphic: Incomplete

def polymorphic_eager_fallback(a, name, ctx): ...
def polymorphic_default_out(T=..., name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: An optional `tf.DType`. Defaults to `tf.string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  """

PolymorphicDefaultOut: Incomplete

def polymorphic_default_out_eager_fallback(T, name, ctx): ...
def polymorphic_out(T, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  """

PolymorphicOut: Incomplete

def polymorphic_out_eager_fallback(T, name, ctx): ...
def ref_in(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A mutable `Tensor`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

RefIn: Incomplete

def ref_in_eager_fallback(a, name, ctx) -> None: ...
def ref_input_float_input(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type mutable `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

RefInputFloatInput: Incomplete

def ref_input_float_input_eager_fallback(a, b, name, ctx) -> None: ...
def ref_input_float_input_int_output(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type mutable `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

RefInputFloatInputIntOutput: Incomplete

def ref_input_float_input_int_output_eager_fallback(a, b, name, ctx) -> None: ...
def ref_input_int_input(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type mutable `int32`.
    b: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

RefInputIntInput: Incomplete

def ref_input_int_input_eager_fallback(a, b, name, ctx) -> None: ...
def ref_out(T, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor` of type `T`.
  """

RefOut: Incomplete

def ref_out_eager_fallback(T, name, ctx) -> None: ...
def ref_output(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type mutable `int32`.
  """

RefOutput: Incomplete

def ref_output_eager_fallback(name, ctx) -> None: ...

class _RefOutputFloatOutputOutput(NamedTuple):
    a: Incomplete
    b: Incomplete

def ref_output_float_output(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type mutable `float32`.
    b: A `Tensor` of type `float32`.
  """

RefOutputFloatOutput: Incomplete

def ref_output_float_output_eager_fallback(name, ctx) -> None: ...
def requires_older_graph_version(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

RequiresOlderGraphVersion: Incomplete

def requires_older_graph_version_eager_fallback(name, ctx): ...
def reserved_attr(range, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    range: An `int`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ReservedAttr: Incomplete

def reserved_attr_eager_fallback(range, name, ctx): ...
def reserved_input(input, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ReservedInput: Incomplete

def reserved_input_eager_fallback(input, name, ctx): ...
def resource_create_op(resource, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ResourceCreateOp: Incomplete

def resource_create_op_eager_fallback(resource, name, ctx): ...
def resource_initialized_op(resource, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

ResourceInitializedOp: Incomplete

def resource_initialized_op_eager_fallback(resource, name, ctx): ...
def resource_using_op(resource, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ResourceUsingOp: Incomplete

def resource_using_op_eager_fallback(resource, name, ctx): ...
def restrict(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor`. Must be one of the following types: `string`, `bool`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Restrict: Incomplete

def restrict_eager_fallback(a, name, ctx): ...
def simple(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

Simple: Incomplete

def simple_eager_fallback(a, name, ctx): ...
def simple_struct(n_a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    n_a: An `int` that is `>= 0`.
    name: A name for the operation (optional).

  Returns:
    A list of `n_a` `Tensor` objects with type `int32`.
  """

SimpleStruct: Incomplete

def simple_struct_eager_fallback(n_a, name, ctx): ...
def sleep_identity_op(sleep_seconds, input, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    sleep_seconds: A `Tensor` of type `int32`.
    input: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

SleepIdentityOp: Incomplete

def sleep_identity_op_eager_fallback(sleep_seconds, input, name, ctx): ...
def sleep_op(sleep_seconds, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    sleep_seconds: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

SleepOp: Incomplete

def sleep_op_eager_fallback(sleep_seconds, name, ctx): ...
def string_list_attr(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `strings`.
    b: A `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

StringListAttr: Incomplete

def string_list_attr_eager_fallback(a, b, name, ctx): ...
def stub_resource_handle_op(container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

StubResourceHandleOp: Incomplete

def stub_resource_handle_op_eager_fallback(container, shared_name, name, ctx): ...
def test_attr(T, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    T: A `tf.DType` from: `tf.float32, tf.float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  """

TestAttr: Incomplete

def test_attr_eager_fallback(T, name, ctx): ...

class _TestStringOutputOutput(NamedTuple):
    output1: Incomplete
    output2: Incomplete

def test_string_output(input, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output1, output2).

    output1: A `Tensor` of type `float32`.
    output2: A `Tensor` of type `string`.
  """

TestStringOutput: Incomplete

def test_string_output_eager_fallback(input, name, ctx): ...
def two_float_inputs(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

TwoFloatInputs: Incomplete

def two_float_inputs_eager_fallback(a, b, name, ctx): ...
def two_float_inputs_float_output(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

TwoFloatInputsFloatOutput: Incomplete

def two_float_inputs_float_output_eager_fallback(a, b, name, ctx): ...
def two_float_inputs_int_output(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

TwoFloatInputsIntOutput: Incomplete

def two_float_inputs_int_output_eager_fallback(a, b, name, ctx): ...

class _TwoFloatOutputsOutput(NamedTuple):
    a: Incomplete
    b: Incomplete

def two_float_outputs(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
  """

TwoFloatOutputs: Incomplete

def two_float_outputs_eager_fallback(name, ctx): ...
def two_int_inputs(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

TwoIntInputs: Incomplete

def two_int_inputs_eager_fallback(a, b, name, ctx): ...

class _TwoIntOutputsOutput(NamedTuple):
    a: Incomplete
    b: Incomplete

def two_int_outputs(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `int32`.
  """

TwoIntOutputs: Incomplete

def two_int_outputs_eager_fallback(name, ctx): ...
def two_refs_in(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A mutable `Tensor`.
    b: A mutable `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

TwoRefsIn: Incomplete

def two_refs_in_eager_fallback(a, b, name, ctx) -> None: ...
def type_list(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `Tensor` objects.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

TypeList: Incomplete

def type_list_eager_fallback(a, name, ctx): ...
def type_list_restrict(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `Tensor` objects with types from: `string`, `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

TypeListRestrict: Incomplete

def type_list_restrict_eager_fallback(a, name, ctx): ...
def type_list_twice(a, b, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A list of `Tensor` objects.
    b: A list of `Tensor` objects. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

TypeListTwice: Incomplete

def type_list_twice_eager_fallback(a, b, name, ctx): ...
def unary(a, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Unary: Incomplete

def unary_eager_fallback(a, name, ctx): ...
