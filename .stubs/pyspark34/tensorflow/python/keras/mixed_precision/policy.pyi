from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.mixed_precision import device_compatibility_check as device_compatibility_check
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.training.experimental import mixed_precision_global_state as mixed_precision_global_state
from tensorflow.python.util.tf_export import keras_export as keras_export

class Policy:
    '''A dtype policy for a Keras layer.

  A dtype policy determines a layer\'s computation and variable dtypes. Each
  layer has a policy. Policies can be passed to the `dtype` argument of layer
  constructors, or a global policy can be set with
  `tf.keras.mixed_precision.set_global_policy`.

  Args:
    name: The policy name, which determines the compute and variable dtypes. Can
      be any dtype name, such as `\'float32\'` or `\'float64\'`, which causes both
      the compute and variable dtypes will be that dtype. Can also be the string
      `\'mixed_float16\'` or `\'mixed_bfloat16\'`, which causes the compute dtype to
      be float16 or bfloat16 and the variable dtype to be float32.

  Typically you only need to interact with dtype policies when using mixed
  precision, which is the use of float16 or bfloat16 for computations and
  float32 for variables. This is why the term `mixed_precision` appears in the
  API name. Mixed precision can be enabled by passing `\'mixed_float16\'` or
  `\'mixed_bfloat16\'` to `tf.keras.mixed_precision.set_global_policy`. See [the
  mixed precision guide](https://www.tensorflow.org/guide/keras/mixed_precision)
  for more information on how to use mixed precision.

  >>> tf.keras.mixed_precision.set_global_policy(\'mixed_float16\')
  >>> layer1 = tf.keras.layers.Dense(10)
  >>> layer1.dtype_policy  # `layer1` will automatically use mixed precision
  <Policy "mixed_float16">
  >>> # Can optionally override layer to use float32 instead of mixed precision.
  >>> layer2 = tf.keras.layers.Dense(10, dtype=\'float32\')
  >>> layer2.dtype_policy
  <Policy "float32">
  >>> # Set policy back to initial float32 for future examples.
  >>> tf.keras.mixed_precision.set_global_policy(\'float32\')

  In the example above, passing `dtype=\'float32\'` to the layer is equivalent to
  passing `dtype=tf.keras.mixed_precision.Policy(\'float32\')`. In general,
  passing a dtype policy name to a layer is equivalent to passing the
  corresponding policy, so it is never necessary to explicitly construct a
  `Policy` object.

  Note: `Model.compile` will automatically wrap an optimizer with a
  `tf.keras.mixed_precision.LossScaleOptimizer` if you use the `\'mixed_float16\'`
  policy. If you use a custom training loop instead of calling `Model.compile`,
  you should explicitly use a `tf.keras.mixed_precision.LossScaleOptimizer` to
  avoid numeric underflow with float16.

  ### How a layer uses its policy\'s compute dtype

  A layer casts its inputs to its compute dtype. This causes the layer\'s
  computations and output to also be in the compute dtype. For example:

  >>> x = tf.ones((4, 4, 4, 4), dtype=\'float64\')
  >>> # `layer`\'s policy defaults to float32.
  >>> layer = tf.keras.layers.Conv2D(filters=4, kernel_size=2)
  >>> layer.compute_dtype  # Equivalent to layer.dtype_policy.compute_dtype
  \'float32\'
  >>> # `layer` casts its inputs to its compute dtype and does computations in
  >>> # that dtype.
  >>> y = layer(x)
  >>> y.dtype
  tf.float32

  Note that the base `tf.keras.layers.Layer` class inserts the casts. If
  subclassing your own layer, you do not have to insert any casts.

  Currently, only tensors in the first argument to the layer\'s `call` method are
  casted (although this will likely be changed in a future minor release). For
  example:

  >>> class MyLayer(tf.keras.layers.Layer):
  ...   # Bug! `b` will not be casted.
  ...   def call(self, a, b):
  ...     return a + 1., b + 1.
  >>> a = tf.constant(1., dtype="float32")
  >>> b = tf.constant(1., dtype="float32")
  >>> layer = MyLayer(dtype="float64")
  >>> x, y = layer(a, b)
  >>> x.dtype
  tf.float64
  >>> y.dtype
  tf.float32

  If writing your own layer with multiple inputs, you should either explicitly
  cast other tensors to `self.compute_dtype` in `call` or accept all tensors in
  the first argument as a list.

  The casting only occurs in TensorFlow 2. If
  `tf.compat.v1.disable_v2_behavior()` has been called, you can enable the
  casting behavior with `tf.compat.v1.keras.layers.enable_v2_dtype_behavior()`.

  ### How a layer uses its policy\'s variable dtype

  The default dtype of variables created by `tf.keras.layers.Layer.add_weight`
  is the layer\'s policy\'s variable dtype.

  If a layer\'s compute and variable dtypes differ, `add_weight` will wrap
  floating-point variables with a special wrapper called an `AutoCastVariable`.
  `AutoCastVariable` is identical to the original variable except it casts
  itself to the layer\'s compute dtype when used within `Layer.call`. This means
  if you are writing a layer, you do not have to explicitly cast the variables
  to the layer\'s compute dtype. For example:

  >>> class SimpleDense(tf.keras.layers.Layer):
  ...
  ...   def build(self, input_shape):
  ...     # With mixed precision, self.kernel is a float32 AutoCastVariable
  ...     self.kernel = self.add_weight(\'kernel\', (input_shape[-1], 10))
  ...
  ...   def call(self, inputs):
  ...     # With mixed precision, self.kernel will be casted to float16
  ...     return tf.linalg.matmul(inputs, self.kernel)
  ...
  >>> layer = SimpleDense(dtype=\'mixed_float16\')
  >>> y = layer(tf.ones((10, 10)))
  >>> y.dtype
  tf.float16
  >>> layer.kernel.dtype
  tf.float32

  A layer author can prevent a variable from being wrapped with an
  `AutoCastVariable` by passing `experimental_autocast=False` to `add_weight`,
  which is useful if the float32 value of the variable must be accessed within
  the layer.

  ### How to write a layer that supports mixed precision and float64.

  For the most part, layers will automatically support mixed precision and
  float64 without any additional work, due to the fact the base layer
  automatically casts inputs, creates variables of the correct type, and in the
  case of mixed precision, wraps variables with `AutoCastVariables`.

  The primary case where you need extra work to support mixed precision or
  float64 is when you create a new tensor, such as with `tf.ones` or
  `tf.random.normal`, In such cases, you must create the tensor of the correct
  dtype. For example, if you call `tf.random.normal`, you must pass the compute
  dtype, which is the dtype the inputs have been casted to:

  >>> class AddRandom(tf.keras.layers.Layer):
  ...
  ...   def call(self, inputs):
  ...     # We must pass `dtype=inputs.dtype`, otherwise a TypeError may
  ...     # occur when adding `inputs` to `rand`.
  ...     rand = tf.random.normal(shape=inputs.shape, dtype=inputs.dtype)
  ...     return inputs + rand
  >>> layer = AddRandom(dtype=\'mixed_float16\')
  >>> y = layer(x)
  >>> y.dtype
  tf.float16

  If you did not pass `dtype=inputs.dtype` to `tf.random.normal`, a
  `TypeError` would have occurred. This is because the `tf.random.normal`\'s
  dtype defaults to `"float32"`, but the input dtype is float16. You cannot add
  a float32 tensor with a float16 tensor.
  '''
    def __init__(self, name) -> None: ...
    @property
    def variable_dtype(self):
        """The variable dtype of this policy.

    This is the dtype layers will create their variables in, unless a layer
    explicitly chooses a different dtype. If this is different than
    `Policy.compute_dtype`, Layers will cast variables to the compute dtype to
    avoid type errors.

    Variable regularizers are run in the variable dtype, not the compute dtype.

    Returns:
      The variable dtype of this policy, as a string.
    """
    @property
    def compute_dtype(self):
        """The compute dtype of this policy.

    This is the dtype layers will do their computations in. Typically layers
    output tensors with the compute dtype as well.

    Note that even if the compute dtype is float16 or bfloat16, hardware devices
    may not do individual adds, multiplies, and other fundamental operations in
    float16 or bfloat16, but instead may do some of them in float32 for numeric
    stability. The compute dtype is the dtype of the inputs and outputs of the
    TensorFlow ops that the layer executes. Internally, many TensorFlow ops will
    do certain internal calculations in float32 or some other device-internal
    intermediate format with higher precision than float16/bfloat16, to increase
    numeric stability.

    For example, a `tf.keras.layers.Dense` layer, when run on a GPU with a
    float16 compute dtype, will pass float16 inputs to `tf.linalg.matmul`. But,
    `tf.linalg.matmul` will do use float32 intermediate math. The performance
    benefit of float16 is still apparent, due to increased memory bandwidth and
    the fact modern GPUs have specialized hardware for computing matmuls on
    float16 inputs while still keeping intermediate computations in float32.

    Returns:
      The compute dtype of this policy, as a string.
    """
    @property
    def name(self):
        """Returns the name of this policy."""
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class PolicyV1(Policy):
    '''A deprecated dtype policy for a Keras layer.

  Warning: This class is now deprecated and will be removed soon. Please use the
  non-experimental class `tf.keras.mixed_precision.Policy` instead.

  The difference between this class and the non-experimental class is that this
  class has a `loss_scale` field and the non-experimental class does not. The
  loss scale is only used by `tf.keras.Model.compile`, which automatically wraps
  the optimizer with a `LossScaleOptimizer` if the optimizer is not already a
  `LossScaleOptimizer`. For the non-experimental Policy class, `Model.compile`
  instead wraps the optimizer with a `LossScaleOptimizer` if `Policy.name` is
  "mixed_float16".

  When deserializing objects with an experimental policy using functions like
  `tf.keras.utils.deserialize_keras_object`, the policy will be deserialized as
  the non-experimental `tf.keras.mixed_precision.Policy`, and the loss scale
  will silently be dropped. This is so that SavedModels that are generated
  with an experimental policy can be restored after the experimental policy is
  removed.
  '''
    def __init__(self, name, loss_scale: str = 'auto') -> None:
        '''Constructs the policy.

    The `name` argument determines the compute and variable dtype, the default
    loss scale, and has no additional effect on the Policy. The compute and
    variable dtypes can only be specified through `name`, and cannot be
    specified directly.

    Args:
      name: A string. Can be one of the following values:
        * Any dtype name, such as \'float32\' or \'float64\'. Both the variable and
          compute dtypes will be that dtype.
        * \'mixed_float16\' or \'mixed_bfloat16\': The compute dtype is float16 or
          bfloat16, while the variable dtype is float32. With \'mixed_float16\',
          a dynamic loss scale is used. These policies are used for mixed
          precision training.
      loss_scale: A `tf.compat.v1.mixed_precision.LossScale`, an int (which
        uses a `FixedLossScale`), the string "dynamic" (which uses a
        `DynamicLossScale`), or None (which uses no loss scale). Defaults to
        `"auto"`. In the `"auto"` case: 1) if `name` is `"mixed_float16"`, then
        use `loss_scale="dynamic"`. 2) otherwise, do not use a loss scale. Only
        `tf.keras.Model`s, not layers, use the loss scale, and it is only used
        during `Model.fit`, `Model.train_on_batch`, and other similar methods.
    '''
    @property
    def loss_scale(self):
        """Returns the loss scale of this Policy.

    Returns:
      A `tf.compat.v1.mixed_precision.experimental.LossScale`, or None.
    """
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

def global_policy():
    '''Returns the global dtype policy.

  The global policy is the default `tf.keras.mixed_precision.Policy` used for
  layers, if no policy is passed to the layer constructor. If no policy has been
  set with `keras.mixed_precision.set_global_policy`, this will return a policy
  constructed from `tf.keras.backend.floatx()` (floatx defaults to float32).

  >>> tf.keras.mixed_precision.global_policy()
  <Policy "float32">
  >>> tf.keras.layers.Dense(10).dtype_policy  # Defaults to the global policy
  <Policy "float32">

  If TensorFlow 2 behavior has been disabled with
  `tf.compat.v1.disable_v2_behavior()`, this will instead return a special
  "_infer" policy which infers the dtype from the dtype of the first input the
  first time the layer is called. This behavior matches the behavior that
  existed in TensorFlow 1.

  See `tf.keras.mixed_precision.Policy` for more information on policies.

  Returns:
    The global Policy.
  '''
def set_global_policy(policy) -> None:
    '''Sets the global dtype policy.

  The global policy is the default `tf.keras.mixed_precision.Policy` used for
  layers, if no policy is passed to the layer constructor.

  >>> tf.keras.mixed_precision.set_global_policy(\'mixed_float16\')
  >>> tf.keras.mixed_precision.global_policy()
  <Policy "mixed_float16">
  >>> tf.keras.layers.Dense(10).dtype_policy
  <Policy "mixed_float16">
  >>> # Global policy is not used if a policy is directly passed to constructor
  >>> tf.keras.layers.Dense(10, dtype=\'float64\').dtype_policy
  <Policy "float64">
  >>> tf.keras.mixed_precision.set_global_policy(\'float32\')

  If no global policy is set, layers will instead default to a Policy
  constructed from `tf.keras.backend.floatx()`.

  To use mixed precision, the global policy should be set to `\'mixed_float16\'`
  or `\'mixed_bfloat16\'`, so that every layer uses a 16-bit compute dtype and
  float32 variable dtype by default.

  Only floating point policies can be set as the global policy, such as
  `\'float32\'` and `\'mixed_float16\'`. Non-floating point policies such as
  `\'int32\'` and `\'complex64\'` cannot be set as the global policy because most
  layers do not support such policies.

  See `tf.keras.mixed_precision.Policy` for more information.

  Args:
    policy: A Policy, or a string that will be converted to a Policy. Can also
      be None, in which case the global policy will be constructed from
      `tf.keras.backend.floatx()`
  '''
def policy_scope(policy) -> Generator[None, None, None]:
    """A context manager that sets the global Policy under it.

  Args:
    policy: A Policy, or a string that will be converted to a Policy..

  Yields:
    Nothing.
  """
def serialize(policy): ...
def deserialize(config, custom_objects: Incomplete | None = None): ...
