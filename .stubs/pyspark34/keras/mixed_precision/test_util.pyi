from _typeshed import Incomplete
from keras import regularizers as regularizers
from keras.engine import base_layer as base_layer

def create_identity_with_grad_check_fn(expected_gradient, expected_dtype: Incomplete | None = None):
    """Returns a function that asserts it's gradient has a certain value.

    This serves as a hook to assert intermediate gradients have a certain value.
    This returns an identity function. The identity's gradient function is also
    the identity function, except it asserts that the gradient equals
    `expected_gradient` and has dtype `expected_dtype`.

    Args:
      expected_gradient: The gradient function asserts that the gradient is this
        value.
      expected_dtype: The gradient function asserts the gradient has this dtype.

    Returns:
      An identity function whose gradient function asserts the gradient has a
      certain value.
    """
def create_identity_with_nan_gradients_fn(have_nan_gradients):
    """Returns a function that optionally has NaN gradients.

    This serves as a hook to introduce NaN gradients to a model. This returns an
    identity function. The identity's gradient function will check if the
    boolean tensor `have_nan_gradients` is True. If so, the gradient will be
    NaN.  Otherwise, the gradient will also be the identity.

    Args:
      have_nan_gradients: A scalar boolean tensor. If True, gradients will be
        NaN. Otherwise, the gradient function is the identity function.

    Returns:
      An identity function whose gradient function will return NaNs, if
      `have_nan_gradients` is True.
    """

class AssertTypeLayer(base_layer.Layer):
    """A layer which asserts it's inputs are a certain type."""
    def __init__(self, assert_type: Incomplete | None = None, **kwargs) -> None: ...
    def assert_input_types(self, inputs) -> None:
        """Asserts `inputs` are of the correct type. Should be called in
        call()."""

class MultiplyLayer(AssertTypeLayer):
    """A layer which multiplies its input by a scalar variable."""
    def __init__(self, regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, use_operator: bool = False, var_name: str = 'v', **kwargs) -> None:
        """Initializes the MultiplyLayer.

        Args:
          regularizer: The weight regularizer on the scalar variable.
          activity_regularizer: The activity regularizer.
          use_operator: If True, add using the * operator. If False, add using
            tf.multiply.
          var_name: The name of the variable. It can be useful to pass a name
            other than 'v', to test having the attribute name (self.v) being
            different from the variable name.
          **kwargs: Passed to AssertTypeLayer constructor.
        """
    v: Incomplete
    built: bool
    def build(self, _) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...

class MultiplyLayerWithoutAutoCast(MultiplyLayer):
    """Same as MultiplyLayer, but does not use AutoCastVariables."""
    v: Incomplete
    built: bool
    def build(self, _) -> None: ...
    def call(self, inputs): ...

class IdentityRegularizer(regularizers.Regularizer):
    def __call__(self, x): ...
    def get_config(self): ...

class ReduceSumRegularizer(regularizers.Regularizer):
    def __call__(self, x): ...
    def get_config(self): ...
