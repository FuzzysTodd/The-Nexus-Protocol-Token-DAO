from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.util import tf_inspect as tf_inspect

def adjoint(lin_op_a, name: Incomplete | None = None):
    """Get the adjoint associated to lin_op_a.

  Args:
    lin_op_a: The LinearOperator to take the adjoint of.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the adjoint of `lin_op_a`.

  Raises:
    NotImplementedError: If no Adjoint method is defined for the LinearOperator
      type of `lin_op_a`.
  """
def cholesky(lin_op_a, name: Incomplete | None = None):
    """Get the Cholesky factor associated to lin_op_a.

  Args:
    lin_op_a: The LinearOperator to decompose.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the lower Cholesky factor of `lin_op_a`.

  Raises:
    NotImplementedError: If no Cholesky method is defined for the LinearOperator
      type of `lin_op_a`.
  """
def matmul(lin_op_a, lin_op_b, name: Incomplete | None = None):
    """Compute lin_op_a.matmul(lin_op_b).

  Args:
    lin_op_a: The LinearOperator on the left.
    lin_op_b: The LinearOperator on the right.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the matmul between `lin_op_a` and
      `lin_op_b`.

  Raises:
    NotImplementedError: If no matmul method is defined between types of
      `lin_op_a` and `lin_op_b`.
  """
def solve(lin_op_a, lin_op_b, name: Incomplete | None = None):
    """Compute lin_op_a.solve(lin_op_b).

  Args:
    lin_op_a: The LinearOperator on the left.
    lin_op_b: The LinearOperator on the right.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the solve between `lin_op_a` and
      `lin_op_b`.

  Raises:
    NotImplementedError: If no solve method is defined between types of
      `lin_op_a` and `lin_op_b`.
  """
def inverse(lin_op_a, name: Incomplete | None = None):
    """Get the Inverse associated to lin_op_a.

  Args:
    lin_op_a: The LinearOperator to decompose.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the inverse of `lin_op_a`.

  Raises:
    NotImplementedError: If no Inverse method is defined for the LinearOperator
      type of `lin_op_a`.
  """

class RegisterAdjoint:
    """Decorator to register an Adjoint implementation function.

  Usage:

  @linear_operator_algebra.RegisterAdjoint(lin_op.LinearOperatorIdentity)
  def _adjoint_identity(lin_op_a):
    # Return the identity matrix.
  """
    def __init__(self, lin_op_cls_a) -> None:
        """Initialize the LinearOperator registrar.

    Args:
      lin_op_cls_a: the class of the LinearOperator to decompose.
    """
    def __call__(self, adjoint_fn):
        """Perform the Adjoint registration.

    Args:
      adjoint_fn: The function to use for the Adjoint.

    Returns:
      adjoint_fn

    Raises:
      TypeError: if adjoint_fn is not a callable.
      ValueError: if a Adjoint function has already been registered for
        the given argument classes.
    """

class RegisterCholesky:
    """Decorator to register a Cholesky implementation function.

  Usage:

  @linear_operator_algebra.RegisterCholesky(lin_op.LinearOperatorIdentity)
  def _cholesky_identity(lin_op_a):
    # Return the identity matrix.
  """
    def __init__(self, lin_op_cls_a) -> None:
        """Initialize the LinearOperator registrar.

    Args:
      lin_op_cls_a: the class of the LinearOperator to decompose.
    """
    def __call__(self, cholesky_fn):
        """Perform the Cholesky registration.

    Args:
      cholesky_fn: The function to use for the Cholesky.

    Returns:
      cholesky_fn

    Raises:
      TypeError: if cholesky_fn is not a callable.
      ValueError: if a Cholesky function has already been registered for
        the given argument classes.
    """

class RegisterMatmul:
    """Decorator to register a Matmul implementation function.

  Usage:

  @linear_operator_algebra.RegisterMatmul(
    lin_op.LinearOperatorIdentity,
    lin_op.LinearOperatorIdentity)
  def _matmul_identity(a, b):
    # Return the identity matrix.
  """
    def __init__(self, lin_op_cls_a, lin_op_cls_b) -> None:
        """Initialize the LinearOperator registrar.

    Args:
      lin_op_cls_a: the class of the LinearOperator to multiply.
      lin_op_cls_b: the class of the second LinearOperator to multiply.
    """
    def __call__(self, matmul_fn):
        """Perform the Matmul registration.

    Args:
      matmul_fn: The function to use for the Matmul.

    Returns:
      matmul_fn

    Raises:
      TypeError: if matmul_fn is not a callable.
      ValueError: if a Matmul function has already been registered for
        the given argument classes.
    """

class RegisterSolve:
    """Decorator to register a Solve implementation function.

  Usage:

  @linear_operator_algebra.RegisterSolve(
    lin_op.LinearOperatorIdentity,
    lin_op.LinearOperatorIdentity)
  def _solve_identity(a, b):
    # Return the identity matrix.
  """
    def __init__(self, lin_op_cls_a, lin_op_cls_b) -> None:
        """Initialize the LinearOperator registrar.

    Args:
      lin_op_cls_a: the class of the LinearOperator that is computing solve.
      lin_op_cls_b: the class of the second LinearOperator to solve.
    """
    def __call__(self, solve_fn):
        """Perform the Solve registration.

    Args:
      solve_fn: The function to use for the Solve.

    Returns:
      solve_fn

    Raises:
      TypeError: if solve_fn is not a callable.
      ValueError: if a Solve function has already been registered for
        the given argument classes.
    """

class RegisterInverse:
    """Decorator to register an Inverse implementation function.

  Usage:

  @linear_operator_algebra.RegisterInverse(lin_op.LinearOperatorIdentity)
  def _inverse_identity(lin_op_a):
    # Return the identity matrix.
  """
    def __init__(self, lin_op_cls_a) -> None:
        """Initialize the LinearOperator registrar.

    Args:
      lin_op_cls_a: the class of the LinearOperator to decompose.
    """
    def __call__(self, inverse_fn):
        """Perform the Inverse registration.

    Args:
      inverse_fn: The function to use for the Inverse.

    Returns:
      inverse_fn

    Raises:
      TypeError: if inverse_fn is not a callable.
      ValueError: if a Inverse function has already been registered for
        the given argument classes.
    """
