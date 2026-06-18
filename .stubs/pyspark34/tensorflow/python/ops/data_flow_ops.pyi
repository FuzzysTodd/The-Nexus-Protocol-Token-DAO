from tensorflow.python.ops.gen_data_flow_ops import *
from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import indexed_slices as indexed_slices, ops as ops, random_seed as random_seed, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.lib.io import python_io as python_io
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_data_flow_ops as gen_data_flow_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

class QueueBase:
    """Base class for queue implementations.

  A queue is a TensorFlow data structure that stores tensors across
  multiple steps, and exposes operations that enqueue and dequeue
  tensors.

  Each queue element is a tuple of one or more tensors, where each
  tuple component has a static dtype, and may have a static shape. The
  queue implementations support versions of enqueue and dequeue that
  handle single elements, versions that support enqueuing and
  dequeuing a batch of elements at once.

  See `tf.queue.FIFOQueue` and
  `tf.queue.RandomShuffleQueue` for concrete
  implementations of this class, and instructions on how to create
  them.
  """
    def __init__(self, dtypes, shapes, names, queue_ref) -> None:
        """Constructs a queue object from a queue reference.

    The two optional lists, `shapes` and `names`, must be of the same length
    as `dtypes` if provided.  The values at a given index `i` indicate the
    shape and name to use for the corresponding queue component in `dtypes`.

    Args:
      dtypes:  A list of types.  The length of dtypes must equal the number
        of tensors in each element.
      shapes: Constraints on the shapes of tensors in an element:
        A list of shape tuples or None. This list is the same length
        as dtypes.  If the shape of any tensors in the element are constrained,
        all must be; shapes can be None if the shapes should not be constrained.
      names: Optional list of names.  If provided, the `enqueue()` and
        `dequeue()` methods will use dictionaries with these names as keys.
        Must be None or a list or tuple of the same length as `dtypes`.
      queue_ref: The queue reference, i.e. the output of the queue op.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
    @staticmethod
    def from_list(index, queues):
        """Create a queue using the queue reference from `queues[index]`.

    Args:
      index: An integer scalar tensor that determines the input that gets
        selected.
      queues: A list of `QueueBase` objects.

    Returns:
      A `QueueBase` object.

    Raises:
      TypeError: When `queues` is not a list of `QueueBase` objects,
        or when the data types of `queues` are not all the same.
    """
    @property
    def queue_ref(self):
        """The underlying queue reference."""
    @property
    def name(self):
        """The name of the underlying queue."""
    @property
    def dtypes(self):
        """The list of dtypes for each component of a queue element."""
    @property
    def shapes(self):
        """The list of shapes for each component of a queue element."""
    @property
    def names(self):
        """The list of names for each component of a queue element."""
    def enqueue(self, vals, name: Incomplete | None = None):
        """Enqueues one element to this queue.

    If the queue is full when this operation executes, it will block
    until the element has been enqueued.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed before this operation runs,
    `tf.errors.CancelledError` will be raised. If this operation is
    blocked, and either (i) the queue is closed by a close operation
    with `cancel_pending_enqueues=True`, or (ii) the session is
    `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      vals: A tensor, a list or tuple of tensors, or a dictionary containing
        the values to enqueue.
      name: A name for the operation (optional).

    Returns:
      The operation that enqueues a new tuple of tensors to the queue.
    """
    def enqueue_many(self, vals, name: Incomplete | None = None):
        """Enqueues zero or more elements to this queue.

    This operation slices each component tensor along the 0th dimension to
    make multiple queue elements. All of the tensors in `vals` must have the
    same size in the 0th dimension.

    If the queue is full when this operation executes, it will block
    until all of the elements have been enqueued.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed before this operation runs,
    `tf.errors.CancelledError` will be raised. If this operation is
    blocked, and either (i) the queue is closed by a close operation
    with `cancel_pending_enqueues=True`, or (ii) the session is
    `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      vals: A tensor, a list or tuple of tensors, or a dictionary
        from which the queue elements are taken.
      name: A name for the operation (optional).

    Returns:
      The operation that enqueues a batch of tuples of tensors to the queue.
    """
    def dequeue(self, name: Incomplete | None = None):
        """Dequeues one element from this queue.

    If the queue is empty when this operation executes, it will block
    until there is an element to dequeue.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed, the queue is empty, and there are no pending
    enqueue operations that can fulfill this request,
    `tf.errors.OutOfRangeError` will be raised. If the session is
    `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      name: A name for the operation (optional).

    Returns:
      The tuple of tensors that was dequeued.
    """
    def dequeue_many(self, n, name: Incomplete | None = None):
        """Dequeues and concatenates `n` elements from this queue.

    This operation concatenates queue-element component tensors along
    the 0th dimension to make a single component tensor.  All of the
    components in the dequeued tuple will have size `n` in the 0th dimension.

    If the queue is closed and there are less than `n` elements left, then an
    `OutOfRange` exception is raised.

    At runtime, this operation may raise an error if the queue is
    `tf.QueueBase.close` before or during its execution. If the
    queue is closed, the queue contains fewer than `n` elements, and
    there are no pending enqueue operations that can fulfill this
    request, `tf.errors.OutOfRangeError` will be raised. If the
    session is `tf.Session.close`,
    `tf.errors.CancelledError` will be raised.

    Args:
      n: A scalar `Tensor` containing the number of elements to dequeue.
      name: A name for the operation (optional).

    Returns:
      The list of concatenated tensors that was dequeued.
    """
    def dequeue_up_to(self, n, name: Incomplete | None = None):
        """Dequeues and concatenates `n` elements from this queue.

    **Note** This operation is not supported by all queues.  If a queue does not
    support DequeueUpTo, then a `tf.errors.UnimplementedError` is raised.

    This operation concatenates queue-element component tensors along
    the 0th dimension to make a single component tensor. If the queue
    has not been closed, all of the components in the dequeued tuple
    will have size `n` in the 0th dimension.

    If the queue is closed and there are more than `0` but fewer than
    `n` elements remaining, then instead of raising a
    `tf.errors.OutOfRangeError` like `tf.QueueBase.dequeue_many`,
    less than `n` elements are returned immediately.  If the queue is
    closed and there are `0` elements left in the queue, then a
    `tf.errors.OutOfRangeError` is raised just like in `dequeue_many`.
    Otherwise the behavior is identical to `dequeue_many`.

    Args:
      n: A scalar `Tensor` containing the number of elements to dequeue.
      name: A name for the operation (optional).

    Returns:
      The tuple of concatenated tensors that was dequeued.
    """
    def close(self, cancel_pending_enqueues: bool = False, name: Incomplete | None = None):
        """Closes this queue.

    This operation signals that no more elements will be enqueued in
    the given queue. Subsequent `enqueue` and `enqueue_many`
    operations will fail. Subsequent `dequeue` and `dequeue_many`
    operations will continue to succeed if sufficient elements remain
    in the queue. Subsequently dequeue and dequeue_many operations
    that would otherwise block waiting for more elements (if close
    hadn't been called) will now fail immediately.

    If `cancel_pending_enqueues` is `True`, all pending requests will also
    be canceled.

    Args:
      cancel_pending_enqueues: (Optional.) A boolean, defaulting to
        `False` (described above).
      name: A name for the operation (optional).

    Returns:
      The operation that closes the queue.
    """
    def is_closed(self, name: Incomplete | None = None):
        """Returns true if queue is closed.

    This operation returns true if the queue is closed and false if the queue
    is open.

    Args:
      name: A name for the operation (optional).

    Returns:
      True if the queue is closed and false if the queue is open.
    """
    def size(self, name: Incomplete | None = None):
        """Compute the number of elements in this queue.

    Args:
      name: A name for the operation (optional).

    Returns:
      A scalar tensor containing the number of elements in this queue.
    """

class RandomShuffleQueue(QueueBase):
    """A queue implementation that dequeues elements in a random order.

  See `tf.queue.QueueBase` for a description of the methods on
  this class.
  """
    def __init__(self, capacity, min_after_dequeue, dtypes, shapes: Incomplete | None = None, names: Incomplete | None = None, seed: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'random_shuffle_queue') -> None:
        """Create a queue that dequeues elements in a random order.

    A `RandomShuffleQueue` has bounded capacity; supports multiple
    concurrent producers and consumers; and provides exactly-once
    delivery.

    A `RandomShuffleQueue` holds a list of up to `capacity`
    elements. Each element is a fixed-length tuple of tensors whose
    dtypes are described by `dtypes`, and whose shapes are optionally
    described by the `shapes` argument.

    If the `shapes` argument is specified, each component of a queue
    element must have the respective fixed shape. If it is
    unspecified, different queue elements may have different shapes,
    but the use of `dequeue_many` is disallowed.

    The `min_after_dequeue` argument allows the caller to specify a
    minimum number of elements that will remain in the queue after a
    `dequeue` or `dequeue_many` operation completes, to ensure a
    minimum level of mixing of elements. This invariant is maintained
    by blocking those operations until sufficient elements have been
    enqueued. The `min_after_dequeue` argument is ignored after the
    queue has been closed.

    Args:
      capacity: An integer. The upper bound on the number of elements
        that may be stored in this queue.
      min_after_dequeue: An integer (described above).
      dtypes:  A list of `DType` objects. The length of `dtypes` must equal
        the number of tensors in each queue element.
      shapes: (Optional.) A list of fully-defined `TensorShape` objects
        with the same length as `dtypes`, or `None`.
      names: (Optional.) A list of string naming the components in the queue
        with the same length as `dtypes`, or `None`.  If specified the dequeue
        methods return a dictionary with the names as keys.
      seed: A Python integer. Used to create a random seed. See
        `tf.compat.v1.set_random_seed`
        for behavior.
      shared_name: (Optional.) If non-empty, this queue will be shared under
        the given name across multiple sessions.
      name: Optional name for the queue operation.
    """

class FIFOQueue(QueueBase):
    """A queue implementation that dequeues elements in first-in first-out order.

  See `tf.queue.QueueBase` for a description of the methods on
  this class.
  """
    def __init__(self, capacity, dtypes, shapes: Incomplete | None = None, names: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'fifo_queue') -> None:
        """Creates a queue that dequeues elements in a first-in first-out order.

    A `FIFOQueue` has bounded capacity; supports multiple concurrent
    producers and consumers; and provides exactly-once delivery.

    A `FIFOQueue` holds a list of up to `capacity` elements. Each
    element is a fixed-length tuple of tensors whose dtypes are
    described by `dtypes`, and whose shapes are optionally described
    by the `shapes` argument.

    If the `shapes` argument is specified, each component of a queue
    element must have the respective fixed shape. If it is
    unspecified, different queue elements may have different shapes,
    but the use of `dequeue_many` is disallowed.

    Args:
      capacity: An integer. The upper bound on the number of elements
        that may be stored in this queue.
      dtypes:  A list of `DType` objects. The length of `dtypes` must equal
        the number of tensors in each queue element.
      shapes: (Optional.) A list of fully-defined `TensorShape` objects
        with the same length as `dtypes`, or `None`.
      names: (Optional.) A list of string naming the components in the queue
        with the same length as `dtypes`, or `None`.  If specified the dequeue
        methods return a dictionary with the names as keys.
      shared_name: (Optional.) If non-empty, this queue will be shared under
        the given name across multiple sessions.
      name: Optional name for the queue operation.
    """

class GPUCompatibleFIFOQueue(QueueBase):
    """A queue implementation that dequeues elements in first-in first-out order.

  GPUCompatibleFIFOQueue is like FIFOQueue, but the queue resource may be placed
  either on a CPU or on a GPU. It is not cross-device: enqueues and dequeues
  will be colocated with the queue resource. GPUCompatibleFIFOQueue only
  supports enqueue and dequeue at the moment, not enqueue_many or dequeue_many.

  See `tf.queue.QueueBase` for a description of the methods on this class.
  """
    def __init__(self, capacity, dtypes, shapes: Incomplete | None = None, names: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'fifo_queue') -> None:
        """Creates a queue that dequeues elements in a first-in first-out order.

    A `FIFOQueue` has bounded capacity; supports multiple concurrent
    producers and consumers; and provides exactly-once delivery.

    A `FIFOQueue` holds a list of up to `capacity` elements. Each
    element is a fixed-length tuple of tensors whose dtypes are
    described by `dtypes`, and whose shapes are optionally described
    by the `shapes` argument.

    If the `shapes` argument is specified, each component of a queue
    element must have the respective fixed shape. If it is
    unspecified, different queue elements may have different shapes,
    but the use of `dequeue_many` is disallowed.

    Args:
      capacity: An integer. The upper bound on the number of elements
        that may be stored in this queue.
      dtypes:  A list of `DType` objects. The length of `dtypes` must equal
        the number of tensors in each queue element.
      shapes: (Optional.) A list of fully-defined `TensorShape` objects
        with the same length as `dtypes`, or `None`.
      names: (Optional.) A list of string naming the components in the queue
        with the same length as `dtypes`, or `None`.  If specified the dequeue
        methods return a dictionary with the names as keys.
      shared_name: (Optional.) If non-empty, this queue will be shared under
        the given name across multiple sessions.
      name: Optional name for the queue operation.
    """
    def enqueue_many(self, vals, name: Incomplete | None = None) -> None:
        """enqueue_many is not supported on GPUCompatibleFIFOQueue."""
    def dequeue_many(self, n, name: Incomplete | None = None) -> None:
        """dequeue_many is not supported on GPUCompatibleFIFOQueue."""

class PaddingFIFOQueue(QueueBase):
    """A FIFOQueue that supports batching variable-sized tensors by padding.

  A `PaddingFIFOQueue` may contain components with dynamic shape, while also
  supporting `dequeue_many`.  See the constructor for more details.

  See `tf.queue.QueueBase` for a description of the methods on
  this class.
  """
    def __init__(self, capacity, dtypes, shapes, names: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'padding_fifo_queue') -> None:
        """Creates a queue that dequeues elements in a first-in first-out order.

    A `PaddingFIFOQueue` has bounded capacity; supports multiple concurrent
    producers and consumers; and provides exactly-once delivery.

    A `PaddingFIFOQueue` holds a list of up to `capacity` elements. Each
    element is a fixed-length tuple of tensors whose dtypes are
    described by `dtypes`, and whose shapes are described by the `shapes`
    argument.

    The `shapes` argument must be specified; each component of a queue
    element must have the respective shape.  Shapes of fixed
    rank but variable size are allowed by setting any shape dimension to None.
    In this case, the inputs' shape may vary along the given dimension, and
    `dequeue_many` will pad the given dimension with zeros up to the maximum
    shape of all elements in the given batch.

    Args:
      capacity: An integer. The upper bound on the number of elements
        that may be stored in this queue.
      dtypes:  A list of `DType` objects. The length of `dtypes` must equal
        the number of tensors in each queue element.
      shapes: A list of `TensorShape` objects, with the same length as
        `dtypes`.  Any dimension in the `TensorShape` containing value
        `None` is dynamic and allows values to be enqueued with
         variable size in that dimension.
      names: (Optional.) A list of string naming the components in the queue
        with the same length as `dtypes`, or `None`.  If specified the dequeue
        methods return a dictionary with the names as keys.
      shared_name: (Optional.) If non-empty, this queue will be shared under
        the given name across multiple sessions.
      name: Optional name for the queue operation.

    Raises:
      ValueError: If shapes is not a list of shapes, or the lengths of dtypes
        and shapes do not match, or if names is specified and the lengths of
        dtypes and names do not match.
    """

class PriorityQueue(QueueBase):
    """A queue implementation that dequeues elements in prioritized order.

  See `tf.queue.QueueBase` for a description of the methods on
  this class.
  """
    def __init__(self, capacity, types, shapes: Incomplete | None = None, names: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'priority_queue') -> None:
        """Creates a queue that dequeues elements in a first-in first-out order.

    A `PriorityQueue` has bounded capacity; supports multiple concurrent
    producers and consumers; and provides exactly-once delivery.

    A `PriorityQueue` holds a list of up to `capacity` elements. Each
    element is a fixed-length tuple of tensors whose dtypes are
    described by `types`, and whose shapes are optionally described
    by the `shapes` argument.

    If the `shapes` argument is specified, each component of a queue
    element must have the respective fixed shape. If it is
    unspecified, different queue elements may have different shapes,
    but the use of `dequeue_many` is disallowed.

    Enqueues and Dequeues to the `PriorityQueue` must include an additional
    tuple entry at the beginning: the `priority`.  The priority must be
    an int64 scalar (for `enqueue`) or an int64 vector (for `enqueue_many`).

    Args:
      capacity: An integer. The upper bound on the number of elements
        that may be stored in this queue.
      types:  A list of `DType` objects. The length of `types` must equal
        the number of tensors in each queue element, except the first priority
        element.  The first tensor in each element is the priority,
        which must be type int64.
      shapes: (Optional.) A list of fully-defined `TensorShape` objects,
        with the same length as `types`, or `None`.
      names: (Optional.) A list of strings naming the components in the queue
        with the same length as `dtypes`, or `None`.  If specified, the dequeue
        methods return a dictionary with the names as keys.
      shared_name: (Optional.) If non-empty, this queue will be shared under
        the given name across multiple sessions.
      name: Optional name for the queue operation.
    """

class Barrier:
    """Represents a key-value map that persists across graph executions."""
    def __init__(self, types, shapes: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'barrier') -> None:
        '''Creates a barrier that persists across different graph executions.

    A barrier represents a key-value map, where each key is a string, and
    each value is a tuple of tensors.

    At runtime, the barrier contains \'complete\' and \'incomplete\'
    elements. A complete element has defined tensors for all
    components of its value tuple, and may be accessed using
    take_many. An incomplete element has some undefined components in
    its value tuple, and may be updated using insert_many.

    The barrier call `take_many` outputs values in a particular order.
    First, it only outputs completed values.  Second, the order in which
    completed values are returned matches the order in which their very
    first component was inserted into the barrier.  So, for example, for this
    sequence of insertions and removals:

      barrier = Barrier((tf.string, tf.int32), shapes=((), ()))
      barrier.insert_many(0, keys=["k1", "k2"], values=["a", "b"]).run()
      barrier.insert_many(1, keys=["k1"], values=[1]).run()
      barrier.insert_many(0, keys=["k3"], values=["c"]).run()
      barrier.insert_many(1, keys=["k3"], values=[3]).run()
      barrier.insert_many(1, keys=["k2"], values=[2]).run()

      (indices, keys, values) = barrier.take_many(2)
      (indices_val, keys_val, values0_val, values1_val) =
         session.run([indices, keys, values[0], values[1]])

    The output will be (up to permutation of "k1" and "k2"):

      indices_val == (-2**63, -2**63)
      keys_val == ("k1", "k2")
      values0_val == ("a", "b")
      values1_val == (1, 2)

    Note the key "k2" was inserted into the barrier before "k3".  Even though
    "k3" was completed first, both are complete by the time
    take_many is called.  As a result, "k2" is prioritized and "k1" and "k2"
    are returned first.  "k3" remains in the barrier until the next execution
    of `take_many`.  Since "k1" and "k2" had their first insertions into
    the barrier together, their indices are the same (-2**63).  The index
    of "k3" will be -2**63 + 1, because it was the next new inserted key.

    Args:
      types: A single dtype or a tuple of dtypes, corresponding to the
        dtypes of the tensor elements that comprise a value in this barrier.
      shapes: Optional. Constraints on the shapes of tensors in the values:
        a single tensor shape tuple; a tuple of tensor shape tuples
        for each barrier-element tuple component; or None if the shape should
        not be constrained.
      shared_name: Optional. If non-empty, this barrier will be shared under
        the given name across multiple sessions.
      name: Optional name for the barrier op.

    Raises:
      ValueError: If one of the `shapes` indicate no elements.
    '''
    @property
    def barrier_ref(self):
        """Get the underlying barrier reference."""
    @property
    def name(self):
        """The name of the underlying barrier."""
    def insert_many(self, component_index, keys, values, name: Incomplete | None = None):
        """For each key, assigns the respective value to the specified component.

    This operation updates each element at component_index.

    Args:
      component_index: The component of the value that is being assigned.
      keys: A vector of keys, with length n.
      values: An any-dimensional tensor of values, which are associated with the
        respective keys. The first dimension must have length n.
      name: Optional name for the op.

    Returns:
      The operation that performs the insertion.
    Raises:
      InvalidArgumentsError: If inserting keys and values without elements.
    """
    def take_many(self, num_elements, allow_small_batch: bool = False, timeout: Incomplete | None = None, name: Incomplete | None = None):
        '''Takes the given number of completed elements from this barrier.

    This operation concatenates completed-element component tensors along
    the 0th dimension to make a single component tensor.

    If barrier has no completed elements, this operation will block
    until there are \'num_elements\' elements to take.

    TODO(b/25743580): the semantics of `allow_small_batch` are experimental
    and may be extended to other cases in the future.

    TODO(ebrevdo): If a take_many(allow_small_batch=True) is blocking
    already when the barrier is closed, it will block for ever. Fix this
    by using asynchronous operations.

    Args:
      num_elements: The number of elements to take.
      allow_small_batch: If the barrier is closed, don\'t block if there are less
        completed elements than requested, but instead return all available
        completed elements.
      timeout: This specifies the number of milliseconds to block
        before returning with DEADLINE_EXCEEDED. (This option is not
        supported yet.)
      name: A name for the operation (optional).

    Returns:
      A tuple of (index, key, value_list).
      "index" is a int64 tensor of length num_elements containing the
        index of the insert_many call for which the very first component of
        the given element was inserted into the Barrier, starting with
        the value -2**63.  Note, this value is different from the
        index of the insert_many call for which the element was completed.
      "key" is a string tensor of length num_elements containing the keys.
      "value_list" is a tuple of tensors, each one with size num_elements
        in the 0th dimension for each component in the barrier\'s values.

    '''
    def close(self, cancel_pending_enqueues: bool = False, name: Incomplete | None = None):
        """Closes this barrier.

    This operation signals that no more new key values will be inserted in the
    given barrier. Subsequent InsertMany operations with new keys will fail.
    InsertMany operations that just complement already existing keys with other
    components, will continue to succeed. Subsequent TakeMany operations will
    continue to succeed if sufficient elements remain in the barrier. Subsequent
    TakeMany operations that would block will fail immediately.

    If `cancel_pending_enqueues` is `True`, all pending requests to the
    underlying queue will also be canceled, and completing of already
    started values is also not acceptable anymore.

    Args:
      cancel_pending_enqueues: (Optional.) A boolean, defaulting to
        `False` (described above).
      name: Optional name for the op.

    Returns:
      The operation that closes the barrier.
    """
    def ready_size(self, name: Incomplete | None = None):
        """Compute the number of complete elements in the given barrier.

    Args:
      name: A name for the operation (optional).

    Returns:
      A single-element tensor containing the number of complete elements in the
      given barrier.
    """
    def incomplete_size(self, name: Incomplete | None = None):
        """Compute the number of incomplete elements in the given barrier.

    Args:
      name: A name for the operation (optional).

    Returns:
      A single-element tensor containing the number of incomplete elements in
      the given barrier.
    """

class ConditionalAccumulatorBase:
    """A conditional accumulator for aggregating gradients.

  Up-to-date gradients (i.e., time step at which gradient was computed is
  equal to the accumulator's time step) are added to the accumulator.

  Extraction of the average gradient is blocked until the required number of
  gradients has been accumulated.
  """
    def __init__(self, dtype, shape, accumulator_ref) -> None:
        """Creates a new ConditionalAccumulator.

    Args:
      dtype: Datatype of the accumulated gradients.
      shape: Shape of the accumulated gradients.
      accumulator_ref: A handle to the conditional accumulator, created by sub-
        classes
    """
    @property
    def accumulator_ref(self):
        """The underlying accumulator reference."""
    @property
    def name(self):
        """The name of the underlying accumulator."""
    @property
    def dtype(self):
        """The datatype of the gradients accumulated by this accumulator."""
    def num_accumulated(self, name: Incomplete | None = None):
        """Number of gradients that have currently been aggregated in accumulator.

    Args:
      name: Optional name for the operation.

    Returns:
      Number of accumulated gradients currently in accumulator.
    """
    def set_global_step(self, new_global_step, name: Incomplete | None = None):
        """Sets the global time step of the accumulator.

    The operation logs a warning if we attempt to set to a time step that is
    lower than the accumulator's own time step.

    Args:
      new_global_step: Value of new time step. Can be a variable or a constant
      name: Optional name for the operation.

    Returns:
      Operation that sets the accumulator's time step.
    """

class ConditionalAccumulator(ConditionalAccumulatorBase):
    """A conditional accumulator for aggregating gradients.

  Up-to-date gradients (i.e., time step at which gradient was computed is
  equal to the accumulator's time step) are added to the accumulator.

  Extraction of the average gradient is blocked until the required number of
  gradients has been accumulated.
  """
    def __init__(self, dtype, shape: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'conditional_accumulator', reduction_type: str = 'MEAN') -> None:
        """Creates a new ConditionalAccumulator.

    Args:
      dtype: Datatype of the accumulated gradients.
      shape: Shape of the accumulated gradients.
      shared_name: Optional. If non-empty, this accumulator will be shared under
        the given name across multiple sessions.
      name: Optional name for the accumulator.
      reduction_type: Reduction type to use when taking the gradient.
    """
    def apply_grad(self, grad, local_step: int = 0, name: Incomplete | None = None):
        """Attempts to apply a gradient to the accumulator.

    The attempt is silently dropped if the gradient is stale, i.e., local_step
    is less than the accumulator's global time step.

    Args:
      grad: The gradient tensor to be applied.
      local_step: Time step at which the gradient was computed.
      name: Optional name for the operation.

    Returns:
      The operation that (conditionally) applies a gradient to the accumulator.

    Raises:
      ValueError: If grad is of the wrong shape
    """
    def take_grad(self, num_required, name: Incomplete | None = None):
        """Attempts to extract the average gradient from the accumulator.

    The operation blocks until sufficient number of gradients have been
    successfully applied to the accumulator.

    Once successful, the following actions are also triggered:

    - Counter of accumulated gradients is reset to 0.
    - Aggregated gradient is reset to 0 tensor.
    - Accumulator's internal time step is incremented by 1.

    Args:
      num_required: Number of gradients that needs to have been aggregated
      name: Optional name for the operation

    Returns:
      A tensor holding the value of the average gradient.

    Raises:
      InvalidArgumentError: If num_required < 1
    """

class SparseConditionalAccumulator(ConditionalAccumulatorBase):
    """A conditional accumulator for aggregating sparse gradients.

  Sparse gradients are represented by `IndexedSlices`.

  Up-to-date gradients (i.e., time step at which gradient was computed is
  equal to the accumulator's time step) are added to the accumulator.

  Extraction of the average gradient is blocked until the required number of
  gradients has been accumulated.

  Args:
    dtype: Datatype of the accumulated gradients.
    shape: Shape of the accumulated gradients.
    shared_name: Optional. If non-empty, this accumulator will be shared under
      the given name across multiple sessions.
    name: Optional name for the accumulator.
    reduction_type: Reduction type to use when taking the gradient.
  """
    def __init__(self, dtype, shape: Incomplete | None = None, shared_name: Incomplete | None = None, name: str = 'sparse_conditional_accumulator', reduction_type: str = 'MEAN') -> None: ...
    def apply_indexed_slices_grad(self, grad, local_step: int = 0, name: Incomplete | None = None):
        """Attempts to apply a gradient to the accumulator.

    The attempt is silently dropped if the gradient is stale, i.e., `local_step`
    is less than the accumulator's global time step.

    Args:
      grad: The gradient `IndexedSlices` to be applied.
      local_step: Time step at which the gradient was computed.
      name: Optional name for the operation.

    Returns:
      The operation that (conditionally) applies a gradient to the accumulator.

    Raises:
      InvalidArgumentError: If grad is of the wrong shape
    """
    def apply_grad(self, grad_indices, grad_values, grad_shape: Incomplete | None = None, local_step: int = 0, name: Incomplete | None = None):
        """Attempts to apply a sparse gradient to the accumulator.

    The attempt is silently dropped if the gradient is stale, i.e., `local_step`
    is less than the accumulator's global time step.

    A sparse gradient is represented by its indices, values and possibly empty
    or None shape. Indices must be a vector representing the locations of
    non-zero entries in the tensor. Values are the non-zero slices of the
    gradient, and must have the same first dimension as indices, i.e., the nnz
    represented by indices and values must be consistent. Shape, if not empty or
    None, must be consistent with the accumulator's shape (if also provided).

    Example:
      A tensor [[0, 0], [0, 1], [2, 3]] can be represented
        indices: [1,2]
        values: [[0,1],[2,3]]
        shape: [3, 2]

    Args:
      grad_indices: Indices of the sparse gradient to be applied.
      grad_values: Values of the sparse gradient to be applied.
      grad_shape: Shape of the sparse gradient to be applied.
      local_step: Time step at which the gradient was computed.
      name: Optional name for the operation.

    Returns:
      The operation that (conditionally) applies a gradient to the accumulator.

    Raises:
      InvalidArgumentError: If grad is of the wrong shape
    """
    def take_grad(self, num_required, name: Incomplete | None = None):
        """Attempts to extract the average gradient from the accumulator.

    The operation blocks until sufficient number of gradients have been
    successfully applied to the accumulator.

    Once successful, the following actions are also triggered:
    - Counter of accumulated gradients is reset to 0.
    - Aggregated gradient is reset to 0 tensor.
    - Accumulator's internal time step is incremented by 1.

    Args:
      num_required: Number of gradients that needs to have been aggregated
      name: Optional name for the operation

    Returns:
      A tuple of indices, values, and shape representing the average gradient.

    Raises:
      InvalidArgumentError: If `num_required` < 1
    """
    def take_indexed_slices_grad(self, num_required, name: Incomplete | None = None):
        """Attempts to extract the average gradient from the accumulator.

    The operation blocks until sufficient number of gradients have been
    successfully applied to the accumulator.

    Once successful, the following actions are also triggered:
    - Counter of accumulated gradients is reset to 0.
    - Aggregated gradient is reset to 0 tensor.
    - Accumulator's internal time step is incremented by 1.

    Args:
      num_required: Number of gradients that needs to have been aggregated
      name: Optional name for the operation

    Returns:
      An `IndexedSlices` holding the value of the average gradient.

    Raises:
      InvalidArgumentError: If `num_required` < 1
    """
    def num_accumulated(self, name: Incomplete | None = None):
        """Number of gradients that have currently been aggregated in accumulator.

    Args:
      name: Optional name for the operation.

    Returns:
      Number of accumulated gradients currently in accumulator.
    """
    def set_global_step(self, new_global_step, name: Incomplete | None = None):
        """Sets the global time step of the accumulator.

    The operation logs a warning if we attempt to set to a time step that is
    lower than the accumulator's own time step.

    Args:
      new_global_step: Value of new time step. Can be a variable or a constant
      name: Optional name for the operation.

    Returns:
      Operation that sets the accumulator's time step.
    """

class BaseStagingArea:
    """Base class for Staging Areas."""
    def __init__(self, dtypes, shapes: Incomplete | None = None, names: Incomplete | None = None, shared_name: Incomplete | None = None, capacity: int = 0, memory_limit: int = 0) -> None: ...
    @property
    def name(self):
        """The name of the staging area."""
    @property
    def dtypes(self):
        """The list of dtypes for each component of a staging area element."""
    @property
    def shapes(self):
        """The list of shapes for each component of a staging area element."""
    @property
    def names(self):
        """The list of names for each component of a staging area element."""
    @property
    def capacity(self):
        """The maximum number of elements of this staging area."""
    @property
    def memory_limit(self):
        """The maximum number of bytes of this staging area."""

class StagingArea(BaseStagingArea):
    """Class for staging inputs. No ordering guarantees.

  A `StagingArea` is a TensorFlow data structure that stores tensors across
  multiple steps, and exposes operations that can put and get tensors.

  Each `StagingArea` element is a tuple of one or more tensors, where each
  tuple component has a static dtype, and may have a static shape.

  The capacity of a `StagingArea` may be bounded or unbounded.
  It supports multiple concurrent producers and consumers; and
  provides exactly-once delivery.

  Each element of a `StagingArea` is a fixed-length tuple of tensors whose
  dtypes are described by `dtypes`, and whose shapes are optionally described
  by the `shapes` argument.

  If the `shapes` argument is specified, each component of a staging area
  element must have the respective fixed shape. If it is
  unspecified, different elements may have different shapes,

  It can be configured with a capacity in which case
  put(values) will block until space becomes available.

  Similarly, it can be configured with a memory limit which
  will block put(values) until space is available.
  This is mostly useful for limiting the number of tensors on
  devices such as GPUs.

  All get() and peek() commands block if the requested data
  is not present in the Staging Area.

  """
    def __init__(self, dtypes, shapes: Incomplete | None = None, names: Incomplete | None = None, shared_name: Incomplete | None = None, capacity: int = 0, memory_limit: int = 0) -> None:
        """Constructs a staging area object.

    The two optional lists, `shapes` and `names`, must be of the same length
    as `dtypes` if provided.  The values at a given index `i` indicate the
    shape and name to use for the corresponding queue component in `dtypes`.

    The device scope at the time of object creation determines where the
    storage for the `StagingArea` will reside.  Calls to `put` will incur a copy
    to this memory space, if necessary.  Tensors returned by `get` will be
    placed according to the device scope when `get` is called.

    Args:
      dtypes:  A list of types.  The length of dtypes must equal the number
        of tensors in each element.
      shapes: (Optional.) Constraints on the shapes of tensors in an element.
        A list of shape tuples or None. This list is the same length
        as dtypes.  If the shape of any tensors in the element are constrained,
        all must be; shapes can be None if the shapes should not be constrained.
      names: (Optional.) If provided, the `get()` and
        `put()` methods will use dictionaries with these names as keys.
        Must be None or a list or tuple of the same length as `dtypes`.
      shared_name: (Optional.) A name to be used for the shared object. By
        passing the same name to two different python objects they will share
        the underlying staging area. Must be a string.
      capacity: (Optional.) Maximum number of elements.
        An integer. If zero, the Staging Area is unbounded
      memory_limit: (Optional.) Maximum number of bytes of all tensors
        in the Staging Area.
        An integer. If zero, the Staging Area is unbounded

    Raises:
      ValueError: If one of the arguments is invalid.
    """
    def put(self, values, name: Incomplete | None = None):
        """Create an op that places a value into the staging area.

    This operation will block if the `StagingArea` has reached
    its capacity.

    Args:
      values: A single tensor, a list or tuple of tensors, or a dictionary with
        tensor values. The number of elements must match the length of the
        list provided to the dtypes argument when creating the StagingArea.
      name: A name for the operation (optional).

    Returns:
        The created op.

    Raises:
      ValueError: If the number or type of inputs don't match the staging area.
    """
    def get(self, name: Incomplete | None = None):
        """Gets one element from this staging area.

    If the staging area is empty when this operation executes, it will block
    until there is an element to dequeue.

    Note that unlike others ops that can block, like the queue Dequeue
    operations, this can stop other work from happening.  To avoid this, the
    intended use is for this to be called only when there will be an element
    already available.  One method for doing this in a training loop would be to
    run a `put()` call during a warmup session.run call, and then call both
    `get()` and `put()` in each subsequent step.

    The placement of the returned tensor will be determined by the current
    device scope when this function is called.

    Args:
      name: A name for the operation (optional).

    Returns:
      The tuple of tensors that was gotten.
    """
    def peek(self, index, name: Incomplete | None = None):
        """Peeks at an element in the staging area.

    If the staging area is too small to contain the element at
    the specified index, it will block until enough elements
    are inserted to complete the operation.

    The placement of the returned tensor will be determined by
    the current device scope when this function is called.

    Args:
      index: The index of the tensor within the staging area
              to look up.
      name: A name for the operation (optional).

    Returns:
      The tuple of tensors that was gotten.
    """
    def size(self, name: Incomplete | None = None):
        """Returns the number of elements in the staging area.

    Args:
        name: A name for the operation (optional)

    Returns:
        The created op
    """
    def clear(self, name: Incomplete | None = None):
        """Clears the staging area.

    Args:
        name: A name for the operation (optional)

    Returns:
        The created op
    """

class MapStagingArea(BaseStagingArea):
    """A `MapStagingArea` is a TensorFlow data structure that stores tensors
  across multiple steps, and exposes operations that can put and get tensors.

  Each `MapStagingArea` element is a (key, value) pair.
  Only int64 keys are supported, other types should be
  hashed to produce a key.
  Values are a tuple of one or more tensors.
  Each tuple component has a static dtype,
  and may have a static shape.

  The capacity of a `MapStagingArea` may be bounded or unbounded.
  It supports multiple concurrent producers and consumers; and
  provides exactly-once delivery.

  Each value tuple of a `MapStagingArea` is a fixed-length tuple of tensors
  whose
  dtypes are described by `dtypes`, and whose shapes are optionally described
  by the `shapes` argument.

  If the `shapes` argument is specified, each component of a staging area
  element must have the respective fixed shape. If it is
  unspecified, different elements may have different shapes,

  It behaves like an associative container with support for:

   - put(key, values)
   - peek(key)         like dict.get(key)
   - get(key)          like dict.pop(key)
   - get(key=None)     like dict.popitem()
   - size()
   - clear()

  If ordered a tree structure ordered by key will be used and
  get(key=None) will remove (key, value) pairs in increasing key order.
  Otherwise a hashtable

  It can be configured with a capacity in which case
  put(key, values) will block until space becomes available.

  Similarly, it can be configured with a memory limit which
  will block put(key, values) until space is available.
  This is mostly useful for limiting the number of tensors on
  devices such as GPUs.

  All get() and peek() commands block if the requested
  (key, value) pair is not present in the staging area.

  Partial puts are supported and will be placed in an incomplete
  map until such time as all values associated with the key have
  been inserted. Once completed, this (key, value) pair will be
  inserted into the map. Data in the incomplete map
  counts towards the memory limit, but not towards capacity limit.

  Partial gets from the map are also supported.
  This removes the partially requested tensors from the entry,
  but the entry is only removed from the map once all tensors
  associated with it are removed.
  """
    def __init__(self, dtypes, shapes: Incomplete | None = None, names: Incomplete | None = None, shared_name: Incomplete | None = None, ordered: bool = False, capacity: int = 0, memory_limit: int = 0) -> None:
        """Args:

      dtypes:  A list of types.  The length of dtypes must equal the number
        of tensors in each element.
      capacity: (Optional.) Maximum number of elements.
        An integer. If zero, the Staging Area is unbounded
      memory_limit: (Optional.) Maximum number of bytes of all tensors
        in the Staging Area (excluding keys).
        An integer. If zero, the Staging Area is unbounded
      ordered: (Optional.) If True the underlying data structure
        is a tree ordered on key. Otherwise assume a hashtable.
      shapes: (Optional.) Constraints on the shapes of tensors in an element.
        A list of shape tuples or None. This list is the same length
        as dtypes.  If the shape of any tensors in the element are constrained,
        all must be; shapes can be None if the shapes should not be constrained.
      names: (Optional.) If provided, the `get()` and
        `put()` methods will use dictionaries with these names as keys.
        Must be None or a list or tuple of the same length as `dtypes`.
      shared_name: (Optional.) A name to be used for the shared object. By
        passing the same name to two different python objects they will share
        the underlying staging area. Must be a string.

    Raises:
      ValueError: If one of the arguments is invalid.

    """
    def put(self, key, vals, indices: Incomplete | None = None, name: Incomplete | None = None):
        """Create an op that stores the (key, vals) pair in the staging area.

    Incomplete puts are possible, preferably using a dictionary for vals
    as the appropriate dtypes and shapes can be inferred from the value names
    dictionary key values. If vals is a list or tuple, indices must
    also be specified so that the op knows at which element position
    to perform the insert.

    This operation will block if the capacity or memory limit of this
    container is reached.

    Args:
        key: Key associated with the data
        vals: Tensor (or a dict/tuple of Tensors) to place
                into the staging area.
        indices: (Optional) if vals is a tuple/list, this is required.
        name: A name for the operation (optional)

    Returns:
        The created op

    Raises:
        ValueError: If the number or type of inputs don't match the staging
        area.
    """
    def peek(self, key, indices: Incomplete | None = None, name: Incomplete | None = None):
        """Peeks at staging area data associated with the key.

    If the key is not in the staging area, it will block
    until the associated (key, value) is inserted.

    Args:
        key: Key associated with the required data
        indices: Partial list of tensors to retrieve (optional).
                A list of integer or string indices.
                String indices are only valid if the Staging Area
                has names associated with it.
        name: A name for the operation (optional)

    Returns:
        The created op
    """
    def get(self, key: Incomplete | None = None, indices: Incomplete | None = None, name: Incomplete | None = None):
        """If the key is provided, the associated (key, value) is returned from the staging area.

    If the key is not in the staging area, this method will block until
    the associated (key, value) is inserted.
    If no key is provided and the staging area is ordered,
    the (key, value) with the smallest key will be returned.
    Otherwise, a random (key, value) will be returned.

    If the staging area is empty when this operation executes,
    it will block until there is an element to dequeue.

    Args:
        key: Key associated with the required data (Optional)
        indices: Partial list of tensors to retrieve (optional).
                A list of integer or string indices.
                String indices are only valid if the Staging Area
                has names associated with it.
        name: A name for the operation (optional)

    Returns:
        The created op
    """
    def size(self, name: Incomplete | None = None):
        """Returns the number of elements in the staging area.

    Args:
        name: A name for the operation (optional)

    Returns:
        The created op
    """
    def incomplete_size(self, name: Incomplete | None = None):
        """Returns the number of incomplete elements in the staging area.

    Args:
        name: A name for the operation (optional)

    Returns:
        The created op
    """
    def clear(self, name: Incomplete | None = None):
        """Clears the staging area.

    Args:
        name: A name for the operation (optional)

    Returns:
        The created op
    """

class RecordInput:
    """RecordInput asynchronously reads and randomly yields TFRecords.

  A RecordInput Op will continuously read a batch of records asynchronously
  into a buffer of some fixed capacity. It can also asynchronously yield
  random records from this buffer.

  It will not start yielding until at least `buffer_size / 2` elements have been
  placed into the buffer so that sufficient randomization can take place.

  The order the files are read will be shifted each epoch by `shift_amount` so
  that the data is presented in a different order every epoch.
  """
    def __init__(self, file_pattern, batch_size: int = 1, buffer_size: int = 1, parallelism: int = 1, shift_ratio: int = 0, seed: int = 0, name: Incomplete | None = None, batches: Incomplete | None = None, compression_type: Incomplete | None = None) -> None:
        """Constructs a RecordInput Op.

    Args:
      file_pattern: File path to the dataset, possibly containing wildcards.
        All matching files will be iterated over each epoch.
      batch_size: How many records to return at a time.
      buffer_size: The maximum number of records the buffer will contain.
      parallelism: How many reader threads to use for reading from files.
      shift_ratio: What percentage of the total number files to move the start
        file forward by each epoch.
      seed: Specify the random number seed used by generator that randomizes
        records.
      name: Optional name for the operation.
      batches: None by default, creating a single batch op. Otherwise specifies
        how many batches to create, which are returned as a list when
        `get_yield_op()` is called. An example use case is to split processing
        between devices on one computer.
      compression_type: The type of compression for the file. Currently ZLIB and
        GZIP are supported. Defaults to none.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
    def get_yield_op(self):
        """Adds a node that yields a group of records every time it is executed.
    If RecordInput `batches` parameter is not None, it yields a list of
    record batches with the specified `batch_size`.
    """
