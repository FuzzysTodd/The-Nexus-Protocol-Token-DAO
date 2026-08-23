from _typeshed import Incomplete
from keras import activations as activations, backend as backend
from keras.engine import base_layer as base_layer, data_adapter as data_adapter, training as keras_training
from keras.saving.legacy import serialization as serialization

class WideDeepModel(keras_training.Model):
    """Wide & Deep Model for regression and classification problems.

    This model jointly train a linear and a dnn model.

    Example:

    ```python
    linear_model = LinearModel()
    dnn_model = keras.Sequential([keras.layers.Dense(units=64),
                                 keras.layers.Dense(units=1)])
    combined_model = WideDeepModel(linear_model, dnn_model)
    combined_model.compile(optimizer=['sgd', 'adam'],
                           loss='mse', metrics=['mse'])
    # define dnn_inputs and linear_inputs as separate numpy arrays or
    # a single numpy array if dnn_inputs is same as linear_inputs.
    combined_model.fit([linear_inputs, dnn_inputs], y, epochs)
    # or define a single `tf.data.Dataset` that contains a single tensor or
    # separate tensors for dnn_inputs and linear_inputs.
    dataset = tf.data.Dataset.from_tensors(([linear_inputs, dnn_inputs], y))
    combined_model.fit(dataset, epochs)
    ```

    Both linear and dnn model can be pre-compiled and trained separately
    before jointly training:

    Example:
    ```python
    linear_model = LinearModel()
    linear_model.compile('adagrad', 'mse')
    linear_model.fit(linear_inputs, y, epochs)
    dnn_model = keras.Sequential([keras.layers.Dense(units=1)])
    dnn_model.compile('rmsprop', 'mse')
    dnn_model.fit(dnn_inputs, y, epochs)
    combined_model = WideDeepModel(linear_model, dnn_model)
    combined_model.compile(optimizer=['sgd', 'adam'],
                           loss='mse', metrics=['mse'])
    combined_model.fit([linear_inputs, dnn_inputs], y, epochs)
    ```

    """
    linear_model: Incomplete
    dnn_model: Incomplete
    activation: Incomplete
    def __init__(self, linear_model, dnn_model, activation: Incomplete | None = None, **kwargs) -> None:
        """Create a Wide & Deep Model.

        Args:
          linear_model: a premade LinearModel, its output must match the output
            of the dnn model.
          dnn_model: a `tf.keras.Model`, its output must match the output of the
            linear model.
          activation: Activation function. Set it to None to maintain a linear
            activation.
          **kwargs: The keyword arguments that are passed on to
            BaseLayer.__init__. Allowed keyword arguments include `name`.
        """
    def call(self, inputs, training: Incomplete | None = None): ...
    def train_step(self, data): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
