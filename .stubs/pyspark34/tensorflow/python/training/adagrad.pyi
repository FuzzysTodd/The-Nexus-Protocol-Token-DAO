from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, init_ops as init_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class AdagradOptimizer(optimizer.Optimizer):
    """Optimizer that implements the Adagrad algorithm.

  References:
    Adaptive Subgradient Methods for Online Learning and Stochastic Optimization
      :[Duchi et al., 2011](http://jmlr.org/papers/v12/duchi11a.html)
      ([pdf](http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf))

  @compatibility(TF2)
  tf.compat.v1.train.AdagradOptimizer is compatible with eager mode and
  `tf.function`.
  When eager execution is enabled, `learning_rate`,
  `initial_accumulator_value`, and `epsilon` can each be a callable that
  takes no arguments and returns the actual value to use. This can be useful
  for changing these values across different invocations of optimizer
  functions.

  To switch to native TF2 style, use [`tf.keras.optimizers.Adagrad`]
  (https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adagrad)
  instead. Please notice that due to the implementation differences,
  `tf.keras.optimizers.Adagrad` and
  `tf.compat.v1.train.AdagradOptimizer` may have slight differences in
  floating point numerics even though the formula used for the variable
  updates still matches.

  #### Structural mapping to native TF2

  Before:

  ```python
  optimizer = tf.compat.v1.train.AdagradOptimizer(
    learning_rate=learning_rate,
    initial_accumulator_value=initial_accumulator_value)
  ```

  After:

  ```python
  optimizer = tf.keras.optimizers.Adagrad(
    learning_rate=learning_rate,
    initial_accumulator_value=initial_accumulator_value,
    epsilon=1e-07)
  ```

  #### How to map arguments
  | TF1 Arg Name       | TF2 Arg Name   | Note                             |
  | ------------------ | -------------  | -------------------------------  |
  | `learning_rate`    | `learning_rate` | Be careful of setting           |
  : : : learning_rate tensor value computed from the global step.          :
  : : : In TF1 this was usually meant to imply a dynamic learning rate and :
  : : : would recompute in each step. In TF2 (eager + function) it will    :
  : : : treat it as a scalar value that only gets computed once instead of :
  : : : a symbolic placeholder to be computed each time.                   :
  | `initial_accumulator_value` | `initial_accumulator_value` | The        |
  : : : argument can be value of zero in TF2, which is not accepted in TF1.|
  | - | `epsilon`      | `epsilon` is become configurable in TF2. The      |
  : : : defualt value is changed from 1e-8 to 1e-7                         :
  | `use_locking`      | -             | Not applicable in TF2.            |

  #### Before & after usage example
  Before:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.compat.v1.train.AdagradOptimizer(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  After:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.keras.optimizers.Adagrad(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  @end_compatibility
  """
    def __init__(self, learning_rate, initial_accumulator_value: float = 0.1, use_locking: bool = False, name: str = 'Adagrad') -> None:
        '''Construct a new Adagrad optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value.  The learning rate.
      initial_accumulator_value: A floating point value.
        Starting value for the accumulators, must be positive.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Adagrad".

    Raises:
      ValueError: If the `initial_accumulator_value` is invalid.

    '''
