from tensorflow.python.ops.gen_state_ops import *
from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_math_ops as gen_math_ops, gen_resource_variable_ops as gen_resource_variable_ops, gen_state_ops as gen_state_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export

def variable_op(shape, dtype, name: str = 'Variable', set_shape: bool = True, container: str = '', shared_name: str = ''):
    """Deprecated. Used variable_op_v2 instead."""
def variable_op_v2(shape, dtype, name: str = 'Variable', container: str = '', shared_name: str = ''):
    '''Create a variable Operation.

  See also variables.Variable.

  Args:
    shape: The shape of the tensor managed by this variable
    dtype: The underlying type of the tensor values.
    name: optional name to use for the variable op.
    container: An optional string. Defaults to "".
      If non-empty, this variable is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional string. Defaults to "".
      If non-empty, this variable is named in the given bucket
      with this shared_name. Otherwise, the node name is used instead.

  Returns:
    A variable tensor.
  '''
def init_variable(v, init, name: str = 'init'):
    '''Initializes variable with "init".

  This op does the following:
  if init is a Tensor, v = init
  if callable(init): v = init(VariableShape(v), v.dtype)

  Args:
    v: Variable to initialize
    init: Tensor to assign to v,
      Or an object convertible to Tensor e.g. nparray,
      Or an Initializer that generates a tensor given the shape and type of v.
      An "Initializer" is a callable that returns a tensor that "v" should be
      set to. It will be called as init(shape, dtype).
    name: Optional name for the op.

  Returns:
    The operation that initializes v.
  '''
def is_variable_initialized(ref, name: Incomplete | None = None):
    """Checks whether a tensor has been initialized.

  Outputs boolean scalar indicating whether the tensor has been initialized.

  Args:
    ref: A mutable `Tensor`.
      Should be from a `Variable` node. May be uninitialized.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """
def assign_sub(ref, value, use_locking: Incomplete | None = None, name: Incomplete | None = None):
    """Update `ref` by subtracting `value` from it.

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.
  Unlike `tf.math.subtract`, this op does not broadcast. `ref` and `value`
  must have the same shape.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`,
      `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. Should be
      from a `Variable` node.
    value: A `Tensor`. Must have the same shape and dtype as `ref`. The value to
      be subtracted to the variable.
    use_locking: An optional `bool`. Defaults to `False`. If True, the
      subtraction will be protected by a lock; otherwise the behavior is
      undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the new value after the variable has been updated.

  @compatibility(TF2)
  `tf.compat.v1.assign_sub` is mostly compatible with eager
  execution and `tf.function`.

  To switch to the native TF2 style, one could use method 'assign_sub' of
  `tf.Variable`:

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `ref`                 | `self`          | In `assign_sub()` method   |
  | `value`               | `value`         | In `assign_sub()` method   |
  | `use_locking`         | `use_locking`   | In `assign_sub()` method   |
  | `name`                | `name`          | In `assign_sub()` method   |
  | -                     | `read_value`    | Set to True to replicate   |
  :                       :                 : behavior (True is default) :


  #### Before & After Usage Example

  Before:

  >>> with tf.Graph().as_default():
  ...   with tf.compat.v1.Session() as sess:
  ...     a = tf.compat.v1.Variable(1, dtype=tf.int64)
  ...     sess.run(a.initializer)
  ...     update_op = tf.compat.v1.assign_sub(a, 1)
  ...     res_a = sess.run(update_op)
  ...     res_a
  0

  After:

  >>> b = tf.Variable(1, dtype=tf.int64)
  >>> res_b = b.assign_sub(1)
  >>> res_b.numpy()
  0

  @end_compatibility
  """
def assign_add(ref, value, use_locking: Incomplete | None = None, name: Incomplete | None = None):
    """Update `ref` by adding `value` to it.

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.
  Unlike `tf.math.add`, this op does not broadcast. `ref` and `value` must have
  the same shape.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`,
      `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. Should be
      from a `Variable` node.
    value: A `Tensor`. Must have the same shape and dtype as `ref`. The value to
      be added to the variable.
    use_locking: An optional `bool`. Defaults to `False`. If True, the addition
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the new value after the variable has been updated.

  @compatibility(TF2)
  `tf.compat.v1.assign_add` is mostly compatible with eager
  execution and `tf.function`.

  To switch to the native TF2 style, one could use method 'assign_add' of
  `tf.Variable`:

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `ref`                 | `self`          | In `assign_add()` method   |
  | `value`               | `value`         | In `assign_add()` method   |
  | `use_locking`         | `use_locking`   | In `assign_add()` method   |
  | `name`                | `name`          | In `assign_add()` method   |
  | -                     | `read_value`    | Set to True to replicate   |
  :                       :                 : behavior (True is default) :


  #### Before & After Usage Example

  Before:

  >>> with tf.Graph().as_default():
  ...   with tf.compat.v1.Session() as sess:
  ...     a = tf.compat.v1.Variable(0, dtype=tf.int64)
  ...     sess.run(a.initializer)
  ...     update_op = tf.compat.v1.assign_add(a, 1)
  ...     res_a = sess.run(update_op)
  ...     res_a
  1

  After:

  >>> b = tf.Variable(0, dtype=tf.int64)
  >>> res_b = b.assign_add(1)
  >>> res_b.numpy()
  1

  @end_compatibility
  """
def assign(ref, value, validate_shape: Incomplete | None = None, use_locking: Incomplete | None = None, name: Incomplete | None = None):
    """Update `ref` by assigning `value` to it.

  This operation outputs a Tensor that holds the new value of `ref` after
  the value has been assigned. This makes it easier to chain operations that
  need to use the reset value.

  Args:
    ref: A mutable `Tensor`. Should be from a `Variable` node. May be
      uninitialized.
    value: A `Tensor`. Must have the same shape and dtype as `ref`. The value to
      be assigned to the variable.
    validate_shape: An optional `bool`. Defaults to `True`. If true, the
      operation will validate that the shape of 'value' matches the shape of the
      Tensor being assigned to.  If false, 'ref' will take on the shape of
      'value'.
    use_locking: An optional `bool`. Defaults to `True`. If True, the assignment
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` that will hold the new value of `ref` after
      the assignment has completed.

  @compatibility(TF2)
  `tf.compat.v1.assign` is mostly compatible with eager
  execution and `tf.function`. However, argument 'validate_shape' will be
  ignored. To avoid shape validation, set 'shape' to tf.TensorShape(None) when
  constructing the variable:

  >>> import tensorflow as tf
  >>> a = tf.Variable([1], shape=tf.TensorShape(None))
  >>> tf.compat.v1.assign(a, [2,3])

  To switch to the native TF2 style, one could use method 'assign' of
  `tf.Variable`:

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `ref`                 | `self`          | In `assign()` method       |
  | `value`               | `value`         | In `assign()` method       |
  | `validate_shape`      | Not supported   | Specify `shape` in the     |
  :                       :                 : constructor to replicate   :
  :                       :                 : behavior                   :
  | `use_locking`         | `use_locking`   | In `assign()` method       |
  | `name`                | `name`          | In `assign()` method       |
  | -                     | `read_value`    | Set to True to replicate   |
  :                       :                 : behavior (True is default) :
  @end_compatibility


  #### Before & After Usage Example

  Before:

  >>> with tf.Graph().as_default():
  ...   with tf.compat.v1.Session() as sess:
  ...     a = tf.compat.v1.Variable(0, dtype=tf.int64)
  ...     sess.run(a.initializer)
  ...     update_op = tf.compat.v1.assign(a, 2)
  ...     res_a = sess.run(update_op)
  ...     res_a
  2

  After:

  >>> b = tf.Variable(0, dtype=tf.int64)
  >>> res_b = b.assign(2)
  >>> res_b.numpy()
  2
  """
def count_up_to(ref, limit, name: Incomplete | None = None):
    """Increments 'ref' until it reaches 'limit'.

  Args:
    ref: A Variable. Must be one of the following types: `int32`, `int64`.
      Should be from a scalar `Variable` node.
    limit: An `int`.
      If incrementing ref would bring it above limit, instead generates an
      'OutOfRange' error.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `ref`.
    A copy of the input before increment. If nothing else modifies the
    input, the values produced will all be distinct.
  """
def scatter_update(ref, indices, updates, use_locking: bool = True, name: Incomplete | None = None):
    '''Applies sparse updates to a variable reference.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] = updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] = updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] = updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  If values in `ref` is to be updated more than once, because there are
  duplicate entries in `indices`, the order at which the updates happen
  for each value is undefined.

  Requires `updates.shape = indices.shape + ref.shape[1:]`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/ScatterUpdate.png" alt>
  </div>

  Args:
    ref: A `Variable`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to store in `ref`.
    use_locking: An optional `bool`. Defaults to `True`.
      If True, the assignment will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the updated values after the update is done.
  '''
def scatter_nd_update(ref, indices, updates, use_locking: bool = True, name: Incomplete | None = None):
    """Applies sparse `updates` to individual values or slices in a Variable.

  `ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

  `indices` must be integer tensor, containing indices into `ref`.
  It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

  The innermost dimension of `indices` (with length `K`) corresponds to
  indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
  dimension of `ref`.

  `updates` is `Tensor` of rank `Q-1+P-K` with shape:

  ```
  [d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].
  ```

  For example, say we want to update 4 scattered elements to a rank-1 tensor to
  8 elements. In Python, that update would look like this:

  ```python
      ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
      indices = tf.constant([[4], [3], [1] ,[7]])
      updates = tf.constant([9, 10, 11, 12])
      update = tf.compat.v1.scatter_nd_update(ref, indices, updates)
      with tf.compat.v1.Session() as sess:
        print sess.run(update)
  ```

  The resulting update to ref would look like this:

      [1, 11, 3, 10, 9, 6, 7, 12]

  See `tf.scatter_nd` for more details about how to make updates to
  slices.

  Args:
    ref: A Variable.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into ref.
    updates: A `Tensor`. Must have the same type as `ref`.
      A Tensor. Must have the same type as ref. A tensor of updated
      values to add to ref.
    use_locking: An optional `bool`. Defaults to `True`.
      An optional bool. Defaults to True. If True, the assignment will
      be protected by a lock; otherwise the behavior is undefined,
      but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    The value of the variable after the update.
  """
def scatter_add(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    '''Adds sparse updates to the variable referenced by `resource`.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] += updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] += updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] += updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the updated value.
  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions add.

  Requires `updates.shape = indices.shape + ref.shape[1:]`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src=\'https://www.tensorflow.org/images/ScatterAdd.png\' alt>
  </div>

  Args:
    ref: A `Variable`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to store in `ref`.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the assignment will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the updated values after the update is done.
  '''
def scatter_nd_add(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    """Applies sparse addition to individual values or slices in a Variable.

  `ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

  `indices` must be integer tensor, containing indices into `ref`.
  It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

  The innermost dimension of `indices` (with length `K`) corresponds to
  indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
  dimension of `ref`.

  `updates` is `Tensor` of rank `Q-1+P-K` with shape:

  ```
  [d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]]
  ```

  For example, say we want to add 4 scattered elements to a rank-1 tensor to
  8 elements. In Python, that addition would look like this:

  ```python
  ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
  indices = tf.constant([[4], [3], [1], [7]])
  updates = tf.constant([9, 10, 11, 12])
  add = tf.compat.v1.scatter_nd_add(ref, indices, updates)
  with tf.compat.v1.Session() as sess:
    print sess.run(add)
  ```

  The resulting update to ref would look like this:

      [1, 13, 3, 14, 14, 6, 7, 20]

  See `tf.scatter_nd` for more details about how to make updates to
  slices.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
      `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
      `uint32`, `uint64`. A mutable Tensor. Should be from a Variable node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into ref.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to add to ref.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the assignment will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  """
def scatter_sub(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    '''Subtracts sparse updates to a variable reference.

  ```python
      # Scalar indices
      ref[indices, ...] -= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] -= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] -= updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their (negated) contributions add.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or
  `updates.shape = []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%"
       src="https://www.tensorflow.org/images/ScatterSub.png" alt>
  </div>

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
      `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
      `uint32`, `uint64`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to subtract from `ref`.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the subtraction will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  '''
def scatter_nd_sub(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    """Applies sparse subtraction to individual values or slices in a Variable.

  `ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

  `indices` must be integer tensor, containing indices into `ref`.
  It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

  The innermost dimension of `indices` (with length `K`) corresponds to
  indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
  dimension of `ref`.

  `updates` is `Tensor` of rank `Q-1+P-K` with shape:

  ```
  [d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]]
  ```

  For example, say we want to subtract 4 scattered elements from a rank-1 tensor
  with 8 elements. In Python, that update would look like this:

  ```python
  ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
  indices = tf.constant([[4], [3], [1] ,[7]])
  updates = tf.constant([9, 10, 11, 12])
  op = tf.compat.v1.scatter_nd_sub(ref, indices, updates)
  with tf.compat.v1.Session() as sess:
    print sess.run(op)
  ```

  The resulting update to ref would look like this:

      [1, -9, 3, -6, -6, 6, 7, -4]

  See `tf.scatter_nd` for more details about how to make updates to
  slices.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
      `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
      `uint32`, `uint64`. A mutable Tensor. Should be from a Variable node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into ref.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to add to ref.
    use_locking: An optional `bool`. Defaults to `False`.
      An optional bool. Defaults to True. If True, the assignment will
      be protected by a lock; otherwise the behavior is undefined,
      but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  """
def scatter_mul(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    """Multiplies sparse updates into a variable reference.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] *= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] *= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] *= updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions multiply.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape =
  []`.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
      `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
      `uint32`, `uint64`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`. A
      tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`. A tensor of updated
      values to multiply to `ref`.
    use_locking: An optional `bool`. Defaults to `False`. If True, the operation
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  """
def scatter_div(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    """Divides a variable reference by sparse updates.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] /= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] /= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] /= updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions divide.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape =
  []`.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`,
      `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
      `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
      `uint32`, `uint64`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`. A
      tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`. A tensor of values
      that `ref` is divided by.
    use_locking: An optional `bool`. Defaults to `False`. If True, the operation
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  """
def scatter_max(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    '''Reduces sparse updates into a variable reference using the `max` operation.

  This operation computes

      # Scalar indices
      ref[indices, ...] = max(ref[indices, ...], updates[...])

      # Vector indices (for each i)
      ref[indices[i], ...] = max(ref[indices[i], ...], updates[i, ...])

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] = max(ref[indices[i, ..., j], ...],
      updates[i, ..., j, ...])

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions combine.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape =
  []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/ScatterAdd.png"
  alt>
  </div>

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `half`,
      `bfloat16`, `float32`, `float64`, `int32`, `int64`. Should be from a
      `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`. A
      tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`. A tensor of updated
      values to reduce into `ref`.
    use_locking: An optional `bool`. Defaults to `False`. If True, the update
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  '''
def scatter_min(ref, indices, updates, use_locking: bool = False, name: Incomplete | None = None):
    '''Reduces sparse updates into a variable reference using the `min` operation.

  This operation computes

      # Scalar indices
      ref[indices, ...] = min(ref[indices, ...], updates[...])

      # Vector indices (for each i)
      ref[indices[i], ...] = min(ref[indices[i], ...], updates[i, ...])

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] = min(ref[indices[i, ..., j], ...],
      updates[i, ..., j, ...])

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions combine.

  Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape =
  []`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/ScatterAdd.png"
  alt>
  </div>

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `half`,
      `bfloat16`, `float32`, `float64`, `int32`, `int64`. Should be from a
      `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`. A
      tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`. A tensor of updated
      values to reduce into `ref`.
    use_locking: An optional `bool`. Defaults to `False`. If True, the update
      will be protected by a lock; otherwise the behavior is undefined, but may
      exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
  '''
def batch_scatter_update(ref, indices, updates, use_locking: bool = True, name: Incomplete | None = None):
    """Generalization of `tf.compat.v1.scatter_update` to axis different than 0.

  Analogous to `batch_gather`. This assumes that `ref`, `indices` and `updates`
  have a series of leading dimensions that are the same for all of them, and the
  updates are performed on the last dimension of indices. In other words, the
  dimensions should be the following:

  `num_prefix_dims = indices.ndims - 1`
  `batch_dim = num_prefix_dims + 1`
  `updates.shape = indices.shape + var.shape[batch_dim:]`

  where

  `updates.shape[:num_prefix_dims]`
  `== indices.shape[:num_prefix_dims]`
  `== var.shape[:num_prefix_dims]`

  And the operation performed can be expressed as:

  `var[i_1, ..., i_n, indices[i_1, ..., i_n, j]] = updates[i_1, ..., i_n, j]`

  When indices is a 1D tensor, this operation is equivalent to
  `tf.compat.v1.scatter_update`.

  To avoid this operation there would be 2 alternatives:
  1) Reshaping the variable by merging the first `ndims` dimensions. However,
     this is not possible because `tf.reshape` returns a Tensor, which we
     cannot use `tf.compat.v1.scatter_update` on.
  2) Looping over the first `ndims` of the variable and using
     `tf.compat.v1.scatter_update` on the subtensors that result of slicing the
     first
     dimension. This is a valid option for `ndims = 1`, but less efficient than
     this implementation.

  See also `tf.compat.v1.scatter_update` and `tf.compat.v1.scatter_nd_update`.

  Args:
    ref: `Variable` to scatter onto.
    indices: Tensor containing indices as described above.
    updates: Tensor of updates to apply to `ref`.
    use_locking: Boolean indicating whether to lock the writing operation.
    name: Optional scope name string.

  Returns:
    Ref to `variable` after it has been modified.

  Raises:
    ValueError: If the initial `ndims` of `ref`, `indices`, and `updates` are
        not the same.
  """
