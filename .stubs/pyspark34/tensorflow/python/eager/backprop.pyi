from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import backprop_util as backprop_util, context as context, execute as execute, imperative_grad as imperative_grad, tape as tape
from tensorflow.python.framework import composite_tensor as composite_tensor, composite_tensor_gradient as composite_tensor_gradient, constant_op as constant_op, dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_util as control_flow_util, default_gradient as default_gradient, gen_array_ops as gen_array_ops, gen_math_ops as gen_math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import nest as nest, tf_contextlib as tf_contextlib, tf_inspect as tf_inspect, variable_utils as variable_utils
from tensorflow.python.util.tf_export import tf_export as tf_export

def op_attr_type(op_type, attr_name): ...
def make_attr(attr_type, value): ...

class _MockOp:
    """Pretends to be a tf.Operation for the gradient functions."""
    attrs: Incomplete
    inputs: Incomplete
    outputs: Incomplete
    type: Incomplete
    skip_input_indices: Incomplete
    def __init__(self, attrs, inputs, outputs, typ, skip_input_indices) -> None: ...
    def get_attr(self, attr): ...

def record_gradient(op_name, inputs, attrs, outputs) -> None:
    """Explicitly record the gradient for a given op.

  Args:
    op_name: The op name as listed in the `OpDef` for the op.
    inputs: A list of tensor inputs to the op.
    attrs: The op attributes as a flattened list of alternating attribute names
      and attribute values.
    outputs: A list of tensor outputs from the op.
  """
def implicit_val_and_grad(f):
    """Returns a function which differentiates f with respect to variables.

  The wrapped function returns the value and the gradient of f when called with
  the same arguments. The gradient is with respect to all trainable TFE
  variables accessed by `f`.

  This function is useful when the exact set of variables to differentiate with
  is not known ahead of time.

  Example:

  ```python
  dense_layer = tf.compat.v1.layers.Dense(1)
  def loss(x, y):
    return tf.reduce_sum(tf.square(dense_layer(x) - y))

  # Obtain the gradient function.
  val_grad_fn = tfe.implicit_value_and_gradients(loss)

  # Invoke the gradient function with concrete values of x and y.
  x = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
  y = tf.constant([[10.0], [20.0]])
  value, grads_and_vars = val_grad_fn(x, y)
  print('Value of loss: %s' % value)

  # Apply the gradients to Variables.
  optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.1)
  optimizer.apply_gradients(grads_and_vars)
  ```

  Args:
    f: function to be differentiated. If `f` returns a scalar, this scalar will
      be differentiated. If `f` returns a tensor or list of tensors, by default
      a scalar will be computed by adding all their values to produce a single
      scalar.

  Returns:
    A function which, when called, returns a tuple pair.
    Its first element is the value to which the function evaluates.
    Its second element is list of (gradient, variable) pairs.

  Raises:
    ValueError: if `f` returns None.
  """
def implicit_grad(f):
    """Returns a function which differentiates f with respect to variables.

  The wrapped function returns the gradient of f when called with the same
  arguments. The gradient is with respect to all trainable TFE variables
  accessed by `f`.

  This function is useful when the exact set of variables to differentiate with
  is not known ahead of time.

  Example:

  ```python
  dense_layer = tf.compat.v1.layers.Dense(1)
  def loss(x, y):
    return tf.reduce_sum(tf.square(dense_layer(x) - y))

  # Obtain the gradient function.
  grad_fn = tfe.implicit_gradients(loss)

  # Invoke the gradient function with concrete values of x and y.
  x = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
  y = tf.constant([[10.0], [20.0]])
  grads_and_vars = grad_fn(x, y)

  # Apply the gradients to Variables.
  optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.1)
  optimizer.apply_gradients(grads_and_vars)
  ```

  Args:
    f: function to be differentiated. If `f` returns a scalar, this scalar will
      be differentiated. If `f` returns a tensor or list of tensors, by default
      a scalar will be computed by adding all their values to produce a single
      scalar.

  Returns:
    A function which, when called, returns a list of (gradient, variable) pairs.
  """
def gradients_function(f, params: Incomplete | None = None):
    """Returns a function which differentiates f with respect to params.

  Example:
  ```python
  # f(x, y) = (x ^ 3) * y - x * (y ^ 2)
  # Therefore, the 1st order derivatives are:
  #   df / dx = 3 * (x ^ 2) * y - y ^ 2
  #   df / dy = x ^ 3 - 2 * x * y
  # The 2nd order derivatives with respect to x is:
  #   d^2 f / (dx)^2 = 6 * x * y
  def f(x, y):
    return x * x * x * y - x * y * y

  # Obtain a function that returns 1st order gradients.
  grad_fn = tfe.gradients_function(f)

  x = 2.0
  y = 3.0

  # Invoke the 1st order gradient function.
  x_grad, y_grad = grad_fn(x, y)
  assert x_grad.numpy() == 3 * (2 ** 2) * 3 - 3 ** 2
  assert y_grad.numpy() == (2 ** 3) - 2 * 2 * 3

  # Obtain a function that returns the 2nd order gradient with respect to x.
  gradgrad_fn = tfe.gradients_function(lambda x, y: grad_fn(x, y)[0])

  # Invoke the 2nd order gradient function.
  x_gradgrad = gradgrad_fn(x, y)[0]
  assert x_gradgrad.numpy() == 6 * 2 * 3

  # To obtain a callable that returns the gradient(s) of `f` with respect to a
  # subset of its inputs, use the `params` keyword argument with
  # `gradients_function()`.
  ygrad_fn = tfe.gradients_function(f, params=[1])

  (y_grad,) = ygrad_fn(x, y)
  assert y_grad.numpy() == (2 ** 3) - 2 * 2 * 3
  ```

  Note that only tensors with real or complex dtypes are differentiable.

  Args:
    f: function to be differentiated. If `f` returns a scalar, this scalar will
      be differentiated. If `f` returns a tensor or list of tensors, by default
      a scalar will be computed by adding all their values to produce a single
      scalar. If desired, the tensors can be elementwise multiplied by the
      tensors passed as the `dy` keyword argument to the returned gradient
      function.
    params: list of parameter names of f or list of integers indexing the
      parameters with respect to which we'll differentiate. Passing None
      differentiates with respect to all parameters.

  Returns:
    function which, when called, returns the value of f and the gradient
    of `f` with respect to all of `params`. The function takes an extra optional
    keyword argument `dy`. Setting it allows computation of vector jacobian
    products for vectors other than the vector of ones.

  Raises:
    ValueError: if the params are not all strings or all integers.
  """
def val_and_grad_function(f, params: Incomplete | None = None):
    '''Returns a function that computes f and its derivative w.r.t. params.

  Example:
  ```python
  # f(x, y) = (x ^ 3) * y - x * (y ^ 2)
  # Therefore, the 1st order derivatives are:
  #   df / dx = 3 * (x ^ 2) * y - y ^ 2
  #   df / dy = x ^ 3 - 2 * x * y
  def f(x, y):
    return x * x * x * y - x * y * y

  # Obtain a function that returns the function value and the 1st order
  # gradients.
  val_grads_fn = tfe.value_and_gradients_function(f)

  x = 2.0
  y = 3.0

  # Invoke the value-and-gradients function.
  f_val, (x_grad, y_grad) = val_grads_fn(x, y)
  assert f_val.numpy() == (2 ** 3) * 3 - 2 * (3 ** 2)
  assert x_grad.numpy() == 3 * (2 ** 2) * 3 - 3 ** 2
  assert y_grad.numpy() == (2 ** 3) - 2 * 2 * 3

  # To obtain a callable that returns the value of `f` and the gradient(s) of
  # `f` with respect to a subset of its inputs, use the `params` keyword
  # argument with `value_and_gradients_function()`.
  val_ygrad_fn = tfe.value_and_gradients_function(f, params=[1])

  f_val, (y_grad,) = val_ygrad_fn(x, y)
  assert f_val.numpy() == (2 ** 3) * 3 - 2 * (3 ** 2)
  assert y_grad.numpy() == (2 ** 3) - 2 * 2 * 3
  ```

  Args:
    f: function to be differentiated. If `f` returns a scalar, this scalar will
      be differentiated. If `f` returns a tensor or list of tensors, by default
      a scalar will be computed by adding all their values to produce a single
      scalar. If desired, the tensors can be elementwise multiplied by the
      tensors passed as the `dy` keyword argument to the returned gradient
      function.
    params: list of parameter names of f or list of integers indexing the
      parameters with respect to which we\'ll differentiate. Passing `None`
      differentiates with respect to all parameters.

  Returns:
    function which, when called, returns the value of f and the gradient
    of f with respect to all of `params`. The function takes an extra optional
    keyword argument "dy". Setting it allows computation of vector jacobian
    products for vectors other than the vector of ones.

  Raises:
    ValueError: if the params are not all strings or all integers.
  '''
def make_vjp(f, params: Incomplete | None = None, persistent: bool = True):
    '''Returns a function that computes f and its vjp w.r.t.

  params.

  The term "vjp" here is an abbreviation for vector-jacobian product.

  Args:
    f: the function to be differentiated.
    params: the parameters (numbers or names) to differentiate with respect to.
      A value of None will differentiate with respect to all parameters.
    persistent: Boolean controlling whether the VJP function can be re-used.
      Must be True or False.

  Returns:
    A function, which when called, returns a tuple (value, vjp), where:
    - value is the result of calling f.
    - vjp is a function, which takes a vector as an argument and
      returns the product of that vector with the Jacobian of f.
      Providing no argument to vjp is equivalent to providing a
      vector of ones.

    For example,
    ```python
    def f(x):
      return x * x

    wrapped_fn = tfe.make_vjp(f)
    result, vjp = wrapped_fn(tf.constant(3.0))
    # result is 9.0
    vjp()  # the vjp function returns 6.0

  Raises:
    ValueError: if `f` returns None.
  '''

class GradientTape:
    '''Record operations for automatic differentiation.

  Operations are recorded if they are executed within this context manager and
  at least one of their inputs is being "watched".

  Trainable variables (created by `tf.Variable` or `tf.compat.v1.get_variable`,
  where `trainable=True` is default in both cases) are automatically watched.
  Tensors can be manually watched by invoking the `watch` method on this context
  manager.

  For example, consider the function `y = x * x`. The gradient at `x = 3.0` can
  be computed as:

  >>> x = tf.constant(3.0)
  >>> with tf.GradientTape() as g:
  ...   g.watch(x)
  ...   y = x * x
  >>> dy_dx = g.gradient(y, x)
  >>> print(dy_dx)
  tf.Tensor(6.0, shape=(), dtype=float32)

  GradientTapes can be nested to compute higher-order derivatives. For example,

  >>> x = tf.constant(5.0)
  >>> with tf.GradientTape() as g:
  ...   g.watch(x)
  ...   with tf.GradientTape() as gg:
  ...     gg.watch(x)
  ...     y = x * x
  ...   dy_dx = gg.gradient(y, x)  # dy_dx = 2 * x
  >>> d2y_dx2 = g.gradient(dy_dx, x)  # d2y_dx2 = 2
  >>> print(dy_dx)
  tf.Tensor(10.0, shape=(), dtype=float32)
  >>> print(d2y_dx2)
  tf.Tensor(2.0, shape=(), dtype=float32)

  By default, the resources held by a GradientTape are released as soon as
  GradientTape.gradient() method is called. To compute multiple gradients over
  the same computation, create a persistent gradient tape. This allows multiple
  calls to the gradient() method as resources are released when the tape object
  is garbage collected. For example:

  >>> x = tf.constant(3.0)
  >>> with tf.GradientTape(persistent=True) as g:
  ...   g.watch(x)
  ...   y = x * x
  ...   z = y * y
  >>> dz_dx = g.gradient(z, x)  # (4*x^3 at x = 3)
  >>> print(dz_dx)
  tf.Tensor(108.0, shape=(), dtype=float32)
  >>> dy_dx = g.gradient(y, x)
  >>> print(dy_dx)
  tf.Tensor(6.0, shape=(), dtype=float32)

  By default GradientTape will automatically watch any trainable variables that
  are accessed inside the context. If you want fine grained control over which
  variables are watched you can disable automatic tracking by passing
  `watch_accessed_variables=False` to the tape constructor:

  >>> x = tf.Variable(2.0)
  >>> w = tf.Variable(5.0)
  >>> with tf.GradientTape(
  ...     watch_accessed_variables=False, persistent=True) as tape:
  ...   tape.watch(x)
  ...   y = x ** 2  # Gradients will be available for `x`.
  ...   z = w ** 3  # No gradients will be available as `w` isn\'t being watched.
  >>> dy_dx = tape.gradient(y, x)
  >>> print(dy_dx)
  tf.Tensor(4.0, shape=(), dtype=float32)
  >>> # No gradients will be available as `w` isn\'t being watched.
  >>> dz_dw = tape.gradient(z, w)
  >>> print(dz_dw)
  None

  Note that when using models you should ensure that your variables exist when
  using `watch_accessed_variables=False`. Otherwise it\'s quite easy to make your
  first iteration not have any gradients:

  ```python
  a = tf.keras.layers.Dense(32)
  b = tf.keras.layers.Dense(32)

  with tf.GradientTape(watch_accessed_variables=False) as tape:
    tape.watch(a.variables)  # Since `a.build` has not been called at this point
                             # `a.variables` will return an empty list and the
                             # tape will not be watching anything.
    result = b(a(inputs))
    tape.gradient(result, a.variables)  # The result of this computation will be
                                        # a list of `None`s since a\'s variables
                                        # are not being watched.
  ```

  Note that only tensors with real or complex dtypes are differentiable.
  '''
    def __init__(self, persistent: bool = False, watch_accessed_variables: bool = True) -> None:
        """Creates a new GradientTape.

    Args:
      persistent: Boolean controlling whether a persistent gradient tape
        is created. False by default, which means at most one call can
        be made to the gradient() method on this object.
      watch_accessed_variables: Boolean controlling whether the tape will
        automatically `watch` any (trainable) variables accessed while the tape
        is active. Defaults to True meaning gradients can be requested from any
        result computed in the tape derived from reading a trainable `Variable`.
        If False users must explicitly `watch` any `Variable`s they want to
        request gradients from.
    """
    def __enter__(self):
        """Enters a context inside which operations are recorded on this tape."""
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None:
        """Exits the recording context, no further operations are traced."""
    def watch(self, tensor) -> None:
        """Ensures that `tensor` is being traced by this tape.

    Args:
      tensor: a Tensor/Variable or list of Tensors/Variables.

    Raises:
      ValueError: if it encounters something that is not a tensor.
    """
    def stop_recording(self) -> Generator[None, None, None]:
        """Temporarily stops recording operations on this tape.

    Operations executed while this context manager is active will not be
    recorded on the tape. This is useful for reducing the memory used by tracing
    all computations.

    For example:

    >>> x = tf.constant(4.0)
    >>> with tf.GradientTape() as tape:
    ...   with tape.stop_recording():
    ...     y = x ** 2
    >>> dy_dx = tape.gradient(y, x)
    >>> print(dy_dx)
    None

    Yields:
      None
    Raises:
      RuntimeError: if the tape is not currently recording.
    """
    def reset(self) -> None:
        """Clears all information stored in this tape.

    Equivalent to exiting and reentering the tape context manager with a new
    tape. For example, the two following code blocks are equivalent:

    ```
    with tf.GradientTape() as t:
      loss = loss_fn()
    with tf.GradientTape() as t:
      loss += other_loss_fn()
    t.gradient(loss, ...)  # Only differentiates other_loss_fn, not loss_fn


    # The following is equivalent to the above
    with tf.GradientTape() as t:
      loss = loss_fn()
      t.reset()
      loss += other_loss_fn()
    t.gradient(loss, ...)  # Only differentiates other_loss_fn, not loss_fn
    ```

    This is useful if you don't want to exit the context manager for the tape,
    or can't because the desired reset point is inside a control flow construct:

    ```
    with tf.GradientTape() as t:
      loss = ...
      if loss > k:
        t.reset()
    ```
    """
    def watched_variables(self):
        """Returns variables watched by this tape in order of construction."""
    def gradient(self, target, sources, output_gradients: Incomplete | None = None, unconnected_gradients=...):
        """Computes the gradient using operations recorded in context of this tape.

    Note: Unless you set `persistent=True` a GradientTape can only be used to
    compute one set of gradients (or jacobians).

    In addition to Tensors, gradient also supports RaggedTensors. For example,

    >>> x = tf.ragged.constant([[1.0, 2.0], [3.0]])
    >>> with tf.GradientTape() as g:
    ...   g.watch(x)
    ...   y = x * x
    >>> g.gradient(y, x)
    <tf.RaggedTensor [[2.0, 4.0], [6.0]]>

    Args:
      target: a list or nested structure of Tensors or Variables or
        CompositeTensors to be differentiated.
      sources: a list or nested structure of Tensors or Variables or
        CompositeTensors. `target` will be differentiated against elements in
        `sources`.
      output_gradients: a list of gradients, one for each differentiable
        element of target. Defaults to None.
      unconnected_gradients: a value which can either hold 'none' or 'zero' and
        alters the value which will be returned if the target and sources are
        unconnected. The possible values and effects are detailed in
        'UnconnectedGradients' and it defaults to 'none'.

    Returns:
      a list or nested structure of Tensors (or IndexedSlices, or None, or
      CompositeTensor), one for each element in `sources`. Returned structure
      is the same as the structure of `sources`.

    Raises:
      RuntimeError: If called on a used, non-persistent tape.
      RuntimeError: If called inside the context of the tape.
      TypeError: If the target is a None object.
      ValueError: If the target is a variable or if unconnected gradients is
       called with an unknown value.
    """
    def jacobian(self, target, sources, unconnected_gradients=..., parallel_iterations: Incomplete | None = None, experimental_use_pfor: bool = True):
        """Computes the jacobian using operations recorded in context of this tape.

    Note: Unless you set `persistent=True` a GradientTape can only be used to
    compute one set of gradients (or jacobians).

    Note: By default the jacobian implementation uses parallel for (pfor), which
    creates a tf.function under the hood for each jacobian call. For better
    performance, and to avoid recompilation and vectorization rewrites on each
    call, enclose GradientTape code in @tf.function.

    See[wikipedia
    article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant)
    for the definition of a Jacobian.

    Example usage:

    ```python
    with tf.GradientTape() as g:
      x  = tf.constant([1.0, 2.0])
      g.watch(x)
      y = x * x
    jacobian = g.jacobian(y, x)
    # jacobian value is [[2., 0.], [0., 4.]]
    ```

    Args:
      target: Tensor to be differentiated.
      sources: a list or nested structure of Tensors or Variables. `target`
        will be differentiated against elements in `sources`.
      unconnected_gradients: a value which can either hold 'none' or 'zero' and
        alters the value which will be returned if the target and sources are
        unconnected. The possible values and effects are detailed in
        'UnconnectedGradients' and it defaults to 'none'.
      parallel_iterations: A knob to control how many iterations are dispatched
        in parallel. This knob can be used to control the total memory usage.
      experimental_use_pfor: If true, vectorizes the jacobian computation. Else
        falls back to a sequential while_loop. Vectorization can sometimes fail
        or lead to excessive memory usage. This option can be used to disable
        vectorization in such cases.

    Returns:
      A list or nested structure of Tensors (or None), one for each element in
      `sources`. Returned structure is the same as the structure of `sources`.
      Note if any gradient is sparse (IndexedSlices), jacobian function
      currently makes it dense and returns a Tensor instead. This may change in
      the future.


    Raises:
      RuntimeError: If called on a used, non-persistent tape.
      RuntimeError: If called on a non-persistent tape with eager execution
        enabled and without enabling experimental_use_pfor.
      ValueError: If vectorization of jacobian computation fails.
    """
    def batch_jacobian(self, target, source, unconnected_gradients=..., parallel_iterations: Incomplete | None = None, experimental_use_pfor: bool = True):
        """Computes and stacks per-example jacobians.

    See [wikipedia article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant)
    for the definition of a Jacobian. This function is essentially an efficient
    implementation of the following:

    `tf.stack([self.jacobian(y[i], x[i]) for i in range(x.shape[0])])`.

    Note that compared to `GradientTape.jacobian` which computes gradient of
    each output value w.r.t each input value, this function is useful when
    `target[i,...]` is independent of `source[j,...]` for `j != i`. This
    assumption allows more efficient computation as compared to
    `GradientTape.jacobian`. The output, as well as intermediate activations,
    are lower dimensional and avoid a bunch of redundant zeros which would
    result in the jacobian computation given the independence assumption.

    Note: Unless you set `persistent=True` a GradientTape can only be used to
    compute one set of gradients (or jacobians).

    Note: By default the batch_jacobian implementation uses parallel for (pfor),
    which creates a tf.function under the hood for each batch_jacobian call.
    For better performance, and to avoid recompilation and vectorization
    rewrites on each call, enclose GradientTape code in @tf.function.


    Example usage:

    ```python
    with tf.GradientTape() as g:
      x = tf.constant([[1., 2.], [3., 4.]], dtype=tf.float32)
      g.watch(x)
      y = x * x
    batch_jacobian = g.batch_jacobian(y, x)
    # batch_jacobian is [[[2,  0], [0,  4]], [[6,  0], [0,  8]]]
    ```

    Args:
      target: A tensor with rank 2 or higher and with shape [b, y1, ..., y_n].
        `target[i,...]` should only depend on `source[i,...]`.
      source: A tensor with rank 2 or higher and with shape [b, x1, ..., x_m].
      unconnected_gradients: a value which can either hold 'none' or 'zero' and
        alters the value which will be returned if the target and sources are
        unconnected. The possible values and effects are detailed in
        'UnconnectedGradients' and it defaults to 'none'.
      parallel_iterations: A knob to control how many iterations are dispatched
        in parallel. This knob can be used to control the total memory usage.
      experimental_use_pfor: If true, uses pfor for computing the Jacobian. Else
        uses a tf.while_loop.

    Returns:
      A tensor `t` with shape [b, y_1, ..., y_n, x1, ..., x_m] where `t[i, ...]`
      is the jacobian of `target[i, ...]` w.r.t. `source[i, ...]`, i.e. stacked
      per-example jacobians.

    Raises:
      RuntimeError: If called on a used, non-persistent tape.
      RuntimeError: If called on a non-persistent tape with eager execution
        enabled and without enabling experimental_use_pfor.
      ValueError: If vectorization of jacobian computation fails or if first
        dimension of `target` and `source` do not match.
    """
