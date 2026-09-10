from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops, state_ops as state_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class AdamOptimizer(optimizer.Optimizer):
    """Optimizer that implements the Adam algorithm.

  References:
    Adam - A Method for Stochastic Optimization:
      [Kingma et al., 2015](https://arxiv.org/abs/1412.6980)
      ([pdf](https://arxiv.org/pdf/1412.6980.pdf))

  @compatibility(TF2)
  tf.compat.v1.train.AdamOptimizer is compatible with eager mode and
  `tf.function`.
  When eager execution is enabled, `learning_rate`, `beta1`, `beta2`, and
  `epsilon` can each be a callable that takes no arguments and returns the
  actual value to use. This can be useful for changing these values across
  different invocations of optimizer functions.

  To switch to native TF2 style, use [`tf.keras.optimizers.Adam`]
  (https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam)
  instead. Please notice that due to the implementation differences,
  `tf.keras.optimizers.Adam` and
  `tf.compat.v1.train.AdamOptimizer` may have slight differences in
  floating point numerics even though the formula used for the variable
  updates still matches.

  #### Structural Mapping to Native TF2

  Before:

  ```python
  optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.001)
  ```

  After:

  ```python
  optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
  ```

  #### How to Map Arguments
  |TF1 Arg Name          |TF2 Arg Name |Note                  |
  |----------------------|-------------|----------------------|
  |learning_rate         |learning_rate|Be careful of setting learning_rate as a
  :                      :             : tensor value computed from the global
  :                      :             : step. In TF1 this was usually meant to
  :                      :             : imply a dynamic learning rate and would
  :                      :             : recompute in each step. In TF2 (eager +
  :                      :             : function) it will treat it as a scalar
  :                      :             : value that only gets computed once
  :                      :             : instead of a symbolic placeholder to be
  :                      :             : computed each time.                   :
  |beta1                 |beta_1        |                      |
  |beta2                 |beta_2        |                      |
  |epsilon               |epsilon      | Default value is 1e-08 in TF1, but
  :                      :             : 1e-07 in TF2.                     :
  |use_locking           |N/A          |Not applicable in TF2. |

  #### Before & After Usage Example
  Before:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  After:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  @end_compatibility
  """
    def __init__(self, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, use_locking: bool = False, name: str = 'Adam') -> None:
        '''Construct a new Adam optimizer.

    Initialization:

    $$m_0 := 0 \\text{(Initialize initial 1st moment vector)}$$
    $$v_0 := 0 \\text{(Initialize initial 2nd moment vector)}$$
    $$t := 0 \\text{(Initialize timestep)}$$

    The update rule for `variable` with gradient `g` uses an optimization
    described at the end of section 2 of the paper:

    $$t := t + 1$$
    $$\\text{lr}_t := \\mathrm{learning_rate} *
      \\sqrt{1 - \\beta_2^t} / (1 - \\beta_1^t)$$

    $$m_t := \\beta_1 * m_{t-1} + (1 - \\beta_1) * g$$
    $$v_t := \\beta_2 * v_{t-1} + (1 - \\beta_2) * g * g$$
    $$\\text{variable} := \\text{variable} -
      \\text{lr}_t * m_t / (\\sqrt{v_t} + \\epsilon)$$

    The default value of 1e-8 for epsilon might not be a good default in
    general. For example, when training an Inception network on ImageNet a
    current good choice is 1.0 or 0.1. Note that since AdamOptimizer uses the
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

    Args:
      learning_rate: A Tensor or a floating point value.  The learning rate.
      beta1: A float value or a constant float tensor. The exponential decay
        rate for the 1st moment estimates.
      beta2: A float value or a constant float tensor. The exponential decay
        rate for the 2nd moment estimates.
      epsilon: A small constant for numerical stability. This epsilon is
        "epsilon hat" in the Kingma and Ba paper (in the formula just before
        Section 2.1), not the epsilon in Algorithm 1 of the paper.
      use_locking: If True use locks for update operations.
      name: Optional name for the operations created when applying gradients.
        Defaults to "Adam".


    '''
