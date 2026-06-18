from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python.eager import context as context, monitoring as monitoring
from tensorflow.python.framework import device as device, error_interpolation as error_interpolation, errors as errors, indexed_slices as indexed_slices, ops as ops, sparse_tensor as sparse_tensor
from tensorflow.python.ops import session_ops as session_ops
from tensorflow.python.training.experimental import mixed_precision_global_state as mixed_precision_global_state
from tensorflow.python.util import compat as compat, nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

class SessionInterface:
    """Base class for implementations of TensorFlow client sessions."""
    @property
    def graph(self) -> None:
        """The underlying TensorFlow graph, to be used in building Operations."""
    @property
    def sess_str(self) -> None:
        """The TensorFlow process to which this session will connect."""
    def run(self, fetches, feed_dict: Incomplete | None = None, options: Incomplete | None = None, run_metadata: Incomplete | None = None) -> None:
        """Runs operations in the session. See `BaseSession.run()` for details."""
    def partial_run_setup(self, fetches, feeds: Incomplete | None = None) -> None:
        """Sets up the feeds and fetches for partial runs in the session."""
    def partial_run(self, handle, fetches, feed_dict: Incomplete | None = None) -> None:
        """Continues the execution with additional feeds and fetches."""

def register_session_run_conversion_functions(tensor_type, fetch_function, feed_function: Incomplete | None = None, feed_function_for_partial_run: Incomplete | None = None) -> None:
    """Register fetch and feed conversion functions for `tf.Session.run()`.

  This function registers a triple of conversion functions for fetching and/or
  feeding values of user-defined types in a call to tf.Session.run().

  An example

  ```python
     class SquaredTensor(object):
       def __init__(self, tensor):
         self.sq = tf.square(tensor)
     #you can define conversion functions as follows:
     fetch_function = lambda squared_tensor:([squared_tensor.sq],
                                             lambda val: val[0])
     feed_function = lambda feed, feed_val: [(feed.sq, feed_val)]
     feed_function_for_partial_run = lambda feed: [feed.sq]
     #then after invoking this register function, you can use as follows:
     session.run(squared_tensor1,
                 feed_dict = {squared_tensor2 : some_numpy_array})
  ```

  Args:
    tensor_type: The type for which you want to register a conversion function.
    fetch_function: A callable that takes an object of type `tensor_type` and
      returns a tuple, where the first element is a list of `tf.Tensor` objects,
      and the second element is a callable that takes a list of ndarrays and
      returns an object of some value type that corresponds to `tensor_type`.
      fetch_function describes how to expand fetch into its component Tensors
      and how to contract the fetched results back into a single return value.
    feed_function: A callable that takes feed_key and feed_value as input, and
      returns a list of tuples (feed_tensor, feed_val), feed_key must have type
      `tensor_type`, and feed_tensor must have type `tf.Tensor`. Each feed
      function describes how to unpack a single fed value and map it to feeds of
      one or more tensors and their corresponding values.
    feed_function_for_partial_run: A callable for specifying tensor values to
      feed when setting up a partial run, which takes a `tensor_type` type
      object as input, and returns a list of Tensors.

  Raises:
    ValueError: If `tensor_type` has already been registered.
  """

class _FetchMapper:
    """Definition of the interface provided by fetch mappers.

  Fetch mappers are utility classes used by the _FetchHandler to handle
  arbitrary structures for the `fetch` argument to `Session.run()`.

  The `fetch` argument can be of various shapes: single tensor or op, list of
  fetches, tuple of fetches, namedtuple of fetches, or dict of fetches.  The
  structures can be arbitrarily nested.

  The low level run() API only wants a list of tensor or op names.  The various
  `_FetchMapper` subclasses below take care of handling the different shapes:
  uniquifying the fetches, and constructing results with the original shape.
  """
    def unique_fetches(self) -> None:
        """Return the list of unique tensors or ops needed by this fetch mapper.

    Returns:
      A list of tensors or ops.
    """
    def build_results(self, values) -> None:
        """Build results that match the original shape of the fetch.

    Args:
      values: List of values returned by run(). The values correspond exactly to
        the list tensors or ops returned by unique_fetches().

    Returns:
      A struct of the same shape as the original fetch object handled by
      this fetch mapper.  In the returned struct, the original fetches are
      replaced by their fetched values.
    """
    @staticmethod
    def for_fetch(fetch):
        """Creates fetch mapper that handles the structure of `fetch`.

    The default graph must be the one from which we want to fetch values when
    this function is called.

    Args:
      fetch: An arbitrary fetch structure: singleton, list, tuple, namedtuple,
        or dict.

    Returns:
      An instance of a subclass of `_FetchMapper` that handles the shape.
    """

class _ElementFetchMapper(_FetchMapper):
    """Fetch mapper for singleton tensors and ops."""
    def __init__(self, fetches, contraction_fn) -> None:
        """Creates an _ElementFetchMapper.

    This is the fetch mapper used for leaves in the fetch struct.  Because of
    the expansions mechanism, a leaf can actually fetch more than one tensor.

    Also note that the fetches here can be just strings (tensor or op names) or
    any other object that the graph knows how to convert to a tensor, such as a
    Variable.  So we have to run each fetch through `as_graph_element()` to get
    the corresponding tensor or op.

    Args:
      fetches: List of objects, as returned by a fetch_fn defined in
        _REGISTERED_EXPANSIONS.
      contraction_fn: Callable as returned by a fetch_fn.
    """
    def unique_fetches(self): ...
    def build_results(self, values): ...

class _ListFetchMapper(_FetchMapper):
    """Fetch mapper for lists, tuples, and namedtuples."""
    def __init__(self, fetches) -> None:
        """Creates a _ListFetchMapper.

    Args:
      fetches: List, tuple, or namedtuple of fetches.
    """
    def unique_fetches(self): ...
    def build_results(self, values): ...

class _DictFetchMapper(_FetchMapper):
    """Fetch mapper for dicts."""
    def __init__(self, fetches) -> None:
        """Creates a _DictFetchMapper.

    Args:
      fetches: Dict of fetches.
    """
    def unique_fetches(self): ...
    def build_results(self, values): ...

class _AttrsFetchMapper(_FetchMapper):
    """Fetch mapper for attrs decorated classes."""
    def __init__(self, fetches) -> None:
        """Creates a _AttrsFetchMapper.

    Args:
      fetches: An instance of an attrs decorated class.
    """
    def unique_fetches(self): ...
    def build_results(self, values): ...

class _FetchHandler:
    """Handler for structured fetches.

  Given a graph, a user-provided structure for fetches, and a feed dict, this
  class takes care of generating a list of tensor names to fetch and op names
  to run for a low level `run()` call.

  Given the results of the low level run call, this class can also rebuild a
  result structure matching the user-provided structure for fetches, but
  containing the corresponding results.
  """
    def __init__(self, graph, fetches, feeds, feed_handles: Incomplete | None = None) -> None:
        """Creates a fetch handler.

    Args:
      graph: Graph of the fetches.   Used to check for fetchability and to
        convert all fetches to tensors or ops as needed.
      fetches: An arbitrary fetch structure: singleton, list, tuple, namedtuple,
        or dict.
      feeds: A feed dict where keys are Tensors.
      feed_handles: A dict from feed Tensors to TensorHandle objects used as
        direct feeds.
    """
    def fetches(self):
        """Return the unique names of tensors to fetch.

    Returns:
      A list of strings.
    """
    def targets(self):
        """Return the unique names of ops to run.

    Returns:
      A list of strings.
    """
    def build_results(self, session, tensor_values):
        """Build results matching the original fetch shape.

    `tensor_values` must be a list of the same length as
    the one returned by `fetches()`, and holding the requested
    fetch values.

    This method builds a struct with the same shape as the original `fetches`
    passed to the constructor, in which the fetches are replaced by their
    fetched value.

    Args:
      session: The enclosing session.  Used for tensor handles.
      tensor_values: List of values matching the list returned by fetches().

    Returns:
      A structure of the same shape as the original `fetches` argument but
        containing tensors or None (for fetched ops).
    """

class _DeviceAttributes:
    """Struct-like object describing a device's attributes.

  Each device has 3 key properties:
   - name: the fully-qualified TensorFlow path to the device. For
        example: /job:worker/replica:0/task:3/device:CPU:0
   - device_type: the type of the device (e.g. CPU, GPU, TPU, etc.)
   - memory_limit_bytes: the maximum amount of memory available on the device
        (in bytes).
  """
    def __init__(self, name, device_type, memory_limit_bytes, incarnation) -> None: ...
    @property
    def name(self): ...
    @property
    def device_type(self): ...
    @property
    def memory_limit_bytes(self): ...
    @property
    def incarnation(self): ...

class BaseSession(SessionInterface):
    """A class for interacting with a TensorFlow computation.

  The BaseSession enables incremental graph building with inline
  execution of Operations and evaluation of Tensors.
  """
    def __init__(self, target: str = '', graph: Incomplete | None = None, config: Incomplete | None = None) -> None:
        """Constructs a new TensorFlow session.

    Args:
      target: (Optional) The TensorFlow execution engine to connect to.
      graph: (Optional) The graph to be used. If this argument is None, the
        default graph will be used.
      config: (Optional) ConfigProto proto used to configure the session. If no
        config is specified, the global default will be used. The global default
        can be configured via the tf.config APIs.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        creating the TensorFlow session.
      TypeError: If one of the arguments has the wrong type.
    """
    def list_devices(self):
        """Lists available devices in this session.

    ```python
    devices = sess.list_devices()
    for d in devices:
      print(d.name)
    ```

    Where:
      Each element in the list has the following properties
      name: A string with the full name of the device. ex:
          `/job:worker/replica:0/task:3/device:CPU:0`
      device_type: The type of the device (e.g. `CPU`, `GPU`, `TPU`.)
      memory_limit: The maximum amount of memory available on the device.
          Note: depending on the device, it is possible the usable memory could
          be substantially less.

    Raises:
      tf.errors.OpError: If it encounters an error (e.g. session is in an
      invalid state, or network errors occur).

    Returns:
      A list of devices in the session.
    """
    def close(self) -> None:
        """Closes this session.

    Calling this method frees all resources associated with the session.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        closing the TensorFlow session.
    """
    def __del__(self) -> None: ...
    @property
    def graph(self):
        """The graph that was launched in this session."""
    @property
    def graph_def(self):
        """A serializable version of the underlying TensorFlow graph.

    Returns:
      A graph_pb2.GraphDef proto containing nodes for all of the Operations in
      the underlying TensorFlow graph.
    """
    @property
    def sess_str(self): ...
    def as_default(self):
        """Returns a context manager that makes this object the default session.

    Use with the `with` keyword to specify that calls to
    `tf.Operation.run` or `tf.Tensor.eval` should be executed in
    this session.

    ```python
    c = tf.constant(..)
    sess = tf.compat.v1.Session()

    with sess.as_default():
      assert tf.compat.v1.get_default_session() is sess
      print(c.eval())
    ```

    To get the current default session, use `tf.compat.v1.get_default_session`.

    *N.B.* The `as_default` context manager *does not* close the
    session when you exit the context, and you must close the session
    explicitly.

    ```python
    c = tf.constant(...)
    sess = tf.compat.v1.Session()
    with sess.as_default():
      print(c.eval())
    # ...
    with sess.as_default():
      print(c.eval())

    sess.close()
    ```

    Alternatively, you can use `with tf.compat.v1.Session():` to create a
    session that is automatically closed on exiting the context,
    including when an uncaught exception is raised.

    *N.B.* The default session is a property of the current thread. If you
    create a new thread, and wish to use the default session in that
    thread, you must explicitly add a `with sess.as_default():` in that
    thread's function.

    *N.B.* Entering a `with sess.as_default():` block does not affect
    the current default graph. If you are using multiple graphs, and
    `sess.graph` is different from the value of
    `tf.compat.v1.get_default_graph`, you must explicitly enter a
    `with sess.graph.as_default():` block to make `sess.graph` the default
    graph.

    Returns:
      A context manager using this session as the default session.
    """
    def run(self, fetches, feed_dict: Incomplete | None = None, options: Incomplete | None = None, run_metadata: Incomplete | None = None):
        '''Runs operations and evaluates tensors in `fetches`.

    This method runs one "step" of TensorFlow computation, by
    running the necessary graph fragment to execute every `Operation`
    and evaluate every `Tensor` in `fetches`, substituting the values in
    `feed_dict` for the corresponding input values.

    The `fetches` argument may be a single graph element, or an arbitrarily
    nested list, tuple, namedtuple, dict, or OrderedDict containing graph
    elements at its leaves.  A graph element can be one of the following types:

    * A `tf.Operation`.
      The corresponding fetched value will be `None`.
    * A `tf.Tensor`.
      The corresponding fetched value will be a numpy ndarray containing the
      value of that tensor.
    * A `tf.sparse.SparseTensor`.
      The corresponding fetched value will be a
      `tf.compat.v1.SparseTensorValue`
      containing the value of that sparse tensor.
    * A `get_tensor_handle` op.  The corresponding fetched value will be a
      numpy ndarray containing the handle of that tensor.
    * A `string` which is the name of a tensor or operation in the graph.

    The value returned by `run()` has the same shape as the `fetches` argument,
    where the leaves are replaced by the corresponding values returned by
    TensorFlow.

    Example:

    ```python
       a = tf.constant([10, 20])
       b = tf.constant([1.0, 2.0])
       # \'fetches\' can be a singleton
       v = session.run(a)
       # v is the numpy array [10, 20]
       # \'fetches\' can be a list.
       v = session.run([a, b])
       # v is a Python list with 2 numpy arrays: the 1-D array [10, 20] and the
       # 1-D array [1.0, 2.0]
       # \'fetches\' can be arbitrary lists, tuples, namedtuple, dicts:
       MyData = collections.namedtuple(\'MyData\', [\'a\', \'b\'])
       v = session.run({\'k1\': MyData(a, b), \'k2\': [b, a]})
       # v is a dict with
       # v[\'k1\'] is a MyData namedtuple with \'a\' (the numpy array [10, 20]) and
       # \'b\' (the numpy array [1.0, 2.0])
       # v[\'k2\'] is a list with the numpy array [1.0, 2.0] and the numpy array
       # [10, 20].
    ```

    The optional `feed_dict` argument allows the caller to override
    the value of tensors in the graph. Each key in `feed_dict` can be
    one of the following types:

    * If the key is a `tf.Tensor`, the
      value may be a Python scalar, string, list, or numpy ndarray
      that can be converted to the same `dtype` as that
      tensor. Additionally, if the key is a
      `tf.compat.v1.placeholder`, the shape of
      the value will be checked for compatibility with the placeholder.
    * If the key is a
      `tf.sparse.SparseTensor`,
      the value should be a
      `tf.compat.v1.SparseTensorValue`.
    * If the key is a nested tuple of `Tensor`s or `SparseTensor`s, the value
      should be a nested tuple with the same structure that maps to their
      corresponding values as above.

    Each value in `feed_dict` must be convertible to a numpy array of the dtype
    of the corresponding key.

    The optional `options` argument expects a [`RunOptions`] proto. The options
    allow controlling the behavior of this particular step (e.g. turning tracing
    on).

    The optional `run_metadata` argument expects a [`RunMetadata`] proto. When
    appropriate, the non-Tensor output of this step will be collected there. For
    example, when users turn on tracing in `options`, the profiled info will be
    collected into this argument and passed back.

    Args:
      fetches: A single graph element, a list of graph elements, or a dictionary
        whose values are graph elements or lists of graph elements (described
        above).
      feed_dict: A dictionary that maps graph elements to values (described
        above).
      options: A [`RunOptions`] protocol buffer
      run_metadata: A [`RunMetadata`] protocol buffer

    Returns:
      Either a single value if `fetches` is a single graph element, or
      a list of values if `fetches` is a list, or a dictionary with the
      same keys as `fetches` if that is a dictionary (described above).
      Order in which `fetches` operations are evaluated inside the call
      is undefined.

    Raises:
      RuntimeError: If this `Session` is in an invalid state (e.g. has been
        closed).
      TypeError: If `fetches` or `feed_dict` keys are of an inappropriate type.
      ValueError: If `fetches` or `feed_dict` keys are invalid or refer to a
        `Tensor` that doesn\'t exist.
    '''
    def partial_run(self, handle, fetches, feed_dict: Incomplete | None = None):
        """Continues the execution with more feeds and fetches.

    This is EXPERIMENTAL and subject to change.

    To use partial execution, a user first calls `partial_run_setup()` and
    then a sequence of `partial_run()`. `partial_run_setup` specifies the
    list of feeds and fetches that will be used in the subsequent
    `partial_run` calls.

    The optional `feed_dict` argument allows the caller to override
    the value of tensors in the graph. See run() for more information.

    Below is a simple example:

    ```python
    a = array_ops.placeholder(dtypes.float32, shape=[])
    b = array_ops.placeholder(dtypes.float32, shape=[])
    c = array_ops.placeholder(dtypes.float32, shape=[])
    r1 = math_ops.add(a, b)
    r2 = math_ops.multiply(r1, c)

    h = sess.partial_run_setup([r1, r2], [a, b, c])
    res = sess.partial_run(h, r1, feed_dict={a: 1, b: 2})
    res = sess.partial_run(h, r2, feed_dict={c: res})
    ```

    Args:
      handle: A handle for a sequence of partial runs.
      fetches: A single graph element, a list of graph elements, or a dictionary
        whose values are graph elements or lists of graph elements (see
        documentation for `run`).
      feed_dict: A dictionary that maps graph elements to values (described
        above).

    Returns:
      Either a single value if `fetches` is a single graph element, or
      a list of values if `fetches` is a list, or a dictionary with the
      same keys as `fetches` if that is a dictionary
      (see documentation for `run`).

    Raises:
      tf.errors.OpError: Or one of its subclasses on error.
    """
    def partial_run_setup(self, fetches, feeds: Incomplete | None = None):
        """Sets up a graph with feeds and fetches for partial run.

    This is EXPERIMENTAL and subject to change.

    Note that contrary to `run`, `feeds` only specifies the graph elements.
    The tensors will be supplied by the subsequent `partial_run` calls.

    Args:
      fetches: A single graph element, or a list of graph elements.
      feeds: A single graph element, or a list of graph elements.

    Returns:
      A handle for partial run.

    Raises:
      RuntimeError: If this `Session` is in an invalid state (e.g. has been
        closed).
      TypeError: If `fetches` or `feed_dict` keys are of an inappropriate type.
      tf.errors.OpError: Or one of its subclasses if a TensorFlow error happens.
    """
    def make_callable(self, fetches, feed_list: Incomplete | None = None, accept_options: bool = False):
        """Returns a Python callable that runs a particular step.

    The returned callable will take `len(feed_list)` arguments whose types
    must be compatible feed values for the respective elements of `feed_list`.
    For example, if element `i` of `feed_list` is a `tf.Tensor`, the `i`th
    argument to the returned callable must be a numpy ndarray (or something
    convertible to an ndarray) with matching element type and shape. See
    `tf.Session.run` for details of the allowable feed key and value types.

    The returned callable will have the same return type as
    `tf.Session.run(fetches, ...)`. For example, if `fetches` is a `tf.Tensor`,
    the callable will return a numpy ndarray; if `fetches` is a `tf.Operation`,
    it will return `None`.

    Args:
      fetches: A value or list of values to fetch. See `tf.Session.run` for
        details of the allowable fetch types.
      feed_list: (Optional.) A list of `feed_dict` keys. See `tf.Session.run`
        for details of the allowable feed key types.
      accept_options: (Optional.) If `True`, the returned `Callable` will be
        able to accept `tf.compat.v1.RunOptions` and `tf.compat.v1.RunMetadata`
        as optional keyword arguments `options` and `run_metadata`,
        respectively, with the same syntax and semantics as `tf.Session.run`,
        which is useful for certain use cases (profiling and debugging) but will
        result in measurable slowdown of the `Callable`'s
        performance. Default: `False`.

    Returns:
      A function that when called will execute the step defined by
      `feed_list` and `fetches` in this session.

    Raises:
      TypeError: If `fetches` or `feed_list` cannot be interpreted
        as arguments to `tf.Session.run`.
    """
    class _Callable:
        """Experimental wrapper for the C++ `Session::MakeCallable()` API."""
        def __init__(self, session, callable_options) -> None: ...
        def __call__(self, *args, **kwargs): ...
        def __del__(self) -> None: ...

class Session(BaseSession):
    """A class for running TensorFlow operations.

  A `Session` object encapsulates the environment in which `Operation`
  objects are executed, and `Tensor` objects are evaluated. For
  example:

  ```python
  tf.compat.v1.disable_eager_execution() # need to disable eager in TF2.x
  # Build a graph.
  a = tf.constant(5.0)
  b = tf.constant(6.0)
  c = a * b

  # Launch the graph in a session.
  sess = tf.compat.v1.Session()

  # Evaluate the tensor `c`.
  print(sess.run(c)) # prints 30.0
  ```

  A session may own resources, such as
  `tf.Variable`, `tf.queue.QueueBase`,
  and `tf.compat.v1.ReaderBase`. It is important to release
  these resources when they are no longer required. To do this, either
  invoke the `tf.Session.close` method on the session, or use
  the session as a context manager. The following two examples are
  equivalent:

  ```python
  # Using the `close()` method.
  sess = tf.compat.v1.Session()
  sess.run(...)
  sess.close()

  # Using the context manager.
  with tf.compat.v1.Session() as sess:
    sess.run(...)
  ```

  The
  [`ConfigProto`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config.proto)
  protocol buffer exposes various configuration options for a
  session. For example, to create a session that uses soft constraints
  for device placement, and log the resulting placement decisions,
  create a session as follows:

  ```python
  # Launch the graph in a session that allows soft device placement and
  # logs the placement decisions.
  sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(
      allow_soft_placement=True,
      log_device_placement=True))
  ```

  @compatibility(TF2)
  `Session` does not work with either eager execution or `tf.function`, and you
  should not invoke it directly. To migrate code that uses sessions to TF2,
  rewrite the code without it. See the
  [migration
  guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
  on replacing `Session.run` calls.
  @end_compatibility
  """
    def __init__(self, target: str = '', graph: Incomplete | None = None, config: Incomplete | None = None) -> None:
        """Creates a new TensorFlow session.

    If no `graph` argument is specified when constructing the session,
    the default graph will be launched in the session. If you are
    using more than one graph (created with `tf.Graph()`) in the same
    process, you will have to use different sessions for each graph,
    but each graph can be used in multiple sessions. In this case, it
    is often clearer to pass the graph to be launched explicitly to
    the session constructor.

    Args:
      target: (Optional.) The execution engine to connect to. Defaults to using
        an in-process engine. See
        [Distributed TensorFlow](https://tensorflow.org/deploy/distributed) for
          more examples.
      graph: (Optional.) The `Graph` to be launched (described above).
      config: (Optional.) A
        [`ConfigProto`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config.proto)
          protocol buffer with configuration options for the session.
    """
    def __enter__(self): ...
    def __exit__(self, exec_type: type[BaseException] | None, exec_value: BaseException | None, exec_tb: types.TracebackType | None) -> None: ...
    @staticmethod
    def reset(target, containers: Incomplete | None = None, config: Incomplete | None = None) -> None:
        """Resets resource containers on `target`, and close all connected sessions.

    A resource container is distributed across all workers in the
    same cluster as `target`.  When a resource container on `target`
    is reset, resources associated with that container will be cleared.
    In particular, all Variables in the container will become undefined:
    they lose their values and shapes.

    NOTE:
    (i) reset() is currently only implemented for distributed sessions.
    (ii) Any sessions on the master named by `target` will be closed.

    If no resource containers are provided, all containers are reset.

    Args:
      target: The execution engine to connect to.
      containers: A list of resource container name strings, or `None` if all of
        all the containers are to be reset.
      config: (Optional.) Protocol buffer with configuration options.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        resetting containers.
    """

class InteractiveSession(BaseSession):
    """A TensorFlow `Session` for use in interactive contexts, such as a shell.

  The only difference with a regular `Session` is that an `InteractiveSession`
  installs itself as the default session on construction.
  The methods `tf.Tensor.eval`
  and `tf.Operation.run`
  will use that session to run ops.

  This is convenient in interactive shells and [IPython
  notebooks](http://ipython.org), as it avoids having to pass an explicit
  `Session` object to run ops.

  For example:

  ```python
  sess = tf.compat.v1.InteractiveSession()
  a = tf.constant(5.0)
  b = tf.constant(6.0)
  c = a * b
  # We can just use 'c.eval()' without passing 'sess'
  print(c.eval())
  sess.close()
  ```

  Note that a regular session installs itself as the default session when it
  is created in a `with` statement.  The common usage in non-interactive
  programs is to follow that pattern:

  ```python
  a = tf.constant(5.0)
  b = tf.constant(6.0)
  c = a * b
  with tf.compat.v1.Session():
    # We can also use 'c.eval()' here.
    print(c.eval())
  ```
  """
    def __init__(self, target: str = '', graph: Incomplete | None = None, config: Incomplete | None = None) -> None:
        """Creates a new interactive TensorFlow session.

    If no `graph` argument is specified when constructing the session,
    the default graph will be launched in the session. If you are
    using more than one graph (created with `tf.Graph()`) in the same
    process, you will have to use different sessions for each graph,
    but each graph can be used in multiple sessions. In this case, it
    is often clearer to pass the graph to be launched explicitly to
    the session constructor.

    Args:
      target: (Optional.) The execution engine to connect to. Defaults to using
        an in-process engine.
      graph: (Optional.) The `Graph` to be launched (described above).
      config: (Optional) `ConfigProto` proto used to configure the session.
    """
    def close(self) -> None:
        """Closes an `InteractiveSession`."""
