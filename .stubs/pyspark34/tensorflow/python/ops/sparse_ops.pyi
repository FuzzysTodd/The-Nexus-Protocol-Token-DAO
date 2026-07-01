from tensorflow.python.ops.gen_sparse_ops import *
from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_sparse_ops as gen_sparse_ops, math_ops as math_ops, special_math_ops as special_math_ops
from tensorflow.python.util import compat as compat, deprecation as deprecation, dispatch as dispatch, nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import get_canonical_name_for_symbol as get_canonical_name_for_symbol, tf_export as tf_export

def from_dense(tensor, name: Incomplete | None = None):
    """Converts a dense tensor into a sparse tensor.

  Only elements not equal to zero will be present in the result. The resulting
  `SparseTensor` has the same dtype and shape as the input.

  >>> sp = tf.sparse.from_dense([0, 0, 3, 0, 1])
  >>> sp.shape.as_list()
  [5]
  >>> sp.values.numpy()
  array([3, 1], dtype=int32)
  >>> sp.indices.numpy()
  array([[2],
         [4]])

  Args:
    tensor: A dense `Tensor` to be converted to a `SparseTensor`.
    name: Optional name for the op.

  Returns:
    The `SparseTensor`.
  """
def sparse_expand_dims(sp_input, axis: Incomplete | None = None, name: Incomplete | None = None):
    '''Returns a tensor with an length 1 axis inserted at index `axis`.

  Given a tensor `input`, this operation inserts a dimension of length 1 at the
  dimension index `axis` of `input`\'s shape. The dimension index follows python
  indexing rules: It\'s zero-based, a negative index it is counted backward
  from the end.

  This operation is useful to:

  * Add an outer "batch" dimension to a single element.
  * Align axes for broadcasting.
  * To add an inner vector length axis to a tensor of scalars.

  For example:

  If you have a sparse tensor with shape `[height, width, depth]`:

  >>> sp = tf.sparse.SparseTensor(indices=[[3,4,1]], values=[7,],
  ...                             dense_shape=[10,10,3])

  You can add an outer `batch` axis by passing `axis=0`:

  >>> tf.sparse.expand_dims(sp, axis=0).shape.as_list()
  [1, 10, 10, 3]

  The new axis location matches Python `list.insert(axis, 1)`:

  >>> tf.sparse.expand_dims(sp, axis=1).shape.as_list()
  [10, 1, 10, 3]

  Following standard python indexing rules, a negative `axis` counts from the
  end so `axis=-1` adds an inner most dimension:

  >>> tf.sparse.expand_dims(sp, axis=-1).shape.as_list()
  [10, 10, 3, 1]

  Note: Unlike `tf.expand_dims` this function includes a default value for the
  `axis`: `-1`. So if `axis is not specified, an inner dimension is added.

  >>> sp.shape.as_list()
  [10, 10, 3]
  >>> tf.sparse.expand_dims(sp).shape.as_list()
  [10, 10, 3, 1]

  This operation requires that `axis` is a valid index for `input.shape`,
  following python indexing rules:

  ```
  -1-tf.rank(input) <= axis <= tf.rank(input)
  ```

  This operation is related to:

  * `tf.expand_dims`, which provides this functionality for dense tensors.
  * `tf.squeeze`, which removes dimensions of size 1, from dense tensors.
  * `tf.sparse.reshape`, which provides more flexible reshaping capability.

  Args:
    sp_input: A `SparseTensor`.
    axis: 0-D (scalar). Specifies the dimension index at which to expand the
      shape of `input`. Must be in the range `[-rank(sp_input) - 1,
      rank(sp_input)]`. Defaults to `-1`.
    name: The name of the output `SparseTensor`.

  Returns:
    A `SparseTensor` with the same data as `sp_input`, but its shape has an
    additional dimension of size 1 added.
  '''
def sparse_eye(num_rows, num_columns: Incomplete | None = None, dtype=..., name: Incomplete | None = None):
    '''Creates a two-dimensional sparse tensor with ones along the diagonal.

  Args:
    num_rows: Non-negative integer or `int32` scalar `tensor` giving the number
      of rows in the resulting matrix.
    num_columns: Optional non-negative integer or `int32` scalar `tensor` giving
      the number of columns in the resulting matrix. Defaults to `num_rows`.
    dtype: The type of element in the resulting `Tensor`.
    name: A name for this `Op`. Defaults to "eye".

  Returns:
    A `SparseTensor` of shape [num_rows, num_columns] with ones along the
    diagonal.
  '''
def sparse_concat(axis, sp_inputs, name: Incomplete | None = None, expand_nonconcat_dim: bool = False, concat_dim: Incomplete | None = None, expand_nonconcat_dims: Incomplete | None = None):
    '''Concatenates a list of `SparseTensor` along the specified dimension.

  Concatenation is with respect to the dense versions of each sparse input.
  It is assumed that each inputs is a `SparseTensor` whose elements are ordered
  along increasing dimension number.

  If expand_nonconcat_dim is False, all inputs\' shapes must match, except for
  the concat dimension. If expand_nonconcat_dim is True, then inputs\' shapes are
  allowed to vary among all inputs.

  The `indices`, `values`, and `shapes` lists must have the same length.

  If expand_nonconcat_dim is False, then the output shape is identical to the
  inputs\', except along the concat dimension, where it is the sum of the inputs\'
  sizes along that dimension.

  If expand_nonconcat_dim is True, then the output shape along the non-concat
  dimensions will be expand to be the largest among all inputs, and it is the
  sum of the inputs sizes along the concat dimension.

  The output elements will be resorted to preserve the sort order along
  increasing dimension number.

  This op runs in `O(M log M)` time, where `M` is the total number of non-empty
  values across all inputs. This is due to the need for an internal sort in
  order to concatenate efficiently across an arbitrary dimension.

  For example, if `axis = 1` and the inputs are

      sp_inputs[0]: shape = [2, 3]
      [0, 2]: "a"
      [1, 0]: "b"
      [1, 1]: "c"

      sp_inputs[1]: shape = [2, 4]
      [0, 1]: "d"
      [0, 2]: "e"

  then the output will be

      shape = [2, 7]
      [0, 2]: "a"
      [0, 4]: "d"
      [0, 5]: "e"
      [1, 0]: "b"
      [1, 1]: "c"

  Graphically this is equivalent to doing

      [    a] concat [  d e  ] = [    a   d e  ]
      [b c  ]        [       ]   [b c          ]

  Another example, if \'axis = 1\' and the inputs are

      sp_inputs[0]: shape = [3, 3]
      [0, 2]: "a"
      [1, 0]: "b"
      [2, 1]: "c"

      sp_inputs[1]: shape = [2, 4]
      [0, 1]: "d"
      [0, 2]: "e"

  if expand_nonconcat_dim = False, this will result in an error. But if
  expand_nonconcat_dim = True, this will result in:

      shape = [3, 7]
      [0, 2]: "a"
      [0, 4]: "d"
      [0, 5]: "e"
      [1, 0]: "b"
      [2, 1]: "c"

  Graphically this is equivalent to doing

      [    a] concat [  d e  ] = [    a   d e  ]
      [b    ]        [       ]   [b            ]
      [  c  ]                    [  c          ]


  Args:
    axis: Dimension to concatenate along. Must be in range [-rank, rank),
      where rank is the number of dimensions in each input `SparseTensor`.
    sp_inputs: List of `SparseTensor` to concatenate.
    name: A name prefix for the returned tensors (optional).
    expand_nonconcat_dim: Whether to allow the expansion in the non-concat
      dimensions. Defaulted to False.
    concat_dim: The old (deprecated) name for axis.
    expand_nonconcat_dims: alias for expand_nonconcat_dim

  Returns:
    A `SparseTensor` with the concatenated output.

  Raises:
    TypeError: If `sp_inputs` is not a list of `SparseTensor`.
  '''
def sparse_concat_v2(axis, sp_inputs, expand_nonconcat_dims: bool = False, name: Incomplete | None = None): ...
def sparse_add(a, b, threshold: Incomplete | None = None, thresh: Incomplete | None = None):
    '''Adds two tensors, at least one of each is a `SparseTensor`.

  If one `SparseTensor` and one `Tensor` are passed in, returns a `Tensor`.  If
  both arguments are `SparseTensor`s, this returns a `SparseTensor`.  The order
  of arguments does not matter.  Use vanilla `tf.add()` for adding two dense
  `Tensor`s.

  The shapes of the two operands must match: broadcasting is not supported.

  The indices of any input `SparseTensor` are assumed ordered in standard
  lexicographic order.  If this is not the case, before this step run
  `SparseReorder` to restore index ordering.

  If both arguments are sparse, we perform "clipping" as follows.  By default,
  if two values sum to zero at some index, the output `SparseTensor` would still
  include that particular location in its index, storing a zero in the
  corresponding value slot.  To override this, callers can specify `thresh`,
  indicating that if the sum has a magnitude strictly smaller than `thresh`, its
  corresponding value and index would then not be included.  In particular,
  `thresh == 0.0` (default) means everything is kept and actual thresholding
  happens only for a positive value.

  For example, suppose the logical sum of two sparse operands is (densified):

      [       2]
      [.1     0]
      [ 6   -.2]

  Then,

  * `thresh == 0` (the default): all 5 index/value pairs will be returned.
  * `thresh == 0.11`: only .1 and 0 will vanish, and the remaining three
      index/value pairs will be returned.
  * `thresh == 0.21`: .1, 0, and -.2 will vanish.

  Args:
    a: The first operand; `SparseTensor` or `Tensor`.
    b: The second operand; `SparseTensor` or `Tensor`. At least one operand
      must be sparse.
    threshold: An optional 0-D `Tensor` (defaults to `0`). The magnitude
      threshold that determines if an output value/index pair takes space. Its
      dtype should match that of the values if they are real; if the latter are
      complex64/complex128, then the dtype should be float32/float64,
      correspondingly.
    thresh: Deprecated alias for `threshold`.

  Returns:
    A `SparseTensor` or a `Tensor`, representing the sum.

  Raises:
    TypeError: If both `a` and `b` are `Tensor`s.  Use `tf.add()` instead.
  '''
def sparse_add_v2(a, b, threshold: int = 0):
    '''Adds two tensors, at least one of each is a `SparseTensor`.

  If one `SparseTensor` and one `Tensor` are passed in, returns a `Tensor`.  If
  both arguments are `SparseTensor`s, this returns a `SparseTensor`.  The order
  of arguments does not matter.  Use vanilla `tf.add()` for adding two dense
  `Tensor`s.

  The shapes of the two operands must match: broadcasting is not supported.

  The indices of any input `SparseTensor` are assumed ordered in standard
  lexicographic order.  If this is not the case, before this step run
  `SparseReorder` to restore index ordering.

  If both arguments are sparse, we perform "clipping" as follows.  By default,
  if two values sum to zero at some index, the output `SparseTensor` would still
  include that particular location in its index, storing a zero in the
  corresponding value slot.  To override this, callers can specify `threshold`,
  indicating that if the sum has a magnitude strictly smaller than `threshold`,
  its corresponding value and index would then not be included.  In particular,
  `threshold == 0.0` (default) means everything is kept and actual thresholding
  happens only for a positive value.

  For example, suppose the logical sum of two sparse operands is (densified):

      [       2]
      [.1     0]
      [ 6   -.2]

  Then,

  * `threshold == 0` (the default): all 5 index/value pairs will be
      returned.
  * `threshold == 0.11`: only .1 and 0 will vanish, and the remaining three
      index/value pairs will be returned.
  * `threshold == 0.21`: .1, 0, and -.2 will vanish.

  Args:
    a: The first operand; `SparseTensor` or `Tensor`.
    b: The second operand; `SparseTensor` or `Tensor`. At least one operand
      must be sparse.
    threshold: A 0-D `Tensor`. The magnitude threshold that determines if an
      output value/index pair takes space. Its dtype should match that of the
      values if they are real; if the latter are complex64/complex128, then the
      dtype should be float32/float64, correspondingly.

  Returns:
    A `SparseTensor` or a `Tensor`, representing the sum.

  Raises:
    TypeError: If both `a` and `b` are `Tensor`s.  Use `tf.add()` instead.
  '''
def sparse_cross(inputs, name: Incomplete | None = None, separator: Incomplete | None = None):
    '''Generates sparse cross from a list of sparse and dense tensors.

  For example, if the inputs are

      * inputs[0]: SparseTensor with shape = [2, 2]
        [0, 0]: "a"
        [1, 0]: "b"
        [1, 1]: "c"
      * inputs[1]: SparseTensor with shape = [2, 1]
        [0, 0]: "d"
        [1, 0]: "e"
      * inputs[2]: Tensor [["f"], ["g"]]

  then the output will be:

      shape = [2, 2]
      [0, 0]: "a_X_d_X_f"
      [1, 0]: "b_X_e_X_g"
      [1, 1]: "c_X_e_X_g"

  Customized separator "_Y_":

  >>> inp_0 = tf.constant([[\'a\'], [\'b\']])
  >>> inp_1 = tf.constant([[\'c\'], [\'d\']])
  >>> output = tf.sparse.cross([inp_0, inp_1], separator=\'_Y_\')
  >>> output.values
  <tf.Tensor: shape=(2,), dtype=string, numpy=array([b\'a_Y_c\', b\'b_Y_d\'],
    dtype=object)>


  Args:
    inputs: An iterable of `Tensor` or `SparseTensor`.
    name: Optional name for the op.
    separator: A string added between each string being joined. Defaults to
      \'_X_\'.

  Returns:
    A `SparseTensor` of type `string`.
  '''
def sparse_cross_hashed(inputs, num_buckets: int = 0, hash_key: Incomplete | None = None, name: Incomplete | None = None):
    '''Generates hashed sparse cross from a list of sparse and dense tensors.

  For example, if the inputs are

      * inputs[0]: SparseTensor with shape = [2, 2]
        [0, 0]: "a"
        [1, 0]: "b"
        [1, 1]: "c"
      * inputs[1]: SparseTensor with shape = [2, 1]
        [0, 0]: "d"
        [1, 0]: "e"
      * inputs[2]: Tensor [["f"], ["g"]]

  then the output will be:

      shape = [2, 2]
      [0, 0]: FingerprintCat64(
                  Fingerprint64("f"), FingerprintCat64(
                      Fingerprint64("d"), Fingerprint64("a")))
      [1, 0]: FingerprintCat64(
                  Fingerprint64("g"), FingerprintCat64(
                      Fingerprint64("e"), Fingerprint64("b")))
      [1, 1]: FingerprintCat64(
                  Fingerprint64("g"), FingerprintCat64(
                      Fingerprint64("e"), Fingerprint64("c")))

  Args:
    inputs: An iterable of `Tensor` or `SparseTensor`.
    num_buckets: An `int` that is `>= 0`.
      output = hashed_value%num_buckets if num_buckets > 0 else hashed_value.
    hash_key: Integer hash_key that will be used by the `FingerprintCat64`
      function. If not given, will use a default key.
    name: Optional name for the op.

  Returns:
    A `SparseTensor` of type `int64`.
  '''
def sparse_dense_cwise_add(sp_t, dense_t):
    """Adds up a SparseTensor and a dense Tensor, using these special rules:

  (1) Broadcasts the dense side to have the same shape as the sparse side, if
      eligible;
  (2) Then, only the dense values pointed to by the indices of the SparseTensor
      participate in the cwise addition.

  By the rules, the result is a logical SparseTensor with exactly the same
  indices and shape, but possibly with different non-zero values.  The output of
  this Op is the resultant non-zero values.

  Args:
    sp_t: the SparseTensor operand.
    dense_t: the dense Tensor operand; must have the same dtype and a
      broadcast-compatible shape as `sp_t`.

  Returns:
    output: the SparseTensor output.
  """
def sparse_reorder(sp_input, name: Incomplete | None = None):
    """Reorders a `SparseTensor` into the canonical, row-major ordering.

  Note that by convention, all sparse ops preserve the canonical ordering
  along increasing dimension number. The only time ordering can be violated
  is during manual manipulation of the indices and values to add entries.

  Reordering does not affect the shape of the `SparseTensor`.

  For example, if `sp_input` has shape `[4, 5]` and `indices` / `values`:

      [0, 3]: b
      [0, 1]: a
      [3, 1]: d
      [2, 0]: c

  then the output will be a `SparseTensor` of shape `[4, 5]` and
  `indices` / `values`:

      [0, 1]: a
      [0, 3]: b
      [2, 0]: c
      [3, 1]: d

  Args:
    sp_input: The input `SparseTensor`.
    name: A name prefix for the returned tensors (optional)

  Returns:
    A `SparseTensor` with the same shape and non-empty values, but in
    canonical ordering.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def sparse_reshape(sp_input, shape, name: Incomplete | None = None):
    """Reshapes a `SparseTensor` to represent values in a new dense shape.

  This operation has the same semantics as `reshape` on the represented dense
  tensor.  The indices of non-empty values in `sp_input` are recomputed based
  on the new dense shape, and a new `SparseTensor` is returned containing the
  new indices and new shape.  The order of non-empty values in `sp_input` is
  unchanged.

  If one component of `shape` is the special value -1, the size of that
  dimension is computed so that the total dense size remains constant.  At
  most one component of `shape` can be -1.  The number of dense elements
  implied by `shape` must be the same as the number of dense elements
  originally represented by `sp_input`.

  For example, if `sp_input` has shape `[2, 3, 6]` and `indices` / `values`:

      [0, 0, 0]: a
      [0, 0, 1]: b
      [0, 1, 0]: c
      [1, 0, 0]: d
      [1, 2, 3]: e

  and `shape` is `[9, -1]`, then the output will be a `SparseTensor` of
  shape `[9, 4]` and `indices` / `values`:

      [0, 0]: a
      [0, 1]: b
      [1, 2]: c
      [4, 2]: d
      [8, 1]: e

  Args:
    sp_input: The input `SparseTensor`.
    shape: A 1-D (vector) int64 `Tensor` specifying the new dense shape of the
      represented `SparseTensor`.
    name: A name prefix for the returned tensors (optional)

  Returns:
    A `SparseTensor` with the same non-empty values but with indices calculated
    by the new dense shape.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
    ValueError:  If argument `shape` requests a `SparseTensor` with a different
      number of elements than `sp_input`.
    ValueError:  If `shape` has more than one inferred (== -1) dimension.
  """

class KeywordRequired: ...

def sparse_split(keyword_required=..., sp_input: Incomplete | None = None, num_split: Incomplete | None = None, axis: Incomplete | None = None, name: Incomplete | None = None, split_dim: Incomplete | None = None):
    """Split a `SparseTensor` into `num_split` tensors along `axis`.

  If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split`
  each slice starting from 0:`shape[axis] % num_split` gets extra one
  dimension. For example, if `axis = 1` and `num_split = 2` and the
  input is:

      input_tensor = shape = [2, 7]
      [    a   d e  ]
      [b c          ]

  Graphically the output tensors are:

      output_tensor[0] =
      [    a   ]
      [b c     ]

      output_tensor[1] =
      [ d e  ]
      [      ]

  Args:
    keyword_required: Python 2 standin for * (temporary for argument reorder)
    sp_input: The `SparseTensor` to split.
    num_split: A Python integer. The number of ways to split.
    axis: A 0-D `int32` `Tensor`. The dimension along which to split. Must be in
      range [-rank, rank), where rank is the number of dimensions in the input
      `SparseTensor`.
    name: A name for the operation (optional).
    split_dim: Deprecated old name for axis.

  Returns:
    `num_split` `SparseTensor` objects resulting from splitting `value`.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
    ValueError: If the deprecated `split_dim` and `axis` are both non None.
  """
def sparse_split_v2(sp_input: Incomplete | None = None, num_split: Incomplete | None = None, axis: Incomplete | None = None, name: Incomplete | None = None):
    """Split a `SparseTensor` into `num_split` tensors along `axis`.

  If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split`
  each slice starting from 0:`shape[axis] % num_split` gets extra one
  dimension. For example:

  >>> indices = [[0, 2], [0, 4], [0, 5], [1, 0], [1, 1]]
  >>> values = [1, 2, 3, 4, 5]
  >>> t = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=[2, 7])
  >>> tf.sparse.to_dense(t)
  <tf.Tensor: shape=(2, 7), dtype=int32, numpy=
  array([[0, 0, 1, 0, 2, 3, 0],
         [4, 5, 0, 0, 0, 0, 0]], dtype=int32)>

  >>> output = tf.sparse.split(sp_input=t, num_split=2, axis=1)
  >>> tf.sparse.to_dense(output[0])
  <tf.Tensor: shape=(2, 4), dtype=int32, numpy=
  array([[0, 0, 1, 0],
         [4, 5, 0, 0]], dtype=int32)>
  >>> tf.sparse.to_dense(output[1])
  <tf.Tensor: shape=(2, 3), dtype=int32, numpy=
  array([[2, 3, 0],
         [0, 0, 0]], dtype=int32)>

  >>> output = tf.sparse.split(sp_input=t, num_split=2, axis=0)
  >>> tf.sparse.to_dense(output[0])
  <tf.Tensor: shape=(1, 7), dtype=int32, numpy=array([[0, 0, 1, 0, 2, 3, 0]],
  dtype=int32)>
  >>> tf.sparse.to_dense(output[1])
  <tf.Tensor: shape=(1, 7), dtype=int32, numpy=array([[4, 5, 0, 0, 0, 0, 0]],
  dtype=int32)>

  >>> output = tf.sparse.split(sp_input=t, num_split=2, axis=-1)
  >>> tf.sparse.to_dense(output[0])
  <tf.Tensor: shape=(2, 4), dtype=int32, numpy=
  array([[0, 0, 1, 0],
         [4, 5, 0, 0]], dtype=int32)>
  >>> tf.sparse.to_dense(output[1])
  <tf.Tensor: shape=(2, 3), dtype=int32, numpy=
  array([[2, 3, 0],
         [0, 0, 0]], dtype=int32)>

  Args:
    sp_input: The `SparseTensor` to split.
    num_split: A Python integer. The number of ways to split.
    axis: A 0-D `int32` `Tensor`. The dimension along which to split. Must be in
      range [-rank, rank), where rank is the number of dimensions in the input
      `SparseTensor`.
    name: A name for the operation (optional).

  Returns:
    `num_split` `SparseTensor` objects resulting from splitting `value`.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def sparse_slice(sp_input, start, size, name: Incomplete | None = None):
    """Slice a `SparseTensor` based on the `start` and `size`.

  For example, if the input is

      input_tensor = shape = [2, 7]
      [    a   d e  ]
      [b c          ]

  Graphically the output tensors are:

      sparse.slice([0, 0], [2, 4]) = shape = [2, 4]
      [    a  ]
      [b c    ]

      sparse.slice([0, 4], [2, 3]) = shape = [2, 3]
      [ d e  ]
      [      ]

  Args:
    sp_input: The `SparseTensor` to split.
    start: 1-D. tensor represents the start of the slice.
    size: 1-D. tensor represents the size of the slice.
    name: A name for the operation (optional).

  Returns:
    A `SparseTensor` objects resulting from splicing.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def sparse_to_dense(sparse_indices, output_shape, sparse_values, default_value: int = 0, validate_indices: bool = True, name: Incomplete | None = None):
    """Converts a sparse representation into a dense tensor.

  Builds an array `dense` with shape `output_shape` such that

  ```python
  # If sparse_indices is scalar
  dense[i] = (i == sparse_indices ? sparse_values : default_value)

  # If sparse_indices is a vector, then for each i
  dense[sparse_indices[i]] = sparse_values[i]

  # If sparse_indices is an n by d matrix, then for each i in [0, n)
  dense[sparse_indices[i][0], ..., sparse_indices[i][d-1]] = sparse_values[i]
  ```

  All other values in `dense` are set to `default_value`.  If `sparse_values`
  is a scalar, all sparse indices are set to this single value.

  Indices should be sorted in lexicographic order, and indices must not
  contain any repeats. If `validate_indices` is True, these properties
  are checked during execution.

  Args:
    sparse_indices: A 0-D, 1-D, or 2-D `Tensor` of type `int32` or `int64`.
      `sparse_indices[i]` contains the complete index where `sparse_values[i]`
      will be placed.
    output_shape: A 1-D `Tensor` of the same type as `sparse_indices`.  Shape
      of the dense output tensor.
    sparse_values: A 0-D or 1-D `Tensor`.  Values corresponding to each row of
      `sparse_indices`, or a scalar value to be used for all sparse indices.
    default_value: A 0-D `Tensor` of the same type as `sparse_values`.  Value
      to set for indices not specified in `sparse_indices`.  Defaults to zero.
    validate_indices: A boolean value.  If True, indices are checked to make
      sure they are sorted in lexicographic order and that there are no repeats.
    name: A name for the operation (optional).

  Returns:
    Dense `Tensor` of shape `output_shape`.  Has the same type as
    `sparse_values`.
  """
def sparse_reduce_max_v2(sp_input, axis: Incomplete | None = None, keepdims: Incomplete | None = None, output_is_sparse: bool = False, name: Incomplete | None = None):
    """Computes `tf.sparse.maximum` of elements across dimensions of a SparseTensor.

  This is the reduction operation for the elementwise `tf.sparse.maximum` op.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_max()`.  In particular, this Op also returns a dense `Tensor`
  if `output_is_sparse` is `False`, or a `SparseTensor` if `output_is_sparse`
  is `True`.

  Note: A gradient is not defined for this function, so it can't be used
  in training models that need gradient descent.

  Reduces `sp_input` along the dimensions given in `axis`.  Unless
  `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
  `axis`. If `keepdims` is true, the reduced dimensions are retained
  with length 1.

  If `axis` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  similar to the indexing rules in Python.

  The values not defined in `sp_input` don't participate in the reduce max,
  as opposed to be implicitly assumed 0 -- hence it can return negative values
  for sparse `axis`. But, in case there are no values in
  `axis`, it will reduce to 0. See second example below.

  For example:

    # 'x' represents [[1, ?, 2]
    #                 [?, 3, ?]]
    # where ? is implicitly-zero.

    >>> x = tf.sparse.SparseTensor([[0, 0], [0, 2], [1, 1]], [1, 2, 3], [2, 3])
    >>> tf.sparse.reduce_max(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=3>
    >>> tf.sparse.reduce_max(x, 0)
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 3, 2], dtype=int32)>
    >>> tf.sparse.reduce_max(x, 1)
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 3], dtype=int32)>
    >>> tf.sparse.reduce_max(x, 1, keepdims=True)
    <tf.Tensor: shape=(2, 1), dtype=int32, numpy=
    array([[2],
           [3]], dtype=int32)>
    >>> tf.sparse.reduce_max(x, [0, 1])
    <tf.Tensor: shape=(), dtype=int32, numpy=3>

    # 'y' represents [[-7, ?]
    #                 [ 4, 3]
    #                 [ ?, ?]

    >>> y = tf.sparse.SparseTensor([[0, 0,], [1, 0], [1, 1]], [-7, 4, 3],
    ... [3, 2])
    >>> tf.sparse.reduce_max(y, 1)
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([-7,  4,  0], dtype=int32)>

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    output_is_sparse: If true, returns a `SparseTensor` instead of a dense
      `Tensor` (the default).
    name: A name for the operation (optional).

  Returns:
    The reduced Tensor or the reduced SparseTensor if `output_is_sparse` is
    True.
  """
def sparse_reduce_max(sp_input, axis: Incomplete | None = None, keepdims: Incomplete | None = None, reduction_axes: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes `tf.sparse.maximum` of elements across dimensions of a SparseTensor.

  This is the reduction operation for the elementwise `tf.sparse.maximum` op.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_max()`.  In particular, this Op also returns a dense `Tensor`
  instead of a sparse one.

  Note: A gradient is not defined for this function, so it can't be used
  in training models that need gradient descent.

  Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
  `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
  `reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
  with length 1.

  If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  similar to the indexing rules in Python.

  The values not defined in `sp_input` don't participate in the reduce max,
  as opposed to be implicitly assumed 0 -- hence it can return negative values
  for sparse `reduction_axes`. But, in case there are no values in
  `reduction_axes`, it will reduce to 0. See second example below.

  For example:

    # 'x' represents [[1, ?, 2]
    #                 [?, 3, ?]]
    # where ? is implicitly-zero.

    >>> x = tf.sparse.SparseTensor([[0, 0], [0, 2], [1, 1]], [1, 2, 3], [2, 3])
    >>> tf.sparse.reduce_max(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=3>
    >>> tf.sparse.reduce_max(x, 0)
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 3, 2], dtype=int32)>
    >>> tf.sparse.reduce_max(x, 1)
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 3], dtype=int32)>
    >>> tf.sparse.reduce_max(x, 1, keepdims=True)
    <tf.Tensor: shape=(2, 1), dtype=int32, numpy=
    array([[2],
           [3]], dtype=int32)>
    >>> tf.sparse.reduce_max(x, [0, 1])
    <tf.Tensor: shape=(), dtype=int32, numpy=3>

    # 'y' represents [[-7, ?]
    #                 [ 4, 3]
    #                 [ ?, ?]

    >>> y = tf.sparse.SparseTensor([[0, 0,], [1, 0], [1, 1]], [-7, 4, 3],
    ... [3, 2])
    >>> tf.sparse.reduce_max(y, 1)
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([-7,  4,  0], dtype=int32)>

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    reduction_axes: Deprecated name of `axis`.
    keep_dims:  Deprecated alias for `keepdims`.

  Returns:
    The reduced Tensor.
  """
def sparse_reduce_max_sparse(sp_input, axis: Incomplete | None = None, keepdims: Incomplete | None = None, reduction_axes: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes the max of elements across dimensions of a SparseTensor.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_max()`.  In contrast to SparseReduceSum, this Op returns a
  SparseTensor.

  Note: A gradient is not defined for this function, so it can't be used
  in training models that need gradient descent.

  Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
  `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
  `reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
  with length 1.

  If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  which are interpreted according to the indexing rules in Python.

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    reduction_axes: Deprecated name of axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced SparseTensor.
  """
def sparse_reduce_sum_v2(sp_input, axis: Incomplete | None = None, keepdims: Incomplete | None = None, output_is_sparse: bool = False, name: Incomplete | None = None):
    """Computes `tf.sparse.add` of elements across dimensions of a SparseTensor.

  This is the reduction operation for the elementwise `tf.sparse.add` op.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_sum()`.  In particular, this Op also returns a dense `Tensor`
  if `output_is_sparse` is `False`, or a `SparseTensor` if `output_is_sparse`
  is `True`.

  Note: if `output_is_sparse` is True, a gradient is not defined for this
  function, so it can't be used in training models that need gradient descent.

  Reduces `sp_input` along the dimensions given in `axis`.  Unless `keepdims` is
  true, the rank of the tensor is reduced by 1 for each entry in `axis`. If
  `keepdims` is true, the reduced dimensions are retained with length 1.

  If `axis` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  similar to the indexing rules in Python.

  For example:

    # 'x' represents [[1, ?, 1]
    #                 [?, 1, ?]]
    # where ? is implicitly-zero.

    >>> x = tf.sparse.SparseTensor([[0, 0], [0, 2], [1, 1]], [1, 1, 1], [2, 3])
    >>> tf.sparse.reduce_sum(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=3>
    >>> tf.sparse.reduce_sum(x, 0)
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 1, 1], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, 1)  # Can also use -1 as the axis
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 1], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, 1, keepdims=True)
    <tf.Tensor: shape=(2, 1), dtype=int32, numpy=
    array([[2],
           [1]], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, [0, 1])
    <tf.Tensor: shape=(), dtype=int32, numpy=3>

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    output_is_sparse: If true, returns a `SparseTensor` instead of a dense
      `Tensor` (the default).
    name: A name for the operation (optional).

  Returns:
    The reduced Tensor or the reduced SparseTensor if `output_is_sparse` is
    True.
  """
def sparse_reduce_sum(sp_input, axis: Incomplete | None = None, keepdims: Incomplete | None = None, reduction_axes: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes `tf.sparse.add` of elements across dimensions of a SparseTensor.

  This is the reduction operation for the elementwise `tf.sparse.add` op.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_sum()`.  In particular, this Op also returns a dense `Tensor`
  instead of a sparse one.

  Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
  `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
  `reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
  with length 1.

  If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  similar to the indexing rules in Python.

  For example:

    # 'x' represents [[1, ?, 1]
    #                 [?, 1, ?]]
    # where ? is implicitly-zero.

    >>> x = tf.sparse.SparseTensor([[0, 0], [0, 2], [1, 1]], [1, 1, 1], [2, 3])
    >>> tf.sparse.reduce_sum(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=3>
    >>> tf.sparse.reduce_sum(x, 0)
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 1, 1], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, 1)  # Can also use -1 as the axis
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 1], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, 1, keepdims=True)
    <tf.Tensor: shape=(2, 1), dtype=int32, numpy=
    array([[2],
           [1]], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, [0, 1])
    <tf.Tensor: shape=(), dtype=int32, numpy=3>

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    reduction_axes: Deprecated name of `axis`.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced Tensor.
  """
def sparse_reduce_sum_sparse(sp_input, axis: Incomplete | None = None, keepdims: Incomplete | None = None, reduction_axes: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes the sum of elements across dimensions of a SparseTensor.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_sum()`.  In contrast to SparseReduceSum, this Op returns a
  SparseTensor.

  Note: A gradient is not defined for this function, so it can't be used
  in training models that need gradient descent.

  Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
  `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
  `reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
  with length 1.

  If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  which are interpreted according to the indexing rules in Python.

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    reduction_axes: Deprecated name of axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced SparseTensor.
  """
def sparse_tensor_to_dense(sp_input, default_value: Incomplete | None = None, validate_indices: bool = True, name: Incomplete | None = None):
    """Converts a `SparseTensor` into a dense tensor.

  For this sparse tensor with three non-empty values:

  >>> sp_input = tf.sparse.SparseTensor(
  ...   dense_shape=[3, 5],
  ...   values=[7, 8, 9],
  ...   indices =[[0, 1],
  ...             [0, 3],
  ...             [2, 0]])

  The output will be a dense `[3, 5]` tensor with values:

  >>> tf.sparse.to_dense(sp_input).numpy()
  array([[0, 7, 0, 8, 0],
         [0, 0, 0, 0, 0],
         [9, 0, 0, 0, 0]], dtype=int32)

  Note: Indices must be without repeats.  This is only tested if
  `validate_indices` is `True`.

  Args:
    sp_input: The input `SparseTensor`.
    default_value: Scalar value to set for indices not specified in
      `sp_input`.  Defaults to zero.
    validate_indices: A boolean value.  If `True`, indices are checked to make
      sure they are sorted in lexicographic order and that there are no repeats.
    name: A name prefix for the returned tensors (optional).

  Returns:
    A dense tensor with shape `sp_input.dense_shape` and values specified by
    the non-empty values in `sp_input`. Indices not in `sp_input` are assigned
    `default_value`.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def sparse_to_indicator(sp_input, vocab_size, name: Incomplete | None = None):
    """Converts a `SparseTensor` of ids into a dense bool indicator tensor.

  The last dimension of `sp_input.indices` is discarded and replaced with
  the values of `sp_input`.  If `sp_input.dense_shape = [D0, D1, ..., Dn, K]`,
  then `output.shape = [D0, D1, ..., Dn, vocab_size]`, where

      output[d_0, d_1, ..., d_n, sp_input[d_0, d_1, ..., d_n, k]] = True

  and False elsewhere in `output`.

  For example, if `sp_input.dense_shape = [2, 3, 4]` with non-empty values:

      [0, 0, 0]: 0
      [0, 1, 0]: 10
      [1, 0, 3]: 103
      [1, 1, 1]: 150
      [1, 1, 2]: 149
      [1, 1, 3]: 150
      [1, 2, 1]: 121

  and `vocab_size = 200`, then the output will be a `[2, 3, 200]` dense bool
  tensor with False everywhere except at positions

      (0, 0, 0), (0, 1, 10), (1, 0, 103), (1, 1, 149), (1, 1, 150),
      (1, 2, 121).

  Note that repeats are allowed in the input SparseTensor.
  This op is useful for converting `SparseTensor`s into dense formats for
  compatibility with ops that expect dense tensors.

  The input `SparseTensor` must be in row-major order.

  Args:
    sp_input: A `SparseTensor` with `values` property of type `int32` or
      `int64`.
    vocab_size: A scalar int64 Tensor (or Python int) containing the new size
      of the last dimension, `all(0 <= sp_input.values < vocab_size)`.
    name: A name prefix for the returned tensors (optional)

  Returns:
    A dense bool indicator tensor representing the indices with specified value.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def sparse_merge(sp_ids, sp_values, vocab_size, name: Incomplete | None = None, already_sorted: bool = False):
    '''Combines a batch of feature ids and values into a single `SparseTensor`.

  The most common use case for this function occurs when feature ids and
  their corresponding values are stored in `Example` protos on disk.
  `parse_example` will return a batch of ids and a batch of values, and this
  function joins them into a single logical `SparseTensor` for use in
  functions such as `sparse_tensor_dense_matmul`, `sparse_to_dense`, etc.

  The `SparseTensor` returned by this function has the following properties:

    - `indices` is equivalent to `sp_ids.indices` with the last
      dimension discarded and replaced with `sp_ids.values`.
    - `values` is simply `sp_values.values`.
    - If `sp_ids.dense_shape = [D0, D1, ..., Dn, K]`, then
      `output.shape = [D0, D1, ..., Dn, vocab_size]`.

  For example, consider the following feature vectors:

  ```python
    vector1 = [-3, 0, 0, 0, 0, 0]
    vector2 = [ 0, 1, 0, 4, 1, 0]
    vector3 = [ 5, 0, 0, 9, 0, 0]
  ```

  These might be stored sparsely in the following Example protos by storing
  only the feature ids (column number if the vectors are treated as a matrix)
  of the non-zero elements and the corresponding values:

  ```python
    examples = [Example(features={
                    "ids": Feature(int64_list=Int64List(value=[0])),
                    "values": Feature(float_list=FloatList(value=[-3]))}),
                Example(features={
                    "ids": Feature(int64_list=Int64List(value=[1, 4, 3])),
                    "values": Feature(float_list=FloatList(value=[1, 1, 4]))}),
                Example(features={
                    "ids": Feature(int64_list=Int64List(value=[0, 3])),
                    "values": Feature(float_list=FloatList(value=[5, 9]))})]
  ```

  The result of calling parse_example on these examples will produce a
  dictionary with entries for "ids" and "values". Passing those two objects
  to this function along with vocab_size=6, will produce a `SparseTensor` that
  sparsely represents all three instances. Namely, the `indices` property will
  contain the coordinates of the non-zero entries in the feature matrix (the
  first dimension is the row number in the matrix, i.e., the index within the
  batch, and the second dimension is the column number, i.e., the feature id);
  `values` will contain the actual values. `shape` will be the shape of the
  original matrix, i.e., (3, 6). For our example above, the output will be
  equal to:

  ```python
    SparseTensor(indices=[[0, 0], [1, 1], [1, 3], [1, 4], [2, 0], [2, 3]],
                 values=[-3, 1, 4, 1, 5, 9],
                 dense_shape=[3, 6])
  ```

  This method generalizes to higher-dimensions by simply providing a list for
  both the sp_ids as well as the vocab_size.
  In this case the resulting `SparseTensor` has the following properties:
    - `indices` is equivalent to `sp_ids[0].indices` with the last
      dimension discarded and concatenated with
      `sp_ids[0].values, sp_ids[1].values, ...`.
    - `values` is simply `sp_values.values`.
    - If `sp_ids.dense_shape = [D0, D1, ..., Dn, K]`, then
      `output.shape = [D0, D1, ..., Dn] + vocab_size`.

  Args:
    sp_ids: A single `SparseTensor` with `values` property of type `int32`
      or `int64` or a Python list of such `SparseTensor`s or a list thereof.
    sp_values: A `SparseTensor` of any type.
    vocab_size: A scalar `int64` Tensor (or Python int) containing the new size
      of the last dimension, `all(0 <= sp_ids.values < vocab_size)`.
      Or a list thereof with `all(0 <= sp_ids[i].values < vocab_size[i])` for
      all `i`.
    name: A name prefix for the returned tensors (optional)
    already_sorted: A boolean to specify whether the per-batch values in
     `sp_values` are already sorted. If so skip sorting, False by default
     (optional).

  Returns:
    A `SparseTensor` compactly representing a batch of feature ids and values,
    useful for passing to functions that expect such a `SparseTensor`.

  Raises:
    TypeError: If `sp_values` is not a `SparseTensor`. Or if `sp_ids` is neither
      a `SparseTensor` nor a list thereof. Or if `vocab_size` is not a
      `Tensor` or a Python int and `sp_ids` is a `SparseTensor`. Or if
      `vocab_size` is not a or list thereof and `sp_ids` is a list.
    ValueError: If `sp_ids` and `vocab_size` are lists of different lengths.
  '''
def sparse_merge_impl(sp_ids, sp_values, vocab_size, name: Incomplete | None = None, already_sorted: bool = False):
    """Internal implementation for sparse_merge to avoid deprecation warnings."""
def sparse_retain(sp_input, to_retain):
    """Retains specified non-empty values within a `SparseTensor`.

  For example, if `sp_input` has shape `[4, 5]` and 4 non-empty string values:

      [0, 1]: a
      [0, 3]: b
      [2, 0]: c
      [3, 1]: d

  and `to_retain = [True, False, False, True]`, then the output will
  be a `SparseTensor` of shape `[4, 5]` with 2 non-empty values:

      [0, 1]: a
      [3, 1]: d

  Args:
    sp_input: The input `SparseTensor` with `N` non-empty elements.
    to_retain: A bool vector of length `N` with `M` true values.

  Returns:
    A `SparseTensor` with the same shape as the input and `M` non-empty
    elements corresponding to the true positions in `to_retain`.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def sparse_reset_shape(sp_input, new_shape: Incomplete | None = None):
    """Resets the shape of a `SparseTensor` with indices and values unchanged.

  If `new_shape` is None, returns a copy of `sp_input` with its shape reset
  to the tight bounding box of `sp_input`. This will be a shape consisting of
  all zeros if sp_input has no values.

  If `new_shape` is provided, then it must be larger or equal in all dimensions
  compared to the shape of `sp_input`. When this condition is met, the returned
  SparseTensor will have its shape reset to `new_shape` and its indices and
  values unchanged from that of `sp_input.`

  For example:

    Consider a `sp_input` with shape [2, 3, 5]:

      [0, 0, 1]: a
      [0, 1, 0]: b
      [0, 2, 2]: c
      [1, 0, 3]: d

    - It is an error to set `new_shape` as [3, 7] since this represents a
      rank-2 tensor while `sp_input` is rank-3. This is either a ValueError
      during graph construction (if both shapes are known) or an OpError during
      run time.

    - Setting `new_shape` as [2, 3, 6] will be fine as this shape is larger or
      equal in every dimension compared to the original shape [2, 3, 5].

    - On the other hand, setting new_shape as [2, 3, 4] is also an error: The
      third dimension is smaller than the original shape [2, 3, 5] (and an
      `InvalidArgumentError` will be raised).

    - If `new_shape` is None, the returned SparseTensor will have a shape
      [2, 3, 4], which is the tight bounding box of `sp_input`.

  Args:
    sp_input: The input `SparseTensor`.
    new_shape: None or a vector representing the new shape for the returned
      `SparseTensor`.

  Returns:
    A `SparseTensor` indices and values unchanged from `sp_input`. Its shape is
      `new_shape` if that is set. Otherwise it is the tight bounding box of
       `sp_input`

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
    ValueError: If `new_shape` represents a tensor with a different rank from
      that of `sp_input` (if shapes are known when graph is constructed).
    ValueError:  If `new_shape` is determined during graph build to have
      dimension sizes that are too small.
    OpError:
      - If `new_shape` has dimension sizes that are too small.
      - If shapes are not known during graph construction time, and during run
        time it is found out that the ranks do not match.
  """
def sparse_fill_empty_rows(sp_input, default_value, name: Incomplete | None = None):
    """Fills empty rows in the input 2-D `SparseTensor` with a default value.

  This op adds entries with the specified `default_value` at index
  `[row, 0]` for any row in the input that does not already have a value.

  For example, suppose `sp_input` has shape `[5, 6]` and non-empty values:

      [0, 1]: a
      [0, 3]: b
      [2, 0]: c
      [3, 1]: d

  Rows 1 and 4 are empty, so the output will be of shape `[5, 6]` with values:

      [0, 1]: a
      [0, 3]: b
      [1, 0]: default_value
      [2, 0]: c
      [3, 1]: d
      [4, 0]: default_value

  Note that the input may have empty columns at the end, with no effect on
  this op.

  The output `SparseTensor` will be in row-major order and will have the
  same shape as the input.

  This op also returns an indicator vector such that

      empty_row_indicator[i] = True iff row i was an empty row.

  Args:
    sp_input: A `SparseTensor` with shape `[N, M]`.
    default_value: The value to fill for empty rows, with the same type as
      `sp_input.`
    name: A name prefix for the returned tensors (optional)

  Returns:
    sp_ordered_output: A `SparseTensor` with shape `[N, M]`, and with all empty
      rows filled in with `default_value`.
    empty_row_indicator: A bool vector of length `N` indicating whether each
      input row was empty.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def serialize_sparse(sp_input, name: Incomplete | None = None, out_type=...):
    """Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

  Args:
    sp_input: The input `SparseTensor`.
    name: A name prefix for the returned tensors (optional).
    out_type: The `dtype` to use for serialization.

  Returns:
    A 3-vector (1-D `Tensor`), with each column representing the serialized
    `SparseTensor`'s indices, values, and shape (respectively).

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def serialize_sparse_v2(sp_input, out_type=..., name: Incomplete | None = None):
    """Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

  Args:
    sp_input: The input `SparseTensor`.
    out_type: The `dtype` to use for serialization.
    name: A name prefix for the returned tensors (optional).

  Returns:
    A 3-vector (1-D `Tensor`), with each column representing the serialized
    `SparseTensor`'s indices, values, and shape (respectively).

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def serialize_many_sparse(sp_input, name: Incomplete | None = None, out_type=...):
    """Serialize `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

  The `SparseTensor` must have rank `R` greater than 1, and the first dimension
  is treated as the minibatch dimension.  Elements of the `SparseTensor`
  must be sorted in increasing order of this first dimension.  The serialized
  `SparseTensor` objects going into each row of the output `Tensor` will have
  rank `R-1`.

  The minibatch size `N` is extracted from `sparse_shape[0]`.

  Args:
    sp_input: The input rank `R` `SparseTensor`.
    name: A name prefix for the returned tensors (optional).
    out_type: The `dtype` to use for serialization.

  Returns:
    A matrix (2-D `Tensor`) with `N` rows and `3` columns. Each column
    represents serialized `SparseTensor`'s indices, values, and shape
    (respectively).

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def serialize_many_sparse_v2(sp_input, out_type=..., name: Incomplete | None = None):
    """Serialize `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

  The `SparseTensor` must have rank `R` greater than 1, and the first dimension
  is treated as the minibatch dimension.  Elements of the `SparseTensor`
  must be sorted in increasing order of this first dimension.  The serialized
  `SparseTensor` objects going into each row of the output `Tensor` will have
  rank `R-1`.

  The minibatch size `N` is extracted from `sparse_shape[0]`.

  Args:
    sp_input: The input rank `R` `SparseTensor`.
    out_type: The `dtype` to use for serialization.
    name: A name prefix for the returned tensors (optional).

  Returns:
    A matrix (2-D `Tensor`) with `N` rows and `3` columns. Each column
    represents serialized `SparseTensor`'s indices, values, and shape
    (respectively).

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def deserialize_sparse(serialized_sparse, dtype, rank: Incomplete | None = None, name: Incomplete | None = None):
    """Deserialize `SparseTensor` objects.

  The input `serialized_sparse` must have the shape `[?, ?, ..., ?, 3]` where
  the last dimension stores serialized `SparseTensor` objects and the other N
  dimensions (N >= 0) correspond to a batch. The ranks of the original
  `SparseTensor` objects must all match. When the final `SparseTensor` is
  created, its rank is the rank of the incoming `SparseTensor` objects plus N;
  the sparse tensors have been concatenated along new dimensions, one for each
  batch.

  The output `SparseTensor` object's shape values for the original dimensions
  are the max across the input `SparseTensor` objects' shape values for the
  corresponding dimensions. The new dimensions match the size of the batch.

  The input `SparseTensor` objects' indices are assumed ordered in
  standard lexicographic order.  If this is not the case, after this
  step run `SparseReorder` to restore index ordering.

  For example, if the serialized input is a `[2 x 3]` matrix representing two
  original `SparseTensor` objects:

      index = [ 0]
              [10]
              [20]
      values = [1, 2, 3]
      shape = [50]

  and

      index = [ 2]
              [10]
      values = [4, 5]
      shape = [30]

  then the final deserialized `SparseTensor` will be:

      index = [0  0]
              [0 10]
              [0 20]
              [1  2]
              [1 10]
      values = [1, 2, 3, 4, 5]
      shape = [2 50]

  Args:
    serialized_sparse: The serialized `SparseTensor` objects.
      The last dimension must have 3 columns.
    dtype: The `dtype` of the serialized `SparseTensor` objects.
    rank: (optional) Python int, the rank of the `SparseTensor` objects.
    name: A name prefix for the returned tensors (optional).

  Returns:
    A `SparseTensor` representing the deserialized `SparseTensor` objects.

  """
def deserialize_many_sparse(serialized_sparse, dtype, rank: Incomplete | None = None, name: Incomplete | None = None):
    """Deserialize and concatenate `SparseTensors` from a serialized minibatch.

  The input `serialized_sparse` must be a string matrix of shape `[N x 3]` where
  `N` is the minibatch size and the rows correspond to packed outputs of
  `serialize_sparse`.  The ranks of the original `SparseTensor` objects
  must all match.  When the final `SparseTensor` is created, it has rank one
  higher than the ranks of the incoming `SparseTensor` objects (they have been
  concatenated along a new row dimension).

  The output `SparseTensor` object's shape values for all dimensions but the
  first are the max across the input `SparseTensor` objects' shape values
  for the corresponding dimensions.  Its first shape value is `N`, the minibatch
  size.

  The input `SparseTensor` objects' indices are assumed ordered in
  standard lexicographic order.  If this is not the case, after this
  step run `sparse.reorder` to restore index ordering.

  For example, if the serialized input is a `[2, 3]` matrix representing two
  original `SparseTensor` objects:

      index = [ 0]
              [10]
              [20]
      values = [1, 2, 3]
      shape = [50]

  and

      index = [ 2]
              [10]
      values = [4, 5]
      shape = [30]

  then the final deserialized `SparseTensor` will be:

      index = [0  0]
              [0 10]
              [0 20]
              [1  2]
              [1 10]
      values = [1, 2, 3, 4, 5]
      shape = [2 50]

  Args:
    serialized_sparse: 2-D `Tensor` of type `string` of shape `[N, 3]`.
      The serialized and packed `SparseTensor` objects.
    dtype: The `dtype` of the serialized `SparseTensor` objects.
    rank: (optional) Python int, the rank of the `SparseTensor` objects.
    name: A name prefix for the returned tensors (optional)

  Returns:
    A `SparseTensor` representing the deserialized `SparseTensor`s,
    concatenated along the `SparseTensor`s' first dimension.

    All of the serialized `SparseTensor`s must have had the same rank and type.
  """
def sparse_tensor_dense_matmul(sp_a, b, adjoint_a: bool = False, adjoint_b: bool = False, name: Incomplete | None = None):
    '''Multiply SparseTensor (or dense Matrix) (of rank 2) "A" by dense matrix

  (or SparseTensor) "B". Please note that one and only one of the inputs MUST
  be a SparseTensor and the other MUST be a dense matrix.

  The following input format is recommended (but not required) for optimal
  performance:

  * If `adjoint_a == false`: `A` should be sorted in lexicographically
    increasing order.  Use `sparse.reorder` if you\'re not sure.
  * If `adjoint_a == true`: `A` should be sorted in order of increasing
    dimension 1 (i.e., "column major" order instead of "row major" order).

  Args:
    sp_a: SparseTensor (or dense Matrix) A, of rank 2.
    b: dense Matrix (or SparseTensor) B, with the same dtype as sp_a.
    adjoint_a: Use the adjoint of A in the matrix multiply.  If A is complex,
      this is transpose(conj(A)).  Otherwise it\'s transpose(A).
    adjoint_b: Use the adjoint of B in the matrix multiply.  If B is complex,
      this is transpose(conj(B)).  Otherwise it\'s transpose(B).
    name: A name prefix for the returned tensors (optional)

  Returns:
    A dense matrix (pseudo-code in dense np.matrix notation):
      `A = A.H if adjoint_a else A`
      `B = B.H if adjoint_b else B`
      `return A*B`

  Notes:

  Using `tf.nn.embedding_lookup_sparse` for sparse multiplication:

  It\'s not obvious but you can consider `embedding_lookup_sparse` as another
  sparse and dense multiplication. In some situations, you may prefer to use
  `embedding_lookup_sparse` even though you\'re not dealing with embeddings.

  There are two questions to ask in the decision process: Do you need gradients
  computed as sparse too? Is your sparse data represented as two
  `SparseTensor`s: ids and values? There is more explanation about data format
  below. If you answer any of these questions as yes, consider using
  `tf.nn.embedding_lookup_sparse`.

  Following explains differences between the expected SparseTensors:
  For example if dense form of your sparse data has shape `[3, 5]` and values:

      [[  a      ]
       [b       c]
       [    d    ]]


  `SparseTensor` format expected by `sparse_tensor_dense_matmul`:
   `sp_a` (indices, values):

      [0, 1]: a
      [1, 0]: b
      [1, 4]: c
      [2, 2]: d

  `SparseTensor` format expected by `embedding_lookup_sparse`:
   `sp_ids`                 `sp_weights`

      [0, 0]: 1                [0, 0]: a
      [1, 0]: 0                [1, 0]: b
      [1, 1]: 4                [1, 1]: c
      [2, 0]: 2                [2, 0]: d


  Deciding when to use `sparse_tensor_dense_matmul` vs.
  `matmul`(a_is_sparse=True):

  There are a number of questions to ask in the decision process, including:

  * Will the SparseTensor `A` fit in memory if densified?
  * Is the column count of the product large (>> 1)?
  * Is the density of `A` larger than approximately 15%?

  If the answer to several of these questions is yes, consider
  converting the `SparseTensor` to a dense one and using `tf.matmul` with
  `a_is_sparse=True`.

  This operation tends to perform well when `A` is more sparse, if the column
  size of the product is small (e.g. matrix-vector multiplication), if
  `sp_a.dense_shape` takes on large values.

  Below is a rough speed comparison between `sparse_tensor_dense_matmul`,
  labeled \'sparse\', and `matmul`(a_is_sparse=True), labeled \'dense\'.  For
  purposes of the comparison, the time spent converting from a `SparseTensor` to
  a dense `Tensor` is not included, so it is overly conservative with respect to
  the time ratio.

  Benchmark system:
  CPU: Intel Ivybridge with HyperThreading (6 cores) dL1:32KB dL2:256KB dL3:12MB
  GPU: NVidia Tesla k40c

  Compiled with:
  `-c opt --config=cuda --copt=-mavx`

  ```
  tensorflow/python/sparse_tensor_dense_matmul_op_test --benchmarks
  A sparse [m, k] with % nonzero values between 1% and 80%
  B dense [k, n]

  % nnz  n   gpu   m     k     dt(dense)     dt(sparse)   dt(sparse)/dt(dense)
  0.01   1   True  100   100   0.000221166   0.00010154   0.459112
  0.01   1   True  100   1000  0.00033858    0.000109275  0.322745
  0.01   1   True  1000  100   0.000310557   9.85661e-05  0.317385
  0.01   1   True  1000  1000  0.0008721     0.000100875  0.115669
  0.01   1   False 100   100   0.000208085   0.000107603  0.51711
  0.01   1   False 100   1000  0.000327112   9.51118e-05  0.290762
  0.01   1   False 1000  100   0.000308222   0.00010345   0.335635
  0.01   1   False 1000  1000  0.000865721   0.000101397  0.117124
  0.01   10  True  100   100   0.000218522   0.000105537  0.482958
  0.01   10  True  100   1000  0.000340882   0.000111641  0.327506
  0.01   10  True  1000  100   0.000315472   0.000117376  0.372064
  0.01   10  True  1000  1000  0.000905493   0.000123263  0.136128
  0.01   10  False 100   100   0.000221529   9.82571e-05  0.44354
  0.01   10  False 100   1000  0.000330552   0.000112615  0.340687
  0.01   10  False 1000  100   0.000341277   0.000114097  0.334324
  0.01   10  False 1000  1000  0.000819944   0.000120982  0.147549
  0.01   25  True  100   100   0.000207806   0.000105977  0.509981
  0.01   25  True  100   1000  0.000322879   0.00012921   0.400181
  0.01   25  True  1000  100   0.00038262    0.00014158   0.370035
  0.01   25  True  1000  1000  0.000865438   0.000202083  0.233504
  0.01   25  False 100   100   0.000209401   0.000104696  0.499979
  0.01   25  False 100   1000  0.000321161   0.000130737  0.407076
  0.01   25  False 1000  100   0.000377012   0.000136801  0.362856
  0.01   25  False 1000  1000  0.000861125   0.00020272   0.235413
  0.2    1   True  100   100   0.000206952   9.69219e-05  0.46833
  0.2    1   True  100   1000  0.000348674   0.000147475  0.422959
  0.2    1   True  1000  100   0.000336908   0.00010122   0.300439
  0.2    1   True  1000  1000  0.001022      0.000203274  0.198898
  0.2    1   False 100   100   0.000207532   9.5412e-05   0.459746
  0.2    1   False 100   1000  0.000356127   0.000146824  0.41228
  0.2    1   False 1000  100   0.000322664   0.000100918  0.312764
  0.2    1   False 1000  1000  0.000998987   0.000203442  0.203648
  0.2    10  True  100   100   0.000211692   0.000109903  0.519165
  0.2    10  True  100   1000  0.000372819   0.000164321  0.440753
  0.2    10  True  1000  100   0.000338651   0.000144806  0.427596
  0.2    10  True  1000  1000  0.00108312    0.000758876  0.70064
  0.2    10  False 100   100   0.000215727   0.000110502  0.512231
  0.2    10  False 100   1000  0.000375419   0.0001613    0.429653
  0.2    10  False 1000  100   0.000336999   0.000145628  0.432132
  0.2    10  False 1000  1000  0.00110502    0.000762043  0.689618
  0.2    25  True  100   100   0.000218705   0.000129913  0.594009
  0.2    25  True  100   1000  0.000394794   0.00029428   0.745402
  0.2    25  True  1000  100   0.000404483   0.0002693    0.665788
  0.2    25  True  1000  1000  0.0012002     0.00194494   1.62052
  0.2    25  False 100   100   0.000221494   0.0001306    0.589632
  0.2    25  False 100   1000  0.000396436   0.000297204  0.74969
  0.2    25  False 1000  100   0.000409346   0.000270068  0.659754
  0.2    25  False 1000  1000  0.00121051    0.00193737   1.60046
  0.5    1   True  100   100   0.000214981   9.82111e-05  0.456836
  0.5    1   True  100   1000  0.000415328   0.000223073  0.537101
  0.5    1   True  1000  100   0.000358324   0.00011269   0.314492
  0.5    1   True  1000  1000  0.00137612    0.000437401  0.317851
  0.5    1   False 100   100   0.000224196   0.000101423  0.452386
  0.5    1   False 100   1000  0.000400987   0.000223286  0.556841
  0.5    1   False 1000  100   0.000368825   0.00011224   0.304318
  0.5    1   False 1000  1000  0.00136036    0.000429369  0.31563
  0.5    10  True  100   100   0.000222125   0.000112308  0.505608
  0.5    10  True  100   1000  0.000461088   0.00032357   0.701753
  0.5    10  True  1000  100   0.000394624   0.000225497  0.571422
  0.5    10  True  1000  1000  0.00158027    0.00190898   1.20801
  0.5    10  False 100   100   0.000232083   0.000114978  0.495418
  0.5    10  False 100   1000  0.000454574   0.000324632  0.714146
  0.5    10  False 1000  100   0.000379097   0.000227768  0.600817
  0.5    10  False 1000  1000  0.00160292    0.00190168   1.18638
  0.5    25  True  100   100   0.00023429    0.000151703  0.647501
  0.5    25  True  100   1000  0.000497462   0.000598873  1.20386
  0.5    25  True  1000  100   0.000460778   0.000557038  1.20891
  0.5    25  True  1000  1000  0.00170036    0.00467336   2.74845
  0.5    25  False 100   100   0.000228981   0.000155334  0.678371
  0.5    25  False 100   1000  0.000496139   0.000620789  1.25124
  0.5    25  False 1000  100   0.00045473    0.000551528  1.21287
  0.5    25  False 1000  1000  0.00171793    0.00467152   2.71927
  0.8    1   True  100   100   0.000222037   0.000105301  0.47425
  0.8    1   True  100   1000  0.000410804   0.000329327  0.801664
  0.8    1   True  1000  100   0.000349735   0.000131225  0.375212
  0.8    1   True  1000  1000  0.00139219    0.000677065  0.48633
  0.8    1   False 100   100   0.000214079   0.000107486  0.502085
  0.8    1   False 100   1000  0.000413746   0.000323244  0.781261
  0.8    1   False 1000  100   0.000348983   0.000131983  0.378193
  0.8    1   False 1000  1000  0.00136296    0.000685325  0.50282
  0.8    10  True  100   100   0.000229159   0.00011825   0.516017
  0.8    10  True  100   1000  0.000498845   0.000532618  1.0677
  0.8    10  True  1000  100   0.000383126   0.00029935   0.781336
  0.8    10  True  1000  1000  0.00162866    0.00307312   1.88689
  0.8    10  False 100   100   0.000230783   0.000124958  0.541452
  0.8    10  False 100   1000  0.000493393   0.000550654  1.11606
  0.8    10  False 1000  100   0.000377167   0.000298581  0.791642
  0.8    10  False 1000  1000  0.00165795    0.00305103   1.84024
  0.8    25  True  100   100   0.000233496   0.000175241  0.75051
  0.8    25  True  100   1000  0.00055654    0.00102658   1.84458
  0.8    25  True  1000  100   0.000463814   0.000783267  1.68875
  0.8    25  True  1000  1000  0.00186905    0.00755344   4.04132
  0.8    25  False 100   100   0.000240243   0.000175047  0.728625
  0.8    25  False 100   1000  0.000578102   0.00104499   1.80763
  0.8    25  False 1000  100   0.000485113   0.000776849  1.60138
  0.8    25  False 1000  1000  0.00211448    0.00752736   3.55992
  ```

  '''
def sparse_softmax(sp_input, name: Incomplete | None = None):
    """Applies softmax to a batched N-D `SparseTensor`.

  The inputs represent an N-D SparseTensor with logical shape `[..., B, C]`
  (where `N >= 2`), and with indices sorted in the canonical lexicographic
  order.

  This op is equivalent to applying the normal `tf.nn.softmax()` to each
  innermost logical submatrix with shape `[B, C]`, but with the catch that *the
  implicitly zero elements do not participate*.  Specifically, the algorithm is
  equivalent to:

    (1) Applies `tf.nn.softmax()` to a densified view of each innermost
        submatrix with shape `[B, C]`, along the size-C dimension;
    (2) Masks out the original implicitly-zero locations;
    (3) Renormalizes the remaining elements.

  Hence, the `SparseTensor` result has exactly the same non-zero indices and
  shape.

  Example using a 3-D SparseTensor:

    >>> st = tf.sparse.from_dense(
    ...   [[[0., np.e],
    ...     [1., 0.]],
    ...
    ...    [[np.e, 0.],
    ...     [np.e, np.e]]])
    >>> res = tf.sparse.softmax(st)
    >>> res.indices
    <tf.Tensor: shape=(5, 3), dtype=int64, numpy=
    array([[0, 0, 1],
           [0, 1, 0],
           [1, 0, 0],
           [1, 1, 0],
           [1, 1, 1]])>
    >>> res.values
    <tf.Tensor: ... numpy=array([1. , 1. , 1. , 0.5, 0.5], dtype=float32)>
    >>> res.dense_shape
    <tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 2, 2])>
    >>> tf.sparse.to_dense(res)
    <tf.Tensor: shape=(2, 2, 2), dtype=float32, numpy=
    array([[[0. , 1. ],
            [1. , 0. ]],
           [[1. , 0. ],
            [0.5, 0.5]]], dtype=float32)>

  Args:
    sp_input: N-D `SparseTensor`, where `N >= 2`.
    name: optional name of the operation.
  Returns:
    output: N-D `SparseTensor` representing the results.
  """
def sparse_maximum(sp_a, sp_b, name: Incomplete | None = None):
    """Returns the element-wise max of two SparseTensors.

  Assumes the two SparseTensors have the same shape, i.e., no broadcasting.

  Example:

    >>> sp_zero = tf.sparse.SparseTensor([[0]], [0], [7])
    >>> sp_one = tf.sparse.SparseTensor([[1]], [1], [7])
    >>> res = tf.sparse.maximum(sp_zero, sp_one)
    >>> res.indices
    <tf.Tensor: shape=(2, 1), dtype=int64, numpy=
    array([[0],
           [1]])>
    >>> res.values
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 1], dtype=int32)>
    >>> res.dense_shape
    <tf.Tensor: shape=(1,), dtype=int64, numpy=array([7])>

  The reduction version of this elementwise operation is `tf.sparse.reduce_max`

  Args:
    sp_a: a `SparseTensor` operand whose dtype is real, and indices
      lexicographically ordered.
    sp_b: the other `SparseTensor` operand with the same requirements (and the
      same shape).
    name: optional name of the operation.
  Returns:
    output: the output SparseTensor.
  """
def sparse_minimum(sp_a, sp_b, name: Incomplete | None = None):
    """Returns the element-wise min of two SparseTensors.

  Assumes the two SparseTensors have the same shape, i.e., no broadcasting.

  Example:

    >>> sp_zero = tf.sparse.SparseTensor([[0]], [0], [7])
    >>> sp_one = tf.sparse.SparseTensor([[1]], [1], [7])
    >>> res = tf.sparse.minimum(sp_zero, sp_one)
    >>> res.indices
    <tf.Tensor: shape=(2, 1), dtype=int64, numpy=
    array([[0],
           [1]])>
    >>> res.values
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 0], dtype=int32)>
    >>> res.dense_shape
    <tf.Tensor: shape=(1,), dtype=int64, numpy=array([7])>

  Args:
    sp_a: a `SparseTensor` operand whose dtype is real, and indices
      lexicographically ordered.
    sp_b: the other `SparseTensor` operand with the same requirements (and the
      same shape).
    name: optional name of the operation.
  Returns:
    output: the output SparseTensor.
  """
def sparse_transpose(sp_input, perm: Incomplete | None = None, name: Incomplete | None = None):
    """Transposes a `SparseTensor`.

  Permutes the dimensions according to the value of `perm`.  This is the sparse
  version of `tf.transpose`.

  The returned tensor's dimension `i` will correspond to the input dimension
  `perm[i]`. If `perm` is not given, it is set to (n-1...0), where n is the rank
  of the input tensor. Hence, by default, this operation performs a regular
  matrix transpose on 2-D input Tensors.

  For example:

  >>> x = tf.SparseTensor(indices=[[0, 1], [0, 3], [2, 3], [3, 1]],
  ...                     values=[1.1, 2.2, 3.3, 4.4],
  ...                     dense_shape=[4, 5])
  >>> print('x =', tf.sparse.to_dense(x))
  x = tf.Tensor(
  [[0.  1.1 0.  2.2 0. ]
  [0.  0.  0.  0.  0. ]
  [0.  0.  0.  3.3 0. ]
  [0.  4.4 0.  0.  0. ]], shape=(4, 5), dtype=float32)

  >>> x_transpose = tf.sparse.transpose(x)
  >>> print('x_transpose =', tf.sparse.to_dense(x_transpose))
  x_transpose = tf.Tensor(
  [[0.  0.  0.  0. ]
  [1.1 0.  0.  4.4]
  [0.  0.  0.  0. ]
  [2.2 0.  3.3 0. ]
  [0.  0.  0.  0. ]], shape=(5, 4), dtype=float32)

  Equivalently, you could call `tf.sparse.transpose(x, perm=[1, 0])`.  The
  `perm` argument is more useful for n-dimensional tensors where n > 2.

  >>> x = tf.SparseTensor(indices=[[0, 0, 1], [0, 0, 3], [1, 2, 3], [1, 3, 1]],
  ...                     values=[1.1, 2.2, 3.3, 4.4],
  ...                     dense_shape=[2, 4, 5])
  >>> print('x =', tf.sparse.to_dense(x))
  x = tf.Tensor(
  [[[0.  1.1 0.  2.2 0. ]
    [0.  0.  0.  0.  0. ]
    [0.  0.  0.  0.  0. ]
    [0.  0.  0.  0.  0. ]]
  [[0.  0.  0.  0.  0. ]
    [0.  0.  0.  0.  0. ]
    [0.  0.  0.  3.3 0. ]
    [0.  4.4 0.  0.  0. ]]], shape=(2, 4, 5), dtype=float32)

  As above, simply calling `tf.sparse.transpose` will default to `perm=[2,1,0]`.

  To take the transpose of a batch of sparse matrices, where 0 is the batch
  dimension, you would set `perm=[0,2,1]`.

  >>> x_transpose = tf.sparse.transpose(x, perm=[0, 2, 1])
  >>> print('x_transpose =', tf.sparse.to_dense(x_transpose))
  x_transpose = tf.Tensor(
  [[[0.  0.  0.  0. ]
    [1.1 0.  0.  0. ]
    [0.  0.  0.  0. ]
    [2.2 0.  0.  0. ]
    [0.  0.  0.  0. ]]
  [[0.  0.  0.  0. ]
    [0.  0.  0.  4.4]
    [0.  0.  0.  0. ]
    [0.  0.  3.3 0. ]
    [0.  0.  0.  0. ]]], shape=(2, 5, 4), dtype=float32)

  Args:
    sp_input: The input `SparseTensor`.
    perm: A permutation vector of the dimensions of `sp_input`.
    name: A name prefix for the returned tensors (optional).

  Returns:
    A transposed `SparseTensor`.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
def map_values(op, *args, **kwargs):
    """Applies `op` to the `.values` tensor of one or more `SparseTensor`s.

  Replaces any `SparseTensor` in `args` or `kwargs` with its `values`
  tensor (which contains the non-default values for the SparseTensor),
  and then calls `op`.  Returns a `SparseTensor` that is constructed
  from the input `SparseTensor`s' `indices`, `dense_shape`, and the
  value returned by the `op`.

  If the input arguments contain multiple `SparseTensor`s, then they must have
  equal `indices` and dense shapes.

  Examples:

  >>> s = tf.sparse.from_dense([[1, 2, 0],
  ...                           [0, 4, 0],
  ...                           [1, 0, 0]])
  >>> tf.sparse.to_dense(tf.sparse.map_values(tf.ones_like, s)).numpy()
  array([[1, 1, 0],
         [0, 1, 0],
         [1, 0, 0]], dtype=int32)

  >>> tf.sparse.to_dense(tf.sparse.map_values(tf.multiply, s, s)).numpy()
  array([[ 1,  4,  0],
         [ 0, 16,  0],
         [ 1,  0,  0]], dtype=int32)

  >>> tf.sparse.to_dense(tf.sparse.map_values(tf.add, s, 5)).numpy()
  array([[6, 7, 0],
         [0, 9, 0],
         [6, 0, 0]], dtype=int32)

  Note: even though `tf.add(0, 5) != 0`, implicit zeros
  will remain unchanged. However, if the sparse tensor contains any explicit
  zeros, these will be affected by the mapping!

  Args:
    op: The operation that should be applied to the SparseTensor `values`. `op`
      is typically an element-wise operation (such as math_ops.add), but any
      operation that preserves the shape can be used.
    *args: Arguments for `op`.
    **kwargs: Keyword arguments for `op`.

  Returns:
    A `SparseTensor` whose `indices` and `dense_shape` matches the `indices`
    and `dense_shape` of all input `SparseTensor`s.
  Raises:
    ValueError: If args contains no `SparseTensor`, or if the `indices`
      or `dense_shape`s of the input `SparseTensor`s are not equal.
  """

class _UnaryMapValueDispatcher(dispatch.OpDispatcher):
    """OpDispatcher for unary ops that maps base function across sparse values."""
    def __init__(self, original_func) -> None: ...
    def handle(self, args, kwargs): ...
