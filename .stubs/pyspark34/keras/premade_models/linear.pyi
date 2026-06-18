from _typeshed import Incomplete
from keras import activations as activations, initializers as initializers, regularizers as regularizers
from keras.engine import base_layer as base_layer, input_spec as input_spec, training as training
from keras.layers import core as core

class LinearModel(training.Model):
    """Linear Model for regression and classification problems.

    This model approximates the following function:
    $$y = \\beta + \\sum_{i=1}^{N} w_{i} * x_{i}$$
    where $$\\beta$$ is the bias and $$w_{i}$$ is the weight for each feature.

    Example:

    ```python
    model = LinearModel()
    model.compile(optimizer='sgd', loss='mse')
    model.fit(x, y, epochs=epochs)
    ```

    This model accepts sparse float inputs as well:

    Example:
    ```python
    model = LinearModel()
    opt = tf.keras.optimizers.Adam()
    loss_fn = tf.keras.losses.MeanSquaredError()
    with tf.GradientTape() as tape:
      output = model(sparse_input)
      loss = tf.reduce_mean(loss_fn(target, output))
    grads = tape.gradient(loss, model.weights)
    opt.apply_gradients(zip(grads, model.weights))
    ```

    """
    units: Incomplete
    activation: Incomplete
    use_bias: Incomplete
    kernel_initializer: Incomplete
    bias_initializer: Incomplete
    kernel_regularizer: Incomplete
    bias_regularizer: Incomplete
    def __init__(self, units: int = 1, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'zeros', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, **kwargs) -> None:
        """Create a Linear Model.

        Args:
          units: Positive integer, output dimension without the batch size.
          activation: Activation function to use.
            If you don't specify anything, no activation is applied.
          use_bias: whether to calculate the bias/intercept for this model. If
            set to False, no bias/intercept will be used in calculations, e.g.,
            the data is already centered.
          kernel_initializer: Initializer for the `kernel` weights matrices.
          bias_initializer: Initializer for the bias vector.
          kernel_regularizer: regularizer for kernel vectors.
          bias_regularizer: regularizer for bias vector.
          **kwargs: The keyword arguments that are passed on to
            BaseLayer.__init__.
        """
    input_specs: Incomplete
    dense_layers: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
