from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, init_ops as init_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class RMSPropOptimizer(optimizer.Optimizer):
    """Optimizer that implements the RMSProp algorithm (Tielemans et al.

  2012).

  References:
    Coursera slide 29:
    Hinton, 2012
    ([pdf](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf))

  @compatibility(TF2)
  tf.compat.v1.train.RMSPropOptimizer is compatible with eager mode and
  `tf.function`.
  When eager execution is enabled, `learning_rate`, `decay`, `momentum`,
  and `epsilon` can each be a callable that
  takes no arguments and returns the actual value to use. This can be useful
  for changing these values across different invocations of optimizer
  functions.

  To switch to native TF2 style, use [`tf.keras.optimizers.RMSprop`]
  (https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/RMSprop)
  instead. Please notice that due to the implementation differences,
  `tf.keras.optimizers.RMSprop` and
  `tf.compat.v1.train.RMSPropOptimizer` may have slight differences in
  floating point numerics even though the formula used for the variable
  updates still matches.

  #### Structural mapping to native TF2

  Before:

  ```python
  optimizer = tf.compat.v1.train.RMSPropOptimizer(
    learning_rate=learning_rate,
    decay=decay,
    momentum=momentum,
    epsilon=epsilon)
  ```

  After:

  ```python
  optimizer = tf.keras.optimizers.RMSprop(
    learning_rate=learning_rate,
    rho=decay,
    momentum=momentum,
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
  | `decay`            | `rho`          | -                                |
  | `momentum`         | `momentum`     | -                                |
  | `epsilon`          | `epsilon`      | Default value is 1e-10 in TF1,   |
  :                    :                : but 1e-07 in TF2.                :
  | `use_locking`      | -              | Not applicable in TF2.           |

  #### Before & after usage example
  Before:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.compat.v1.train.RMSPropOptimizer(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  After:

  ```python
  x = tf.Variable([1,2,3], dtype=tf.float32)
  grad = tf.constant([0.1, 0.2, 0.3])
  optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001)
  optimizer.apply_gradients(zip([grad], [x]))
  ```

  @end_compatibility
  """
    def __init__(self, learning_rate, decay: float = 0.9, momentum: float = 0.0, epsilon: float = 1e-10, use_locking: bool = False, centered: bool = False, name: str = 'RMSProp') -> None:
        '''Construct a new RMSProp optimizer.

    Note that in the dense implementation of this algorithm, variables and their
    corresponding accumulators (momentum, gradient moving average, square
    gradient moving average) will be updated even if the gradient is zero
    (i.e. accumulators will decay, momentum will be applied). The sparse
    implementation (used when the gradient is an `IndexedSlices` object,
    typically because of `tf.gather` or an embedding lookup in the forward pass)
    will not update variable slices or their accumulators unless those slices
    were used in the forward pass (nor is there an "eventual" correction to
    account for these omitted updates). This leads to more efficient updates for
    large embedding lookup tables (where most of the slices are not accessed in
    a particular graph execution), but differs from the published algorithm.

    Args:
      learning_rate: A Tensor or a floating point value.  The learning rate.
      decay: Discounting factor for the history/coming gradient
      momentum: A scalar tensor.
      epsilon: Small value to avoid zero denominator.
      use_locking: If True use locks for update operation.
      centered: If True, gradients are normalized by the estimated variance of
        the gradient; if False, by the uncentered second moment. Setting this to
        True may help with training, but is slightly more expensive in terms of
        computation and memory. Defaults to False.
      name: Optional name prefix for the operations created when applying
        gradients. Defaults to "RMSProp".

    '''
