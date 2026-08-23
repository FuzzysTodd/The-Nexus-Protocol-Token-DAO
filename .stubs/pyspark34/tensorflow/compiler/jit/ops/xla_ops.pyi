from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def xla_cluster_output(input, name: Incomplete | None = None):
    """Operator that connects the output of an XLA computation to other consumer graph nodes.

  Args:
    input: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaClusterOutput: Incomplete

def xla_cluster_output_eager_fallback(input, name, ctx): ...
def xla_launch(constants, args, resources, Tresults, function, name: Incomplete | None = None):
    """XLA Launch Op. For use by the XLA JIT only.

  Args:
    constants: A list of `Tensor` objects.
    args: A list of `Tensor` objects.
    resources: A list of `Tensor` objects with type `resource`.
    Tresults: A list of `tf.DTypes`.
    function: A function decorated with @Defun.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tresults`.
  """

XlaLaunch: Incomplete

def xla_launch_eager_fallback(constants, args, resources, Tresults, function, name, ctx): ...
