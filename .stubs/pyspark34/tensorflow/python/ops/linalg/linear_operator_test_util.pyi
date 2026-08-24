import abc
from _typeshed import Incomplete
from tensorflow.python.eager import backprop as backprop, context as context, def_function as def_function
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops, random_seed as random_seed, tensor_shape as tensor_shape, tensor_util as tensor_util, test_util as test_util
from tensorflow.python.module import module as module
from tensorflow.python.ops import array_ops as array_ops, linalg_ops as linalg_ops, math_ops as math_ops, random_ops as random_ops, sort_ops as sort_ops, variables as variables, while_v2 as while_v2
from tensorflow.python.ops.linalg import linear_operator_util as linear_operator_util
from tensorflow.python.platform import test as test
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import nest as nest

class OperatorShapesInfo:
    """Object encoding expected shape for a test.

  Encodes the expected shape of a matrix for a test. Also
  allows additional metadata for the test harness.
  """
    shape: Incomplete
    def __init__(self, shape, **kwargs) -> None: ...

class CheckTapeSafeSkipOptions:
    DETERMINANT: str
    DIAG_PART: str
    LOG_ABS_DETERMINANT: str
    TRACE: str

class LinearOperatorDerivedClassTest(test.TestCase, metaclass=abc.ABCMeta):
    """Tests for derived classes.

  Subclasses should implement every abstractmethod, and this will enable all
  test methods to work.
  """
    def assertAC(self, x, y, check_dtype: bool = False) -> None:
        """Derived classes can set _atol, _rtol to get different tolerance."""
    @staticmethod
    def adjoint_options(): ...
    @staticmethod
    def adjoint_arg_options(): ...
    @staticmethod
    def dtypes_to_test(): ...
    @staticmethod
    def use_placeholder_options(): ...
    @staticmethod
    def use_blockwise_arg(): ...
    @staticmethod
    def operator_shapes_infos() -> None:
        """Returns list of OperatorShapesInfo, encapsulating the shape to test."""
    @abc.abstractmethod
    def operator_and_matrix(self, shapes_info, dtype, use_placeholder, ensure_self_adjoint_and_pd: bool = False):
        """Build a batch matrix and an Operator that should have similar behavior.

    Every operator acts like a (batch) matrix.  This method returns both
    together, and is used by tests.

    Args:
      shapes_info: `OperatorShapesInfo`, encoding shape information about the
        operator.
      dtype:  Numpy dtype.  Data type of returned array/operator.
      use_placeholder:  Python bool.  If True, initialize the operator with a
        placeholder of undefined shape and correct dtype.
      ensure_self_adjoint_and_pd: If `True`,
        construct this operator to be Hermitian Positive Definite, as well
        as ensuring the hints `is_positive_definite` and `is_self_adjoint`
        are set.
        This is useful for testing methods such as `cholesky`.

    Returns:
      operator:  `LinearOperator` subclass instance.
      mat:  `Tensor` representing operator.
    """
    @abc.abstractmethod
    def make_rhs(self, operator, adjoint, with_batch: bool = True):
        """Make a rhs appropriate for calling operator.solve(rhs).

    Args:
      operator:  A `LinearOperator`
      adjoint:  Python `bool`.  If `True`, we are making a 'rhs' value for the
        adjoint operator.
      with_batch: Python `bool`. If `True`, create `rhs` with the same batch
        shape as operator, and otherwise create a matrix without any batch
        shape.

    Returns:
      A `Tensor`
    """
    @abc.abstractmethod
    def make_x(self, operator, adjoint, with_batch: bool = True):
        """Make an 'x' appropriate for calling operator.matmul(x).

    Args:
      operator:  A `LinearOperator`
      adjoint:  Python `bool`.  If `True`, we are making an 'x' value for the
        adjoint operator.
      with_batch: Python `bool`. If `True`, create `x` with the same batch shape
        as operator, and otherwise create a matrix without any batch shape.

    Returns:
      A `Tensor`
    """
    @staticmethod
    def skip_these_tests():
        """List of test names to skip."""
    @staticmethod
    def optional_tests():
        """List of optional test names to run."""
    def assertRaisesError(self, msg):
        """assertRaisesRegexp or OpError, depending on context.executing_eagerly."""
    def check_convert_variables_to_tensors(self, operator) -> None:
        """Checks that internal Variables are correctly converted to Tensors."""
    def check_tape_safe(self, operator, skip_options: Incomplete | None = None) -> None:
        """Check gradients are not None w.r.t. operator.variables.

    Meant to be called from the derived class.

    This ensures grads are not w.r.t every variable in operator.variables.  If
    more fine-grained testing is needed, a custom test should be written.

    Args:
      operator: LinearOperator.  Exact checks done will depend on hints.
      skip_options: Optional list of CheckTapeSafeSkipOptions.
        Makes this test skip particular checks.
    """

def add_tests(test_cls) -> None:
    """Add tests for LinearOperator methods."""

class SquareLinearOperatorDerivedClassTest(LinearOperatorDerivedClassTest, metaclass=abc.ABCMeta):
    """Base test class appropriate for square operators.

  Sub-classes must still define all abstractmethods from
  LinearOperatorDerivedClassTest that are not defined here.
  """
    @staticmethod
    def operator_shapes_infos(): ...
    def make_rhs(self, operator, adjoint, with_batch: bool = True): ...
    def make_x(self, operator, adjoint, with_batch: bool = True): ...

class NonSquareLinearOperatorDerivedClassTest(LinearOperatorDerivedClassTest, metaclass=abc.ABCMeta):
    """Base test class appropriate for generic rectangular operators.

  Square shapes are never tested by this class, so if you want to test your
  operator with a square shape, create two test classes, the other subclassing
  SquareLinearOperatorFullMatrixTest.

  Sub-classes must still define all abstractmethods from
  LinearOperatorDerivedClassTest that are not defined here.
  """
    @staticmethod
    def skip_these_tests():
        """List of test names to skip."""
    @staticmethod
    def operator_shapes_infos(): ...
    def make_rhs(self, operator, adjoint, with_batch: bool = True) -> None: ...
    def make_x(self, operator, adjoint, with_batch: bool = True): ...

def random_positive_definite_matrix(shape, dtype, oversampling_ratio: int = 4, force_well_conditioned: bool = False):
    """[batch] positive definite Wisart matrix.

  A Wishart(N, S) matrix is the S sample covariance matrix of an N-variate
  (standard) Normal random variable.

  Args:
    shape:  `TensorShape` or Python list.  Shape of the returned matrix.
    dtype:  `TensorFlow` `dtype` or Python dtype.
    oversampling_ratio: S / N in the above.  If S < N, the matrix will be
      singular (unless `force_well_conditioned is True`).
    force_well_conditioned:  Python bool.  If `True`, add `1` to the diagonal
      of the Wishart matrix, then divide by 2, ensuring most eigenvalues are
      close to 1.

  Returns:
    `Tensor` with desired shape and dtype.
  """
def random_tril_matrix(shape, dtype, force_well_conditioned: bool = False, remove_upper: bool = True):
    """[batch] lower triangular matrix.

  Args:
    shape:  `TensorShape` or Python `list`.  Shape of the returned matrix.
    dtype:  `TensorFlow` `dtype` or Python dtype
    force_well_conditioned:  Python `bool`. If `True`, returned matrix will have
      eigenvalues with modulus in `(1, 2)`.  Otherwise, eigenvalues are unit
      normal random variables.
    remove_upper:  Python `bool`.
      If `True`, zero out the strictly upper triangle.
      If `False`, the lower triangle of returned matrix will have desired
      properties, but will not have the strictly upper triangle zero'd out.

  Returns:
    `Tensor` with desired shape and dtype.
  """
def random_normal(shape, mean: float = 0.0, stddev: float = 1.0, dtype=..., seed: Incomplete | None = None):
    """Tensor with (possibly complex) Gaussian entries.

  Samples are distributed like

  ```
  N(mean, stddev^2), if dtype is real,
  X + iY,  where X, Y ~ N(mean, stddev^2) if dtype is complex.
  ```

  Args:
    shape:  `TensorShape` or Python list.  Shape of the returned tensor.
    mean:  `Tensor` giving mean of normal to sample from.
    stddev:  `Tensor` giving stdev of normal to sample from.
    dtype:  `TensorFlow` `dtype` or numpy dtype
    seed:  Python integer seed for the RNG.

  Returns:
    `Tensor` with desired shape and dtype.
  """
def random_uniform(shape, minval: Incomplete | None = None, maxval: Incomplete | None = None, dtype=..., seed: Incomplete | None = None):
    """Tensor with (possibly complex) Uniform entries.

  Samples are distributed like

  ```
  Uniform[minval, maxval], if dtype is real,
  X + iY,  where X, Y ~ Uniform[minval, maxval], if dtype is complex.
  ```

  Args:
    shape:  `TensorShape` or Python list.  Shape of the returned tensor.
    minval:  `0-D` `Tensor` giving the minimum values.
    maxval:  `0-D` `Tensor` giving the maximum values.
    dtype:  `TensorFlow` `dtype` or Python dtype
    seed:  Python integer seed for the RNG.

  Returns:
    `Tensor` with desired shape and dtype.
  """
def random_sign_uniform(shape, minval: Incomplete | None = None, maxval: Incomplete | None = None, dtype=..., seed: Incomplete | None = None):
    '''Tensor with (possibly complex) random entries from a "sign Uniform".

  Letting `Z` be a random variable equal to `-1` and `1` with equal probability,
  Samples from this `Op` are distributed like

  ```
  Z * X, where X ~ Uniform[minval, maxval], if dtype is real,
  Z * (X + iY),  where X, Y ~ Uniform[minval, maxval], if dtype is complex.
  ```

  Args:
    shape:  `TensorShape` or Python list.  Shape of the returned tensor.
    minval:  `0-D` `Tensor` giving the minimum values.
    maxval:  `0-D` `Tensor` giving the maximum values.
    dtype:  `TensorFlow` `dtype` or Python dtype
    seed:  Python integer seed for the RNG.

  Returns:
    `Tensor` with desired shape and dtype.
  '''
def random_normal_correlated_columns(shape, mean: float = 0.0, stddev: float = 1.0, dtype=..., eps: float = 0.0001, seed: Incomplete | None = None):
    '''Batch matrix with (possibly complex) Gaussian entries and correlated cols.

  Returns random batch matrix `A` with specified element-wise `mean`, `stddev`,
  living close to an embedded hyperplane.

  Suppose `shape[-2:] = (M, N)`.

  If `M < N`, `A` is a random `M x N` [batch] matrix with iid Gaussian entries.

  If `M >= N`, then the columns of `A` will be made almost dependent as follows:

  ```
  L = random normal N x N-1 matrix, mean = 0, stddev = 1 / sqrt(N - 1)
  B = random normal M x N-1 matrix, mean = 0, stddev = stddev.

  G = (L B^H)^H, a random normal M x N matrix, living on N-1 dim hyperplane
  E = a random normal M x N matrix, mean = 0, stddev = eps
  mu = a constant M x N matrix, equal to the argument "mean"

  A = G + E + mu
  ```

  Args:
    shape:  Python list of integers.
      Shape of the returned tensor.  Must be at least length two.
    mean:  `Tensor` giving mean of normal to sample from.
    stddev:  `Tensor` giving stdev of normal to sample from.
    dtype:  `TensorFlow` `dtype` or numpy dtype
    eps:  Distance each column is perturbed from the low-dimensional subspace.
    seed:  Python integer seed for the RNG.

  Returns:
    `Tensor` with desired shape and dtype.

  Raises:
    ValueError:  If `shape` is not at least length 2.
  '''
