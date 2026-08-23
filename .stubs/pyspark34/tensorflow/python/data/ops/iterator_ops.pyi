import abc
from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.checkpoint import saveable_compat as saveable_compat
from tensorflow.python.data.ops import iterator_autograph as iterator_autograph, optional_ops as optional_ops
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, errors as errors, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.trackable import base as trackable
from tensorflow.python.training.saver import BaseSaverBuilder as BaseSaverBuilder
from tensorflow.python.util import deprecation as deprecation, lazy_loader as lazy_loader
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

GET_NEXT_CALL_WARNING_THRESHOLD: int
GET_NEXT_CALL_WARNING_MESSAGE: str
GET_NEXT_CALL_ERROR_THRESHOLD: int
GET_NEXT_CALL_ERROR_MESSAGE: str
GLOBAL_ITERATORS: str
autograph_ctx: Incomplete
type_utils: Incomplete

class Iterator(trackable.Trackable):
    """Represents the state of iterating through a `Dataset`."""
    def __init__(self, iterator_resource, initializer, output_types, output_shapes, output_classes) -> None:
        """Creates a new iterator from the given iterator resource.

    Note: Most users will not call this initializer directly, and will
    instead use `Dataset.make_initializable_iterator()` or
    `Dataset.make_one_shot_iterator()`.

    Args:
      iterator_resource: A `tf.resource` scalar `tf.Tensor` representing the
        iterator.
      initializer: A `tf.Operation` that should be run to initialize this
        iterator.
      output_types: A (nested) structure of `tf.DType` objects corresponding to
        each component of an element of this iterator.
      output_shapes: A (nested) structure of `tf.TensorShape` objects
        corresponding to each component of an element of this iterator.
      output_classes: A (nested) structure of Python `type` objects
        corresponding to each component of an element of this iterator.

    Raises:
      TypeError: If `output_types`, `output_shapes`, or `output_classes` is not
        specified.
    """
    @staticmethod
    def from_structure(output_types, output_shapes: Incomplete | None = None, shared_name: Incomplete | None = None, output_classes: Incomplete | None = None):
        """Creates a new, uninitialized `Iterator` with the given structure.

    This iterator-constructing method can be used to create an iterator that
    is reusable with many different datasets.

    The returned iterator is not bound to a particular dataset, and it has
    no `initializer`. To initialize the iterator, run the operation returned by
    `Iterator.make_initializer(dataset)`.

    The following is an example

    ```python
    iterator = Iterator.from_structure(tf.int64, tf.TensorShape([]))

    dataset_range = Dataset.range(10)
    range_initializer = iterator.make_initializer(dataset_range)

    dataset_evens = dataset_range.filter(lambda x: x % 2 == 0)
    evens_initializer = iterator.make_initializer(dataset_evens)

    # Define a model based on the iterator; in this example, the model_fn
    # is expected to take scalar tf.int64 Tensors as input (see
    # the definition of 'iterator' above).
    prediction, loss = model_fn(iterator.get_next())

    # Train for `num_epochs`, where for each epoch, we first iterate over
    # dataset_range, and then iterate over dataset_evens.
    for _ in range(num_epochs):
      # Initialize the iterator to `dataset_range`
      sess.run(range_initializer)
      while True:
        try:
          pred, loss_val = sess.run([prediction, loss])
        except tf.errors.OutOfRangeError:
          break

      # Initialize the iterator to `dataset_evens`
      sess.run(evens_initializer)
      while True:
        try:
          pred, loss_val = sess.run([prediction, loss])
        except tf.errors.OutOfRangeError:
          break
    ```

    Args:
      output_types: A (nested) structure of `tf.DType` objects corresponding to
        each component of an element of this dataset.
      output_shapes: (Optional.) A (nested) structure of `tf.TensorShape`
        objects corresponding to each component of an element of this dataset.
        If omitted, each component will have an unconstrainted shape.
      shared_name: (Optional.) If non-empty, this iterator will be shared under
        the given name across multiple sessions that share the same devices
        (e.g. when using a remote server).
      output_classes: (Optional.) A (nested) structure of Python `type` objects
        corresponding to each component of an element of this iterator. If
        omitted, each component is assumed to be of type `tf.Tensor`.

    Returns:
      An `Iterator`.

    Raises:
      TypeError: If the structures of `output_shapes` and `output_types` are
        not the same.
    """
    @staticmethod
    def from_string_handle(string_handle, output_types, output_shapes: Incomplete | None = None, output_classes: Incomplete | None = None):
        '''Creates a new, uninitialized `Iterator` based on the given handle.

    This method allows you to define a "feedable" iterator where you can choose
    between concrete iterators by feeding a value in a `tf.Session.run` call.
    In that case, `string_handle` would be a `tf.compat.v1.placeholder`, and you
    would
    feed it with the value of `tf.data.Iterator.string_handle` in each step.

    For example, if you had two iterators that marked the current position in
    a training dataset and a test dataset, you could choose which to use in
    each step as follows:

    ```python
    train_iterator = tf.data.Dataset(...).make_one_shot_iterator()
    train_iterator_handle = sess.run(train_iterator.string_handle())

    test_iterator = tf.data.Dataset(...).make_one_shot_iterator()
    test_iterator_handle = sess.run(test_iterator.string_handle())

    handle = tf.compat.v1.placeholder(tf.string, shape=[])
    iterator = tf.data.Iterator.from_string_handle(
        handle, train_iterator.output_types)

    next_element = iterator.get_next()
    loss = f(next_element)

    train_loss = sess.run(loss, feed_dict={handle: train_iterator_handle})
    test_loss = sess.run(loss, feed_dict={handle: test_iterator_handle})
    ```

    Args:
      string_handle: A scalar `tf.Tensor` of type `tf.string` that evaluates to
        a handle produced by the `Iterator.string_handle()` method.
      output_types: A (nested) structure of `tf.DType` objects corresponding to
        each component of an element of this dataset.
      output_shapes: (Optional.) A (nested) structure of `tf.TensorShape`
        objects corresponding to each component of an element of this dataset.
        If omitted, each component will have an unconstrainted shape.
      output_classes: (Optional.) A (nested) structure of Python `type` objects
        corresponding to each component of an element of this iterator. If
        omitted, each component is assumed to be of type `tf.Tensor`.

    Returns:
      An `Iterator`.
    '''
    @property
    def initializer(self):
        """A `tf.Operation` that should be run to initialize this iterator.

    Returns:
      A `tf.Operation` that should be run to initialize this iterator

    Raises:
      ValueError: If this iterator initializes itself automatically.
    """
    def make_initializer(self, dataset, name: Incomplete | None = None):
        """Returns a `tf.Operation` that initializes this iterator on `dataset`.

    Args:
      dataset: A `Dataset` whose `element_spec` if compatible with this
        iterator.
      name: (Optional.) A name for the created operation.

    Returns:
      A `tf.Operation` that can be run to initialize this iterator on the given
      `dataset`.

    Raises:
      TypeError: If `dataset` and this iterator do not have a compatible
        `element_spec`.
    """
    def get_next(self, name: Incomplete | None = None):
        """Returns the next element.

    In graph mode, you should typically call this method *once* and use its
    result as the input to another computation. A typical loop will then call
    `tf.Session.run` on the result of that computation. The loop will terminate
    when the `Iterator.get_next()` operation raises
    `tf.errors.OutOfRangeError`. The following skeleton shows how to use
    this method when building a training loop:

    ```python
    dataset = ...  # A `tf.data.Dataset` object.
    iterator = dataset.make_initializable_iterator()
    next_element = iterator.get_next()

    # Build a TensorFlow graph that does something with each element.
    loss = model_function(next_element)
    optimizer = ...  # A `tf.compat.v1.train.Optimizer` object.
    train_op = optimizer.minimize(loss)

    with tf.compat.v1.Session() as sess:
      try:
        while True:
          sess.run(train_op)
      except tf.errors.OutOfRangeError:
        pass
    ```

    NOTE: It is legitimate to call `Iterator.get_next()` multiple times, e.g.
    when you are distributing different elements to multiple devices in a single
    step. However, a common pitfall arises when users call `Iterator.get_next()`
    in each iteration of their training loop. `Iterator.get_next()` adds ops to
    the graph, and executing each op allocates resources (including threads); as
    a consequence, invoking it in every iteration of a training loop causes
    slowdown and eventual resource exhaustion. To guard against this outcome, we
    log a warning when the number of uses crosses a fixed threshold of
    suspiciousness.

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      A (nested) structure of values matching `tf.data.Iterator.element_spec`.
    """
    def get_next_as_optional(self): ...
    def string_handle(self, name: Incomplete | None = None):
        """Returns a string-valued `tf.Tensor` that represents this iterator.

    Args:
      name: (Optional.) A name for the created operation.

    Returns:
      A scalar `tf.Tensor` of type `tf.string`.
    """
    @property
    def output_classes(self):
        """Returns the class of each component of an element of this iterator.

    The expected values are `tf.Tensor` and `tf.sparse.SparseTensor`.

    Returns:
      A (nested) structure of Python `type` objects corresponding to each
      component of an element of this dataset.
    """
    @property
    def output_shapes(self):
        """Returns the shape of each component of an element of this iterator.

    Returns:
      A (nested) structure of `tf.TensorShape` objects corresponding to each
      component of an element of this dataset.
    """
    @property
    def output_types(self):
        """Returns the type of each component of an element of this iterator.

    Returns:
      A (nested) structure of `tf.DType` objects corresponding to each component
      of an element of this dataset.
    """
    @property
    def element_spec(self):
        """The type specification of an element of this iterator.

    For more information,
    read [this guide](https://www.tensorflow.org/guide/data#dataset_structure).

    Returns:
      A (nested) structure of `tf.TypeSpec` objects matching the structure of an
      element of this iterator and specifying the type of individual components.
    """

class IteratorBase(collections_abc.Iterator, trackable.Trackable, composite_tensor.CompositeTensor, metaclass=abc.ABCMeta):
    """Represents an iterator of a `tf.data.Dataset`.

  `tf.data.Iterator` is the primary mechanism for enumerating elements of a
  `tf.data.Dataset`. It supports the Python Iterator protocol, which means
  it can be iterated over using a for-loop:

  >>> dataset = tf.data.Dataset.range(2)
  >>> for element in dataset:
  ...   print(element)
  tf.Tensor(0, shape=(), dtype=int64)
  tf.Tensor(1, shape=(), dtype=int64)

  or by fetching individual elements explicitly via `get_next()`:

  >>> dataset = tf.data.Dataset.range(2)
  >>> iterator = iter(dataset)
  >>> print(iterator.get_next())
  tf.Tensor(0, shape=(), dtype=int64)
  >>> print(iterator.get_next())
  tf.Tensor(1, shape=(), dtype=int64)

  In addition, non-raising iteration is supported via `get_next_as_optional()`,
  which returns the next element (if available) wrapped in a
  `tf.experimental.Optional`.

  >>> dataset = tf.data.Dataset.from_tensors(42)
  >>> iterator = iter(dataset)
  >>> optional = iterator.get_next_as_optional()
  >>> print(optional.has_value())
  tf.Tensor(True, shape=(), dtype=bool)
  >>> optional = iterator.get_next_as_optional()
  >>> print(optional.has_value())
  tf.Tensor(False, shape=(), dtype=bool)
  """
    @property
    @abc.abstractmethod
    def element_spec(self):
        """The type specification of an element of this iterator.

    >>> dataset = tf.data.Dataset.from_tensors(42)
    >>> iterator = iter(dataset)
    >>> iterator.element_spec
    tf.TensorSpec(shape=(), dtype=tf.int32, name=None)

    For more information,
    read [this guide](https://www.tensorflow.org/guide/data#dataset_structure).

    Returns:
      A (nested) structure of `tf.TypeSpec` objects matching the structure of an
      element of this iterator, specifying the type of individual components.
    """
    @abc.abstractmethod
    def get_next(self):
        """Returns the next element.

    >>> dataset = tf.data.Dataset.from_tensors(42)
    >>> iterator = iter(dataset)
    >>> print(iterator.get_next())
    tf.Tensor(42, shape=(), dtype=int32)

    Returns:
      A (nested) structure of values matching `tf.data.Iterator.element_spec`.

    Raises:
      `tf.errors.OutOfRangeError`: If the end of the iterator has been reached.
    """
    @abc.abstractmethod
    def get_next_as_optional(self):
        """Returns the next element wrapped in `tf.experimental.Optional`.

    If the iterator has reached the end of the sequence, the returned
    `tf.experimental.Optional` will have no value.

    >>> dataset = tf.data.Dataset.from_tensors(42)
    >>> iterator = iter(dataset)
    >>> optional = iterator.get_next_as_optional()
    >>> print(optional.has_value())
    tf.Tensor(True, shape=(), dtype=bool)
    >>> print(optional.get_value())
    tf.Tensor(42, shape=(), dtype=int32)
    >>> optional = iterator.get_next_as_optional()
    >>> print(optional.has_value())
    tf.Tensor(False, shape=(), dtype=bool)

    Returns:
      A `tf.experimental.Optional` object representing the next element.
    """

class OwnedIterator(IteratorBase):
    """An iterator producing tf.Tensor objects from a tf.data.Dataset.

  The iterator resource  created through `OwnedIterator` is owned by the Python
  object and the life time of the underlying resource is tied to the life time
  of the `OwnedIterator` object. This makes `OwnedIterator` appropriate for use
  in eager mode and inside of tf.functions.
  """
    def __init__(self, dataset: Incomplete | None = None, components: Incomplete | None = None, element_spec: Incomplete | None = None) -> None:
        """Creates a new iterator from the given dataset.

    If `dataset` is not specified, the iterator will be created from the given
    tensor components and element structure. In particular, the alternative for
    constructing the iterator is used when the iterator is reconstructed from
    it `CompositeTensor` representation.

    Args:
      dataset: A `tf.data.Dataset` object.
      components: Tensor components to construct the iterator from.
      element_spec: A (nested) structure of `TypeSpec` objects that
        represents the type specification of elements of the iterator.

    Raises:
      ValueError: If `dataset` is not provided and either `components` or
        `element_spec` is not provided. Or `dataset` is provided and either
        `components` and `element_spec` is provided.
    """
    def __iter__(self): ...
    def next(self): ...
    def __next__(self): ...
    @property
    def output_classes(self):
        """Returns the class of each component of an element of this iterator.

    The expected values are `tf.Tensor` and `tf.sparse.SparseTensor`.

    Returns:
      A (nested) structure of Python `type` objects corresponding to each
      component of an element of this dataset.
    """
    @property
    def output_shapes(self):
        """Returns the shape of each component of an element of this iterator.

    Returns:
      A (nested) structure of `tf.TensorShape` objects corresponding to each
      component of an element of this dataset.
    """
    @property
    def output_types(self):
        """Returns the type of each component of an element of this iterator.

    Returns:
      A (nested) structure of `tf.DType` objects corresponding to each component
      of an element of this dataset.
    """
    @property
    def element_spec(self): ...
    def get_next(self): ...
    def get_next_as_optional(self): ...
    def __tf_tracing_type__(self, _): ...

class IteratorSpec(type_spec.TypeSpec):
    """Type specification for `tf.data.Iterator`.

  For instance, `tf.data.IteratorSpec` can be used to define a tf.function that
  takes `tf.data.Iterator` as an input argument:

  >>> @tf.function(input_signature=[tf.data.IteratorSpec(
  ...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))])
  ... def square(iterator):
  ...   x = iterator.get_next()
  ...   return x * x
  >>> dataset = tf.data.Dataset.from_tensors(5)
  >>> iterator = iter(dataset)
  >>> print(square(iterator))
  tf.Tensor(25, shape=(), dtype=int32)

  Attributes:
    element_spec: A (nested) structure of `tf.TypeSpec` objects that represents
      the type specification of the iterator elements.
  """
    def __init__(self, element_spec) -> None: ...
    @property
    def value_type(self): ...
    @staticmethod
    def from_value(value): ...

class _IteratorSaveable(BaseSaverBuilder.SaveableObject):
    """SaveableObject for saving/restoring iterator state."""
    def __init__(self, iterator_resource, name, external_state_policy=...) -> None: ...
    def restore(self, restored_tensors, restored_shapes): ...

def get_next_as_optional(iterator):
    """Returns a `tf.experimental.Optional` with the next element of the iterator.

  If the iterator has reached the end of the sequence, the returned
  `tf.experimental.Optional` will have no value.

  Args:
    iterator: A `tf.data.Iterator`.

  Returns:
    A `tf.experimental.Optional` object which either contains the next element
    of the iterator (if it exists) or no value.
  """
