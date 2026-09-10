from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class AdadeltaOptimizer(optimizer.Optimizer):
    """Optimizer that implements the Adadelta algorithm.

  References:
    ADADELTA - An Adaptive Learning Rate Method:
      [Zeiler, 2012](http://arxiv.org/abs/1212.5701)
      ([pdf](http://arxiv.org/pdf/1212.5701v1.pdf))

  @compatibility(TF2)
  tf.compat.v1.train.AdadeltaOptimizer is compatible with eager mode and
  `tf.function`.
  When eager execution is enabled, `learning_rate`, `rho`,
  and `epsilon` can each be a callable that
  takes no arguments and returns the actual value to use. This can be useful
  for changing these values across different invocations of optimizer
  functions.

  To switch to native TF2 style, use [`tf.keras.optimizers.Adadelta`]
  (https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adadelta)
  instead. Please notice that due to the implementation differences,
  `tf.keras.optimizers.Adadelta` and
  `tf.compat.v1.train.AdadeltaOptimizer` may have slight differences in
  floating point numerics even though the formula used for the variable
  updates still matches.

  #### Structural mapping to native TF2

  Before:

  ```python
  optimizer = tf.compat.v1.train.AdadeltaOptimizer(
    learning_rate=learning_rate,
    rho=rho,
    epsilon=epsilon)
  ```

  After:

  ```python
  optimizer = tf.keras.optimizers.Adadelta(
    learning_rate=learning_rate,
    rho=rho,
    epsilon=epsilon)
  ```

  #### How to map arguments
  | TF1 Arg Name       | TF2 Arg Name   | Note                             |
  | ------------------ | -------------  | -------------------------------  |
  | `learning_rate`    | `learning_rate`| Be careful of setting           |
  : : : learning_rate tensor value computed from the global step.          :
  : : : In TF1 this was usually meant to imply a dynamic learning rate and :
  : : : would recompute in each step. In TF2 (eager + function) it will    :
  : : : treat it as a scalar value that only gets computed once instead of :
  : : : a symbolic placeholder to be computed each time.                   :
  | `rho`              | `rho`          | -                                |
  | `epsilon`          | `epsilon`      | Default value is 1e-08 in TF1,   |
  :                    :                : but 1e-07 in TF2.                :
  | `use_locking`      | -              | Not applicable in TF2.           |

  #### Before & after usage example
  Before:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.compat.v1.train.AdadeltaOptimizer(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  After:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.keras.optimizers.Adadelta(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  @end_compatibility
  """
    def __init__(self, learning_rate: float = 0.001, rho: float = 0.95, epsilon: float = 1e-08, use_locking: bool = False, name: str = 'Adadelta') -> None:
        '''Construct a new Adadelta optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value. The learning rate.
        To match the exact form in the original paper use 1.0.
      rho: A `Tensor` or a floating point value. The decay rate.
      epsilon: A `Tensor` or a floating point value.  A constant epsilon used
               to better conditioning the grad update.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Adadelta".


    '''
