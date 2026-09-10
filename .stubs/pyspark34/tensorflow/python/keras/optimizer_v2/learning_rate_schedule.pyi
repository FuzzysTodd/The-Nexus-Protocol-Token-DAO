import abc
from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export

class LearningRateSchedule(metaclass=abc.ABCMeta):
    """The learning rate schedule base class.

  You can use a learning rate schedule to modulate how the learning rate
  of your optimizer changes over time.

  Several built-in learning rate schedules are available, such as
  `tf.keras.optimizers.schedules.ExponentialDecay` or
  `tf.keras.optimizers.schedules.PiecewiseConstantDecay`:

  ```python
  lr_schedule = keras.optimizers.schedules.ExponentialDecay(
      initial_learning_rate=1e-2,
      decay_steps=10000,
      decay_rate=0.9)
  optimizer = keras.optimizers.SGD(learning_rate=lr_schedule)
  ```

  A `LearningRateSchedule` instance can be passed in as the `learning_rate`
  argument of any optimizer.

  To implement your own schedule object, you should implement the `__call__`
  method, which takes a `step` argument (scalar integer tensor, the
  current training step count).
  Like for any other Keras object, you can also optionally
  make your object serializable by implementing the `get_config`
  and `from_config` methods.

  Example:

  ```python
  class MyLRSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):

    def __init__(self, initial_learning_rate):
      self.initial_learning_rate = initial_learning_rate

    def __call__(self, step):
       return self.initial_learning_rate / (step + 1)

  optimizer = tf.keras.optimizers.SGD(learning_rate=MyLRSchedule(0.1))
  ```
  """
    @abc.abstractmethod
    def __call__(self, step): ...
    @abc.abstractmethod
    def get_config(self): ...
    @classmethod
    def from_config(cls, config):
        """Instantiates a `LearningRateSchedule` from its config.

    Args:
        config: Output of `get_config()`.

    Returns:
        A `LearningRateSchedule` instance.
    """

class ExponentialDecay(LearningRateSchedule):
    """A LearningRateSchedule that uses an exponential decay schedule.

  When training a model, it is often useful to lower the learning rate as
  the training progresses. This schedule applies an exponential decay function
  to an optimizer step, given a provided initial learning rate.

  The schedule a 1-arg callable that produces a decayed learning
  rate when passed the current optimizer step. This can be useful for changing
  the learning rate value across different invocations of optimizer functions.
  It is computed as:

  ```python
  def decayed_learning_rate(step):
    return initial_learning_rate * decay_rate ^ (step / decay_steps)
  ```

  If the argument `staircase` is `True`, then `step / decay_steps` is
  an integer division and the decayed learning rate follows a
  staircase function.

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate.
  Example: When fitting a Keras model, decay every 100000 steps with a base
  of 0.96:

  ```python
  initial_learning_rate = 0.1
  lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
      initial_learning_rate,
      decay_steps=100000,
      decay_rate=0.96,
      staircase=True)

  model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=lr_schedule),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  model.fit(data, labels, epochs=5)
  ```

  The learning rate schedule is also serializable and deserializable using
  `tf.keras.optimizers.schedules.serialize` and
  `tf.keras.optimizers.schedules.deserialize`.

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as `initial_learning_rate`.
  """
    initial_learning_rate: Incomplete
    decay_steps: Incomplete
    decay_rate: Incomplete
    staircase: Incomplete
    name: Incomplete
    def __init__(self, initial_learning_rate, decay_steps, decay_rate, staircase: bool = False, name: Incomplete | None = None) -> None:
        """Applies exponential decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Must be positive.  See the decay computation above.
      decay_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The decay rate.
      staircase: Boolean.  If `True` decay the learning rate at discrete
        intervals
      name: String.  Optional name of the operation.  Defaults to
        'ExponentialDecay'.
    """
    def __call__(self, step): ...
    def get_config(self): ...

class PiecewiseConstantDecay(LearningRateSchedule):
    """A LearningRateSchedule that uses a piecewise constant decay schedule.

  The function returns a 1-arg callable to compute the piecewise constant
  when passed the current optimizer step. This can be useful for changing the
  learning rate value across different invocations of optimizer functions.

  Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5
    for the next 10000 steps, and 0.1 for any additional steps.

  ```python
  step = tf.Variable(0, trainable=False)
  boundaries = [100000, 110000]
  values = [1.0, 0.5, 0.1]
  learning_rate_fn = keras.optimizers.schedules.PiecewiseConstantDecay(
      boundaries, values)

  # Later, whenever we perform an optimization step, we pass in the step.
  learning_rate = learning_rate_fn(step)
  ```

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate. The learning rate schedule is also serializable and
  deserializable using `tf.keras.optimizers.schedules.serialize` and
  `tf.keras.optimizers.schedules.deserialize`.

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as the boundary tensors.

    The output of the 1-arg function that takes the `step`
    is `values[0]` when `step <= boundaries[0]`,
    `values[1]` when `step > boundaries[0]` and `step <= boundaries[1]`, ...,
    and values[-1] when `step > boundaries[-1]`.
  """
    boundaries: Incomplete
    values: Incomplete
    name: Incomplete
    def __init__(self, boundaries, values, name: Incomplete | None = None) -> None:
        """Piecewise constant from boundaries and interval values.

    Args:
      boundaries: A list of `Tensor`s or `int`s or `float`s with strictly
        increasing entries, and with all elements having the same type as the
        optimizer step.
      values: A list of `Tensor`s or `float`s or `int`s that specifies the
        values for the intervals defined by `boundaries`. It should have one
        more element than `boundaries`, and all elements should have the same
        type.
      name: A string. Optional name of the operation. Defaults to
        'PiecewiseConstant'.

    Raises:
      ValueError: if the number of elements in the lists do not match.
    """
    def __call__(self, step): ...
    def get_config(self): ...

class PolynomialDecay(LearningRateSchedule):
    """A LearningRateSchedule that uses a polynomial decay schedule.

  It is commonly observed that a monotonically decreasing learning rate, whose
  degree of change is carefully chosen, results in a better performing model.
  This schedule applies a polynomial decay function to an optimizer step,
  given a provided `initial_learning_rate`, to reach an `end_learning_rate`
  in the given `decay_steps`.

  It requires a `step` value to compute the decayed learning rate. You
  can just pass a TensorFlow variable that you increment at each training
  step.

  The schedule is a 1-arg callable that produces a decayed learning rate
  when passed the current optimizer step. This can be useful for changing the
  learning rate value across different invocations of optimizer functions.
  It is computed as:

  ```python
  def decayed_learning_rate(step):
    step = min(step, decay_steps)
    return ((initial_learning_rate - end_learning_rate) *
            (1 - step / decay_steps) ^ (power)
           ) + end_learning_rate
  ```

  If `cycle` is True then a multiple of `decay_steps` is used, the first one
  that is bigger than `step`.

  ```python
  def decayed_learning_rate(step):
    decay_steps = decay_steps * ceil(step / decay_steps)
    return ((initial_learning_rate - end_learning_rate) *
            (1 - step / decay_steps) ^ (power)
           ) + end_learning_rate
  ```

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate.
  Example: Fit a model while decaying from 0.1 to 0.01 in 10000 steps using
  sqrt (i.e. power=0.5):

  ```python
  ...
  starter_learning_rate = 0.1
  end_learning_rate = 0.01
  decay_steps = 10000
  learning_rate_fn = tf.keras.optimizers.schedules.PolynomialDecay(
      starter_learning_rate,
      decay_steps,
      end_learning_rate,
      power=0.5)

  model.compile(optimizer=tf.keras.optimizers.SGD(
                    learning_rate=learning_rate_fn),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  model.fit(data, labels, epochs=5)
  ```

  The learning rate schedule is also serializable and deserializable using
  `tf.keras.optimizers.schedules.serialize` and
  `tf.keras.optimizers.schedules.deserialize`.

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as `initial_learning_rate`.
  """
    initial_learning_rate: Incomplete
    decay_steps: Incomplete
    end_learning_rate: Incomplete
    power: Incomplete
    cycle: Incomplete
    name: Incomplete
    def __init__(self, initial_learning_rate, decay_steps, end_learning_rate: float = 0.0001, power: float = 1.0, cycle: bool = False, name: Incomplete | None = None) -> None:
        """Applies a polynomial decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Must be positive.  See the decay computation above.
      end_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The minimal end learning rate.
      power: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The power of the polynomial. Defaults to linear, 1.0.
      cycle: A boolean, whether or not it should cycle beyond decay_steps.
      name: String.  Optional name of the operation. Defaults to
        'PolynomialDecay'.
    """
    def __call__(self, step): ...
    def get_config(self): ...

class InverseTimeDecay(LearningRateSchedule):
    """A LearningRateSchedule that uses an inverse time decay schedule.

  When training a model, it is often useful to lower the learning rate as
  the training progresses. This schedule applies the inverse decay function
  to an optimizer step, given a provided initial learning rate.
  It requires a `step` value to compute the decayed learning rate. You can
  just pass a TensorFlow variable that you increment at each training step.

  The schedule a 1-arg callable that produces a decayed learning
  rate when passed the current optimizer step. This can be useful for changing
  the learning rate value across different invocations of optimizer functions.
  It is computed as:

  ```python
  def decayed_learning_rate(step):
    return initial_learning_rate / (1 + decay_rate * step / decay_step)
  ```

  or, if `staircase` is `True`, as:

  ```python
  def decayed_learning_rate(step):
    return initial_learning_rate / (1 + decay_rate * floor(step / decay_step))
  ```

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate.
  Example: Fit a Keras model when decaying 1/t with a rate of 0.5:

  ```python
  ...
  initial_learning_rate = 0.1
  decay_steps = 1.0
  decay_rate = 0.5
  learning_rate_fn = keras.optimizers.schedules.InverseTimeDecay(
    initial_learning_rate, decay_steps, decay_rate)

  model.compile(optimizer=tf.keras.optimizers.SGD(
                    learning_rate=learning_rate_fn),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  model.fit(data, labels, epochs=5)
  ```

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as `initial_learning_rate`.
  """
    initial_learning_rate: Incomplete
    decay_steps: Incomplete
    decay_rate: Incomplete
    staircase: Incomplete
    name: Incomplete
    def __init__(self, initial_learning_rate, decay_steps, decay_rate, staircase: bool = False, name: Incomplete | None = None) -> None:
        """Applies inverse time decay to the initial learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` `Tensor` or a
        Python number.  The initial learning rate.
      decay_steps: How often to apply decay.
      decay_rate: A Python number.  The decay rate.
      staircase: Whether to apply decay in a discrete staircase, as opposed to
        continuous, fashion.
      name: String.  Optional name of the operation.  Defaults to
        'InverseTimeDecay'.
    """
    def __call__(self, step): ...
    def get_config(self): ...

class CosineDecay(LearningRateSchedule):
    """A LearningRateSchedule that uses a cosine decay schedule.

  See [Loshchilov & Hutter, ICLR2016](https://arxiv.org/abs/1608.03983),
  SGDR: Stochastic Gradient Descent with Warm Restarts.

  When training a model, it is often useful to lower the learning rate as
  the training progresses. This schedule applies a cosine decay function
  to an optimizer step, given a provided initial learning rate.
  It requires a `step` value to compute the decayed learning rate. You can
  just pass a TensorFlow variable that you increment at each training step.

  The schedule a 1-arg callable that produces a decayed learning
  rate when passed the current optimizer step. This can be useful for changing
  the learning rate value across different invocations of optimizer functions.
  It is computed as:

  ```python
  def decayed_learning_rate(step):
    step = min(step, decay_steps)
    cosine_decay = 0.5 * (1 + cos(pi * step / decay_steps))
    decayed = (1 - alpha) * cosine_decay + alpha
    return initial_learning_rate * decayed
  ```

  Example usage:
  ```python
  decay_steps = 1000
  lr_decayed_fn = tf.keras.optimizers.schedules.CosineDecay(
      initial_learning_rate, decay_steps)
  ```

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate. The learning rate schedule is also serializable and
  deserializable using `tf.keras.optimizers.schedules.serialize` and
  `tf.keras.optimizers.schedules.deserialize`.

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as `initial_learning_rate`.
  """
    initial_learning_rate: Incomplete
    decay_steps: Incomplete
    alpha: Incomplete
    name: Incomplete
    def __init__(self, initial_learning_rate, decay_steps, alpha: float = 0.0, name: Incomplete | None = None) -> None:
        """Applies cosine decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` Tensor or a
        Python number. The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Number of steps to decay over.
      alpha: A scalar `float32` or `float64` Tensor or a Python number.
        Minimum learning rate value as a fraction of initial_learning_rate.
      name: String. Optional name of the operation.  Defaults to 'CosineDecay'.
    """
    def __call__(self, step): ...
    def get_config(self): ...

class CosineDecayRestarts(LearningRateSchedule):
    """A LearningRateSchedule that uses a cosine decay schedule with restarts.

  See [Loshchilov & Hutter, ICLR2016](https://arxiv.org/abs/1608.03983),
  SGDR: Stochastic Gradient Descent with Warm Restarts.

  When training a model, it is often useful to lower the learning rate as
  the training progresses. This schedule applies a cosine decay function with
  restarts to an optimizer step, given a provided initial learning rate.
  It requires a `step` value to compute the decayed learning rate. You can
  just pass a TensorFlow variable that you increment at each training step.

  The schedule a 1-arg callable that produces a decayed learning
  rate when passed the current optimizer step. This can be useful for changing
  the learning rate value across different invocations of optimizer functions.

  The learning rate multiplier first decays
  from 1 to `alpha` for `first_decay_steps` steps. Then, a warm
  restart is performed. Each new warm restart runs for `t_mul` times more
  steps and with `m_mul` times smaller initial learning rate.

  Example usage:
  ```python
  first_decay_steps = 1000
  lr_decayed_fn = (
    tf.keras.optimizers.schedules.CosineDecayRestarts(
        initial_learning_rate,
        first_decay_steps))
  ```

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate. The learning rate schedule is also serializable and
  deserializable using `tf.keras.optimizers.schedules.serialize` and
  `tf.keras.optimizers.schedules.deserialize`.

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as `initial_learning_rate`.
  """
    initial_learning_rate: Incomplete
    first_decay_steps: Incomplete
    alpha: Incomplete
    name: Incomplete
    def __init__(self, initial_learning_rate, first_decay_steps, t_mul: float = 2.0, m_mul: float = 1.0, alpha: float = 0.0, name: Incomplete | None = None) -> None:
        """Applies cosine decay with restarts to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` Tensor or a Python
        number. The initial learning rate.
      first_decay_steps: A scalar `int32` or `int64` `Tensor` or a Python
        number. Number of steps to decay over.
      t_mul: A scalar `float32` or `float64` `Tensor` or a Python number.
        Used to derive the number of iterations in the i-th period
      m_mul: A scalar `float32` or `float64` `Tensor` or a Python number.
        Used to derive the initial learning rate of the i-th period:
      alpha: A scalar `float32` or `float64` Tensor or a Python number.
        Minimum learning rate value as a fraction of the initial_learning_rate.
      name: String. Optional name of the operation.  Defaults to 'SGDRDecay'.
    """
    def __call__(self, step): ...
    def get_config(self): ...

class LinearCosineDecay(LearningRateSchedule):
    """A LearningRateSchedule that uses a linear cosine decay schedule.

  See [Bello et al., ICML2017] Neural Optimizer Search with RL.
  https://arxiv.org/abs/1709.07417

  For the idea of warm starts here controlled by `num_periods`,
  see [Loshchilov & Hutter, ICLR2016] SGDR: Stochastic Gradient Descent
  with Warm Restarts. https://arxiv.org/abs/1608.03983

  Note that linear cosine decay is more aggressive than cosine decay and
  larger initial learning rates can typically be used.

  When training a model, it is often recommended to lower the learning rate as
  the training progresses. This schedule applies a linear cosine decay
  function to an optimizer step, given a provided initial learning rate.
  It requires a `step` value to compute the decayed learning rate. You can
  just pass a TensorFlow variable that you increment at each training step.

  The schedule a 1-arg callable that produces a decayed learning
  rate when passed the current optimizer step. This can be useful for changing
  the learning rate value across different invocations of optimizer functions.
  It is computed as:

  ```python
  def decayed_learning_rate(step):
    step = min(step, decay_steps)
    linear_decay = (decay_steps - step) / decay_steps
    cosine_decay = 0.5 * (
        1 + cos(pi * 2 * num_periods * step / decay_steps))
    decayed = (alpha + linear_decay) * cosine_decay + beta
    return initial_learning_rate * decayed
  ```

  Example usage:
  ```python
  decay_steps = 1000
  lr_decayed_fn = (
    tf.keras.experimental.LinearCosineDecay(
      initial_learning_rate, decay_steps))
  ```

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate. The learning rate schedule is also serializable and
  deserializable using `tf.keras.optimizers.schedules.serialize` and
  `tf.keras.optimizers.schedules.deserialize`.

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as `initial_learning_rate`.
  """
    initial_learning_rate: Incomplete
    decay_steps: Incomplete
    num_periods: Incomplete
    alpha: Incomplete
    beta: Incomplete
    name: Incomplete
    def __init__(self, initial_learning_rate, decay_steps, num_periods: float = 0.5, alpha: float = 0.0, beta: float = 0.001, name: Incomplete | None = None) -> None:
        """Applies linear cosine decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` Tensor or a Python
        number. The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Number of steps to decay over.
      num_periods: Number of periods in the cosine part of the decay.
        See computation above.
      alpha: See computation above.
      beta: See computation above.
      name: String.  Optional name of the operation.  Defaults to
        'LinearCosineDecay'.
    """
    def __call__(self, step): ...
    def get_config(self): ...

class NoisyLinearCosineDecay(LearningRateSchedule):
    """A LearningRateSchedule that uses a noisy linear cosine decay schedule.

  See [Bello et al., ICML2017] Neural Optimizer Search with RL.
  https://arxiv.org/abs/1709.07417

  For the idea of warm starts here controlled by `num_periods`,
  see [Loshchilov & Hutter, ICLR2016] SGDR: Stochastic Gradient Descent
  with Warm Restarts. https://arxiv.org/abs/1608.03983

  Note that linear cosine decay is more aggressive than cosine decay and
  larger initial learning rates can typically be used.

  When training a model, it is often recommended to lower the learning rate as
  the training progresses. This schedule applies a noisy linear cosine decay
  function to an optimizer step, given a provided initial learning rate.
  It requires a `step` value to compute the decayed learning rate. You can
  just pass a TensorFlow variable that you increment at each training step.

  The schedule a 1-arg callable that produces a decayed learning
  rate when passed the current optimizer step. This can be useful for changing
  the learning rate value across different invocations of optimizer functions.
  It is computed as:

  ```python
  def decayed_learning_rate(step):
    step = min(step, decay_steps)
    linear_decay = (decay_steps - step) / decay_steps)
    cosine_decay = 0.5 * (
        1 + cos(pi * 2 * num_periods * step / decay_steps))
    decayed = (alpha + linear_decay + eps_t) * cosine_decay + beta
    return initial_learning_rate * decayed
  ```
  where eps_t is 0-centered gaussian noise with variance
  initial_variance / (1 + global_step) ** variance_decay

  Example usage:
  ```python
  decay_steps = 1000
  lr_decayed_fn = (
    tf.keras.experimental.NoisyLinearCosineDecay(
      initial_learning_rate, decay_steps))
  ```

  You can pass this schedule directly into a `tf.keras.optimizers.Optimizer`
  as the learning rate. The learning rate schedule is also serializable and
  deserializable using `tf.keras.optimizers.schedules.serialize` and
  `tf.keras.optimizers.schedules.deserialize`.

  Returns:
    A 1-arg callable learning rate schedule that takes the current optimizer
    step and outputs the decayed learning rate, a scalar `Tensor` of the same
    type as `initial_learning_rate`.
  """
    initial_learning_rate: Incomplete
    decay_steps: Incomplete
    initial_variance: Incomplete
    variance_decay: Incomplete
    num_periods: Incomplete
    alpha: Incomplete
    beta: Incomplete
    name: Incomplete
    def __init__(self, initial_learning_rate, decay_steps, initial_variance: float = 1.0, variance_decay: float = 0.55, num_periods: float = 0.5, alpha: float = 0.0, beta: float = 0.001, name: Incomplete | None = None) -> None:
        """Applies noisy linear cosine decay to the learning rate.

    Args:
      initial_learning_rate: A scalar `float32` or `float64` Tensor or a Python
        number. The initial learning rate.
      decay_steps: A scalar `int32` or `int64` `Tensor` or a Python number.
        Number of steps to decay over.
      initial_variance: initial variance for the noise. See computation above.
      variance_decay: decay for the noise's variance. See computation above.
      num_periods: Number of periods in the cosine part of the decay.
        See computation above.
      alpha: See computation above.
      beta: See computation above.
      name: String.  Optional name of the operation.  Defaults to
        'NoisyLinearCosineDecay'.
    """
    def __call__(self, step): ...
    def get_config(self): ...

def serialize(learning_rate_schedule): ...
def deserialize(config, custom_objects: Incomplete | None = None): ...
