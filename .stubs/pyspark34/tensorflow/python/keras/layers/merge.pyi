from _typeshed import Incomplete
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn
from tensorflow.python.util.tf_export import keras_export as keras_export

class _Merge(Layer):
    """Generic merge layer for elementwise merge functions.

  Used to implement `Sum`, `Average`, etc.
  """
    supports_masking: bool
    def __init__(self, **kwargs) -> None:
        """Intializes a Merge layer.

    Args:
      **kwargs: standard layer keyword arguments.
    """
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...

class Add(_Merge):
    """Layer that adds a list of inputs.

  It takes as input a list of tensors,
  all of the same shape, and returns
  a single tensor (also of the same shape).

  Examples:

  >>> input_shape = (2, 3, 4)
  >>> x1 = tf.random.normal(input_shape)
  >>> x2 = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Add()([x1, x2])
  >>> print(y.shape)
  (2, 3, 4)

  Used in a functional model:

  >>> input1 = tf.keras.layers.Input(shape=(16,))
  >>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1)
  >>> input2 = tf.keras.layers.Input(shape=(32,))
  >>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2)
  >>> # equivalent to `added = tf.keras.layers.add([x1, x2])`
  >>> added = tf.keras.layers.Add()([x1, x2])
  >>> out = tf.keras.layers.Dense(4)(added)
  >>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)

  """

class Subtract(_Merge):
    """Layer that subtracts two inputs.

  It takes as input a list of tensors of size 2,
  both of the same shape, and returns a single tensor, (inputs[0] - inputs[1]),
  also of the same shape.

  Examples:

  ```python
      import keras

      input1 = keras.layers.Input(shape=(16,))
      x1 = keras.layers.Dense(8, activation='relu')(input1)
      input2 = keras.layers.Input(shape=(32,))
      x2 = keras.layers.Dense(8, activation='relu')(input2)
      # Equivalent to subtracted = keras.layers.subtract([x1, x2])
      subtracted = keras.layers.Subtract()([x1, x2])

      out = keras.layers.Dense(4)(subtracted)
      model = keras.models.Model(inputs=[input1, input2], outputs=out)
  ```
  """
    def build(self, input_shape) -> None: ...

class Multiply(_Merge):
    """Layer that multiplies (element-wise) a list of inputs.

  It takes as input a list of tensors, all of the same shape, and returns
  a single tensor (also of the same shape).

  >>> tf.keras.layers.Multiply()([np.arange(5).reshape(5, 1),
  ...                             np.arange(5, 10).reshape(5, 1)])
  <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
  array([[ 0],
       [ 6],
       [14],
       [24],
       [36]])>

  >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
  >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
  >>> multiplied = tf.keras.layers.Multiply()([x1, x2])
  >>> multiplied.shape
  TensorShape([5, 8])
  """
class Average(_Merge):
    """Layer that averages a list of inputs element-wise.

  It takes as input a list of tensors, all of the same shape, and returns
  a single tensor (also of the same shape).

  Example:

  >>> x1 = np.ones((2, 2))
  >>> x2 = np.zeros((2, 2))
  >>> y = tf.keras.layers.Average()([x1, x2])
  >>> y.numpy().tolist()
  [[0.5, 0.5], [0.5, 0.5]]

  Usage in a functional model:

  >>> input1 = tf.keras.layers.Input(shape=(16,))
  >>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1)
  >>> input2 = tf.keras.layers.Input(shape=(32,))
  >>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2)
  >>> avg = tf.keras.layers.Average()([x1, x2])
  >>> out = tf.keras.layers.Dense(4)(avg)
  >>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)

  Raises:
    ValueError: If there is a shape mismatch between the inputs and the shapes
      cannot be broadcasted to match.
  """
class Maximum(_Merge):
    """Layer that computes the maximum (element-wise) a list of inputs.

  It takes as input a list of tensors, all of the same shape, and returns
  a single tensor (also of the same shape).

  >>> tf.keras.layers.Maximum()([np.arange(5).reshape(5, 1),
  ...                            np.arange(5, 10).reshape(5, 1)])
  <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
  array([[5],
       [6],
       [7],
       [8],
       [9]])>

  >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
  >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
  >>> maxed = tf.keras.layers.Maximum()([x1, x2])
  >>> maxed.shape
  TensorShape([5, 8])
  """
class Minimum(_Merge):
    """Layer that computes the minimum (element-wise) a list of inputs.

  It takes as input a list of tensors, all of the same shape, and returns
  a single tensor (also of the same shape).

  >>> tf.keras.layers.Minimum()([np.arange(5).reshape(5, 1),
  ...                            np.arange(5, 10).reshape(5, 1)])
  <tf.Tensor: shape=(5, 1), dtype=int64, numpy=
  array([[0],
       [1],
       [2],
       [3],
       [4]])>

  >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
  >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
  >>> minned = tf.keras.layers.Minimum()([x1, x2])
  >>> minned.shape
  TensorShape([5, 8])
  """

class Concatenate(_Merge):
    """Layer that concatenates a list of inputs.

  It takes as input a list of tensors, all of the same shape except
  for the concatenation axis, and returns a single tensor that is the
  concatenation of all inputs.

  >>> x = np.arange(20).reshape(2, 2, 5)
  >>> print(x)
  [[[ 0  1  2  3  4]
    [ 5  6  7  8  9]]
   [[10 11 12 13 14]
    [15 16 17 18 19]]]
  >>> y = np.arange(20, 30).reshape(2, 1, 5)
  >>> print(y)
  [[[20 21 22 23 24]]
   [[25 26 27 28 29]]]
  >>> tf.keras.layers.Concatenate(axis=1)([x, y])
  <tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
  array([[[ 0,  1,  2,  3,  4],
          [ 5,  6,  7,  8,  9],
          [20, 21, 22, 23, 24]],
         [[10, 11, 12, 13, 14],
          [15, 16, 17, 18, 19],
          [25, 26, 27, 28, 29]]])>

  >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
  >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
  >>> concatted = tf.keras.layers.Concatenate()([x1, x2])
  >>> concatted.shape
  TensorShape([5, 16])

  """
    axis: Incomplete
    supports_masking: bool
    def __init__(self, axis: int = -1, **kwargs) -> None:
        """Instantiates a Concatenate layer.

    >>> x = np.arange(20).reshape(2, 2, 5)
    >>> print(x)
    [[[ 0  1  2  3  4]
      [ 5  6  7  8  9]]
     [[10 11 12 13 14]
      [15 16 17 18 19]]]
    >>> y = np.arange(20, 30).reshape(2, 1, 5)
    >>> print(y)
    [[[20 21 22 23 24]]
     [[25 26 27 28 29]]]
    >>> tf.keras.layers.Concatenate(axis=1)([x, y])
    <tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
    array([[[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [20, 21, 22, 23, 24]],
           [[10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [25, 26, 27, 28, 29]]])>

    Args:
      axis: Axis along which to concatenate.
      **kwargs: standard layer keyword arguments.
    """
    def build(self, input_shape) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...
    def get_config(self): ...

class Dot(_Merge):
    """Layer that computes a dot product between samples in two tensors.

  E.g. if applied to a list of two tensors `a` and `b` of shape
  `(batch_size, n)`, the output will be a tensor of shape `(batch_size, 1)`
  where each entry `i` will be the dot product between
  `a[i]` and `b[i]`.

  >>> x = np.arange(10).reshape(1, 5, 2)
  >>> print(x)
  [[[0 1]
    [2 3]
    [4 5]
    [6 7]
    [8 9]]]
  >>> y = np.arange(10, 20).reshape(1, 2, 5)
  >>> print(y)
  [[[10 11 12 13 14]
    [15 16 17 18 19]]]
  >>> tf.keras.layers.Dot(axes=(1, 2))([x, y])
  <tf.Tensor: shape=(1, 2, 2), dtype=int64, numpy=
  array([[[260, 360],
          [320, 445]]])>

  >>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
  >>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
  >>> dotted = tf.keras.layers.Dot(axes=1)([x1, x2])
  >>> dotted.shape
  TensorShape([5, 1])


  """
    axes: Incomplete
    normalize: Incomplete
    supports_masking: bool
    def __init__(self, axes, normalize: bool = False, **kwargs) -> None:
        """Initializes a layer that computes the element-wise dot product.

      >>> x = np.arange(10).reshape(1, 5, 2)
      >>> print(x)
      [[[0 1]
        [2 3]
        [4 5]
        [6 7]
        [8 9]]]
      >>> y = np.arange(10, 20).reshape(1, 2, 5)
      >>> print(y)
      [[[10 11 12 13 14]
        [15 16 17 18 19]]]
      >>> tf.keras.layers.Dot(axes=(1, 2))([x, y])
      <tf.Tensor: shape=(1, 2, 2), dtype=int64, numpy=
      array([[[260, 360],
              [320, 445]]])>

    Args:
      axes: Integer or tuple of integers,
        axis or axes along which to take the dot product. If a tuple, should
        be two integers corresponding to the desired axis from the first input
        and the desired axis from the second input, respectively. Note that the
        size of the two selected axes must match.
      normalize: Whether to L2-normalize samples along the
        dot product axis before taking the dot product.
        If set to True, then the output of the dot product
        is the cosine proximity between the two samples.
      **kwargs: Standard layer keyword arguments.
    """
    def build(self, input_shape) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None) -> None: ...
    def get_config(self): ...

def add(inputs, **kwargs):
    """Functional interface to the `tf.keras.layers.Add` layer.

  Args:
      inputs: A list of input tensors (at least 2) with the same shape.
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor as the sum of the inputs. It has the same shape as the inputs.

  Examples:

  >>> input_shape = (2, 3, 4)
  >>> x1 = tf.random.normal(input_shape)
  >>> x2 = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.add([x1, x2])
  >>> print(y.shape)
  (2, 3, 4)

  Used in a functional model:

  >>> input1 = tf.keras.layers.Input(shape=(16,))
  >>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1)
  >>> input2 = tf.keras.layers.Input(shape=(32,))
  >>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2)
  >>> added = tf.keras.layers.add([x1, x2])
  >>> out = tf.keras.layers.Dense(4)(added)
  >>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)

  """
def subtract(inputs, **kwargs):
    """Functional interface to the `Subtract` layer.

  Args:
      inputs: A list of input tensors (exactly 2).
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor, the difference of the inputs.

  Examples:

  ```python
      import keras

      input1 = keras.layers.Input(shape=(16,))
      x1 = keras.layers.Dense(8, activation='relu')(input1)
      input2 = keras.layers.Input(shape=(32,))
      x2 = keras.layers.Dense(8, activation='relu')(input2)
      subtracted = keras.layers.subtract([x1, x2])

      out = keras.layers.Dense(4)(subtracted)
      model = keras.models.Model(inputs=[input1, input2], outputs=out)
  ```
  """
def multiply(inputs, **kwargs):
    """Functional interface to the `Multiply` layer.

  Example:

  >>> x1 = np.arange(3.0)
  >>> x2 = np.arange(3.0)
  >>> tf.keras.layers.multiply([x1, x2])
  <tf.Tensor: shape=(3,), dtype=float32, numpy=array([0., 1., 4.], ...)>

  Usage in a functional model:

  >>> input1 = tf.keras.layers.Input(shape=(16,))
  >>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1) #shape=(None, 8)
  >>> input2 = tf.keras.layers.Input(shape=(32,))
  >>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2) #shape=(None, 8)
  >>> out = tf.keras.layers.multiply([x1,x2]) #shape=(None, 8)
  >>> out = tf.keras.layers.Dense(4)(out)
  >>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)

  Args:
      inputs: A list of input tensors (at least 2).
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor, the element-wise product of the inputs.
  """
def average(inputs, **kwargs):
    """Functional interface to the `tf.keras.layers.Average` layer.

  Example:

  >>> x1 = np.ones((2, 2))
  >>> x2 = np.zeros((2, 2))
  >>> y = tf.keras.layers.Average()([x1, x2])
  >>> y.numpy().tolist()
  [[0.5, 0.5], [0.5, 0.5]]

  Usage in a functional model:

  >>> input1 = tf.keras.layers.Input(shape=(16,))
  >>> x1 = tf.keras.layers.Dense(8, activation='relu')(input1)
  >>> input2 = tf.keras.layers.Input(shape=(32,))
  >>> x2 = tf.keras.layers.Dense(8, activation='relu')(input2)
  >>> avg = tf.keras.layers.Average()([x1, x2])
  >>> out = tf.keras.layers.Dense(4)(avg)
  >>> model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)

  Args:
      inputs: A list of input tensors (at least 2).
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor, the average of the inputs.

  Raises:
    ValueError: If there is a shape mismatch between the inputs and the shapes
      cannot be broadcasted to match.
  """
def maximum(inputs, **kwargs):
    """Functional interface to compute maximum (element-wise) list of `inputs`.

  This is equivalent to the `tf.keras.layers.Maximum` layer.

  For example:

  ```python
  input1 = tf.keras.layers.Input(shape=(16,))
  x1 = tf.keras.layers.Dense(8, activation='relu')(input1) #shape=(None, 8)
  input2 = tf.keras.layers.Input(shape=(32,))
  x2 = tf.keras.layers.Dense(8, activation='relu')(input2) #shape=(None, 8)
  max_inp=tf.keras.layers.maximum([x1,x2]) #shape=(None, 8)
  out = tf.keras.layers.Dense(4)(max_inp)
  model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)
  ```

  Args:
      inputs: A list of input tensors (at least 2) of same shape.
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor (of same shape as input tensor) with the element-wise
      maximum of the inputs.

  Raises:
      ValueError: If input tensors are of different shape.
  """
def minimum(inputs, **kwargs):
    """Functional interface to the `Minimum` layer.

  Args:
      inputs: A list of input tensors (at least 2).
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor, the element-wise minimum of the inputs.
  """
def concatenate(inputs, axis: int = -1, **kwargs):
    """Functional interface to the `Concatenate` layer.

  >>> x = np.arange(20).reshape(2, 2, 5)
  >>> print(x)
  [[[ 0  1  2  3  4]
    [ 5  6  7  8  9]]
   [[10 11 12 13 14]
    [15 16 17 18 19]]]
  >>> y = np.arange(20, 30).reshape(2, 1, 5)
  >>> print(y)
  [[[20 21 22 23 24]]
   [[25 26 27 28 29]]]
  >>> tf.keras.layers.concatenate([x, y],
  ...                             axis=1)
  <tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
  array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9],
        [20, 21, 22, 23, 24]],
       [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [25, 26, 27, 28, 29]]])>

  Args:
      inputs: A list of input tensors (at least 2).
      axis: Concatenation axis.
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor, the concatenation of the inputs alongside axis `axis`.
  """
def dot(inputs, axes, normalize: bool = False, **kwargs):
    """Functional interface to the `Dot` layer.

  Args:
      inputs: A list of input tensors (at least 2).
      axes: Integer or tuple of integers,
          axis or axes along which to take the dot product.
      normalize: Whether to L2-normalize samples along the
          dot product axis before taking the dot product.
          If set to True, then the output of the dot product
          is the cosine proximity between the two samples.
      **kwargs: Standard layer keyword arguments.

  Returns:
      A tensor, the dot product of the samples from the inputs.
  """
