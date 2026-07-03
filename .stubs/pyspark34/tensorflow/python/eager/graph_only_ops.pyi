from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.framework import op_callbacks as op_callbacks, ops as ops, tensor_shape as tensor_shape

def graph_placeholder(dtype, shape, name: Incomplete | None = None):
    """Graph-only version of tf.compat.v1.placeholder(), for internal use only."""
