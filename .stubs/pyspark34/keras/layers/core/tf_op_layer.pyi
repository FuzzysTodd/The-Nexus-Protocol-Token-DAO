import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import keras_tensor as keras_tensor
from keras.engine.base_layer import Layer as Layer

class ClassMethod(Layer):
    """Wraps a TF API Class's class method  in a `Layer` object.

    It is inserted by the Functional API construction whenever users call
    a supported TF Class's class method on KerasTensors.

    This is useful in the case where users do something like:
    x = keras.Input(...)
    y = keras.Input(...)
    out = tf.RaggedTensor.from_row_splits(x, y)
    """
    cls_ref: Incomplete
    method_name: Incomplete
    cls_symbol: Incomplete
    def __init__(self, cls_ref, method_name, **kwargs) -> None: ...
    def call(self, args, kwargs): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class KerasOpDispatcher(tf.__internal__.dispatch.GlobalOpDispatcher):
    """A global dispatcher that allows building a functional model with TF
    Ops."""
    def handle(self, op, args, kwargs):
        """Handle the specified operation with the specified arguments."""

class InstanceProperty(Layer):
    """Wraps an instance property access (e.g.

    `x.foo`) in a Keras Layer.

    This layer takes an attribute name `attr_name` in the constructor and,
    when called on input tensor `obj` returns `obj.attr_name`.

    KerasTensors specialized for specific extension types use it to
    represent instance property accesses on the represented object in the
    case where the property needs to be dynamically accessed as opposed to
    being statically computed from the typespec, e.g.

    x = keras.Input(..., ragged=True)
    out = x.flat_values
    """
    attr_name: Incomplete
    def __init__(self, attr_name, **kwargs) -> None: ...
    def call(self, obj): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class InstanceMethod(InstanceProperty):
    """Wraps an instance method access (e.g. `x.foo(arg)` in a Keras Layer.

    This layer takes an attribute name `attr_name` in the constructor and,
    when called on input tensor `obj` with additional arguments `args` and
    `kwargs` returns `obj.attr_name(*args, **kwargs)`.

    KerasTensors specialized for specific extension types use it to
    represent dynamic instance method calls on the represented object, e.g.

    x = keras.Input(..., ragged=True)
    new_values = keras.Input(...)
    out = x.with_values(new_values)
    """
    def call(self, obj, args, kwargs): ...

class TFOpLambda(Layer):
    """Wraps TF API symbols in a `Layer` object.

    It is inserted by the Functional API construction whenever users call
    a supported TF symbol on KerasTensors.

    Like Lambda layers, this layer tries to raise warnings when it detects users
    explicitly use variables in the call. (To let them know
    that the layer will not capture the variables).

    This is useful in the case where users do something like:
    x = keras.Input(...)
    y = tf.Variable(...)
    out = x * tf_variable
    """
    function: Incomplete
    symbol: Incomplete
    call: Incomplete
    def __init__(self, function, **kwargs) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class TFClassMethodDispatcher(tf.__internal__.dispatch.OpDispatcher):
    """A class method dispatcher that allows building a functional model with TF
    class methods."""
    cls: Incomplete
    method_name: Incomplete
    def __init__(self, cls, method_name) -> None: ...
    def handle(self, args, kwargs):
        """Handle the specified operation with the specified arguments."""

class SlicingOpLambda(TFOpLambda):
    """Wraps TF API symbols in a `Layer` object.

    It is inserted by the Functional API construction whenever users call
    a supported TF symbol on KerasTensors.

    Like Lambda layers, this layer tries to raise warnings when it detects users
    explicitly use variables in the call. (To let them know
    that the layer will not capture the variables).

    This is useful in the case where users do something like:
    x = keras.Input(...)
    y = tf.Variable(...)
    out = x * tf_variable
    """
    call: Incomplete
    def __init__(self, function, **kwargs) -> None: ...

class TFSlicingOpDispatcher(tf.__internal__.dispatch.OpDispatcher):
    """A global dispatcher that allows building a functional model with TF
    Ops."""
    op: Incomplete
    def __init__(self, op) -> None: ...
    def handle(self, args, kwargs):
        """Handle the specified operation with the specified arguments."""
