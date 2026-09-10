from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def configure_and_initialize_global_tpu(use_tfrt_host_runtime: bool = True, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    use_tfrt_host_runtime: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

ConfigureAndInitializeGlobalTPU: Incomplete

def configure_and_initialize_global_tpu_eager_fallback(use_tfrt_host_runtime, name, ctx): ...
def copy_to_mesh(input, layout, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input: A `Tensor`.
    layout: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

CopyToMesh: Incomplete

def copy_to_mesh_eager_fallback(input, layout, name, ctx): ...
def copy_to_mesh_grad(input, forward_input, reference_layout: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    input: A `Tensor`.
    forward_input: A `Tensor`. Must have the same type as `input`.
    reference_layout: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CopyToMeshGrad: Incomplete

def copy_to_mesh_grad_eager_fallback(input, forward_input, reference_layout, name, ctx): ...
def d_tensor_restore_v2(prefix, tensor_names, shape_and_slices, input_shapes, input_layouts, dtypes, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    prefix: A `Tensor` of type `string`.
    tensor_names: A `Tensor` of type `string`.
    shape_and_slices: A `Tensor` of type `string`.
    input_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
    input_layouts: A list of `strings`.
    dtypes: A list of `tf.DTypes` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `dtypes`.
  """

DTensorRestoreV2: Incomplete

def d_tensor_restore_v2_eager_fallback(prefix, tensor_names, shape_and_slices, input_shapes, input_layouts, dtypes, name, ctx): ...
def d_tensor_set_global_tpu_array(topology, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    topology: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DTensorSetGlobalTPUArray: Incomplete

def d_tensor_set_global_tpu_array_eager_fallback(topology, name, ctx): ...
def relayout(input, layout, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    input: A `Tensor`.
    layout: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

Relayout: Incomplete

def relayout_eager_fallback(input, layout, name, ctx): ...
def shutdown_tpu_system(name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

ShutdownTPUSystem: Incomplete

def shutdown_tpu_system_eager_fallback(name, ctx): ...
