from tensorflow.core.config import flags as flags
from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, handle_data_util as handle_data_util, math_ops as math_ops

def IsTrainable(tensor_or_dtype):
    """Determines whether a tensor or dtype supports infinitesimal changes."""
def FlattenNestedIndexedSlices(grad): ...
def AggregateIndexedSlicesGradients(grads):
    """Aggregates gradients containing `IndexedSlices`s."""
