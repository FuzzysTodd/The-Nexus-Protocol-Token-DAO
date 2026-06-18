from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, image_ops as image_ops, map_fn as map_fn, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util import dispatch as dispatch

def resize_images_v2(images: ragged_tensor.RaggedTensor, size, method=..., preserve_aspect_ratio: bool = False, antialias: bool = False, name: Incomplete | None = None):
    """RaggedTensor dispatcher for tf.image.resize (tf-v2)."""
def resize_images_v1(images: ragged_tensor.RaggedTensor, size, method=..., align_corners: bool = False, preserve_aspect_ratio: bool = False, name: Incomplete | None = None):
    """RaggedTensor dispatcher for tf.image.resize (tf-v1)."""
