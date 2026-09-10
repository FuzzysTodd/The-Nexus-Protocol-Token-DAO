from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import sparse_ops as sparse_ops

def any_sparse(classes):
    """Checks for sparse tensor.

  Args:
    classes: a structure of objects that identify the dataset item classes

  Returns:
    `True` if `classes` contains a sparse tensor type and `False` otherwise.
  """
def as_dense_shapes(shapes, classes):
    """Converts sparse tensor shapes to their physical shapes.

  Args:
    shapes: a structure of shapes to convert.
    classes: a structure of objects that identify the dataset item classes

  Returns:
    a structure matching the nested structure of `shapes`, containing
    `tensor_shape.unknown_shape()` at positions where `classes` contains
    `tf.sparse.SparseTensor` and matching contents of `shapes` otherwise
  """
def as_dense_types(types, classes):
    """Converts sparse tensor types to `dtypes.variant`.

  Args:
    types: a structure of types to convert.
    classes: a structure of objects that identify the dataset item classes

  Returns:
    a structure matching the nested structure of `types`, containing
    `dtypes.variant` at positions where `classes` contains
    `tf.sparse.SparseTensor` and matching contents of `types` otherwise
  """
def deserialize_sparse_tensors(tensors, types, shapes, classes):
    """Deserializes sparse tensors.

  Args:
    tensors: a structure of tensors to deserialize.
    types: a structure that holds information about types of `tensors`
    shapes: a structure that holds information about shapes of `tensors`
    classes: a structure of objects that identify the dataset item classes

  Returns:
    `tensors` with any serialized sparse tensors replaced by their deserialized
    version.
  """
def get_classes(tensors):
    """Gets classes for a structure of tensors.

  Args:
    tensors: the tensor structure to get classes for.

  Returns:
    a structure matching the nested structure of `tensors`, containing
    `tf.sparse.SparseTensor` at positions where `tensors` contains a sparse
    tensor and `tf.Tensor` otherwise.
  """
def serialize_many_sparse_tensors(tensors):
    """Serializes many sparse tensors into a batch.

  Args:
    tensors: a tensor structure to serialize.

  Returns:
    `tensors` with any sparse tensors replaced by the serialized batch.
  """
def serialize_sparse_tensors(tensors):
    """Serializes sparse tensors.

  Args:
    tensors: a tensor structure to serialize.

  Returns:
    `tensors` with any sparse tensors replaced by their serialized version.
  """
