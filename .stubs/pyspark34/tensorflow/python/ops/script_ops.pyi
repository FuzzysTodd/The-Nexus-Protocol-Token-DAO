from _typeshed import Incomplete
from tensorflow.python.eager import backprop as backprop, backprop_util as backprop_util, context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, func_graph as func_graph, function as function, ops as ops, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import gen_script_ops as gen_script_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import compat as compat, deprecation as deprecation, dispatch as dispatch, nest as nest, tf_inspect as tf_inspect, variable_utils as variable_utils
from tensorflow.python.util.tf_export import tf_export as tf_export

tape_cache: Incomplete

class EagerFunc:
    """A wrapper for a function owned by an EagerPyFunc."""
    def __init__(self, func, Tout, is_grad_func) -> None:
        """Constructs an EagerFunc.

    Args:
      func: The function to wrap.
      Tout: A list of datatypes for the output; an empty list if the output is
        None.
      is_grad_func: Whether this EagerFunc is the gradient of another
        EagerPyFunc.
    """
    def set_support_graph_mode_gradient(self) -> None:
        """Indicates the object shall support gradient ops.

    This function is internally used by _EagerPyFuncGrad to support
    graph mode gradient of EagerFunc via tf.gradient().
    """
    def __call__(self, device, token, args):
        """Calls `self._func` in eager mode, recording the tape if needed."""

class FuncRegistry:
    """A helper class to keep track of registered py functions.

  FuncRegistry keeps a map from unique tokens (string) to python
  functions, which takes numpy arrays and outputs numpy arrays.
  """
    def __init__(self) -> None: ...
    def insert(self, func):
        """Registers `func` and returns a unique token for this entry."""
    def remove(self, token) -> None:
        """Removes the registered function corresponding to `token`."""
    def get(self, token, default: Incomplete | None = None):
        """Gets the registered function corresponding to `token`."""
    def __call__(self, token, device, args):
        """Calls the registered function for `token` with args.

    Args:
      token: A key into this `FuncRegistry` identifying which function to call.
      device: Name of the device on which outputs of `token`'s corresponding
        operation should be placed. Used iff the function registered for `token`
        is an EagerPyFunc.
      args: The arguments to pass to the function registered for `token`.

    Returns:
      The output of the function registered for `token`.

    Raises:
      ValueError: if no function is registered for `token`.
    """
    def size(self):
        """Returns how many functions are currently registered."""

def eager_py_func(func, inp, Tout, name: Incomplete | None = None):
    """Wraps a python function into a TensorFlow op that executes it eagerly.

  This function allows expressing computations in a TensorFlow graph as
  Python functions. In particular, it wraps a Python function `func`
  in a once-differentiable TensorFlow operation that executes it with eager
  execution enabled. As a consequence, `tf.py_function` makes it
  possible to express control flow using Python constructs (`if`, `while`,
  `for`, etc.), instead of TensorFlow control flow constructs (`tf.cond`,
  `tf.while_loop`). For example, you might use `tf.py_function` to
  implement the log huber function:

  ```python
  def log_huber(x, m):
    if tf.abs(x) <= m:
      return x**2
    else:
      return m**2 * (1 - 2 * tf.math.log(m) + tf.math.log(x**2))

  x = tf.constant(1.0)
  m = tf.constant(2.0)

  with tf.GradientTape() as t:
    t.watch([x, m])
    y = tf.py_function(func=log_huber, inp=[x, m], Tout=tf.float32)

  dy_dx = t.gradient(y, x)
  assert dy_dx.numpy() == 2.0
  ```

  You can also use `tf.py_function` to debug your models at runtime
  using Python tools, i.e., you can isolate portions of your code that
  you want to debug, wrap them in Python functions and insert `pdb` tracepoints
  or print statements as desired, and wrap those functions in
  `tf.py_function`.

  For more information on eager execution, see the
  [Eager guide](https://tensorflow.org/guide/eager).

  `tf.py_function` is similar in spirit to `tf.compat.v1.py_func`, but unlike
  the latter, the former lets you use TensorFlow operations in the wrapped
  Python function. In particular, while `tf.compat.v1.py_func` only runs on CPUs
  and wraps functions that take NumPy arrays as inputs and return NumPy arrays
  as outputs, `tf.py_function` can be placed on GPUs and wraps functions
  that take Tensors as inputs, execute TensorFlow operations in their bodies,
  and return Tensors as outputs.

  Note: We recommend to avoid using `tf.py_function` outside of prototyping
  and experimentation due to the following known limitations:

  * Calling `tf.py_function` will acquire the Python Global Interpreter Lock
    (GIL) that allows only one thread to run at any point in time. This will
    preclude efficient parallelization and distribution of the execution of the
    program.

  * The body of the function (i.e. `func`) will not be serialized in a
    `GraphDef`. Therefore, you should not use this function if you need to
    serialize your model and restore it in a different environment.

  * The operation must run in the same address space as the Python program
    that calls `tf.py_function()`. If you are using distributed
    TensorFlow, you must run a `tf.distribute.Server` in the same process as the
    program that calls `tf.py_function()` and you must pin the created
    operation to a device in that server (e.g. using `with tf.device():`).

  * Currently `tf.py_function` is not compatible with XLA. Calling
    `tf.py_function` inside `tf.function(jit_compile=True)` will raise an
    error.

  Args:
    func: A Python function that accepts `inp` as arguments, and returns a
      value (or list of values) whose type is described by `Tout`.

    inp: Input arguments for `func`.  A list whose elements are `Tensor`s or
      `CompositeTensors` (such as `tf.RaggedTensor`); or a single `Tensor` or
      `CompositeTensor`.

    Tout: The type(s) of the value(s) returned by `func`.  One of the
      following.

      * If `func` returns a `Tensor` (or a value that can be converted to a
        Tensor): the `tf.DType` for that value.
      * If `func` returns a `CompositeTensor`: The `tf.TypeSpec` for that value.
      * If `func` returns `None`: the empty list (`[]`).
      * If `func` returns a list of `Tensor` and `CompositeTensor` values:
        a corresponding list of `tf.DType`s and `tf.TypeSpec`s for each value.

    name: A name for the operation (optional).

  Returns:
    The value(s) computed by `func`: a `Tensor`, `CompositeTensor`, or list of
    `Tensor` and `CompositeTensor`; or an empty list if `func` returns `None`.
  """
def py_func_common(func, inp, Tout, stateful: bool = True, name: Incomplete | None = None):
    """Wraps a python function and uses it as a TensorFlow op.

  Given a python function `func`, which takes numpy arrays as its
  arguments and returns numpy arrays as its outputs, wrap this function as an
  operation in a TensorFlow graph. The following snippet constructs a simple
  TensorFlow graph that invokes the `np.sinh()` NumPy function as a operation
  in the graph:

  ```python
  def my_func(x):
    # x will be a numpy array with the contents of the placeholder below
    return np.sinh(x)
  input = tf.compat.v1.placeholder(tf.float32)
  y = tf.compat.v1.py_func(my_func, [input], tf.float32)
  ```

  **N.B.** The `tf.compat.v1.py_func()` operation has the following known
  limitations:

  * The body of the function (i.e. `func`) will not be serialized in a
    `GraphDef`. Therefore, you should not use this function if you need to
    serialize your model and restore it in a different environment.

  * The operation must run in the same address space as the Python program
    that calls `tf.compat.v1.py_func()`. If you are using distributed
    TensorFlow, you
    must run a `tf.distribute.Server` in the same process as the program that
    calls
    `tf.compat.v1.py_func()` and you must pin the created operation to a device
    in that
    server (e.g. using `with tf.device():`).

  Note: It produces tensors of unknown shape and rank as shape inference
    does not work on arbitrary Python code.
    If you need the shape, you need to set it based on statically
    available information.

    E.g.
    ```python
    import tensorflow as tf
    import numpy as np

    def make_synthetic_data(i):
        return np.cast[np.uint8](i) * np.ones([20,256,256,3],
                dtype=np.float32) / 10.

    def preprocess_fn(i):
        ones = tf.py_function(make_synthetic_data,[i],tf.float32)
        ones.set_shape(tf.TensorShape([None, None, None, None]))
        ones = tf.image.resize(ones, [224,224])
        return ones

    ds = tf.data.Dataset.range(10)
    ds = ds.map(preprocess_fn)
    ```

  Args:
    func: A Python function, which accepts `ndarray` objects as arguments and
      returns a list of `ndarray` objects (or a single `ndarray`). This function
      must accept as many arguments as there are tensors in `inp`, and these
      argument types will match the corresponding `tf.Tensor` objects in `inp`.
      The returns `ndarray`s must match the number and types defined `Tout`.
      Important Note: Input and output numpy `ndarray`s of `func` are not
        guaranteed to be copies. In some cases their underlying memory will be
        shared with the corresponding TensorFlow tensors. In-place modification
        or storing `func` input or return values in python datastructures
        without explicit (np.)copy can have non-deterministic consequences.
    inp: A list of `Tensor` objects.
    Tout: A list or tuple of tensorflow data types or a single tensorflow data
      type if there is only one, indicating what `func` returns.
    stateful: (Boolean.) If True, the function should be considered stateful. If
      a function is stateless, when given the same input it will return the same
      output and have no observable side effects. Optimizations such as common
      subexpression elimination are only performed on stateless operations.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` or a single `Tensor` which `func` computes.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but `tf.numpy_function` is a
  near-exact replacement, just drop the `stateful` argument (all
  `tf.numpy_function` calls are considered stateful). It is compatible with
  eager execution and `tf.function`.

  `tf.py_function` is a close but not an exact replacement, passing TensorFlow
  tensors to the wrapped function instead of NumPy arrays, which provides
  gradients and can take advantage of accelerators.

  Before:

  >>> def fn_using_numpy(x):
  ...   x[0] = 0.
  ...   return x
  >>> tf.compat.v1.py_func(fn_using_numpy, inp=[tf.constant([1., 2.])],
  ...     Tout=tf.float32, stateful=False)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([0., 2.], dtype=float32)>

  After:

  >>> tf.numpy_function(fn_using_numpy, inp=[tf.constant([1., 2.])],
  ...     Tout=tf.float32)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([0., 2.], dtype=float32)>

  @end_compatibility

  """
def py_func(func, inp, Tout, stateful: bool = True, name: Incomplete | None = None): ...
def numpy_function(func, inp, Tout, stateful: bool = True, name: Incomplete | None = None):
    """Wraps a python function and uses it as a TensorFlow op.

  Given a python function `func` wrap this function as an operation in a
  TensorFlow function. `func` must take numpy arrays as its arguments and
  return numpy arrays as its outputs.

  The following example creates a TensorFlow graph with `np.sinh()` as an
  operation in the graph:

  >>> def my_numpy_func(x):
  ...   # x will be a numpy array with the contents of the input to the
  ...   # tf.function
  ...   return np.sinh(x)
  >>> @tf.function(input_signature=[tf.TensorSpec(None, tf.float32)])
  ... def tf_function(input):
  ...   y = tf.numpy_function(my_numpy_func, [input], tf.float32)
  ...   return y * y
  >>> tf_function(tf.constant(1.))
  <tf.Tensor: shape=(), dtype=float32, numpy=1.3810978>

  Comparison to `tf.py_function`:
  `tf.py_function` and `tf.numpy_function` are very similar, except that
  `tf.numpy_function` takes numpy arrays, and not `tf.Tensor`s. If you want the
  function to contain `tf.Tensors`, and have any TensorFlow operations executed
  in the function be differentiable, please use `tf.py_function`.

  Note: We recommend to avoid using `tf.numpy_function` outside of
  prototyping and experimentation due to the following known limitations:

  * Calling `tf.numpy_function` will acquire the Python Global Interpreter Lock
    (GIL) that allows only one thread to run at any point in time. This will
    preclude efficient parallelization and distribution of the execution of the
    program. Therefore, you are discouraged to use `tf.numpy_function` outside
    of prototyping and experimentation.

  * The body of the function (i.e. `func`) will not be serialized in a
    `tf.SavedModel`. Therefore, you should not use this function if you need to
    serialize your model and restore it in a different environment.

  * The operation must run in the same address space as the Python program
    that calls `tf.numpy_function()`. If you are using distributed
    TensorFlow, you must run a `tf.distribute.Server` in the same process as the
    program that calls `tf.numpy_function`  you must pin the created
    operation to a device in that server (e.g. using `with tf.device():`).

  * Currently `tf.numpy_function` is not compatible with XLA. Calling
    `tf.numpy_function` inside `tf.function(jit_compile=True)` will raise an
    error.

  * Since the function takes numpy arrays, you cannot take gradients
    through a numpy_function. If you require something that is differentiable,
    please consider using tf.py_function.

  Args:
    func: A Python function, which accepts `numpy.ndarray` objects as arguments
      and returns a list of `numpy.ndarray` objects (or a single
      `numpy.ndarray`). This function must accept as many arguments as there are
      tensors in `inp`, and these argument types will match the corresponding
      `tf.Tensor` objects in `inp`. The returns `numpy.ndarray`s must match the
      number and types defined `Tout`.
      Important Note: Input and output `numpy.ndarray`s of `func` are not
        guaranteed to be copies. In some cases their underlying memory will be
        shared with the corresponding TensorFlow tensors. In-place modification
        or storing `func` input or return values in python datastructures
        without explicit (np.)copy can have non-deterministic consequences.
    inp: A list of `tf.Tensor` objects.
    Tout: A list or tuple of tensorflow data types or a single tensorflow data
      type if there is only one, indicating what `func` returns.
    stateful: (Boolean.) Setting this argument to False tells the runtime to
      treat the function as stateless, which enables certain optimizations.
      A function is stateless when given the same input it will return the
      same output and have no side effects; its only purpose is to have a
      return value.
      The behavior for a stateful function with the `stateful` argument False
      is undefined. In particular, caution should be taken when
      mutating the input arguments as this is a stateful operation.
    name: (Optional) A name for the operation.

  Returns:
    Single or list of `tf.Tensor` which `func` computes.
  """
