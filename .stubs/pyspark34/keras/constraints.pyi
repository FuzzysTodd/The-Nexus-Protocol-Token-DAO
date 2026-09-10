from _typeshed import Incomplete
from keras import backend as backend
from keras.saving.legacy.serialization import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object

class Constraint:
    """Base class for weight constraints.

    A `Constraint` instance works like a stateless function.
    Users who subclass this
    class should override the `__call__` method, which takes a single
    weight parameter and return a projected version of that parameter
    (e.g. normalized or clipped). Constraints can be used with various Keras
    layers via the `kernel_constraint` or `bias_constraint` arguments.

    Here's a simple example of a non-negative weight constraint:

    >>> class NonNegative(tf.keras.constraints.Constraint):
    ...
    ...  def __call__(self, w):
    ...    return w * tf.cast(tf.math.greater_equal(w, 0.), w.dtype)

    >>> weight = tf.constant((-1.0, 1.0))
    >>> NonNegative()(weight)
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([0.,  1.],
    dtype=float32)>

    >>> tf.keras.layers.Dense(4, kernel_constraint=NonNegative())
    """
    def __call__(self, w):
        """Applies the constraint to the input weight variable.

        By default, the inputs weight variable is not modified.
        Users should override this method to implement their own projection
        function.

        Args:
          w: Input weight variable.

        Returns:
          Projected variable (by default, returns unmodified inputs).
        """
    def get_config(self):
        """Returns a Python dict of the object config.

        A constraint config is a Python dictionary (JSON-serializable) that can
        be used to reinstantiate the same object.

        Returns:
          Python dict containing the configuration of the constraint object.
        """
    @classmethod
    def from_config(cls, config):
        """Instantiates a weight constraint from a configuration dictionary.

        Example:

        ```python
        constraint = UnitNorm()
        config = constraint.get_config()
        constraint = UnitNorm.from_config(config)
        ```

        Args:
          config: A Python dictionary, the output of `get_config`.

        Returns:
          A `tf.keras.constraints.Constraint` instance.
        """

class MaxNorm(Constraint):
    '''MaxNorm weight constraint.

    Constrains the weights incident to each hidden unit
    to have a norm less than or equal to a desired value.

    Also available via the shortcut function `tf.keras.constraints.max_norm`.

    Args:
      max_value: the maximum norm value for the incoming weights.
      axis: integer, axis along which to calculate weight norms.
        For instance, in a `Dense` layer the weight matrix
        has shape `(input_dim, output_dim)`,
        set `axis` to `0` to constrain each weight vector
        of length `(input_dim,)`.
        In a `Conv2D` layer with `data_format="channels_last"`,
        the weight tensor has shape
        `(rows, cols, input_depth, output_depth)`,
        set `axis` to `[0, 1, 2]`
        to constrain the weights of each filter tensor of size
        `(rows, cols, input_depth)`.

    '''
    max_value: Incomplete
    axis: Incomplete
    def __init__(self, max_value: int = 2, axis: int = 0) -> None: ...
    def __call__(self, w): ...
    def get_config(self): ...

class NonNeg(Constraint):
    """Constrains the weights to be non-negative.

    Also available via the shortcut function `tf.keras.constraints.non_neg`.
    """
    def __call__(self, w): ...

class UnitNorm(Constraint):
    '''Constrains the weights incident to each hidden unit to have unit norm.

    Also available via the shortcut function `tf.keras.constraints.unit_norm`.

    Args:
      axis: integer, axis along which to calculate weight norms.
        For instance, in a `Dense` layer the weight matrix
        has shape `(input_dim, output_dim)`,
        set `axis` to `0` to constrain each weight vector
        of length `(input_dim,)`.
        In a `Conv2D` layer with `data_format="channels_last"`,
        the weight tensor has shape
        `(rows, cols, input_depth, output_depth)`,
        set `axis` to `[0, 1, 2]`
        to constrain the weights of each filter tensor of size
        `(rows, cols, input_depth)`.
    '''
    axis: Incomplete
    def __init__(self, axis: int = 0) -> None: ...
    def __call__(self, w): ...
    def get_config(self): ...

class MinMaxNorm(Constraint):
    '''MinMaxNorm weight constraint.

    Constrains the weights incident to each hidden unit
    to have the norm between a lower bound and an upper bound.

    Also available via the shortcut function
    `tf.keras.constraints.min_max_norm`.

    Args:
      min_value: the minimum norm for the incoming weights.
      max_value: the maximum norm for the incoming weights.
      rate: rate for enforcing the constraint: weights will be
        rescaled to yield
        `(1 - rate) * norm + rate * norm.clip(min_value, max_value)`.
        Effectively, this means that rate=1.0 stands for strict
        enforcement of the constraint, while rate<1.0 means that
        weights will be rescaled at each step to slowly move
        towards a value inside the desired interval.
      axis: integer, axis along which to calculate weight norms.
        For instance, in a `Dense` layer the weight matrix
        has shape `(input_dim, output_dim)`,
        set `axis` to `0` to constrain each weight vector
        of length `(input_dim,)`.
        In a `Conv2D` layer with `data_format="channels_last"`,
        the weight tensor has shape
        `(rows, cols, input_depth, output_depth)`,
        set `axis` to `[0, 1, 2]`
        to constrain the weights of each filter tensor of size
        `(rows, cols, input_depth)`.
    '''
    min_value: Incomplete
    max_value: Incomplete
    rate: Incomplete
    axis: Incomplete
    def __init__(self, min_value: float = 0.0, max_value: float = 1.0, rate: float = 1.0, axis: int = 0) -> None: ...
    def __call__(self, w): ...
    def get_config(self): ...

class RadialConstraint(Constraint):
    '''Constrains `Conv2D` kernel weights to be the same for each radius.

    Also available via the shortcut function
    `tf.keras.constraints.radial_constraint`.

    For example, the desired output for the following 4-by-4 kernel:

    ```
        kernel = [[v_00, v_01, v_02, v_03],
                  [v_10, v_11, v_12, v_13],
                  [v_20, v_21, v_22, v_23],
                  [v_30, v_31, v_32, v_33]]
    ```

    is this::

    ```
        kernel = [[v_11, v_11, v_11, v_11],
                  [v_11, v_33, v_33, v_11],
                  [v_11, v_33, v_33, v_11],
                  [v_11, v_11, v_11, v_11]]
    ```

    This constraint can be applied to any `Conv2D` layer version, including
    `Conv2DTranspose` and `SeparableConv2D`, and with either `"channels_last"`
    or `"channels_first"` data format. The method assumes the weight tensor is
    of shape `(rows, cols, input_depth, output_depth)`.
    '''
    def __call__(self, w): ...
max_norm = MaxNorm
non_neg = NonNeg
unit_norm = UnitNorm
min_max_norm = MinMaxNorm
radial_constraint = RadialConstraint
maxnorm = max_norm
nonneg = non_neg
unitnorm = unit_norm

def serialize(constraint, use_legacy_format: bool = False): ...
def deserialize(config, custom_objects: Incomplete | None = None, use_legacy_format: bool = False): ...
def get(identifier):
    """Retrieves a Keras constraint function."""
