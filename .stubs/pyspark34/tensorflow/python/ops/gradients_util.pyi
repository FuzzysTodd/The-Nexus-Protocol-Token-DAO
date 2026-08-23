from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import backprop_util as backprop_util, context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, composite_tensor_gradient as composite_tensor_gradient, dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.framework.func_graph import FuncGraph as FuncGraph
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_state as control_flow_state, control_flow_util as control_flow_util, default_gradient as default_gradient, functional_ops as functional_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.ops.unconnected_gradients import UnconnectedGradients as UnconnectedGradients
from tensorflow.python.util import compat as compat, object_identity as object_identity, variable_utils as variable_utils
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

class AggregationMethod:
    '''A class listing aggregation methods used to combine gradients.

  Computing partial derivatives can require aggregating gradient
  contributions. This class lists the various methods that can
  be used to combine gradients in the graph.

  The following aggregation methods are part of the stable API for
  aggregating gradients:

  *  `ADD_N`: All of the gradient terms are summed as part of one
     operation using the "AddN" op (see `tf.add_n`). This
     method has the property that all gradients must be ready and
     buffered separately in memory before any aggregation is performed.
  *  `DEFAULT`: The system-chosen default aggregation method.

  The following aggregation methods are experimental and may not
  be supported in future releases:

  * `EXPERIMENTAL_TREE`: Gradient terms are summed in pairs using
    the "AddN" op. This method of summing gradients may reduce
    performance, but it can improve memory utilization because the
    gradients can be released earlier.
  * `EXPERIMENTAL_ACCUMULATE_N`: Same as `EXPERIMENTAL_TREE`.

  Example usage when computing gradient:

  >>> @tf.function
  ... def example():
  ...   x = tf.constant(1.0)
  ...   y = x * 2.0
  ...   z = y + y + y + y
  ...   return tf.gradients(z, [x, y],
  ...     aggregation_method=tf.AggregationMethod.EXPERIMENTAL_ACCUMULATE_N)
  >>> example()
  [<tf.Tensor: shape=(), dtype=float32, numpy=8.0>,
   <tf.Tensor: shape=(), dtype=float32, numpy=4.0>]

  '''
    ADD_N: int
    DEFAULT = ADD_N
    EXPERIMENTAL_TREE: int
    EXPERIMENTAL_ACCUMULATE_N: int

POSSIBLE_GRADIENT_TYPES_NONE: int
POSSIBLE_GRADIENT_TYPES_FIRST_ORDER: int
POSSIBLE_GRADIENT_TYPES_HIGHER_ORDER: int

def PossibleTapeGradientTypes(tensors):
    """Determines whether and how `args` may require tape gradients."""
