from _typeshed import Incomplete
from tensorflow.python.distribute import collective_all_reduce_strategy as collective_all_reduce_strategy, distribution_strategy_context as distribution_strategy_context, mirrored_strategy as mirrored_strategy, one_device_strategy as one_device_strategy, tpu_strategy as tpu_strategy
from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, smart_cond as smart_cond
from tensorflow.python.keras import backend as backend, optimizers as optimizers
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.ops import control_flow_ops as control_flow_ops, math_ops as math_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.trackable import base as trackable, base_delegate as base_delegate
from tensorflow.python.training.experimental import mixed_precision as mixed_precision
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export

class _UnwrapPreventer:
    """Wrapper that DistributionStrategy will not unwrap.

  Typically, DistributionStrategy will unwrap values when going from a cross-
  replica context to a replica context via `call_for_each_replica`. This class
  is a wrapper that DistributionStrategy will not unwrap, so it can be used to
  prevent it from unwrapping a value.

  TODO(reedwm): Find/implement a better way of preventing values from being
  unwrapped by DistributionStrategy
  """
    value: Incomplete
    def __init__(self, value) -> None: ...

class _DynamicLossScaleState(trackable.Trackable):
    """The state of a dynamic loss scale."""
    def __init__(self, initial_loss_scale, growth_steps, multiplier) -> None:
        """Creates the dynamic loss scale."""
    @property
    def initial_loss_scale(self): ...
    @property
    def growth_steps(self): ...
    @property
    def multiplier(self): ...
    @property
    def current_loss_scale(self):
        """Returns the current loss scale as a float32 `tf.Variable`."""
    @property
    def counter(self):
        """Returns the counter as a float32 `tf.Variable`."""
    def __call__(self):
        """Returns the current loss scale as a scalar `float32` tensor."""
    def update(self, grads):
        """Updates the value of the loss scale.

    Args:
      grads: A nested structure of unscaled gradients, each which is an
        all-reduced gradient of the loss with respect to a weight.

    Returns:
      update_op: In eager mode, None. In graph mode, an op to update the loss
        scale.
      should_apply_gradients: Either a bool or a scalar boolean tensor. If
        False, the caller should skip applying `grads` to the variables this
        step.
    """

class LossScaleOptimizer(base_delegate.DelegatingTrackableMixin, optimizer_v2.OptimizerV2):
    '''An optimizer that applies loss scaling to prevent numeric underflow.

  Loss scaling is a technique to prevent numeric underflow in intermediate
  gradients when float16 is used. To prevent underflow, the loss is multiplied
  (or "scaled") by a certain factor called the "loss scale", which causes
  intermediate gradients to be scaled by the loss scale as well. The final
  gradients are divided (or "unscaled") by the loss scale to bring them back to
  their original value.

  `LossScaleOptimizer` wraps another optimizer and applies loss scaling to it.
  By default, the loss scale is dynamically updated over time so you do not have
  to choose the loss scale. The `minimize` method automatically scales the loss,
  unscales the gradients, and updates the loss scale so all you have to do is
  wrap your optimizer with a `LossScaleOptimizer` if you use `minimize`. For
  example:

  >>> opt = tf.keras.optimizers.SGD(0.25)
  >>> opt = tf.keras.mixed_precision.LossScaleOptimizer(opt)
  >>> var = tf.Variable(1.)
  >>> loss_fn = lambda: var ** 2
  >>> # \'minimize\' applies loss scaling and updates the loss sale.
  >>> opt.minimize(loss_fn, var_list=var)
  >>> var.numpy()
  0.5

  If a `tf.GradientTape` is used to compute gradients instead of `minimize`, you
  must scale the loss and gradients manually. This can be done with the
  `LossScaleOptimizer.get_scaled_loss` and
  `LossScaleOptimizer.get_unscaled_gradients` methods. For example:

  >>> with tf.GradientTape() as tape:
  ...   loss = loss_fn()
  ...   scaled_loss = opt.get_scaled_loss(loss)
  >>> scaled_grad = tape.gradient(scaled_loss, var)
  >>> (grad,) = opt.get_unscaled_gradients([scaled_grad])
  >>> opt.apply_gradients([(grad, var)])  # Loss scale is updated here
  >>> var.numpy()
  0.25

  Warning: If you forget to call `get_scaled_loss` or `get_unscaled_gradients`
  (or both) when using a `tf.GradientTape`, the model will likely converge to a
  worse quality. Please make sure you call each function exactly once.

  When mixed precision with float16 is used, there is typically no risk of
  underflow affecting model quality if loss scaling is properly used. See
  [the mixed precision guide](
  https://www.tensorflow.org/guide/keras/mixed_precision) for more information
  on how to use mixed precision.

  Args:
    inner_optimizer: The `tf.keras.optimizers.Optimizer` instance to wrap.
    dynamic: Bool indicating whether dynamic loss scaling is used. Defaults to
      True. If True, the loss scale will be dynamically updated over time using
      an algorithm that keeps the loss scale at approximately its optimal value.
      If False, a single fixed loss scale is used and `initial_scale` must be
      specified, which is used as the loss scale. Recommended to keep as True,
      as choosing a fixed loss scale can be tricky. Currently, there is a small
      performance overhead to dynamic loss scaling compared to fixed loss
      scaling.
    initial_scale: The initial loss scale. If `dynamic` is True, this defaults
      to `2 ** 15`. If `dynamic` is False, this must be specified and acts as
      the sole loss scale, as the loss scale does not change over time. When
      dynamic loss scaling is used, is better for this to be a very high number,
      because a loss scale that is too high gets lowered far more quickly than a
      loss scale that is too low gets raised.
    dynamic_growth_steps: With dynamic loss scaling, every
      `dynamic_growth_steps` steps with finite gradients, the loss scale is
      doubled. Defaults to 2000. If a nonfinite gradient is encountered, the
      count is reset back to zero, gradients are skipped that step, and the loss
      scale is halved. The count can be queried with
      `LossScaleOptimizer.dynamic_counter`. This argument can only be specified
      if `dynamic` is True.

  `LossScaleOptimizer` will occasionally skip applying gradients to the
  variables, in which case the trainable variables will not change that step.
  This is done because the dynamic loss scale will sometimes be raised too
  high, causing overflow in the gradients. Typically, the first 2 to 15 steps of
  the model are skipped as the initial loss scale is very high, but afterwards
  steps will only be skipped on average 0.05% of the time (the fraction of steps
  skipped is `1 / dynamic_growth_steps`).

  `LossScaleOptimizer` delegates all public `Optimizer` methods to the inner
  optimizer. Additionally, in methods `minimize` and `get_gradients`, it scales
  the loss and unscales the gradients. In methods `minimize` and
  `apply_gradients`, it additionally updates the loss scale and skips applying
  gradients if any gradient has a nonfinite value.

  ### Hyperparameters

  Hyperparameters can be accessed and set on the LossScaleOptimizer, which will
  be delegated to the wrapped optimizer.

  >>> opt = tf.keras.optimizers.Adam(beta_1=0.8, epsilon=1e-5)
  >>> opt = tf.keras.mixed_precision.LossScaleOptimizer(opt)
  >>> opt.beta_1  # Equivalent to `opt.inner_optimizer.beta_1`
  0.8
  >>> opt.beta_1 = 0.7  # Equivalent to `opt.inner_optimizer.beta_1 = 0.7`
  >>> opt.beta_1
  0.7
  >>> opt.inner_optimizer.beta_1
  0.7

  However, accessing or setting non-hyperparameters is not delegated to the
  LossScaleOptimizer. In an Adam optimizer, `beta_1` is a hyperparameter but
  `epsilon` is not, as the Adam optimizer only calls `Optimizer._set_hyper` on
  `beta_1`.

  >>> opt.inner_optimizer.epsilon
  1e-5
  >>> opt.epsilon
  Traceback (most recent call last):
  ...
  AttributeError: \'LossScaleOptimizer\' object has no attribute \'epsilon\'
  >>> opt.epsilon = 1e-4  # This does NOT set epsilon on `opt.inner_optimizer`
  >>> opt.inner_optimizer.epsilon
  >>> 1e-5

  In the above example, despite epsilon being set on the LossScaleOptimizer, the
  old epsilon value will still be used when training as epsilon was not set on
  the inner optimizer.
  '''
    def __init__(self, inner_optimizer, dynamic: bool = True, initial_scale: Incomplete | None = None, dynamic_growth_steps: Incomplete | None = None) -> None: ...
    @property
    def dynamic(self):
        """Bool indicating whether dynamic loss scaling is used."""
    @property
    def loss_scale(self):
        """The current loss scale as a float32 scalar tensor."""
    @property
    def dynamic_counter(self):
        """The number of steps since the loss scale was last increased or decreased.

    This is None if `LossScaleOptimizer.dynamic` is False.

    The counter is incremented every step. Once it reaches
    `LossScaleOptimizer.dynamic_growth_steps`, the loss scale will be doubled
    and the counter will be reset back to zero. If nonfinite gradients are
    encountered, the loss scale will be halved and the counter will be reset
    back to zero.
    """
    @property
    def initial_scale(self):
        """The initial loss scale.

    If `LossScaleOptimizer.dynamic` is False, this is the same number as
    `LossScaleOptimizer.loss_scale`, as the loss scale never changes.
    """
    @property
    def dynamic_growth_steps(self):
        """The number of steps it takes to increase the loss scale.

    This is None if `LossScaleOptimizer.dynamic` is False.

    Every `dynamic_growth_steps` consecutive steps with finite gradients, the
    loss scale is increased.
    """
    @property
    def inner_optimizer(self):
        """The optimizer that this LossScaleOptimizer is wrapping."""
    def get_scaled_loss(self, loss):
        """Scales the loss by the loss scale.

    This method is only needed if you compute gradients manually, e.g. with
    `tf.GradientTape`. In that case, call this method to scale the loss before
    passing the loss to `tf.GradientTape`. If you use
    `LossScaleOptimizer.minimize` or `LossScaleOptimizer.get_gradients`, loss
    scaling is automatically applied and this method is unneeded.

    If this method is called, `get_unscaled_gradients` should also be called.
    See the `tf.keras.mixed_precision.LossScaleOptimizer` doc for
    an example.

    Args:
      loss: The loss, which will be multiplied by the loss scale. Can either be
        a tensor or a callable returning a tensor.

    Returns:
      `loss` multiplied by `LossScaleOptimizer.loss_scale`.
    """
    def get_unscaled_gradients(self, grads):
        """Unscales the gradients by the loss scale.

    This method is only needed if you compute gradients manually, e.g. with
    `tf.GradientTape`. In that case, call this method to unscale the gradients
    after computing them with `tf.GradientTape`. If you use
    `LossScaleOptimizer.minimize` or `LossScaleOptimizer.get_gradients`, loss
    scaling is automatically applied and this method is unneeded.

    If this method is called, `get_scaled_loss` should also be called. See
    the `tf.keras.mixed_precision.LossScaleOptimizer` doc for an
    example.

    Args:
      grads: A list of tensors, each which will be divided by the loss scale.
        Can have None values, which are ignored.

    Returns:
      A new list the same size as `grads`, where every non-None value in `grads`
      is divided by `LossScaleOptimizer.loss_scale`.
    """
    def get_gradients(self, loss, params): ...
    def apply_gradients(self, grads_and_vars, name: Incomplete | None = None, experimental_aggregate_gradients: bool = True): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
    @property
    def iterations(self): ...
    @iterations.setter
    def iterations(self, variable) -> None: ...
    def get_slot_names(self): ...
    def variables(self): ...
    @property
    def weights(self): ...
    def get_weights(self): ...
    def set_weights(self, weights): ...
    @property
    def clipnorm(self): ...
    @clipnorm.setter
    def clipnorm(self, val) -> None: ...
    @property
    def global_clipnorm(self): ...
    @global_clipnorm.setter
    def global_clipnorm(self, val) -> None: ...
    @property
    def clipvalue(self): ...
    @clipvalue.setter
    def clipvalue(self, val) -> None: ...
    def get_slot(self, var, slot_name): ...
    def add_slot(self, var, slot_name, initializer: str = 'zeros'): ...
    def __getattribute__(self, name): ...
    def __dir__(self): ...
    def __setattr__(self, name, value) -> None: ...
    @property
    def learning_rate(self): ...
    @learning_rate.setter
    def learning_rate(self, value) -> None: ...
    @property
    def lr(self): ...
    @lr.setter
    def lr(self, value) -> None: ...

class LossScaleOptimizerV1(LossScaleOptimizer):
    '''An deprecated optimizer that applies loss scaling.

  Warning: This class is deprecated and will be removed in a future version of
  TensorFlow. Please use the non-experimental class
  `tf.keras.mixed_precision.LossScaleOptimizer` instead.

  This class is identical to the non-experimental
  `keras.mixed_precision.LossScaleOptimizer` except its constructor takes
  different arguments. For this class (the experimental version), the
  constructor takes a `loss_scale` argument.  For the non-experimental class,
  the constructor encodes the loss scaling information in multiple arguments.
  Note that unlike this class, the non-experimental class does not accept a
  `tf.compat.v1.mixed_precision.LossScale`, which is deprecated.

  If you currently use this class, you should switch to the non-experimental
  `tf.keras.mixed_precision.LossScaleOptimizer` instead. We show several
  examples of converting the use of the experimental class to the equivalent
  non-experimental class.

  >>> # In all of the examples below, `opt1` and `opt2` are identical
  >>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD(), loss_scale=\'dynamic\')
  >>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD())
  >>> assert opt1.get_config() == opt2.get_config()

  >>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD(), loss_scale=123)
  >>> # dynamic=False indicates to use fixed loss scaling. initial_scale=123
  >>> # refers to the initial loss scale, which is the single fixed loss scale
  >>> # when dynamic=False.
  >>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD(), dynamic=False, initial_scale=123)
  >>> assert opt1.get_config() == opt2.get_config()

  >>> loss_scale = tf.compat.v1.mixed_precision.experimental.DynamicLossScale(
  ...     initial_loss_scale=2048, increment_period=500)
  >>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD(), loss_scale=loss_scale)
  >>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD(), initial_scale=2048,
  ...     dynamic_growth_steps=500)
  >>> assert opt1.get_config() == opt2.get_config()

  Make sure to also switch from this class to the non-experimental class in
  isinstance checks, if you have any. If you do not do this, your model may run
  into hard-to-debug issues, as the experimental `LossScaleOptimizer` subclasses
  the non-experimental `LossScaleOptimizer`, but not vice versa. It is safe to
  switch isinstance checks to the non-experimental `LossScaleOptimizer` even
  before using the non-experimental `LossScaleOptimizer`.

  >>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD(), loss_scale=\'dynamic\')
  >>> # The experimental class subclasses the non-experimental class
  >>> isinstance(opt1, tf.keras.mixed_precision.LossScaleOptimizer)
  True
  >>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
  ...     tf.keras.optimizers.SGD())
  >>> # The non-experimental class does NOT subclass the experimental class.
  >>> isinstance(opt2, tf.keras.mixed_precision.experimental.LossScaleOptimizer)
  False

  Args:
    optimizer: The Optimizer instance to wrap.
    loss_scale: The loss scale to scale the loss and gradients. This can
      either be an int/float to use a fixed loss scale, the string "dynamic"
      to use dynamic loss scaling, or an instance of a LossScale. The string
      "dynamic" equivalent to passing `DynamicLossScale()`, and passing an
      int/float is equivalent to passing a FixedLossScale with the given loss
      scale. If a DynamicLossScale is passed, DynamicLossScale.multiplier must
      be 2 (the default).
  '''
    def __init__(self, optimizer, loss_scale) -> None: ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class FakeOptimizerForRestoration(trackable.Trackable):
    """A fake optimizer used to support restoring TensorFlow 2.2 checkpoints.

  The checkpoint format for LossScaleOptimizers changed after TF 2.2. This class
  exists to support restoring TF 2.2 checkpoints in newer version of TensorFlow.

  In TF 2.2, LossScaleOptimizer would track the wrapped optimizer by calling the
  following in LossScaleOptimizer.__init__

  ```
  self._track_trackable(self._optimizer, 'base_optimizer')
  ```

  This means a dependency from the LossScaleOptimizer to the wrapped optimizer
  would be stored in the checkpoint. However now, the checkpoint format with a
  LossScaleOptimizer is the same as the format without a LossScaleOptimizer,
  except the loss scale is also stored. This means there is no dependency from
  the LossScaleOptimizer to the wrapped optimizer. Instead, the
  LossScaleOptimizer acts as if it is the wrapped optimizer, from a checkpoint's
  perspective, by overriding all Trackable methods and delegating them to the
  wrapped optimizer.

  To allow restoring TF 2.2. checkpoints, LossScaleOptimizer adds a dependency
  on this class instead of the inner optimizer. When restored, this class will
  instead restore the slot variables of the inner optimizer. Since this class
  has no variables, it does not affect the checkpoint when saved.
  """
    def __init__(self, optimizer) -> None: ...
    def get_slot_names(self): ...

def strategy_supports_loss_scaling():
    """Returns True if the current Strategy supports loss scaling."""
