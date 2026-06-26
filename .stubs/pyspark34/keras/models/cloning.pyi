from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import functional as functional, sequential as sequential, training as training, training_v1 as training_v1
from keras.engine.base_layer import AddMetric as AddMetric, Layer as Layer
from keras.engine.input_layer import Input as Input, InputLayer as InputLayer
from keras.optimizers import optimizer_v1 as optimizer_v1
from keras.saving.legacy import serialization as serialization
from keras.saving.object_registration import CustomObjectScope as CustomObjectScope
from keras.utils import generic_utils as generic_utils, version_utils as version_utils

Model = training.Model
Sequential = sequential.Sequential

def share_weights(layer): ...
def clone_model(model, input_tensors: Incomplete | None = None, clone_function: Incomplete | None = None):
    """Clone a Functional or Sequential `Model` instance.

    Model cloning is similar to calling a model on new inputs,
    except that it creates new layers (and thus new weights) instead
    of sharing the weights of the existing layers.

    Note that
    `clone_model` will not preserve the uniqueness of shared objects within the
    model (e.g. a single variable attached to two distinct layers will be
    restored as two separate variables).

    Args:
        model: Instance of `Model`
            (could be a Functional model or a Sequential model).
        input_tensors: optional list of input tensors or InputLayer objects
            to build the model upon. If not provided,
            new `Input` objects will be created.
        clone_function: Callable to be used to clone each layer in the target
            model (except `InputLayer` instances). It takes as argument the
            layer instance to be cloned, and returns the corresponding layer
            instance to be used in the model copy. If unspecified, this callable
            defaults to the following serialization/deserialization function:
            `lambda layer: layer.__class__.from_config(layer.get_config())`.
            By passing a custom callable, you can customize your copy of the
            model, e.g. by wrapping certain layers of interest (you might want
            to replace all `LSTM` instances with equivalent
            `Bidirectional(LSTM(...))` instances, for example).

    Returns:
      An instance of `Model` reproducing the behavior
      of the original model, on top of new inputs tensors,
      using newly instantiated weights. The cloned model may behave
      differently from the original model if a custom `clone_function`
      modifies the layer.

    Example:

    ```python
    # Create a test Sequential model.
    model = keras.Sequential([
        keras.Input(shape=(728,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid'),
    ])
    # Create a copy of the test model (with freshly initialized weights).
    new_model = clone_model(model)
    ```

    Note that subclassed models cannot be cloned, since their internal
    layer structure is not known. To achieve equivalent functionality
    as `clone_model` in the case of a subclassed model, simply make sure
    that the model class implements `get_config()`
    (and optionally `from_config()`), and call:

    ```python
    new_model = model.__class__.from_config(model.get_config())
    ```
    """
def in_place_subclassed_model_state_restoration(model) -> None:
    '''Restores the original state of a model after it was "reset".

    This undoes this action of `_in_place_subclassed_model_reset`, which is
    called in `clone_and_build_model` if `in_place_reset` is set to True.

    Args:
      model: Instance of a Keras model created via subclassing, on which
        `_in_place_subclassed_model_reset` was previously called.
    '''
def clone_and_build_model(model, input_tensors: Incomplete | None = None, target_tensors: Incomplete | None = None, custom_objects: Incomplete | None = None, compile_clone: bool = True, in_place_reset: bool = False, optimizer_iterations: Incomplete | None = None, optimizer_config: Incomplete | None = None):
    """Clone a `Model` and build/compile it with the same settings used before.

    This function can be run in the same graph or in a separate graph from the
    model. When using a separate graph, `in_place_reset` must be `False`.

    Note that, currently, the clone produced from this function may not work
    with TPU DistributionStrategy. Try at your own risk.

    Args:
      model: `tf.keras.Model` object. Can be Functional, Sequential, or
        sub-classed.
      input_tensors: Optional list or dictionary of input tensors to build the
        model upon. If not provided, placeholders will be created.
      target_tensors: Optional list of target tensors for compiling the model.
        If not provided, placeholders will be created.
      custom_objects: Optional dictionary mapping string names to custom classes
        or functions.
      compile_clone: Boolean, whether to compile model clone (default `True`).
      in_place_reset: Boolean, whether to reset the model in place. Only used if
        the model is a subclassed model. In the case of a subclassed model,
        this argument must be set to `True` (default `False`). To restore the
        original model, use the function
        `in_place_subclassed_model_state_restoration(model)`.
      optimizer_iterations: An iterations variable that will be incremented by
        the optimizer if the clone is compiled. This argument is used when a
        Keras model is cloned into an Estimator model function, because
        Estimators create their own global step variable.
      optimizer_config: Optimizer config dictionary or list of dictionary
        returned from `get_config()`. This argument should be defined if
        `clone_and_build_model` is called in a different graph or session from
        the original model, and the optimizer is an instance of `OptimizerV2`.

    Returns:
      Clone of the model.

    Raises:
      ValueError: Cloning fails in the following cases
        - cloning a subclassed model with `in_place_reset` set to False.
        - compiling the clone when the original model has not been compiled.
    """
