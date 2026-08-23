from _typeshed import Incomplete
from tensorflow.python.util.tf_export import keras_export as keras_export

def to_categorical(y, num_classes: Incomplete | None = None, dtype: str = 'float32'):
    """Converts a class vector (integers) to binary class matrix.

  E.g. for use with categorical_crossentropy.

  Args:
      y: class vector to be converted into a matrix
          (integers from 0 to num_classes).
      num_classes: total number of classes. If `None`, this would be inferred
        as the (largest number in `y`) + 1.
      dtype: The data type expected by the input. Default: `'float32'`.

  Returns:
      A binary matrix representation of the input. The classes axis is placed
      last.

  Example:

  >>> a = tf.keras.utils.to_categorical([0, 1, 2, 3], num_classes=4)
  >>> a = tf.constant(a, shape=[4, 4])
  >>> print(a)
  tf.Tensor(
    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]], shape=(4, 4), dtype=float32)

  >>> b = tf.constant([.9, .04, .03, .03,
  ...                  .3, .45, .15, .13,
  ...                  .04, .01, .94, .05,
  ...                  .12, .21, .5, .17],
  ...                 shape=[4, 4])
  >>> loss = tf.keras.backend.categorical_crossentropy(a, b)
  >>> print(np.around(loss, 5))
  [0.10536 0.82807 0.1011  1.77196]

  >>> loss = tf.keras.backend.categorical_crossentropy(a, a)
  >>> print(np.around(loss, 5))
  [0. 0. 0. 0.]

  Raises:
      Value Error: If input contains string value

  """
def normalize(x, axis: int = -1, order: int = 2):
    """Normalizes a Numpy array.

  Args:
      x: Numpy array to normalize.
      axis: axis along which to normalize.
      order: Normalization order (e.g. `order=2` for L2 norm).

  Returns:
      A normalized copy of the array.
  """
