from tensorflow.python.ops.gen_resource_variable_ops import *
from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, variable_pb2 as variable_pb2
from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.checkpoint import tensor_callable as tensor_callable
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.eager import context as context, tape as tape
from tensorflow.python.framework import composite_tensor as composite_tensor, composite_tensor_gradient as composite_tensor_gradient, constant_op as constant_op, cpp_shape_inference_pb2 as cpp_shape_inference_pb2, dtypes as dtypes, errors as errors, indexed_slices as indexed_slices, meta_graph as meta_graph, ops as ops, tensor_conversion_registry as tensor_conversion_registry, tensor_shape as tensor_shape, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, gen_resource_variable_ops as gen_resource_variable_ops, gen_state_ops as gen_state_ops, handle_data_util as handle_data_util, math_ops as math_ops, state_ops as state_ops, variables as variables
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.types import core as core
from tensorflow.python.util import compat as compat
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export

get_resource_handle_data: Incomplete

def get_eager_safe_handle_data(handle):
    """Get the data handle from the Tensor `handle`."""
def eager_safe_variable_handle(initial_value, shape, shared_name, name, graph_mode):
    """Creates a variable handle with information to do shape inference.

  The dtype is read from `initial_value` and stored in the returned
  resource tensor's handle data.

  If `initial_value.dtype == tf.variant`, we additionally extract the handle
  data (if any) from `initial_value` and append it to the `handle_data`.
  In this case, the returned tensor's handle data is in the form

  ```
  is_set: true
  shape_and_type {
    shape {
      // initial_value.shape
    }
    dtype: DT_VARIANT
  }
  shape_and_type {
    // handle_data(initial_value).shape_and_type[0]
  }
  shape_and_type {
    // handle_data(initial_value).shape_and_type[1]
  }
  ...
  ```

  Ops that read from this tensor, such as `ReadVariableOp` and
  `AssignVariableOp`, know that `handle_data(handle).shape_and_type[1:]`
  correspond to the handle data of the variant(s) stored in the Variable.

  Args:
    initial_value: A `Tensor`.
    shape: The shape of the handle data. Can be `TensorShape(None)` (i.e.
      unknown shape).
    shared_name: A string.
    name: A string.
    graph_mode: A python bool.

  Returns:
    The handle, a `Tensor` of type `resource`.
  """

class EagerResourceDeleter:
    """An object which cleans up a resource handle.

  An alternative to defining a __del__ method on an object. The intended use is
  that ResourceVariables or other objects with resource handles will maintain a
  single reference to this object. When the parent object is collected, this
  object will be too. Even if the parent object is part of a reference cycle,
  the cycle will be collectable.
  """
    def __init__(self, handle, handle_device) -> None: ...
    def __del__(self) -> None: ...

def shape_safe_assign_variable_handle(handle, shape, value, name: Incomplete | None = None):
    """Helper that checks shape compatibility and assigns variable."""
def variable_accessed(variable) -> None:
    """Records that `variable` was accessed for the tape and FuncGraph."""

class BaseResourceVariable(variables.VariableV1, core.Tensor):
    """A python variable from an existing handle."""
    def __init__(self, trainable: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, handle: Incomplete | None = None, constraint: Incomplete | None = None, synchronization: Incomplete | None = None, aggregation: Incomplete | None = None, distribute_strategy: Incomplete | None = None, name: Incomplete | None = None, unique_id: Incomplete | None = None, handle_name: Incomplete | None = None, graph_element: Incomplete | None = None, initial_value: Incomplete | None = None, initializer_op: Incomplete | None = None, is_initialized_op: Incomplete | None = None, cached_value: Incomplete | None = None, save_slice_info: Incomplete | None = None, caching_device: Incomplete | None = None, in_graph_mode: Incomplete | None = None, validate_shape: bool = True, **unused_kwargs) -> None:
        """Creates a variable from a handle.

    Args:
      trainable: If `True`, GradientTapes automatically watch uses of this
        Variable.
      shape: The variable's shape. This shape can be set to tf.TensorShape(None)
        in order to assign values of different shapes to this variable.
        Otherwise (i.e. if the shape is fully determined), it will trigger run
        time checks to ensure that each assignment is of the same shape.
      dtype: The variable's dtype.
      handle: The variable's handle
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses when to
        synchronize.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      distribute_strategy: The distribution strategy this variable was created
        under.
      name: The name for this variable.
      unique_id: Internal. Unique ID for this variable's handle.
      handle_name: The name for the variable's handle.
      graph_element: Optional, required only in session.run-mode. Pre-created
        tensor which reads this variable's value.
      initial_value: Optional. Variable's initial value.
      initializer_op: Operation which assigns the variable's initial value.
      is_initialized_op: Pre-created operation to check whether this variable is
        initialized.
      cached_value: Pre-created operation to read this variable in a specific
        device.
      save_slice_info: Metadata for variable partitioning.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      in_graph_mode: whether we are executing in TF1 graph mode. If None, will
        detect within the function. This is to avoid repeated init_scope()
        conetxt entrances which can add up.
      validate_shape: If `False`, allows the variable to be initialized with a
        value of unknown shape. If `True`, the default, the shape of
        `initial_value` must be known.
    """
    def __tf_tracing_type__(self, signature_context): ...
    def __array__(self, dtype: Incomplete | None = None):
        """Allows direct conversion to a numpy array.

    >>> np.array(tf.Variable([1.0]))
    array([1.], dtype=float32)

    Returns:
      The variable value as a numpy array.
    """
    def __nonzero__(self): ...
    def __bool__(self) -> bool: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    @property
    def dtype(self):
        """The dtype of this variable."""
    @property
    def device(self):
        """The device this variable is on."""
    @property
    def graph(self):
        """The `Graph` of this variable."""
    @property
    def name(self):
        """The name of the handle for this variable."""
    @property
    def shape(self):
        """The shape of this variable."""
    def set_shape(self, shape) -> None: ...
    @property
    def create(self):
        """The op responsible for initializing this variable."""
    @property
    def handle(self):
        """The handle by which this variable can be accessed."""
    def value(self):
        """A cached operation which reads the value of this variable."""
    @property
    def initializer(self):
        """The op responsible for initializing this variable."""
    @property
    def initial_value(self):
        """Returns the Tensor used as the initial value for the variable."""
    @property
    def constraint(self):
        """Returns the constraint function associated with this variable.

    Returns:
      The constraint function that was passed to the variable constructor.
      Can be `None` if no constraint was passed.
    """
    @property
    def op(self):
        """The op for this variable."""
    @property
    def trainable(self): ...
    @property
    def synchronization(self): ...
    @property
    def aggregation(self): ...
    def eval(self, session: Incomplete | None = None):
        """Evaluates and returns the value of this variable."""
    def numpy(self): ...
    def count_up_to(self, limit):
        """Increments this variable until it reaches `limit`.

    When that Op is run it tries to increment the variable by `1`. If
    incrementing the variable would bring it above `limit` then the Op raises
    the exception `OutOfRangeError`.

    If no error is raised, the Op outputs the value of the variable before
    the increment.

    This is essentially a shortcut for `count_up_to(self, limit)`.

    Args:
      limit: value at which incrementing the variable raises an error.

    Returns:
      A `Tensor` that will hold the variable value before the increment. If no
      other Op modifies this variable, the values produced will all be
      distinct.
    """
    def read_value(self):
        """Constructs an op which reads the value of this variable.

    Should be used when there are multiple reads, or when it is desirable to
    read the value only after some condition is true.

    Returns:
      The value of the variable.
    """
    def read_value_no_copy(self):
        """Constructs an op which reads the value of this variable without copy.

    The variable is read without making a copy even when it has been sparsely
    accessed. Variables in copy-on-read mode will be converted to copy-on-write
    mode.

    Returns:
      The value of the variable.
    """
    def sparse_read(self, indices, name: Incomplete | None = None):
        """Reads the value of this variable sparsely, using `gather`."""
    def gather_nd(self, indices, name: Incomplete | None = None):
        """Reads the value of this variable sparsely, using `gather_nd`."""
    def to_proto(self, export_scope: Incomplete | None = None):
        """Converts a `ResourceVariable` to a `VariableDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Raises:
      RuntimeError: If run in EAGER mode.

    Returns:
      A `VariableDef` protocol buffer, or `None` if the `Variable` is not
      in the specified name scope.
    """
    @staticmethod
    def from_proto(variable_def, import_scope: Incomplete | None = None): ...
    __array_priority__: int
    def is_initialized(self, name: Incomplete | None = None):
        """Checks whether a resource variable has been initialized.

    Outputs boolean scalar indicating whether the tensor has been initialized.

    Args:
      name: A name for the operation (optional).

    Returns:
      A `Tensor` of type `bool`.
    """
    def assign_sub(self, delta, use_locking: Incomplete | None = None, name: Incomplete | None = None, read_value: bool = True):
        """Subtracts a value from this variable.

    Args:
      delta: A `Tensor`. The value to subtract from this variable.
      use_locking: If `True`, use locking during the operation.
      name: The name to use for the operation.
      read_value: A `bool`. Whether to read and return the new value of the
        variable or not.

    Returns:
      If `read_value` is `True`, this method will return the new value of the
      variable after the assignment has completed. Otherwise, when in graph mode
      it will return the `Operation` that does the assignment, and when in eager
      mode it will return `None`.
    """
    def assign_add(self, delta, use_locking: Incomplete | None = None, name: Incomplete | None = None, read_value: bool = True):
        """Adds a value to this variable.

    Args:
      delta: A `Tensor`. The value to add to this variable.
      use_locking: If `True`, use locking during the operation.
      name: The name to use for the operation.
      read_value: A `bool`. Whether to read and return the new value of the
        variable or not.

    Returns:
      If `read_value` is `True`, this method will return the new value of the
      variable after the assignment has completed. Otherwise, when in graph mode
      it will return the `Operation` that does the assignment, and when in eager
      mode it will return `None`.
    """
    def assign(self, value, use_locking: Incomplete | None = None, name: Incomplete | None = None, read_value: bool = True):
        """Assigns a new value to this variable.

    Args:
      value: A `Tensor`. The new value for this variable.
      use_locking: If `True`, use locking during the assignment.
      name: The name to use for the assignment.
      read_value: A `bool`. Whether to read and return the new value of the
        variable or not.

    Returns:
      If `read_value` is `True`, this method will return the new value of the
      variable after the assignment has completed. Otherwise, when in graph mode
      it will return the `Operation` that does the assignment, and when in eager
      mode it will return `None`.
    """
    def __reduce__(self): ...
    def scatter_sub(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Subtracts `tf.IndexedSlices` from this variable.

    Args:
      sparse_delta: `tf.IndexedSlices` to be subtracted from this variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def scatter_add(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Adds `tf.IndexedSlices` to this variable.

    Args:
      sparse_delta: `tf.IndexedSlices` to be added to this variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def scatter_max(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Updates this variable with the max of `tf.IndexedSlices` and itself.

    Args:
      sparse_delta: `tf.IndexedSlices` to use as an argument of max with this
        variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def scatter_min(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Updates this variable with the min of `tf.IndexedSlices` and itself.

    Args:
      sparse_delta: `tf.IndexedSlices` to use as an argument of min with this
        variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def scatter_mul(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Multiply this variable by `tf.IndexedSlices`.

    Args:
      sparse_delta: `tf.IndexedSlices` to multiply this variable by.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def scatter_div(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Divide this variable by `tf.IndexedSlices`.

    Args:
      sparse_delta: `tf.IndexedSlices` to divide this variable by.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def scatter_update(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Assigns `tf.IndexedSlices` to this variable.

    Args:
      sparse_delta: `tf.IndexedSlices` to be assigned to this variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def batch_scatter_update(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Assigns `tf.IndexedSlices` to this variable batch-wise.

    Analogous to `batch_gather`. This assumes that this variable and the
    sparse_delta IndexedSlices have a series of leading dimensions that are the
    same for all of them, and the updates are performed on the last dimension of
    indices. In other words, the dimensions should be the following:

    `num_prefix_dims = sparse_delta.indices.ndims - 1`
    `batch_dim = num_prefix_dims + 1`
    `sparse_delta.updates.shape = sparse_delta.indices.shape + var.shape[
         batch_dim:]`

    where

    `sparse_delta.updates.shape[:num_prefix_dims]`
    `== sparse_delta.indices.shape[:num_prefix_dims]`
    `== var.shape[:num_prefix_dims]`

    And the operation performed can be expressed as:

    `var[i_1, ..., i_n,
         sparse_delta.indices[i_1, ..., i_n, j]] = sparse_delta.updates[
            i_1, ..., i_n, j]`

    When sparse_delta.indices is a 1D tensor, this operation is equivalent to
    `scatter_update`.

    To avoid this operation one can looping over the first `ndims` of the
    variable and using `scatter_update` on the subtensors that result of slicing
    the first dimension. This is a valid option for `ndims = 1`, but less
    efficient than this implementation.

    Args:
      sparse_delta: `tf.IndexedSlices` to be assigned to this variable.
      use_locking: If `True`, use locking during the operation.
      name: the name of the operation.

    Returns:
      The updated variable.

    Raises:
      TypeError: if `sparse_delta` is not an `IndexedSlices`.
    """
    def scatter_nd_sub(self, indices, updates, name: Incomplete | None = None):
        """Applies sparse subtraction to individual values or slices in a Variable.

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

    For example, say we want to add 4 scattered elements to a rank-1 tensor to
    8 elements. In Python, that update would look like this:

    ```python
        ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        op = ref.scatter_nd_sub(indices, updates)
        with tf.compat.v1.Session() as sess:
          print sess.run(op)
    ```

    The resulting update to ref would look like this:

        [1, -9, 3, -6, -6, 6, 7, -4]

    See `tf.scatter_nd` for more details about how to make updates to
    slices.

    Args:
      indices: The indices to be used in the operation.
      updates: The values to be used in the operation.
      name: the name of the operation.

    Returns:
      The updated variable.
    """
    def scatter_nd_add(self, indices, updates, name: Incomplete | None = None):
        """Applies sparse addition to individual values or slices in a Variable.

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

    For example, say we want to add 4 scattered elements to a rank-1 tensor to
    8 elements. In Python, that update would look like this:

    ```python
        ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        add = ref.scatter_nd_add(indices, updates)
        with tf.compat.v1.Session() as sess:
          print sess.run(add)
    ```

    The resulting update to ref would look like this:

        [1, 13, 3, 14, 14, 6, 7, 20]

    See `tf.scatter_nd` for more details about how to make updates to
    slices.

    Args:
      indices: The indices to be used in the operation.
      updates: The values to be used in the operation.
      name: the name of the operation.

    Returns:
      The updated variable.
    """
    def scatter_nd_update(self, indices, updates, name: Incomplete | None = None):
        """Applies sparse assignment to individual values or slices in a Variable.

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

    For example, say we want to add 4 scattered elements to a rank-1 tensor to
    8 elements. In Python, that update would look like this:

    ```python
        ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
        indices = tf.constant([[4], [3], [1] ,[7]])
        updates = tf.constant([9, 10, 11, 12])
        op = ref.scatter_nd_update(indices, updates)
        with tf.compat.v1.Session() as sess:
          print sess.run(op)
    ```

    The resulting update to ref would look like this:

        [1, 11, 3, 10, 9, 6, 7, 12]

    See `tf.scatter_nd` for more details about how to make updates to
    slices.

    Args:
      indices: The indices to be used in the operation.
      updates: The values to be used in the operation.
      name: the name of the operation.

    Returns:
      The updated variable.
    """
    def scatter_nd_max(self, indices, updates, name: Incomplete | None = None):
        """Updates this variable with the max of `tf.IndexedSlices` and itself.

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

    See `tf.scatter_nd` for more details about how to make updates to
    slices.

    Args:
      indices: The indices to be used in the operation.
      updates: The values to be used in the operation.
      name: the name of the operation.

    Returns:
      The updated variable.
    """
    def scatter_nd_min(self, indices, updates, name: Incomplete | None = None):
        """Updates this variable with the min of `tf.IndexedSlices` and itself.

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

    See `tf.scatter_nd` for more details about how to make updates to
    slices.

    Args:
      indices: The indices to be used in the operation.
      updates: The values to be used in the operation.
      name: the name of the operation.

    Returns:
      The updated variable.
    """
    def __complex__(self) -> complex: ...
    def __int__(self) -> int: ...
    def __long__(self): ...
    def __float__(self) -> float: ...
    def __iadd__(self, unused_other) -> None: ...
    def __isub__(self, unused_other) -> None: ...
    def __imul__(self, unused_other) -> None: ...
    def __idiv__(self, unused_other) -> None: ...
    def __itruediv__(self, unused_other) -> None: ...
    def __irealdiv__(self, unused_other) -> None: ...
    def __ipow__(self, unused_other) -> None: ...

class ResourceVariableGradient(composite_tensor_gradient.CompositeTensorGradient):
    """CompositeTensorGradient protocol for ResourceVariable."""
    def get_gradient_components(self, value):
        """Returns the components of `value` that should be included in gradients.

    For a ResourceVariable, its gradient component is its handle tensor.
    For now, we return the ResourceVariable because the gradient infrastructure
    has special logics to handle ResourceVariables. We should remove those
    special logics and return the handle tensor.

    Args:
      value: A `ResourceVariable`.

    Returns:
      `value` itself.
    """
    def replace_gradient_components(self, value, component_grads):
        """Replaces the gradient components in `value` with `component_grads`.

    The gradient of a ResourceVariable is either None or a Tensor. So we don't
    need `value`'s TypeSpec or non-gradient components in this method.

    Args:
      value: A `ResourceVariable` with its gradient components compatible with
        `component_grads`.
      component_grads: A `Tensor` or None as the gradient result.

    Returns:
      The `component_grads`, which is either a `Tensor` or None.
    """

class ResourceVariable(BaseResourceVariable, composite_tensor.CompositeTensor):
    """Variable based on resource handles.

  See the [Variables How To](https://tensorflow.org/guide/variables)
  for a high level overview.

  A `ResourceVariable` allows you to maintain state across subsequent calls to
  session.run.

  The `ResourceVariable` constructor requires an initial value for the variable,
  which can be a `Tensor` of any type and shape. The initial value defines the
  type and shape of the variable. After construction, the type and shape of
  the variable are fixed. The value can be changed using one of the assign
  methods.

  Just like any `Tensor`, variables created with
  `tf.Variable(use_resource=True)` can be used as inputs for other Ops in the
  graph. Additionally, all the operators overloaded for the `Tensor` class are
  carried over to variables, so you can also add nodes to the graph by just
  doing arithmetic on variables.

  Unlike ref-based variable, a ResourceVariable has well-defined semantics. Each
  usage of a ResourceVariable in a TensorFlow graph adds a read_value operation
  to the graph. The Tensors returned by a read_value operation are guaranteed to
  see all modifications to the value of the variable which happen in any
  operation on which the read_value depends on (either directly, indirectly, or
  via a control dependency) and guaranteed to not see any modification to the
  value of the variable from operations that depend on the read_value operation.
  Updates from operations that have no dependency relationship to the read_value
  operation might or might not be visible to read_value.

  For example, if there is more than one assignment to a ResourceVariable in
  a single session.run call there is a well-defined value for each operation
  which uses the variable's value if the assignments and the read are connected
  by edges in the graph. Consider the following example, in which two writes
  can cause tf.Variable and tf.ResourceVariable to behave differently:

  ```python
  a = tf.Variable(1.0, use_resource=True)
  a.initializer.run()

  assign = a.assign(2.0)
  with tf.control_dependencies([assign]):
    b = a.read_value()
  with tf.control_dependencies([b]):
    other_assign = a.assign(3.0)
  with tf.control_dependencies([other_assign]):
    # Will print 2.0 because the value was read before other_assign ran. If
    # `a` was a tf.Variable instead, 2.0 or 3.0 could be printed.
    tf.compat.v1.Print(b, [b]).eval()
  ```
  """
    def __init__(self, initial_value: Incomplete | None = None, trainable: Incomplete | None = None, collections: Incomplete | None = None, validate_shape: bool = True, caching_device: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None, variable_def: Incomplete | None = None, import_scope: Incomplete | None = None, constraint: Incomplete | None = None, distribute_strategy: Incomplete | None = None, synchronization: Incomplete | None = None, aggregation: Incomplete | None = None, shape: Incomplete | None = None, handle: Incomplete | None = None, experimental_enable_variable_lifting: Incomplete | None = None) -> None:
        '''Creates a variable.

    Args:
      initial_value: A `Tensor`, or Python object convertible to a `Tensor`,
        which is the initial value for the Variable. Can also be a callable with
        no argument that returns the initial value when called. (Note that
        initializer functions from init_ops.py must first be bound to a shape
        before being used here.)
      trainable: If `True`, the default, also adds the variable to the graph
        collection `GraphKeys.TRAINABLE_VARIABLES`. This collection is used as
        the default list of variables to use by the `Optimizer` classes.
        Defaults to `True`, unless `synchronization` is set to `ON_READ`, in
        which case it defaults to `False`.
      collections: List of graph collections keys. The new variable is added to
        these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
      validate_shape: If `False`, allows the variable to be initialized with a
        value of unknown shape. If `True`, the default, the shape of
        `initial_value` must be known.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable\'s
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      name: Optional name for the variable. Defaults to `\'Variable\'` and gets
        uniquified automatically.
      dtype: If set, initial_value will be converted to the given type. If None,
        either the datatype will be kept (if initial_value is a Tensor) or
        float32 will be used (if it is a Python object convertible to a Tensor).
      variable_def: `VariableDef` protocol buffer. If not None, recreates the
        `ResourceVariable` object with its contents. `variable_def` and other
        arguments (except for import_scope) are mutually exclusive.
      import_scope: Optional `string`. Name scope to add to the
        ResourceVariable. Only used when `variable_def` is provided.
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
      distribute_strategy: The tf.distribute.Strategy this variable is being
        created inside of.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses when to
        synchronize.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      shape: (optional) The shape of this variable. If None, the shape of
        `initial_value` will be used. When setting this argument to
        `tf.TensorShape(None)` (representing an unspecified shape), the variable
        can be assigned with values of different shapes.
      handle: (optional) The handle of a `tf.Variable`. If provided, only
        `trainable`, `shape`, `dtype`, and `handle` will be used to construct
        this `tf.Variable`.
      experimental_enable_variable_lifting: Whether to lift the variable out if
        it\'s in a `tf.function`. Default is `True`. When this argument
        is `True`, variable creation will follow the behavior and
        restrictions described
        [here](https://www.tensorflow.org/guide/function#creating_tfvariables).
        If this argument is `False`, that description doesn\'t apply,
        and you can freely create and use the variable in the
        `tf.function`, as if it\'s a "mutable `tf.Tensor`". You can\'t
        return the variable though.

    Raises:
      ValueError: If the initial value is not specified, or does not have a
        shape and `validate_shape` is `True`.

    @compatibility(eager)
    When Eager Execution is enabled, the default for the `collections` argument
    is `None`, which signifies that this `Variable` will not be added to any
    collections.
    @end_compatibility
    '''
    __composite_gradient__: Incomplete

class UninitializedVariable(BaseResourceVariable):
    """A variable with no initializer."""
    def __init__(self, trainable: Incomplete | None = None, caching_device: Incomplete | None = None, name: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, constraint: Incomplete | None = None, synchronization: Incomplete | None = None, aggregation: Incomplete | None = None, extra_handle_data: Incomplete | None = None, distribute_strategy: Incomplete | None = None, **unused_kwargs) -> None:
        """Creates the variable handle.

    Args:
      trainable: If `True`, GradientTapes automatically watch uses of this
        Variable.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      name: Optional name for the variable. Defaults to `'Variable'` and gets
        uniquified automatically.
      shape: The variable's shape.
      dtype: The variable's dtype.
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses when to
        synchronize.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      extra_handle_data: Optional, another resource handle or Tensor with handle
        data to merge with `shape` and `dtype`.
      distribute_strategy: The tf.distribute.Strategy this variable is being
        created inside of.
    """

class _UnreadVariable(BaseResourceVariable):
    """Represents a future for a read of a variable.

  Pretends to be the tensor if anyone looks.
  """
    def __init__(self, handle, dtype, shape, in_graph_mode, parent_op, unique_id) -> None: ...
    @property
    def name(self): ...
    def value(self): ...
    def read_value(self): ...
    def assign_sub(self, delta, use_locking: Incomplete | None = None, name: Incomplete | None = None, read_value: bool = True): ...
    def assign_add(self, delta, use_locking: Incomplete | None = None, name: Incomplete | None = None, read_value: bool = True): ...
    def assign(self, value, use_locking: Incomplete | None = None, name: Incomplete | None = None, read_value: bool = True): ...
    def scatter_sub(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def scatter_add(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def scatter_max(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def scatter_min(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def scatter_mul(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def scatter_div(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def scatter_update(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def batch_scatter_update(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None): ...
    def scatter_nd_sub(self, indices, updates, name: Incomplete | None = None): ...
    def scatter_nd_add(self, indices, updates, name: Incomplete | None = None): ...
    def scatter_nd_update(self, indices, updates, name: Incomplete | None = None): ...
    def scatter_nd_max(self, indices, updates, name: Incomplete | None = None): ...
    def scatter_nd_min(self, indices, updates, name: Incomplete | None = None): ...
    @property
    def op(self):
        """The op for this variable."""

def variable_shape(handle, out_type=...): ...
def is_resource_variable(var):
    '''"Returns True if `var` is to be considered a ResourceVariable.'''
def copy_to_graph_uninitialized(var):
    """Copies an existing variable to a new graph, with no initializer."""

class StructurePattern: ...

class PLeaf(StructurePattern):
    """Represents a singleton leaf StructurePattern."""
    def __new__(cls): ...

class PList(StructurePattern):
    """Represents a list of StructurePatterns."""
    components: Incomplete
    def __init__(self, *components) -> None: ...
    def __eq__(self, other): ...

class VariableSpec(tensor_spec.DenseSpec):
    """Describes a tf.Variable.

  A `VariableSpec` provides metadata describing the `tf.Variable` objects
  accepted or returned by TensorFlow 2.x APIs.
  """
    value_type: Incomplete
    trainable: Incomplete
    alias_id: Incomplete
    def __init__(self, shape, dtype=..., trainable: bool = True, alias_id: Incomplete | None = None) -> None: ...
    def is_compatible_with(self, spec_or_value):
        """Returns True if `spec_or_value` is compatible with this `VariableSpec`.

    `spec_or_value` is considered to be compatible with this `VariableSpec` if

    * `spec_or_value` is a `Variable` or `VariableSpec`,
    * their shapes are compatible,
    * their dtypes are the same,
    * they are both trainable or not trainable.
    * they share the same alias_id if `spec_or_value` is a `VariableSpec`.

    Example:

    >>> v = tf.Variable([1., 2., 3.])
    >>> spec = VariableSpec([None])
    >>> spec.is_compatible_with(v)
    True
    >>> v = tf.Variable(1)
    >>> spec.is_compatible_with(v)
    False

    Args:
      spec_or_value: A VariableSpec or Variable to compare against.

    Returns:
      True if `spec_or_value` is compatible with this `VariableSpec`.
    """
    @classmethod
    def from_value(cls, value):
        """Creates a `VariableSpec` from the given `Variable`.

    `value`'s shape, dtype, and trainable attributes will be used to create
    the new `VariableSpec`.

    Example:

    >>> v = tf.Variable([1., 2., 3.])
    >>> VariableSpec.from_value(v)
    VariableSpec(shape=(3,), dtype=tf.float32, trainable=True, alias_id=None)

    Args:
      value: A Variable.

    Returns:
      A `VariableSpec` created from `value`.
    """
    def is_subtype_of(self, other): ...
    def most_specific_common_supertype(self, others): ...
    def placeholder_value(self, placeholder_context): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def write_object_proto_for_resource_variable(resource_variable, proto, options, enforce_naming: bool = True) -> None:
    """Writes additional information of the variable into the SavedObject proto.

  This allows users to define a `hook` to provide extra information of the
  variable to the SavedObject.

  For example, DistributedVariable class would fill in components in the
  distributed context.

  Args:
    resource_variable: A `ResourceVariable` or `DistributedValue` that has the
      information to be saved into the proto.
    proto: `SavedObject` proto to update.
    options: A `SaveOption` instance that configures save behavior.
    enforce_naming: A bool determining whether to check that names end in the
      expected string ':0'
  """
