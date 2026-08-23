from _typeshed import Incomplete
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.utils import conv_utils as conv_utils
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn
from tensorflow.python.util.tf_export import keras_export as keras_export

class Pooling1D(Layer):
    """Pooling layer for arbitrary pooling functions, for 1D inputs.

  This class only exists for code reuse. It will never be an exposed API.

  Args:
    pool_function: The pooling function to apply, e.g. `tf.nn.max_pool2d`.
    pool_size: An integer or tuple/list of a single integer,
      representing the size of the pooling window.
    strides: An integer or tuple/list of a single integer, specifying the
      strides of the pooling operation.
    padding: A string. The padding method, either 'valid' or 'same'.
      Case-insensitive.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, steps, features)` while `channels_first`
      corresponds to inputs with shape
      `(batch, features, steps)`.
    name: A string, the name of the layer.
  """
    pool_function: Incomplete
    pool_size: Incomplete
    strides: Incomplete
    padding: Incomplete
    data_format: Incomplete
    input_spec: Incomplete
    def __init__(self, pool_function, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class MaxPooling1D(Pooling1D):
    '''Max pooling operation for 1D temporal data.

  Downsamples the input representation by taking the maximum value over a
  spatial window of size `pool_size`. The window is shifted by `strides`.  The
  resulting output, when using the `"valid"` padding option, has a shape of:
  `output_shape = (input_shape - pool_size + 1) / strides)`

  The resulting output shape when using the `"same"` padding option is:
  `output_shape = input_shape / strides`

  For example, for `strides=1` and `padding="valid"`:

  >>> x = tf.constant([1., 2., 3., 4., 5.])
  >>> x = tf.reshape(x, [1, 5, 1])
  >>> max_pool_1d = tf.keras.layers.MaxPooling1D(pool_size=2,
  ...    strides=1, padding=\'valid\')
  >>> max_pool_1d(x)
  <tf.Tensor: shape=(1, 4, 1), dtype=float32, numpy=
  array([[[2.],
          [3.],
          [4.],
          [5.]]], dtype=float32)>

  For example, for `strides=2` and `padding="valid"`:

  >>> x = tf.constant([1., 2., 3., 4., 5.])
  >>> x = tf.reshape(x, [1, 5, 1])
  >>> max_pool_1d = tf.keras.layers.MaxPooling1D(pool_size=2,
  ...    strides=2, padding=\'valid\')
  >>> max_pool_1d(x)
  <tf.Tensor: shape=(1, 2, 1), dtype=float32, numpy=
  array([[[2.],
          [4.]]], dtype=float32)>

  For example, for `strides=1` and `padding="same"`:

  >>> x = tf.constant([1., 2., 3., 4., 5.])
  >>> x = tf.reshape(x, [1, 5, 1])
  >>> max_pool_1d = tf.keras.layers.MaxPooling1D(pool_size=2,
  ...    strides=1, padding=\'same\')
  >>> max_pool_1d(x)
  <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=
  array([[[2.],
          [3.],
          [4.],
          [5.],
          [5.]]], dtype=float32)>

  Args:
    pool_size: Integer, size of the max pooling window.
    strides: Integer, or None. Specifies how much the pooling window moves
      for each pooling step.
      If None, it will default to `pool_size`.
    padding: One of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, steps, features)` while `channels_first`
      corresponds to inputs with shape
      `(batch, features, steps)`.

  Input shape:
    - If `data_format=\'channels_last\'`:
      3D tensor with shape `(batch_size, steps, features)`.
    - If `data_format=\'channels_first\'`:
      3D tensor with shape `(batch_size, features, steps)`.

  Output shape:
    - If `data_format=\'channels_last\'`:
      3D tensor with shape `(batch_size, downsampled_steps, features)`.
    - If `data_format=\'channels_first\'`:
      3D tensor with shape `(batch_size, features, downsampled_steps)`.
  '''
    def __init__(self, pool_size: int = 2, strides: Incomplete | None = None, padding: str = 'valid', data_format: str = 'channels_last', **kwargs) -> None: ...

class AveragePooling1D(Pooling1D):
    '''Average pooling for temporal data.

  Downsamples the input representation by taking the average value over the
  window defined by `pool_size`. The window is shifted by `strides`.  The
  resulting output when using "valid" padding option has a shape of:
  `output_shape = (input_shape - pool_size + 1) / strides)`

  The resulting output shape when using the "same" padding option is:
  `output_shape = input_shape / strides`

  For example, for strides=1 and padding="valid":

  >>> x = tf.constant([1., 2., 3., 4., 5.])
  >>> x = tf.reshape(x, [1, 5, 1])
  >>> x
  <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=
    array([[[1.],
            [2.],
            [3.],
            [4.],
            [5.]], dtype=float32)>
  >>> avg_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=2,
  ...    strides=1, padding=\'valid\')
  >>> avg_pool_1d(x)
  <tf.Tensor: shape=(1, 4, 1), dtype=float32, numpy=
  array([[[1.5],
          [2.5],
          [3.5],
          [4.5]]], dtype=float32)>

  For example, for strides=2 and padding="valid":

  >>> x = tf.constant([1., 2., 3., 4., 5.])
  >>> x = tf.reshape(x, [1, 5, 1])
  >>> x
  <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=
    array([[[1.],
            [2.],
            [3.],
            [4.],
            [5.]], dtype=float32)>
  >>> avg_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=2,
  ...    strides=2, padding=\'valid\')
  >>> avg_pool_1d(x)
  <tf.Tensor: shape=(1, 2, 1), dtype=float32, numpy=
  array([[[1.5],
          [3.5]]], dtype=float32)>

  For example, for strides=1 and padding="same":

  >>> x = tf.constant([1., 2., 3., 4., 5.])
  >>> x = tf.reshape(x, [1, 5, 1])
  >>> x
  <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=
    array([[[1.],
            [2.],
            [3.],
            [4.],
            [5.]], dtype=float32)>
  >>> avg_pool_1d = tf.keras.layers.AveragePooling1D(pool_size=2,
  ...    strides=1, padding=\'same\')
  >>> avg_pool_1d(x)
  <tf.Tensor: shape=(1, 5, 1), dtype=float32, numpy=
  array([[[1.5],
          [2.5],
          [3.5],
          [4.5],
          [5.]]], dtype=float32)>

  Args:
    pool_size: Integer, size of the average pooling windows.
    strides: Integer, or None. Factor by which to downscale.
      E.g. 2 will halve the input.
      If None, it will default to `pool_size`.
    padding: One of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, steps, features)` while `channels_first`
      corresponds to inputs with shape
      `(batch, features, steps)`.

  Input shape:
    - If `data_format=\'channels_last\'`:
      3D tensor with shape `(batch_size, steps, features)`.
    - If `data_format=\'channels_first\'`:
      3D tensor with shape `(batch_size, features, steps)`.

  Output shape:
    - If `data_format=\'channels_last\'`:
      3D tensor with shape `(batch_size, downsampled_steps, features)`.
    - If `data_format=\'channels_first\'`:
      3D tensor with shape `(batch_size, features, downsampled_steps)`.
  '''
    def __init__(self, pool_size: int = 2, strides: Incomplete | None = None, padding: str = 'valid', data_format: str = 'channels_last', **kwargs) -> None: ...

class Pooling2D(Layer):
    """Pooling layer for arbitrary pooling functions, for 2D inputs (e.g. images).

  This class only exists for code reuse. It will never be an exposed API.

  Args:
    pool_function: The pooling function to apply, e.g. `tf.nn.max_pool2d`.
    pool_size: An integer or tuple/list of 2 integers: (pool_height, pool_width)
      specifying the size of the pooling window.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    strides: An integer or tuple/list of 2 integers,
      specifying the strides of the pooling operation.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    padding: A string. The padding method, either 'valid' or 'same'.
      Case-insensitive.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, height, width, channels)` while `channels_first` corresponds to
      inputs with shape `(batch, channels, height, width)`.
    name: A string, the name of the layer.
  """
    pool_function: Incomplete
    pool_size: Incomplete
    strides: Incomplete
    padding: Incomplete
    data_format: Incomplete
    input_spec: Incomplete
    def __init__(self, pool_function, pool_size, strides, padding: str = 'valid', data_format: Incomplete | None = None, name: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class MaxPooling2D(Pooling2D):
    '''Max pooling operation for 2D spatial data.

  Downsamples the input along its spatial dimensions (height and width)
  by taking the maximum value over an input window
  (of size defined by `pool_size`) for each channel of the input.
  The window is shifted by `strides` along each dimension.

  The resulting output,
  when using the `"valid"` padding option, has a spatial shape
  (number of rows or columns) of:
  `output_shape = math.floor((input_shape - pool_size) / strides) + 1`
  (when `input_shape >= pool_size`)

  The resulting output shape when using the `"same"` padding option is:
  `output_shape = math.floor((input_shape - 1) / strides) + 1`

  For example, for `strides=(1, 1)` and `padding="valid"`:

  >>> x = tf.constant([[1., 2., 3.],
  ...                  [4., 5., 6.],
  ...                  [7., 8., 9.]])
  >>> x = tf.reshape(x, [1, 3, 3, 1])
  >>> max_pool_2d = tf.keras.layers.MaxPooling2D(pool_size=(2, 2),
  ...    strides=(1, 1), padding=\'valid\')
  >>> max_pool_2d(x)
  <tf.Tensor: shape=(1, 2, 2, 1), dtype=float32, numpy=
    array([[[[5.],
             [6.]],
            [[8.],
             [9.]]]], dtype=float32)>

  For example, for `strides=(2, 2)` and `padding="valid"`:

  >>> x = tf.constant([[1., 2., 3., 4.],
  ...                  [5., 6., 7., 8.],
  ...                  [9., 10., 11., 12.]])
  >>> x = tf.reshape(x, [1, 3, 4, 1])
  >>> max_pool_2d = tf.keras.layers.MaxPooling2D(pool_size=(2, 2),
  ...    strides=(2, 2), padding=\'valid\')
  >>> max_pool_2d(x)
  <tf.Tensor: shape=(1, 1, 2, 1), dtype=float32, numpy=
    array([[[[6.],
             [8.]]]], dtype=float32)>

  Usage Example:

  >>> input_image = tf.constant([[[[1.], [1.], [2.], [4.]],
  ...                            [[2.], [2.], [3.], [2.]],
  ...                            [[4.], [1.], [1.], [1.]],
  ...                            [[2.], [2.], [1.], [4.]]]])
  >>> output = tf.constant([[[[1], [0]],
  ...                       [[0], [1]]]])
  >>> model = tf.keras.models.Sequential()
  >>> model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2),
  ...    input_shape=(4, 4, 1)))
  >>> model.compile(\'adam\', \'mean_squared_error\')
  >>> model.predict(input_image, steps=1)
  array([[[[2.],
           [4.]],
          [[4.],
           [4.]]]], dtype=float32)

  For example, for stride=(1, 1) and padding="same":

  >>> x = tf.constant([[1., 2., 3.],
  ...                  [4., 5., 6.],
  ...                  [7., 8., 9.]])
  >>> x = tf.reshape(x, [1, 3, 3, 1])
  >>> max_pool_2d = tf.keras.layers.MaxPooling2D(pool_size=(2, 2),
  ...    strides=(1, 1), padding=\'same\')
  >>> max_pool_2d(x)
  <tf.Tensor: shape=(1, 3, 3, 1), dtype=float32, numpy=
    array([[[[5.],
             [6.],
             [6.]],
            [[8.],
             [9.],
             [9.]],
            [[8.],
             [9.],
             [9.]]]], dtype=float32)>

  Args:
    pool_size: integer or tuple of 2 integers,
      window size over which to take the maximum.
      `(2, 2)` will take the max value over a 2x2 pooling window.
      If only one integer is specified, the same window length
      will be used for both dimensions.
    strides: Integer, tuple of 2 integers, or None.
      Strides values.  Specifies how far the pooling window moves
      for each pooling step. If None, it will default to `pool_size`.
    padding: One of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".

  Input shape:
    - If `data_format=\'channels_last\'`:
      4D tensor with shape `(batch_size, rows, cols, channels)`.
    - If `data_format=\'channels_first\'`:
      4D tensor with shape `(batch_size, channels, rows, cols)`.

  Output shape:
    - If `data_format=\'channels_last\'`:
      4D tensor with shape `(batch_size, pooled_rows, pooled_cols, channels)`.
    - If `data_format=\'channels_first\'`:
      4D tensor with shape `(batch_size, channels, pooled_rows, pooled_cols)`.

  Returns:
    A tensor of rank 4 representing the maximum pooled values.  See above for
    output shape.
  '''
    def __init__(self, pool_size=(2, 2), strides: Incomplete | None = None, padding: str = 'valid', data_format: Incomplete | None = None, **kwargs) -> None: ...

class AveragePooling2D(Pooling2D):
    '''Average pooling operation for spatial data.

  Downsamples the input along its spatial dimensions (height and width)
  by taking the average value over an input window
  (of size defined by `pool_size`) for each channel of the input.
  The window is shifted by `strides` along each dimension.

  The resulting output when using `"valid"` padding option has a shape
  (number of rows or columns) of:
  `output_shape = math.floor((input_shape - pool_size) / strides) + 1`
  (when `input_shape >= pool_size`)

  The resulting output shape when using the `"same"` padding option is:
  `output_shape = math.floor((input_shape - 1) / strides) + 1`

  For example, for `strides=(1, 1)` and `padding="valid"`:

  >>> x = tf.constant([[1., 2., 3.],
  ...                  [4., 5., 6.],
  ...                  [7., 8., 9.]])
  >>> x = tf.reshape(x, [1, 3, 3, 1])
  >>> avg_pool_2d = tf.keras.layers.AveragePooling2D(pool_size=(2, 2),
  ...    strides=(1, 1), padding=\'valid\')
  >>> avg_pool_2d(x)
  <tf.Tensor: shape=(1, 2, 2, 1), dtype=float32, numpy=
    array([[[[3.],
             [4.]],
            [[6.],
             [7.]]]], dtype=float32)>

  For example, for `stride=(2, 2)` and `padding="valid"`:

  >>> x = tf.constant([[1., 2., 3., 4.],
  ...                  [5., 6., 7., 8.],
  ...                  [9., 10., 11., 12.]])
  >>> x = tf.reshape(x, [1, 3, 4, 1])
  >>> avg_pool_2d = tf.keras.layers.AveragePooling2D(pool_size=(2, 2),
  ...    strides=(2, 2), padding=\'valid\')
  >>> avg_pool_2d(x)
  <tf.Tensor: shape=(1, 1, 2, 1), dtype=float32, numpy=
    array([[[[3.5],
             [5.5]]]], dtype=float32)>

  For example, for `strides=(1, 1)` and `padding="same"`:

  >>> x = tf.constant([[1., 2., 3.],
  ...                  [4., 5., 6.],
  ...                  [7., 8., 9.]])
  >>> x = tf.reshape(x, [1, 3, 3, 1])
  >>> avg_pool_2d = tf.keras.layers.AveragePooling2D(pool_size=(2, 2),
  ...    strides=(1, 1), padding=\'same\')
  >>> avg_pool_2d(x)
  <tf.Tensor: shape=(1, 3, 3, 1), dtype=float32, numpy=
    array([[[[3.],
             [4.],
             [4.5]],
            [[6.],
             [7.],
             [7.5]],
            [[7.5],
             [8.5],
             [9.]]]], dtype=float32)>

  Args:
    pool_size: integer or tuple of 2 integers,
      factors by which to downscale (vertical, horizontal).
      `(2, 2)` will halve the input in both spatial dimension.
      If only one integer is specified, the same window length
      will be used for both dimensions.
    strides: Integer, tuple of 2 integers, or None.
      Strides values.
      If None, it will default to `pool_size`.
    padding: One of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".

  Input shape:
    - If `data_format=\'channels_last\'`:
      4D tensor with shape `(batch_size, rows, cols, channels)`.
    - If `data_format=\'channels_first\'`:
      4D tensor with shape `(batch_size, channels, rows, cols)`.

  Output shape:
    - If `data_format=\'channels_last\'`:
      4D tensor with shape `(batch_size, pooled_rows, pooled_cols, channels)`.
    - If `data_format=\'channels_first\'`:
      4D tensor with shape `(batch_size, channels, pooled_rows, pooled_cols)`.
  '''
    def __init__(self, pool_size=(2, 2), strides: Incomplete | None = None, padding: str = 'valid', data_format: Incomplete | None = None, **kwargs) -> None: ...

class Pooling3D(Layer):
    """Pooling layer for arbitrary pooling functions, for 3D inputs.

  This class only exists for code reuse. It will never be an exposed API.

  Args:
    pool_function: The pooling function to apply, e.g. `tf.nn.max_pool2d`.
    pool_size: An integer or tuple/list of 3 integers:
      (pool_depth, pool_height, pool_width)
      specifying the size of the pooling window.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    strides: An integer or tuple/list of 3 integers,
      specifying the strides of the pooling operation.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    padding: A string. The padding method, either 'valid' or 'same'.
      Case-insensitive.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, depth, height, width, channels)`
      while `channels_first` corresponds to
      inputs with shape `(batch, channels, depth, height, width)`.
    name: A string, the name of the layer.
  """
    pool_function: Incomplete
    pool_size: Incomplete
    strides: Incomplete
    padding: Incomplete
    data_format: Incomplete
    input_spec: Incomplete
    def __init__(self, pool_function, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class MaxPooling3D(Pooling3D):
    '''Max pooling operation for 3D data (spatial or spatio-temporal).

  Downsamples the input along its spatial dimensions (depth, height, and width)
  by taking the maximum value over an input window
  (of size defined by `pool_size`) for each channel of the input.
  The window is shifted by `strides` along each dimension.

  Args:
    pool_size: Tuple of 3 integers,
      factors by which to downscale (dim1, dim2, dim3).
      `(2, 2, 2)` will halve the size of the 3D input in each dimension.
    strides: tuple of 3 integers, or None. Strides values.
    padding: One of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
      while `channels_first` corresponds to inputs with shape
      `(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".

  Input shape:
    - If `data_format=\'channels_last\'`:
      5D tensor with shape:
      `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
    - If `data_format=\'channels_first\'`:
      5D tensor with shape:
      `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

  Output shape:
    - If `data_format=\'channels_last\'`:
      5D tensor with shape:
      `(batch_size, pooled_dim1, pooled_dim2, pooled_dim3, channels)`
    - If `data_format=\'channels_first\'`:
      5D tensor with shape:
      `(batch_size, channels, pooled_dim1, pooled_dim2, pooled_dim3)`

  Example:

  ```python
  depth = 30
  height = 30
  width = 30
  input_channels = 3

  inputs = tf.keras.Input(shape=(depth, height, width, input_channels))
  layer = tf.keras.layers.MaxPooling3D(pool_size=3)
  outputs = layer(inputs)  # Shape: (batch_size, 10, 10, 10, 3)
  ```
  '''
    def __init__(self, pool_size=(2, 2, 2), strides: Incomplete | None = None, padding: str = 'valid', data_format: Incomplete | None = None, **kwargs) -> None: ...

class AveragePooling3D(Pooling3D):
    '''Average pooling operation for 3D data (spatial or spatio-temporal).

  Downsamples the input along its spatial dimensions (depth, height, and width)
  by taking the average value over an input window
  (of size defined by `pool_size`) for each channel of the input.
  The window is shifted by `strides` along each dimension.

  Args:
    pool_size: tuple of 3 integers,
      factors by which to downscale (dim1, dim2, dim3).
      `(2, 2, 2)` will halve the size of the 3D input in each dimension.
    strides: tuple of 3 integers, or None. Strides values.
    padding: One of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
      while `channels_first` corresponds to inputs with shape
      `(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".

  Input shape:
    - If `data_format=\'channels_last\'`:
      5D tensor with shape:
      `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
    - If `data_format=\'channels_first\'`:
      5D tensor with shape:
      `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

  Output shape:
    - If `data_format=\'channels_last\'`:
      5D tensor with shape:
      `(batch_size, pooled_dim1, pooled_dim2, pooled_dim3, channels)`
    - If `data_format=\'channels_first\'`:
      5D tensor with shape:
      `(batch_size, channels, pooled_dim1, pooled_dim2, pooled_dim3)`

  Example:

  ```python
  depth = 30
  height = 30
  width = 30
  input_channels = 3

  inputs = tf.keras.Input(shape=(depth, height, width, input_channels))
  layer = tf.keras.layers.AveragePooling3D(pool_size=3)
  outputs = layer(inputs)  # Shape: (batch_size, 10, 10, 10, 3)
  ```
  '''
    def __init__(self, pool_size=(2, 2, 2), strides: Incomplete | None = None, padding: str = 'valid', data_format: Incomplete | None = None, **kwargs) -> None: ...

class GlobalPooling1D(Layer):
    """Abstract class for different global pooling 1D layers."""
    input_spec: Incomplete
    data_format: Incomplete
    keepdims: Incomplete
    def __init__(self, data_format: str = 'channels_last', keepdims: bool = False, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling1D(GlobalPooling1D):
    """Global average pooling operation for temporal data.

  Examples:

  >>> input_shape = (2, 3, 4)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.GlobalAveragePooling1D()(x)
  >>> print(y.shape)
  (2, 4)

  Args:
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, steps, features)` while `channels_first`
      corresponds to inputs with shape
      `(batch, features, steps)`.
    keepdims: A boolean, whether to keep the temporal dimension or not.
      If `keepdims` is `False` (default), the rank of the tensor is reduced
      for spatial dimensions.
      If `keepdims` is `True`, the temporal dimension are retained with
      length 1.
      The behavior is the same as for `tf.reduce_mean` or `np.mean`.

  Call arguments:
    inputs: A 3D tensor.
    mask: Binary tensor of shape `(batch_size, steps)` indicating whether
      a given step should be masked (excluded from the average).

  Input shape:
    - If `data_format='channels_last'`:
      3D tensor with shape:
      `(batch_size, steps, features)`
    - If `data_format='channels_first'`:
      3D tensor with shape:
      `(batch_size, features, steps)`

  Output shape:
    - If `keepdims`=False:
      2D tensor with shape `(batch_size, features)`.
    - If `keepdims`=True:
      - If `data_format='channels_last'`:
        3D tensor with shape `(batch_size, 1, features)`
      - If `data_format='channels_first'`:
        3D tensor with shape `(batch_size, features, 1)`
  """
    supports_masking: bool
    def __init__(self, data_format: str = 'channels_last', **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None) -> None: ...

class GlobalMaxPooling1D(GlobalPooling1D):
    """Global max pooling operation for 1D temporal data.

  Downsamples the input representation by taking the maximum value over
  the time dimension.

  For example:

  >>> x = tf.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
  >>> x = tf.reshape(x, [3, 3, 1])
  >>> x
  <tf.Tensor: shape=(3, 3, 1), dtype=float32, numpy=
  array([[[1.], [2.], [3.]],
         [[4.], [5.], [6.]],
         [[7.], [8.], [9.]]], dtype=float32)>
  >>> max_pool_1d = tf.keras.layers.GlobalMaxPooling1D()
  >>> max_pool_1d(x)
  <tf.Tensor: shape=(3, 1), dtype=float32, numpy=
  array([[3.],
         [6.],
         [9.], dtype=float32)>

  Args:
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, steps, features)` while `channels_first`
      corresponds to inputs with shape
      `(batch, features, steps)`.
    keepdims: A boolean, whether to keep the temporal dimension or not.
      If `keepdims` is `False` (default), the rank of the tensor is reduced
      for spatial dimensions.
      If `keepdims` is `True`, the temporal dimension are retained with
      length 1.
      The behavior is the same as for `tf.reduce_max` or `np.max`.

  Input shape:
    - If `data_format='channels_last'`:
      3D tensor with shape:
      `(batch_size, steps, features)`
    - If `data_format='channels_first'`:
      3D tensor with shape:
      `(batch_size, features, steps)`

  Output shape:
    - If `keepdims`=False:
      2D tensor with shape `(batch_size, features)`.
    - If `keepdims`=True:
      - If `data_format='channels_last'`:
        3D tensor with shape `(batch_size, 1, features)`
      - If `data_format='channels_first'`:
        3D tensor with shape `(batch_size, features, 1)`
  """
    def call(self, inputs): ...

class GlobalPooling2D(Layer):
    """Abstract class for different global pooling 2D layers.
  """
    data_format: Incomplete
    input_spec: Incomplete
    keepdims: Incomplete
    def __init__(self, data_format: Incomplete | None = None, keepdims: bool = False, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling2D(GlobalPooling2D):
    '''Global average pooling operation for spatial data.

  Examples:

  >>> input_shape = (2, 4, 5, 3)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.GlobalAveragePooling2D()(x)
  >>> print(y.shape)
  (2, 3)

  Args:
      data_format: A string,
        one of `channels_last` (default) or `channels_first`.
        The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, height, width, channels)` while `channels_first`
        corresponds to inputs with shape
        `(batch, channels, height, width)`.
        It defaults to the `image_data_format` value found in your
        Keras config file at `~/.keras/keras.json`.
        If you never set it, then it will be "channels_last".
      keepdims: A boolean, whether to keep the spatial dimensions or not.
        If `keepdims` is `False` (default), the rank of the tensor is reduced
        for spatial dimensions.
        If `keepdims` is `True`, the spatial dimensions are retained with
        length 1.
        The behavior is the same as for `tf.reduce_mean` or `np.mean`.

  Input shape:
    - If `data_format=\'channels_last\'`:
      4D tensor with shape `(batch_size, rows, cols, channels)`.
    - If `data_format=\'channels_first\'`:
      4D tensor with shape `(batch_size, channels, rows, cols)`.

  Output shape:
    - If `keepdims`=False:
      2D tensor with shape `(batch_size, channels)`.
    - If `keepdims`=True:
      - If `data_format=\'channels_last\'`:
        4D tensor with shape `(batch_size, 1, 1, channels)`
      - If `data_format=\'channels_first\'`:
        4D tensor with shape `(batch_size, channels, 1, 1)`
  '''
    def call(self, inputs): ...

class GlobalMaxPooling2D(GlobalPooling2D):
    '''Global max pooling operation for spatial data.

  Examples:

  >>> input_shape = (2, 4, 5, 3)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.GlobalMaxPool2D()(x)
  >>> print(y.shape)
  (2, 3)

  Args:
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    keepdims: A boolean, whether to keep the spatial dimensions or not.
      If `keepdims` is `False` (default), the rank of the tensor is reduced
      for spatial dimensions.
      If `keepdims` is `True`, the spatial dimensions are retained with
      length 1.
      The behavior is the same as for `tf.reduce_max` or `np.max`.

  Input shape:
    - If `data_format=\'channels_last\'`:
      4D tensor with shape `(batch_size, rows, cols, channels)`.
    - If `data_format=\'channels_first\'`:
      4D tensor with shape `(batch_size, channels, rows, cols)`.

  Output shape:
    - If `keepdims`=False:
      2D tensor with shape `(batch_size, channels)`.
    - If `keepdims`=True:
      - If `data_format=\'channels_last\'`:
        4D tensor with shape `(batch_size, 1, 1, channels)`
      - If `data_format=\'channels_first\'`:
        4D tensor with shape `(batch_size, channels, 1, 1)`
  '''
    def call(self, inputs): ...

class GlobalPooling3D(Layer):
    """Abstract class for different global pooling 3D layers."""
    data_format: Incomplete
    input_spec: Incomplete
    keepdims: Incomplete
    def __init__(self, data_format: Incomplete | None = None, keepdims: bool = False, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class GlobalAveragePooling3D(GlobalPooling3D):
    '''Global Average pooling operation for 3D data.

  Args:
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
      while `channels_first` corresponds to inputs with shape
      `(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    keepdims: A boolean, whether to keep the spatial dimensions or not.
      If `keepdims` is `False` (default), the rank of the tensor is reduced
      for spatial dimensions.
      If `keepdims` is `True`, the spatial dimensions are retained with
      length 1.
      The behavior is the same as for `tf.reduce_mean` or `np.mean`.

  Input shape:
    - If `data_format=\'channels_last\'`:
      5D tensor with shape:
      `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
    - If `data_format=\'channels_first\'`:
      5D tensor with shape:
      `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

  Output shape:
    - If `keepdims`=False:
      2D tensor with shape `(batch_size, channels)`.
    - If `keepdims`=True:
      - If `data_format=\'channels_last\'`:
        5D tensor with shape `(batch_size, 1, 1, 1, channels)`
      - If `data_format=\'channels_first\'`:
        5D tensor with shape `(batch_size, channels, 1, 1, 1)`
  '''
    def call(self, inputs): ...

class GlobalMaxPooling3D(GlobalPooling3D):
    '''Global Max pooling operation for 3D data.

  Args:
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
      while `channels_first` corresponds to inputs with shape
      `(batch, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    keepdims: A boolean, whether to keep the spatial dimensions or not.
      If `keepdims` is `False` (default), the rank of the tensor is reduced
      for spatial dimensions.
      If `keepdims` is `True`, the spatial dimensions are retained with
      length 1.
      The behavior is the same as for `tf.reduce_max` or `np.max`.

  Input shape:
    - If `data_format=\'channels_last\'`:
      5D tensor with shape:
      `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
    - If `data_format=\'channels_first\'`:
      5D tensor with shape:
      `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`

  Output shape:
    - If `keepdims`=False:
      2D tensor with shape `(batch_size, channels)`.
    - If `keepdims`=True:
      - If `data_format=\'channels_last\'`:
        5D tensor with shape `(batch_size, 1, 1, 1, channels)`
      - If `data_format=\'channels_first\'`:
        5D tensor with shape `(batch_size, channels, 1, 1, 1)`
  '''
    def call(self, inputs): ...
AvgPool1D = AveragePooling1D
MaxPool1D = MaxPooling1D
AvgPool2D = AveragePooling2D
MaxPool2D = MaxPooling2D
AvgPool3D = AveragePooling3D
MaxPool3D = MaxPooling3D
GlobalMaxPool1D = GlobalMaxPooling1D
GlobalMaxPool2D = GlobalMaxPooling2D
GlobalMaxPool3D = GlobalMaxPooling3D
GlobalAvgPool1D = GlobalAveragePooling1D
GlobalAvgPool2D = GlobalAveragePooling2D
GlobalAvgPool3D = GlobalAveragePooling3D
