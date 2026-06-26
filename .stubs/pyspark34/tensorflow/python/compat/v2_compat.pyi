from tensorflow.python import tf2 as tf2
from tensorflow.python.data.experimental.ops import counter as counter, interleave_ops as interleave_ops, random_ops as random_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, readers as readers
from tensorflow.python.eager import monitoring as monitoring
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import control_flow_v2_toggles as control_flow_v2_toggles, variable_scope as variable_scope
from tensorflow.python.util.tf_export import tf_export as tf_export

def enable_v2_behavior() -> None:
    """Enables TensorFlow 2.x behaviors.

  This function can be called at the beginning of the program (before `Tensors`,
  `Graphs` or other structures have been created, and before devices have been
  initialized. It switches all global behaviors that are different between
  TensorFlow 1.x and 2.x to behave as intended for 2.x.

  This function is called in the main TensorFlow `__init__.py` file, user should
  not need to call it, except during complex migrations.

  @compatibility(TF2)
  This function is not necessary if you are using TF2. V2 behavior is enabled by
  default.
  @end_compatibility
  """
def disable_v2_behavior() -> None:
    """Disables TensorFlow 2.x behaviors.

  This function can be called at the beginning of the program (before `Tensors`,
  `Graphs` or other structures have been created, and before devices have been
  initialized. It switches all global behaviors that are different between
  TensorFlow 1.x and 2.x to behave as intended for 1.x.

  User can call this function to disable 2.x behavior during complex migrations.

  @compatibility(TF2)
  Using this function indicates that your software is not compatible
  with eager execution and `tf.function` in TF2.

  To migrate to TF2, rewrite your code to be compatible with eager execution.
  Please refer to the [migration guide]
  (https://www.tensorflow.org/guide/migrate) for additional resource on the
  topic.
  @end_compatibility
  """
