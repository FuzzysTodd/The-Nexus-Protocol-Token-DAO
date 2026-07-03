import abc
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context, reduce_util as reduce_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, math_ops as math_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.trackable import base as trackable
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

class LossScale(trackable.Trackable, metaclass=abc.ABCMeta):
    '''Base class for all TF1 loss scales.

  This is an abstract base class, so you cannot instantiate it directly.
  Instead, use one of its concrete subclasses:
    * `tf.compat.v1.mixed_precision.DynamicLossScale`
    * `tf.compat.v1.mixed_precision.FixedLossScale`

  Loss scaling is a process that multiplies the loss by a multiplier called the
  loss scale, and divides each gradient by the same multiplier. The pseudocode
  for this process is:

  ```
  loss = ...
  loss *= loss_scale
  grads = gradients(loss, vars)
  grads /= loss_scale
  ```

  Mathematically, loss scaling has no effect, but can help avoid numerical
  underflow in intermediate gradients when float16 tensors are used for mixed
  precision training. By multiplying the loss, each intermediate gradient will
  have the same multiplier applied.

  Instances of this class represent a loss scale. Calling instances of this
  class returns the loss scale as a scalar float32 tensor, while method
  `update()` updates the loss scale depending on the values of the gradients.
  Optimizers use instances of this class to scale loss and gradients.

  In most functions that accept a LossScale, you can also pass an int (such as
  8) to create a `FixedLossScale` or the string `"dynamic"` to create a dynamic
  loss scale.
  '''
    def __init__(self) -> None:
        """Initializes the loss scale class."""
    @abc.abstractmethod
    def __call__(self):
        """Returns the current loss scale as a scalar `float32` tensor."""
    @abc.abstractmethod
    def update(self, grads):
        """Updates the value of the loss scale.

    The loss scale will be potentially updated, based on the value of `grads`.
    The tensor returned by calling this class is only updated when this function
    is evaluated.

    In eager mode, this directly updates the loss scale, so that calling
    `__call__` will return the newly updated loss scale. In graph mode,
    this returns an op that, when evaluated, updates the loss scale.

    This function also returns a `should_apply_gradients` bool. If False,
    gradients should not be applied to the variables that step, as nonfinite
    gradients were found, and the loss scale has been be updated to reduce the
    chance of finding nonfinite gradients in the next step. Some loss scale
    classes will always return True, as they cannot adjust themselves in
    response to nonfinite gradients.

    When a DistributionStrategy is used, this function may only be called in a
    cross-replica context.

    Args:
      grads: A nested structure of unscaled gradients, each which is the
        gradient of the loss with respect to a weight. The gradients should have
        already been divided by the loss scale being before passed to this
        function. 'None' gradients are accepted, and are ignored.

    Returns:
      update_op: In eager mode, None. In graph mode, an op to update the loss
        scale.
      should_apply_gradients: Either a bool or a scalar boolean tensor. If
        False, the caller should skip applying `grads` to the variables this
        step.
    """
    @abc.abstractmethod
    def get_config(self):
        """Returns the config of this loss scale."""
    @classmethod
    def from_config(cls, config):
        """Creates the LossScale from its config."""

class FixedLossScale(LossScale):
    """Loss scale with a fixed value.

  The loss scale is not updated for the lifetime of instances of this class.
  A given instance of this class always returns the same number when called.
  """
    def __init__(self, loss_scale_value) -> None:
        """Creates the fixed loss scale.

    Args:
      loss_scale_value: A Python float. Its ideal value varies depending on
        models to run. Choosing a too small loss_scale might affect model
        quality; a too big loss_scale might cause inf or nan. There is no single
        right loss_scale to apply. There is no harm choosing a relatively big
        number as long as no nan or inf is encountered in training.

    Raises:
      ValueError: If loss_scale_value is less than 1.
    """
    def __call__(self): ...
    def update(self, grads): ...
    def get_config(self): ...

class DynamicLossScale(LossScale):
    """Loss scale that dynamically adjusts itself.

  Dynamic loss scaling works by adjusting the loss scale as training progresses.
  The goal is to keep the loss scale as high as possible without overflowing the
  gradients. As long as the gradients do not overflow, raising the loss scale
  never hurts.

  The algorithm starts by setting the loss scale to an initial value. Every N
  steps that the gradients are finite, the loss scale is increased by some
  factor. However, if a NaN or Inf gradient is found, the gradients for that
  step are not applied, and the loss scale is decreased by the factor. This
  process tends to keep the loss scale as high as possible without gradients
  overflowing.
  """
    def __init__(self, initial_loss_scale=..., increment_period: int = 2000, multiplier: float = 2.0) -> None:
        """Creates the dynamic loss scale.

    Args:
      initial_loss_scale: A Python float.  The loss scale to use at the
        beginning. It's better to start this at a very high number, because a
        loss scale that is too high gets lowered far more quickly than a loss
        scale that is too low gets raised. The default is 2 ** 15, which is
        approximately half the maximum float16 value.
      increment_period: Increases loss scale every `increment_period`
        consecutive steps that finite gradients are encountered. If a nonfinite
        gradient is encountered, the count is reset back to zero.
      multiplier: The multiplier to use when increasing or decreasing the loss
        scale.
    """
    @property
    def initial_loss_scale(self): ...
    @property
    def increment_period(self): ...
    @property
    def multiplier(self): ...
    def __call__(self): ...
    def update(self, grads):
        """Updates loss scale based on if gradients are finite in current step."""
    def get_config(self): ...

def get(identifier):
    """Get a loss scale object."""
