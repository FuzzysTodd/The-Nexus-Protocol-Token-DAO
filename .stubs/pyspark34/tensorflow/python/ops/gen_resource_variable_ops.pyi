from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def assign_add_variable_op(resource, value, name: Incomplete | None = None):
    """Adds a value to the current value of a variable.

  Any ReadVariableOp with a control dependency on this op is guaranteed to
  see the incremented value or a subsequent newer one.

  Args:
    resource: A `Tensor` of type `resource`.
      handle to the resource in which to store the variable.
    value: A `Tensor`. the value by which the variable will be incremented.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AssignAddVariableOp: Incomplete

def assign_add_variable_op_eager_fallback(resource, value, name, ctx): ...
def assign_sub_variable_op(resource, value, name: Incomplete | None = None):
    """Subtracts a value from the current value of a variable.

  Any ReadVariableOp with a control dependency on this op is guaranteed to
  see the decremented value or a subsequent newer one.

  Args:
    resource: A `Tensor` of type `resource`.
      handle to the resource in which to store the variable.
    value: A `Tensor`. the value by which the variable will be incremented.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AssignSubVariableOp: Incomplete

def assign_sub_variable_op_eager_fallback(resource, value, name, ctx): ...
def assign_variable_op(resource, value, validate_shape: bool = False, name: Incomplete | None = None):
    """Assigns a new value to a variable.

  Any ReadVariableOp with a control dependency on this op is guaranteed to return
  this value or a subsequent newer value of the variable.

  Args:
    resource: A `Tensor` of type `resource`.
      handle to the resource in which to store the variable.
    value: A `Tensor`. the value to set the new tensor to use.
    validate_shape: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

AssignVariableOp: Incomplete

def assign_variable_op_eager_fallback(resource, value, validate_shape, name, ctx): ...
def consume_mutex_lock(mutex_lock, name: Incomplete | None = None):
    """This op consumes a lock created by `MutexLock`.

  This op exists to consume a tensor created by `MutexLock` (other than
  direct control dependencies).  It should be the only that consumes the tensor,
  and will raise an error if it is not.  Its only purpose is to keep the
  mutex lock tensor alive until it is consumed by this op.

  **NOTE**: This operation must run on the same device as its input.  This may
  be enforced via the `colocate_with` mechanism.

  Args:
    mutex_lock: A `Tensor` of type `variant`.
      A tensor returned by `MutexLock`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ConsumeMutexLock: Incomplete

def consume_mutex_lock_eager_fallback(mutex_lock, name, ctx): ...
def destroy_resource_op(resource, ignore_lookup_error: bool = True, name: Incomplete | None = None):
    """Deletes the resource specified by the handle.

  All subsequent operations using the resource will result in a NotFound
  error status.

  Args:
    resource: A `Tensor` of type `resource`. handle to the resource to delete.
    ignore_lookup_error: An optional `bool`. Defaults to `True`.
      whether to ignore the error when the resource
      doesn't exist.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DestroyResourceOp: Incomplete

def destroy_resource_op_eager_fallback(resource, ignore_lookup_error, name, ctx): ...
def disable_copy_on_read(resource, name: Incomplete | None = None):
    """Turns off the copy-on-read mode.

  Turns off the copy-on-read mode of a resource variable. If the variable is not in copy-on-read mode, this op has no effect.

  Args:
    resource: A `Tensor` of type `resource`.
      The resource handle of the resource variable.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

DisableCopyOnRead: Incomplete

def disable_copy_on_read_eager_fallback(resource, name, ctx): ...
def mutex_lock(mutex, name: Incomplete | None = None):
    """Locks a mutex resource.  The output is the lock.  So long as the lock tensor

  is alive, any other request to use `MutexLock` with this mutex will wait.

  This is particularly useful for creating a critical section when used in
  conjunction with `MutexLockIdentity`:

  ```python

  mutex = mutex_v2(
    shared_name=handle_name, container=container, name=name)

  def execute_in_critical_section(fn, *args, **kwargs):
    lock = gen_resource_variable_ops.mutex_lock(mutex)

    with ops.control_dependencies([lock]):
      r = fn(*args, **kwargs)

    with ops.control_dependencies(nest.flatten(r)):
      with ops.colocate_with(mutex):
        ensure_lock_exists = mutex_lock_identity(lock)

      # Make sure that if any element of r is accessed, all of
      # them are executed together.
      r = nest.map_structure(tf.identity, r)

    with ops.control_dependencies([ensure_lock_exists]):
      return nest.map_structure(tf.identity, r)
  ```

  While `fn` is running in the critical section, no other functions which wish to
  use this critical section may run.

  Often the use case is that two executions of the same graph, in parallel,
  wish to run `fn`; and we wish to ensure that only one of them executes
  at a time.  This is especially important if `fn` modifies one or more
  variables at a time.

  It is also useful if two separate functions must share a resource, but we
  wish to ensure the usage is exclusive.

  Args:
    mutex: A `Tensor` of type `resource`. The mutex resource to lock.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """

MutexLock: Incomplete

def mutex_lock_eager_fallback(mutex, name, ctx): ...
def mutex_v2(container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Creates a Mutex resource that can be locked by `MutexLock`.

  Args:
    container: An optional `string`. Defaults to `""`.
      If non-empty, this variable is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this variable is named in the given bucket
      with this shared_name. Otherwise, the node name is used instead.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

MutexV2: Incomplete

def mutex_v2_eager_fallback(container, shared_name, name, ctx): ...
def read_variable_op(resource, dtype, name: Incomplete | None = None):
    """Reads the value of a variable.

  The tensor returned by this operation is immutable.

  The value returned by this operation is guaranteed to be influenced by all the
  writes on which this operation depends directly or indirectly, and to not be
  influenced by any of the writes which depend directly or indirectly on this
  operation.

  Args:
    resource: A `Tensor` of type `resource`.
      handle to the resource in which to store the variable.
    dtype: A `tf.DType`. the dtype of the value.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

ReadVariableOp: Incomplete

def read_variable_op_eager_fallback(resource, dtype, name, ctx): ...
def resource_gather(resource, indices, dtype, batch_dims: int = 0, validate_indices: bool = True, name: Incomplete | None = None):
    """Gather slices from the variable pointed to by `resource` according to `indices`.

  `indices` must be an integer tensor of any dimension (usually 0-D or 1-D).
  Produces an output tensor with shape `indices.shape + params.shape[1:]` where:

  ```python
      # Scalar indices
      output[:, ..., :] = params[indices, :, ... :]

      # Vector indices
      output[i, :, ..., :] = params[indices[i], :, ... :]

      # Higher rank indices
      output[i, ..., j, :, ... :] = params[indices[i, ..., j], :, ..., :]
  ```

  Args:
    resource: A `Tensor` of type `resource`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    dtype: A `tf.DType`.
    batch_dims: An optional `int`. Defaults to `0`.
    validate_indices: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

ResourceGather: Incomplete

def resource_gather_eager_fallback(resource, indices, dtype, batch_dims, validate_indices, name, ctx): ...
def resource_gather_nd(resource, indices, dtype, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    resource: A `Tensor` of type `resource`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    dtype: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

ResourceGatherNd: Incomplete

def resource_gather_nd_eager_fallback(resource, indices, dtype, name, ctx): ...
def resource_scatter_add(resource, indices, updates, name: Incomplete | None = None):
    '''Adds sparse updates to the variable referenced by `resource`.

  This operation computes

      # Scalar indices
      ref[indices, ...] += updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] += updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] += updates[i, ..., j, ...]

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions add.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src=\'https://www.tensorflow.org/images/ScatterAdd.png\' alt>
  </div>

  Args:
    resource: A `Tensor` of type `resource`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A tensor of updated values to add to `ref`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

ResourceScatterAdd: Incomplete

def resource_scatter_add_eager_fallback(resource, indices, updates, name, ctx): ...
def resource_scatter_div(resource, indices, updates, name: Incomplete | None = None):
    '''Divides sparse updates into the variable referenced by `resource`.

  This operation computes

      # Scalar indices
      ref[indices, ...] /= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] /= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] /= updates[i, ..., j, ...]

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions multiply.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src=\'https://www.tensorflow.org/images/ScatterAdd.png\' alt>
  </div>

  Args:
    resource: A `Tensor` of type `resource`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A tensor of updated values to add to `ref`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

ResourceScatterDiv: Incomplete

def resource_scatter_div_eager_fallback(resource, indices, updates, name, ctx): ...
def resource_scatter_max(resource, indices, updates, name: Incomplete | None = None):
    '''Reduces sparse updates into the variable referenced by `resource` using the `max` operation.

  This operation computes

      # Scalar indices
      ref[indices, ...] = max(ref[indices, ...], updates[...])

      # Vector indices (for each i)
      ref[indices[i], ...] = max(ref[indices[i], ...], updates[i, ...])

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] = max(ref[indices[i, ..., j], ...], updates[i, ..., j, ...])

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions are combined.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src=\'https://www.tensorflow.org/images/ScatterAdd.png\' alt>
  </div>

  Args:
    resource: A `Tensor` of type `resource`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A tensor of updated values to add to `ref`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

ResourceScatterMax: Incomplete

def resource_scatter_max_eager_fallback(resource, indices, updates, name, ctx): ...
def resource_scatter_min(resource, indices, updates, name: Incomplete | None = None):
    '''Reduces sparse updates into the variable referenced by `resource` using the `min` operation.

  This operation computes

      # Scalar indices
      ref[indices, ...] = min(ref[indices, ...], updates[...])

      # Vector indices (for each i)
      ref[indices[i], ...] = min(ref[indices[i], ...], updates[i, ...])

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] = min(ref[indices[i, ..., j], ...], updates[i, ..., j, ...])

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions are combined.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src=\'https://www.tensorflow.org/images/ScatterAdd.png\' alt>
  </div>

  Args:
    resource: A `Tensor` of type `resource`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A tensor of updated values to add to `ref`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

ResourceScatterMin: Incomplete

def resource_scatter_min_eager_fallback(resource, indices, updates, name, ctx): ...
def resource_scatter_mul(resource, indices, updates, name: Incomplete | None = None):
    '''Multiplies sparse updates into the variable referenced by `resource`.

  This operation computes

      # Scalar indices
      ref[indices, ...] *= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] *= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] *= updates[i, ..., j, ...]

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions multiply.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src=\'https://www.tensorflow.org/images/ScatterAdd.png\' alt>
  </div>

  Args:
    resource: A `Tensor` of type `resource`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A tensor of updated values to add to `ref`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

ResourceScatterMul: Incomplete

def resource_scatter_mul_eager_fallback(resource, indices, updates, name, ctx): ...
def resource_scatter_sub(resource, indices, updates, name: Incomplete | None = None):
    '''Subtracts sparse updates from the variable referenced by `resource`.

  This operation computes

      # Scalar indices
      ref[indices, ...] -= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] -= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] -= updates[i, ..., j, ...]

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions add.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src=\'https://www.tensorflow.org/images/ScatterAdd.png\' alt>
  </div>

  Args:
    resource: A `Tensor` of type `resource`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A tensor of updated values to add to `ref`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

ResourceScatterSub: Incomplete

def resource_scatter_sub_eager_fallback(resource, indices, updates, name, ctx): ...
def resource_scatter_update(resource, indices, updates, name: Incomplete | None = None):
    """Assigns sparse updates to the variable referenced by `resource`.

  This operation computes

      # Scalar indices
      ref[indices, ...] = updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] = updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] = updates[i, ..., j, ...]

  Args:
    resource: A `Tensor` of type `resource`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. A tensor of updated values to add to `ref`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ResourceScatterUpdate: Incomplete

def resource_scatter_update_eager_fallback(resource, indices, updates, name, ctx): ...
def var_handle_op(dtype, shape, container: str = '', shared_name: str = '', allowed_devices=[], name: Incomplete | None = None):
    '''Creates a handle to a Variable resource.

  Args:
    dtype: A `tf.DType`. the type of this variable. Must agree with the dtypes
      of all ops using this variable.
    shape: A `tf.TensorShape` or list of `ints`.
      The (possibly partially specified) shape of this variable.
    container: An optional `string`. Defaults to `""`.
      the container this variable is placed in.
    shared_name: An optional `string`. Defaults to `""`.
      the name by which this variable is referred to.
    allowed_devices: An optional list of `strings`. Defaults to `[]`.
      DEPRECATED. The allowed devices containing the resource variable. Set when the
      output ResourceHandle represents a per-replica/partitioned resource variable.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

VarHandleOp: Incomplete

def var_handle_op_eager_fallback(dtype, shape, container, shared_name, allowed_devices, name, ctx): ...
def var_is_initialized_op(resource, name: Incomplete | None = None):
    """Checks whether a resource handle-based variable has been initialized.

  Args:
    resource: A `Tensor` of type `resource`. the input resource handle.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

VarIsInitializedOp: Incomplete

def var_is_initialized_op_eager_fallback(resource, name, ctx): ...
def variable_shape(input, out_type=..., name: Incomplete | None = None):
    """Returns the shape of the variable pointed to by `resource`.

  This operation returns a 1-D integer tensor representing the shape of `input`.

  For example:

  ```
  # 't' is [[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]]
  shape(t) ==> [2, 2, 3]
  ```

  Args:
    input: A `Tensor` of type `resource`.
    out_type: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
  """

VariableShape: Incomplete

def variable_shape_eager_fallback(input, out_type, name, ctx): ...
