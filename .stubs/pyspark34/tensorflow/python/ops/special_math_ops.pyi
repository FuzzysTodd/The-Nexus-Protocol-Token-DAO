from _typeshed import Incomplete
from tensorflow.compiler.tf2xla.ops import gen_xla_ops as gen_xla_ops
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_linalg_ops as gen_linalg_ops, gen_special_math_ops as gen_special_math_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def lbeta(x, name: Incomplete | None = None):
    """Computes \\\\(ln(|Beta(x)|)\\\\), reducing along the last dimension.

  Given one-dimensional $z = [z_1,...,z_K]$, we define

  $$Beta(z) = \\frac{\\prod_j \\Gamma(z_j)}{\\Gamma(\\sum_j z_j)},$$

  where $\\Gamma$ is the gamma function.

  And for $n + 1$ dimensional $x$ with shape $[N_1, ..., N_n, K]$, we define

  $$lbeta(x)[i_1, ..., i_n] = \\log{|Beta(x[i_1, ..., i_n, :])|}.$$

  In other words, the last dimension is treated as the $z$ vector.

  Note that if $z = [u, v]$, then

  $$Beta(z) = \\frac{\\Gamma(u)\\Gamma(v)}{\\Gamma(u + v)}
    = \\int_0^1 t^{u-1} (1 - t)^{v-1} \\mathrm{d}t,$$

  which defines the traditional bivariate beta function.

  If the last dimension is empty, we follow the convention that the sum over
  the empty set is zero, and the product is one.

  Args:
    x: A rank `n + 1` `Tensor`, `n >= 0` with type `float`, or `double`.
    name: A name for the operation (optional).

  Returns:
    The logarithm of \\\\(|Beta(x)|\\\\) reducing along the last dimension.
  """
def dawsn(x, name: Incomplete | None = None):
    """Computes Dawson's integral of `x` element-wise.

  Dawson's integral is defined as `exp(-x**2)` times the integral of
  `exp(t**2)` from `0` to `x`, with the domain of definition all real numbers.

  Dawson's function is odd.
  >>> tf.math.special.dawsn([-1., -0.5, 0.5, 1.]).numpy()
  array([-0.5380795, -0.4244364, 0.4244364,  0.5380795], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.dawsn
  @end_compatibility
  """
def expint(x, name: Incomplete | None = None):
    """Computes the Exponential integral of `x` element-wise.

  The Exponential integral is defined as the integral of `exp(t) / t` from
  `-inf` to `x`, with the domain of definition all positive real numbers.

  >>> tf.math.special.expint([1., 1.1, 2.1, 4.1]).numpy()
  array([ 1.8951179,  2.1673784,  5.3332353, 21.048464], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.expi
  @end_compatibility
  """
def fresnel_cos(x, name: Incomplete | None = None):
    """Computes Fresnel's cosine integral of `x` element-wise.

  The Fresnel cosine integral is defined as the integral of `cos(t^2)` from
  `0` to `x`, with the domain of definition all real numbers.

  The Fresnel cosine integral is odd.
  >>> tf.math.special.fresnel_cos([-1., -0.1, 0.1, 1.]).numpy()
  array([-0.7798934 , -0.09999753,  0.09999753,  0.7798934 ], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.fresnel second output.
  @end_compatibility
  """
def fresnel_sin(x, name: Incomplete | None = None):
    """Computes Fresnel's sine integral of `x` element-wise.

  The Fresnel sine integral is defined as the integral of `sin(t^2)` from
  `0` to `x`, with the domain of definition all real numbers.

  >>> tf.math.special.fresnel_sin([-1., -0.1, 0.1, 1.]).numpy()
  array([-0.43825912, -0.00052359,  0.00052359,  0.43825912], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.fresnel first output.
  @end_compatibility
  """
def spence(x, name: Incomplete | None = None):
    """Computes Spence's integral of `x` element-wise.

  Spence's integral is defined as the integral of `log(t) / (1 - t)` from
  `1` to `x`, with the domain of definition all non-negative real numbers.

  >>> tf.math.special.spence([0.5, 1., 2., 3.]).numpy()
  array([ 0.58224034,  0.        , -0.82246685, -1.4367464], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.spence
  @end_compatibility
  """
def bessel_i0(x, name: Incomplete | None = None):
    """Computes the Bessel i0 function of `x` element-wise.

  Modified Bessel function of order 0.

  It is preferable to use the numerically stabler function `i0e(x)` instead.

  >>> tf.math.special.bessel_i0([-1., -0.5, 0.5, 1.]).numpy()
  array([1.26606588, 1.06348337, 1.06348337, 1.26606588], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i0
  @end_compatibility
  """
def bessel_i0e(x, name: Incomplete | None = None):
    """Computes the Bessel i0e function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_i0e([-1., -0.5, 0.5, 1.]).numpy()
  array([0.46575961, 0.64503527, 0.64503527, 0.46575961], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i0e
  @end_compatibility
  """
def bessel_i1(x, name: Incomplete | None = None):
    """Computes the Bessel i1 function of `x` element-wise.

  Modified Bessel function of order 1.

  It is preferable to use the numerically stabler function `i1e(x)` instead.

  >>> tf.math.special.bessel_i1([-1., -0.5, 0.5, 1.]).numpy()
  array([-0.5651591 , -0.25789431,  0.25789431,  0.5651591 ], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i1
  @end_compatibility
  """
def bessel_i1e(x, name: Incomplete | None = None):
    """Computes the Bessel i1e function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_i1e([-1., -0.5, 0.5, 1.]).numpy()
  array([-0.20791042, -0.15642083,  0.15642083,  0.20791042], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i1e
  @end_compatibility
  """
def bessel_k0(x, name: Incomplete | None = None):
    """Computes the Bessel k0 function of `x` element-wise.

  Modified Bessel function of order 0.

  It is preferable to use the numerically stabler function `k0e(x)` instead.

  >>> tf.math.special.bessel_k0([0.5, 1., 2., 4.]).numpy()
  array([0.92441907, 0.42102444, 0.11389387, 0.01115968], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k0
  @end_compatibility
  """
def bessel_k0e(x, name: Incomplete | None = None):
    """Computes the Bessel k0e function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_k0e([0.5, 1., 2., 4.]).numpy()
  array([1.52410939, 1.14446308, 0.84156822, 0.60929767], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k0e
  @end_compatibility
  """
def bessel_k1(x, name: Incomplete | None = None):
    """Computes the Bessel k1 function of `x` element-wise.

  Modified Bessel function of order 1.

  It is preferable to use the numerically stabler function `k1e(x)` instead.

  >>> tf.math.special.bessel_k1([0.5, 1., 2., 4.]).numpy()
  array([1.65644112, 0.60190723, 0.13986588, 0.0124835 ], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k1
  @end_compatibility
  """
def bessel_k1e(x, name: Incomplete | None = None):
    """Computes the Bessel k1e function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_k1e([0.5, 1., 2., 4.]).numpy()
  array([2.73100971, 1.63615349, 1.03347685, 0.68157595], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k1e
  @end_compatibility
  """
def bessel_j0(x, name: Incomplete | None = None):
    """Computes the Bessel j0 function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_j0([0.5, 1., 2., 4.]).numpy()
  array([ 0.93846981,  0.76519769,  0.22389078, -0.39714981], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.j0
  @end_compatibility
  """
def bessel_j1(x, name: Incomplete | None = None):
    """Computes the Bessel j1 function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_j1([0.5, 1., 2., 4.]).numpy()
  array([ 0.24226846,  0.44005059,  0.57672481, -0.06604333], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.j1
  @end_compatibility
  """
def bessel_y0(x, name: Incomplete | None = None):
    """Computes the Bessel y0 function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_y0([0.5, 1., 2., 4.]).numpy()
  array([-0.44451873,  0.08825696,  0.51037567, -0.01694074], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.y0
  @end_compatibility
  """
def bessel_y1(x, name: Incomplete | None = None):
    """Computes the Bessel y1 function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_y1([0.5, 1., 2., 4.]).numpy()
  array([-1.47147239, -0.78121282, -0.10703243,  0.39792571], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.y1
  @end_compatibility
  """
def einsum(equation, *inputs, **kwargs):
    '''Tensor contraction over specified indices and outer product.

  Einsum allows defining Tensors by defining their element-wise computation.
  This computation is defined by `equation`, a shorthand form based on Einstein
  summation. As an example, consider multiplying two matrices A and B to form a
  matrix C.  The elements of C are given by:

  $$ C_{i,k} = \\sum_j A_{i,j} B_{j,k} $$

  or

  ```
  C[i,k] = sum_j A[i,j] * B[j,k]
  ```

  The corresponding einsum `equation` is:

  ```
  ij,jk->ik
  ```

  In general, to convert the element-wise equation into the `equation` string,
  use the following procedure (intermediate strings for matrix multiplication
  example provided in parentheses):

  1. remove variable names, brackets, and commas, (`ik = sum_j ij * jk`)
  2. replace "*" with ",", (`ik = sum_j ij , jk`)
  3. drop summation signs, and (`ik = ij, jk`)
  4. move the output to the right, while replacing "=" with "->". (`ij,jk->ik`)

  Note: If the output indices are not specified repeated indices are summed.
  So `ij,jk->ik` can be simplified to `ij,jk`.

  Many common operations can be expressed in this way.  For example:

  **Matrix multiplication**

  >>> m0 = tf.random.normal(shape=[2, 3])
  >>> m1 = tf.random.normal(shape=[3, 5])
  >>> e = tf.einsum(\'ij,jk->ik\', m0, m1)
  >>> # output[i,k] = sum_j m0[i,j] * m1[j, k]
  >>> print(e.shape)
  (2, 5)

  Repeated indices are summed if the output indices are not specified.

  >>> e = tf.einsum(\'ij,jk\', m0, m1)  # output[i,k] = sum_j m0[i,j] * m1[j, k]
  >>> print(e.shape)
  (2, 5)


  **Dot product**

  >>> u = tf.random.normal(shape=[5])
  >>> v = tf.random.normal(shape=[5])
  >>> e = tf.einsum(\'i,i->\', u, v)  # output = sum_i u[i]*v[i]
  >>> print(e.shape)
  ()

  **Outer product**

  >>> u = tf.random.normal(shape=[3])
  >>> v = tf.random.normal(shape=[5])
  >>> e = tf.einsum(\'i,j->ij\', u, v)  # output[i,j] = u[i]*v[j]
  >>> print(e.shape)
  (3, 5)

  **Transpose**

  >>> m = tf.ones(2,3)
  >>> e = tf.einsum(\'ij->ji\', m0)  # output[j,i] = m0[i,j]
  >>> print(e.shape)
  (3, 2)

  **Diag**

  >>> m = tf.reshape(tf.range(9), [3,3])
  >>> diag = tf.einsum(\'ii->i\', m)
  >>> print(diag.shape)
  (3,)

  **Trace**

  >>> # Repeated indices are summed.
  >>> trace = tf.einsum(\'ii\', m)  # output[j,i] = trace(m) = sum_i m[i, i]
  >>> assert trace == sum(diag)
  >>> print(trace.shape)
  ()

  **Batch matrix multiplication**

  >>> s = tf.random.normal(shape=[7,5,3])
  >>> t = tf.random.normal(shape=[7,3,2])
  >>> e = tf.einsum(\'bij,bjk->bik\', s, t)
  >>> # output[a,i,k] = sum_j s[a,i,j] * t[a, j, k]
  >>> print(e.shape)
  (7, 5, 2)

  This method does not support broadcasting on named-axes. All axes with
  matching labels should have the same length. If you have length-1 axes,
  use `tf.squeeze` or `tf.reshape` to eliminate them.

  To write code that is agnostic to the number of indices in the input
  use an ellipsis. The ellipsis is a placeholder for "whatever other indices
  fit here".

  For example, to perform a NumPy-style broadcasting-batch-matrix multiplication
  where the matrix multiply acts on the last two axes of the input, use:

  >>> s = tf.random.normal(shape=[11, 7, 5, 3])
  >>> t = tf.random.normal(shape=[11, 7, 3, 2])
  >>> e =  tf.einsum(\'...ij,...jk->...ik\', s, t)
  >>> print(e.shape)
  (11, 7, 5, 2)

  Einsum **will** broadcast over axes covered by the ellipsis.

  >>> s = tf.random.normal(shape=[11, 1, 5, 3])
  >>> t = tf.random.normal(shape=[1, 7, 3, 2])
  >>> e =  tf.einsum(\'...ij,...jk->...ik\', s, t)
  >>> print(e.shape)
  (11, 7, 5, 2)

  Args:
    equation: a `str` describing the contraction, in the same format as
      `numpy.einsum`.
    *inputs: the inputs to contract (each one a `Tensor`), whose shapes should
      be consistent with `equation`.
    **kwargs:
      - optimize: Optimization strategy to use to find contraction path using
        opt_einsum. Must be \'greedy\', \'optimal\', \'branch-2\', \'branch-all\' or
          \'auto\'. (optional, default: \'greedy\').
      - name: A name for the operation (optional).

  Returns:
    The contracted `Tensor`, with shape determined by `equation`.

  Raises:
    ValueError: If
      - the format of `equation` is incorrect,
      - number of inputs or their shapes are inconsistent with `equation`.
  '''
