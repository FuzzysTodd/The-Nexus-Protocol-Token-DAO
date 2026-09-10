from . import compat as compat, dtypes as dtypes
from _typeshed import Incomplete
from tensorboard.compat.proto import tensor_shape_pb2 as tensor_shape_pb2

class Dimension:
    """Represents the value of one dimension in a TensorShape."""
    def __init__(self, value) -> None:
        """Creates a new Dimension with the given value."""
    def __eq__(self, other):
        """Returns true if `other` has the same known value as this
        Dimension."""
    def __ne__(self, other):
        """Returns true if `other` has a different known value from `self`."""
    def __int__(self) -> int: ...
    def __long__(self): ...
    def __index__(self) -> int: ...
    @property
    def value(self):
        """The value of this dimension, or None if it is unknown."""
    def is_convertible_with(self, other):
        """Returns true if `other` is convertible with this Dimension.

        Two known Dimensions are convertible if they have the same value.
        An unknown Dimension is convertible with all other Dimensions.

        Args:
          other: Another Dimension.

        Returns:
          True if this Dimension and `other` are convertible.
        """
    def assert_is_convertible_with(self, other) -> None:
        """Raises an exception if `other` is not convertible with this
        Dimension.

        Args:
          other: Another Dimension.

        Raises:
          ValueError: If `self` and `other` are not convertible (see
            is_convertible_with).
        """
    def merge_with(self, other):
        """Returns a Dimension that combines the information in `self` and
        `other`.

        Dimensions are combined as follows:

        ```python
        tf.Dimension(n)   .merge_with(tf.Dimension(n))    == tf.Dimension(n)
        tf.Dimension(n)   .merge_with(tf.Dimension(None)) == tf.Dimension(n)
        tf.Dimension(None).merge_with(tf.Dimension(n))    == tf.Dimension(n)
        tf.Dimension(None).merge_with(tf.Dimension(None)) == tf.Dimension(None)
        tf.Dimension(n)   .merge_with(tf.Dimension(m))  # raises ValueError for n != m
        ```

        Args:
          other: Another Dimension.

        Returns:
          A Dimension containing the combined information of `self` and
          `other`.

        Raises:
          ValueError: If `self` and `other` are not convertible (see
            is_convertible_with).
        """
    def __add__(self, other):
        """Returns the sum of `self` and `other`.

        Dimensions are summed as follows:

        ```python
        tf.Dimension(m)    + tf.Dimension(n)    == tf.Dimension(m + n)
        tf.Dimension(m)    + tf.Dimension(None) == tf.Dimension(None)
        tf.Dimension(None) + tf.Dimension(n)    == tf.Dimension(None)
        tf.Dimension(None) + tf.Dimension(None) == tf.Dimension(None)
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
        tf.Dimension(m)    - tf.Dimension(n)    == tf.Dimension(m - n)
        tf.Dimension(m)    - tf.Dimension(None) == tf.Dimension(None)
        tf.Dimension(None) - tf.Dimension(n)    == tf.Dimension(None)
        tf.Dimension(None) - tf.Dimension(None) == tf.Dimension(None)
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
        tf.Dimension(m)    * tf.Dimension(n)    == tf.Dimension(m * n)
        tf.Dimension(m)    * tf.Dimension(None) == tf.Dimension(None)
        tf.Dimension(None) * tf.Dimension(n)    == tf.Dimension(None)
        tf.Dimension(None) * tf.Dimension(None) == tf.Dimension(None)
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
        tf.Dimension(m)    // tf.Dimension(n)    == tf.Dimension(m // n)
        tf.Dimension(m)    // tf.Dimension(None) == tf.Dimension(None)
        tf.Dimension(None) // tf.Dimension(n)    == tf.Dimension(None)
        tf.Dimension(None) // tf.Dimension(None) == tf.Dimension(None)
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

        This function exists only for backwards convertibility purposes; new code
        should use `__floordiv__` via the syntax `x // y`.  Using `x // y`
        communicates clearly that the result rounds down, and is forward convertible
        to Python 3.

        Args:
          other: Another `Dimension`.

        Returns:
          A `Dimension` whose value is the integer quotient of `self` and `other`.
        """
    def __mod__(self, other):
        """Returns `self` modulo `other`.

        Dimension moduli are computed as follows:

        ```python
        tf.Dimension(m)    % tf.Dimension(n)    == tf.Dimension(m % n)
        tf.Dimension(m)    % tf.Dimension(None) == tf.Dimension(None)
        tf.Dimension(None) % tf.Dimension(n)    == tf.Dimension(None)
        tf.Dimension(None) % tf.Dimension(None) == tf.Dimension(None)
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
        (tf.Dimension(m)    < tf.Dimension(n))    == (m < n)
        (tf.Dimension(m)    < tf.Dimension(None)) == None
        (tf.Dimension(None) < tf.Dimension(n))    == None
        (tf.Dimension(None) < tf.Dimension(None)) == None
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
        (tf.Dimension(m)    <= tf.Dimension(n))    == (m <= n)
        (tf.Dimension(m)    <= tf.Dimension(None)) == None
        (tf.Dimension(None) <= tf.Dimension(n))    == None
        (tf.Dimension(None) <= tf.Dimension(None)) == None
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
        (tf.Dimension(m)    > tf.Dimension(n))    == (m > n)
        (tf.Dimension(m)    > tf.Dimension(None)) == None
        (tf.Dimension(None) > tf.Dimension(n))    == None
        (tf.Dimension(None) > tf.Dimension(None)) == None
        ```

        Args:
          other: Another Dimension.

        Returns:
          The value of `self.value > other.value` if both are known, otherwise
          None.
        """
    def __ge__(self, other):
        """Returns True if `self` is known to be greater than or equal to
        `other`.

        Dimensions are compared as follows:

        ```python
        (tf.Dimension(m)    >= tf.Dimension(n))    == (m >= n)
        (tf.Dimension(m)    >= tf.Dimension(None)) == None
        (tf.Dimension(None) >= tf.Dimension(n))    == None
        (tf.Dimension(None) >= tf.Dimension(None)) == None
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

class TensorShape:
    '''Represents the shape of a `Tensor`.

    A `TensorShape` represents a possibly-partial shape specification for a
    `Tensor`. It may be one of the following:

    * *Fully-known shape:* has a known number of dimensions and a known size
      for each dimension. e.g. `TensorShape([16, 256])`
    * *Partially-known shape:* has a known number of dimensions, and an unknown
      size for one or more dimension. e.g. `TensorShape([None, 256])`
    * *Unknown shape:* has an unknown number of dimensions, and an unknown
      size in all dimensions. e.g. `TensorShape(None)`

    If a tensor is produced by an operation of type `"Foo"`, its shape
    may be inferred if there is a registered shape function for
    `"Foo"`. See @{$adding_an_op#shape-functions-in-c$`Shape functions in C++`}
    for details of shape functions and how to register them. Alternatively,
    the shape may be set explicitly using @{tf.Tensor.set_shape}.
    '''
    def __init__(self, dims) -> None:
        """Creates a new TensorShape with the given dimensions.

        Args:
          dims: A list of Dimensions, or None if the shape is unspecified.
            DEPRECATED: A single integer is treated as a singleton list.

        Raises:
          TypeError: If dims cannot be converted to a list of dimensions.
        """
    @property
    def dims(self):
        """Returns a list of Dimensions, or None if the shape is
        unspecified."""
    @dims.setter
    def dims(self, dims) -> None: ...
    @property
    def ndims(self):
        """Returns the rank of this shape, or None if it is unspecified."""
    def __len__(self) -> int:
        """Returns the rank of this shape, or raises ValueError if
        unspecified."""
    def __bool__(self) -> bool:
        """Returns True if this shape contains non-zero information."""
    __nonzero__ = __bool__
    def __iter__(self):
        """Returns `self.dims` if the rank is known, otherwise raises
        ValueError."""
    def __getitem__(self, key):
        """Returns the value of a dimension or a shape, depending on the key.

        Args:
          key: If `key` is an integer, returns the dimension at that index;
            otherwise if `key` is a slice, returns a TensorShape whose
            dimensions are those selected by the slice from `self`.

        Returns:
          A dimension if `key` is an integer, or a `TensorShape` if `key` is a
          slice.

        Raises:
          ValueError: If `key` is a slice, and any of its elements are negative, or
            if `self` is completely unknown and the step is set.
        """
    def num_elements(self):
        """Returns the total number of elements, or none for incomplete
        shapes."""
    def merge_with(self, other):
        """Returns a `TensorShape` combining the information in `self` and
        `other`.

        The dimensions in `self` and `other` are merged elementwise,
        according to the rules defined for `Dimension.merge_with()`.

        Args:
          other: Another `TensorShape`.

        Returns:
          A `TensorShape` containing the combined information of `self` and
          `other`.

        Raises:
          ValueError: If `self` and `other` are not convertible.
        """
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
        """Raises an exception if `self` and `other` do not have convertible
        ranks.

        Args:
          other: Another `TensorShape`.

        Raises:
          ValueError: If `self` and `other` do not represent shapes with the
            same rank.
        """
    def assert_has_rank(self, rank) -> None:
        """Raises an exception if `self` is not convertible with the given
        `rank`.

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
    def is_convertible_with(self, other):
        """Returns True iff `self` is convertible with `other`.

        Two possibly-partially-defined shapes are convertible if there
        exists a fully-defined shape that both shapes can represent. Thus,
        convertibility allows the shape inference code to reason about
        partially-defined shapes. For example:

        * TensorShape(None) is convertible with all shapes.

        * TensorShape([None, None]) is convertible with all two-dimensional
          shapes, such as TensorShape([32, 784]), and also TensorShape(None). It is
          not convertible with, for example, TensorShape([None]) or
          TensorShape([None, None, None]).

        * TensorShape([32, None]) is convertible with all two-dimensional shapes
          with size 32 in the 0th dimension, and also TensorShape([None, None])
          and TensorShape(None). It is not convertible with, for example,
          TensorShape([32]), TensorShape([32, None, 1]) or TensorShape([64, None]).

        * TensorShape([32, 784]) is convertible with itself, and also
          TensorShape([32, None]), TensorShape([None, 784]), TensorShape([None,
          None]) and TensorShape(None). It is not convertible with, for example,
          TensorShape([32, 1, 784]) or TensorShape([None]).

        The convertibility relation is reflexive and symmetric, but not
        transitive. For example, TensorShape([32, 784]) is convertible with
        TensorShape(None), and TensorShape(None) is convertible with
        TensorShape([4, 4]), but TensorShape([32, 784]) is not convertible with
        TensorShape([4, 4]).

        Args:
          other: Another TensorShape.

        Returns:
          True iff `self` is convertible with `other`.
        """
    def assert_is_convertible_with(self, other) -> None:
        """Raises exception if `self` and `other` do not represent the same
        shape.

        This method can be used to assert that there exists a shape that both
        `self` and `other` represent.

        Args:
          other: Another TensorShape.

        Raises:
          ValueError: If `self` and `other` do not represent the same shape.
        """
    def most_specific_convertible_shape(self, other):
        """Returns the most specific TensorShape convertible with `self` and
        `other`.

        * TensorShape([None, 1]) is the most specific TensorShape convertible with
          both TensorShape([2, 1]) and TensorShape([5, 1]). Note that
          TensorShape(None) is also convertible with above mentioned TensorShapes.

        * TensorShape([1, 2, 3]) is the most specific TensorShape convertible with
          both TensorShape([1, 2, 3]) and TensorShape([1, 2, 3]). There are more
          less specific TensorShapes convertible with above mentioned TensorShapes,
          e.g. TensorShape([1, 2, None]), TensorShape(None).

        Args:
          other: Another `TensorShape`.

        Returns:
          A `TensorShape` which is the most specific convertible shape of `self`
          and `other`.
        """
    def is_fully_defined(self):
        """Returns True iff `self` is fully defined in every dimension."""
    def assert_is_fully_defined(self) -> None:
        """Raises an exception if `self` is not fully defined in every
        dimension.

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
        """Returns True if `self` is equivalent to `other`."""
    def __ne__(self, other):
        """Returns True if `self` is known to be different from `other`."""
    def __reduce__(self): ...

def as_shape(shape):
    """Converts the given object to a TensorShape."""
def unknown_shape(ndims: Incomplete | None = None):
    """Returns an unknown TensorShape, optionally with a known rank.

    Args:
      ndims: (Optional) If specified, the number of dimensions in the shape.

    Returns:
      An unknown TensorShape.
    """
def scalar():
    """Returns a shape representing a scalar."""
def vector(length):
    """Returns a shape representing a vector.

    Args:
      length: The length of the vector, which may be None if unknown.

    Returns:
      A TensorShape representing a vector of the given length.
    """
def matrix(rows, cols):
    """Returns a shape representing a matrix.

    Args:
      rows: The number of rows in the matrix, which may be None if unknown.
      cols: The number of columns in the matrix, which may be None if unknown.

    Returns:
      A TensorShape representing a matrix of the given size.
    """
