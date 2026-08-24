from _typeshed import Incomplete
from tensorflow.python.distribute import distribute_lib as distribute_lib, distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import control_flow_ops as control_flow_ops, init_ops as init_ops, math_ops as math_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.training import slot_creator as slot_creator
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls

def assign_moving_average(variable, value, decay, zero_debias: bool = True, name: Incomplete | None = None):
    """Compute the moving average of a variable.

  The moving average of 'variable' updated with 'value' is:
    variable * decay + value * (1 - decay)

  The returned Operation sets 'variable' to the newly computed moving average,
  by performing this subtraction:
     variable -= (1 - decay) * (variable - value)

  Since variables that are initialized to a `0` value will be `0` biased,
  `zero_debias` optionally enables scaling by the mathematically correct
  debiasing factor of
    1 - decay ** num_updates
  See Section 3 of (Kingma et al., 2015) for more details.

  The names of the debias shadow variables, by default, include both the scope
  they were created in and the scope of the variables they debias. They are also
  given a uniquifying-suffix.

  E.g.:

  ```
    with tf.compat.v1.variable_scope('scope1'):
      with tf.compat.v1.variable_scope('scope2'):
        var = tf.compat.v1.get_variable('foo')
        update_1 = tf.assign_moving_average(var, 0.0, 1.0)
        update_2 = tf.assign_moving_average(var, 0.0, 0.9)

    # var.name: 'scope1/scope2/foo'
    # shadow var names: 'scope1/scope2/scope1/scope2/foo/biased'
    #                   'scope1/scope2/scope1/scope2/foo/biased_1'
  ```

  Args:
    variable: A Variable.
    value: A tensor with the same shape as 'variable'.
    decay: A float `Tensor` or float value. The moving average decay.
    zero_debias: A python bool. If true, assume the variable is 0-initialized
      and unbias it, as in (Kingma et al., 2015). See docstring in
        `_zero_debias` for more details.
    name: Optional name of the returned operation.

  Returns:
    A tensor which if evaluated will compute and return the new moving average.

  References:
    Adam - A Method for Stochastic Optimization:
      [Kingma et al., 2015](https://arxiv.org/abs/1412.6980)
      ([pdf](https://arxiv.org/pdf/1412.6980.pdf))
  """
def weighted_moving_average(value, decay, weight, truediv: bool = True, collections: Incomplete | None = None, name: Incomplete | None = None):
    '''Compute the weighted moving average of `value`.

  Conceptually, the weighted moving average is:
    `moving_average(value * weight) / moving_average(weight)`,
  where a moving average updates by the rule
    `new_value = decay * old_value + (1 - decay) * update`
  Internally, this Op keeps moving average variables of both `value * weight`
  and `weight`.

  Args:
    value: A numeric `Tensor`.
    decay: A float `Tensor` or float value. The moving average decay.
    weight:  `Tensor` that keeps the current value of a weight. Shape should be
      able to multiply `value`.
    truediv:  Boolean, if `True`, dividing by `moving_average(weight)` is
      floating point division.  If `False`, use division implied by dtypes.
    collections:  List of graph collections keys to add the internal variables
      `value * weight` and `weight` to. Defaults to
      `[GraphKeys.GLOBAL_VARIABLES]`.
    name: Optional name of the returned operation. Defaults to
      "WeightedMovingAvg".

  Returns:
    An Operation that updates and returns the weighted moving average.
  '''

class ExponentialMovingAverage:
    '''Maintains moving averages of variables by employing an exponential decay.

  When training a model, it is often beneficial to maintain moving averages of
  the trained parameters.  Evaluations that use averaged parameters sometimes
  produce significantly better results than the final trained values.

  The `apply()` method adds shadow copies of trained variables the first time
  it is called, and maintains a moving average of the trained variables in
  their shadow copies at every additional invocation.
  It should generally be called immediately after creating the model weights,
  and then after each training step.

  The `average()` method gives access to the shadow variables.
  It allows you to use the moving averages in place of the last trained values
  for evaluations, by loading the moving averages into your model via
  `var.assign(ema.average(var))`.
  Additionally, although `ExponentialMovingAverage`
  objects are not directly trackable by checkpoints,
  `average()` returns the moving average variables for your model weights,
  which you can then checkpoint. (There is an example
  of this near the bottom of this docstring).
  So, `average()` is useful when
  building an evaluation model, or when restoring a model from a checkpoint
  file.

  The moving averages are computed using exponential decay.  You specify the
  decay value (as a scalar float value, `Tensor`, or `Variable`) when creating
  the `ExponentialMovingAverage` object.  The shadow variables are initialized
  with the same initial values as the trained variables.  When you run `apply`
  to update the moving averages, each shadow variable is updated with the
  formula:

    `shadow_variable -= (1 - decay) * (shadow_variable - variable)`

  This is mathematically equivalent to the classic formula below, but the use
  of an `assign_sub` op (the `"-="` in the formula) allows concurrent lockless
  updates to the variables:

    `shadow_variable = decay * shadow_variable + (1 - decay) * variable`

  Reasonable values for `decay` are close to 1.0, typically in the
  multiple-nines range: 0.999, 0.9999, etc.

  To have fine-grained control over the value of the decay parameter during
  training, pass a scalar `tf.Variable` as the `decay` value to the constructor,
  and update the variable as needed.

  Example usage when creating a training model:

  ```python
  # Create variables.
  var0 = tf.Variable(...)
  var1 = tf.Variable(...)
  # ... use the variables to build a training model...

  # Create an ExponentialMovingAverage object
  ema = tf.train.ExponentialMovingAverage(decay=0.9999)

  # The first `apply` creates the shadow variables that hold the moving averages
  ema.apply([var0, var1])

  # grab the moving averages for checkpointing purposes or to be able to
  # load the moving averages into the model weights
  averages = [ema.average(var0), ema.average(var1)]

  ...
  def train_step(...):
  ...
    # Apply the optimizer.
    opt.minimize(my_loss, [var0, var1])

    # Update the moving averages
    # of var0 and var1 with additional calls to `apply`
    ema.apply([var0, var1])

  ...train the model by running train_step multiple times...
  ```

  There are several ways to use the moving averages for evaluations:

  1. Assign the values of the shadow variables to your model variables with
     `Variable.assign(...)` before evaluating your
     model. You can use the `average()`
     method to get the shadow variable for a given variable. To continue
     training after using this approach, make sure to record the unaveraged
     weights and restore them before continuing to train. You can see the
     tensorflow-addons\' MovingAverage optimizer\'s `swap_weights` method for
     one example of how to swap variables efficiently in distributed settings:
     https://github.com/tensorflow/addons/blob/v0.13.0/tensorflow_addons/optimizers/moving_average.py#L151
  2. Make sure to checkpoint out your moving average variables in your
     `tf.train.Checkpoint`. At evaluation time, create your shadow variables and
     use `tf.train.Checkpoint` to restore the moving averages into the shadow
     variables. Then, load the moving averages into the actual model weights via
     `var.assign(moving_avg)`.
  3. Checkpoint out your moving average variables in your `tf.train.Checkpoint`.
     For evaluation, restore your model weights directly from the moving
     averages instead of from the non-averaged weights.
     Caution: If you choose this approach, include only the object-graph paths
     to the averaged path in your checkpoint restore.
     If you point both the unaveraged and averaged paths in a checkpoint
     restore to the same variables, it is hard to reason about whether your
     model will restore the averaged or non-averaged variables.

  Example of saving out then restoring the shadow variable values:

  ```python
  # Create variables.
  var0 = tf.Variable(...)
  var1 = tf.Variable(...)
  # ... use the variables to build a training model...

  # Create an ExponentialMovingAverage object, create the shadow variables,
  # and grab the moving averages for checkpointing purposes.
  # (The ExponentialMovingAverage object itself is not checkpointable)
  ema = tf.train.ExponentialMovingAverage(decay=0.9999)
  ema.apply([var0, var1])
  avg_var0 = ema.average(var0)
  avg_var1 = ema.average(var1)

  # Create a Checkpoint that will manage the model weights and the averages,
  checkpoint = tf.train.Checkpoint(model_weights=[var0, var1],
                                   averaged_weights=[avg_var0, avg_var1])
  ... # Do training

  # Save out the checkpoint including the model weights and the moving averages
  checkpoint.save(...)
  ```

  Restore option: restore all averaged & non-averaged weights, then load
  moving averages into the model via `var.assign()`
  ```python
  # Create variables.
  var0 = tf.Variable(...)
  var1 = tf.Variable(...)
  # ... use the variables to build a training model...

  # Create an ExponentialMovingAverage object, create the shadow variables,
  # and grab the moving averages for checkpoint restore purposes.
  # (The ExponentialMovingAverage object itself is not checkpointable)
  ema = tf.train.ExponentialMovingAverage(decay=0.9999)
  ema.apply([var0, var1])
  avg_var0 = ema.average(var0)
  avg_var1 = ema.average(var1)

  # Create a Checkpoint that will manage the model weights and the averages,
  checkpoint = tf.train.Checkpoint(model_weights=[var0, var1],
                                   averaged_weights=[avg_var0, avg_var1])
  checkpoint.restore(...)
  var0.assign(avg_var0)
  var1.assign(avg_var1)
  # var0 and var1 now hold the moving average values
  ```

  Restore option: Directly restore the moving averages into the model weights.
  ```python
  # Create variables.
  var0 = tf.Variable(...)
  var1 = tf.Variable(...)
  # ... use the variables to build a training model...

  # Create a Checkpoint that will manage two objects with trackable state,
  checkpoint = tf.train.Checkpoint(averaged_weights=[var0, var1])
  checkpoint.restore(...)
  # var0 and var1 now hold the moving average values
  ```
  '''
    def __init__(self, decay, num_updates: Incomplete | None = None, zero_debias: bool = False, name: str = 'ExponentialMovingAverage') -> None:
        """Creates a new ExponentialMovingAverage object.

    The `apply()` method has to be called to create shadow variables.
    Follow-on calls to the `apply()` method will update the moving averages
    in the shadow variables.
    (In TF 1.x graphs `apply()` will return an update op to update
    the moving averages which must be explicitly run).

    The optional `num_updates` parameter allows one to tweak the decay rate
    dynamically. It is typical to pass the count of training steps, usually
    kept in a variable that is incremented at each step, in which case the
    decay rate is lower at the start of training.  This makes moving averages
    move faster.  If passed, the actual decay rate used is:

      `min(decay, (1 + num_updates) / (10 + num_updates))`

    Args:
      decay: A scalar float value, `Tensor`, or `Variable`. The decay parameter.
      num_updates: Optional count of number of updates applied to variables.
      zero_debias: If `True`, zero debias moving-averages that are initialized
        with tensors. (Note: moving averages may not be initialized with
        non-variable tensors when eager execution is enabled).
      name: String. Optional prefix name to use for the name of ops added in
        `apply()`.
    """
    @property
    def name(self):
        """The name of this ExponentialMovingAverage object."""
    def apply(self, var_list: Incomplete | None = None):
        """Maintains moving averages of variables.

    `var_list` must be a list of `Variable` objects.  This method
    creates shadow variables (holding the moving averages)
    for all elements of `var_list`, and
    updates the moving averages using the current `var_list` values. Shadow
    variables for `Variable` objects are initialized to the variable's initial
    value.

    Shadow variables are created with `trainable=False`. To access them you
    can use the EMA object's `average` method. Note that `EMA` objects are
    not trackable by checkpoints, so if you want to checkpoint or restore the
    moving variables you will need to manually grab the shadow
    variables via `average()` and assign them as `tf.Module` properties or
    directly pass them to your `tf.train.Checkpoint`.

    Note that `apply()` can be called multiple times. When eager execution is
    enabled each call to apply will update the variables once, so this needs to
    be called in a loop.

    In legacy TF 1.x graphs, this method returns an op that updates all
    shadow variables from the current value of their associated variables. In
    TF 1.x graphs without automatically control dependencies this op needs to be
    manually run.

    Args:
      var_list: A list of Variable objects. The variables
        must be of types bfloat16, float16, float32, or float64.
        (In legacy TF 1.x graphs these may be tensors, but this is unsupported
        when eager execution is enabled.)

    Returns:
      An Operation that updates the moving averages.

    Raises:
      TypeError: If the arguments are not an allowed type.
    """
    def average(self, var):
        """Returns the `Variable` holding the average of `var`.

    Args:
      var: A `Variable` object.

    Returns:
      A `Variable` object or `None` if the moving average of `var`
      is not maintained.
    """
    def average_name(self, var):
        """[Meant for TF1] Returns name of `Variable` holding the average for `var`.

    (Designed to work with legacy `tf.compat.v1.train.Saver`, it is sensitive to
    specific variable names and not recommended for TF2)

    The typical scenario for `ExponentialMovingAverage` is to compute moving
    averages of variables during training, and restore the variables from the
    computed moving averages during evaluations.

    To restore variables, you have to know the name of the shadow variables.
    That name and the original variable can then be passed to a `Saver()` object
    to restore the variable from the moving average value with:
      `saver = tf.compat.v1.train.Saver({ema.average_name(var): var})`

    `average_name()` can be called whether or not `apply()` has been called.

    Args:
      var: A `Variable` object.

    Returns:
      A string: The name of the variable that will be used or was used
      by the `ExponentialMovingAverage class` to hold the moving average of
      `var`.
    """
    def variables_to_restore(self, moving_avg_variables: Incomplete | None = None):
        """[Designed for TF 1.x] Returns a map of names to `Variables` to restore.

    (Designed to work with legacy `tf.compat.v1.train.Saver`, sensitive to
    specific variable names and not recommended for TF2)

    If a variable has a moving average, use the moving average variable name as
    the restore name; otherwise, use the variable name.

    For example,

    ```python
      variables_to_restore = ema.variables_to_restore()
      saver = tf.compat.v1.train.Saver(variables_to_restore)
    ```

    Below is an example of such mapping:

    ```
      conv/batchnorm/gamma/ExponentialMovingAverage: conv/batchnorm/gamma,
      conv_4/conv2d_params/ExponentialMovingAverage: conv_4/conv2d_params,
      global_step: global_step
    ```

    Args:
      moving_avg_variables: a list of variables that require to use of the
        moving average variable name to be restored. If None, it will default to
        variables.moving_average_variables() + variables.trainable_variables()

    Returns:
      A map from restore_names to variables. The restore_name is either the
      original or the moving average version of the variable name, depending
      on whether the variable name is in the `moving_avg_variables`.
    """
