from tensorflow.python.ops.gen_image_ops import *
from tensorflow.python.ops.image_ops_impl import *
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_image_ops as gen_image_ops, linalg_ops as linalg_ops

def flat_transforms_to_matrices(transforms):
    """Converts `tf.contrib.image` projective transforms to affine matrices.

  Note that the output matrices map output coordinates to input coordinates. For
  the forward transformation matrix, call `tf.linalg.inv` on the result.

  Args:
    transforms: Vector of length 8, or batches of transforms with shape `(N,
      8)`.

  Returns:
    3D tensor of matrices with shape `(N, 3, 3)`. The output matrices map the
      *output coordinates* (in homogeneous coordinates) of each transform to the
      corresponding *input coordinates*.

  Raises:
    ValueError: If `transforms` have an invalid shape.
  """
def matrices_to_flat_transforms(transform_matrices):
    """Converts affine matrices to `tf.contrib.image` projective transforms.

  Note that we expect matrices that map output coordinates to input coordinates.
  To convert forward transformation matrices, call `tf.linalg.inv` on the
  matrices and use the result here.

  Args:
    transform_matrices: One or more affine transformation matrices, for the
      reverse transformation in homogeneous coordinates. Shape `(3, 3)` or `(N,
      3, 3)`.

  Returns:
    2D tensor of flat transforms with shape `(N, 8)`, which may be passed into
      `tf.contrib.image.transform`.

  Raises:
    ValueError: If `transform_matrices` have an invalid shape.
  """
