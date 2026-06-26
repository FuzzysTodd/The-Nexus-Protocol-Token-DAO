from _typeshed import Incomplete
from keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.dtensor import utils as utils
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec

class Dense(Layer):
    '''Just your regular densely-connected NN layer.

    `Dense` implements the operation:
    `output = activation(dot(input, kernel) + bias)`
    where `activation` is the element-wise activation function
    passed as the `activation` argument, `kernel` is a weights matrix
    created by the layer, and `bias` is a bias vector created by the layer
    (only applicable if `use_bias` is `True`). These are all attributes of
    `Dense`.

    Note: If the input to the layer has a rank greater than 2, then `Dense`
    computes the dot product between the `inputs` and the `kernel` along the
    last axis of the `inputs` and axis 0 of the `kernel` (using `tf.tensordot`).
    For example, if input has dimensions `(batch_size, d0, d1)`, then we create
    a `kernel` with shape `(d1, units)`, and the `kernel` operates along axis 2
    of the `input`, on every sub-tensor of shape `(1, 1, d1)` (there are
    `batch_size * d0` such sub-tensors).  The output in this case will have
    shape `(batch_size, d0, units)`.

    Besides, layer attributes cannot be modified after the layer has been called
    once (except the `trainable` attribute).
    When a popular kwarg `input_shape` is passed, then keras will create
    an input layer to insert before the current layer. This can be treated
    equivalent to explicitly defining an `InputLayer`.

    Example:

    >>> # Create a `Sequential` model and add a Dense layer as the first layer.
    >>> model = tf.keras.models.Sequential()
    >>> model.add(tf.keras.Input(shape=(16,)))
    >>> model.add(tf.keras.layers.Dense(32, activation=\'relu\'))
    >>> # Now the model will take as input arrays of shape (None, 16)
    >>> # and output arrays of shape (None, 32).
    >>> # Note that after the first layer, you don\'t need to specify
    >>> # the size of the input anymore:
    >>> model.add(tf.keras.layers.Dense(32))
    >>> model.output_shape
    (None, 32)

    Args:
        units: Positive integer, dimensionality of the output space.
        activation: Activation function to use.
            If you don\'t specify anything, no activation is applied
            (ie. "linear" activation: `a(x) = x`).
        use_bias: Boolean, whether the layer uses a bias vector.
        kernel_initializer: Initializer for the `kernel` weights matrix.
        bias_initializer: Initializer for the bias vector.
        kernel_regularizer: Regularizer function applied to
            the `kernel` weights matrix.
        bias_regularizer: Regularizer function applied to the bias vector.
        activity_regularizer: Regularizer function applied to
            the output of the layer (its "activation").
        kernel_constraint: Constraint function applied to
            the `kernel` weights matrix.
        bias_constraint: Constraint function applied to the bias vector.

    Input shape:
        N-D tensor with shape: `(batch_size, ..., input_dim)`.
        The most common situation would be
        a 2D input with shape `(batch_size, input_dim)`.

    Output shape:
        N-D tensor with shape: `(batch_size, ..., units)`.
        For instance, for a 2D input with shape `(batch_size, input_dim)`,
        the output would have shape `(batch_size, units)`.
    '''
    units: Incomplete
    activation: Incomplete
    use_bias: Incomplete
    kernel_initializer: Incomplete
    bias_initializer: Incomplete
    kernel_regularizer: Incomplete
    bias_regularizer: Incomplete
    kernel_constraint: Incomplete
    bias_constraint: Incomplete
    input_spec: Incomplete
    supports_masking: bool
    def __init__(self, units, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
