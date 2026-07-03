from _typeshed import Incomplete
from tensorflow.core.framework import tensor_shape_pb2 as tensor_shape_pb2
from tensorflow.core.function import trace_type as trace_type
from tensorflow.python import tf2 as tf2
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.types import trace as trace
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Optional, Sequence, Type

def enable_v2_tensorshape() -> None:
    """In TensorFlow 2.0, iterating over a TensorShape instance returns values.

  This enables the new behavior.

  Concretely, `tensor_shape[i]` returned a Dimension instance in V1, but
  it V2 it returns either an integer, or None.

  Examples:

  ```
  #######################
  # If you had this in V1:
  value = tensor_shape[i].value

  # Do this in V2 instead:
  value = tensor_shape[i]

  #######################
  # If you had this in V1:
  for dim in tensor_shape:
    value = dim.value
    print(value)

  # Do this in V2 instead:
  for value in tensor_shape:
    print(value)

  #######################
  # If you had this in V1:
  dim = tensor_shape[i]
  dim.assert_is_compatible_with(other_shape)  # or using any other shape method

  # Do this in V2 instead:
  if tensor_shape.rank is None:
    dim = Dimension(None)
  else:
    dim = tensor_shape.dims[i]
  dim.assert_is_compatible_with(other_shape)  # or using any other shape method

  # The V2 suggestion above is more explicit, which will save you from
  # the following trap (present in V1):
  # you might do in-place modifications to `dim` and expect them to be reflected
  # in `tensor_shape[i]`, but they would not be.
  ```
  """
def disable_v2_tensorshape() -> None:
    """Disables the V2 TensorShape behavior and reverts to V1 behavior.

  See docstring for `enable_v2_tensorshape` for details about the new behavior.
  """
def dimension_value(dimension):
    """Compatibility utility required to allow for both V1 and V2 behavior in TF.

  Until the release of TF 2.0, we need the legacy behavior of `TensorShape` to
  coexist with the new behavior. This utility is a bridge between the two.

  When accessing the value of a TensorShape dimension,
  use this utility, like this:

  ```
  # If you had this in your V1 code:
  value = tensor_shape[i].value

  # Use `dimension_value` as direct replacement compatible with both V1 & V2:
  value = dimension_value(tensor_shape[i])

  # This would be the V2 equivalent:
  value = tensor_shape[i]  # Warning: this will return the dim value in V2!
  ```

  Args:
    dimension: Either a `Dimension` instance, an integer, or None.

  Returns:
    A plain value, i.e. an integer or None.
  """
def dimension_at_index(shape, index):
    """Compatibility utility required to allow for both V1 and V2 behavior in TF.

  Until the release of TF 2.0, we need the legacy behavior of `TensorShape` to
  coexist with the new behavior. This utility is a bridge between the two.

  If you want to retrieve the Dimension instance corresponding to a certain
  index in a TensorShape instance, use this utility, like this:

  ```
  # If you had this in your V1 code:
  dim = tensor_shape[i]

  # Use `dimension_at_index` as direct replacement compatible with both V1 & V2:
  dim = dimension_at_index(tensor_shape, i)

  # Another possibility would be this, but WARNING: it only works if the
  # tensor_shape instance has a defined rank.
  dim = tensor_shape.dims[i]  # `dims` may be None if the rank is undefined!

  # In native V2 code, we recommend instead being more explicit:
  if tensor_shape.rank is None:
    dim = Dimension(None)
  else:
    dim = tensor_shape.dims[i]

  # Being more explicit will save you from the following trap (present in V1):
  # you might do in-place modifications to `dim` and expect them to be reflected
  # in `tensor_shape[i]`, but they would not be (as the Dimension object was
  # instantiated on the fly.
  ```

  Args:
    shape: A TensorShape instance.
    index: An integer index.

  Returns:
    A dimension object.
  """

class Dimension:
    """Represents the value of one dimension in a TensorShape.

  @compatibility(TF2)
  In TF2, members of a `TensorShape` object are integers. The `Dimension` class
  is not part of TF2's data model.

  Please refer to the [TensorShape section of the migration guide]
  (https://www.tensorflow.org/guide/migrate/index#tensorshape) on common code
  patterns adapting Dimension objects to a TF2 syntax.
  @end_compatibility
  """
    def __init__(self, value) -> None:
        """Creates a new Dimension with the given value."""
    def __eq__(self, other):
        """Returns true if `other` has the same known value as this Dimension."""
    def __ne__(self, other):
        """Returns true if `other` has a different known value from `self`."""
    def __bool__(self) -> bool:
        """Equivalent to `bool(self.value)`."""
    def __int__(self) -> int: ...
    def __long__(self): ...
    def __index__(self) -> int: ...
    @property
    def value(self):
        """The value of this dimension, or None if it is unknown."""
    def is_compatible_with(self, other):
        """Returns true if `other` is compatible with this Dimension.

    Two known Dimensions are compatible if they have the same value.
    An unknown Dimension is compatible with all other Dimensions.

    Args:
      other: Another Dimension.

    Returns:
      True if this Dimension and `other` are compatible.
    """
    def assert_is_compatible_with(self, other) -> None:
        """Raises an exception if `other` is not compatible with this Dimension.

    Args:
      other: Another Dimension.

    Raises:
      ValueError: If `self` and `other` are not compatible (see
        is_compatible_with).
    """
    def merge_with(self, other):
        """Returns a Dimension that combines the information in `self` and `other`.

    Dimensions are combined as follows:

    ```python
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(n))     ==
    tf.compat.v1.Dimension(n)
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(None))  ==
    tf.compat.v1.Dimension(n)
    tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(n))     ==
    tf.compat.v1.Dimension(n)
    # equivalent to tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None).merge_with(tf.compat.v1.Dimension(None))

    # raises ValueError for n != m
    tf.compat.v1.Dimension(n)   .merge_with(tf.compat.v1.Dimension(m))
    ```

    Args:
      other: Another Dimension.

    Returns:
      A Dimension containing the combined information of `self` and
      `other`.

    Raises:
      ValueError: If `self` and `other` are not compatible (see
        is_compatible_with).
    """
    def __add__(self, other):
        """Returns the sum of `self` and `other`.

    Dimensions are summed as follows:

    ```python
    tf.compat.v1.Dimension(m)    + tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m + n)
    tf.compat.v1.Dimension(m)    + tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) + tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) + tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    ```

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is the sum of `self` and `other`.
    """
    def __radd__(self, other):
        """Returns the sum of `other` and `self`.

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is the sum of `self` and `other`.
    """
    def __sub__(self, other):
        """Returns the subtraction of `other` from `self`.

    Dimensions are subtracted as follows:

    ```python
    tf.compat.v1.Dimension(m)    - tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m - n)
    tf.compat.v1.Dimension(m)    - tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) - tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) - tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    ```

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is the subtraction of `other` from `self`.
    """
    def __rsub__(self, other):
        """Returns the subtraction of `self` from `other`.

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is the subtraction of `self` from `other`.
    """
    def __mul__(self, other):
        """Returns the product of `self` and `other`.

    Dimensions are summed as follows:

    ```python
    tf.compat.v1.Dimension(m)    * tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m * n)
    tf.compat.v1.Dimension(m)    * tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) * tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) * tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    ```

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is the product of `self` and `other`.
    """
    def __rmul__(self, other):
        """Returns the product of `self` and `other`.

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is the product of `self` and `other`.
    """
    def __floordiv__(self, other):
        """Returns the quotient of `self` and `other` rounded down.

    Dimensions are divided as follows:

    ```python
    tf.compat.v1.Dimension(m)    // tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m // n)
    tf.compat.v1.Dimension(m)    // tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) // tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) // tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    ```

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A `Dimension` whose value is the integer quotient of `self` and `other`.
    """
    def __rfloordiv__(self, other):
        """Returns the quotient of `other` and `self` rounded down.

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A `Dimension` whose value is the integer quotient of `self` and `other`.
    """
    def __div__(self, other):
        """DEPRECATED: Use `__floordiv__` via `x // y` instead.

    This function exists only for backwards compatibility purposes; new code
    should use `__floordiv__` via the syntax `x // y`.  Using `x // y`
    communicates clearly that the result rounds down, and is forward compatible
    to Python 3.

    Args:
      other: Another `Dimension`.

    Returns:
      A `Dimension` whose value is the integer quotient of `self` and `other`.
    """
    def __rdiv__(self, other) -> None:
        """Use `__floordiv__` via `x // y` instead.

    This function exists only to have a better error message. Instead of:
    `TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`,
    this function will explicitly call for usage of `//` instead.

    Args:
      other: Another `Dimension`.

    Raises:
      TypeError.
    """
    def __truediv__(self, other) -> None:
        """Use `__floordiv__` via `x // y` instead.

    This function exists only to have a better error message. Instead of:
    `TypeError: unsupported operand type(s) for /: 'Dimension' and 'int'`,
    this function will explicitly call for usage of `//` instead.

    Args:
      other: Another `Dimension`.

    Raises:
      TypeError.
    """
    def __rtruediv__(self, other) -> None:
        """Use `__floordiv__` via `x // y` instead.

    This function exists only to have a better error message. Instead of:
    `TypeError: unsupported operand type(s) for /: 'int' and 'Dimension'`,
    this function will explicitly call for usage of `//` instead.

    Args:
      other: Another `Dimension`.

    Raises:
      TypeError.
    """
    def __mod__(self, other):
        """Returns `self` modulo `other`.

    Dimension modulo are computed as follows:

    ```python
    tf.compat.v1.Dimension(m)    % tf.compat.v1.Dimension(n)     ==
    tf.compat.v1.Dimension(m % n)
    tf.compat.v1.Dimension(m)    % tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) % tf.compat.v1.Dimension(n)     # equiv. to
    tf.compat.v1.Dimension(None)
    tf.compat.v1.Dimension(None) % tf.compat.v1.Dimension(None)  # equiv. to
    tf.compat.v1.Dimension(None)
    ```

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is `self` modulo `other`.
    """
    def __rmod__(self, other):
        """Returns `other` modulo `self`.

    Args:
      other: Another Dimension, or a value accepted by `as_dimension`.

    Returns:
      A Dimension whose value is `other` modulo `self`.
    """
    def __lt__(self, other):
        """Returns True if `self` is known to be less than `other`.

    Dimensions are compared as follows:

    ```python
    (tf.compat.v1.Dimension(m)    < tf.compat.v1.Dimension(n))    == (m < n)
    (tf.compat.v1.Dimension(m)    < tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) < tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) < tf.compat.v1.Dimension(None)) == None
    ```

    Args:
      other: Another Dimension.

    Returns:
      The value of `self.value < other.value` if both are known, otherwise
      None.
    """
    def __le__(self, other):
        """Returns True if `self` is known to be less than or equal to `other`.

    Dimensions are compared as follows:

    ```python
    (tf.compat.v1.Dimension(m)    <= tf.compat.v1.Dimension(n))    == (m <= n)
    (tf.compat.v1.Dimension(m)    <= tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) <= tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) <= tf.compat.v1.Dimension(None)) == None
    ```

    Args:
      other: Another Dimension.

    Returns:
      The value of `self.value <= other.value` if both are known, otherwise
      None.
    """
    def __gt__(self, other):
        """Returns True if `self` is known to be greater than `other`.

    Dimensions are compared as follows:

    ```python
    (tf.compat.v1.Dimension(m)    > tf.compat.v1.Dimension(n))    == (m > n)
    (tf.compat.v1.Dimension(m)    > tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) > tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) > tf.compat.v1.Dimension(None)) == None
    ```

    Args:
      other: Another Dimension.

    Returns:
      The value of `self.value > other.value` if both are known, otherwise
      None.
    """
    def __ge__(self, other):
        """Returns True if `self` is known to be greater than or equal to `other`.

    Dimensions are compared as follows:

    ```python
    (tf.compat.v1.Dimension(m)    >= tf.compat.v1.Dimension(n))    == (m >= n)
    (tf.compat.v1.Dimension(m)    >= tf.compat.v1.Dimension(None)) == None
    (tf.compat.v1.Dimension(None) >= tf.compat.v1.Dimension(n))    == None
    (tf.compat.v1.Dimension(None) >= tf.compat.v1.Dimension(None)) == None
    ```

    Args:
      other: Another Dimension.

    Returns:
      The value of `self.value >= other.value` if both are known, otherwise
      None.
    """
    def __reduce__(self): ...

def as_dimension(value):
    """Converts the given value to a Dimension.

  A Dimension input will be returned unmodified.
  An input of `None` will be converted to an unknown Dimension.
  An integer input will be converted to a Dimension with that value.

  Args:
    value: The value to be converted.

  Returns:
    A Dimension corresponding to the given value.
  """

class TensorShape(trace.TraceType, trace_type.Serializable):
    '''Represents the shape of a `Tensor`.

  >>> t = tf.constant([[1,2,3],[4,5,6]])
  >>> t.shape
  TensorShape([2, 3])

  `TensorShape` is the *static* shape representation of a Tensor.
  During eager execution a Tensor always has a fully specified shape but
  when tracing a `tf.function` it may be one of the following:

  * *Fully-known shape:* has a known number of dimensions and a known size
    for each dimension. e.g. `TensorShape([16, 256])`
  * *Partially-known shape:* has a known number of dimensions, and an unknown
    size for one or more dimension. e.g. `TensorShape([None, 256])`
  * *Unknown shape:* has an unknown number of dimensions, and an unknown
    size in all dimensions. e.g. `TensorShape(None)`

  During function tracing `t.shape` will return a `TensorShape` object
  representing the shape of Tensor as it is known during tracing.
  This static representation will be partially defined in cases where the
  exact shape depends on the values within the tensors. To get the
  *dynamic* representation, please use `tf.shape(t)`
  which will return Tensor representing the fully defined shape of `t`.
  This way, you can express logic that manipulates the shapes of tensors by
  building other tensors that depend on the dynamic shape of `t`.

  Note: `tf.RaggedTensor.shape` also returns a `tf.TensorShape`,
  the lengths of any ragged dimensions are unknown (`None`).

  For example, this function prints the `TensorShape\' (`t.shape`), when you
  trace the function, and returns a tensor `tf.shape(t)` for given input `t`:

  >>> @tf.function
  ... def get_dynamic_shape(t):
  ...   print("tracing...")
  ...   print(f"static shape is {t.shape}")
  ...   return tf.shape(t)

  Just calling the function traces it with a fully-specified static shape:

  >>> result = get_dynamic_shape(tf.constant([[1, 1, 1], [0, 0, 0]]))
  tracing...
  static shape is (2, 3)
  >>> result.numpy()
  array([2, 3], dtype=int32)

  But `tf.function` can also trace the function with a partially specified
  (or even unspecified) shape:

  >>> cf1 = get_dynamic_shape.get_concrete_function(tf.TensorSpec(
  ...                                               shape=[None, 2]))
  tracing...
  static shape is (None, 2)
  >>> cf1(tf.constant([[1., 0],[1, 0],[1, 0]])).numpy()
  array([3, 2], dtype=int32)

  >>> cf2 = get_dynamic_shape.get_concrete_function(tf.TensorSpec(shape=None))
  tracing...
  static shape is <unknown>
  >>> cf2(tf.constant([[[[[1., 0]]]]])).numpy()
  array([1, 1, 1, 1, 2], dtype=int32)

  If a tensor is produced by an operation of type `"Foo"`, its shape
  may be inferred if there is a registered shape function for
  `"Foo"`. See [Shape
  functions](https://www.tensorflow.org/guide/create_op#shape_functions_in_c)
  for details of shape functions and how to register them. Alternatively,
  you may set the shape explicitly using `tf.Tensor.ensure_shape`.
  '''
    def __init__(self, dims) -> None:
        """Creates a new TensorShape with the given dimensions.

    Args:
      dims: A list of Dimensions, or None if the shape is unspecified.

    Raises:
      TypeError: If dims cannot be converted to a list of dimensions.
    """
    @property
    def rank(self):
        """Returns the rank of this shape, or None if it is unspecified."""
    @property
    def dims(self):
        """Deprecated.  Returns list of dimensions for this shape.

    Suggest `TensorShape.as_list` instead.

    Returns:
      A list containing `tf.compat.v1.Dimension`s, or None if the shape is
      unspecified.
    """
    @property
    def ndims(self):
        """Deprecated accessor for `rank`."""
    def __len__(self) -> int:
        """Returns the rank of this shape, or raises ValueError if unspecified."""
    def __bool__(self) -> bool:
        """Returns True if this shape contains non-zero information."""
    __nonzero__ = __bool__
    def __iter__(self):
        """Returns `self.dims` if the rank is known, otherwise raises ValueError."""
    def __getitem__(self, key):
        """Returns the value of a dimension or a shape, depending on the key.

    Args:
      key: If `key` is an integer, returns the dimension at that index;
        otherwise if `key` is a slice, returns a TensorShape whose dimensions
        are those selected by the slice from `self`.

    Returns:
      An integer if `key` is an integer, or a `TensorShape` if `key` is a
      slice.

    Raises:
      ValueError: If `key` is a slice and `self` is completely unknown and
        the step is set.
    """
    def num_elements(self):
        """Returns the total number of elements, or none for incomplete shapes."""
    def merge_with(self, other):
        """Returns a `TensorShape` combining the information in `self` and `other`.

    The dimensions in `self` and `other` are merged element-wise,
    according to the rules below:

    ```python
    Dimension(n).merge_with(Dimension(None)) == Dimension(n)
    Dimension(None).merge_with(Dimension(n)) == Dimension(n)
    Dimension(None).merge_with(Dimension(None)) == Dimension(None)
    # raises ValueError for n != m
    Dimension(n).merge_with(Dimension(m))
    ```
    >> ts = tf.TensorShape([1,2])
    >> ot1 = tf.TensorShape([1,2])
    >> ts.merge_with(ot).as_list()
    [1,2]

    >> ot2 = tf.TensorShape([1,None])
    >> ts.merge_with(ot2).as_list()
    [1,2]

    >> ot3 = tf.TensorShape([None, None])
    >> ot3.merge_with(ot2).as_list()
    [1, None]

    Args:
      other: Another `TensorShape`.

    Returns:
      A `TensorShape` containing the combined information of `self` and
      `other`.

    Raises:
      ValueError: If `self` and `other` are not compatible.
    """
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def concatenate(self, other):
        """Returns the concatenation of the dimension in `self` and `other`.

    *N.B.* If either `self` or `other` is completely unknown,
    concatenation will discard information about the other shape. In
    future, we might support concatenation that preserves this
    information for use with slicing.

    Args:
      other: Another `TensorShape`.

    Returns:
      A `TensorShape` whose dimensions are the concatenation of the
      dimensions in `self` and `other`.
    """
    def assert_same_rank(self, other) -> None:
        """Raises an exception if `self` and `other` do not have compatible ranks.

    Args:
      other: Another `TensorShape`.

    Raises:
      ValueError: If `self` and `other` do not represent shapes with the
        same rank.
    """
    def assert_has_rank(self, rank) -> None:
        """Raises an exception if `self` is not compatible with the given `rank`.

    Args:
      rank: An integer.

    Raises:
      ValueError: If `self` does not represent a shape with the given `rank`.
    """
    def with_rank(self, rank):
        """Returns a shape based on `self` with the given rank.

    This method promotes a completely unknown shape to one with a
    known rank.

    Args:
      rank: An integer.

    Returns:
      A shape that is at least as specific as `self` with the given rank.

    Raises:
      ValueError: If `self` does not represent a shape with the given `rank`.
    """
    def with_rank_at_least(self, rank):
        """Returns a shape based on `self` with at least the given rank.

    Args:
      rank: An integer.

    Returns:
      A shape that is at least as specific as `self` with at least the given
      rank.

    Raises:
      ValueError: If `self` does not represent a shape with at least the given
        `rank`.
    """
    def with_rank_at_most(self, rank):
        """Returns a shape based on `self` with at most the given rank.

    Args:
      rank: An integer.

    Returns:
      A shape that is at least as specific as `self` with at most the given
      rank.

    Raises:
      ValueError: If `self` does not represent a shape with at most the given
        `rank`.
    """
    def is_subtype_of(self, other: trace.TraceType) -> bool:
        """Returns True iff `self` is subtype of `other`.

    Shape A is a subtype of shape B if shape B can successfully represent it:

    * A `TensorShape` of any rank is a subtype of `TensorShape(None)`.

    *  TensorShapes of equal ranks are covariant, i.e.
      `TensorShape([A1, A2, ..])` is a subtype of
      `TensorShape([B1, B2, ..])` iff An is a subtype of Bn.

      An is subtype of Bn iff An == Bn or Bn is None.

    * TensorShapes of different defined ranks have no subtyping relation.

    The subtyping relation is reflexive and transitive, but not symmetric.

    Some examples:
    * `TensorShape([32, 784])` is a subtype of `TensorShape(None)`, and
      `TensorShape([4, 4])` is also a subtype of `TensorShape(None)` but
      `TensorShape([32, 784])` and `TensorShape([4, 4])` are not subtypes of
      each other.

    * All two-dimensional shapes are subtypes of `TensorShape([None, None])`,
      such as `TensorShape([32, 784])`. There is no subtype relationship with,
      for example, `TensorShape([None])` or `TensorShape([None, None, None])`.

    * `TensorShape([32, None])` is also a subtype of `TensorShape([None, None])`
      and `TensorShape(None)`. It is not a subtype of, for example,
      `TensorShape([32])`, `TensorShape([32, None, 1])`,
      `TensorShape([64, None])` or `TensorShape([None, 32])`.

    * `TensorShape([32, 784])` is a subtype of itself, and also
      `TensorShape([32, None])`, `TensorShape([None, 784])`,
      `TensorShape([None, None])` and `TensorShape(None)`.
      It has no subtype relation with, for example, `TensorShape([32, 1, 784])`
      or `TensorShape([None])`.

    Args:
      other: Another `TensorShape`.

    Returns:
      True iff `self` is subtype of `other`.

    """
    def most_specific_common_supertype(self, others: Sequence[trace.TraceType]) -> Optional['TensorShape']:
        '''Returns the most specific supertype `TensorShape` of self and others.

    * `TensorShape([None, 1])` is the most specific `TensorShape` supertyping
      both `TensorShape([2, 1])` and `TensorShape([5, 1])`. Note that
      `TensorShape(None)` is also a supertype but it is not "most specific".

    * `TensorShape([1, 2, 3])` is the most specific `TensorShape` supertyping
      both `TensorShape([1, 2, 3])` and `TensorShape([1, 2, 3]`). There are
      other less specific TensorShapes that supertype above mentioned
      TensorShapes, e.g. `TensorShape([1, 2, None])`, `TensorShape(None)`.

     * `TensorShape([None, None])` is the most specific `TensorShape`
       supertyping both `TensorShape([2, None])` and `TensorShape([None, 3])`.
       As always, `TensorShape(None)` is also a supertype but not the most
       specific one.

     * `TensorShape(None`) is the only `TensorShape` supertyping both
       `TensorShape([1, 2, 3])` and `TensorShape([1, 2])`. In general, any two
       shapes that have different ranks will only have `TensorShape(None)`
       as a common supertype.

     * `TensorShape(None)` is the only `TensorShape` supertyping both
       `TensorShape([1, 2, 3])` and `TensorShape(None)`. In general, the common
       supertype of any shape with `TensorShape(None)` is `TensorShape(None)`.

    Args:
      others: Sequence of `TensorShape`.

    Returns:
      A `TensorShape` which is the most specific supertype shape of `self`
      and `others`. None if it does not exist.
    '''
    def placeholder_value(self, placeholder_context: Incomplete | None = None) -> None: ...
    @classmethod
    def experimental_type_proto(cls) -> Type[tensor_shape_pb2.TensorShapeProto]:
        """Returns the type of proto associated with TensorShape serialization."""
    @classmethod
    def experimental_from_proto(cls, proto: tensor_shape_pb2.TensorShapeProto) -> TensorShape:
        """Returns a TensorShape instance based on the serialized proto."""
    def experimental_as_proto(self) -> tensor_shape_pb2.TensorShapeProto:
        """Returns a proto representation of the TensorShape instance."""
    def is_compatible_with(self, other):
        """Returns True iff `self` is compatible with `other`.

    Two possibly-partially-defined shapes are compatible if there
    exists a fully-defined shape that both shapes can represent. Thus,
    compatibility allows the shape inference code to reason about
    partially-defined shapes. For example:

    * TensorShape(None) is compatible with all shapes.

    * TensorShape([None, None]) is compatible with all two-dimensional
      shapes, such as TensorShape([32, 784]), and also TensorShape(None). It is
      not compatible with, for example, TensorShape([None]) or
      TensorShape([None, None, None]).

    * TensorShape([32, None]) is compatible with all two-dimensional shapes
      with size 32 in the 0th dimension, and also TensorShape([None, None])
      and TensorShape(None). It is not compatible with, for example,
      TensorShape([32]), TensorShape([32, None, 1]) or TensorShape([64, None]).

    * TensorShape([32, 784]) is compatible with itself, and also
      TensorShape([32, None]), TensorShape([None, 784]), TensorShape([None,
      None]) and TensorShape(None). It is not compatible with, for example,
      TensorShape([32, 1, 784]) or TensorShape([None]).

    The compatibility relation is reflexive and symmetric, but not
    transitive. For example, TensorShape([32, 784]) is compatible with
    TensorShape(None), and TensorShape(None) is compatible with
    TensorShape([4, 4]), but TensorShape([32, 784]) is not compatible with
    TensorShape([4, 4]).

    Args:
      other: Another TensorShape.

    Returns:
      True iff `self` is compatible with `other`.

    """
    def assert_is_compatible_with(self, other) -> None:
        """Raises exception if `self` and `other` do not represent the same shape.

    This method can be used to assert that there exists a shape that both
    `self` and `other` represent.

    Args:
      other: Another TensorShape.

    Raises:
      ValueError: If `self` and `other` do not represent the same shape.
    """
    def most_specific_compatible_shape(self, other):
        """Returns the most specific TensorShape compatible with `self` and `other`.

    * TensorShape([None, 1]) is the most specific TensorShape compatible with
      both TensorShape([2, 1]) and TensorShape([5, 1]). Note that
      TensorShape(None) is also compatible with above mentioned TensorShapes.

    * TensorShape([1, 2, 3]) is the most specific TensorShape compatible with
      both TensorShape([1, 2, 3]) and TensorShape([1, 2, 3]). There are more
      less specific TensorShapes compatible with above mentioned TensorShapes,
      e.g. TensorShape([1, 2, None]), TensorShape(None).

    Args:
      other: Another `TensorShape`.

    Returns:
      A `TensorShape` which is the most specific compatible shape of `self`
      and `other`.
    """
    def is_fully_defined(self):
        """Returns True iff `self` is fully defined in every dimension."""
    def assert_is_fully_defined(self) -> None:
        """Raises an exception if `self` is not fully defined in every dimension.

    Raises:
      ValueError: If `self` does not have a known value for every dimension.
    """
    def as_list(self):
        """Returns a list of integers or `None` for each dimension.

    Returns:
      A list of integers or `None` for each dimension.

    Raises:
      ValueError: If `self` is an unknown shape with an unknown rank.
    """
    def as_proto(self):
        """Returns this shape as a `TensorShapeProto`."""
    def __eq__(self, other):
        """Returns True if `self` is equivalent to `other`.

    It first tries to convert `other` to `TensorShape`. `TypeError` is thrown
    when the conversion fails. Otherwise, it compares each element in the
    TensorShape dimensions.

    * Two *Fully known* shapes, return True iff each element is equal.
    >>> t_a = tf.TensorShape([1,2])
    >>> a = [1, 2]
    >>> t_b = tf.TensorShape([1,2])
    >>> t_c = tf.TensorShape([1,2,3])
    >>> t_a.__eq__(a)
    True
    >>> t_a.__eq__(t_b)
    True
    >>> t_a.__eq__(t_c)
    False

    * Two *Partially-known* shapes, return True iff each element is equal.
    >>> p_a = tf.TensorShape([1,None])
    >>> p_b = tf.TensorShape([1,None])
    >>> p_c = tf.TensorShape([2,None])
    >>> p_a.__eq__(p_b)
    True
    >>> t_a.__eq__(p_a)
    False
    >>> p_a.__eq__(p_c)
    False

    * Two *Unknown shape*, return True.
    >>> unk_a = tf.TensorShape(None)
    >>> unk_b = tf.TensorShape(None)
    >>> unk_a.__eq__(unk_b)
    True
    >>> unk_a.__eq__(t_a)
    False

    Args:
      other: A `TensorShape` or type that can be converted to `TensorShape`.

    Returns:
      True if the dimensions are all equal.

    Raises:
      TypeError if `other` can not be converted to `TensorShape`.
    """
    def __hash__(self): ...
    def __reduce__(self): ...
    def __concat__(self, other): ...

def as_shape(shape):
    """Converts the given object to a TensorShape."""
def unknown_shape(rank: Incomplete | None = None, **kwargs):
    """Returns an unknown TensorShape, optionally with a known rank.

  Args:
    rank: (Optional) If specified, the number of dimensions in the shape.
    **kwargs: For backwards compatibility.

  Returns:
    An unknown TensorShape.

  Raises:
    TypeError: In case of invalid arguments.
  """
