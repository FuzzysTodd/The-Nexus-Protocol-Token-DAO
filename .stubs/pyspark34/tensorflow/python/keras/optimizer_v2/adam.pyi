from _typeshed import Incomplete
from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import indexed_slices as indexed_slices, ops as ops
from tensorflow.python.keras import backend_config as backend_config
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, state_ops as state_ops
from tensorflow.python.training import gen_training_ops as gen_training_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

class Adam(optimizer_v2.OptimizerV2):
    '''Optimizer that implements the Adam algorithm.

  Adam optimization is a stochastic gradient descent method that is based on
  adaptive estimation of first-order and second-order moments.

  According to
  [Kingma et al., 2014](http://arxiv.org/abs/1412.6980),
  the method is "*computationally
  efficient, has little memory requirement, invariant to diagonal rescaling of
  gradients, and is well suited for problems that are large in terms of
  data/parameters*".

  Args:
    learning_rate: A `Tensor`, floating point value, or a schedule that is a
      `tf.keras.optimizers.schedules.LearningRateSchedule`, or a callable
      that takes no arguments and returns the actual value to use, The
      learning rate. Defaults to 0.001.
    beta_1: A float value or a constant float tensor, or a callable
      that takes no arguments and returns the actual value to use. The
      exponential decay rate for the 1st moment estimates. Defaults to 0.9.
    beta_2: A float value or a constant float tensor, or a callable
      that takes no arguments and returns the actual value to use, The
      exponential decay rate for the 2nd moment estimates. Defaults to 0.999.
    epsilon: A small constant for numerical stability. This epsilon is
      "epsilon hat" in the Kingma and Ba paper (in the formula just before
      Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
      1e-7.
    amsgrad: Boolean. Whether to apply AMSGrad variant of this algorithm from
      the paper "On the Convergence of Adam and beyond". Defaults to `False`.
    name: Optional name for the operations created when applying gradients.
      Defaults to `"Adam"`.
    **kwargs: Keyword arguments. Allowed to be one of
      `"clipnorm"` or `"clipvalue"`.
      `"clipnorm"` (float) clips gradients by norm; `"clipvalue"` (float) clips
      gradients by value.

  Usage:

  >>> opt = tf.keras.optimizers.Adam(learning_rate=0.1)
  >>> var1 = tf.Variable(10.0)
  >>> loss = lambda: (var1 ** 2)/2.0       # d(loss)/d(var1) == var1
  >>> step_count = opt.minimize(loss, [var1]).numpy()
  >>> # The first step is `-learning_rate*sign(grad)`
  >>> var1.numpy()
  9.9

  Reference:
    - [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
    - [Reddi et al., 2018](
        https://openreview.net/pdf?id=ryQu7f-RZ) for `amsgrad`.

  Notes:

  The default value of 1e-7 for epsilon might not be a good default in
  general. For example, when training an Inception network on ImageNet a
  current good choice is 1.0 or 0.1. Note that since Adam uses the
  formulation just before Section 2.1 of the Kingma and Ba paper rather than
  the formulation in Algorithm 1, the "epsilon" referred to here is "epsilon
  hat" in the paper.

  The sparse implementation of this algorithm (used when the gradient is an
  IndexedSlices object, typically because of `tf.gather` or an embedding
  lookup in the forward pass) does apply momentum to variable slices even if
  they were not used in the forward pass (meaning they have a gradient equal
  to zero). Momentum decay (beta1) is also applied to the entire momentum
  accumulator. This means that the sparse behavior is equivalent to the dense
  behavior (in contrast to some momentum implementations which ignore momentum
  unless a variable slice was actually used).
  '''
    epsilon: Incomplete
    amsgrad: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, amsgrad: bool = False, name: str = 'Adam', **kwargs) -> None: ...
    def set_weights(self, weights) -> None: ...
    def get_config(self): ...

class NonFusedAdam(optimizer_v2.OptimizerV2):
    '''Optimizer that implements the Adam algorithm without fused kernels.

  Adam optimization is a stochastic gradient descent method that is based on
  adaptive estimation of first-order and second-order moments.
  According to the paper
  [Adam: A Method for Stochastic Optimization. Kingma et al.,
  2014](http://arxiv.org/abs/1412.6980), the method is "*computationally
  efficient, has little memory requirement, invariant to diagonal rescaling of
  gradients, and is well suited for problems that are large in terms of
  data/parameters*".

  For AMSGrad see [On The Convergence Of Adam And Beyond.
  Reddi et al., 5-8](https://openreview.net/pdf?id=ryQu7f-RZ).

  **If amsgrad = False**:

  initialize $m_0$ as 1st moment vector
  initialize $v_0$ as 2nd moment vector

  The update rule for $\\theta$ with gradient $g$ uses an optimization
  described at the end of section 2 of the paper:

  $$lr_t = \\mathrm{learning\\_rate} *
    \\sqrt{1 - \\beta_2^t} / (1 - \\beta_1^t)$$
  $$m_t = \\beta_1 * m_{t-1} + (1 - \\beta_1) * g$$
  $$v_t = \\beta_2 * v_{t-1} + (1 - \\beta_2) * g^2$$
  $$\\theta_t = \\theta_{t-1} - lr_t * m_t / (\\sqrt{v_t} + \\epsilon)$$

  **If amsgrad = True**:

  initialize $m_0$ as 1st moment vector
  initialize $v_0$ as 2nd moment vector
  initialize $\\hat{v}_0$ as 2nd moment vector

  The update rule for $\\theta$ with gradient $g$ uses an optimization
  described at the end of section 2 of the paper:

  $$lr_t = \\mathrm{learning\\_rate} *
    \\sqrt{1 - \\beta_2^t} / (1 - \\beta_1^t)$$

  $$m_t = \\beta_1 * m_{t-1} + (1 - \\beta_1) * g$$
  $$v_t = \\beta_2 * v_{t-1} + (1 - \\beta_2) * g^2$$
  $$\\hat{v}_t = \\max(\\hat{v}_{t-1}, v_t)$$
  $$\\theta_t = \\theta_{t-1} - lr_t * m_t / (\\sqrt{\\hat{v}_t} + \\epsilon)$$

  The default value of 1e-7 for epsilon might not be a good default in
  general. For example, when training an Inception network on ImageNet a
  current good choice is 1.0 or 0.1. Note that since Adam uses the
  formulation just before Section 2.1 of the Kingma and Ba paper rather than
  the formulation in Algorithm 1, the "epsilon" referred to here is "epsilon
  hat" in the paper.

  The sparse implementation of this algorithm (used when the gradient is an
  IndexedSlices object, typically because of `tf.gather` or an embedding
  lookup in the forward pass) does apply momentum to variable slices even if
  they were not used in the forward pass (meaning they have a gradient equal
  to zero). Momentum decay (beta1) is also applied to the entire momentum
  accumulator. This means that the sparse behavior is equivalent to the dense
  behavior (in contrast to some momentum implementations which ignore momentum
  unless a variable slice was actually used).

  Usage:

  >>> opt = tf.keras.optimizers.Adam(learning_rate=0.1)
  >>> var1 = tf.Variable(10.0)
  >>> loss = lambda: (var1 ** 2)/2.0       # d(loss)/d(var1) == var1
  >>> step_count = opt.minimize(loss, [var1]).numpy()
  >>> # The first step is `-learning_rate*sign(grad)`
  >>> var1.numpy()
  9.9
  '''
    epsilon: Incomplete
    amsgrad: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, amsgrad: bool = False, name: str = 'Adam', **kwargs) -> None:
        '''Construct a new Adam optimizer.

    Args:
      learning_rate: A `Tensor`, floating point value, or a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`, or a callable that
        takes no arguments and returns the actual value to use, The learning
        rate. Defaults to 0.001.
      beta_1: A float value or a constant float tensor, or a callable that takes
        no arguments and returns the actual value to use. The exponential decay
        rate for the 1st moment estimates. Defaults to 0.9.
      beta_2: A float value or a constant float tensor, or a callable that takes
        no arguments and returns the actual value to use, The exponential decay
        rate for the 2nd moment estimates. Defaults to 0.999.
      epsilon: A small constant for numerical stability. This epsilon is
        "epsilon hat" in the Kingma and Ba paper (in the formula just before
        Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
        1e-7.
      amsgrad: Boolean. Whether to apply AMSGrad variant of this algorithm from
        the paper "On the Convergence of Adam and beyond". Defaults to `False`.
      name: Optional name for the operations created when applying gradients.
        Defaults to "Adam".
      **kwargs: keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
        `decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
        gradients by value, `decay` is included for backward compatibility to
        allow time inverse decay of learning rate. `lr` is included for backward
        compatibility, recommended to use `learning_rate` instead.
    '''
    def set_weights(self, weights) -> None: ...
    def get_config(self): ...
