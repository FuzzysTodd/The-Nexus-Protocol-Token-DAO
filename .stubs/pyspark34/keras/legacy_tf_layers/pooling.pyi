from _typeshed import Incomplete
from keras import layers as keras_layers
from keras.legacy_tf_layers import base as base

class AveragePooling1D(keras_layers.AveragePooling1D, base.Layer):
    """Average Pooling layer for 1D inputs.

    Args:
      pool_size: An integer or tuple/list of a single integer,
        representing the size of the pooling window.
      strides: An integer or tuple/list of a single integer, specifying the
        strides of the pooling operation.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string, one of `channels_last` (default) or
        `channels_first`. The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, length, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, length)`.
      name: A string, the name of the layer.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.AveragePooling1D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     pooling = tf.compat.v1.layers.AveragePooling1D(pool_size=2, strides=2)
    ```

    After:

    ```python
     pooling = tf.keras.layers.AveragePooling1D(pool_size=2, strides=2)
    ```
    @end_compatibility
    """
    def __init__(self, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...

def average_pooling1d(inputs, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None):
    """Average Pooling layer for 1D inputs.

    Args:
      inputs: The tensor over which to pool. Must have rank 3.
      pool_size: An integer or tuple/list of a single integer,
        representing the size of the pooling window.
      strides: An integer or tuple/list of a single integer, specifying the
        strides of the pooling operation.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string, one of `channels_last` (default) or
        `channels_first`. The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, length, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, length)`.
      name: A string, the name of the layer.

    Returns:
      The output tensor, of rank 3.

    Raises:
      ValueError: if eager execution is enabled.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.AveragePooling1D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     y = tf.compat.v1.layers.average_pooling1d(x, pool_size=2, strides=2)
    ```

    After:

    To migrate code using TF1 functional layers use the [Keras Functional API]
    (https://www.tensorflow.org/guide/keras/functional):

    ```python
     x = tf.keras.Input((28, 28, 1))
     y = tf.keras.layers.AveragePooling1D(pool_size=2, strides=2)(x)
     model = tf.keras.Model(x, y)
    ```
    @end_compatibility
    """

class MaxPooling1D(keras_layers.MaxPooling1D, base.Layer):
    """Max Pooling layer for 1D inputs.

    Args:
      pool_size: An integer or tuple/list of a single integer,
        representing the size of the pooling window.
      strides: An integer or tuple/list of a single integer, specifying the
        strides of the pooling operation.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string, one of `channels_last` (default) or
        `channels_first`. The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, length, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, length)`.
      name: A string, the name of the layer.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.MaxPooling1D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     pooling = tf.compat.v1.layers.MaxPooling1D(pool_size=2, strides=2)
    ```

    After:

    ```python
     pooling = tf.keras.layers.MaxPooling1D(pool_size=2, strides=2)
    ```
    @end_compatibility
    """
    def __init__(self, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...

def max_pooling1d(inputs, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None):
    """Max Pooling layer for 1D inputs.

    Args:
      inputs: The tensor over which to pool. Must have rank 3.
      pool_size: An integer or tuple/list of a single integer,
        representing the size of the pooling window.
      strides: An integer or tuple/list of a single integer, specifying the
        strides of the pooling operation.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string, one of `channels_last` (default) or
        `channels_first`. The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, length, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, length)`.
      name: A string, the name of the layer.

    Returns:
      The output tensor, of rank 3.

    Raises:
      ValueError: if eager execution is enabled.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.MaxPooling1D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     y = tf.compat.v1.layers.max_pooling1d(x, pool_size=2, strides=2)
    ```

    After:

    To migrate code using TF1 functional layers use the [Keras Functional API]
    (https://www.tensorflow.org/guide/keras/functional):

    ```python
     x = tf.keras.Input((28, 28, 1))
     y = tf.keras.layers.MaxPooling1D(pool_size=2, strides=2)(x)
     model = tf.keras.Model(x, y)
    ```
    @end_compatibility
    """

class AveragePooling2D(keras_layers.AveragePooling2D, base.Layer):
    """Average pooling layer for 2D inputs (e.g. images).

    Args:
      pool_size: An integer or tuple/list of 2 integers: (pool_height,
        pool_width) specifying the size of the pooling window.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      strides: An integer or tuple/list of 2 integers,
        specifying the strides of the pooling operation.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape
        `(batch, height, width, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, height, width)`.
      name: A string, the name of the layer.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.AveragePooling2D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     pooling = tf.compat.v1.layers.AveragePooling2D(pool_size=2, strides=2)
    ```

    After:

    ```python
     pooling = tf.keras.layers.AveragePooling2D(pool_size=2, strides=2)
    ```
    @end_compatibility
    """
    def __init__(self, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...

def average_pooling2d(inputs, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None):
    """Average pooling layer for 2D inputs (e.g. images).

    Args:
      inputs: The tensor over which to pool. Must have rank 4.
      pool_size: An integer or tuple/list of 2 integers: (pool_height,
        pool_width) specifying the size of the pooling window.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      strides: An integer or tuple/list of 2 integers,
        specifying the strides of the pooling operation.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape
        `(batch, height, width, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, height, width)`.
      name: A string, the name of the layer.

    Returns:
      Output tensor.

    Raises:
      ValueError: if eager execution is enabled.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.AveragePooling2D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     y = tf.compat.v1.layers.average_pooling2d(x, pool_size=2, strides=2)
    ```

    After:

    To migrate code using TF1 functional layers use the [Keras Functional API]
    (https://www.tensorflow.org/guide/keras/functional):

    ```python
     x = tf.keras.Input((28, 28, 1))
     y = tf.keras.layers.AveragePooling2D(pool_size=2, strides=2)(x)
     model = tf.keras.Model(x, y)
    ```
    @end_compatibility
    """

class MaxPooling2D(keras_layers.MaxPooling2D, base.Layer):
    """Max pooling layer for 2D inputs (e.g. images).

    Args:
      pool_size: An integer or tuple/list of 2 integers: (pool_height,
        pool_width) specifying the size of the pooling window.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      strides: An integer or tuple/list of 2 integers,
        specifying the strides of the pooling operation.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape
        `(batch, height, width, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, height, width)`.
      name: A string, the name of the layer.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.MaxPooling2D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     pooling = tf.compat.v1.layers.MaxPooling2D(pool_size=2, strides=2)
    ```

    After:

    ```python
     pooling = tf.keras.layers.MaxPooling2D(pool_size=2, strides=2)
    ```
    @end_compatibility
    """
    def __init__(self, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...

def max_pooling2d(inputs, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None):
    """Max pooling layer for 2D inputs (e.g. images).

    Args:
      inputs: The tensor over which to pool. Must have rank 4.
      pool_size: An integer or tuple/list of 2 integers: (pool_height,
        pool_width) specifying the size of the pooling window.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      strides: An integer or tuple/list of 2 integers,
        specifying the strides of the pooling operation.
        Can be a single integer to specify the same value for
        all spatial dimensions.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape
        `(batch, height, width, channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, height, width)`.
      name: A string, the name of the layer.

    Returns:
      Output tensor.

    Raises:
      ValueError: if eager execution is enabled.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.MaxPooling2D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     y = tf.compat.v1.layers.max_pooling2d(x, pool_size=2, strides=2)
    ```

    After:

    To migrate code using TF1 functional layers use the [Keras Functional API]
    (https://www.tensorflow.org/guide/keras/functional):

    ```python
     x = tf.keras.Input((28, 28, 1))
     y = tf.keras.layers.MaxPooling2D(pool_size=2, strides=2)(x)
     model = tf.keras.Model(x, y)
    ```
    @end_compatibility
    """

class AveragePooling3D(keras_layers.AveragePooling3D, base.Layer):
    """Average pooling layer for 3D inputs (e.g. volumes).

    Args:
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
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape
        `(batch, depth, height, width, channels)` while `channels_first`
        corresponds to inputs with shape
        `(batch, channels, depth, height, width)`.
      name: A string, the name of the layer.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.AveragePooling3D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     pooling = tf.compat.v1.layers.AveragePooling3D(pool_size=2, strides=2)
    ```

    After:

    ```python
     pooling = tf.keras.layers.AveragePooling3D(pool_size=2, strides=2)
    ```
    @end_compatibility
    """
    def __init__(self, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...

def average_pooling3d(inputs, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None):
    """Average pooling layer for 3D inputs (e.g. volumes).

    Args:
      inputs: The tensor over which to pool. Must have rank 5.
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
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape
        `(batch, depth, height, width, channels)` while `channels_first`
        corresponds to inputs with shape
        `(batch, channels, depth, height, width)`.
      name: A string, the name of the layer.

    Returns:
      Output tensor.

    Raises:
      ValueError: if eager execution is enabled.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.AveragePooling3D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     y = tf.compat.v1.layers.average_pooling3d(x, pool_size=2, strides=2)
    ```

    After:

    To migrate code using TF1 functional layers use the [Keras Functional API]
    (https://www.tensorflow.org/guide/keras/functional):

    ```python
     x = tf.keras.Input((28, 28, 1))
     y = tf.keras.layers.AveragePooling3D(pool_size=2, strides=2)(x)
     model = tf.keras.Model(x, y)
    ```
    @end_compatibility
    """

class MaxPooling3D(keras_layers.MaxPooling3D, base.Layer):
    """Max pooling layer for 3D inputs (e.g. volumes).

    Args:
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
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape
        `(batch, depth, height, width, channels)` while `channels_first`
        corresponds to inputs with shape
        `(batch, channels, depth, height, width)`.
      name: A string, the name of the layer.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.MaxPooling3D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     pooling = tf.compat.v1.layers.MaxPooling3D(pool_size=2, strides=2)
    ```

    After:

    ```python
     pooling = tf.keras.layers.MaxPooling3D(pool_size=2, strides=2)
    ```
    @end_compatibility
    """
    def __init__(self, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None, **kwargs) -> None: ...

def max_pooling3d(inputs, pool_size, strides, padding: str = 'valid', data_format: str = 'channels_last', name: Incomplete | None = None):
    """Max pooling layer for 3D inputs (e.g.

    volumes).

    Args:
      inputs: The tensor over which to pool. Must have rank 5.
      pool_size: An integer or tuple/list of 3 integers: (pool_depth,
        pool_height, pool_width) specifying the size of the pooling window. Can
        be a single integer to specify the same value for all spatial
        dimensions.
      strides: An integer or tuple/list of 3 integers, specifying the strides of
        the pooling operation. Can be a single integer to specify the same value
        for all spatial dimensions.
      padding: A string. The padding method, either 'valid' or 'same'.
        Case-insensitive.
      data_format: A string. The ordering of the dimensions in the inputs.
        `channels_last` (default) and `channels_first` are supported.
        `channels_last` corresponds to inputs with shape `(batch, depth, height,
        width, channels)` while `channels_first` corresponds to inputs with
        shape `(batch, channels, depth, height, width)`.
      name: A string, the name of the layer.

    Returns:
      Output tensor.

    Raises:
      ValueError: if eager execution is enabled.


    @compatibility(TF2)
    This API is a legacy api that is only compatible with eager execution and
    `tf.function` if you combine it with
    `tf.compat.v1.keras.utils.track_tf1_style_variables`

    Please refer to [tf.layers model mapping section of the migration guide]
    (https://www.tensorflow.org/guide/migrate/model_mapping)
    to learn how to use your TensorFlow v1 model in TF2 with Keras.

    The corresponding TensorFlow v2 layer is
    `tf.keras.layers.MaxPooling3D`.


    #### Structural Mapping to Native TF2

    None of the supported arguments have changed name.

    Before:

    ```python
     y = tf.compat.v1.layers.max_pooling3d(x, pool_size=2, strides=2)
    ```

    After:

    To migrate code using TF1 functional layers use the [Keras Functional API]
    (https://www.tensorflow.org/guide/keras/functional):

    ```python
     x = tf.keras.Input((28, 28, 1))
     y = tf.keras.layers.MaxPooling3D(pool_size=2, strides=2)(x)
     model = tf.keras.Model(x, y)
    ```
    @end_compatibility
    """
AvgPool2D = AveragePooling2D
MaxPool2D = MaxPooling2D
max_pool2d = max_pooling2d
avg_pool2d = average_pooling2d
