from keras.engine import base_preprocessing_layer as base_preprocessing_layer, functional as functional, sequential as sequential
from keras.utils import tf_utils as tf_utils

class PreprocessingStage(sequential.Sequential, base_preprocessing_layer.PreprocessingLayer):
    """A sequential preprocessing stage.

    This preprocessing stage wraps a list of preprocessing layers into a
    Sequential-like object that enables you to `adapt()` the whole list via
    a single `adapt()` call on the preprocessing stage.

    Args:
      layers: List of layers. Can include layers that aren't preprocessing
        layers.
      name: String. Optional name for the preprocessing stage object.
    """
    def adapt(self, data, reset_state: bool = True):
        """Adapt the state of the layers of the preprocessing stage to the data.

        Args:
          data: A batched Dataset object, or a NumPy array, or an EagerTensor.
            Data to be iterated over to adapt the state of the layers in this
            preprocessing stage.
          reset_state: Whether this call to `adapt` should reset the state of
            the layers in this preprocessing stage.
        """

class FunctionalPreprocessingStage(functional.Functional, base_preprocessing_layer.PreprocessingLayer):
    """A functional preprocessing stage.

    This preprocessing stage wraps a graph of preprocessing layers into a
    Functional-like object that enables you to `adapt()` the whole graph via
    a single `adapt()` call on the preprocessing stage.

    Preprocessing stage is not a complete model, so it cannot be called with
    `fit()`. However, it is possible to add regular layers that may be trainable
    to a preprocessing stage.

    A functional preprocessing stage is created in the same way as `Functional`
    models. A stage can be instantiated by passing two arguments to
    `__init__`. The first argument is the `keras.Input` Tensors that represent
    the inputs to the stage. The second argument specifies the output
    tensors that represent the outputs of this stage. Both arguments can be a
    nested structure of tensors.

    Example:

    >>> inputs = {'x2': tf.keras.Input(shape=(5,)),
    ...           'x1': tf.keras.Input(shape=(1,))}
    >>> norm_layer = tf.keras.layers.Normalization()
    >>> y = norm_layer(inputs['x2'])
    >>> y, z = tf.keras.layers.Lambda(lambda x: (x, x))(inputs['x1'])
    >>> outputs = [inputs['x1'], [y, z]]
    >>> stage = FunctionalPreprocessingStage(inputs, outputs)

    Args:
      inputs: An input tensor (must be created via `tf.keras.Input()`), or a
        list, a dict, or a nested structure of input tensors.
      outputs: An output tensor, or a list, a dict or a nested structure of
        output tensors.
      name: String, optional. Name of the preprocessing stage.
    """
    def fit(self, *args, **kwargs) -> None: ...
    def adapt(self, data, reset_state: bool = True):
        """Adapt the state of the layers of the preprocessing stage to the data.

        Args:
          data: A batched Dataset object, a NumPy array, an EagerTensor, or a
            list, dict or nested structure of Numpy Arrays or EagerTensors. The
            elements of Dataset object need to conform with inputs of the stage.
            The first dimension of NumPy arrays or EagerTensors are understood
            to be batch dimension. Data to be iterated over to adapt the state
            of the layers in this preprocessing stage.
          reset_state: Whether this call to `adapt` should reset the state of
            the layers in this preprocessing stage.

        Examples:

        >>> # For a stage with dict input
        >>> inputs = {'x2': tf.keras.Input(shape=(5,)),
        ...           'x1': tf.keras.Input(shape=(1,))}
        >>> outputs = [inputs['x1'], inputs['x2']]
        >>> stage = FunctionalPreprocessingStage(inputs, outputs)
        >>> ds = tf.data.Dataset.from_tensor_slices({'x1': tf.ones((4,5)),
        ...                                          'x2': tf.ones((4,1))})
        >>> sorted(ds.element_spec.items()) # Check element_spec
        [('x1', TensorSpec(shape=(5,), dtype=tf.float32, name=None)),
         ('x2', TensorSpec(shape=(1,), dtype=tf.float32, name=None))]
        >>> stage.adapt(ds)
        >>> data_np = {'x1': np.ones((4, 5)), 'x2': np.ones((4, 1))}
        >>> stage.adapt(data_np)

        """
